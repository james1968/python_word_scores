__author__ = 'codesse'
import random
import string


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return:
        """
        # iterate over the valid_words list to calculate the scores for each work in the list
        for word in self.valid_words:
            # only process word of length 3 or greater
            if len(word) >= self.MIN_WORD_LENGTH:
                score = 0
                wordscore = {}
                for letter in word:
                    score += self.letter_values[letter]
                    wordscore = {'word': word, 'score': score}
                self.leaderboard.append(wordscore)
        # sort the leader board by highest score first
        sortedleaderboard = sorted(self.leaderboard, key=lambda k: k['score'], reverse=True)
        # return first 100 results
        ans = sortedleaderboard[0:self.MAX_LEADERBOARD_LENGTH]
        return ans


    def build_leaderboard_for_letters(self, starting_letters):
        starting_letters = string.ascii_lowercase
        print(' '.join(random.choice(starting_letters) for i in range(7))

        
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """
