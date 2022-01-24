import os
from setuptools import setup, find_packages

def read_requirements():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    requirements_txt = os.path.join(current_dir, 'requirements.txt')
    with open(requirements_txt, 'r') as f:
        return f.read().splitlines()

def get_version():
    return os.environ.get('CI_COMMIT_TAG') if os.environ.get('CI_COMMIT_TAG') else 'v0.0.1'


setup(
    name='package_obfuscator',
    version=get_version(),
    packages=find_packages(include=['package_obfuscator']),
    scripts=["package_obfuscator/scripts/package_obfuscator.py"],
    install_requires=read_requirements()
)
