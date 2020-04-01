def display_board(board):
	print('\n'*100)
	print(board[1]+'|' + board[2] + '|' + board[3])
	print(board[4] + '|' + board[5] + '|' + board[6])
	print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():
	'''
	OUTPUT:(Player1,Player2)
	'''
	marker=''
	while (marker!='X') or (marker!='O'):
		marker=input('Please choose X or O').upper()
		break 

	if marker=='X':
		return ('X','O')
	else:
		return ('O','X')


def place_marker(board, marker, position):
	board[position]=marker

def win_check(board,mark):
#3 Rows, 3 Columns, 2 diagnols
	return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)  
		  
import random
def choose_first():
	flip = random.randint(0,1)

	if flip==0:
		return 'Player1'
	else:
		return 'Player2'

def space_check(board,position):
	return board[position]==' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	# IF BOARD IS FULL , WE RETURN TRUE
	return True

def player_choice(board):
	
	position=0
	while position not in {1,2,3,4,5,6,7,8,9} or not space_check(board,position):
		position=int(input('Please choose a number between 1-9'))

	return position

def replay():
		choice = input('Wanna play again? Say Yes or No')
		return choice == 'Yes'



#While Loop to keep the Game Running

print('Hey,Welcome to Tic-Tac-Toe')

while True:
	board=[' ']*10

	player1_marker,player2_marker=player_input()
	turn = choose_first()

	print(turn +  'will have the turn first' )

	play_game= input('Ready to play? Yes or No')

	if play_game=='Yes':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player1':
			display_board(board)
			position_check = player_choice(board)
			place_marker(board,player1_marker,position_check)
			
			if win_check(board,player1_marker):
				display_board(board)
				print('Bingo!Player1 has won')
				game_on=False
			else:
				if full_board_check(board):
					print('Oh Snap!Its a tie!!')
					game_on=False
				else:
					turn = 'Player2'


		if turn == 'Player2':
			display_board(board)
			position_check = player_choice(board)
			place_marker(board,player2_marker,position_check)
			
			if win_check(board,player2_marker):
				display_board(board)
				print('Bingo!Player2 has won')
				game_on=False
			else:
				if full_board_check(board):
					print('Oh Snap!Its a tie!!')
					game_on=False
				else:
					turn = 'Player1'			

	if not replay():
		break
