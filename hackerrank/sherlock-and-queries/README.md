Sherlock and Queries
====================

Watson gives to Sherlock an array: *A<sub>1</sub>*, *A<sub>2</sub>, ..., *A<sub>N</sub>*. He also gives to Sherlock two other arrays: *B<sub>1</sub>*, *B<sub>2</sub>*, ..., *B<sub>M</sub>* and *C<sub>1</sub>*, *C<sub>2</sub>*, ..., *C<sub>M</sub>*. 

Then Watson asks Sherlock to perform the following program:

    for i = 1 to M do
        for j = 1 to N do
            if j % B[i] == 0 then
                A[j] = A[j] * C[i]
            endif
        end do
    end do

Can you help Sherlock and tell him the resulting array *A*? You should print all the array elements modulo (10<sup>9</sup> + 7).

### Input:

The first line contains two integer numbers *N* and *M*. The next line contains *N* integers, the elements of array *A*. The next two lines contains *M* integers each, the elements of array *B* and *C*.

### Output:

Print *N* integers, the elements of array *A* after performing the program modulo (10<sup>9</sup> + 7).

### Constraints:

* 1 <= *N*, *M* <= 10<sup>5</sup>
* 1 <= *B<sub>i</sub>* <= N
* 1 <= *A<sub>i</sub>*, *C<sub>i</sub>* <= 10<sup>5</sup>

### Sample Input:

    4 3
    1 2 3 4
    1 2 3
    13 29 71

### Sample Output:

    13 754 2769 1508