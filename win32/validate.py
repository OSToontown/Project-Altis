############################################
#
# validate.py
#
# Created by Hunter Ray "Judge2020"
# Created at 8/21/2017 7:30 PM EST
#
# This file itself is licensed under the MIT license
# For full license details, see https://choosealicense.com/licenses/mit/
#
# This license should NOT apply to any other files, even if the files interact with this file OR this file interacts with them.
#
#
# Premise:
#
# Extremely simple script that verifies the syntax of python files without checking PEP, usages, code style, etc.
#
# Created for Continuous integration scripts like travis CI, if the environment required to test python modules is too complex.
#
#
# Usage:
#
# 1. Change your working directory to the root of where you want to validate
# 2. python validate.py
#
# If a file has invalid syntax, it will print to stdout the path to the file.
# It will also exit with code 1, making it easy for CI to tell if validation failed.
#
############################################

import ast
import sys
import os, fnmatch


def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename


for fname in find_files('.', '*.py'):
	with open(fname) as f:
		contents = f.read()
		try:
			ast.parse(contents)
		except:
			print 'Failed at ' + fname
			sys.exit(1)

print 'Success!'
sys.exit(0)
