from os import chdir, mkdir
from pathlib import Path
from shutil import copy


def main():
    manifest_path = 'hotel-vs-gozilla-sgf-order.txt'
    input_directory = 'sgf-unsorted'
    output_directory = 'sgf'
    current_directory = Path(__file__).parent
    chdir(current_directory)
    output_path = Path(output_directory)
    output_path.mkdir(parents = True, exist_ok = True)
    prepend_number_to_filenames(
        manifest_path, input_directory, output_directory, copy)
    

def prepend_number_to_filenames(
        manifest_path, input_directory, output_directory, on_numbered):
    sorted_filenames = Path(manifest_path).read_text().splitlines()
    
    number = 1
    for sorted_filename in sorted_filenames:
        sorted_path = Path(input_directory, sorted_filename)
        numbered_filename = f'{number:02d}_{sorted_filename}'
        numbered_path = Path(output_directory, numbered_filename)
        on_numbered(sorted_path, numbered_path)
        number += 1


if '__main__' == __name__:
    main()
