Caesar cipher
=============


Description
-----------

***
The Caesar Cipher program is designed to encode / decode text. 
The encoding and decoding uses a standard 3-character left shift. 
This method was used by Julius Caesar himself.
***


Using
-----

***
To use the program, you must specify the name of the operation and pass a string.
***
For encoding:
***
    python main.py encoding one_word
---
***
    python main.py -e one_word
---
***
    python main.py encoding "your_text"
---
***
For decoding:
***
    python main.py decoding one_word
---
***
    python main.py -d one_word
---
***
    python main.py decoding "your_text"
---
***


File name       | Content
----------------|--------------------------------------
data/           | Directory with files with alphabets
test/           | Directory with test files
decoding.py     | Data decoding module
encoding.py     | Data encoding module
main.py         | Running the program
tox.ini         | Auto test configuration file


What's next
-----------

***
1. Implement passing a text file as an accepted parameter.
2. Setting the key for encoding / decoding at the request of the user.
3. Determine whether an encoded text or a text file was transmitted during the decoding operation.
4. Add support for other languages.
***
