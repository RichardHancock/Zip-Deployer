import logging
import os
from pathlib import Path
import shutil
from zipfile import ZipFile, BadZipFile

LOGGER = logging.getLogger(__name__)


def clear_folder_contents(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            LOGGER.error('Failed to delete %s. Reason: %s' % (file_path, e))


def extract_zip(zip_file, dest_path):
    with ZipFile(zip_file, mode='r') as zip:
        zip.extractall(dest_path)


def zip_deployer(dest_path, zip_file, clear_folder = False, delete_zip = False):
    LOGGER.debug("Debug flag is on! Outputting debug information.")

    if not os.path.isdir(dest_path):
        try:
            os.makedirs(dest_path, exist_ok=True)
        except Exception as e:
            LOGGER.error("""dest_path is not a valid path or could not be
            created""", dest_path, e)

    if not os.path.isfile(zip_file):
        LOGGER.error(
            "Passed in zip_file is not a valid path to a file",
            zip_file
        )
        return

    if clear_folder:
        LOGGER.info("Clearing Dest Folder")
        clear_folder_contents(dest_path)

    try:
        extract_zip(zip_file, dest_path)
    except BadZipFile as e:
        LOGGER.error(
            "zip_file could not be opened, make sure its a .zip file "
            "and unencrypted: ",
            e
        )
        return

    if delete_zip:
        LOGGER.info("Deleting Zip File")
        try:
            p = Path(zip_file)
            p.unlink()
        except FileNotFoundError as e:
            LOGGER.error(
                "Could not find zip_file to delete, Shouldn't ever happen",
                e
            )
