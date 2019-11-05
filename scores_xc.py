#formats the score based on the file strips based on white space
#splits on new line, with output team_name:score_

def get_scores(filename):

  with open(filename, 'r') as data:
    plaintext = data.read()
    scores = []
    for line in plaintext.split('\n'):
      if not line:
        continue
      a, b = line.split(',')
      a_name, a_score = a.strip().rsplit(' ', 1)
      b_name, b_score = b.strip().rsplit(' ', 1)
   # print([a_name, a_score, b_name, b_score])
      dict = {a_name:a_score, b_name:b_score}

      scores.append(dict)
    #scores.append({a_name: a_score, b_name: b_score})
    return(scores)
#result   scores = [{'Lions': '3', 'Snakes': '3'}, {'Tarantulas': '1', 'FC Awesome': '0'}, {'Lions': '1', 'FC Awesome': '1'}, {'Tarantulas': '3', 'Snakes': '1'}, {'Lions': '4', 'Grouches': '0'}]
filename= input(" which file in txt format to output ?")
get_scores(filename)
games = get_scores(filename)


#get unique team names from the list
def get_team_names():

  from itertools import chain




  team_names = set(chain.from_iterable(games))


  teams = list(
    set(chain.from_iterable(games)))

  return teams


teams = get_team_names()
#result team = teams = ['FC Awesome', 'Tarantulas', 'Grouches', 'Lions', 'Snakes']

#iterate over each game in games and we compare the scores
#and turn the values into a a list and also an integer, compare first score to the input_text
#if first is greater than update the values for the keys based on results
#match is a draw if their a no game winner
def get_results():

  output = []
  games = [{'Lions': '3', 'Snakes': '3'}, {'Tarantulas': '1', 'FC Awesome': '0'}, {'Lions': '1', 'FC Awesome': '1'}, {'Tarantulas': '3', 'Snakes': '1'}, {'Lions': '4', 'Grouches': '0'}]
  for game in games:
    if int(list(game.values())[0]) > int(list(game.values())[1]):
        gamewinner = {list(game.keys())[0]: "Won", list(game.keys())[1]: "Lost"}
    elif int(list(game.values())[0]) < int(list(game.values())[1]):
        gamewinner = {list(game.keys())[0]: "Lost", list(game.keys())[1]: "Won"}
    else:
        gamewinner = {list(game.keys())[0]: "Draw", list(game.keys())[1]: "Draw"}
    output.append(gamewinner)
  return output


#get the winners and make a list of each respective winnings ie
#team = teams = ['FC Awesome', 'Tarantulas', 'Grouches', 'Lions', 'Snakes']
#respectively for each team such as [0, 2, 0, 1,0]
output_1 = get_results()
#output_1 = [{'Lions': 'Draw', 'Snakes': 'Draw'}, {'Tarantulas': 'Won', 'FC Awesome': 'Lost'}, {'Lions': 'Draw', 'FC Awesome': 'Draw'}, {'Tarantulas': 'Won', 'Snakes': 'Lost'}, {'Lions': 'Won', 'Grouches': 'Lost'}]
#teams = ['FC Awesome', 'Tarantulas', 'Grouches', 'Lions', 'Snakes']
def get_winners():

    win_count = []
    for team in teams:
      win_counter = 0
      for game in output_1:

        if (list(game.keys())[0]) == team and (list(game.values())[0]) =="Won":
          win_counter += 1
        elif (list(game.keys())[1]) == team and (list(game.values())[1]) =="Won":
          win_counter += 1
         #   win_counter = 0
      win_count.append(win_counter)

    return win_count


def get_games_played():
    game_count = []
    for team in teams:
      game_counter = 0
      for game in output_1:

        if (list(game.keys())[0]) == team:
          game_counter += 1
        elif (list(game.keys())[1]) == team:
          game_counter += 1
         #   win_counter = 0
      game_count.append(game_counter)

    return game_count

game_count = get_games_played()
print(game_count)
#get the winners and make a list of each respective draws ie
#team = teams = ['FC Awesome', 'Tarantulas', 'Grouches', 'Lions', 'Snakes']
#respectively for each team such as [1, 0, 0, 2, 1]
def get_drawers():


    draw_count = []
    for team in teams:
      draw_counter = 0
      for game in output_1:

        if (list(game.keys())[0]) == team and (list(game.values())[0]) =="Draw":
          draw_counter += 1
        elif (list(game.keys())[1]) == team and (list(game.values())[0]) =="Draw":
          draw_counter += 1

      draw_count.append(draw_counter)
    return draw_count

def get_losers():


    lose_count = []
    for team in teams:
      lose_counter = 0
      for game in output_1:

        if (list(game.keys())[0]) == team and (list(game.values())[0]) =="Lose":
          lose_counter += 1
        elif (list(game.keys())[1]) == team and (list(game.values())[0]) =="Lose":
          lose_counter += 1

      lose_count.append(lose_counter)
    return lose_count
def goals_scored():
    goals_scored_count = []
  #  goals_counter = 0

    for team in teams:
      goals_counter = 0

      for game in games:
        #goals_counter = 0
              #goals_counter = 0

        if (list(game.keys())[0]) == team:
            goals_scored = int(list(game.values())[0])
            goals_counter = goals_scored + goals_counter
        elif (list(game.keys())[1]) == team:
            goals_scored = int(list(game.values())[1])
            goals_counter = goals_counter + goals_scored
      goals_scored_count.append(goals_counter)
    return goals_scored_count


def goals_against():
    goals_against_count = []
  #  goals_counter = 0

    for team in teams:
      goals_against_counter = 0

      for game in games:
        #goals_counter = 0
              #goals_counter = 0

        if (list(game.keys())[0]) == team:
            goal_against = int(list(game.values())[1])
            goals_against_counter = goal_against + goals_against_counter
        elif (list(game.keys())[1]) == team:
            goal_against = int(list(game.values())[0])
            goals_against_counter = goal_against + goals_against_counter
      goals_against_count.append(goals_against_counter)
    return goals_against_count
goals_scored= goals_scored()

goals_against= goals_against()


lose_count = get_losers()
#in socer each point is worth 3 points so multiple the list
win_count = get_winners()
win_points = [i * 3 for i in win_count]#should be [0,6,3,0]

#draws are one point so need to alter list, just add draw_count to win_points to
#get total points per list
draws = get_drawers()
#draws + win_points

def total_pts():
  total_pts = []
  for i in range(0, len(draws)):
    total_pts.append(draws[i] + win_points[i])
  return total_pts

total_pts = total_pts()

#team = ['FC Awesome', 'Tarantulas', 'Grouches', 'Lions', 'Snakes']
#to do how dou associate each points per team with the list
#so Fc awesoeome has 3 points, tarantulas has four.. .getScores
#into a sorted likst such as [6,4,3,0,3] and then sort the team list


       #this doesnt work im trying to make the last rank be the next rank.. ie 4,5 should chnage to 4,4
print("goals_against")
print(goals_against)
print("goal_scored")
print(goals_scored)
goal_differential = [a - b for a, b in zip(goals_scored, goals_against)]
print("goal diff")
print(goal_differential)
print(teams)
#now sort the teams and their respective points_plural
total_pts, teams, goal_scored, goals_against, goal_differential, game_count = zip(*sorted(zip(total_pts, teams, goals_scored, goals_against, goal_differential, game_count),reverse=True))
points_plural = ["pt" if i == 1 else "pts" for i in total_pts]
total_pts = list(total_pts)


vars = [total_pts, teams, goal_scored, goals_against, goal_differential, game_count]
res = [list(ele) for ele in vars]

print(res)
goal_differential = list(goal_differential)
print("goal differ")
print(goal_differential)
def ranks():
    rank_list = []
    rank_count = 0
    for i in range(len(teams)):
      rank_count += 1
      rank_list.append(rank_count)
    return rank_list

rank = ranks()


rank = ranks()
#vars = list(zip(rank, teams, total_pts, points_plural, goals_scored, goals_against, goal_differential, game_count))
def ranker():
  current = 0
  for i in range(len(total_pts)-1):
    if (total_pts[i] == total_pts[i+1]) and (goal_differential[i] == goal_differential[i+1]):
        print("tie")
        current = rank[i]
        rank[i + 1] = current
    #elif (total_pts[i] == total_pts[i+1]) and (goal_differential[i] > goal_differential[i+1]):
        #rank = rank

    elif (total_pts[i] == total_pts[i+1]) and (goal_differential[i] < goal_differential[i+1]):
         return rank
         #for var in vars:
          # return rank

  return rank

print(res)
rank_1=ranker()
print(rank_1)
#and then sorted code
#print a ranking table based on each teams rank, team name, and points
import sys
print(list(zip(rank_1, teams, total_pts, points_plural, goals_scored, goals_against, goal_differential, game_count)))
#and then sorted code
#print a ranking table based on each teams rank, team name, and points
f = open("output.txt", "a")
for a,b,c,d,e,f,g,h in list(rank_1, teams, total_pts, points_plural, goals_scored, goals_against, goal_differential, game_count):
      #print(a,'. ', b,', ', c, ' ', d, " GP ", h,  " GF ", e, " GA ", f, " GD ", g, sep='')
      string = f"{a}. {b}  {c} {d}  gf {e}  ga {f}  gd  {g}  games played {h}"
      string_sort = sorted(string.split('\n'))
      print(string_sort)

#f.close()
