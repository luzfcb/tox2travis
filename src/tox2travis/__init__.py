__version__ = "0.1.0"
import sys
from tox import hookimpl


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
        tox_envs = [{'basepython': value.basepython,
                     'tox_env_name': value.envname,
                     } for value in config.envconfigs.values()]

        pprint(tox_envs)

        sys.exit(0)
