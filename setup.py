import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="pycryptic",
	version="1.0.1",
	author="JlXip",
	author_email="jlxip@protonmail.com",
	description="A simple wrapper for PyCrypto",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jlxip/pycryptic",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
)
