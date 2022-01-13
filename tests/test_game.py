import pytest

from wordle.game import Wordle


@pytest.mark.parametrize("word_input, expected_response", [
    ("aaaaa", False), ("fable", True)])
def test_check_word_exists(word_input, expected_response):
    wordle_object = Wordle(word_input, "banal")
    assert wordle_object.check_word_exists() == expected_response


@pytest.mark.parametrize("word_input, ground_truth, expected_tags", [
    ("alive", "banal", {0: 'yellow', 1: 'yellow', 2: 'grey', 3: 'grey', 4: 'grey'}),
    ("alarm", "banal", {0: 'yellow', 1: 'yellow', 2: 'yellow', 3: 'grey', 4: 'grey'}),
    ("canal", "banal", {0: 'grey', 1: 'green', 2: 'green', 3: 'green', 4: 'green'}),
    ("alram", "banal", {0: 'yellow', 1: 'yellow', 2: 'grey', 3: 'green', 4: 'grey'})
])
def test_process_word(word_input, ground_truth, expected_tags):
    wordle_object = Wordle(word_input, ground_truth)
    wordle_object.process_word()
    assert wordle_object._tags == expected_tags
