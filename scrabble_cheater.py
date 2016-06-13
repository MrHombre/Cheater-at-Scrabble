import sys

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10}

# Get Scrabble rack from the command line
rack = sys.argv[1]

# Turn the words in sowpods.txt file into a Python list
wordlist = []

f = open("sowpods.txt", "r")
for line in f:
    line = line.strip()
    wordlist.append(line)

# Find all of the valid sowpods words that can be made
# up of the letters in the rack.
vwords = []

for word in wordlist:
    candidate = True
    rack_letters = list(rack)
    for letter in word:
        if letter not in rack_letters:
            candidate = False
            break # No need to keep checking letters.
        else:
            rack_letters.remove(letter)
    if candidate == True:
        # Get the Scrabble scores for each word.
        total = 0
        for letter in word:
            total = total + scores[letter]
        vwords.append([total, word])

# Print calid words, sorted by Score.

vwords.sort()

for entry in vwords:
    score = entry[0]
    word  = entry[1]
    print(str(score) + " " + word)
