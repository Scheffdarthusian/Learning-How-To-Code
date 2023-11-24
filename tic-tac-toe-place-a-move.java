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
            int row = scanner.nextInt();
            int col = scanner.nextInt();

            if (isValidMove(row, col, scanner, board)) {
                board[row - 1][col - 1] = 'X';
                printBoard(board);
                break;
            } else {
                System.out.println("Invalid move. Please try again.");
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
        if (!scanner.hasNextInt()) {
            System.out.println("You should enter numbers!");
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
