
import random
total_attempts = 3
min_number = 1
max_number = 20
games_played = 0
won_games = 0
isOver = False
isBckdrActived = False
txt_game_title = "Game \"Guess the Hidden Number\"."
txt_attempt_left = "{} more attempt(s)"
txt_first_input = "-> Guess the hidden number between {} and {}: "
txt_input_with_hint = "-> Guess the hidden number between {} and {} (Hint: {} and {}): "
txt_hint = "You should enter a {} number."
txt_discover = "[The hidden number is {}]"
txt_bckdr = "__HIDDEN [{}] NUMBER__"
txt_u_win = "YOU GUESSED IT!"
txt_u_lose = "You lose :(\nGood Luck next time."
txt_invalid_warning = "Invalid number! Try again..."
txt_play_again = "Play again? (Y/N): "
txt_game_over = ":::: GAME OVER ::::"
txt_games_played = "Games played: {}"
txt_won_lose_games = "{} games: {}"
txt_player_efficent = "Efficent: {}%"
txt_middle_dash = "------------------------------"
txt_asteriks = "****************************"
txt_middle_under_dash = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
while ~isOver:
   games_played = games_played + 1
   attempts_remain = total_attempts
   smaller_number_tried = min_number
   greater_number_tried = max_number
   isAvailableToPlay = attempts_remain > 0
   hidden_number = random.randint(min_number, max_number)
   print(txt_game_title)
   while isAvailableToPlay:
      isBeginning = attempts_remain == total_attempts
      isGameOver = attempts_remain == 0
      if isBckdrActived:
         print(txt_bckdr.format(hidden_number))
      if isBeginning:
         print(txt_attempt_left.format(attempts_remain))
         print(txt_first_input.format(min_number, max_number))
      elif isGameOver:
         isOver = True
         print(txt_middle_under_dash)
         print(txt_u_lose)
         print(txt_discover.format(hidden_number))
         print(txt_middle_under_dash)
         break
      else:
         print(txt_attempt_left.format(attempts_remain))
         print(txt_input_with_hint.format(min_number, max_number, smaller_number_tried, greater_number_tried))
      try_to_guess = int(input())
      isValidNumber = try_to_guess >= min_number and try_to_guess <= max_number
      isSmallerThanHiddenNumber = try_to_guess < hidden_number
      isGreaterThanHiddenNumber = try_to_guess > hidden_number
      if isValidNumber:
         if isGreaterThanHiddenNumber:
            attempts_remain = attempts_remain - 1
            greater_number_tried = try_to_guess
            print(txt_hint.format("smaller"))
            print(txt_middle_dash)
         elif isSmallerThanHiddenNumber:
            attempts_remain = attempts_remain - 1
            smaller_number_tried = try_to_guess
            print(txt_hint.format("greatest"))
            print(txt_middle_dash)
         else:
            print(txt_asteriks)
            print(txt_u_win)
            print(txt_discover.format(try_to_guess))
            print(txt_asteriks)
            isOver = True
            won_games = won_games + 1
            break
      else:
         print(txt_invalid_warning)
         print(txt_middle_dash)
   if isOver:
      answer = input(txt_play_again)
      willContinue = answer == 'y' or answer == 'Y'
      if willContinue:
         isOver = False
      else:
         print(txt_game_over)
         break
lose_games = games_played - won_games
player_efficent = (won_games * 100) / games_played
print(txt_middle_under_dash)
print(txt_games_played.format(games_played))
print(txt_won_lose_games.format("Won", won_games))
print(txt_won_lose_games.format("Lose", lose_games))
print(txt_player_efficent.format(player_efficent))
print(txt_middle_under_dash)




#let random = [Math.random()*100](https://Math.random()*100)
#let number = [Math.ceil(random)](https://Math.ceil(random))
# Math.random() devuelve un número aleatorio entre 0 y 1 con muchos decimales
# Se multiplica por 100 para que los números aleatorios sean entre 0 y 100.
# Y Math.ceil() aproxima el decimal al menor entero mayor a él JAVASC