#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

# var = {}
# with open('sofa/__version__.py') as fp:
#     exec(fp.read(), var)

# This test is redundant given setuptools>=24.2.0 and pip>=9.0.0.
if sys.version_info < (3, 4):
    raise Exception('This project only supports Python 3.4+.')


setup(
        name='sofa',
        # version=var['__version__'],
        # description='',
        # long_description='',
        url='https://github.com/cyliustack/sofa',
        author='TODO',
        author_email='TODO',
        license='Apache',
        packages=find_packages('.'),
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',

            'Intended Audience :: Developers',

            'License :: OSI Approved :: Apache Software License',

            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
        ],
        # keywords='space-separated strings',
        install_requires=[
            'cxxfilt',
            'networkx',
            'pandas',
        ],
        python_requires='>=3.4',
        # tests_require=[
        # ],
        package_data={
            'sofa': ['../sofaboard/*'],
        },
        entry_points={
            'console_scripts': [
                'sofa = sofa.cli:main',
            ]
        },
        # setup_requires=['pytest-runner'],
)
