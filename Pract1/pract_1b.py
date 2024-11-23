#import python lib natural language toolkit
import nltk

nltk.download('brown')

from nltk.corpus import brown

# List all fileids in the Brown corpus
print("File IDs in Brown Corpus:", brown.fileids())


# List all categories in the Brown corpus
print("Categories in Brown Corpus:", brown.categories())


# Get the raw content of specific files
print("\nRaw content of 'ca01':", brown.raw('ca01')[:500])  # Read first 500 characters of 'ca01'
print("Raw content from multiple files (ca01, cp01):", brown.raw(fileids=['ca01', 'cp01'])[:500])


# Get words from the entire corpus
print("\nWords from 'ca01':", brown.words('ca01')[:100])  # First 100 words from 'ca01'


# Get words from multiple files
print("\nWords from 'ca01' and 'cp01':", brown.words(fileids=['ca01', 'cp01'])[:100])


# Get words from a specific category (e.g., 'news')
print("\nWords from the 'news' category:", brown.words(categories='news')[:100])


# Get sentences from the whole corpus
print("\nSentences from 'ca01':", brown.sents('ca01')[:2])  # First 2 sentences from 'ca01'


# Get sentences from multiple files
print("\nSentences from 'ca01' and 'cp01':", brown.sents(fileids=['ca01', 'cp01'])[:2])


# Get sentences from a specific category
print("\nSentences from the 'news' category:", brown.sents(categories='news')[:2])


# Get the absolute path of a file in the corpus
print("\nAbsolute path of 'ca01':", brown.abspath('ca01'))


# Get the encoding of a file in the corpus
print("\nEncoding of 'ca01':", brown.encoding('ca01'))


# Open and read the content of 'ca01'
with brown.open('ca01') as f:
    content = f.read()
print("\nFirst 500 characters of file 'ca01':", content[:500])


# Get the root directory where the Brown corpus is located
print("\nRoot directory of Brown corpus:", brown.root)


# Print the README for the Brown corpus
print("\nBrown README:", brown.readme())


# Get categories for a specific file
print("\nCategories of 'ca01':", brown.categories('ca01'))


# Get categories for multiple files
print("\nCategories of 'ca01' and 'cp01':", brown.categories(fileids=['ca01', 'cp01']))
