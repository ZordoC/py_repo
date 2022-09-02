#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

#requirements = ''

test_requirements = 'pytest>=3'

setup(
    author="Jose Pedro Godinho Rodrigues Conceicao",
    author_email='pedrogodinhoc@gmail.com',
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
    description="Package implementing repository patterns for different types of storage, SQL, NoSQL, Storage.",
    entry_points={
        'console_scripts': [
            'pd_repo=pd_repo.cli:main',
        ],
    },
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pd_repo',
    name='pd_repo',
    packages=find_packages(include=['pd_repo', 'pd_repo.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ZordoC/pd_repo',
    version='0.1.0',
    zip_safe=False,
)
