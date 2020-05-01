class TicTacToe:
    def __init__(self):
        current_state = list(input("Enter cells: "))
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
            if self.current_state[i][0] == self.current_state[i][1] == self.current_state[i][2]:
                win_list.add(self.current_state[i][0])
            if self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i]:
                win_list.add(self.current_state[0][i])
        # check diagonals
        if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] or \
                self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0]:
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


game = TicTacToe()
game.show_table()
print(game.check_game_state())
