game_names = []
for game in video_game_sales:
    game_names.append(game[NAME])
print(game_names)

video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

dataset_info = (len(video_game_sales), 10, 'Video Game Sales')
print (dataset_info)

NAME = 1
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9
