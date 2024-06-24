import random


def get_word():
    word_list = [word[:-1] for word in open('word_list.txt', encoding='utf-8')]
    return random.choice(word_list).upper()
