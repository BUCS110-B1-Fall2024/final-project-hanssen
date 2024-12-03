
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Snakes and Apples 
## CS110 B1 Final Project  Fall Semester, Freshman

## Team Members

Hanssen Ly

***

## Project Description

This game will involve playing as a snake and eating apples. For every apple you eat, your score and body length will increase by one. If you run into your own body, you die and you have to start over. Your goal is to stay alive as long as you can and eat all the apples you can.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Basic Snake Movement: The snake moves in four directions (up, down, left, right) controlled by the W, A, S, D keys. The snake's body follows the movement of its head.

2. Apple Consumption and Growth: The snake consumes apples when it collides with them, and its length increases by one block. The apple then moves to a random position on the screen.

3. Collision Detection: The game checks for collisions. An apple collision when the snake eats an apple, and a self-collision when the snake's head collides with its body, causing a game over. 

4. Score Display: The player's score is displayed at the top-right of the screen, based on the number of apples eaten (snake length - 1).

5. Game Over Screen and Restart: When the snake collides with itself, the game shows a Game Over screen with the score and options to restart (press Enter) or exit (press Escape).

### Classes

- Apple: This class controls the apple's behavior, like moving around the screen, and staying within the bounds of the screen.
- Snake: This class controls the snake's behavior, like moving with the arrow keys, and increasing length when the score appears.
- Game: This controls the behavior of the game, like keeping score, and when to start and end.

## ATP

1: Using the WASD keys to control the direction of the snake.  

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game.          | The program should start.         |
|                      |                      |                                   |
|  2                   | Press the A key on   | The snake should change directions|
|                      | the keyboard.        | from its current direction to     |
|                      |                      | left.                             |
|                      |                      |                                   |
|  3                   | Press the S key on   | The snake should change directions|
|                      | the keyboard.        | from its current direction to     |
|                      |                      | down.                             |
|                      |                      |                                   |
|  4                   | Press the D key on   | The snake should change directions|
|                      | the keyboard.        | from its current direction to     |
|                      |                      | right.                            |
|                      |                      |                                   |
|  5                   | Press the W key on   | The snake should change directions|
|                      | the keyboard.        | from its current direction to     |
|                      |                      | up.                               |

2: Making sure collisions between the snake and apples are detected properly.

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game.          | The program should start.         |
|                      |                      |                                   |
|  2                   | Guide the snake      | The score should stay the same,   |
|                      | around the apples.   | and the apple should stay in the  |
|                      |                      | same location.                    |
|                      |                      |                                   |
|  3                   | Guide the snake to   | The apple should disappear and    |
|                      | an apple.            | reappear in a new location. The   |
|                      |                      | score and the snake's length      |
|                      |                      | should both increase by 1.        |

3: Confirm the game ends when the snake runs into itself.

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game.          | The program should start.         |
|                      |                      |                                   |
|  2                   | Play until the       | The snake should be long enough   |
|                      | snake's length is    | to be able to run into itself.    |
|                      | greater than or equal|                                   |
|                      | to 5.                |                                   |
|                      |                      |                                   |
|  3                   | Guide the snake to   | The game should end and the game  |
|                      | its own body segment.| over screen should appear.        |
|                      |                      |                                   |
