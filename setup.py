#!/usr/bin/env python
from pathlib import Path
import json
from setuptools import setup, find_packages

# meta:
meta_file_name = 'src/sqlalchemy_toolkit/meta.json'
meta_path = Path(__file__).resolve().parent.joinpath(meta_file_name)


try:
    with open(meta_path) as file:
        meta = json.load(file)
    del file
except FileNotFoundError:
    meta = dict()


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = ['pytest>=3', ]

setup(
    author="Yi.Q",
    author_email='yitistica@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + '',
    include_package_data=True,
    keywords='sqlalchemy_toolkit',
    name='sqlalchemy_toolkit',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yitistica/sqlalchemy_toolkit',
    version=meta.get('__version__', '0.1.0'),
    zip_safe=False,
)