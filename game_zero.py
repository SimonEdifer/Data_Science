# Создаем игровое поле
board = [[' ' for _ in range(3)] for _ in range(3)]

# Проверка на победителя
def check_winner():
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Отрисовка игрового поля
def draw_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Главная функция игры
def play_game():
    current_player = 'X'
    is_game_over = False

    while not is_game_over:
        draw_board()
        print("Ход игрока", current_player)

        # Запрос координат от игрока
        row = int(input("Введите номер строки (0, 1, 2): "))
        col = int(input("Введите номер столбца (0, 1, 2): "))

        # Проверка на корректность координат
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Некорректные координаты, попробуйте еще раз.")
            continue

        # Установка символа на поле
        board[row][col] = current_player

        # Проверка на победителя или ничью
        winner = check_winner()
        if winner:
            draw_board()
            print("Игрок", winner, "победил!")
            is_game_over = True
        elif all(all(cell != ' ' for cell in row) for row in board):
            draw_board()
            print("Ничья!")
            is_game_over = True

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
play_game()
