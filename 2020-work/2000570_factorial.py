def factorial(n):
	sum = 1
	for i in range(1, n+1):
		sum *= i
	print(sum)
	
if __name__ == '__main__':
	print("n : ")
	n = int(input())
	factorial(n)
