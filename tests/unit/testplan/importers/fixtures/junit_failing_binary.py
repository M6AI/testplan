from pathlib import Path

from testplan.report import TestReport, TestGroupReport, TestCaseReport
from . import ImporterTestFixture


fixture = ImporterTestFixture(
    Path(__file__).with_suffix(".xml"),
    TestReport(
        name="JUnit Result",
        description="JUnit Import",
        entries=[
            TestGroupReport(
                name="JUnit Result",
                category="junit",
                description="JUnit Import",
                entries=[
                    TestGroupReport(
                        name="test/binaries/FooTest",
                        category="testsuite",
                        entries=[
                            TestCaseReport(
                                name="Execution",
                                entries=[
                                    {
                                        "type": "RawAssertion",
                                        "passed": False,
                                        "content": "exited with error code 2",
                                    }
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    ),
)
