import classes as c

player_one = c.Player("Player One", "O")
player_two = c.Player("Player Two", "X")
game = c.Game()
game.play(player_one, player_two)