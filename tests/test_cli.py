from pylenium.scripts import report_portal


def test_download_report_portal_compose_yaml():
    response = report_portal.download_compose_yaml_file()
    assert response.returncode == 0


def test_compose_up_report_portal():
    response = report_portal.compose_up()
    assert response.returncode == 0


def test_down_report_portal():
    response = report_portal.down()
    assert response.returncode == 0
