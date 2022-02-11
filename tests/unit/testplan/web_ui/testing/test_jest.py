"""
Runs tests for the UI code.
"""
import os
import subprocess
from typing import Optional

import pytest

from testplan import web_ui
from pytest_test_filters import skip_on_windows

TESTPLAN_UI_DIR = os.path.abspath(
    os.path.join(os.path.dirname(web_ui.__file__), "testing")
)


def check_manager(*commands: str) -> Optional[str]:
    """
    Checks if package manager is installed and returns the first found.
    """
    for command in commands:
        with open(os.devnull, "w") as FNULL:
            try:
                subprocess.check_call(f"{command}", shell=True, stdout=FNULL)
            except subprocess.CalledProcessError:
                pass
            else:
                return command


MANAGER = check_manager('pnpm', 'npm')


def tp_ui_installed():
    """
    Checks if the Testplan UI dependencies are installed.
    """
    node_modules_dir = os.path.join(TESTPLAN_UI_DIR, "node_modules")
    return os.path.exists(node_modules_dir)


@pytest.mark.skipif(
    not (MANAGER and tp_ui_installed()),
    reason="Requires a NPM/PNPM and UI installation.",
)
def test_testplan_ui():
    """
    Runs the Jest unit tests for the UI.
    """
    env = os.environ.copy()
    env["CI"] = "true"
    subprocess.check_call(
        f"{MANAGER} test", shell=True, cwd=TESTPLAN_UI_DIR, env=env
    )


@skip_on_windows(reason="We run this on linux only")
@pytest.mark.skipif(
    not (MANAGER and tp_ui_installed()),
    reason="Requires a NPM/PNPM and UI installation.",
)
def test_eslint():
    """
    Runs eslint over the UI source code.
    """
    subprocess.check_call(f"{MANAGER} lint", shell=True, cwd=TESTPLAN_UI_DIR)
