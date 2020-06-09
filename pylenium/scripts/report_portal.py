""" ReportPortal.io integration

1. Download the ReportPortal `docker-compose.yml` file as "docker-compose.report-portal.yml"
2. Setup permissions for ElasticSearch
3. Configure the `YAML` file based on OS
4. `docker-compose up`
5. Open ReportPortal and login (change password afterwards)
"""


import platform
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


def setup_elastic_search_permissions():
    """ ElasticSearch needs a data folder with read/write permissions before deploy. """
    system = platform.system()
    if system == 'Linux' or system == 'Darwin':
        cli_utils.run_process(['mkdir', '-p', 'data/elasticsearch'])
        cli_utils.run_process(['chmod', 'g+rwx', 'data/elasticsearch'])
        cli_utils.run_process(['chgrp', '1000', 'data/elasticsearch'])


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
                               'Are you sure you have Docker installed?',
                               f'\nResponse: {response}')
    return response
