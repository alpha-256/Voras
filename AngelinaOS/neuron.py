import re
from collections import Counter

def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('notes.txt').read()))

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

memory = []
memoryValue = []
for word in WORDS :
    memory.append(word)

print(WORDS.keys([1]), WORDS.values())
