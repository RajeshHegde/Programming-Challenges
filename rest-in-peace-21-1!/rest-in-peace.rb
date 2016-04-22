'''
Created on 22 Apr 2016

@author: RAJESH
https://www.hackerearth.com/problem/algorithm/rest-in-peace-21-1
'''

def solve_problem(n)
	if (n.to_s().include?('21') or n%21 == 0)
		puts 'The streak is broken!'
	else
		puts 'The streak lives still in our heart!'
	end
end

t = gets.chomp().to_i()

if (t < 1 or t > 100)
	exit
end

for i in 0...t
	n = gets.chomp().to_i()

	if (n < 1 or n > 1000000)
		exit
	end

	solve_problem(n)
end