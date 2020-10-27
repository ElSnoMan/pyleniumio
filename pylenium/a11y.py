from typing import Any, Dict, List, Optional
from axe_selenium_python.axe import Axe
from pydantic.main import BaseModel
from pydantic import Field
from selenium.webdriver.remote.webdriver import WebDriver


class AxeRelatedNode(BaseModel):
    html: str
    target: List[str]


class AxeSubNode(BaseModel):
    data: Optional[Any]
    id: str
    impact: Optional[str]
    message: str
    related_nodes: List[AxeRelatedNode] = Field(alias='relatedNodes')


class AxeNode(BaseModel):
    all: List[AxeSubNode]
    any: List[AxeSubNode]
    html: str
    impact: Optional[str]
    none: List[AxeSubNode]
    target: List[str]


class AxeAudit(BaseModel):
    description: str
    help: str
    help_url: str = Field(alias='helpUrl')
    id: str
    impact: Optional[str]
    nodes: List
    tags: List[str]


class AxeNodeViolation(AxeNode):
    failure_summary: str = Field(alias='failureSummary')


class AxeAuditViolation(AxeAudit):
    nodes: List[AxeNodeViolation]


class AxeReport(BaseModel):
    """ The aXe Audit Report in a user-friendly object. """
    inapplicable: List[AxeAudit]
    incomplete: List[AxeAudit]
    passes: List[AxeAudit]
    violations: List[AxeAuditViolation]
    timestamp: str
    url: str


class PyleniumAxe:
    """ The Pylenium abstraction of the axe-selenium-python package. """

    def __init__(self, webdriver: WebDriver):
        self.webdriver = webdriver

    def run(self, name: Optional[str] = None, context: Optional[Dict] = None, options: Optional[Dict] = None) -> AxeReport:
        """ Run the aXe audit and return an AxeReport object with the results.

        For more info on the `context` and `options` parameters, visit the aXe official docs:
        https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun

        Args:
            name: The file path and name of the report to save as a JSON. If not provided, the file is not saved.
            context: The dictionary of page part(s), by CSS Selectors, to include or exclude in the audit.
            options: The dictionary of aXe options to include in the audit.

        Examples:
            # Save the report to export or share
            PyleniumAxe(py.webriver).run(name='a11y_report.json')

            # Use the AxeReport for a hard assertion
            report = PyleniumAxe(py.webdriver).run(name='ally_report.json')
            violation_count = len(report.violations)
            assert violation_count == 0, f'{violation_count} violation(s) found!'

        Raises:
            FileNotFoundError if the given `name` is within a directory that doesn't exist.
                * Include the file extension (e.g., axe_audit.json)
                * If the file does not exist, it will be created
                * However, if a directory does not exist, the file is not created and the above Error is raised
        """
        axe = Axe(self.webdriver)
        axe.inject()
        results = axe.run(context=context, options=options)
        if name:
            axe.write_results(results, name)
        return AxeReport(**results)
