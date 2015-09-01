import os
import shutil

from invoke import task, run

cwd = os.path.abspath(os.path.dirname(__file__))
app_root = os.path.join(cwd, 'flaskapp')
venv_dir = os.path.join(cwd, '.venv')

@task
def build():
    run('cookiecutter {0} --no-input'.format(cwd))

@task
def clean():
    if os.path.exists(app_root):
        shutil.rmtree(app_root)
        print('Removed {0}'.format(app_root))

    if os.path.exists(venv_dir):
        shutil.rmtree(venv_dir)
        print('Removed {}'.format(venv_dir))

@task(pre=[clean, build])
def test(virtualenv=False):
    if virtualenv:
        run('virtualenv -p python3 {}'.format(venv_dir), echo=True)
        run('source {}'.format(os.path.join(venv_dir, 'bin/activate')), echo=True)
        run('which python', echo=True)
    os.chdir(app_root)
    run('invoke -r {} test'.format(app_root), echo=True, pty=True)
