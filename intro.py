import random

intro = 'Правила игры таковы: бот и игрок на старте имеют одно количетсво ХП на двоих. Цель: вводить цифру от 1 до ' \
        '10, тот, кто умрет первым, проиграл. Однако есть рандом, который дает шанс критического урона. Удачи!'
username = input('Твое имя? ')
print('Привет, {}! {}'.format(username.title(), intro))
while True:
    respond = input('Хочешь сыграть? Вводи 0, если нет, и 1 - если да ')
    try:
        respond = int(respond)
    except ValueError:
        print('Самое время выгнать тебя в самое начало: нужно ввести число, а не вот это вот: {}.'.format(respond))
        break

    if respond == 1:
        print('Отлично, тогда переходим к настройке.')
    if respond > 1:
        print('Технически, {} включает в себя единицу, поэтому ты будешь играть!'.format(respond))
    if respond == 0:
        print('Это, конечно, тоже выбор, но бууууууууу!')
        break
    while True:
        hp = input('Сколько ХП поставить? Нажми 0, если хочешь рандом ')
        try:
            hp = int(hp)
        except ValueError:
            print('Ну тут-то с чем проблемы? У ХП ведь всегда цифры!')
            break
        if hp > 0:
            print('Отлично! У вас с ботом {} на двоих.'.format(hp))
        elif hp < 0:
            print('Ну, так тоже можно: будет не вычитание, а сложение. У вас с ботом {} ХП на двоих.'.format(hp))
        elif hp == 0:
            hp = random.randint(1, 101)
            print('Ну что, боги рандома назначили вам {} ХП на двоих.'.format(hp))
        while True:
            if hp <= 0:
                break
            hit = int(input('Сколько ХР откусим у бота? '))
            if hit > 0 and hit < 11:
                    hit = hit
            else:
                print('А ведь в правилах сказано: от 1 до 10! Повнимательнее тут, {}!'.format(username.title()))
                break
            while True:
                hp = hp - hit
                if hp == 0:
                    print('Ого-го! Будущее в безопасности! И только благодаря {}!'.format(username.title()))
                    break
                if hp > 0:
                    print('У вас осталось {} ХП на двоих!'.format(hp))
                bothit = random.randint(0, 10)
                hp = hp - bothit
                if hp > 0:
                    print('Бот сделал кусь на {}, у вас осталось {} на двоих.'.format(bothit, hp))
                    break
                elif hp <= 0:
                    print('Бот откусил на {}, ХП больше не осталось. Надеюсь терминатор будет на нашей стороне,'
                      ' ибо компьютер побеждает!'.format(bothit))
                    break


