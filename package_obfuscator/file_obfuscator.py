import os
import py_compile
import uuid


code_template = """
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '{}', '{}'), 'rb')
s.seek(16)
exec(marshal.load(s))
"""

py_cache_folder_name = '__custom_pycache__'


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
