#importing nltk (Natural Language Toolkit)
import nltk


# Check the library location to see where it is installed
print(nltk.__file__)


# Download the "popular" collection which includes various corpora like Gutenberg, Inaugural, Brown, Reuters, etc.
nltk.download('popular')


# Download the "reuters" corpus (an isolated corpus)
nltk.download('reuters')


# Import the Reuters corpus from NLTK
from nltk.corpus import reuters


# Use the 'fileids()' attribute to list the files in the Reuters corpus and 'len' to find the number of files
R_files = reuters.fileids()
print(f"Total number of files in the Reuters corpus: {len(R_files)}")


# List the files of the Reuters corpus
print("List of files in Reuters corpus:")
print(R_files)


# Get all the categories present in the Reuters corpus
categories = nltk.corpus.reuters.categories()
print("Categories in the Reuters corpus:")
print(categories)


# List the files in the "cotton-oil" and "veg-oil" categories
print("Files in 'cotton-oil' and 'veg-oil' categories:")
print(nltk.corpus.reuters.fileids(["cotton-oil", "veg-oil"]))


# Find out the categories of a specific file (e.g., "training/5460")
file_categories = nltk.corpus.reuters.categories("training/5460")
print("Categories for the file 'training/5460':")
print(file_categories)


# Read the content of a single file (e.g., "test/14833") in raw format
print("Raw content of the file 'test/14833':")
print(reuters.raw("test/14833"))


# Print the total number of characters (letters and spaces) in the specified files ("test/14833" and "test/14840")
file_length = len(reuters.raw(["test/14833", "test/14840"]))
print(f"Total number of characters in 'test/14833' and 'test/14840': {file_length}")


# Print the words present in the file "test/14840"
R_words = reuters.words(fileids=["test/14840"])
print("First 100 words in 'test/14840':")
print(R_words[:100])


# Show the root directory of the Reuters corpus
print("Root directory of the Reuters corpus:")
print(reuters.root)


# Get the absolute path of a specific file (e.g., "test/14833")
abspath = reuters.abspath(fileid="test/14833")
print(f"Absolute path of the file 'test/14833': {abspath}")


# Get the encoding of a specific file (e.g., "test/14840")
encoding = reuters.encoding("test/14840")
print(f"Encoding of 'test/14840': {encoding}")


# Open the file "test/14832" and display its content
open_file = reuters.open("test/14832")
print("Content of the file 'test/14832':")
print(open_file)


# Read the 'README' file of the Reuters corpus and print its content
readme = reuters.readme()
print("README content of the Reuters corpus:")
print(readme)
