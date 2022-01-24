from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_obfuscator",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license="MIT",
    description="An obfuscator for python packages.",
    author="Henry Müssemann",
    author_email="henry@muessemann.de",
    url="https://github.com/bubblegumsoldier/package-obfuscator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/bubblegumsoldier/package-obfuscator/tarball/master",
    keywords=["obfuscator"],
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={"console_scripts": [
        "package_obfuscate=package_obfuscator.cli:main"]},
)
