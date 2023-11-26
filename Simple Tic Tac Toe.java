
package tictactoe;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Initialize the board with empty spaces.
        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '_';
            }
        }

        //Print the board. Take players' input and then analyze the game state.
        printBoard(board);

        while (true) {
            xPlayerTurn(board, scanner);
            if (checkState(board)) {
                break;
            }
            printBoard(board);

            oPlayerTurn(board, scanner);
            if (checkState(board)) {
                break;
            }
            printBoard(board);
        }
        scanner.nextLine();
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

    private static void xPlayerTurn(char[][] board, Scanner scanner) {
        while (true) {
            System.out.println("X player, Enter your move: ");
            try {
                int row = scanner.nextInt();
                int col = scanner.nextInt();

                if (isValidMove(row, col, board)) {
                    board[row - 1][col - 1] = 'X';
                    break;
                }
            } catch (Exception e) {
                System.out.println("You should enter numbers!");
                scanner.nextLine();
            }
        }
    }

    private static void oPlayerTurn(char[][] board, Scanner scanner) {
        while (true) {
            System.out.println("O player, Enter your move: ");
            try {
                int row = scanner.nextInt();
                int col = scanner.nextInt();

                if (isValidMove(row, col, board)) {
                    board[row - 1][col - 1] = 'O';
                    break;
                }
            } catch (Exception e) {
                System.out.println("You should enter numbers!");
                scanner.nextLine();
            }
        }
    }

    private static boolean isValidMove (int row, int col, char[][] board) {
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
    private static boolean checkState(char[][] board) {
        // Check if both side have win condition.
        boolean xWon = isSymbolWon(board, 'X');
        boolean oWon = isSymbolWon(board, 'O');

        // Check if a side has won and return the result.
        if (xWon) {
            printBoard(board);
            System.out.println("X wins");
            return true;
        }
        if (oWon) {
            printBoard(board);
            System.out.println("O wins");
            return true;
        }
        // Check if the game is a draw or not finished.
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '_') {
                    return false;
                }
            }
        }
        printBoard(board);
        System.out.println("Draw");
        return true;
    }

    // This method is used to check if a given symbol has win condition.
    private static boolean isSymbolWon(char[][] board, char symbol) {
        return  board[0][0] == symbol && board[0][1] == symbol && board[0][2] == symbol ||
                board[1][0] == symbol && board[1][1] == symbol && board[1][2] == symbol ||
                board[2][0] == symbol && board[2][1] == symbol && board[2][2] == symbol ||
                board[0][0] == symbol && board[1][0] == symbol && board[2][0] == symbol ||
                board[0][1] == symbol && board[1][1] == symbol && board[2][1] == symbol ||
                board[0][2] == symbol && board[1][2] == symbol && board[2][2] == symbol ||
                board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol ||
                board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol;
    }
}
