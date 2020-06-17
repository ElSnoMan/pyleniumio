""" ReportPortal.io integration

1. Download the ReportPortal `docker-compose.yml` file as "docker-compose.report-portal.yml"
2. Setup permissions for ElasticSearch
3. Configure the `YAML` file based on OS
4. `docker-compose up`
5. Open ReportPortal and login (change password afterwards)
"""


from pylenium.scripts import cli_utils


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
        raise ConnectionError(f'Unable to download docker-compose file from ReportPortal repo. '
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
        raise EnvironmentError('Unable to run "docker-compose" command to create ReportPortal instance.'
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
    # 1. Stop all reportportal containers
    stop_containers_response = cli_utils.run_process([
        'docker stop $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
    ], shell=True)
    if stop_containers_response.returncode != 0:
        raise EnvironmentError('[FAILED] docker stop $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
                               '\nUnable to stop ReportPortal containers:'
                               '\n * Make sure Docker is installed and running'
                               '\n * Make sure this command is run in the same dir as docker-compose.report-portal.yml'
                               f'\nResponse: {stop_containers_response}')

    # 2. Kill (remove) all reportportal containers
    remove_containers_response = cli_utils.run_process([
        'docker rm $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
    ], shell=True)
    if remove_containers_response.returncode != 0:
        raise EnvironmentError('[FAILED] docker rm $(docker ps -a -f "name=reportportal" --format "{{.Names}}")'
                               '\nUnable to remove ReportPortal containers after stopping them.'
                               f'\nResponse: {remove_containers_response}')

    # 3. Remove the reportportal_default network. The network may not exist, but that's ok.
    remove_network_response = cli_utils.run_process([
        'docker', 'network', 'rm', 'reportportal_default'
    ])
    return remove_network_response
