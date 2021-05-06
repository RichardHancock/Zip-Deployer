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

    parser.add_argument(
        "dest-path",
        required=True,
        help="Where the zip should be extracted to"
    )

    parser.add_argument(
        "-z",
        "--zip",
        required=True,
        help="Zip to extract"
    )

    parser.add_argument(
        "--no-clear",
        action="store_true",
        help="Do not clear the dest directory of files"
    )

    parser.add_argument(
        "--delete-zip",
        action="store_true",
        help="Delete the zip file after extraction"
    )

    args = parser.parse_args()

    if args.debug:
        logging.root.setLevel(logging.DEBUG)
    dest_path = args.dest_path
    zip_file = args.zip_file
    clear_folder = not args.no_clear
    delete_zip = args.delete_zip

    return dest_path, zip_file, clear_folder, delete_zip
