import json
from difflib import get_close_matches

elements = json.load(open('wordbook.json'))

def findmeaning(word):
    
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]
    elif word.upper() in elements:
        return elements[word]
    elif len(get_close_matches(word, elements.keys())) > 0:
        closematches = (get_close_matches(word, elements.keys())[0])
        user_decision = input("Are you looking for %s instead? [Y/N]" % closematches)
        
        if user_decision == "Y":
            return elements[get_close_matches(word,elements.keys())[0]]
        elif user_decision == "N":
            return "I cant find your word, sorry"
    
    else:
        return ('This word is not found. Check the spelling and retype.')


word = input("Please type any word: ")

output = findmeaning(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

