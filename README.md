  Code Walkthrough:
1. In the `main()`, we create the board from the diagonal size inputted by the user,
   and set the user input as ```X``` or ```O```.
2. The diagonal size ```n``` is used to create a set of all the possible victory
   condition combinations (row, column, diagonal; a total of 2n+2 combos) in the
   method createWinCases(). Every move is saved as a set of matrix indices for 
   their corresponding position on the board. Thus 00 is the upper-left corner
   (0th row, 0th column) and (n-1)(n-1) is the lower-right corner. The counting
   of these indices start from 0 and go till n-1 for obvious reasons. The method
   returns a set of all the possible winCases.
3. The user input ```choice``` is used to create a list of players, which is then used
   to put the input on the board.
4. The ```board```, ```players```, ```n```, and ```winCases``` are sent to the `playerX()` or `playerO()`
   depending upon the player's choice in the `main()`, where the game is played.
5. After the first move by the player and the computer, the game runs within a
   `while` loop, going on until a result (victory, loss, draw) is reached.
6. The moves are saved by the methods `setPlayerMoves()` and `setOppnMoves()`. After
   setting each move, it is saved as a set of all the move combinations made thus
   far.
7. After every move, the board is sent to the `printBoard()` method for printing the
   board.
