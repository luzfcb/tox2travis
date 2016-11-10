#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update encrypted matrix in Travis config file
"""

from __future__ import print_function

import re
import os
from collections import OrderedDict

import py

from tox.config import default_factors, _split_env as split_env

TRAVIS_CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '.travis.yml')

PYTHON_TRAVIS_TEMPLATE = """  - python: '{travis_python}'
    env:
    - {tox_env}
"""

TOX_PYTHON_RE = re.compile(r'((?P<python_version>^(py[2-3]\d)|([2-3]\.\d)|(pypy3?))-.*)|(?P<another>.*)')
# TRAVIS_MATRIX_RE = re.compile(r'matrix:(?P<matrix_section>(\s+.+\n)*)')
TRAVIS_MATRIX_RE = re.compile(r'^matrix:(?P<matrix_section>(\n*[ \t]+.+)*)')
TRAVIS_ENV_RE = re.compile(r'^env:(?P<env_section>(\n*[ \t]+.+)*)')

DEFAULT_PYTHON_ON_TRAVIS = 'py35'

# https://docs.travis-ci.com/user/languages/python/
tox_to_travis_versions_matrix = OrderedDict([
    ('py26', '2.6'),
    ('py27', '2.7'),
    ('py32', '3.2'),
    ('py33', '3.3'),
    ('py34', '3.4'),
    ('py35', '3.5'),
    ('py36', '3.6-dev'),
    ('py37', 'nightly'),
    ('pypy', 'pypy'),
    ('pypy3', 'pypy3')
]
)

available_tox_envs = tuple(tox_to_travis_versions_matrix.keys())


def get_declared_envs_from_tox(filepath):
    """Get the full list of envs from the tox config.
    This notably also includes envs that aren't in the envlist,
    but are declared by having their own testenv:envname section.
    The envs are expected in a particular order. First the ones
    declared in the envlist, then the other testenvs in order.
    code from:
    https://github.com/ryanhiebert/tox-travis/blob/master/src/tox_travis.py#L40-L58
    """

    config = py.iniconfig.IniConfig(filepath)

    tox_section = config.sections.get('tox', {})
    envlist = split_env(tox_section.get('envlist', []))

    # Add additional envs that are declared as sections in the config
    section_envs = [
        section[8:] for section in sorted(config.sections, key=config.lineof)
        if section.startswith('testenv:')
        ]

    return envlist + [env for env in section_envs if env not in envlist]


def load_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()


def save_file_content(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)


def load_travis_config(travisfilepath):
    return load_file_content(travisfilepath)


def save_travis_config(travisfilepath, content):
    save_file_content(travisfilepath, content)


def build_travis_matrix(toxfilepath, default_python=DEFAULT_PYTHON_ON_TRAVIS):
    tox_env_list = []

    output_iter = get_declared_envs_from_tox(toxfilepath)
    for line in output_iter:
        line = line.strip()
        re_result = TOX_PYTHON_RE.search(line)
        tox_python = re_result.group('python_version')
        if tox_python and '.' in tox_python:
            print(tox_python)
            tox_python = 'py{}'.format(tox_python.replace('.', ''))
            print(tox_python)
        travis_python = tox_to_travis_versions_matrix.get(tox_python, default_python)

        tox_env_list.append({'python': travis_python, 'env': ['TOX_ENV={}'.format(line)]})
    return tox_env_list


def update_travis_matrix(toxfilepath, travisfilepath, write=False, silent=False,
                         default_python=DEFAULT_PYTHON_ON_TRAVIS):
    tox_env_list = build_travis_matrix(toxfilepath=toxfilepath, default_python=default_python)
    file_content = load_travis_config(travisfilepath=travisfilepath)
    if TRAVIS_ENV_RE.search(file_content):
        file_content = re.sub(TRAVIS_ENV_RE, "", file_content)
    env_content = ""
    for env in tox_env_list:
        env_content += PYTHON_TRAVIS_TEMPLATE.format(travis_python=env.get('python'), tox_env=env.get('env')[0])
    matrix_section = "matrix:\n  include:\n{}".format(env_content)
    if TRAVIS_MATRIX_RE.search(file_content):
        content = re.sub(TRAVIS_MATRIX_RE, matrix_section, file_content)
    else:
        content = '{}\n{}'.format(file_content, matrix_section)
    if write:
        save_travis_config(travisfilepath, content)
    if not silent or not write:
        print(content)


def main(args):
    update_travis_matrix(write=args.write, silent=args.silent, default_python=args.default_python)


if '__main__' == __name__:
    import argparse


    class DefaultChoiceAction(argparse.Action):
        CHOICES = available_tox_envs

        def __call__(self, parser, namespace, values, option_string=None):
            if values:
                if values not in self.CHOICES:
                    message = ("invalid choice: {0!r} \nchoose one from {1}"
                               .format(values,
                                       ', '.join([repr(action)
                                                  for action in self.CHOICES])))

                    raise argparse.ArgumentError(self, message)
                setattr(namespace, self.dest, values)


    versions_available = ' '.join(available_tox_envs)
    versions_available = versions_available.replace(' ', ', ')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-w',
                        '--write',
                        action='store_true',
                        default=False,
                        help="Inline write 'matrix' section .travis.yml file")
    parser.add_argument('-s',
                        '--silent',
                        action='store_true',
                        default=False,
                        help="Silent mode. Disable all messages.")

    parser.add_argument('-p',
                        '--default-python',
                        # action='store',
                        action=DefaultChoiceAction,
                        default=DEFAULT_PYTHON_ON_TRAVIS,
                        metavar='ACTION',
                        type=str,
                        help='Default python version if (default: {}). the versions available is: {}'.format(
                            DEFAULT_PYTHON_ON_TRAVIS, versions_available))

    args = parser.parse_args()
    main(args)
