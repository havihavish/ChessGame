class game_board:
	def __init__(self):

		self.board = []

		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
		self.board.append(['bl', 'bl', 'bl', 'bl', 'bl', 'bl', 'bl', 'bl'])
		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])
		self.board.append(['wh', 'wh', 'wh', 'wh', 'wh', 'wh', 'wh', 'wh'])
		self.board.append(['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'])

	def update_board(self, move):
		x,y = move[0], move[1]
		nx,ny = move[2], move[3]
		pos = self.board[x][y]
		self.board[x][y] = 'e'
		self.board[nx][ny] = pos

	def print_board(self):
		print("  *----*----*----*----*----*----*----*----* ")
		index = 1
		row_s = ""
		for row in self.board:
			row_s = str(index) + " |"
			for i in row:
				if i == 'bl': row_s += ' BL '
				if i == 'wh': row_s += ' WH '
				if i == 'e': row_s += '    '
				row_s += "| "
				row_s = row_s[:-1]
			print(row_s)
			index += 1
			print("  *----*----*----*----*----*----*----*----* ")
		print("     a    b    c    d    e    f    g    h \n")



