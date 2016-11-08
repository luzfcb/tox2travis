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


@hookimpl
def tox_addoption(parser):
    parser.add_argument("-t",
                        "--to-travis",
                        action="store_true",
                        help="to travis")


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
