import os
import shutil
from .file_obfuscator import obfuscate_file, py_cache_folder_name
import logging


def obfuscate(path, *args, **kwargs):
    if os.path.isfile(path):
        obfuscate_file(path)
        return
    package_location = path
    if 'output' in kwargs:
        if not 'force_output_overwrite' in kwargs or not kwargs['force_output_overwrite']:
            if os.path.exists(kwargs['output']):
                raise Exception(
                    'Output folder exists. Please note that you can force the overwrite of the output folder.')
        if os.path.exists(kwargs['output']):
            shutil.rmtree(kwargs['output'])
        shutil.copytree(path, kwargs['output'])
        package_location = kwargs['output']
    return _obfuscate_package_in_place(package_location)


def _obfuscate_package_in_place(folder):
    blacklist = ['..', '.', '__pycache__', '__init__.py', py_cache_folder_name]
    files_and_folder = [file_or_folder for file_or_folder in os.listdir(
        folder) if file_or_folder not in blacklist]
    files = [file for file in files_and_folder if os.path.isfile(
        os.path.join(folder, file)) and file.endswith('.py')]
    sub_folders = [
        sub_folder for sub_folder in files_and_folder if os.path.isdir(os.path.join(folder, sub_folder))]
    for file in files:
        logging.debug(f'Obfuscating file: {file}')
        obfuscate_file(os.path.join(folder, file))
    for sub_folder in sub_folders:
        logging.debug(f'Obfuscating folder: {sub_folder}')
        _obfuscate_package_in_place(os.path.join(folder, sub_folder))
