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


# https://gist.github.com/natewalck/9139842

@hookimpl
def tox_addoption(parser):
    # http://stackoverflow.com/questions/8521612/argparse-optional-subparser-for-version
    parser.argparser.add_argument("-t",
                                  "--to-travis",
                                  action="store_true",
                                  help="to travis")
    subparsers = parser.argparser.add_subparsers(
        title='tox2travis plugin',
        description='valid subcommands',
        help='Specify secondary options'
    )
    subparsers.required = False  # the fudge
    # subparsers.dest = 'command'
    tox2other_parser = subparsers.add_parser('tox2', help='secondary options')
    tox2other_parser.add_argument('-o',
                                  '--one',
                                  help='Sub-argument one',
                                  action='store_true')

    tox2other_parser.add_argument('-t',
                                  '--two',
                                  help='Sub-argument two',
                                  action='store_true')
    # add_p.add_argument("name_travi")
    # add_p.add_argument("--web_port")
    #
    #
    # upg_p = subparsers.add_parser('upgrade')
    # upg_p.add_argument("name")


@hookimpl
def tox_configure(config):
    from pprint import pprint

    if config.option.to_travis:
        tox_envs = []
        v = None
        for value in config.envconfigs.values():
            tox_envs.append({'basepython': value.basepython,
                             'tox_env_name': value.envname,
                             })
            v = value

        d = {f: getattr(v, f) for f in dir(v) if not f.startswith('_')}
        pprint(d)

        # pprint(tox_envs)

        for v in tox_envs:
            g = 'Nada'
            r = python_version_re.search(v.get('basepython'))
            if r:
                g = r.group('python_version')
                # print(v.get('tox_env_name'), v.get('basepython'), 'regex match value', g)

        sys.exit(0)
