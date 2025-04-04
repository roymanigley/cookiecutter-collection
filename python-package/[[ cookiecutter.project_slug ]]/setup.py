from setuptools import setup

long_description = open('README.md', 'rt').read()
version = open('version.txt', 'rt').readline().strip()

setup(
    name='[[ cookiecutter.project_name ]]',
    version=version,
    description='[[ cookiecutter.description ]]',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/roymanigley/[[ cookiecutter.project_slug ]]',
    author='Roy Manigley',
    author_email='roy.manigley@gmail.com',
    license='MIT',
    packages=['src'],
    install_requires=[
        'click>=8.1.3',
        'requests == 2.31.0',
    ],
    entry_points={
        'console_scripts': [
            '[[ cookiecutter.project_slug ]] = src.main:main',
        ],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
    ],
)
