import setuptools

__version__ = "0.0.0"  # Stops errors, gets overwritten by next call
exec(compile(open(
    "zip_deployer/version.py").read(),
    "zip_deployer/version.py", "exec")
)

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="zip_deployer",
    version=__version__,
    author="Richard Hancock",
    author_email="git@richardh.dev",
    description="Zip Deployer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.trixie.cloud/python-scripts/zip-deployer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
