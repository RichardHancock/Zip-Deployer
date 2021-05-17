Zip Deployer  
=============================

Basic Python package to clear the destination directory and then unzip a file into the directory you specify.  
You could easily do this with bash, but I'm using this as I can quick deploy it using my local pypi instance.
  
Required Command Line inputs
-----------------------------

- **dest_path** Path to extract to  
  
- **-z, --zip** Path to zip file to extract  
  
Optional Command Line inputs
-----------------------------

- **-h, --help** The help for the command line inputs.  
  
- **-d, --debug** Enable debug messages.  
  
- **-v, --version** Show the program's version number and exit.  
  
- **--no-clear** Do not clear the dest directory of files before extraction.  
  
- **--delete-zip** Delete the zip file after extraction.  
