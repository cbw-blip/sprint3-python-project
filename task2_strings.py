messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

game_name = video_game_sales[4][NAME]
print(game_name [0:7])
for name in messy_names:
    print(name.strip( ) .lower( ))
    game = video_game_sales[0]
print(f"#1 Best Seller: {game[NAME]} ({game[YEAR]}) - ${game[GLOBAL_SALES]}M global sales")

NAME = 1
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9
