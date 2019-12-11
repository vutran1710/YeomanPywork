from logzero import logger  # noqa
import pytest  # noqa


def test_01_assert_config():
    from utils import load_config
    config = load_config()
    logger.warning("Success!")
    assert config['LOG_LEVEL'] == 10
