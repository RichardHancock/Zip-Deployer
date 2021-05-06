import logging

import zip_deployer.cli as cli
import zip_deployer.zip_deployer as zd

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(levelname)s:\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    zd.zip_deployer(cli.handle_cli())
