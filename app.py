import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y or N: " %
                   get_close_matches(word, data.keys())[0])
        if yn in ["Y", 'y']:
            return data[get_close_matches(word, data.keys())[0]]
        elif yn in ["N", 'n']:
            return "We didn't understand your entry."
        else:
            return "Please try again."
    else:
        return "Word is not present in database. Please check again."


word = input("Enter word: ")


print(translate(word))
