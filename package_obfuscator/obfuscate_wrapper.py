import os
import shutil
import uuid
import py_compile
import logging


code_template = """
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '{}', '{}'), 'rb')
s.seek(16)  # go past first eight bytes
code_obj = marshal.load(s)

exec(code_obj)
"""

py_cache_folder_name = '__custom_pycache__'


def obfuscate(folder, *args, **kwargs):
    package_location = folder
    if 'output' in kwargs:
        if not 'force_output_overwrite' in kwargs or not kwargs['force_output_overwrite']:
            if os.path.exists(kwargs['output']):
                raise Exception(
                    'Output folder exists. Please note that you can force the overwrite of the output folder.')
        if os.path.exists(kwargs['output']):
            shutil.rmtree(kwargs['output'])
        shutil.copytree(folder, kwargs['output'])
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
        print(f'Obfuscating file: {file}')
        obfuscate_file(os.path.join(folder, file))
    for sub_folder in sub_folders:
        print(f'Obfuscating folder: {sub_folder}')
        _obfuscate_package_in_place(os.path.join(folder, sub_folder))


def _random_suffix():
    return str(uuid.uuid4()).replace('-', '')


def obfuscate_file(path_to_python):
    base_path = os.path.dirname(path_to_python)
    filename = os.path.basename(path_to_python)
    filename_clean = filename.replace('.py', '')
    suffix = _random_suffix()
    interim_python_file_name = f'{filename_clean}_{suffix}.py'
    os.rename(path_to_python, os.path.join(base_path,
              interim_python_file_name))
    renamed_file = os.path.join(
        base_path, interim_python_file_name)

    # Compile renamed_file.py
    new_filename_pyc = interim_python_file_name.replace(
        '.py', '.cpython-xxx.pyc')
    output_pyc_filepath = os.path.join(
        base_path, py_cache_folder_name, new_filename_pyc)
    py_compile.compile(
        renamed_file, cfile=output_pyc_filepath)

    # Remove facebook_original.py
    os.remove(renamed_file)

    # Writing binary parse code to facebook.py
    new_code = code_template.format(py_cache_folder_name, new_filename_pyc)
    with open(path_to_python, 'w') as f:
        f.write(new_code)
