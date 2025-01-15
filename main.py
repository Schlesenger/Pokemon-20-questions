from collections import Counter
from time import sleep
from sys import stdout
from data import *
import sys
class Game:
    def __init__(self):
        self.available_pokemon = GEN1
        self.question_counter = 1
        self.running = True

    def typing_print(self, text):
        for char in text:
            stdout.write(char)
            stdout.flush()
            sleep(0.025)

    def get_most_common_value(self, dict):
        #creates counter
        all_values = []
        for inner_dict in dict.values():
            all_values.extend(inner_dict.values())
        value_counts = Counter(all_values)

        #finds most common that doesn't include all pokemon
        for value, count in value_counts.most_common():
            if count < len(dict):
                return value
        return None

    def remove_pokemon(self, ans, key_1, key_2, value):
        available_pokemon_copy = self.available_pokemon.copy()
        answer = ans
        if answer == 'yes'or answer == 'y':
            self.available_pokemon = {key: val for key, val in available_pokemon_copy.items() if val[key_1] == value or val[key_2] == value}
                
        elif answer == 'no' or answer == 'n':
            self.available_pokemon = {key: val for key, val in available_pokemon_copy.items() if val[key_1] != value and val[key_2] != value}

    def run(self):
        self.typing_print("Hello, welcome to the 20 questions pokemon game\n"\
                          "where I try to guess which pokemon from the first 151 you are thinking of in 20 questions or less!\n"\
                          "For answers, type yes or y for yes, and no or n for no\n"\
                          "Got a pokemon in mind? Let's go\n")
        while self.running == True:
            if self.question_counter <= 20:
                self.typing_print(f'question {self.question_counter}:\n')
                if len(self.available_pokemon) > 21 - self.question_counter:
                    most_common_value = self.get_most_common_value(self.available_pokemon)
                    match most_common_value:
                        case 'normal' | 'fire' | 'fighting' | 'water' | 'flying' | 'grass' | 'poison' | 'electric' | 'ground' | 'pyschic' | 'rock' | 'ice' | 'bug' | 'dragon' | 'ghost' | 'dark' | 'steel' | 'fairy':
                            self.typing_print(f'Is your pokemon a(n) {most_common_value} type?\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'type 1', 'type 2', most_common_value)
                        case 'animal' | 'humanoid' | 'object' | 'plant':
                            self.typing_print(f'Is your pokemon a(n) {most_common_value}?\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'base form', 'base form', most_common_value)
                        case '0 a' | '2 a' | '4 a':
                            value = most_common_value.split(' ')
                            self.typing_print(f'Does your pokemon have {value} arms\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'arms', 'arms', most_common_value)
                        case '0 l' | '2 l' | '4 l' | '14 l':
                            value = most_common_value.split(' ')
                            self.typing_print(f'Does your pokemon have {value} legs\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'legs', 'legs', most_common_value)
                        case 'no w' | 'yes w':
                            self.typing_print(f'Does your pokemon have wings\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'wings', 'wings', 'yes w')
                        case '1' | 'multiple':
                            self.typing_print(f'Does your pokemon have multiple heads\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'heads', 'heads', 'multiple')
                        case 'no h' | 'yes h':
                            self.typing_print(f'Does your pokemon have horns\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'horns', 'horns', 'yes h')
                        case 'no t' | 'yes t':
                            self.typing_print(f'Does your pokemon have tentacles\n')
                            answer = input().lower()
                            self.remove_pokemon(answer, 'tentacles', 'tentacles', 'yes t')
                else:
                    self.typing_print(f"Hmmm... I think I'm getting closer. Is you're pokemon {list(self.available_pokemon.keys())[0]}?\n")
                    answer = input().lower()
                    if answer == 'yes' or answer == 'y':
                        self.typing_print('Hah, I knew I could do it.\nDo you want to play again?\n')
                        new_answer = input().lower()
                        if new_answer == 'yes' or answer == 'y':
                            self.typing_print("Great!! Do you have a new pokemon in mind?\n Let's go!\n")
                            self.available_pokemon = GEN1
                            self.question_counter = 0
                        else:
                            self.running = False
                    elif answer == 'no' or answer == 'n':
                        del self.available_pokemon[list(self.available_pokemon.keys())[0]]
                self.question_counter += 1
            else:   
                self.typing_print ('Wow, you really stumped me there.\nDo you want to play again?\n')
                answer = input().lower()
                if answer == 'yes' or answer == 'y':
                    self.typing_print("Great!! Do you have a new pokemon in mind?\n Let's go!\n")
                    self.available_pokemon = GEN1
                    self.question_counter = 1
                else:
                    self.running = False 

if __name__ == '__main__':
    game = Game()
    game.run()