Caesar cipher
=============
[![Build Status](https://travis-ci.com/dan480/caesars-cipher.svg?branch=master)](https://travis-ci.com/dan480/caesars-cipher)

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

    pipreqs [options] <>
    
    Options:
    -e, encoding        For encoding
    -d, decoding        For decoding

Project structure
---

File name       | Content
----------------|--------------------------------------
data/           | Directory with files with alphabets
src/            | Directory with files with functions
test/           | Directory with test files
.gitignore      | Hiding files and folders from Git version controltox
decoding.py     | Data decoding module
encoding.py     | Data encoding module
main.py         | Running the program
test_main.py    | Test
tox.ini         | Auto test configuration file

What's next
-----------
***
1. Implement passing a text file as an accepted parameter.
2. Setting the key for encoding / decoding at the request of the user.
3. Determine whether an encoded text or a text file was transmitted during the decoding operation.
4. Add support for other languages.
***
