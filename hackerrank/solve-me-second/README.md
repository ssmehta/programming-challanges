Solve Me Second
===============

You learnt about `STDIN` and `STDOUT` in Solve me first.

This is the second challenge in the introduction series.  The purpose of this challenge is to give you a working I/O template in your preferred language.  It includes scanning 2 space separated integers from `STDIN` in a loop over *T* lines, calling a function, returning a value, and printing it to `STDOUT`.

A pseudo code looks like this

    read T
    loop from 1 to T
        read A and B
        compute the sum
        print value in a new line
    end loop

The task is to scan two numbers from `STDIN`, and print the sum *A+B* on `STDOUT`.  The code has already been provided for most of the popular languages.  This is primarily for you to read and inspect how the IO is handled.

**Note:** the code has been saved in a template, which you can submit if you want.  Or, you may try rewriting it and building it up from scratch.

### Input:

This section specifies the input format.

The first line contains *T* (number of test cases) followed by *T* lines

Each line contains *A* and *B* separated by a space

As you can see, we have provided in advance the number of lines.  We discourage the use of scanning till `EOF` as not every language has an easy way to handle that.  In fact, every hackerrank challenge is designed in such a way that multitest beginning with a *T* line to indicate the number of lines.

### Output:

This section specified the output format.

An integer that denotes Sum *(A + B)* printed on new line for every test case

### Constraints:

This section tells what input you can expect.  You can freely assume that the input will remain within the boundaries specified.  As an example here given below, *A* and *B* will never be below 1 or above 1000.

* 1 <= *T* <= 1000.
* 1 <= *A*, *B* <= 1000

### Sample Input:

    2
    2 3
    3 7

### Sample Output:

    5
    10

The above sample should be taken seriously.  The input will be of 2 lines and your test case are `2 3` and `3 7` in 2 separate lines.  And the output is the number `5` and `10` printed on 2 separate lines.  If you print extra lines or `"The answer is: 5"` any such extra characters in output will result in a `Wrong Answer` as the judging is done using diff checker.