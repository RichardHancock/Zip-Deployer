Zip Deployer  
=============================
  
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
  
Use the command below to install and use:  

```sh
pip install --trusted-host 192.168.1.100 --extra-index-url http://192.168.1.100:14480 zip_deployer  
  
python -m zip_deployer -z zip_file.zip dest_folder/  
```
