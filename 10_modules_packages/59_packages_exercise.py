from games import word_game as wordgame, game_of_life as gol

# task create a menu that allow use to pick game to play

def main():
    all_games = {
        "Game of Life": gol.main,
        "Word Game": wordgame.main
    }
    
    for i, game in enumerate(all_games.keys()):
        print(f' {i+1}. {game}')
        
    user_input = input(f"Pick between 1 - {len(all_games.keys())}: ")
    
    if not user_input.isnumeric():
        print("Invalid option.")
        return
    
    user_input = int(user_input)
    
    if user_input > 0 and user_input <= len(all_games.keys()):
        key = ""
        for i, game in enumerate(all_games.keys()):
            if i == user_input - 1:
                key = game
            
        # print(key)
        all_games[key]()
    else:
        print("Invalid option.")
        return
    



if __name__ == '__main__':
    main()