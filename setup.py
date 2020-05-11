import os

from setuptools import setup

name = "pymongo-stubs"
description = "Typing stubs for pymongo package"


def find_stub_files():
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(
    name=name,
    version="0.1.0",
    description=description,
    author="Dylan Anthony",
    author_email="danthony@triaxtec.com",
    license="MIT License",
    url="https://github.com/triaxtec/pymongo-stubs",
    packages=["pymongo-stubs"],
    package_data={"pymongo-stubs": find_stub_files()},
    classifiers=["Development Status :: 3 - Alpha", "Programming Language :: Python :: 3"],
)
