from setuptools import setup, find_packages
import pylenium as app


setup(
    name="pyleniumio",
    version=app.__version__,
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/ElSnoMan/pyleniumio",
    license="MIT",
    author="Carlos Kidman",
    author_email="carlos@qap.dev",
    description="The best of Selenium and Cypress in a single Python Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "selenium>=4.1.0",
        "pytest>=6.1.0",
        "pytest-xdist>=2.4.0",
        "pytest-parallel>=0.1.1",
        "pydantic>=1.9.0",
        "pytest-reportportal>=5.1.0",
        "Faker>=8.16.0",
        "requests>=2.27.1",
        "webdriver-manager>=3.5.4",
        "click>=7.1.2, <8.0.0",
        "pyfiglet>=0.8.post1",
        "axe-selenium-python>=2.1.6",
        "selenium-wire>=4.6.3",
    ],
    data_files=[
        (
            "",
            [
                "pylenium/scripts/pylenium.json",
                "pylenium/scripts/pytest.ini",
                "pylenium/scripts/drag_and_drop.js",
                "pylenium/scripts/load_jquery.js",
            ],
        )
    ],
    entry_points="""
        [console_scripts]
        pylenium=pylenium.scripts.cli:cli
    """,
)
