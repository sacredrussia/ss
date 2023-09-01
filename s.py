print('первым ходит игрок x')
board1 = ['-', '-', '-']
board2 = ['-', '-', '-']
board3 = ['-', '-', '-']

def draw_board(board1, board2, board3):
   print('  '  '1' '   ' '2' '   ' '3')
   print('1', board1[0],' ', board1[1], ' ', board1[2])
   print('2', board2[0], ' ', board2[1], ' ', board2[2])
   print('3', board3[0], ' ', board3[1], ' ', board3[2])

def take_input(player_token):
    valid = False
    while not valid:
        player_answer_vert = input("Куда поставим по вертикали " + player_token + "? ")
        try:
            player_answer_vert = int(player_answer_vert)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer_vert in range(1,4):
             player_answer_gor = input("Куда поставим по горизонтали " + player_token + "? ")
             try:
                 player_answer_gor = int(player_answer_gor)
             except:
                 print("Некорректный ввод. Вы уверены, что ввели число?")
                 continue
             if player_answer_gor >= 1 and player_answer_gor <= 3:
                 if player_answer_vert == 1:
                     if (str(board1[player_answer_gor - 1]) not in "XO"):
                         board1[player_answer_gor - 1] = player_token
                         valid = True
                     else:
                         print("Эта клетка уже занята!")
                 elif player_answer_vert == 2:
                     if (str(board2[player_answer_gor - 1]) not in "XO"):
                         board2[player_answer_gor - 1] = player_token
                         valid = True
                     else:
                         print("Эта клетка уже занята!")
                 elif player_answer_vert == 3:
                     if (str(board3[player_answer_gor - 1]) not in "XO"):
                         board3[player_answer_gor - 1] = player_token
                         valid = True
                     else:
                         print("Эта клетка уже занята!")
             else:
                 print("Некорректный ввод. Введите число от 1 до 3.")
        else:
            print("Некорректный ввод. Введите число от 1 до 3.")
def check_win(board1, board2, board3):
   win_coord1 = ['012']
   win_coord2 = ['012']
   win_coord3 = ['012']
   for each1 in win_coord1:
       for each2 in win_coord2:
           for each3 in win_coord3:
               if board1[int(each1[0])] == board1[int(each1[1])] == board1[int(each1[2])]:
                   if board1[int(each1[0])] != '-' and board1[int(each1[1])] != '-' and board1[int(each1[2])] != '-':
                       return board1[int(each1[0])]
               elif board2[int(each2[0])] == board2[int(each2[1])] == board2[int(each2[2])]:
                   if board2[int(each2[0])] != '-' and board2[int(each2[1])] != '-' and board2[int(each2[2])] != '-':
                       return board2[int(each2[0])]
               elif board3[int(each3[0])] == board3[int(each3[1])] == board3[int(each3[2])]:
                   if board3[int(each3[0])] != '-' and board3[int(each3[1])] != '-' and board3[int(each3[2])] != '-':
                       return board3[int(each3[0])]
               elif board1[int(each1[2])] == board2[int(each2[2])] == board2[int(each2[2])]:
                   if board1[int(each1[2])] != '-' and board2[int(each2[2])] != '-' and board2[int(each2[2])] != '-':
                       return board1[int(each1[2])]
               elif board1[int(each1[1])] == board2[int(each2[1])] == board3[int(each3[1])]:
                   if board1[int(each1[1])] != '-' and board2[int(each2[1])] != '-' and board3[int(each3[1])] != '-':
                       return board1[int(each1[1])]
               elif board1[int(each1[0])] == board2[int(each2[0])] == board3[int(each3[0])]:
                   if board1[int(each1[0])] != '-' and board2[int(each2[0])] != '-' and board3[int(each3[0])] != '-':
                       return board1[int(each1[0])]
               elif board1[int(each1[0])] == board2[int(each2[1])] == board3[int(each3[2])]:
                   if board1[int(each1[0])] != '-' and board2[int(each2[1])] != '-' and board3[int(each3[2])] != '-':
                       return board1[int(each1[0])]
               elif board1[int(each1[2])] == board2[int(each2[1])] == board3[int(each3[0])]:
                   if board1[int(each1[2])] != '-' and board2[int(each2[1])] != '-' and board3[int(each3[0])] != '-':
                       return board1[int(each1[2])]

   return False
def main(board1, board2, board3):
    counter = 0
    win = False
    while not win:
        draw_board(board1, board2, board3)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board1, board2, board3)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board1, board2, board3)

main(board1, board2, board3)
input("Нажмите Enter для выхода!")
