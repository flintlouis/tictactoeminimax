import math
from os import stat
from random import randint

states = 0

def get_states():
	print(states)

def random_move(game):
	while True:
		row, col = randint(0,2), randint(0,2)
		if game[row, col] == 0:
			return row, col

def minmax(game, depth, alpha, beta, maximizing_player, player):
	global states
	score = game.is_finished()
	if not score == None:
		states += 1
		return score
	if depth == 0:
		return 0
	if maximizing_player:
		max_eval = -math.inf
		for place in game.get_empty_places():
			game[place] = player
			eval = minmax(game, depth - 1, alpha, beta, False, -player)
			game[place] = 0
			max_eval = max(max_eval, eval)
			alpha = max(alpha, eval)
			if beta <= alpha:
				break
		return max_eval
	else:
		min_eval = +math.inf
		for place in game.get_empty_places():
			game[place] = player
			states += 1
			eval = minmax(game, depth - 1, alpha, beta, True, -player)
			game[place] = 0
			min_eval = min(min_eval, eval)
			beta = min(beta, eval)
			if beta <= alpha:
				break
		return min_eval

def negamax(game, depth, alpha, beta, player):
	score = game.is_finished()
	if not score == None:
		return player * score
	if depth == 0:
		return 0
	value = -math.inf
	for place in game.get_empty_places():
		game[place] = player
		value = max(value, negamax(game, depth - 1, -beta, -alpha, -player))
		game[place] = 0
		alpha = max(alpha, value)
		if alpha >= beta:
			break
	return -value
