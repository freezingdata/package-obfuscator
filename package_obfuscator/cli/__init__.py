import argparse
from package_obfuscator import obfuscate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("package_location", type=str,
                        help="The path to the package to obfuscate.")
    parser.add_argument("-o", "--output",
                        type=str,
                        default=None,
                        help="The output path of where to put the obfuscated contents.")
    parser.add_argument("-f", "--force-overwrite",
                        type=bool,
                        default=None,
                        help="Enable the overwrite of the output folder if the output folder already exists.")
    parser.add_argument("-s", "--short-filename",
                        action='store_true',
                        help="Enable short names for the files.")
    parser.add_argument("-p", "--py-cache-folder-name",
                        type=str,
                        default=None,
                        help="Add a custom name for pycache files")
    args = parser.parse_args()
    obfuscate(args.package_location, output=args.output, py_cache_folder_name=args.py_cache_folder_name,
              force_output_overwrite=args.force_overwrite, short_filenames=args.short_filename)
