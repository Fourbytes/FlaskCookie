#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

from invoke import task, run

HERE = os.path.abspath(os.path.dirname(__file__))
COOKIE = os.path.join(HERE, 'flaskapp')
REQUIREMENTS = os.path.join(COOKIE, 'requirements.txt')

@task
def build():
    run('cookiecutter {0} --no-input'.format(HERE))

@task
def clean():
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')

@task(pre=[clean, build])
def test():
    run('pip install -r {0}'.format(REQUIREMENTS), echo=True)
    run('npm install', echo=True)
    run('npm install -g gulp', echo=True)
    run('gulp test', echo=True)
    run('python -m unittest tests', echo=True)