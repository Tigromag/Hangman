import random


def input_decision():
    while True:
        decision = input('Введите "да" или "нет": ').lower()
        if not (decision == 'да' or decision == 'нет'):
            print('Введите только "да" или "нет"!')
            continue
        else:
            return decision


def lose(word, tries, word_completion):
    print(f'Увы, Вы проиграли, загаданное слово: {word}')
    print(display_hangman(tries))
    print(word_completion)
    print('Хотите сыграть ещё раз?')


def win(tries, word):
    print('Поздравляем, вы угадали слово! Вы победили!')
    print(display_hangman(tries))
    print(word)
    print('Хотите сыграть ещё раз?')


def get_word():
    word_list = [word[:-1] for word in open('word_list.txt', encoding='utf-8')]
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def is_valid(word):
    return word.isalpha()


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов! (rus)')
    print(display_hangman(tries))
    print(word_completion)

    while True:

        # Проверка введенной строки
        while True:
            string = input('\nВведите букву или слово: ').upper()
            if not (is_valid(string)):
                print('Некорректный ввод!')
                continue
            else:
                if string in guessed_words or string in guessed_letters:
                    print('Вы уже вводили эту букву/это слово')
                    continue
            break

        # Добавление строки к уже названным и изменение "закрытой" строки
        if len(string) == 1:
            guessed_letters.append(string)
            for i in range(len(word)):
                if string == word[i]:
                    guessed = True
                    word_completion = word_completion[:i] + string + word_completion[i + 1:]
        else:
            guessed_words.append(string)
            if string == word:
                win(tries, word_completion)
                return input_decision()

        if word_completion.count('_') == 0:
            win(tries, word)
            return input_decision()

        if guessed == False:
            print('В этом слове нет такой буквы/это другое слово!')
            tries -= 1
        else:
            print('Такая буква есть!')

        if tries == 0:
            lose(word, tries, word_completion)
            return input_decision()
        else:
            print(display_hangman(tries))
            print(word_completion)


while True:
    if play(get_word()) == 'нет':
        break
