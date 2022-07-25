Simple script for combining [ReadmangaGrabber](https://github.com/lirix360/ReadmangaGrabber)'s output.

## Requirements
- [PyPDF2](https://pypi.org/project/PyPDF2/) module

```
pip install PyPDF2
```

## Usage
```
combine-manga.py [-h] [--no-repeats] FOLDER

  Combines manga pages into one PDF

  positional arguments:
    FOLDER        Specify folder containing manga volumes

  options:
    -h, --help    show this help message and exit
    --no-repeats  Don't include pages that had already been added (enable this only if you actually see
                  repeated pages in final PDF)
```
Run `bash install.sh` to add the script to `/usr/local/bin` folder


## Manga folder structure
```
manga_name/ - specified folder
  vol1/
    1.pdf
    2.pdf
    3.pdf
  vol2/
    4.pdf
    5.pdf
```
