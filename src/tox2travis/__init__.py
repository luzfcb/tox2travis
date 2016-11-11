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
    subparsers = parser.argparser.add_subparsers(title='subcommands',
                                                 description='valid subcommands',
                                                 help='additional help')

    # The first subparser 'Create'
    parser_toci = subparsers.add_parser('toci')
    # Store the result in which for a conditional check later
    parser_toci.set_defaults(which='toci')

    # Add the first arg to create (First Name)
    parser_toci.add_argument(
        '--travis',
        # required=False,
        default=False,
        action='store_true',
        help='Generate Travis test matrix from tox')

    # Add the second arg to create (Last Name)
    parser_toci.add_argument(
        '--gitlab',
        # required=False,
        default=False,
        action='store_true',
        help='Generate Travis test matrix from tox')


@hookimpl
def tox_configure(config):
    from pprint import pprint

    print(config.option)
    if config.option.toci:
        print('escolheu toci')
        print('gitlab?', config.option.gitlab)
        print('travis?', config.option.travis)
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
