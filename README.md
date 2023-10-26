# Tic-Tac-Toe-Bot
Tic-Tac-Toe Bot is an AI bot created for the needs of personal practical research. It demonstrates the computer's ability to think and make optimal moves in a game against a human.
<br>The goal of this project is to create a game using the minimax algorithm. 
Almost every existing implementation of this type of project uses the minimax algorithm but in a different way.
The problem with most of these implementations is that the execution is not the fastest, and removing this problem is the goal of this project.
<br>One of the ways in which this algorithm can be accelerated is the implementation of the Alpha-Beta Pruning optimization technique in the minimax algorithm itself, which was done in this project.

# Minimax Algorithm
<a href="https://ibb.co/1XmvgTg"><img src="https://i.ibb.co/DMRVJQJ/Minimax.png" alt="Minimax" border="0"></a>
<br><br>This algorithm is based on a search tree.
<br>This implementation consists of 3 basic outcomes - player won, machine won, and tie.
<br>In our case, the machine is the one doing the minimization and the player is the one doing the maximization.
<br>Since it is a recursive algorithm, in each iteration the current state of the board is passed to it and it is checked whether one of the basic outcomes has occurred.
<br>If not, the best possible move is sought that leads to one of two basic outcomes - a win for the machine or a draw.

# Alpha-Beta Pruning
<a href="https://ibb.co/zGj1qjh"><img src="https://i.ibb.co/qkXzTXM/Blog-8-5-2020-06-1024x598.jpg" alt="Blog-8-5-2020-06-1024x598" border="0"></a>
<br><br>This is an optimization algorithm that has the role of significantly reducing the number of passes through tree nodes.
<br>It uses two values ​​- alpha and beta and performs checks using them.
<br>If a move has a worse result than the previous one (leads to a bad outcome or for a positive outcome it is necessary to go deeper into the tree), that part of the tree is cut off and the search is redirected to other nodes for which the same is checked.

# Potential Expansions
* <b>ADDITIONAL OPTIMIZATION</b>
  <br>Regardless of the fact that this implementation is sufficient for this type of project, one of the possible extensions is to remove unnecessary checks by storing already performed ones somewhere in memory.
* <b>SEQUENCE OF CHECKS</b>
  <br>One good extension would be to introduce some order of checks that should always check the step with the highest probability of failure first.
* <b>DISPLAY OF THE FINAL RESULT</b>
  <br>The current version does not have any indicator that the game is over, nor does it record the results achieved during the game.

