import package_obfuscator
import os
import shutil
import hashlib


def _hash_file(file):
    hasher = hashlib.md5()
    if not os.path.exists(file):
        return None
    with open(file, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def test_obfuscate_folder_with_output():
    test_module_name = 'test_module'
    test_module_name_output = 'test_module_output'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(current_dir, test_module_name_output)
    if os.path.isdir(output_dir) and os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    assert not os.path.exists(output_dir)
    package_obfuscator.obfuscate(
        os.path.join(current_dir, 'test_module'),
        output=output_dir,
        force_output_overwrite=True
    )
    from . import test_module_output
    assert test_module_output.perform() == 2
    hash_0 = _hash_file(os.path.join(
        current_dir, test_module_name, 'hello_world.py'))
    hash_1 = _hash_file(os.path.join(output_dir, 'hello_world.py'))
    assert hash_0 != hash_1


def test_in_place_obfuscation():
    test_module_name = 'test_module'
    test_module_name_output = 'test_module_output'
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(current_dir, test_module_name_output)
    if os.path.isdir(output_dir) and os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    assert not os.path.exists(output_dir)
    shutil.copytree(os.path.join(current_dir, test_module_name), output_dir)
    hash_0 = _hash_file(os.path.join(output_dir, 'hello_world.py'))
    package_obfuscator.obfuscate(
        os.path.join(output_dir)
    )
    from . import test_module_output
    assert test_module_output.perform() == 2
    hash_1 = _hash_file(os.path.join(output_dir, 'hello_world.py'))
    assert hash_0 != hash_1
