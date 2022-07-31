import os
import zipfile
import rarfile
import tempfile
from PIL import Image

from path_utils import *


def make_pdf_from_comicbook(archive_path: str) -> object:
	archive = None

	if get_filetype(archive_path) == 'cbr':
			archive = rarfile.RarFile(archive_path)
	elif get_filetype(archive_path) == 'cbz':
		archive = zipfile.ZipFile(archive_path)
	else:
		print(f"Failed to make PDF from '{archive_path}': Unsupported comic book format '{get_filetype(archive_path)}'")
		quit()

	image_names = [f for f in archive.namelist() if get_filetype(f).lower() in ['jpg', 'jpeg']]
	image_names.sort(key=lambda fp: get_file_order(fp))

	images = list()

	for image_name in image_names:
		try:
			with archive.open(image_name) as image_file:
				images.append(Image.open(image_file).convert('RGB'))
		except rarfile.RarCannotExec:
			print(f"'rarfile' error: can not find external tool to extract RAR file")
			print(f"This script depends on 'unrar' utility")
			quit()

	temp_file = tempfile.TemporaryFile()
	images[0].save(temp_file, format='pdf', save_all=True, append_images=images[1:])

	return temp_file


SUPPORTED_FILE_FORMATS = {
	'pdf': lambda f: open(f, 'rb'),
	'cbr': make_pdf_from_comicbook,
	'cbz': make_pdf_from_comicbook
}


def is_supported(filename: str) -> bool:
	global SUPPORTED_FILE_FORMATS
	return get_filetype(filename).lower() in SUPPORTED_FILE_FORMATS.keys()


def get_supported_files_in(path: str, formats=['pdf']) -> list:
	files = list()
	for f in os.listdir(path):
		filepath = os.path.abspath(os.path.join(path, f))
		if not os.path.isdir(filepath):
			if get_filetype(f) in formats and is_supported(f):
				files.append(filepath)
	return files


def make_pdf_from_file(filepath: str) -> object:
	global SUPPORTED_FILE_FORMATS

	filetype = get_filetype(filepath)

	if not is_supported(filepath):
		print(f"Format '{filetype}' is not supported. Supported formats are " +
			', '.join(["'{}'".format(t) for t in SUPPORTED_FILE_FORMATS.keys()])
		)
		quit()

	return SUPPORTED_FILE_FORMATS[filetype](filepath)
