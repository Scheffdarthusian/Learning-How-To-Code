/*
Write a program that reads an array of integers and two numbers n and m. The program must check that n and m never occur next to each other (in any order) in the array.

Input data format

The first line contains the size of an array.

The second line contains elements of the array.

The third line contains two integer numbers n and m.

All numbers in the same line are separated by the space character.

Output data format

The result is a single boolean value true if n and m never occur next to each other; otherwise, it is false.


Solution:
*/

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);

        int size = scanner.nextInt();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        System.out.println(checkAdjacent(arr,n, m));
    }
    public static boolean checkAdjacent(int[] arr, int n, int m) {
        for (int i = 0; i < arr.length-1; i++) {
            if ((arr[i] == n && arr[i + 1] == m) || (arr[i] == m && arr[i + 1] == n)) {
                return false;
            }
        }
        return true;
    }


}
