Caesar cipher
=============
[![Build Status](https://travis-ci.com/dan480/caesars-cipher.svg?branch=master)](https://travis-ci.com/dan480/caesars-cipher)

Description
-----------
***
The Caesar Cipher program is designed to encode / decode text. 
The encoding and decoding uses a standard 2-character left shift. 
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
    
    <your_text>      The program supports the English 
                     and Russian alphabets.
                     The entered text must be typed in 
                     one language.
                     

Project structure
---

File name          | Content
-------------------|--------------------------------------
data/              | Directory with files with alphabets
src/               | Directory with files with functions
test/              | Directory with test files
.gitignore         | Hiding files and folders from Git
.travis.yml        | Description of Travis-ci options
select_alphabet.py | Alphabet selection module based on input data
decoding.py        | Data decoding module
encoding.py        | Data encoding module
main.py            | Running the program
test_*.py          | Tests
tox.ini            | Auto test configuration file

What's next
-----------
***
1. Implement passing a text file as an accepted parameter.
2. Setting the key for encoding / decoding at the request of the user.
3. Determine whether an encoded text or a text file was transmitted during the decoding operation.
4. Add support for other languages.
***
