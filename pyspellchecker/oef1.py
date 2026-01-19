from spellchecker import SpellChecker

spell = SpellChecker()

while(True):
    # find those words that may be misspelled
    print("geef woord(en) voor spellcheck")
    user = input()

    misspelled = spell.unknown(user.split())

    for word in misspelled:
        # Get the one `most likely` answer
        print(spell.correction(word))
