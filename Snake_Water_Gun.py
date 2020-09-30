import random
x = "*"
print("")
use_name = input("  Input A user Name : ")
user = use_name.capitalize()
print(" ",x*50)
print(" ",x*13," Snake_Water_Gun Game",x*14)
print(" ",x*50)
print(f"  Computer Vs {user} ")
print("  Total Chance : 10")
game_element = {"S":"Snake","W":"Water","G":"Gun"}
symbol_chr = ["Snake","Water","Gun"]
symbol_chr1 = ["S","W","G"]
print("")
for choice,S in game_element.items():
    print(f"  [{choice}] {S}")
computr = 0
player_point  = 0
Total   = 10
number_of_chance  = 0

try :
    while number_of_chance<Total:
     number_of_chance = number_of_chance + 1
     player = str(input(" \n  Choice : "))
     player_S = player.upper()
     random_coice = random.choice(symbol_chr1)
     # USER CHOICE S
     if player_S == "S" and random_coice == "W":
         player_point = player_point + 1
         print("")
         print(" ",x*50)
         print(" ",x*22,"WON",x*23)
         print(" ",x*50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ",x*50)
     elif player_S == "S" and random_coice == "G":
         computr = computr + 1
         print("")
         print(" ", x * 50)
         print(" ", x * 20,"LOSS", x * 24)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     # USER CHOICE W
     elif player_S == "W" and random_coice == "S":
         computr = computr + 1
         print("")
         print(" ", x * 50)
         print(" ", x * 20, "LOSS", x * 24)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     elif player_S == "W" and random_coice == "G":
         player_point = player_point + 1
         print("")
         print(" ", x * 50)
         print(" ", x * 22, " WON ", x * 23)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     # USER CHOICE G
     elif player_S == "G" and random_coice == "W":
         computr = computr + 1
         print("")
         print(" ", x * 50)
         print(" ", x * 20, " LOSS ", x * 24)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     elif player_S == "G" and random_coice == "S":
         player_point = player_point + 1
         print("")
         print(" ", x * 50)
         print(" ", x * 22, " WON ", x * 23)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     elif player_S == random_coice :
         print("")
         print(" ", x * 50)
         print(" ", x * 20, " DRAW ", x * 24)
         print(" ", x * 50)
         print(f"  You Choice      : {game_element[player_S]}")
         print(f"  Computer Choice : {game_element[random_coice]}")
         print(" ", x * 50)
     else :
         print("")
         print(" ",x*50)
         print("  Plz Input Correct and Not input any numeric ")
         print(" ",x*50)
except:
    print("Error")

print(" ",x*50)
print(f"\n       {user} Point  : {player_point} and Computer Point : {computr} ")
if computr == player_point:
    print("\n  ", x * 50)
    print(f"           {user} vs Computer Game is Draw ")
    print(" ", x * 50)
elif computr < player_point:
    print(" ", x * 50)
    print(f"                      {user} Win")
    print(" ", x * 50)
else :
    print(" ", x * 50)
    print("                      Computer Win")
    print(" ", x * 50)














