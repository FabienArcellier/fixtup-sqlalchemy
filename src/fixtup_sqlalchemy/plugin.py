import io
import os

from fixtup.prompt.factory import lookup_prompt
from fixtup.entity.fixture import Fixture
from fixtup.entity.fixture_template import FixtureTemplate

from fixtup_sqlalchemy.logger import get_logger

logger = get_logger()


def on_new_fixture(template: FixtureTemplate):
    """
    This function is called by fixtup when a developer instantiates a new fixture with ``fixtup new``.
    It's the place to bootstrap content relative to your plugin.

    For example, the plugin can create a terraform.tf file if the developer plans to use terraform.
    """
    logger.info(f"trigger on_new_fixture with {template}")


def on_setup_data(fixture: Fixture):
    """
    This function is called by fixtup between each test to provision data
    """
    logger.info(f"trigger on_setup_data with {fixture}")


def on_starting(fixture: Fixture):
    """
    this function is called by fixtup every time it need to start a test that requires the fixture.
    """
    logger.info(f"trigger on_starting with {fixture}")


def on_stopping(fixture: Fixture):
    """
    this function is called by fixtup every time it end a test.
    """
    pass


def on_teardown_data(fixture: Fixture):
    """
    This function is called by fixtup between each test to cleanup data
    """
    pass
