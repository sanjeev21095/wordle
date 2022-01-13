import pytest
from wordle import rules


@pytest.mark.parametrize("word_entered, expected_tags", [
    ("abcde", {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"}),
    ("aaaaa", {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"}),
    ("alpha", {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"})])
def test_create_tags(word_entered, expected_tags):
    tags = rules.create_tags(word_entered)
    assert tags == expected_tags


@pytest.mark.parametrize("truth, word_entered, tags, exp_truth, exp_word, expected_tags", [
    (list("banal"), list("alive"), {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"},
     list("banal"), list("alive"), {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"}),

    (list("banal"), list("alram"), {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"},
     list("ban$l"), list("alr$m"), {0: "grey", 1: "grey", 2: "grey", 3: "green", 4: "grey"}),

    (list("banal"), list("canal"), {0: "grey", 1: "grey", 2: "grey", 3: "grey", 4: "grey"},
     list("b$$$$"), list("c$$$$"), {0: "grey", 1: "green", 2: "green", 3: "green", 4: "green"})
])
def test_green_cycle(truth, word_entered, tags, exp_truth, exp_word, expected_tags):
    mod_truth, mod_word_entered, updated_tags = rules.green_cycle(truth, word_entered, tags)
    assert mod_truth == exp_truth
    assert mod_word_entered == exp_word
    assert updated_tags == expected_tags


@pytest.mark.parametrize("truth, word_entered, tags, exp_truth, exp_word, expected_tags", [
    (list("ban$l"), list("alr$m"), {0: "grey", 1: "grey", 2: "grey", 3: "green", 4: "grey"},
     list("b$n$$"), list("$$r$m"), {0: "yellow", 1: "yellow", 2: "grey", 3: "green", 4: "grey"}),

    (list("b$$$$"), list("c$$$$"), {0: "grey", 1: "green", 2: "green", 3: "green", 4: "green"},
     list("b$$$$"), list("c$$$$"), {0: "grey", 1: "green", 2: "green", 3: "green", 4: "green"})
])
def test_yellow_cycle(truth, word_entered, tags, exp_truth, exp_word, expected_tags):
    mod_truth, mod_word_entered, updated_tags = rules.yellow_cycle(truth, word_entered, tags)
    assert mod_truth == exp_truth
    assert mod_word_entered == exp_word
    assert updated_tags == expected_tags