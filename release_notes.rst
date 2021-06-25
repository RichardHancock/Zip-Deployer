Release Notes
=============

v0.0.0
------
- Folder structure and initial files created from Cookiecutter template.

v1.0.0
------
- First Release

v1.0.1
------
- Fixed error in docs generation
- Removed missing_ok param from zip deletion unlink function as this does not exist in Python 3.7  
  Replaced with a try catch instead

v1.1.0
------
- Will now create folder if dest_path doesn't exist
- Added basic automatic pytests to test this functionality