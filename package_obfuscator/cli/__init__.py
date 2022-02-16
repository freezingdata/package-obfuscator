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
    args = parser.parse_args()
    obfuscate(args.package_location, output=args.output,
              force_output_overwrite=args.force_overwrite)
