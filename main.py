from Game import Game
from minmax import minmax, negamax, random_move, randint, math, get_states
import numpy as np
import os

def main():
	game = Game()
	player = randint(-1, 1)
	os.system("clear")
	game.print_state()
	while True:
		if player == 1:
			best_score = -math.inf
			for place in game.get_empty_places():
				game[place] = player
				score = negamax(game, 10, -math.inf, math.inf, -player)
				# score = minmax(game, 10, -math.inf, math.inf, False, -player)
				game[place] = 0
				if score > best_score:
					best_score = score
					best_move = place
			game[best_move] = player
		else:
			row = int(input("row: "))
			col = int(input("col: "))
			if not game[row, col] == 0:
				continue
			game[row, col] = player
		player = -player
		os.system("clear")
		game.print_state()
		if 0 not in game.state or game.is_finished():
			winner = game.is_finished()
			if winner == 0:
				print("It's a tie")
			elif winner == 1:
				print("O is the winner!")
			else:
				print("X is the winner!")
			break

if __name__ == "__main__":
	main()
