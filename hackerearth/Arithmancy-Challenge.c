/*
Arithmancy Challenge 
Harry, Ron and Hermonie are in their third year at Hogwarts School of Witchcraft and Wizadry. Hermonie has been given a time turner by Professor McGonagall so that she can study extra subjects. One of those subjects is Arithmancy - the study of numbers. Once upon a time, the three of them are sitting in the Gryffindor Common Room and Hermonie is completing an essay for Arithmancy. Ron comes up with an arithmancy challenge to test Hermonie. He gives her two numbers, B and E, and Hermonie has to give the last digit of B^E. Since, Hermonie is the brightest witch of her age, she is able to solve the problem within no time. Now, Ron asks her to give the challenge to "That Arithmancy Witch", Professor Vector. As she is not able to solve the problem, she turns to one of her other favourite students (you), for help. Find the answer to Hermonie's Challenge for Professor Vector.

Note

There is partial marking for this question.

Input

Each test file starts with an integer T - the no. of Test Cases. Each Test Case has a single line which contains two integers - B and E.

Output

For each test case output the last digit of B^E followed by a newline.

Constraints

1<= T <= 1.5 X 10^6

1<= B,E <= 10^18

WARNING

Large Input data. using printf() and scanf() instead of cin and cout

Problem Setter: Jayam Modi

Sample Input (Plaintext Link)
3
2 1
4 2
5 3
Sample Output (Plaintext Link)
2
6
5
Explanation
For the last test case, 5^3 =125. The last digit of 125 is 5.
*/

#include <stdio.h>
int main()
{
    long int t, a, b, i;
    int table[] = {0, 0, 0, 0, 1, 1, 1, 1, 6, 2, 4, 8, 1, 3, 9, 7, 6, 4, 6, 4, 5, 5, 5, 5, 6, 6, 6, 6, 1, 7, 9, 3, 6, 8, 4, 2, 1, 9, 1, 9};
	
	scanf("%ld", &t);
	if(t < 1 || t > 1500000)
		return 0;
		
	for(i = 0; i< t; i++ ){
		scanf("%ld %ld", &a, &b);	
		if (a < 1 || b < 1 || a > 1000000000000000000L || b > 1000000000000000000L)
        	return 0;
        printf("%d\n", table[((a%10)<<2)+(b&3)]);
	}
}
