pre_2000_count = 0        

for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(game[NAME], game[GLOBAL_SALES])

for game in video_game_sales: 
    if game[YEAR] < 2000:
        pre_2000_count += 1
print(pre_2000_count)

total_na= 0 
total_jp=0

for game in video_game_sales:
     total_na += game[NA_SALES]
     total_jp += game[JP_SALES]
if total_na > total_jp:
    print("North America had higher sales.")
elif total_jp > total_na:
    print("Japan had higher sales.")
else:
    print("Both regions had equal sales.")
print (total_na, total_jp)

nintendo_games = []

for game in video_game_sales:
    if game[PUBLISHER] == "Nintendo":
       nintendo_games.append(game[NAME])
print (nintendo_games)
print( len(nintendo_games))

NAME = 1
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9
