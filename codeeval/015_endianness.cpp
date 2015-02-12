/*
Endianness

Description:

Write a program to print out the endianness of the system.

Input sample:

None

Output sample:

Print to stdout, the endianness, wheather it is LittleEndian or BigEndian.
e.g.

    BigEndian
*/

#include <cstdio>

using namespace std;


int main(int argc, char *argv[]) {
	int a = 0, b = 1;
	printf((b << 16) | a == 65536 ? "LittleEndian\n" : "BigEndian\n");
	
    return 0;
}
