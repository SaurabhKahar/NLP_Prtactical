#import python lib natural language toolkit
import nltk


#Check the lib location
nltk.__file__


#Download the collection 'Popular' which consist of various corpus like Gutenberg, Inaugral, Brown, Reuters and so on.
nltk.download('gutenberg')


#Import Gutenberg corpus
from nltk.corpus import gutenberg


#Use API attribute fileids() to list the files of corpus & len to find the number of files in the corpus
a=gutenberg.fileids()
print(a)
print(len(a))


#Read single file & print the no. of character of the file specified
b=gutenberg.raw('austen-emma.txt')
print(b)
print(len(b))


#Print the words present in file
c=gutenberg.words(fileids=['austen-emma.txt'])
print(c[:100])


# Get the absolute path of a specific file in the Gutenberg corpus
file_path = gutenberg.abspath('austen-emma.txt')
print("File path:", file_path)


# Get the encoding of a specific file in the Gutenberg corpus
file_encoding = gutenberg.encoding('austen-emma.txt')
print("File encoding:", file_encoding)


# Open the file stream for 'austen-emma.txt'
with gutenberg.open('austen-emma.txt') as f:
    content = f.read()  # Read the entire file content
# Print the first 500 characters of the file
print(content[:500])


# Get the root directory where the Gutenberg corpus is located
root_directory = gutenberg.root
print("Corpus root directory:", root_directory)


#Print Readme
print("Read Me File :", gutenberg.readme())
