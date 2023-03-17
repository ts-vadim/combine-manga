import argparse


def create_arg_parser():
    arg_parser = argparse.ArgumentParser(
        prog='merge-pdf',
        description="Combines PDFs or comic books into a single PDF document"
    )
    arg_parser.add_argument(
        'input_folder',
        help='Folder in which to search for chapter files.'
    )
    arg_parser.add_argument(
        'output_filename', 
        help='Output filename. Supported formats ' + 
             'are "pdf", "png", "cbr", "cbz".'
    )
    arg_parser.add_argument(
        '-d',
        '--dry-run',
        dest='dry_run',
        action='store_true',
        help='Do not make actual changes.'
    )

    return arg_parser
