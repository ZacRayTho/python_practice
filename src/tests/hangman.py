import random
words = ["hello", "building", "earth", "world", "geometry", "fridge", "apartment", "football", "tennis", "soccer", "chef"]

#choose random word from words array
chosen = words[random.randint(0, len(words) - 1)]
 
empty = []
join = ""
#fill empty array with underscores to match length of chosen word
for x in range(len(chosen)):
    empty.append("_")
print(join.join(empty))

lives = 5
while lives > 0:
    answer = input("Guess a letter? ")
    if answer in chosen:
        # print("im here")
        # get index of answer input so to replace  correct indices of empty array
        indices = [x for x, z in enumerate(chosen) if z == answer]
        # print(indices)
        for x in indices:
            empty[x] = answer
        print(empty)
        # check for underscore in in empty array, if none are left the word has been deciphered and the player wins
        if "_" not in empty:
            print("You Win!, the word was {}".format(chosen))
            break
    else: 
        lives -= 1
        print("Wrong, {} Lives Left".format(lives))

