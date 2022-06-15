# Code Walkthrough:
# 1. In the main(), we create the board from the diagonal size inputted by the user,
#    and set the user input as X or O.
# 2. The diagonal size n is used to create a set of all the possible victory
#    condition combinations (row, column, diagonal; a total of 2n+2 combos) in the
#    method createWinCases(). Every move is saved as a set of matrix indices for 
#    their corresponding position on the board. Thus 00 is the upper-left corner
#    (0th row, 0th column) and (n-1)(n-1) is the lower-right corner. The counting
#    of these indices start from 0 and go till n-1 for obvious reasons. The method
#    returns a set of all the possible winCases.
# 3. The user input choice is used to create a list of players, which is then used
#    to put the input on the board.
# 4. The board, players, n, and winCases are sent to the playerX() or playerO()
#    depending upon the player's choice in the main(), where the game is played.
# 5. After the first move by the player and the computer, the game runs within a
#    while loop, going on until a result (victory, loss, draw) is reached.
# 6. The moves are saved by the methods setPlayerMoves() and setOppnMoves(). After
#    setting each move, it is saved as a set of all the move combinations made thus
#    far.
# 7. After every move, the board is sent to the printBoard() method for printing the
#    board.

import random

# This is to create a set of victory cases based on the size of the board.
# Contains all the rows, columns, and the two diagonals.
def createWinCases(n):
	winCase = set()
	winCases = list()
	count = 0

	# For rows.
	for i in range(0, n):
		for j in range(0, n):
			winCase.add(str(i) + str(j))
			count = count + 1

			if (count == n):
				break

		winCases.append(winCase)
		winCase = set()

	i = j = 0

	# For columns.
	for i in range(0, n):
		for j in range(0, n):
			winCase.add(str(j) + str(i))
			count = count + 1

			if (count == n):
				break

		winCases.append(winCase)
		winCase = set()

	i = 0

	# For leading diagonal.
	for i in range(0, n):
		winCase.add(str(i) + str(i))

	winCases.append(winCase)
	winCase = set()

	i = j = count = 0

	# For backward diagonal.
	for i in range((n-1), -1, -1):
		for j in range(0, n):
			if (count == j):
				winCase.add(str(i) + str(j))
				count = count + 1
				break

	winCases.append(winCase)
	winCase = set()
	# print(winCases)

	return winCases

# |---------------------------------------------------------------------------------|
# That's where the player's choice of whether they want cross or nought is fixed.
def start(choice):
	players = dict()
	
	if (choice == 'x' or choice == 'X'):
		players["Human"] = "X"
		players["Computer"] = "O"

	elif (choice == 'o' or choice == 'O'):
		players["Human"] = "O"
		players["Computer"] = "X"

	else:
		print("Aise karoge ab? Maine nahi khelna.")
		input()
		exit()

	return players

# |---------------------------------------------------------------------------------|
# Defines the game procedure should the player choose cross.
def playerX(players, board, n, winCases):
	moveCount = 2
	playerMoveSet = set()
	oppnMoveSet = set()
	
	playerMoveSet.add(setPlayerMove(players, board, n))
	# print("Player's Moveset: ", playerMoveSet)

	oppnMoveSet.add(setOppnMove(players, board, n))
	# print("Computer's Moveset:", oppnMoveSet)

	# print("Current Board: ", board)
	
	for case in winCases:
		isSubsetPlayer = case <= playerMoveSet
		isSubsetOppn = case <= oppnMoveSet
		if isSubsetPlayer or isSubsetOppn:
			# print(playerMoveSet, oppnMoveSet)
			break

	# This while loop is to run the game till an outcome is reached.
	while (not isSubsetPlayer) and (not isSubsetOppn):
		playerMoveSet.add(setPlayerMove(players, board, n))
		# print("Player's Moveset: ", playerMoveSet)

		oppnMoveSet.add(setOppnMove(players, board, n))
		# print("Computer's Moveset: ", oppnMoveSet)

		# print("Current Board: ", board)

		moveCount = moveCount + 2

		if moveCount == n*n:
			print("\n\nMatch drawn. Hoomanity and machine at stalemate.")
			return

		for case in winCases:
			isSubsetPlayer = case <= playerMoveSet
			isSubsetOppn = case <= oppnMoveSet
			if isSubsetPlayer or isSubsetOppn:
				# print(playerMoveSet, oppnMoveSet)
				break
	
	# Check whose moveset has an intersection with the winCases set, to decide the winner.
	if (isSubsetPlayer):
		print("\n\nHooman won! Take that, machine!")
	elif (isSubsetOppn):
		print("\n\nOh no, the machine won. Hoomanity is doomed!")

# |---------------------------------------------------------------------------------|
# Defines the game procedure should the player choose nought.
def playerO(players, board, n, winCases):
	moveCount = 2
	playerMoveSet = set()
	oppnMoveSet = set()

	oppnMoveSet.add(setOppnMove(players, board, n))
	# print("Computer's Moveset:", oppnMoveSet)

	playerMoveSet.add(setPlayerMove(players, board, n))
	# print("Player's Moveset: ", playerMoveSet)

	# print("Current Board: ", board)

	for case in winCases:
		isSubsetOppn = case <= oppnMoveSet
		isSubsetPlayer = case <= playerMoveSet
		if isSubsetOppn or isSubsetPlayer:
			# print(playerMoveSet, oppnMoveSet)
			break

	# This while loop is to run the game till an outcome is reached.
	while (not isSubsetOppn) and (not isSubsetPlayer):
		oppnMoveSet.add(setOppnMove(players, board, n))
		# print("Computer's Moveset: ", oppnMoveSet)

		playerMoveSet.add(setPlayerMove(players, board, n))
		# print("Player's Moveset: ", playerMoveSet)

		# print("Current Board: ", board)

		moveCount = moveCount + 2

		if moveCount == n*n:
			print("\n\nMatch drawn. Hoomanity and machine at stalemate.")
			return

		for case in winCases:
			isSubsetOppn = case <= oppnMoveSet
			isSubsetPlayer = case <= playerMoveSet
			if isSubsetOppn or isSubsetPlayer:
				# print(playerMoveSet, oppnMoveSet)
				break
	
	# Check whose moveset has an intersection with the winCases set, to decide the winner.
	if (isSubsetPlayer):
		print("\n\nHooman won! Take that, machine!")
	elif (isSubsetOppn):
		print("\n\nOh no, the machine won. Hoomanity is doomed!")

# |---------------------------------------------------------------------------------|
# Lets the player make a move.
def setPlayerMove(players, board, n):
	playerMoveStr = str()
	size = n * n

	refBoard(n)

	print("\nEnter the position where you want to make your move. Enter something between 1 and", size, end=".\n")
	playerMove = int(input("Enter your choice: "))
	playerMove = playerMove - 1
	
	while (playerMove not in range(0, size)):
		print("Aise nahi karte bhai. Phir se try karo.")
		playerMove = int(input("Enter your choice: "))
		playerMove = playerMove - 1

	while (board[playerMove] is players["Human"] or board[playerMove] is players["Computer"]):
		print("Position already taken. Try a different position.")
		playerMove = int(input("Enter your choice: "))
		playerMove = playerMove - 1

	board.pop(playerMove)
	board.insert(playerMove, players["Human"])
	printBoard(board, n)

	row = int(playerMove/n)
	column = (0 if playerMove%n == 0 else ((playerMove%n)))
	playerMoveStr = str(row) + str(column)

	return playerMoveStr

# |---------------------------------------------------------------------------------|
# Defines how the computer-controlled opponent will make a move.
def setOppnMove(players, board, n):
	oppnMoveStr = str()
	oppnMove = random.randint(0, (n*n - 1))

	while (board[oppnMove] is players["Human"] or board[oppnMove] is players["Computer"]):
		oppnMove = random.randint(0, (n*n - 1))
	
	board.pop(oppnMove)
	board.insert(oppnMove, players["Computer"])
	printBoard(board, n)

	row = int(oppnMove/n)
	column = (0 if oppnMove%n == 0 else ((oppnMove%n)))
	oppnMoveStr = str(row) + str(column)

	return oppnMoveStr

# |---------------------------------------------------------------------------------|
# To print a reference board to aid the player. Works till n=31.
def refBoard(n):
	size = n*n
	for i in range(0, n):
		print("|-----", end="")
	print("|")

	count = 0
	pos = str()

	if size <= 9:
		for i in range(1, 10):
			count = count + 1
			pos = '00' + str(count)
			print("|", pos, "", end="")
			
			if i%n == 0:
				print("|\n", end="")
				
				for j in range(0, n):
					print("|-----", end="")
				print("|")

	elif size > 9 and size <= 99:
		for i in range(1, 10):
			count = count + 1
			pos = '00' + str(count)
			print("|", pos, "", end="")
			
			if i%n == 0:
				print("|\n", end="")
				
				for j in range(0, n):
					print("|-----", end="")
				print("|")

			if count > 9:
				break
	
		for i in range(10, 100):
			count = count + 1
			pos = '0' + str(count)
			print("|", pos, "", end="")
			
			if i%n == 0:
				print("|\n", end="")
				for j in range(0, n):
					print("|-----", end="")
				print("|")
			
			if count >= size:
				break

	elif size >= 100:
		for i in range(1, 10):
			count = count + 1
			pos = '00' + str(count)
			print("|", pos, "", end="")
			
			if i%n == 0:
				print("|\n", end="")
				for j in range(0, n):
					print("|-----", end="")
				print("|")

			if count > 9:
				break
	
		for i in range(10, 100):
			count = count + 1
			pos = '0' + str(count)
			print("|", pos, "", end="")
			
			if i%n == 0:
				print("|\n", end="")
				for j in range(0, n):
					print("|-----", end="")
				print("|")
			
			if count >= 99:
				break

		if size == 100:
			count = count + 1
			pos = str(count)
			print("|", pos, end=" |\n")

			for j in range(0, n):
				print("|-----", end="")
			print("|")

		else:
			for i in range(100, size+1):
				count = count + 1
				pos = str(count)
				print("|", pos, "", end="")

				if i%n == 0:
					print("|\n", end="")
					for j in range(0, n):
						print("|-----", end="")
					print("|")

# |---------------------------------------------------------------------------------|
# To print the board after every valid move.
def printBoard(board, n):
	print("")

	for i in range(0, n):
		print("|---", end="")
	print("|")

	index = 0

	for j in range(0, n):
		for k in range (0, n):
			if(board[index] != 'Empty'):
				print("|", board[index], "", end="")

			else:
				print("|   ", end="")
			index = index + 1

		print("|\n", end="")

		for i in range(0, n):
			print("|---", end="")
		print("|")

# |---------------------------------------------------------------------------------|
# main/driver function.
def main():
	n = int(input("Enter the size of the diagonal of the Tic-Tac-Toe board: "))
	if n > 2:
		winCases = createWinCases(n)
	else:
		print("Itna chota number dijiyega? Hum nahi khelenge.")
		exit()

	choice = input("Enter x for playing as cross, or enter o for playing as nought: ")
	players = start(choice)

	# Create the initial board.
	board = list()*n*n
	for i in range(0, n*n):
		board.append('Empty')

	# To run the game if the human player chose X
	if (players["Human"] == "X"):
		playerX(players, board, n, winCases)

	# To run the game if the human player chose O
	elif (players["Human"] == "O"):
		playerO(players, board, n, winCases)

	else:
		print("An error has occured. Exiting now...")
		input()
		exit()

# |---------------------------------------------------------------------------------|
# To call the main()
if __name__ == '__main__':
	main()
