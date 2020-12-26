import board
import collections

stop_loop = False

# Init the board
game_board = board.game_board()

# Initial Kill dictionary for both the pawns
kill_w = collections.defaultdict(list)
kill_b = collections.defaultdict(list)

# Move dictionary for both pawns which contains the key as the
# current pawn position and value as the front directions move

move_w = collections.defaultdict(list)
move_b = collections.defaultdict(list)

arr_idx = {}

# Storing Board Column coordinates in dictionary
arr_idx['a'] = 0
arr_idx['b'] = 1
arr_idx['c'] = 2
arr_idx['d'] = 3
arr_idx['e'] = 4
arr_idx['f'] = 5
arr_idx['g'] = 6
arr_idx['h'] = 7

# Storing Board Row coordinates in dictionary
arr_idx['1'] = 0
arr_idx['2'] = 1
arr_idx['3'] = 2
arr_idx['4'] = 3
arr_idx['5'] = 4
arr_idx['6'] = 5
arr_idx['7'] = 6
arr_idx['8'] = 7

# Storing initial Black pawn positions
move_b['a2'] = ['a3']
move_b['b2'] = ['b3']
move_b['c2'] = ['c3']
move_b['d2'] = ['d3']
move_b['e2'] = ['e3']
move_b['f2'] = ['f3']
move_b['g2'] = ['g3']
move_b['h2'] = ['h3']

# Storing initial White pawn positions
move_w['a7'] = ['a6']
move_w['b7'] = ['b6']
move_w['c7'] = ['c6']
move_w['d7'] = ['d6']
move_w['e7'] = ['e6']
move_w['f7'] = ['f6']
move_w['g7'] = ['g6']
move_w['h7'] = ['h6']

# Checking the black pawn present in the diagonals of the white pawn
def check_white_diagonals(dest):
	l = ""
	if ord('a') <= ord(dest[0]) - 1 <= ord('h'):
		l = str(chr(ord(dest[0]) - 1)) + str(int(dest[1]) - 1)
	r = ""
	if ord('a') <= ord(dest[0]) + 1 <= ord('h'):
		r = str(chr(ord(dest[0]) + 1)) + str(int(dest[1]) - 1)
	if len(l) > 0 and l in move_b:
		kill_b[l] = dest
	if len(r) > 0 and r in move_b:
		kill_b[r] = dest

# Checking the white pawns present in the diagonals of the black pawn
def check_black_diagonals(dest):
	l = ""
	if ord('a') <= ord(dest[0]) - 1 <= ord('h'):
		l = str(chr(ord(dest[0]) - 1)) + str(int(dest[1]) + 1)
	r = ""
	if ord('a') <= ord(dest[0]) + 1 <= ord('h'):
		r = str(chr(ord(dest[0]) + 1)) + str(int(dest[1]) + 1)
	if len(l) > 0 and l in move_w:
		kill_w[l] = dest
	if len(r) > 0 and r in move_w:
		kill_w[r] = dest

def check_white_victory(dest):
	if '1' in dest:
		print("\n*---------------White victory-------------*")
		return True

def check_black_victory(dest):
	if '8' in dest:
		print("\n*---------------Black victory-------------*")
		return True

def update_board_idx(src,dest):
	x1 = arr_idx[src[1]]
	y1 = arr_idx[src[0]]

	x2 = arr_idx[dest[1]]
	y2 = arr_idx[dest[0]]
	move = [x1, y1, x2, y2]
	game_board.update_board(move)

# Writing all the functionalities and moves for White pawn
def get_white_move():

	used_set = set()
	can_move = True
	while can_move:

		print("Player 1's (WHITE) move")
		print("Eg :a7 a6")
		choice = input(">").lower()
		lst = choice.split(" ")
		if len(lst) != 2:
			print("Please enter valid input")
			continue
		src,dest = lst[0],lst[1]

		if len(kill_w) == 0 and (src not in used_set) and (src in move_w) and (dest not in move_w) and (dest not in move_b) and (dest in move_w[src]) :

			new_dest = dest[0]+str(int(dest[1])-1)
			move_w[dest].append(new_dest)
			del move_w[src]
			update_board_idx(src,dest)
			if check_white_victory(dest): return True
			check_white_diagonals(dest)
			break

		elif(len(kill_w) != 0 and (src not in used_set) and (src in kill_w) and (dest in kill_w[src]) ) :

			used_set.add(dest)
			del kill_w[src]
			del move_w[src]
			del move_b[dest]

			new_dest = dest[0] + str(int(dest[1]) - 1)
			move_w[dest].append(new_dest)
			update_board_idx(src, dest)
			if check_white_victory(dest): return True
			check_white_diagonals(dest)

			temp = ""
			for key in kill_w:
				if dest in kill_w[key]:
					temp = key
					break
			if len(temp)>0:
				del kill_w[temp]

			game_board.print_board()
		else:
			print("Please enter valid move")
		if len(used_set) == len(move_w):
			print("\n*---------------Black victory-------------*")
			return True
	return False

# Writing all the functionalities and moves for Black pawn
def get_black_move():

	used_set = set()
	can_move = True
	while can_move:

		print("Player 2's (BLACK) move")
		print("Eg :b2 b3")
		choice = input(">").lower()
		lst = choice.split(" ")
		if len(lst) != 2:
			print("Please enter valid input ex: a6 a7")
			continue
		src,dest = lst[0],lst[1]

		if len(kill_b) == 0 and (src not in used_set) and (src in move_b) and (dest not in move_w) and (dest not in move_b) and (dest in move_b[src]) :

			new_dest = dest[0]+str(int(dest[1])+1)
			move_b[dest].append(new_dest)
			update_board_idx(src, dest)

			del move_b[src]
			if check_black_victory(dest): return True
			# Checking diagonals
			check_black_diagonals(dest)
			break

		elif (len(kill_b) != 0 and (src not in used_set) and (src in kill_b) and (dest in kill_b[src]) ):

			used_set.add(dest)
			del kill_b[src]
			del move_b[src]
			del move_w[dest]

			new_dest = dest[0] + str(int(dest[1]) + 1)
			move_b[dest].append(new_dest)
			update_board_idx(src, dest)

			if check_black_victory(dest): return True

			# Check diagonals
			check_black_diagonals(dest)
			temp = ""
			for key in kill_b:
				if dest in kill_b[key]:
					temp = key
					break
			if len(temp)>0:
				del kill_b[temp]

			game_board.print_board()
		else:
			print("Please enter valid move")
		if len(used_set) == len(move_b):
			print("\n*---------------White victory-------------*")
			return True

	return False

# Program starts from here and the loop breaks if any player wins
print("\n*-----Player 1 moves white pawns ---- Player 2 moves black pawns------*\n")
while(stop_loop == False):

	game_board.print_board()
	stop_loop = get_white_move()
	if stop_loop == False:
		game_board.print_board()
		stop_loop = get_black_move()

print("Final board: ")
game_board.print_board()
