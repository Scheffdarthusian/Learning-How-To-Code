/*
The maximum product of adjacent elements

Write a program that reads an array of ints and outputs the maximum product of two adjacent elements in the given array of non-negative numbers.

Input data format

The first line of the input contains the number of elements in the array.

The second line contains the elements of the array separated by spaces.

The array always has at least two elements.
*/


//Solution:

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        int[] arr = createArr(size, scanner);
        System.out.println(maxProduct(arr));
    }
    public static int maxProduct(int[] arr) {
            int max = 0;
            int product = 0;
            if (arr.length > 1) {
                for (int i = 0; i < arr.length - 1; i++) {
                    product = arr[i] * arr[i+1];
                    if (max < product) {
                        max = product;
                    }
                }
            }
            return max;
        }
    public static int[] createArr(int size, Scanner scanner) {
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }
        return arr;
    }
}
