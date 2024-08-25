"""
Unipay
-------------

A simple and userfriendly all in one payment gateway sdk for python, includes a lot of payment gateway interfaces in a single and simple package.
"""
import re
from setuptools import setup, find_packages

def __get_version():
    with open("unipay/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)

requirements = [
    'requests>=2.25.1',
    "cashfree-pg>=4.0.0"
]


setup(
    name='Unipay',
    version=__get_version(),
    url='https://github.com/spruce87/unipay',
    license='MIT',
    description='A simplified all in one payment gateway sdk for python.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
