Caesar cipher
=============
[![Build Status](https://travis-ci.com/dan480/caesars-cipher.svg?branch=master)](https://travis-ci.com/dan480/caesars-cipher)
[![Coverage Status](https://coveralls.io/repos/github/dan480/caesars-cipher/badge.svg)](https://coveralls.io/github/dan480/caesars-cipher)

Description
-----------
***
The Caesar Cipher program is designed to encode / decode text. 
The encoding and decoding uses a standard 3-character left shift. 
This method was used by Julius Caesar himself.
***

Usage
-----
To use the program, you must specify the name of the operation and pass a string.
***
    Usage:

    python main.py [options] <your_text>
    
    Options:
    e, encode        For encoding
    d, decode        For decoding

Project structure
---

File name       | Content
----------------|--------------------------------------
data/           | Directory with files with alphabets
src/            | Directory with files with functions
test/           | Directory with test files
.gitignore      | Hiding files and folders from Git
.travis.yml     | Description of Travis-ci options
cipher.py       | Data processing and output module
decoding.py     | Data decoding module
encoding.py     | Data encoding module
main.py         | Running the program
test_*.py       | Tests
tox.ini         | Auto test configuration file

What's next
-----------
***
1. Implement passing a text file as an accepted parameter.
2. Setting the key for encoding / decoding at the request of the user.
3. Determine whether an encoded text or a text file was transmitted during the decoding operation.
4. Add support for other languages.
***
