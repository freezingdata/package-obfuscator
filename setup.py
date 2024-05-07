import os
from distutils.core import setup
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

# Get version from the environment, default to '0.0.2' if not set
version = os.getenv("PACKAGE_VERSION", "0.0.1")

setuptools.setup(
    name="package_obfuscator",
    packages=setuptools.find_packages(),
    version=version,
    license="MIT",
    description="An obfuscator for python packages.",
    author="Henry Müssemann",
    author_email="hm@hm-dev-consulting.de",
    url="https://github.com/bubblegumsoldier/package-obfuscator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url=f"https://github.com/bubblegumsoldier/package-obfuscator/tarball/{version}",
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
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={"console_scripts": ["package-obfuscate=package_obfuscator.cli:main"]},
)
