import random

def topicchoice(): #выбор темы
    numbers = ['1', '2', '3'] #допустимые номера тем
    topic = input('Выберите одну из трех тем и введите ее номер:\n1. Крепкие алкогольные напитки\n2. Жанры классической музыки\n3. Языки банту\n')
    if topic not in numbers:
        print('Вы ввели что-то не то. Попробуйте еще раз.')
        exit(0)
    else:
        print('У вас есть 8 попыток.')
        return topic #возвращает номер темы для генерации названия файла со словами

def wordchoice(topicfile):
    fname = topicfile + '.txt' #выбор файла с нужным номером темы в названии
    with open (fname, encoding='utf-8') as f:
        words = f.read().split('\n') #чтобы избавиться от лишних переносов строк в словах
    word = random.choice(words)
    return word

def guess(word, dashscheme, chances):
    used = [] #список использованных букв
    letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') #допустимые буквы
    while chances != 0:
        bet = input('Введите букву русского алфавита или догадку: ').lower() #догадка пользователя в нижнем регистре
        if bet == word: #если слово угадано, программа завершается
            print('Все верно!')
            exit(0)
        elif bet not in letters: #проверка на допустимость ввода
            print('Вы ввели не букву русского алфавита или ваша догадка неверна.')
        elif bet in used:
            print('Вы уже использовали эту букву. Попробуйте еще раз.') #проверка на повторный ввод
        else:
            used.append(bet) #включение буквы в список использованных
            if bet in word: #проверка наличия буквы в слове
                newscheme = list(dashscheme) #рабочая переменная для генерации новой схемы с черточками и накопления изменений
                for symbol in enumerate(list(word)): #побуквенный проход слова
                    if symbol[1] == bet: #если буква слова в итерации равна вводу
                        newscheme[symbol[0]] = bet #нужный элемент в схеме заменяется на эту букву
                dashscheme = ''.join(newscheme)
                print(' '.join(dashscheme))
            else:
                fname = 'hang'+str(chances)+'.txt' #выбор нужной формы виселицы в зависимости от номера попытки
                chances -= 1 #количество попыток уменьшается только при вводе буквы, которой нет в слове
                with open(fname, encoding='utf-8') as f:
                    hangingman = f.read()
                    print(hangingman)
            message = 'У вас остал{}сь {} попыт{}.' #для согласования глагола и существительного с числительным
            if chances > 4:
                print(message.format('о', chances, 'oк'))
            elif chances > 1:
                print(message.format('о', chances, 'ки'))
            elif chances == 1:
                print(message.format('a', chances, 'ка'))
            else:
                print(message.format('о', chances, 'ок'), 'Может, в другой раз получится.') #выход по окончании возможных попыток
                exit(0)

def main():
    file = topicchoice()
    answer = wordchoice(file)
    dashes = '_' * len(answer) #генерация первой схемы с количеством черточек по количеству букв
    print(' '.join(dashes))
    trials = 8 #изначальное количество попыток
    guess(answer, dashes, trials)

if __name__ == "__main__":
    main()