total_games = len(video_game_sales)
print(total_games)
total_sales = 0
for game in video_game_sales:
    total_sales = total_sales + game[GLOBAL_SALES]
avg_global_sales= total_sales/total_games
print (f"Average: {avg_global_sales}")
top_game_share = video_game_sales[0][GLOBAL_SALES] / total_sales * 100
print(top_game_share)



NAME = 1
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9

