from collections import Counter
from time import sleep
from sys import stdout
from data import *
import sys

available_pokemon = GEN1
question_counter = 1
running = True

def typing_print(text):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(0.05)

def get_most_common_value(dict):
    all_values = []
    for inner_dict in dict.values():
        all_values.extend(inner_dict.values())
        counter = Counter(all_values)
        return counter.most_common(1)[0][0]

def remove_pokemon(answer, key_1, key_2, test):
    if answer == 'yes' or answer == 'y':
        for key, dict in available_pokemon.items():
            if dict[key_1] != test and dict[key_2] != test:
                del available_pokemon[key]
    elif answer == 'no' or answer == 'n':
        for key, dict in available_pokemon.items():
            if dict[key_1] == test or dict[key_2] == test:
                del available_pokemon[key]
    
typing_print("Hello, welcome to the 20 questions pokemon game\n\
where I try to guess which pokemon from the first 151 you are thinking of in 20 questions or less!\n\
For answers, type yes or y for yes, and no or n for no\n\
Got a pokemon in mind? Let's go\n")

while running == True:
    while question_counter <= 20:
        typing_print(f'question {question_counter}')
        if len(available_pokemon) > 21 - question_counter:
            most_common_value = get_most_common_value(available_pokemon)
            match most_common_value:
                case 'normal' | 'fire' | 'fighting' | 'water' | 'flying' | 'grass' | 'poison' | 'electric' | 'ground' | 'pyschic' | 'rock' | 'ice' | 'bug' | 'dragon' | 'ghost' | 'dark' | 'steel' | 'fairy':
                    typing_print(f'Is your pokemon a {most_common_value} type?')
                    answer = input().lower()
                    remove_pokemon(answer, 'type 1', 'type 2', most_common_value)
                case 'animal' | 'humanoid' | 'object' | 'plant':
                    typing_print(f'Is your pokemon a(n) {most_common_value}?')
                    answer = input().lower()
                    remove_pokemon(answer, 'base form', 'base form', most_common_value)
                case '0 a' | '2 a' | '4 a':
                    value = most_common_value.split(' ')
                    typing_print(f'Does your pokemon have {value} arms')
                    answer = input().lower()
                    remove_pokemon(answer, 'arms', 'arms', most_common_value)
                case '0 l' | '2 l' | '4 l' | '14 l':
                    value = most_common_value.split(' ')
                    typing_print(f'Does your pokemon have {value} legs')
                    answer = input().lower()
                    remove_pokemon(answer, 'legs', 'legs', most_common_value)
                case 'no w' | 'yes w':
                    typing_print(f'Does your pokemon have wings')
                    answer = input().lower()
                    remove_pokemon(answer, 'wings', 'wings', 'yes w')
                case '1' | 'multiple':
                    typing_print(f'Does your pokemon have multiple heads')
                    answer = input().lower()
                    remove_pokemon(answer, 'heads', 'heads', 'multiple')
                case 'no h' | 'yes h':
                    typing_print(f'Does your pokemon have horns')
                    answer = input().lower()
                    remove_pokemon(answer, 'horns', 'horns', 'yes h')
                case 'no t' | 'yes t':
                    typing_print(f'Does your pokemon have tentacles')
                    answer = input().lower()
                    remove_pokemon(answer, 'tentacles', 'tentacles', 'yes t')
        else:
            typing_print(f"Hmmm... I think I'm getting closer. Is you're pokemon{list(available_pokemon.keys())[0]}")
            answer = input().lower()
            if answer == 'yes' or 'y':
                typing_print('Hah, I knew I could do it.\nDo you want to play again?')
                new_answer = input().lower()
                if new_answer == 'yes' or answer == 'y':
                    typing_print("Great!! Do you have a new pokemon in mind?\n Let's go!")
                    available_pokemon = GEN1
                    question_counter = 0
                else:
                    running = False
            elif answer == 'no' or answer == 'n':
                del available_pokemon[list(available_pokemon.keys())[0]]
        question_counter += 1   
    typing_print ('Wow, you really stumped me there.\nDo you want to play again?')
    answer = input().lower()
    if answer == 'yes' or answer == 'y':
        typing_print("Great!! Do you have a new pokemon in mind?\n Let's go!")
        available_pokemon = GEN1
        question_counter = 0
    else:
        running = False 
