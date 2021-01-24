import json

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word is not present in database."


word = input("Enter word: ")


print(translate(word))
