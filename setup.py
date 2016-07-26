from setuptools import setup, find_packages
from codecs import open
from os import path

from unisquid import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='unisquid',
    version=__version__,
    description='Yet another unittest extension for python.',
    long_description=long_description,
    url='https://github.com/beylsp/unisquid',
    download_url='https://github.com/beylsp/unisquid/tarball/' + __version__,
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Patrik Beyls',
    install_requires=install_requires,
    dependency_links=dependency_links,
    test_suite = "tests",
)
