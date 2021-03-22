# Sydney Kiick
# A program to track volleyball statistics throughout the season.

# Introduction
print("Hello!", end=' ')
print("Welcome to an easy way to track volleyball stats.", "Tracking stats can be a very tedious job, but not anymore!", sep=' ')

# Blank line to make code look prettier
print('')

# Game Information
number_of_players = float(input("Number of players: "))
total_sets = float(input("Total Sets: "))
time_outs_1 = float(input("Time Outs Used in Game 1: "))
time_outs_2 = float(input("Time Outs Used in Game 2: "))
time_outs_3 = float(input("Time Outs Used in Game 3: "))
time_outs_4 = float(input("Time Outs Used in Game 4: "))
time_outs_5 = float(input("Time Outs Used in Game 5: "))
game_score_1_home = input("Game One Score - Home: ")
game_score_2_home = input("Game Two Score - Home: ")
game_score_3_home = input("Game Three Score - Home: ")
game_score_4_home = input("Game Four Score - Home: ")
game_score_5_home = input("Game Five Score - Home: ")
game_score_1_away = input("Game One Score - Away: ")
game_score_2_away = input("Game Two Score - Away: ")
game_score_3_away = input("Game Three Score - Away: ")
game_score_4_away = input("Game Four Score - Away: ")
game_score_5_away = input("Game Five Score - Away: ")
home_team = 0
away_team = 0
# Game Calculations
# Adding up the number of time outs used
total_time_outs = time_outs_1 + time_outs_2 + time_outs_3 + time_outs_4 + time_outs_5
# Subtracting the number of timeouts used from the total available (2 per set)
time_outs_remaining = (total_sets * 2) - total_time_outs

# Blank line to make code look prettier
print('')

# Printing Game Stats
inFile = open("Statistics.txt", 'w')
inFile.write("* GAME STATS " * 3+"*")
inFile.write("\nTime Outs Remaining: " + str(time_outs_remaining))
inFile.write("\nGame One Score: " + str(game_score_1_home) + " - " + str(game_score_1_away))
if (game_score_1_home > game_score_1_away):
    inFile.write("\nHOME TEAM WINS SET 1")
    home_team += 1
else:
    inFile.write("\nAWAY TEAM WINS SET 1")
    away_team += 1
inFile.write("\nGame Two Score: " + str(game_score_2_home) + " - " + str(game_score_2_away))
if (game_score_2_home > game_score_2_away):
    inFile.write("\nHOME TEAM WINS SET 2")
    home_team += 1
else:
    inFile.write("\nAWAY TEAM WINS SET 2")
    away_team += 1
inFile.write("\nGame Three Score: " + str(game_score_3_home) + " - " + str(game_score_3_away))
if (game_score_3_home > game_score_3_away):
    inFile.write("\nHOME TEAM WINS SET 3")
    home_team += 1
else:
    inFile.write("\nAWAY TEAM WINS SET 3")
    away_team += 1
inFile.write("\nGame Four Score: " + str(game_score_4_home) + " - " + str(game_score_4_away))
if (game_score_4_home > game_score_4_away):
    inFile.write("\nHOME TEAM WINS SET 4")
    home_team +=1
else:
    inFile.write("\nAWAY TEAM WINS SET 4")
    away_team +=1
inFile.write("\nGame Five Score: " + str(game_score_5_home) + " - " + str(game_score_5_away))
if (game_score_5_home > game_score_5_away):
    inFile.write("\nHOME TEAM WINS SET 5")
    home_team += 1
else:
    inFile.write("\nAWAY TEAM WINS SET 5")
    away_team += 1
inFile.write("\n")
inFile.write("END SCORE: ")
if (home_team or away_team == 0):
    inFile.write("WINNING TEAM SWEEPS")
elif (home_team > away_team == True):
    inFile.write("HOME TEAM WINS GAME")
elif (away_team > home_team == True):
    inFile.write("AWAY TEAM WINS GAME")






while (number_of_players != 0):
    # Basic Information
    player_name = input("Player Name: ")
    player_number = input("Player Number: ")
    player_position = input("Player Position: ")
    sets_played = float(input("Number of sets played in: "))

    # Player Statistics
    player_passes = float(input("Number of Passes: "))
    player_assists = float(input("Number of Assists: "))
    player_digs = float(input("Number of Digs: "))
    player_serves = float(input("Number of Serves: "))
    player_aces = float(input("Number of Aces: "))
    player_hits = float(input("Number of Hits: "))
    player_kills = float(input("Number of Kills: "))
    print("")

    # Basic Calculations
    # Using the modulus function to provide the number of sets the player did not play in
    sets_benched = total_sets % sets_played
    # Dividing the number of kills by the total number of hits to find the kill percentage.
    kill_percentage = (player_kills / player_hits) * 100
    # Dividing the number of aces by the total number of serves to find the ace percentage.
    ace_percentage = (player_aces / player_serves) * 100
    # Adding up all the touches on the ball to determine the total touches
    total_touches = player_passes + player_assists + player_digs + player_serves + player_hits

    # Printing Player Stats
    inFile.write("\n""* PLAYER STATS " * 3 + "*")
    inFile.write("\nPlayer: " + "#" + str(player_number) + " " + player_name)
    inFile.write("\nPlayer Position: " + player_position)
    inFile.write("\nSets Played: " + str(sets_played))
    inFile.write("\nSets Benched: " + str(sets_benched))
    inFile.write("\nTotal Passes: " + str(player_passes))
    inFile.write("\nTotal Assists: " + str(player_assists))
    inFile.write("\nTotal Digs: " + str(player_digs))
    inFile.write("\nKill Percentage: " + format(kill_percentage, '.0f')+"%")
    inFile.write("\nAce Percentage: " + format(ace_percentage, '.0f')+"%")
    inFile.write("\nTotal Touches: " + str(total_touches))

    # Continue asking for stats?
    number_of_players -= 1

    print("Random Functions")
    # Random exponential function until i can figure out how to incorporate one into my program
    exponential = time_outs_1 ** time_outs_2
    # Random floor division function until i can figure out how to incorporate one into my program
    floor_division = total_sets // sets_played
    print("Exponential Function: ", exponential)
    print("Floor Division: ", floor_division)
    print("")

    # Close file
inFile.close()

# Random functions until I can figure out a use for them
for x in range (5):
    print (x)
print(home_team < away_team)
print((away_team <=3) and (home_team <= 2))
print(not(away_team > 2))
print((away_team == 3) or (home_team == 3))

first_name = input("coach's first name: ")
last_name = input("coach's last name: ")
def coach_name(x,y):
    print(x,y)
coach_name(first_name,last_name)
