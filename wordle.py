#!/usr/bin/env/ python3

"""
wordle.py
This script finds five letter matches based on known letters in known positions,
and known letters that aren't in the word.
"""

__author__ = "Theo Demetriades"
__version__ = "2022-01-26"

def findMatches(wordFile, letters, ins, nots):
    wfile = open(wordFile,'r')
    words = [word.rstrip().lower() for word in wfile]

    matches = []
    for word in words:
        match = True
        for c in ins:
            if c not in word:
                match = False
                break
        if match:
            for i in range(len(word)):
                if (letters[i]!=' ' and word[i]!=letters[i]) or (word[i] in nots):
                    match = False
                    break

        if match:
            matches.append(word)

    return matches


def main():
    wordFile = 'wordles.txt'
    letters = input('Enter known letters (put spaces in places that are unknown): ').lower()
    ins = input('Enter the other letters you know are in the word: ').lower()
    nots = input('Enter letters that are not in the word: ').lower()
    print(findMatches(wordFile, letters, ins, nots))


if __name__ == '__main__':
    main()