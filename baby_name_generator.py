"""
Baby Name Generator

Given the number of baby names needed and the length and preferences for the baby name, the generator produces a list of names according to the preferences passed.

"""
import random

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = vowels + consonants

def get_pref(word_length):
    choice=[]
    print("Enter 'V' for vowel, 'C' for consonant, 'L' for any letter or any single lowercase letter:")
    for word_pos in range(word_length):
        c = input("At position " + str(word_pos+1) + ":")
        choice.append(c)    
    return choice

def name_generator(preferences):
    word_length = len(preferences)
    name = ''
    for position in range(word_length):
        if preferences[position] == 'V':
            name += random.choice(vowels)
        elif preferences[position] == 'C':
            name += random.choice(consonants)
        elif preferences[position] == 'L':
            name += random.choice(letters)
        else:
            name += preferences[position]
    return name

number_of_words = int(input("Enter number of baby names to be printed:"))
word_length = int(input("Enter length of required baby name:"))
preferences = get_pref(word_length)

for item in range(number_of_words):
    print(name_generator(preferences))
