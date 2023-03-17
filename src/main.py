# import io
import os
import fitz
import humanize
from rich.progress import track
# from PIL import Image
from natsort import os_sorted

from utils import create_arg_parser


# class MyImage:
#     def __init__(self, pil_image: Image, name=None):
#         self.memory_file = io.BytesIO()
#         pil_image.save(self.memory_file, format=pil_image.format)
#         self.obj = Image.open(self.memory_file)
#         self.stream = self.obj.tobytes()
#         self.name = name if name else pil_image.filename
#         self.bytesize = len(self.stream)

#     @classmethod
#     def from_bytes(cls, stream, name=None) -> 'MyImage':
#         return cls(Image.open(io.BytesIO(stream)), name)


# def get_images_from_pdf(filepath: str):
#     pdf = fitz.open(filepath)
#     pdf_name = os.path.splitext(os.path.basename(pdf.name))[0]

#     for page in pdf:
#         blocks = page.get_text('dict')['blocks']
#         images = [b for b in blocks if b['type'] == 1]
#         for i, image in enumerate(images):
#             name = f'{pdf_name}_{page.number}_{i}_{image["ext"]}'

#             yield MyImage.from_bytes(
#                 image['image'],
#                 name=name,
#             )


# def get_images_from(filepath):
#     return get_images_from_pdf(filepath)


def main():
    args = create_arg_parser().parse_args()

    supported_formats = ['pdf']

    def get_supported_files_in(folder: str) -> [str]:
        output = []
        for e in os_sorted(os.listdir(folder)):
            e = os.path.join(folder, e)
            if os.path.isdir(e):
                output.extend(get_supported_files_in(e))
            elif os.path.splitext(e)[-1][1:] in supported_formats:
                output.append(e)
        return output

    files_to_merge = get_supported_files_in(args.input_folder)

    if not args.dry_run:
        pdf = fitz.open()
    
    total_size = 0
    status = f'Merging files...{" (dry run)" if args.dry_run else ""}'
    for file in track(files_to_merge, description=status):
        temp_pdf = fitz.open(file)

        if not args.dry_run:
            pdf.insert_pdf(temp_pdf)

        current_size = len(temp_pdf.tobytes())
        temp_pdf.close()

        total_size += current_size

        current_human_size = humanize.naturalsize(current_size)
        total_human_size = humanize.naturalsize(total_size)

        print(
            f'+ {temp_pdf.name} ({current_human_size}) ' + 
            f'{total_human_size} in total'
        )

    print(f'Total size: {humanize.naturalsize(total_size)}')

    if not args.dry_run:
        pdf.save(args.output_filename)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')


# for image in get_images_from(file):
#     page = pdf.new_page(
#         width=image.obj.width,
#         height=image.obj.height
#     )
#     page.insert_image(
#         fitz.Rect(0, 0, image.obj.width, image.obj.height), 
#         stream=image.memory_file
#     )
#     print(f'+ {image.name} ({image.obj.format})')

# for page in temp_pdf:
#    blocks = page.get_text('dict')['blocks']
#    images = [b for b in blocks if b['type'] == 1]
#    for i, image in enumerate(images):
#        bytesize = image["size"]
#        ext = image["ext"]
#        w = image["width"]
#        h = image["height"]

#        page = pdf.new_page(width=w, height=h)
#        page.insert_image(
#            fitz.Rect(0, 0, w, h),
#            stream=image['image']
#        )

#        filename = os.path.splitext(os.path.basename(file))[0]
#        name = f'{filename}_{page.number}_{i}'
#        human_size = humanize.naturalsize(bytesize)
#        ts = humanize.naturalsize(total_size)
#        print(f'+ {name} ({ext}, {human_size}) {ts} in total')

#        total_size += bytesize
