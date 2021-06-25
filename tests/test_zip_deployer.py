import collections
import os
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import pytest
from zip_deployer.zip_deployer import zip_deployer

# Test data
test_files = [
    "content.txt",
    "folder/sub_content.txt"
]

TEST_CONTENT = "Test Content"


@pytest.fixture
def create_test_zip(scope="function"):
    with TemporaryDirectory() as path:
        print("Creating Test Files")

        zip_path = os.path.join(path, "test.zip")
        with ZipFile(zip_path, mode="w") as zip:
            for file in test_files:
                zip.writestr(file, TEST_CONTENT)

        # Create a path down from the zip so the script won't delete it
        dest_path = os.path.join(path, "dest")
        os.mkdir(dest_path)

        yield collections.namedtuple("Paths", "zip dest")(zip_path, dest_path)


def compare_test_files(path):
    # Check test path exists (If this fails it's probably a test setup issue)
    assert os.path.exists(path), "Test Path: {0} doesn't exist".format(path)

    for file in test_files:
        assert os.path.isfile(os.path.join(path, file)),\
            "Test File: {0} was not found after zip extraction".format(file)


def test_zip_deployer_normal(create_test_zip):
    zip_deployer(
        create_test_zip.dest,
        create_test_zip.zip
        )

    compare_test_files(create_test_zip.dest)


def test_zip_deployer_non_existant_dir(create_test_zip):
    dest_path = os.path.join(create_test_zip.dest, "new_folder")

    zip_deployer(
        dest_path,
        create_test_zip.zip
        )

    compare_test_files(dest_path)
