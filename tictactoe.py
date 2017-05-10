"""
TicTacToe
--------------------------------------------------------------------------------------------

I plan for this program to be an automated TicTacToe game between the player and the computer
it will dispay a tictactoe grid, allow the player to pick where they want their X to go,
and the computer will place its O.
"""

# -------------------------------------------------------------------------------------------------------------------------


from random import *

player1 = []
player2 = []
board = [' '] * 10
turn = 3
comp = []
mode = "temp"
complete = 0

def check_board(board):
	""" Function the board to see if win conditions have been met, 
or if the game has ended with a draw. 
	"""
	
	global player1
	global player2
	global comp
	
	
	p1w = "Player 1 wins!"
	p2w = "Player 2 wins!"
	cpw = "Computer wins, sorry."
	cat = "It's a draw!"
	
	if "X" in player1 and won(board,"X") == True:
		print p1w
		replay()
		
	elif "X" in player2 and won(board,"X") == True:
		print p2w
		replay()
		
	elif "O" in player1 and won(board,"O") == True:
		print p1w
		replay()
		
	elif "O" in player2 and won(board,"O") == True:
		print p2w
		replay()
		
	elif "X" in comp and won(board, "X") == True:
		print cpw
		replay()
		
	elif "O" in comp and won(board, "O") == True:
		print cpw
		replay()
		
	elif (is_board_full(board) == True and won(board, "X") == False and won(board, "O") == False):
		print cat
		replay()
		
	else:
		move()
		
def compBoard(board):
	"""Function that copies game board to list for computer to base its decisions on
	"""
	
	compBoard = []
	for i in board:
		compBoard.append(i)
	return compBoard

def compmove(compBoard, letter, move):
	"""Function that preforms a theoretical move to coppied board to help the
computer make its decision.
	"""
	compBoard[move] = letter	

def comp_move(x):
	"""Function that determines the computers letter and preforms its move based
on its decision
	"""
	
	global comp
	global board
	global mode
	
	if "X" in comp:
		board[x] = "X"
		drawBoard(board)
		check_board(board)
	else:
		board[x] = "O"
		drawBoard(board)
		check_board(board)
		
def computer(board):
	"""Function that brings all the parts to the computer's decision making and
movement together. So the "Computer"
	"""
	global comp
	global player1
	global turn
	
	if is_board_full(board) == True:	
		check_board(board)
		
	else:
		pass
		
	if "X" in player1:
		comp = ["O"]
		letter = "O"
		pletter = "X"
	else:
		comp = ["X"]
		letter = "X"
		pletter = "O"
			
	for i in range(1, 10):
		copyboard = compBoard(board)
		if is_space_available(copyboard, i):
			compmove(copyboard,letter,i)
			if won(copyboard,letter):
				return i
				
				
	for i in range(1, 10):
		copyboard = compBoard(board)
		if is_space_available(copyboard, i):
			compmove(copyboard,pletter,i)
			if won(copyboard,pletter):
				return i
				
		
	cmove = get_random_choice(board, [1,3,7,9])
	if cmove != None:
		return cmove
		
	elif is_space_available(board, 5):
		return 5
	
	else:
		return get_random_choice(board, [2,4,6,8])
	
def drawBoard(board):
	"""Function that prings the board and moves
	"""
	
	print ("\t" + board[1] + " | " + board[2] + " | " + board[3])
	print ("\t" + "-" * 9)
	print ("\t" + board[4] + " | " + board[5] + " | " + board[6])
	print ("\t" + "-" * 9)
	print ("\t" + board[7] + " | " + board[8] + " | " + board[9])
	
def first(n):
	"""Function that stores the order of the players.
	"""
	global turn
	global mode
	
	if mode == False:
		if n == 1:
			turn = 0
			
		elif n == 0:
			turn = 1
			
		else:
			print "Please select 1 or 0 for your selection"
			n = int(raw_input("> "))
			first(n)
	else:
		if n == 1:
			turn = 0
			
		elif n == 0:
			turn = 1
			
		else:
			print "Please select 1 or 0 for your selection"
			n = int(raw_input("> "))
			first(n)

def game_mode(n):
	"""Function that determines if it's a single or multiplayer game.
	"""
	global mode
	if n == 1:
		mode = False
		
	elif n == 0:
		mode = True
		
	else:
		"Please type 1 or 0 for your selection."
		n = int(raw_input("> "))
		game_mode(n)

def get_random_choice(board, nums):
	"""Function that returns a random selection from list for computer to move.
	"""
	possible_moves = []
	for i in nums:
		if is_space_available(board, i):
			possible_moves.append(i)
			
	if len(possible_moves) != 0:
		return choice(possible_moves)
	else:
		return None

def is_board_full(b):
	"""Function that determines if all available moves have been exhausted
	"""
	
	max = 0
	for i in range(1,10):
		if b[i] != ' ':
			max += 1
		else:
			pass
	
	if max == 9:
		return True
		
	else:
		return False

def is_space_available(board,location):
	"""Function that determines if a move is possible for the computer to help its 
decision making.
	"""
	return board[location] == ' '
		
def key():
	"""The board key, displays corresponding board locations with numbers.
	"""
	
	print ("\t" + "1" + " | " + "2" + " | " + "3" + " ")
	print ("\t" + "-" * 9)
	print ("\t" + "4" + " | " + "5" + " | " + "6" + " ")
	print ("\t" + "-" * 9)
	print ("\t" + "7" + " | " + "8" + " | " + "9" + " ")	

def move():
	"""Function that preforms takes player's move and adds it to the board,
also swaps between the player's turns
	"""
	
	global player1
	global player2
	global turn
	global board
	global mode
	if is_board_full(board) == True:
		check_board(board)
		
	else:
		pass
	
	if turn == 0:
		try:
			location = int(raw_input("> "))
			test_move(board, location)
			if "X" in player1 and location in range(1,10):
				board[location] = "X"
				print drawBoard(board)
				turn += 1
				check_board(board)
			elif "O" in player1 and location in range(1,10):
				board[location] = "O"
				turn += 1
				print drawBoard(board)
				check_board(board)
			
		
			elif location == "key":
				key()
				move()
		
			else:
				print """please type a choose a number between 1 and 9, remember typing "key"
will bring up the key for the board."""
				move()
			
		except ValueError:
			print "Please type a value between 1 and 9, type key for the board key"
			move()
	
	elif turn == 1 and mode == False:
		turn -= 1
		comp_move(computer(board))
		check_board(board)
	
	else:
		try:
		
			location = int(raw_input("> "))
			test_move(board, location)
			if "X" in player2 and location in range(1,10):
				board[location] = "X"
				turn -= 1
				drawBoard(board)
				check_board(board)
						
			elif "O" in player2 and location in range(1,10):
				board[location] = "O"
				turn -= 1
				drawBoard(board)
				check_board(board)
			
			elif location == "key":
				key()
				move()
			
			else:
				print """please type a choose a number between 1 and 9, remember typing "key"
will bring up the key for the board."""
			move()
		
		except ValueError:
			print "Please type a value between 1 and 9, type key for the board key"
			move()
			
def move_forward(x):
	global complete
	
	complete = x
	start()
			
def quit():
	"""Function to end the game"""
	print "thanks for playing"
	
			
def replay():
	"""Function determines if players want to play again and if they'd like to keep
the same settings.
	"""
	global board
	
	print "Would you like to play again?"
	print "1 : Yes"
	print "0 : No"
	
	confirm1 = int(raw_input("> "))
	if confirm1 == 1:
		
		board = [" "] * 10
		
		print "Would you like to change your settings? (your letter, multiplayer or not)"
		print "1 : Yes"
		print "0 : No"
		
		confirm2 = int(raw_input("> "))
		
		if confirm2 == 1:
			reset()
			start()
		
		else:
			drawBoard(board)
			move()
		
	else:	
		quit()
		exit()
def reset():
	"""This function resets all settings to restart the game with new rules.
	"""

	global player1 
	global player2
	global board 
	global turn 
	global comp 
	global mode 
	global complete
	
	player1 = []
	player2 = []
	board = [' '] * 10
	turn = 3
	comp = []
	mode = "temp"
	complete = 0
	
		
def select_xo(n):
	"""Function that allows the player or players to select their letter.
	"""
	
	global mode
	global player1
	global player2
	global comp
	if mode == False:
		if n == 1:
			player1.append("X")
			comp.append("O")
			
		elif n == 0:
			player1.append("O")
			comp.append("X")
			
		else: 
			print "Please select 1 or 0"
			n = int(raw_input("> "))
			select_xo(n)
			
	else:
		if n == 1:
			player1.append("X")
			player2.append("O")
			
			
		elif n == 0:
			player1.append("O")
			player2.append("X")
			
		else:
			print "Please select 1 or 0"
			n = int(raw_input("> "))
			select_xo(n)
										
def start():
	"""Function that starts the whole game, and ties the setting functions together.
	"""
	
	global player1 
	global player2
	global board 
	global turn 
	global comp 
	global mode 
	global complete
	
	
	while complete == 0:
		print """Welcome to TicTacToe! The rules are simple, it's tictactoe just you select where
you would like to put your letter by selecting the corresponding number to a location (the
key to the board is displayed above.) First, will you be playing alone against our computer,
or will you be playing with a friend?
"""
		
		print "Type \"1\" if you would like to play against the computer."
		print "Type \"0\" if you would like to play with a friend."
	
		try:
			a1 = int(raw_input("> "))
			game_mode(a1)
	
		except ValueError:
			print "Please type a \"1\" or a \"0\""
	
		if mode == True:
			print "Alright, have fun playing with your friend!"
			move_forward(1)
		
		elif mode == False:
			print "Ok, the computer can be tricky though."
			move_forward(1)
		
		else:
			pass
	
	while complete == 1:
	
		print "Ok, now would you (player 1) like to be X's or O's?"
		print "Type \"1\" if you would like to be X's and \"0\" if you'd \
like to be O's"
	
		try:
			a2 = int(raw_input("> "))
			select_xo(a2)
		
		except ValueError:
			print "Please type a \"1\" or a \"0\""
		
		if "X" in player1:
			print "Ok, player1 is X"
			move_forward(2)
		
		elif "O" in player1:
			print "Ok, player1 is O"
			move_forward(2)
		
		else:
			pass
		
	while complete == 2:
		print "Lastly, would you (player1) like to go first, or second?"
		print "Type \"1\" to go first or \"0\" to go second."
	
		try:
			a3 = int(raw_input("> "))
			first(a3)
		
		except ValueError:
			print "Please type \"1\" or \"0\""
		
		if turn == 0:
			print "player1 is first, have fun!"
			complete = "done"
			move()
		
		elif turn == 1:
			print "player1 will go second, have fun!"
			complete = "done"
			move()
		
		else:
			pass
		
		
				
def test_move(board, location):
	"""Function test player's move choice and informs them if their choice is already taken.
	"""

	global mode
	if location in range(1,10) and board[location] == ' ':
		pass
	elif location in range(1, 10) and board[location] != ' ':
		print """%i is already taken, please choose another location, remember type \'key\' to see what numbers
correspond to each location""" % location
		move()
	else:
		print """Please select a number between 1 and 9, remember type 'key' to see what numbers correspond to
each location"""
		move()

def won(bl, pl):
	"""Function that determines if anyone won.
	"""
	return ((bl[1] == pl and bl[2] == pl and bl[3] == pl) or #Top  
	(bl[4] == pl and bl[5] == pl and bl[6] == pl) or   #Middle
	(bl[7] == pl and bl[8] == pl and bl[9] == pl) or  #Bottom
	(bl[1] == pl and bl[4] == pl and bl[7] == pl) or  #Left
	(bl[2] == pl and bl[5] == pl and bl[8] == pl) or  #Center
	(bl[3] == pl and bl[6] == pl and bl[9] == pl) or  #Right
	(bl[1] == pl and bl[5] == pl and bl[9] == pl) or  #Diagnal Right
	(bl[3] == pl and bl[5] == pl and bl[7] == pl))  #Diagnal Left
			
# ---------------------------------------------------------------------------------------------------------


key()
start()


	
