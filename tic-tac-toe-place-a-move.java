/*
Description
It's time to make our game interactive! Now we're going to add the ability for a user to make a move. To do this, we need to divide the grid into cells. Suppose the top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3):

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

The program should ask the user to enter the coordinates of the cell where they want to make a move.

In this stage, the user plays as X, not O. Keep in mind that the first coordinate goes from top to bottom and the second coordinate goes from left to right. The coordinates can include the numbers 1, 2, or 3.

What happens if the user enters incorrect coordinates? The user could enter symbols instead of numbers, or enter coordinates representing occupied cells or cells that aren't even on the grid. You need to check the user's input and catch possible exceptions.

Objectives
The program should work as follows:

Get the initial 3x3 grid from the input as in the previous stages. Here the user should input 9 symbols representing the field, for example, _XXOO_OX_.
Output this 3x3 grid as in the previous stages.
Prompt the user to make a move. The user should input 2 coordinate numbers that represent the cell where they want to place their X, for example, 1 1.
Analyze user input. If the input is incorrect, inform the user why their input is wrong:
Print This cell is occupied! Choose another one! if the cell is not empty.
Print You should enter numbers! if the user enters non-numeric symbols in the coordinates input.
Print Coordinates should be from 1 to 3! if the user enters coordinates outside the game grid.
Keep prompting the user to enter the coordinates until the user input is valid.
If the input is correct, update the grid to include the user's move and print the updated grid to the console.
To summarize, you need to output the field 2 times: once before the user's move (based on the first line of input) and once after the user has entered valid coordinates (then you need to update the grid to include that move).

Do not delete the code you wrote in the previous stage! You will need it in the final stage of this project, so now you can just comment out a part of it.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> X_X_O____
---------
| X   X |
|   O   |
|       |
---------
> 3 1
---------
| X   X |
|   O   |
| X     |
---------
Example 2:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 3:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 3 3
---------
|   X X |
| O O   |
| O X X |
---------
Example 4:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 2 3
---------
|   X X |
| O O X |
| O X   |
---------
Example 5:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 3 1
This cell is occupied! Choose another one!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 6:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> one
You should enter numbers!
> one one
You should enter numbers!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
Example 7:

> _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
> 4 1
Coordinates should be from 1 to 3!
> 1 4
Coordinates should be from 1 to 3!
> 1 1
---------
| X X X |
| O O   |
| O X   |
---------
*/



package tictactoe;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[][] board = new char[3][3];

        //Initialize the board with empty spaces.
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '_';
            }
        }

        // Take input to update the board.
        String input = scanner.nextLine();
        updateBoard(board, input);

        //Print the game board and then place a move.
        printBoard(board);
        placeMove(board, scanner);
        //Check game state and print the result
        // System.out.println(checkState(board));
    }


    private static void updateBoard(char[][] board, String input) {
        int k = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = input.charAt(k++);
                }
            }
        }

    private static void printBoard(char[][] board) {
        System.out.println("---------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println("|");
        }
        System.out.println("---------");
    }

    private static void placeMove(char[][] board, Scanner scanner) {
        while (true) {
            System.out.println("Enter your move: ");
            try {
                int row = scanner.nextInt();
                int col = scanner.nextInt();

                if (isValidMove(row, col, board)) {
                    board[row - 1][col - 1] = 'X';
                    printBoard(board);
                    break;
                }
            } catch (Exception e) {
                System.out.println("You should enter numbers!");
                scanner.reset();
            }
        }
    }

    private static boolean isValidMove (int row, int col, Scanner scanner, char[][] board) {
        if (row < 1 || row > 3 || col < 1 || col > 3) {
            System.out.println("Coordinates should be from 1 to 3!");
            return false;
        }
        if (board[row - 1][col - 1] != '_') {
            System.out.println("This cell is occupied! Choose another one!");
            return false;
        }
        return true;
    }


    // Analyze the game state.
/*    private static String checkState(char[][] board) {
        // Count the number of X and O on the board.
        int xCounts = 0;
        int oCounts = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == 'X') {
                    xCounts++;
                } else if (board[i][j] == 'O') {
                    oCounts++;
                }
            }
        }
        // Check if the difference is valid.
        int difference = oCounts - xCounts;
        if (difference < -1 || difference > 1) {
            return "Impossible";
        }

        // Check if both side have win condition.
        boolean xWon = isSymbolWon(board, 'X');
        boolean oWon = isSymbolWon(board, 'O');
        if (xWon && oWon) {
            return "Impossible";
        }

        // Check if a side has won and return the result.
        if (xWon) {
            return "X wins";
        }
        if (oWon) {
            return "O wins";
        }

        // Check if the game is a draw or not finished.
        if (xCounts + oCounts == 9) {
            return "Draw";
        }
        return "Game not finished";
    }

    // This method is used to check if a given symbol has win condition.
/*    private static boolean isSymbolWon(char[][] board, char symbol) {
        return  board[0][0] == symbol && board[0][1] == symbol && board[0][2] == symbol ||
                board[1][0] == symbol && board[1][1] == symbol && board[1][2] == symbol ||
                board[2][0] == symbol && board[2][1] == symbol && board[2][2] == symbol ||
                board[0][0] == symbol && board[1][0] == symbol && board[2][0] == symbol ||
                board[0][1] == symbol && board[1][1] == symbol && board[2][1] == symbol ||
                board[0][2] == symbol && board[1][2] == symbol && board[2][2] == symbol ||
                board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol ||
                board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol;
    } */
}
