from logzero import logger  # noqa
import pytest  # noqa
from utils import CONFIG


def test_01_assert_config():
    logger.warning("Success!")
    assert CONFIG['LOG_LEVEL'] == 10
