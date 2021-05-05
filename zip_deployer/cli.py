import argparse
import logging

from argparse import RawTextHelpFormatter
from zip_deployer.version import __version__


def handle_cli():
    parser = argparse.ArgumentParser(
        description="Zip Deployer",
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug messages.",
        action="store_true"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version='zip-deployer V{version}'.format(
            version=__version__
        )
    )

    args = parser.parse_args()

    if args.debug:
        logging.root.setLevel(logging.DEBUG)

    return
