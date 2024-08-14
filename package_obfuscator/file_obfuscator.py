import os
import sys
import py_compile
import uuid


code_template = """
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '{}', '{}'), 'rb')
s.seek({})
exec(marshal.load(s))
"""


def _get_header_size():
    if sys.version_info >= (3, 7):
        # See: https://peps.python.org/pep-0552/
        return 16
    if sys.version_info >= (3, 2):
        # See: https://www.python.org/dev/peps/pep-3147/
        return 12
    return 8


def _random_suffix():
    return str(uuid.uuid4()).replace('-', '')


def obfuscate_file(path_to_python, *args, **kwargs):
    base_path = os.path.dirname(path_to_python)
    filename = os.path.basename(path_to_python)
    filename_clean = filename.replace('.py', '')
    suffix = f"_{_random_suffix()}" if not kwargs.get("short_filenames", False) else ""
    interim_python_file_name = f'{filename_clean}{suffix}_.py'
    os.rename(path_to_python, os.path.join(base_path,
              interim_python_file_name))
    renamed_file = os.path.join(
        base_path, interim_python_file_name)

    file_suffix = kwargs["file_suffix"] if "file_suffix" in kwargs else ".cpython-xxx.pyc"
    py_cache_folder_name = kwargs.get("py_cache_folder_name", None) or '__custom_pycache__'
    # Compile renamed_file.py
    new_filename_pyc = interim_python_file_name.replace(
        '_.py', file_suffix)
    output_pyc_filepath = os.path.join(
        base_path, py_cache_folder_name, new_filename_pyc)
    py_compile.compile(
        renamed_file, cfile=output_pyc_filepath)

    # Writing binary parse code to original file
    new_code = code_template.format(py_cache_folder_name, new_filename_pyc, _get_header_size())
    with open(path_to_python, 'w') as f:
        f.write(new_code)
    os.remove(renamed_file)
