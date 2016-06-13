import sys

# Get Scrabble rack from the command line
rack = sys.argv[1]


# Turn the words in sowpods.txt file into a Python list
wordslist = []

f = open("sowpods.txt", "r")
for line in f:
    line = line.strip()
    wordslist.append(list)

f.close()

# Find all of the valid sowpods words that can be made
# up of the letters in the rack.
for word in wordslist:
    candidate = True
    rack_letters = list(rack)
    for letter in word:
        if letter not in rack_letters:
            candidate = False
        else:
            rack_letters.remove(letter)
    if candidate == True:
        print(word)
