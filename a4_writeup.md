# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
Implementing the function that checks whether or not the player has won was kind of confusing, as there were quite a few rulings to implement in order to ensure accuracy with the win.

2. Explain how you would add a computer player to the game.
You would use an if-then statement to intiate each move the CPU makes, making moves based on what squares are filled on the board, alternating moves between the input the player makes and the hypothetical CPU's moves.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

Maybe create if-then statements for each outcome, i.e. if x is placed here, then put o here, here, or here; with options if the intial choice squares are already filled.