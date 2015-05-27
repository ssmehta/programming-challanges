Bot Saves Princess - 2
======================

In this version of “Bot saves princess”, Princess Peach and bot’s position are randomly set. Can you save the princess?

### Task:

Complete the function nextMove which takes in 4 parameters - an integerN, an integer r and c indicating the row & column position of the bot and the character array grid and output only the **next** move the bot makes to rescue the princess.

### Input:

The first line of the input is N (<100), the size of the board (NxN). The second line of the input contains two space seperated integers, which is the position of the bot in row-column format. The Board is indexed at (0,0) on the top left and (N-1,N-1) on the bottom right. The x co-ordinate increases from left to right and y co-ordinate increases from top to bottom. N lines follow each line containing N characters which is the grid data.

The position of the princess is indicated by the character ‘p’ and the position of the bot is indicated by the character ‘m’ and each cell is denoted by ‘-‘ (ascii value 45).

### Output:

Output only the **next** move you take to rescue the princess. Valid moves are LEFT or RIGHT or UP or DOWN

### Sample Input:

    5
    3 2
    -----
    -----
    p--m-
    -----
    -----

### Sample Output:

    LEFT

### Scoring:

Your score for every testcase would be (NxN minus number of moves made to rescue the princess)/10 where N is the size of the grid (5x5 in the sample testcase).
