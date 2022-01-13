from typing import List, Dict, Tuple


def create_tags(word_entered: str) -> Dict[int, str]:
    tags = {}
    for pos, _ in enumerate(word_entered):
        tags[pos] = 'grey'
    return tags


def green_cycle(truth: List[str], word_entered: List[str], tags: Dict[int, str]) -> Tuple:
    for i in range(len(word_entered)):
        char = word_entered[i]
        pos = i
        if char == truth[pos]:
            tags[pos] = "green"
            truth[pos] = "$"
            word_entered[pos] = "$"
    return truth, word_entered, tags


def yellow_cycle(truth: List[str], word_entered: List[str], tags: Dict[int, str]) -> Tuple:
    for i in range(len(word_entered)):
        char = word_entered[i]
        pos = i
        if char is not "$":
            if char in truth:
                tags[pos] = "yellow"
                index = truth.index(char)
                truth[index] = "$"
                word_entered[pos] = "$"
    return truth, word_entered, tags
