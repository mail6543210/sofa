#!/usr/bin/env python
from setuptools import setup, find_packages

# var = {}
# with open('sofa/__version__.py') as fp:
#     exec(fp.read(), var)

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
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        # keywords='space-separated strings',
        install_requires=[
            'cxxfilt',
            'networkx',
            'pandas',
        ],
        python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
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
