import os
import sys
import argparse

from path_utils import *
from format_utils import *

from PyPDF2 import PdfFileMerger


def add_folder_to_index(path: str, index: list, include_formats=['pdf'], readable_path=None):
	print(f"Searching in {readable_path if readable_path is not None else path}")
	index.extend(get_supported_files_in(path, include_formats))


def sort_index(index: list):
	try:
		index.sort(key=get_file_order)
	except Exception as e:
		print(f"Failed to order pages\nError: {str(e)}")


def add_files_to_merger(index: list, merger: PdfFileMerger):
	for file in index:
		merger.append(make_pdf_from_file(file))
		print(f"Added '{os.path.basename(file)}'")
	print(f"Added {len(index)} files")


def create_argparser() -> object:
	arg_parser = argparse.ArgumentParser(prog='merge-pdf', description="Combines PDFs into a single document")
	arg_parser.add_argument('FOLDER', help="Specify folder")
	arg_parser.add_argument(
		'-r',
		'--recursive',
		dest='recursive',
		action='store_true',
		help='Include subfolders of a specified directory'
	)
	arg_parser.add_argument(
		'--comics',
		dest='include_comics',
		action='store_true',
		help='Include comic book files (CBR and CBZ file types)'
	)
	return arg_parser
