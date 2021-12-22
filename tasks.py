"""Invoke Linting Task Automation."""

import os
from invoke import Collection
from invoke import task as invoke_task


namespace = Collection("netopsio")
namespace.configure(
    {
        "netopsio": {
            "project_name": "netopsio",
            "local": False,
            "compose_dir": os.path.join(os.path.dirname(__file__), "development/"),
            "compose_file": "docker-compose.yaml",
        }
    }
)


def task(function=None, *args, **kwargs):
    """Task decorator to override the default Invoke task decorator."""

    def task_wrapper(function=None):
        """Wrapper around invoke.task to add the task to the namespace as well."""
        if args or kwargs:
            task_func = invoke_task(*args, **kwargs)(function)
        else:
            task_func = invoke_task(function)
        namespace.add_task(task_func)
        return task_func

    if function:
        # The decorator was called with no arguments
        return task_wrapper(function)
    # The decorator was called with arguments
    return task_wrapper


def docker_compose(context, command, **kwargs):
    """Helper function for running a specific docker-compose command with all appropriate parameters and environment.
    Args:
        context (obj): Used to run specific commands
        command (str): Command string to append to the "docker-compose ..." command, such as "build", "up", etc.
        **kwargs: Passed through to the context.run() call.
    """
    compose_command = f'docker-compose --project-name {context.netopsio.project_name} --project-directory "{context.netopsio.compose_dir}"'
    compose_file_path = os.path.join(
        context.netopsio.compose_dir, context.netopsio.compose_file
    )
    compose_command += f' -f "{compose_file_path}"'
    compose_command += f" {command}"

    # If `service` was passed as a kwarg, add it to the end.
    service = kwargs.pop("service", None)
    if service is not None:
        compose_command += f" {service}"

    print(f'Running docker-compose command "{command}"')
    return context.run(compose_command, **kwargs)


# Linting Tasks


@task
def black(context):
    """Execute Python Black."""
    context.run("black --check --diff .")


@task
def pylint(context):
    """Execute Python Pylint."""
    context.run("pylint netopsio/*")


@task
def flake8(context):
    """Execute Python Flake8."""
    context.run("flake8 netopsio/* --ignore=E501")


@task
def linting(context):
    """Execute Linting Tasks."""
    black(context)
    pylint(context)
    flake8(context)


# Testing Tasks


@task
def unittest(context, container="frontend"):
    """Execute Unit Tests."""
    command = "python manage.py test"
    docker_compose(context, f"exec {container} {command}", pty=True)


@task
def tests(context):
    """Execute Linting and Testing."""
    linting(context)
    unittest(context)


# Docker Tasks


@task(help={"service": "If specified, only affect this service."})
def build(context, service=None):
    """Build NetOps.io and its dependencies."""
    print("Building NetOps.io.")
    docker_compose(context, "build", service=service)


@task(help={"service": "If specified, only affect this service."})
def start(context, service=None):
    """Start NetOps.io and its dependencies in detached mode."""
    print("Starting NetOps.io in detached mode...")
    docker_compose(context, "up --detach", service=service)


@task(help={"service": "If specified, only affect this service."})
def restart(context, service=None):
    """Gracefully restart containers."""
    print("Restarting NetOps.io.")
    docker_compose(context, "restart", service=service)


@task(help={"service": "If specified, only affect this service."})
def stop(context, service=None):
    """Stop NetOps.io and its dependencies."""
    print("Stopping NetOps.io.")
    if not service:
        docker_compose(context, "down")
    else:
        docker_compose(context, "stop", service=service)


@task
def destroy(context):
    """Destroy all containers and volumes."""
    print("Destroying NetOps.io.")
    docker_compose(context, "down --volumes")


# Django Tasks


@task(help={"container": "Name of the container to shell into"})
def cli(context, container="frontend"):
    """Launch a bash shell inside the running NetOps.io container."""
    docker_compose(context, f"exec {container} bash", pty=True)


@task(
    help={
        "user": "Name of the superuser to create. (Default: admin)",
        "container": "Name of the container to run the 'createsuperuser' command on. (Default: frontend)",
    }
)
def createsuperuser(context, user="admin", container="frontend"):
    """Create a new NetOps.io superuser account (default: "admin"), will prompt for password."""
    command = f"python manage.py createsuperuser --username {user}"
    docker_compose(context, f"exec {container} {command}", pty=True)


@task(
    help={
        "name": "Use this name for migration file(s). If unspecified, a name will be generated.",
        "container": "Name of the container to run the 'makemigrations' command on. (Default: frontend)",
    }
)
def makemigrations(context, name="", container="frontend"):
    """Perform makemigrations operation in Django."""
    command = "python manage.py makemigrations"

    if name:
        command += f" --name {name}"
    docker_compose(context, f"exec {container} {command}", pty=True)


@task(
    help={
        "container": "Name of the container to run the 'migrate' command on. (Default: frontend)"
    }
)
def migrate(context, container="frontend"):
    """Perform migrate operation in Django."""
    command = "python manage.py migrate"
    docker_compose(context, f"exec {container} {command}", pty=True)
