Simple script for combining [lirix360](https://github.com/lirix360)'s [Manga Grabber](https://github.com/lirix360/ReadmangaGrabber)'s output.

## Requirements
- [PyPDF2] module

```
pip install PyPDF2
```

## Usage
```
combine-manga.py [-h] FOLDER

	Combines manga pages into one PDF

	positional arguments:
	  FOLDER      Specify folder containing manga volumes

	options:
	  -h, --help  show this help message and exit
```

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
