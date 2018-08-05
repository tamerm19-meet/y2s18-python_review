# Write your solution for 1.4 here!
def is_prime(x):
	i=2
	while(i<x):
		if(x % i == 0):
			return False
		i+=1
	return True
print(is_prime(17))