class TicTacToe:

    def __init__(self):
        self.current_player = 'X'
        # current_state = list(input("Enter cells: ").replace('_', ' '))
        current_state = list(" " * 9)
        self.current_state = [current_state[0:3], current_state[3:6], current_state[6:9]]

    def show_table(self):
        print("-" * 9)
        for y in range(3):
            print("| " + " ".join(self.current_state[y]) + " |")
        print("-" * 9)

    def check_game_state(self):
        win_list = set()
        # check count of X and O
        count_x = len([x for rows in self.current_state for x in rows if x == 'X'])
        count_o = len([o for rows in self.current_state for o in rows if o == 'O'])
        count__ = 9 - count_o - count_x
        # check horizontal and vertical lines
        for i in range(3):
            if self.current_state[i][0] == self.current_state[i][1] == self.current_state[i][2] == 'X' or \
                    self.current_state[i][0] == self.current_state[i][1] == self.current_state[i][2] == 'O':
                win_list.add(self.current_state[i][0])
            if self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i] == 'X' or \
                    self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i] == 'O':
                win_list.add(self.current_state[0][i])
        # check diagonals
        if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] == 'X' or \
                self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] == 'O' or \
                self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0] == 'X' or \
                self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0] == 'O':
            win_list.add(self.current_state[1][1])
        # difference > 1 or both side wins
        if abs(count_x - count_o) > 1 or len(win_list) > 1:
            return "Impossible"
        # only 1 winner
        elif len(set(win_list)) == 1:
            return f"{list(win_list)[0]} wins"
        # game not ended
        elif count__ > 0:
            return "Game not finished"
        # no free space and nobody wins
        return "Draw"

    def next_move(self):
        coords = ''.join(input("Enter the coordinates: ").split())
        if not coords.isdigit() or len(coords) != 2:
            print("You should enter numbers!")
            return False
        self.coord_x, self.coord_y = int(coords[0]) - 1, 3 - int(coords[1])
        if self.coord_x > 2 or self.coord_y > 2 or \
                self.coord_x < 0 or self.coord_y < 0:
            print("Coordinates should be from 1 to 3!")
            return False
        if self.check_coord():
            self.current_state[self.coord_y][self.coord_x] = self.current_player
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False

    def check_coord(self):
        if ' ' not in self.current_state[self.coord_y][self.coord_x]:
            return False
        return True

    def change_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def game(self):
        game.show_table()
        game_ = True
        while game_:
            game_state = self.check_game_state()
            if game_state.endswith('wins') or game_state == 'Draw':
                game_ = False
                print(game_state)
                continue
            next_player = True
            while next_player:
                next_player = not game.next_move()
            game.show_table()
            self.change_player()


game = TicTacToe()
game.game()
