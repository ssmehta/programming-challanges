QuickSort 1 - Partition
=======================

The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm. Insertion Sort has a running time of O(N<sup>2</sup>) which isn’t fast enough for most purposes. Instead, sorting in the real-world is done with faster algorithms like Quicksort, which will be covered in these challenges.

The first step of Quicksort is to partition an array into two parts.

### Challenge:

Given an array *ar* and a number *p*, can you partition the array, so that all elements greater than *p* are to the right of it and all the numbers smaller than *p* are to its left?

Besides for necessary partitioning, the numbers should otherwise remain in the same order. This means if *n1* was before *n2* in the original array, it must remain before it in the partitioned array, unless *n1* > *p* > *n2*.

*Guideline* - In this challenge, you do not need to move around the numbers ‘in-place’. This means you can create 2 lists and combine them at the end.

### Input:

You will be given an array of integers. The number p is the first element in ar.

There are 2 lines of input:

* *n* - the number of elements in the array *ar*
* the *n* numbers of *ar* (including *p* at the beginning)

### Output:

Print out the numbers of the partitioned array on one line.

### Constraints:

* 1 <= n <= 1000 
* -1000 <= x <= 1000 , x ∈ ar 
* All elements will be distinct

### Sample Input:

    5
    4 5 3 7 2

### Sample Output:

    3 2 4 5 7

### Explanation:

*p* = 4. The 5 was moved to the right of the 4, and the 2 was moved to the left of 4. The numbers otherwise remained in the same order.

### Task:

Complete the method partition which takes in one parameter - an array *ar* to be partitioned, where the first element in it is the number *p*.
