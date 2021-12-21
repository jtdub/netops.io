"""Invoke Linting Task Automation."""

from invoke import task


@task
def black(context):
    """Execute Python Black."""
    context.run("black .")


@task
def pylint(context):
    """Execute Python Pylint."""
    context.run("pylint netopsio/*")


@task
def flake8(context):
    """Execute Python Flake8."""
    context.run("flake8 netopsio/* --ignore=E501")


@task
def lint(context):
    """Execute Linting Tasks."""
    context.run("invoke black")
    context.run("invoke pylint")
    context.run("invoke flake8")


@task
def unittest(context):
    """Execute Unit Tests."""
    context.run("cd netopsio; ./manage.py test")


@task
def tests(context):
    """Execute Linting and Testing."""
    context.run("invoke lint")
    context.run("invoke unittest")


@task
def server(context):
    """Start Django Server."""
    context.run("cd netopsio; ./manage.py runserver 0.0.0.0:8000 --insecure")


@task
def worker(context):
    """Start Celery Workers."""
    context.run("cd netopsio; celery -A netopsio worker -l INFO")
