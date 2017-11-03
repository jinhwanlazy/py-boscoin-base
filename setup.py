# coding: utf-8
import codecs

from setuptools import setup, find_packages

with codecs.open('README.md', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='boscoin-base',
    version='0.1.2',
    description='boscoin-base in python.',
    long_description=long_description,
    url='http://github.com/jinhwanlazy/py-boscoin-base/',
    license='Apache',
    author='Jinhwan Choi',
    author_email='jinhwanlazy@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'ed25519', 'crc16', 'requests', 'SSEClient', 'numpy', 'toml', 'mnemonic'
    ]
)
