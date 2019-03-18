from game import Game


def main():
    game = Game(9)
    game.print_board_help()
    playing = 'Y'

    while (playing == 'Y') | (playing == 'y'):
        game.print_score()
        in_progress = 0
        game.turn = game.first_pick()
        game.clear_board()
        while in_progress == 0:
            game.print_board()
            if game.turn == 0:
                print("Player X's Turn: \n")
                game.place_choice(game.player_x, game.get_choice())
                # check for win
                if game.check_if_win(game.player_x) == 1:
                    in_progress = 1
                    game.print_board()
                game.turn = 1
            else:  # turn = 1
                print("Player O's Turn: \n")
                game.place_choice(game.player_o, game.get_choice())
                # check for win
                if game.check_if_win(game.player_o) == 1:
                    in_progress = 1
                    game.print_board()
                game.turn = 0
        playing = input("Play again?(Y/N)\n")
    print("Thanks for playing!\n")

