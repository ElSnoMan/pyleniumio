""" ReportPortal.io integration

1. Download the ReportPortal `docker-compose.yml` file as "docker-compose.report-portal.yml"
2. Setup permissions for ElasticSearch
3. Configure the `YAML` file based on OS
4. `docker-compose up`
5. Open ReportPortal and login (change password afterwards)
"""


import platform
from pylenium.scripts import cli_utils


def __stop_containers():
    """ Stop all ReportPortal containers.

    Returns:
        `CompletedProcess`
    """
    command = 'docker stop $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
    if platform.system() == 'Windows':
        command = "FOR /f \"tokens=*\" %i IN " \
                  "('docker ps -a -f \"name=reportportal\" --format \"{{.Names}}\"') " \
                  "DO docker stop %i"

    stop_containers_response = cli_utils.run_process(command, shell=True)
    if stop_containers_response.returncode != 0:
        raise EnvironmentError(f'[FAILED] {command}'
                               '\n\nUnable to stop ReportPortal containers:'
                               '\n * Make sure Docker is installed and running'
                               '\n * Make sure this command is run in the same dir as docker-compose.report-portal.yml'
                               f'\nResponse: {stop_containers_response}')
    return stop_containers_response


def __remove_containers():
    """ Remove all ReportPortal containers that are stopped.

    Returns:
        `CompletedProcess`
    """
    command = 'docker rm $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
    if platform.system() == 'Windows':
        command = "FOR /f \"tokens=*\" %i IN " \
                  "('docker ps -a -f \"name=reportportal\" --format \"{{.Names}}\"') " \
                  "DO docker rm %i"

    remove_containers_response = cli_utils.run_process(command, shell=True)
    if remove_containers_response.returncode != 0:
        raise EnvironmentError(f'[FAILED] {command}'
                               '\n\nUnable to remove ReportPortal containers after stopping them.'
                               f'\nResponse: {remove_containers_response}')
    return remove_containers_response


def download_compose_yaml_file():
    """ Download the ReportPortal docker-compose.yml file.

    * It is recommended to run this from the Project Root because
    this places the file as "docker-compose.report-portal.yml" in the context where this command was run.

    Returns:
        `CompletedProcess` if successful.

    Raises:
        `ConnectionError` if process returns non-zero status code.
    """
    response = cli_utils.run_process([
        'curl', 'https://raw.githubusercontent.com/reportportal/reportportal/master/docker-compose.yml',
        '-o', './docker-compose.report-portal.yml'
    ])
    if response.returncode != 0:
        raise ConnectionError(f'\n\nUnable to download docker-compose file from ReportPortal repo. '
                              f'\nResponse: {response}')
    return response


def compose_up():
    """ Spin up a ReportPortal instance using docker-compose.report-portal.yml.

    Returns:
        `CompletedProcess`

    Raises:
        `EnvironmentError` if process returns non-zero status code.
    """
    response = cli_utils.run_process([
        'docker-compose', '-p', 'reportportal',    # prefix containers with 'reportportal'
        '-f', 'docker-compose.report-portal.yml',  # use our auto-generated compose.yml
        'up', '-d', '--force-recreate'             # spin up in detached, "daemon mode"
    ])
    if response.returncode != 0:
        raise EnvironmentError('\n\nUnable to run "docker-compose" command to create ReportPortal instance.'
                               '\n * Make sure Docker is installed and running'
                               '\n * Make sure this command is run in the same dir as docker-compose.report-portal.yml'
                               f'\nResponse: {response}')
    return response


def down():
    """ Tear down the ReportPortal instance.

    This does not use the docker-compose.report-portal.yml file because, depending on Docker version, you may
    or may not have a network created that is not handled by docker-compose down.

    1. Stop all reportportal containers
    2. Kill (remove) all reportportal containers
    3. Remove the reportportal_default network (depends on docker version)

    Returns:
        `CompletedProcess` for the

    Raises:
        `EnvironmentError` if process returns non-zero status code.
    """
    __stop_containers()
    __remove_containers()
    remove_network_response = cli_utils.run_process([
        'docker', 'network', 'rm', 'reportportal_default'
    ])
    return remove_network_response
