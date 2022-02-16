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




def _random_suffix():
    return str(uuid.uuid4()).replace('-', '')


def obfuscate_file(path_to_python, *args, **kwargs):
    base_path = os.path.dirname(path_to_python)
    filename = os.path.basename(path_to_python)
    filename_clean = filename.replace('.py', '')
    suffix = _random_suffix()
    interim_python_file_name = f'{filename_clean}_{suffix}.py'
    os.rename(path_to_python, os.path.join(base_path,
              interim_python_file_name))
    renamed_file = os.path.join(
        base_path, interim_python_file_name)

    file_suffix = kwargs["file_suffix"] if "file_suffix" in kwargs else ".cpython-xxx.pyc"
    py_cache_folder_name = kwargs["py_cache_folder_name"] if "py_cache_folder_name" in kwargs else '__custom_pycache__'
    # Compile renamed_file.py
    new_filename_pyc = interim_python_file_name.replace(
        '.py', file_suffix)
    output_pyc_filepath = os.path.join(
        base_path, py_cache_folder_name, new_filename_pyc)
    py_compile.compile(
        renamed_file, cfile=output_pyc_filepath)

    # Writing binary parse code to original file
    new_code = code_template.format(py_cache_folder_name, new_filename_pyc)
    with open(path_to_python, 'w') as f:
        f.write(new_code)
    os.remove(renamed_file)
