from collections import Counter
from time import sleep
from sys import stdout
from data import *

class Game:
    def __init__(self):
        self.available_pokemon = GEN1
        self.question_counter = 1
        self.running = True
        self.multi_heads_asked = False

    def typing_print(self, text):
        for char in text:
            stdout.write(char)
            stdout.flush()
            sleep(0.025)

    def get_most_common_value(self, data):
        #getting all the values from the data
        all_values = []
        for dict in data.values():
            all_values.extend(dict.values())
        all_values = [x for x in all_values if x != None]
        all_value_counts = Counter(all_values)

        #getting the values shared across each dictionary in the data
        common_values = []
        for value, count in all_value_counts.most_common():
            if count >= len(data):
                common_values.append(value)
            else:
                break
        
        #removing the shared values
        not_common_values = [x for x in all_values if x not in common_values]

        #counting the remaining values to get 1 most common value
        not_common_value_counts = Counter(not_common_values)
        max_count = max(not_common_value_counts.values())
        most_common_values = [key for key, count in not_common_value_counts.items() if count == max_count]
        return most_common_values[0]
        
    def remove_pokemon(self, answer, key_1, key_2, value):
        available_pokemon_copy = self.available_pokemon.copy()
        if answer == 'yes'or answer == 'y':
            self.available_pokemon = {key: val for key, val in available_pokemon_copy.items() if val[key_1] == value or val[key_2] == value}
                
        elif answer == 'no' or answer == 'n':
            self.available_pokemon = {key: val for key, val in available_pokemon_copy.items() if val[key_1] != value and val[key_2] != value}

    def get_answer(self):
        answer = input().lower()
        while answer != 'yes' and answer != 'y' and answer != 'no' and answer != 'n':
            self.typing_print("I'm sorry, I don't recognize that answer\n")
            answer = input().lower()
        return answer
        
    def run(self):
        self.typing_print("Hello, welcome to the 20 questions pokemon game\n"\
                          "where I try to guess which pokemon from the first 151 you are thinking of in 20 questions or less!\n"\
                          "For answers, type yes or y for yes, and no or n for no\n"\
                          "Got a pokemon in mind? Let's go\n")
        while self.running == True:
            if self.question_counter <= 20:
                self.typing_print(f'question {self.question_counter}:\n')
                if len(self.available_pokemon) > 21 - self.question_counter or len(self.available_pokemon) > 5:
                    most_common_value = self.get_most_common_value(self.available_pokemon)
                    match most_common_value:
                        case 'normal' | 'fire' | 'fighting' | 'water' | 'flying' | 'grass' | 'poison' | 'electric' | 'ground' | 'pyschic' | 'rock' | 'ice' | 'bug' | 'dragon' | 'ghost' | 'dark' | 'steel' | 'fairy':
                            self.typing_print(f'Is your pokemon a(n) {most_common_value} type?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'type 1', 'type 2', most_common_value)
                        case 'animal' | 'humanoid' | 'object' | 'plant':
                            self.typing_print(f'Is your pokemon a(n) {most_common_value}?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'base form', 'base form', most_common_value)
                        case '0 a' | '2 a' | '4 a':
                            value = most_common_value.split(' ')
                            self.typing_print(f'Does your pokemon have {value[0]} arms?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'arms', 'arms', most_common_value)
                        case '0 l' | '2 l' | '4 l' | '14 l':
                            value = most_common_value.split(' ')
                            self.typing_print(f'Does your pokemon have {value[0]} legs?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'legs', 'legs', most_common_value)
                        case 'no w' | 'yes w':
                            self.typing_print(f'Does your pokemon have wings?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'wings', 'wings', 'yes w')
                        case '1' | 'multiple':
                            if not self.multi_heads_asked:
                                self.typing_print(f'Does your pokemon have multiple heads?\n')
                                answer = self.get_answer()
                                self.remove_pokemon(answer, 'heads', 'heads', 'multiple')
                                self.multi_heads_asked = True
                            else:
                                self.typing_print(f'Does your pokemon have at least 1 head?\n')
                                answer = self.get_answer()
                                self.remove_pokemon(answer, 'heads', 'heads', '1')
                        case 'no h' | 'yes h':
                            self.typing_print(f'Does your pokemon have horns?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'horns', 'horns', 'yes h')
                        case 'no t' | 'yes t':
                            self.typing_print(f'Does your pokemon have any tails?\n')
                            answer = self.get_answer()
                            self.remove_pokemon(answer, 'tails', 'tails', 'yes t')
                        case _:
                            self.typing_print(f'The most common value is {most_common_value}\n')
                elif len(self.available_pokemon) > 0:
                    self.typing_print(f"Hmmm... I think I'm getting closer. Is you're pokemon {list(self.available_pokemon.keys())[0]}?\n")
                    answer = self.get_answer()
                    if answer == 'yes' or answer == 'y':
                        self.typing_print('Hah, I knew I could do it.\nDo you want to play again?\n')
                        new_answer = self.get_answer()
                        if new_answer == 'yes' or new_answer == 'y':
                            self.typing_print("Great!! Do you have a new pokemon in mind?\nLet's go!\n")
                            self.available_pokemon = GEN1
                            self.question_counter = 0
                            self.multi_heads_asked = False
                        elif new_answer == 'no' or new_answer == 'n':
                            self.running = False
                    elif answer == 'no' or answer == 'n':
                        del self.available_pokemon[list(self.available_pokemon.keys())[0]]
                else:
                    self.typing_print("I'm sorry it seems I've eliminated all the possibilities.\nYou win this round, want to play again?\n")
                    answer = self.get_answer()
                    if answer == 'yes' or answer == 'y':
                        self.typing_print("Great!! Do you have a new pokemon in mind?\nLet's go!\n")
                        self.available_pokemon = GEN1
                        self.question_counter = 0
                        self.multi_heads_asked = False
                    elif answer == 'no' or answer == 'n':
                        self.running = False
                self.question_counter += 1
            else:   
                self.typing_print ('Wow, you really stumped me there.\nDo you want to play again?\n')
                answer = self.get_answer()
                if answer == 'yes' or answer == 'y':
                    self.typing_print("Great!! Do you have a new pokemon in mind?\n Let's go!\n")
                    self.available_pokemon = GEN1
                    self.question_counter = 1
                    self.multi_heads_asked = False
                else:
                    self.running = False 

if __name__ == '__main__':
    game = Game()
    game.run()