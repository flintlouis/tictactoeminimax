import math
from random import randint
from Game import next_player

states = 0

def get_states():
	print(states)

def random_move(game):
	while True:
		row, col = randint(0,2), randint(0,2)
		if game[row, col] == 0:
			return row, col

def minmax(game, depth, alpha, beta, maximizing_player, player):
	finished = game.is_finished()
	if not finished == None:
		return game.get_score(finished)
	if depth == 0:
		return 0
	global states
	if maximizing_player:
		max_eval = -math.inf
		for row in range(3):
			for col in range(3):
				if game[row, col] == 0:
					game[row, col] = player
					states += 1
					eval = minmax(game, depth - 1, alpha, beta, False, next_player(player))
					game[row, col] = 0
					max_eval = max(max_eval, eval)
					alpha = max(alpha, eval)
					if beta <= alpha:
						break
		return max_eval
	else:
		min_eval = +math.inf
		for row in range(3):
			for col in range(3):
				if game[row, col] == 0:
					game[row, col] = player
					states += 1
					eval = minmax(game, depth - 1, alpha, beta, True, next_player(player))
					game[row, col] = 0
					min_eval = min(min_eval, eval)
					beta = min(beta, eval)
					if beta <= alpha:
						break
		return min_eval
