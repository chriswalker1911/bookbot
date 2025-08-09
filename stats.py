#define a function that counts the number of words in a text
#This function will be used in main.py to count the words in a book text
def count_words(text):
    words = text.split()
    return len(words)

#define a function that counts the number of characters in a text
#and returns a dictionary with the characters as the key and the count as the value
def count_characters(text):
    character_count = {}
    
    words = text.lower()
    letters = list(words)
    for letter in letters:
        if letter not in character_count: 
            character_count[letter] = 1
        else: 
            character_count[letter] +=1
            #I'm trying to count of each character in the text
            #try not to use ai to complete this task
    return character_count

#defin a function that organizes the character count based 
#based on the number of occurrences
def sort_character_count(character_count):
    #create a list to hold the sorted characters
    #this will be used to sort the characters by the number of occurrences
    #and return a list of dictionaries with the character and the count
    sorted_list = []
    #sort the character count dictionary by the number of occurrences
    for letter in character_count:
        sorted_characters = {}
        sorted_characters["char"] = letter
        sorted_characters["num"] = character_count[letter]
        sorted_list.append(sorted_characters)

    sorted_list.sort(reverse=True, key=lambda x:x["num"])
    return sorted_list
  


        