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
dictionary = {}
    add_word("Good Morning", {"English": "Good Morning", "Mwgavull": "Terang'a", "Idoma": "Maichi","igbo":"Ụtụtụ-ọma","Hausa":"ina kwana","igala":"Olodu"})
    add_word("Good Afternoon", {"English": "Good Afternoon", "Mwgavull": "Warang'a", "Idoma": "Mainor","igbo":"Ehihie-ọma","Hausa":"ina wuni","igala":"Oroka"})
    add_word("Good Evening", {"English": "Good Evening", "Mwgavull": "Wnd kagam'a", "Idoma": "Maineh","igbo":"Mgbede-ọma","Hausa":"ina wuni","igala":"Olane"})
    add_word("Come", {"English": "Come", "Mwgavull": "nji", "Idoma": "wa","igbo":"Bịa","Hausa":"zo","igala":"liya"})
    add_word("Go", {"English": "Go", "Mwgavull": "sor", "Idoma": "nyo","igbo":"Gaa","Hausa":"tafi","igala":"lo"})
    add_word("Chair", {"English": "Chair", "Mwgavull": "nge tong", "Idoma": "Ochi","igbo":"Oche","Hausa":"kujera","igala":"Akpete"})
    add_word("Car", {"English": "Car", "Mwgavull": "ngum","Idoma": "Elo Quinya","igbo":"Ụgbọ-ala","Hausa":"mota","igala":"Ewunle"})
    add_word("Table", {"English": "Table", "Mwgavull": "Teebul", "Idoma": "Table","igbo":"Tebụl","Hausa":"tebur","igala":"Ewunjewu"})
    add_word("House", {"English": "House", "Mwgavull": "lu", "Idoma": "Oleh","igbo":"Ụlọ","Hausa":"gida","igala":"Unji"})
    add_word("Clock", {"English": "Clock", "Mwgavull": "nbi na pus", "Idoma": "Eko","igbo":"Ọkụ́gbọ́ta or Elekere","Hausa":"agogo","igala":"Ago"})
    add_word("Sky", {"English": "Sky", "Mwgavull": "zar",  "Idoma": "nyirowo","igbo":"Igwé","Hausa":"sama","igala":"Ojale"})
    add_word("Blood", {"English": "Blood", "Mwgavull": "tognom", "Idoma": "oyi","igbo":"Barbara","Hausa":"jini","igala":"Ebie"})
    add_word("Brave", {"English": "Brave", "Mwgavull": "kogorung", "Idoma": "Otu","igbo":" Dike","Hausa":"jarunta","igala":"Ojinoji"})
    add_word("Happy", {"English": "Happy", "Mwgavull": "redyid", "Idoma": "Eyiye","igbo":"Anụrị","Hausa":"farin ciki","igala":"Edebo"})
    add_word("Sad", {"English": "Sad", "Mwgavull": "putugub wan", "Idoma": "Sad","igbo":" Ihe-mgbu or Ụjọ","Hausa":"bakin ciki","igala":"Edekpabie"})
    add_word("Water", {"English": "Water", "Mwgavull": "A'm", "Idoma": "Enyi","igbo":"Mmiri","Hausa":"ruwa","igala":"Omi"})
    add_word("Cloth", {"English": "Cloth", "Mwgavull": "le", "Idoma": "Iri","igbo":"Akwa","Hausa":"kaya","igala":"ukpo"})
    add_word("Food", {"English": "Food", "Mwgavull": "nbise", "Idoma": "Ogire","igbo":"Nri","Hausa":"abinici","igala":"Ujewun"})
    add_word("Door", {"English": "Door", "Mwgavull": "gwan", "Idoma": "Oweh","igbo":"Ụzọ","Hausa":"kofa","igala":"ona"})
    add_word("Bag", {"English": "Bag", "Mwgavull": "dam", "Idoma": "Ekpa","igbo":"Akpa","Hausa":"jaka","igala":"Ekpa"})

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
