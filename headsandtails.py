def solution(A):
	n = len(A)
	if len(set(A))==1:
		return n//2 

	count_1 = A.count(1)
	count_2 = A.count(0)
	print(count_1,count_2)
	return abs(count_2 - count_1)//2 