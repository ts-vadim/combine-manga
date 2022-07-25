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


def get_filetype(filename: str) -> str:
	return '' if not '.' in filename else filename[filename.rindex('.')+1:]


def is_pdf(filename: str) -> bool:
	return get_filetype(filename) == 'pdf'


def get_page_order(filename: str) -> int:
	numeric = ''.join(list(filter(lambda c: c.isnumeric(), filename[:filename.rindex('.')])))
	return int(numeric)


def get_volume_order(dirname: str) -> int:
	numeric = ''.join(list(filter(lambda c: c.isnumeric(), dirname)))
	return int(numeric)


def main(root: str):
	subfolders = [os.path.join(root, f) for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))]
	subfolders.sort(key=get_volume_order)

	for subfolder in subfolders:
		tmp_merger = PdfFileMerger()
		
		subfolder_pdfs = [f for f in os.listdir(os.path.join(root, subfolder)) if is_pdf(f)]
		subfolder_pdfs.sort(key=get_page_order)
		
		for pdf in subfolder_pdfs:
			tmp_merger.append(os.path.abspath(os.path.join(root, subfolder, pdf)))
			#print(f"Added '{pdf}'")

		with open(os.path.join(root, subfolder) + '.pdf', 'wb') as volume_pdf:
			tmp_merger.write(volume_pdf)
			tmp_merger.close()

		from_pdf = subfolder_pdfs[0][:subfolder_pdfs[0].rindex('.')]
		to_pdf = subfolder_pdfs[-1][:subfolder_pdfs[-1].rindex('.')]
		print(f"Combined '{os.path.basename(subfolder)}' ({from_pdf}-{to_pdf})")

	merger = PdfFileMerger()

	for subfolder in subfolders:
		merger.append(os.path.abspath(os.path.join(root, subfolder + '.pdf')))
		print(f"Added volume '{os.path.basename(subfolder)}'")

	final_pdf_path = os.path.abspath(root) + '.pdf'
	with open(final_pdf_path, 'wb') as final_pdf:
		merger.write(final_pdf)
		merger.close()

	print(f"Final PDF: '{os.path.basename(final_pdf_path)}'")


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser(description="Combines manga pages into one PDF")
	arg_parser.add_argument(
		'FOLDER',
		help=f"Specify folder containing manga volumes"
	)
	args = arg_parser.parse_args()

	main(os.path.abspath(args.FOLDER))

