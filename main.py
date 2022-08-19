import random

R = random
while True:
    player_action = input('Сделайте свой выбор: камень, ножницы или бумага: ')
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    print(f'\nВы выбрали {player_action}, компьютер выбрал {computer_action}')
    if player_action == computer_action:
        print(f'Оба игрока выбрали {player_action}. Ничья!')
    elif computer_action == 'камень':
        if player_action == 'ножницы':
            print('Камень побил ножницы,победа компьютера!')
        else:
            player_action == 'бумага'
            print('Бумага обернула камень, победа игрока!')
    elif computer_action == 'ножницы':
        if player_action == 'бумага':
            print('Ножницы режут бумагу, победа компьютера!')
        else:
            player_action == 'камень'
            print('Камень побил ножницы, победа игрока!')
    elif computer_action == 'бумага':
        if player_action == 'камень':
            print('Бумага обернула камень, победа компьютера!')
        else:
            player_action == 'ножницы'
            print('Ножницы режут бумагу, победа игрока!')

    play_go = ''
    play_go = input('Хотите сыграть ещё? (д/н): ')
    if 'д' != play_go.lower():
        break
