from invoke import task, run


@task
def setup():
    run('pip install -r requirements.txt', echo=True)
    run('npm install -g gulp', echo=True)
    run('npm install', echo=True)
    run('gulp bower sass jsx', echo=True)


@task
def update():
    run('pip install -r requirements.txt --upgrade')
    run('npm update')
    run('gulp bower')
    run('gulp bower sass jsx', echo=True)


@task(pre=[setup])
def test():
    run('python -m unittest tests', echo=True)
