dictionary = {}

def add_word(word, meanings):
    """Add a word and its meanings to the dictionary."""
    dictionary[word.lower()] = meanings

def get_meaning(word, language):
    """Get the meaning of a word in a specific language."""
    if word.lower() in dictionary:
        for lang, meaning in dictionary[word.lower()].items():
            if lang.lower() == language.lower():
                return meaning
        return "Meaning not available in this language."
    else:
        return "Word not found in the dictionary."

def main():
    # Add words to the dictionary
    add_word("Good Morning", {"English": "Good Morning", "Mwgavull": "Terang'a", "Idoma": "Maichi","igbo":"Ụtụtụ-ọma"})
    add_word("Good Afternoon", {"English": "Good Afternoon", "Mwgavull": "Warang'a", "Idoma": "Mainor","igbo":"Ehihie-ọma"})
    add_word("Good Evening", {"English": "Good Evening", "Mwgavull": "Wnd kagam'a", "Idoma": "Maineh","igbo":"Mgbede-ọma"})
    add_word("Come", {"English": "Come", "Mwgavull": "nji", "Idoma": "wa","igbo":"Bịa"})
    add_word("Go", {"English": "Go", "Mwgavull": "sor", "Idoma": "nyo","igbo":"Gaa" })
    add_word("Chair", {"English": "Chair", "Mwgavull": "nge tong", "Idoma": "Ochi","igbo":"Oche"})
    add_word("Car", {"English": "Car", "Mwgavull": "ngum","Idoma": "Elo Quinya","igbo":"Ụgbọ-ala"})
    add_word("Table", {"English": "Table", "Mwgavull": "Teebul", "Idoma": "Table","igbo":"Tebụl"})
    add_word("House", {"English": "House", "Mwgavull": "lu", "Idoma": "Oleh","igbo":"Ụlọ"})
    add_word("Clock", {"English": "Clock", "Mwgavull": "nbi na pus", "Idoma": "Eko","igbo":"Ọkụ́gbọ́ta or Elekere"})
    add_word("Sky", {"English": "Sky", "Mwgavull": "zar",  "Idoma": "nyirowo","igbo":"Igwé"})
    add_word("Blood", {"English": "Blood", "Mwgavull": "tognom", "Idoma": "oyi","igbo":"Barbara"})
    add_word("Brave", {"English": "Brave", "Mwgavull": "kogorung", "Idoma": "Otu","igbo":" Dike"})
    add_word("Happy", {"English": "Happy", "Mwgavull": "redyid", "Idoma": "Eyiye","igbo":"Anụrị "})
    add_word("Sad", {"English": "Sad", "Mwgavull": "putugub wan", "Idoma": "Sad","igbo":" Ihe-mgbu or Ụjọ"})
    add_word("Water", {"English": "Water", "Mwgavull": "A'm", "Idoma": "Enyi","igbo":"Mmiri "})
    add_word("Cloth", {"English": "Cloth", "Mwgavull": "le", "Idoma": "Iri","igbo":"Akwa"})
    add_word("Food", {"English": "Food", "Mwgavull": "nbise", "Idoma": "Ogire","igbo":"Nri"})
    add_word("Door", {"English": "Door", "Mwgavull": "gwan", "Idoma": "Oweh","igbo":"Ụzọ"})
    add_word("Bag", {"English": "Bag", "Mwgavull": "dam", "Idoma": "Ekpa","igbo":"Akpa"})

    # ... add more words

    while True:
        word = input("\nEnter a word in English to search for (or type 'exit' to quit): ").strip()
        if word.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        if word.lower() in dictionary:
            print("Available languages for this word:")
            for lang in dictionary[word.lower()].keys():
                print(f"- {lang}")
            language = input("Enter the language you want to know this word in: ").strip()
            meaning = get_meaning(word, language)
            print(f"The meaning of '{word}' in {language} is: {meaning}")
        else:
            print(f"'{word}' is not found in the dictionary. Try adding it!")

if __name__ == "__main__":
    main()
