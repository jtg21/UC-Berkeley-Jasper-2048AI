# 2048-AI-Starter-Code

This is my implementation of the 2048 AI project hosted by UC Berkeley IEEE Student Branch
1. User_game: The traditional one-human-player 2048 game
2. AI_game: Run one-AI-player 2048 game
3. AI_Move: the basic tile move/merge logic based on 2048 rules
4. AI_Minimax: Minimax algorithm for 2048 tree. Max is the AI playing the game, and Min is the computer which generates new 2 or 4 tile randomly
5. AI_Heuristics: The heuristics function to rank/compare possible branch grids. This will be used to collect the best possible move in AI_Minimax

## How to run/test your AI

This AI is built based on the 2048 pypi package made by user 'quantum'. If you don't have this package on your laptop, run <code> pip install 2048 </code> in your terminal.

Then, in the directory, run <code> py AI_game.py </code> to test your AI performance.

The GUI will automatically pops up, and AI will start search.

## Perfomance

So far the AI is a bit inconsistant but I can win and attain a pretty high score. So far the largest tiles I have observed on one board state have been 2048, 1024, 512, and 256, and 128. So the AI near made it to 4096. From what I've observed, the AI occassionally makes some "bad" moves. In some games the moves are so unfavorable that the AI cannot recover and quickly loses. Much of the perfomance variablility is due to this unpredictable behavior.

## AI and Descision making

My verision of 2048 has two playable version: AI and single player. The AI verision relies on an iteratively deepening minimax tree search inorder to find the best moves.

## Heuristics

To evalute the board state I used a weight sum of various hueristics. These heuristics include a measure of weighted patterns, monotonicity, and smoothness.

### Pattern

Using a preset matix of weight, I encourage the AI to choose boards states that load larger tiles into the bottom right corner. The benifit of having larger tiles in the corner is reduced game complexity (right and down) and prevention of isolated small tiles. Its important to note that the choice of the corner is arbitiary.

### Monotinicity

To further enforce the corner stacking behavior, I check the board for monotinicity. I call a column or row monotonic if value of the tiles are increasing from left to right and from top to bottom. This serves to 

### Smoothness

As the tiles on the board increase in value they tend to drift apart from each other. This usually results in the isolation of small tiles which makes it difficult to combine tiles. Smoothness accounts for the difference between adjacent tiles such that board with adjacent tiles of similar value are highly valued. Especially as the tile values increase, the penalty for non adjacent tiles becomes higher. 


