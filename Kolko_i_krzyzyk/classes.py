class Move(object):
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

class Player(object):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_move(self):
        while True:
            x, y = map(int, input(f"{self.name} ruch:\nPodaj wspolrzedne ruchu:").split())
            if x >= 3 or y >= 3 or x <0 or y < 0:
                print("Podales zle wspolrzedne, sprobuj ponownie") 
            else:
                return Move(x,y, self.sign)

class Board(object):
    def __init__(self):
        self.board = [[' ',' ',' '] for i in range(3)]

    def __str__(self):
        rows = ['   0   1   2']
        for i, row in enumerate(self.board):
            rows.append(f"{i}  {' | '.join(row)}")
            if i < 2:
                rows.append("  -----------")
        return '\n'.join(rows)

    def get_state(self):
        print(self)
    
    def get_field(self, x, y):
        return self.board[x][y]

    def set_field(self, move):
        self.board[move.x][move.y] = move.sign

class Game(object):
    def __init__(self):
        self.board = Board()

    def play(self, player_one, player_two):
        players = [player_one, player_two]
        current_player = 0
        moves = 0

        while(self.is_next_move_possible() and moves < 9):
            self.board.get_state()
            move = players[current_player].get_move()
            if self.board.get_field(move.x, move.y) == ' ':
                self.board.set_field(move)
                current_player += 1
                current_player %= 2
                moves += 1
            else:
                print("Wybrane pole jest zajete. Sprobuj ponownie.")
            
        if moves == 9:
            print("REMIS!")
        self.game_over()


    def game_over(self):
        print("Koniec gry")

    def is_next_move_possible(self):
        for sign in ['X', 'O']:
            for row in self.board.board:
                if all(s == sign for s in row):
                    print(f"KONIEC! Wygrywa gracz [{sign}] !")
                    return False
            
        for col in range(3):
            if all(self.board.board[row][col] == sign for row in range(3)):
                print("KONIEC! Wygrywa " + sign)
                return False
            
        if all(self.board.board[i][i] == sign for i in range(3)):
            print("KONIEC! Wygrywa " + sign)
            return False
        
        if all(self.board.board[i][2 - i] == sign for i in range(3)):
            print("KONIEC! Wygrywa " + sign)
            return False
        return True
        
