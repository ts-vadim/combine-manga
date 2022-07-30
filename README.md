Simple script for combining [ReadmangaGrabber](https://github.com/lirix360/ReadmangaGrabber)'s output.

## Requirements
- [PyPDF2](https://pypi.org/project/PyPDF2/) module

```
pip install PyPDF2
```

## Usage
```
merge-pdf [-h] [-r] FOLDER

  Combines PDFs into a single document

  positional arguments:
    FOLDER           Specify folder

  options:
    -h, --help       show this help message and exit
    -r, --recursive  Include subfolders of a specified directory
```
Run `bash install.sh` to add the script to `/usr/local/bin`


## Supposed specified folder structure
```
specified_folder/
  vol1/
    1.pdf
    2.pdf
    3.pdf
  vol2/
    4.pdf
    5.pdf
```
