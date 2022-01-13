import copy

from termcolor import colored, cprint
import os
import random

from wordle import rules

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "common_words.txt")


class Wordle:
    def __init__(self, input_word, true_word):
        self._input_word = input_word
        self._truth = true_word
        self._tags = rules.create_tags(self._input_word)

    def check_word_exists(self):
        if len(self._input_word) != 5:
            print("Enter a 5 letter word only")
            return False

        with open(file_path) as file:
            contents = file.read().split("\n")
            if self._input_word not in contents:
                print('Input word not found. Try again!\n')
                return False
            return True

    def process_word(self):
        # do green cycle and then yellow cycle
        true_copy = copy.deepcopy(self._truth)
        word_copy = copy.deepcopy(self._input_word)
        modified_true, modified_input_word, updated_tags = rules.green_cycle(list(true_copy), list(word_copy),
                                                                             self._tags)
        final_true, final_input, final_tags = rules.yellow_cycle(modified_true, modified_input_word, updated_tags)
        self._tags = final_tags

    def get_answer(self):
        output = ""
        for pos, char in enumerate(self._input_word):
            output += colored(char, self._tags[pos])
        return output

    def check_end_game(self):
        if all(value == "green" for value in self._tags.values()):
            print("Good Job!")
            exit()

    @staticmethod
    def pick_game_word() -> str:
        with open(file_path) as file:
            contents = file.read().split("\n")
        word_index = random.randint(0, len(contents))
        return contents[word_index]


def start_game():
    print("You have 6 guesses!\n")
    ground_truth = Wordle.pick_game_word()
    try_num = 0
    while try_num <= 6:
        input_word = input(f"Guess {try_num + 1}: ")
        wordle_object = Wordle(input_word, ground_truth)
        if wordle_object.check_word_exists():
            wordle_object.process_word()
            cprint("Attempt " + str(try_num + 1) + " : " + wordle_object.get_answer() + "\n")
            wordle_object.check_end_game()
            try_num += 1
        else:
            continue
    print(f"Hard Luck! You were trying to guess the word {ground_truth}")


if __name__ == '__main__':
    start_game()
