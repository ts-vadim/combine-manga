import os
from PIL import Image

from path_utils import *


def make_pdf_from_cbr(pdf_path: str) -> str:
	raise NotImplementedError()


def make_pdf_from_cbz(pdf_path: str) -> str:
	raise NotImplementedError()


SUPPORTED_FILE_FORMATS = {
	'pdf': lambda f: f,
	'cbr': make_pdf_from_cbr,
	'cbz': make_pdf_from_cbz
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



def make_pdf_from_file(filepath: str) -> str:
	global SUPPORTED_FILE_FORMATS

	filetype = get_filetype(filepath)

	if not is_supported(filepath):
		print(f"Format '{filetype}' is not supported. Supported formats are " +
			', '.join(["'{}'".format(t) for t in SUPPORTED_FILE_FORMATS.keys()])
		)
		quit()

	return SUPPORTED_FILE_FORMATS[filetype](filepath)
