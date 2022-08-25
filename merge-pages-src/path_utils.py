import os


def get_filetype(filename: str) -> str:
	return '' if not '.' in filename else filename[filename.rindex('.')+1:]


def get_file_order(filename: str) -> int:
	name = os.path.basename(filename[:filename.rindex('.')])
	numbers_in_name = '0' + ''.join(list(filter(lambda c: c.isnumeric() or c == '.', name)))
	return int(numbers_in_name)


def get_subfolders_of(path: str) -> list:
	return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
