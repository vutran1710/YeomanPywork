from logzero import logger
from utils import load_config

CONFIG = load_config()


def main():
    logger.info('Hello World! This is project: <%= project %>')


if __name__ == '__main__':
    main()
