import os
import sys
import argparse
try:
	from PyPDF2 import PdfFileMerger
except ImportError:
	print("Module 'PyPDF2' is not installed")
	print("You can install it using pip:")
	print('  pip install PyPDF2')
	quit()


def create_argparser() -> object:
	arg_parser = argparse.ArgumentParser(prog='merge-pdf', description="Combines PDFs into a single document")
	arg_parser.add_argument('FOLDER', help="Specify folder")
	# arg_parser.add_argument(
	# 	'-nr',
	# 	'--no-repeats',
	# 	dest='no_repeats',
	# 	action='store_true',
	# 	help="Don't include pages multiple pages with the same base name" +
	# 		 " (enable this only if you actually see repeated pages in final PDF)"
	# )
	arg_parser.add_argument(
		'-r',
		'--recursive',
		dest='recursive',
		action='store_true',
		help='Include subfolders of a specified directory'
	)
	return arg_parser


def get_pdfs_in(path: str) -> list:
	return [os.path.abspath(os.path.join(path, f)) for f in os.listdir(path) if is_pdf(f)]


def get_subfolders_of(path: str) -> list:
	return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def remove_repeats(pdfs: list):
	added = list()
	new_list = list()
	for pdf in pdfs:
		if os.path.basename(pdf) not in added:
			new_list.append(pdf)
			added.append(os.path.basename(pdf))
	return new_list


def get_filetype(filename: str) -> str:
	return '' if not '.' in filename else filename[filename.rindex('.')+1:]


def add_folder_to_index(path: str, index: list, readable_path=None):
	print(f"Searching in {readable_path if readable_path is not None else path}")
	index.extend(get_pdfs_in(path))


def is_pdf(filename: str) -> bool:
	return get_filetype(filename) == 'pdf'


def get_page_order(filename: str) -> int:
	name = os.path.basename(filename[:filename.rindex('.')])
	numbers_in_name = '0' + ''.join(list(filter(lambda c: c.isnumeric(), name)))
	#chars_in_name = ''.join(list(filter(lambda c: c.isalpha(), name)))
	return int(numbers_in_name)


def get_volume_order(dirname: str) -> float:
	numeric = ''.join(list(filter(lambda c: c.isnumeric() or c == '.', dirname)))
	return float(numeric)


def order_pdfs(pdf_list: list):
	try:
		pdf_list.sort(key=get_page_order)
	except Exception as e:
		print(f"Failed to order order pages\nError: {str(e)}")
