import numpy as np

def next_player(player):
	if player == 1:
		return 2
	else:
		return 1

class Game:
	def __init__(self):
		self.state = np.zeros((3,3), dtype=int)
	
	def get_score(self, winner):
		scores = {0:0, 1:1, 2:-1}
		return scores[winner]
	
	def is_finished(self):
		diag = self.state.diagonal()
		if np.all(diag == diag[0]) and diag[0] != 0:
			return diag[0]
		diag = np.fliplr(self.state).diagonal()
		if np.all(diag == diag[0]) and diag[0] != 0:
			return diag[0]
		for row in self.state:
			if np.all(row == row[0]) and row[0] != 0:
				return row[0]
		for row in self.state.transpose():
			if np.all(row == row[0]) and row[0] != 0:
				return row[0]
		if 0 in self.state:
			return None
		return 0

	def print_state(self):
		for j, row in enumerate(self.state):
			for i, piece in enumerate(row):
				if piece == 0:
					print(' ', end='')
				elif piece == 1:
					print('O', end='')
				else:
					print('X', end='')
				if i != 2:
					print('|', end='')
			if j != 2:
				print('\n-----')
		print()

	def __getitem__(self, index):
		row, col = index
		return self.state[row, col]

	def __setitem__(self, index, value):
		row, col = index
		self.state[row, col] = value
