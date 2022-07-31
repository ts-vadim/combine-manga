from common import *


def main(args: dict):
	'''200 IQ stuff goes here'''

	specified_folder = os.path.abspath(args['FOLDER'])
	final_pdf_path = specified_folder + '.pdf'
	merger = PdfFileMerger()
	index = list()

	include_formats = ['pdf']
	if args['include_comics']:
		include_formats.extend(['cbr', 'cbz'])

	add_folder_to_index(specified_folder, index, include_formats, readable_path=os.path.basename(specified_folder)+'/')

	# TODO: combine PDFs folder by folder
	if args['recursive']:
		for subfolder in get_subfolders_of(specified_folder):
			add_folder_to_index(subfolder, index, include_formats, readable_path=os.path.basename(specified_folder)+'/'+os.path.basename(subfolder)+'/')

	sort_index(index)

	add_files_to_merger(index, merger)

	if len(index) > 0:
		print(f"Saving to '{os.path.basename(final_pdf_path)}'...")
		with open(final_pdf_path, 'wb') as pdf:
			merger.write(pdf)
		print('Done.')

	merger.close()


if __name__ == '__main__':
	main(vars(create_argparser().parse_args()))


'''Old algorithm

subfolders = [os.path.join(root, f) for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))]
	subfolders.sort(key=get_volume_order)

	for subfolder in subfolders:
		tmp_merger = PdfFileMerger()
		
		subfolder_pdfs = [f for f in os.listdir(os.path.join(root, subfolder)) if is_pdf(f)]
		subfolder_pdfs.sort(key=get_page_order)
		
		pdfs_to_add = list()
		for pdf in subfolder_pdfs:
			if not (no_repeats and pdf in added_pdfs):
				tmp_merger.append(os.path.abspath(os.path.join(root, subfolder, pdf)))
				pdfs_to_add.append(pdf)
		
		added_pdfs.extend(pdfs_to_add)

		with open(os.path.join(root, subfolder) + '.pdf', 'wb') as volume_pdf:
			tmp_merger.write(volume_pdf)
			tmp_merger.close()

		from_pdf = pdfs_to_add[0][:pdfs_to_add[0].rindex('.')]
		to_pdf = pdfs_to_add[-1][:pdfs_to_add[-1].rindex('.')]
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

	for subfolder in subfolders:
		volume_filename = os.path.join(root, subfolder) + '.pdf'
		os.remove(volume_filename)
'''