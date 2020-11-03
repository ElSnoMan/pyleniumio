from pylenium.scripts.setup_tools import get_install_requirements


def test_get_install_requirements_returns_list(project_root):
    result = get_install_requirements(f'{project_root}/Pipfile')
    assert isinstance(result, list) and 'selenium' in result
