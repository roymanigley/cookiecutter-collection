from argparse import ArgumentParser

import click
import json
import os
import shutil
import tempfile
import uuid
from cookiecutter.main import cookiecutter
from django.core.management.base import BaseCommand
from git import Repo
from git import exc


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            '-t', '--cookiecutter_template',
            type=str,
            default='git+ssh://git@github.com/roymanigley/cookiecutter-collection',
            help='the cookiecutter you want to use'
        )

    def handle(self, *args, **options) -> None:
        self.git_check()
        cookiecutter_copy, migrations_copy = self.backup()

        cookiecutter_template = options['cookiecutter_template']
        try:
            with open(cookiecutter_copy) as f:
                data = json.load(f)

            shutil.rmtree('apps/core')
            cookiecutter(
                cookiecutter_template,
                extra_context=data,
                overwrite_if_exists=True,
                no_input=True,
                output_dir='..',
                directory='[[ cookiecutter._template_dir ]]',
            )
            click.echo(click.style('''
[🍪] Don't forget to apply the migrations
python manage.py makemigrations
python manage.py migrate
            ''', fg='yellow'))
        finally:
            self.restore_backup(cookiecutter_copy, migrations_copy)

    def git_check(self) -> None:
        try:
            repo = Repo('.')
            has_uncommitted_changes = repo.is_dirty() or len(repo.untracked_files) > 0
            if has_uncommitted_changes:
                click.echo(click.style(
                    '[🍪] before running the cookiecutter you need to commit the changes',
                    fg='red'
                ))
                exit(0)
        except exc.InvalidGitRepositoryError:
            click.echo(click.style(
                '[🍪] before running the cookiecutter you need to initialize a git repo and commit the changes',
                fg='red'
            ))
            exit(0)

    def backup(self) -> tuple[str, str]:
        migrations_copy = os.path.join(
            tempfile.gettempdir(),
            f'migrations-{uuid.uuid4().hex}'
        )
        cookiecutter_copy = os.path.join(
            tempfile.gettempdir(),
            f'cookiecutter-{uuid.uuid4().hex}.json'
        )
        shutil.move('cookiecutter.json', cookiecutter_copy)
        if os.path.exists('apps/core/migrations/'):
            shutil.move('apps/core/migrations', migrations_copy)
        return cookiecutter_copy, migrations_copy

    def restore_backup(self, cookiecutter_copy: str, migrations_copy: str) -> None:
        shutil.move(cookiecutter_copy, 'cookiecutter.json')
        if os.path.exists(migrations_copy):
            shutil.rmtree('apps/core/migrations', ignore_errors=True)
            shutil.move(migrations_copy, 'apps/core/migrations')
