import io
import os
from setuptools import find_packages, setup

# Package metadata
NAME = 'python-common'
DESCRIPTION = 'A Python library with common helper code'
URL = ''
EMAIL = 'jtstroup@gmail.com'
AUTHOR = 'Justin Stroup'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None
LICENSE = 'MIT'

# What packages are required for this module to be executed?
REQUIRED = [

]

# What packages are optional?
EXTRAS = {

}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long_description
try:
    with io.open(os.path.join(here, 'READ.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=LICENSE,
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'

    ]
)
