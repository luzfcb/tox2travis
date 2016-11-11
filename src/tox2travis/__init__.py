__version__ = "0.1.0"
import sys
from tox import hookimpl
import re

python_version_re = re.compile(r'(\/?|\\?|^)(?P<python_version>(pypy3?|python([2-3]\.\d)))($|\.)')
matrix_template = """matrix:
  include:
"""

python_template = """  - python: '{travis_python}'
    env:
    - TOX_ENV={tox_env_name}
"""

import argparse


# https://gist.github.com/natewalck/9139842

@hookimpl
def tox_addoption(parser):
    # http://stackoverflow.com/questions/8521612/argparse-optional-subparser-for-version
    # parser.argparser.add_argument("-t",
    #                               "--to-travis",
    #                               action="store_true",
    #                               default=False,
    #                               help="to travis")
    # subparsers = parser.argparser.add_subparsers(
    #     nargs=argparse.ZERO_OR_MORE,
    #     title='tox2travis plugin',
    #     description='valid subcommands',
    #     help='Specify secondary options'
    # )
    subparsers = parser.argparser.add_subparsers(title='subcommands',
                                                 description='valid subcommands',
                                                 help='additional help')

    # The first subparser 'Create'
    parser_create = subparsers.add_parser('create')
    # Store the result in which for a conditional check later
    parser_create.set_defaults(which='create')

    # Add the first arg to create (First Name)
    parser_create.add_argument(
        '--first_name',
        required=True,
        help='First Name')

    # Add the second arg to create (Last Name)
    parser_create.add_argument(
        '--last_name',
        required=True,
        help='Last Name')

    # The Second subparser 'Delete'
    parser_delete = subparsers.add_parser('delete')
    parser_delete.set_defaults(which='delete')

    parser_delete.add_argument(
        'id', help='Database ID')


# #


@hookimpl
def tox_configure(config):
    from pprint import pprint

    # if config.option.to_travis:
    #     tox_envs = []
    #     v = None
    #     for value in config.envconfigs.values():
    #         tox_envs.append({'basepython': value.basepython,
    #                          'tox_env_name': value.envname,
    #                          })
    #         v = value
    #
    #     d = {f: getattr(v, f) for f in dir(v) if not f.startswith('_')}
    #     pprint(d)
    #
    #     # pprint(tox_envs)
    #
    #     for v in tox_envs:
    #         g = 'Nada'
    #         r = python_version_re.search(v.get('basepython'))
    #         if r:
    #             g = r.group('python_version')
    #             # print(v.get('tox_env_name'), v.get('basepython'), 'regex match value', g)

    # sys.exit(0)
