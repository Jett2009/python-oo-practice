"""Word Finder: finds random words from a dictionary."""


import random
class WordFinder:
    """
    >>> wf = WordFinder("/Users/bjett/OneDrive/Desktop/USF class/python/python-oo-practice/words.txt")
       3 words read
    >>> wf.random()
       'cat'
    >>> wf.random()
       'cat'
    >>> wf.random()
      'porcupine'
    >>> wf.random()
    'dog'"""
    def __init__(self, path):
        
        dict_file = open(path)

        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    def parse(self, dict_file):
        """Convert dict_file -> list of words."""
        word_list =[]

        for word in dict_file:
            #return list of word without whitespace
            word_list.append(word.strip())
        print(word_list)

    def random(self):
        """Return random word."""

        return random.choice(self.words)
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("/bjett/OneDrive/Desktop/USF class/python/python-oo-practice/special.txt")
    3 words
    >>> swf.random()
    'Carl'
    >>> swf.random()
    'Braxton'
    >>> swf.random() 
    'Jett'
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        word_list =[]
        for word in dict_file:
            if word.strip() and not word.startswith("#"):
                word_list.append(word.strip())
        print(word_list)