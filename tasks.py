import os
import shutil

from invoke import task, run

cwd = os.path.abspath(os.path.dirname(__file__))
app_root = os.path.join(cwd, 'flaskapp')

@task
def build():
    run('cookiecutter {0} --no-input'.format(cwd))

@task
def clean():
    if os.path.exists(app_root):
        shutil.rmtree(app_root)
        print('Removed {0}'.format(app_root))
    else:
        print('App directory does not exist. Skipping.')

@task(pre=[clean, build])
def test():
    os.chdir(app_root)
    run('invoke -r {} test'.format(app_root), echo=True, pty=True)