import click
import sys


def greet(name: str) -> None:
    print(f'Hello {name}')


@click.command(
    help='[[ cookiecutter.description ]]',
    epilog='''
Error Codes:\n
\t0: Ok
\t99: Unexpected Error
''',
)
@click.argument(
    'name',
    default=None,
    required=False,
)
def main(name: str) -> None:
    if name is None:
        for line in sys.stdin:
            greet(line.strip())
    else:
        print('NAME')
        greet(name)


if __name__ == '__main__':
    main()
