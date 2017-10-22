# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup, find_packages

BASE_DIR = Path(__file__).parent

with (BASE_DIR / 'README').open() as readme:
	README = readme.read()

setup(
	name = 'portage',
	version = '2.3.12',
	url = 'https://wiki.gentoo.org/wiki/Project:Portage',
	author = 'Gentoo Portage Development Team',
	author_email = 'dev-portage@gentoo.org',
	package_dir = {'': 'pym'},
	packages = list(find_packages()),
	long_description = README,
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: System :: Installation/Setup'
	]
)
