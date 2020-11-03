import toml


def get_install_requirements(file) -> list:
    """ Parses a pipfile and returns a list of package names along with a version if applicable """
    pipfile = toml.load(file)
    packages = pipfile.get('packages').items()
    return ["{0}{1}".format(pkg, ver) if ver != "*"
            else pkg for pkg, ver in packages]
