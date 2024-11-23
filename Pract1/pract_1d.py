#importing nltk (natural language toolkit)
import nltk 

# check the library location
nltk.__file__

# download the collection "popular" which consist of various corpus like Gutenberg, inaugural, brown, reuters and so on.
nltk.download('popular')

# download the corpus "inaugural" which is an isolate corpus
nltk.download('inaugural')



# import inaugural corpus
from nltk.corpus import inaugural 

# use api attribute fileids() to list the files of the corpus and len to find the number of files in the corpus
A_files = inaugural.fileids()
print(len(A_files))


# use api attribute fileids() to list the files of the corpus.
A_files = inaugural.fileids()
print((A_files))


#read single file
print(inaugural.raw("1793-Washington.txt"))


# print the number of characters of files specified (letters and space)
print(len(inaugural.raw(["1801-Jefferson.txt", "1793-Washington.txt"])))


# print the words present in the file
A_words = inaugural.words(fileids=["1809-Madison.txt"])
print(A_words[:100])


# show the path
inaugural.root


# show the absolute path of the particular file
abspath = inaugural.abspath(fileid="1809-Madison.txt")
print(abspath)

# encoding of the same file
encoding = inaugural.encoding("1809-Madison.txt")
print(encoding)


# open the file
open = inaugural.open("1809-Madison.txt")
print(open)


# read the file
readme = inaugural.readme()
print(readme)
