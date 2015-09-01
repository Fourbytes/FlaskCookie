from invoke import task, run

@task
def test():
    run('pip install -r requirements.txt', echo=True)
    run('npm install', echo=True)
    run('npm install -g gulp', echo=True)
    run('gulp test', echo=True)
    run('python -m unittest tests', echo=True)