#!/usr/bin/env python3
import argparse
import re
import string

from collections import Counter

class DocumentProcessor(object):
    translate_table = str.maketrans("", "", string.punctuation)

    def __init__(self, document=None):
        self.reset()
        if document is not None:
            self.process_document(document)

    def translate_string(self, string_value):
        return string_value.translate(self.translate_table).lower()

    def process_document(self, document):
        for word_match in re.finditer("([^\s-]+)", document):
            word = self.translate_string(word_match.group())
            if len(word) > 1:
                self._words[word] += 1
            for letter in word:
                self._letters[letter] += 1

    def reset(self):
        self._words = Counter()
        self._letters  = Counter()
    
    def most_common_words(self, n=5):
        return self._words.most_common(n)

    def most_common_letters(self, n=5):
        return self._letters.most_common(n)

    def __str__(self):
        return "Most common words:\n{}\nMost common letters:\n{}".format(
                "\n".join("{}. {} ({})".format(n+1, *mcw) for n, mcw in enumerate(self.most_common_words())),
                "\n".join("{}. {} ({})".format(n+1, *mcl) for n, mcl in enumerate(self.most_common_letters()))
        )

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("document_name")
    args = argument_parser.parse_args()

    document = ""
    with open(args.document_name) as f:
        document = "\n".join(f.readlines())
    d=DocumentProcessor(document)
    print(d)

if __name__ == "__main__":
    main()
