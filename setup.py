import re
import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

README = (here / 'README.md').read_text(encoding='utf-8')
VERSION = (here / 'VERSION').read_text()

setup(
    name='core_utils',
    version=VERSION,
    description='',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Alex Nasukovich',
    author_email='chemiron34@gmail.com',
    url="https://authmachine.com",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='~=3.5',
    install_requires=[
        "django==2.2.2",
        "entitlements @ git+https://github.com/open-cx-platforms/entitlements",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ]
)
