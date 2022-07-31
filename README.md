Simple script for combining [ReadmangaGrabber](https://github.com/lirix360/ReadmangaGrabber)'s output and comic book volumes in `cbr` or `cbz` formats.

## Requirements
- `PyPDF2`
- `Pillow`
- `rarfile`
- `unrar` utility

```
pip install PyPDF2 pillow rarfile
sudo apt install unrar
```

## Usage
```
merge-pages [-h] [-r] FOLDER

  Combines PDFs or comic books into a single PDF document

  positional arguments:
    FOLDER           specify folder

  options:
    -h, --help       show this help message and exit
    -r, --recursive  include subfolders of a specified directory
    -c, --comics     include comic book files (CBR and CBZ file types)
```
Run `bash install.sh` to add the script to `/usr/local/bin`


## Sample output
```
user@pc:~$ merge-pages ./test --recursive
Searching in test/
Searching in test/vol2/
Searching in test/vol1/
Adding '1.pdf'
Adding '2.pdf'
Adding '3.pdf'
Adding '4.pdf'
Adding '5.pdf'
Adding '6.pdf'
Adding '6.pdf'
Adding '7.pdf'
Adding '8.pdf'
Adding '9.pdf'
Adding '10.pdf'
Adding '11.pdf'
Adding '12.pdf'
Adding '13.pdf'
Added 14 files
Saving to 'test.pdf'...
Done.

user@pc:~$ merge-pages ./spider-man --comics
Searching in spider-man/
Adding 'spider-man-1.cbr'
Adding 'spider-man-2.cbr'
Adding 'spider-man-3.cbr'
Adding 'spider-man-4.cbr'
Adding 'spider-man-5.cbr'
Added 5 files
Saving to 'spider-man.pdf'...
Done.
```