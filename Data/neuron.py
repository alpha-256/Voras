import re
from collections import Counter

"""
i copied from line 6 to 10
"""
def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

answer = []
probability = []

def calculateProbability(probability):
    counter = 0
    while counter < len(WORDS.values()):
        probability.append(round(list(WORDS.values() )[counter] / sum(WORDS.values()), 5))
        counter += 1

def showData():
    counter = 0
    while counter < len(WORDS.values()):
        print(probability[counter], "%", "|", "OC:",list(WORDS.values())[counter], list(WORDS.keys())[counter])
        counter += 1

"""
based on the probability of each key
pick key based on "prbability" indexes
"""

calculateProbability(probability)
showData()
