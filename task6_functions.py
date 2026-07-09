def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
print (calculate_total_sales(video_game_sales[0]))

def filter_by_genre(data,genre='Platform'):
    result=[]
    for game in data:
        if game[GENRE] == genre:
              result.append(game)
    return result

def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"
for game in video_game_sales:
    print(get_summary(game))
