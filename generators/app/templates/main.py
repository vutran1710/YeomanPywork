from logzero import logger
from utils import load_config

CONFIG = load_config()


def main():
    logger.info('Hello World! This is project: <%= project %>')
    logger.warning('- To run app from `main.py`, use `pipenv run app`')
    logger.debug('- To test the app, use `pipenv run test`')
    logger.error(
        "- Submit your issues to `https://github.com/vutran1710/Pywork/issues` if needed"
    )


if __name__ == '__main__':
    main()
