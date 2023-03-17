Simple script for combining PDFs and CBRs into a single document.
Originally was created to merge manga chapters from [ReadmangaGrabber](https://github.com/lirix360/ReadmangaGrabber) and [HakuNeko](https://github.com/manga-download/hakuneko).

## Install
On Linux
```
chmod +x ./scripts/install.sh && ./scripts/install.sh
```

## Requirements
On Linux
```
chmod +x ./scripts/setup.sh && ./scripts/setup.sh
```
On Windows
```
python -m venv .venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```
usage: merge-pdf [-h] [-d] input_folder output_filename

Combines PDFs or comic books into a single PDF document

positional arguments:
  input_folder     Folder in which to search for chapter files.
  output_filename  Output filename. Supported formats are "pdf", "png", "cbr", "cbz".

optional arguments:
  -h, --help       show this help message and exit
  -d, --dry-run    Do not make actual changes.
```

## Sample output
```
main@hp-laptop:~/Documents/merge-pdf$ merge-pdf -d ./test/ ./test/out.pdf
+ ./test/1/1.pdf (4.1 MB) 4.1 MB in total
+ ./test/1/2.pdf (2.0 MB) 6.1 MB in total
+ ./test/2/1.pdf (2.8 MB) 8.9 MB in total
+ ./test/2/2.pdf (2.9 MB) 11.8 MB in total
Merging files... (dry run) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:06
Total size: 802.9 MB
```

## Notes
Often cache grows too big. Clear it with this command:
```
sudo sh -c 'echo 1 >  /proc/sys/vm/drop_caches'
```
