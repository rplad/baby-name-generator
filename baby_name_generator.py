"""
Baby Name Generator

Given the number of baby names needed and the length and preferences for the baby name, the generator produces a list of names according to the preferences passed.

"""
import random

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = vowels + consonants
letters_dict = {"V" : vowels, "C" : consonants, "L" : letters}

def get_pref(name_length):
    choice=[]
    print("Enter 'V' for vowel, 'C' for consonant, 'L' for any letter or any single lowercase letter:")
    for word_pos in range(name_length):
        c = input("At position " + str(word_pos+1) + ":")
        choice.append(c)    
    return choice

def name_generator(preferences):
    name = ''
    for preference in preferences:
        if preference in letters_dict:
            name += random.choice(letters_dict[preference])
        else:
            name += preference
    return name

if __name__ == "__main__":
    number_of_names = int(input("Enter number of baby names to be printed:"))
    name_length = int(input("Enter length of required baby name:"))
    preferences = get_pref(name_length)
    
    for item in range(number_of_names):
        print(name_generator(preferences))
