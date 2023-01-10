A = [13,4,10,9,7,5,4,16,2,1]
i = 1
def min_heapifyY(A, i):
	l <- LEFT(i)
	r <- RIGHT(i)
	smallest <- i
	if l ≤ heap-size[A] and A[l] < A[i]:
		then smallest <- l
	if r ≤ heap-size[A] and A[r] < A[smallest]:
		then smallest <- r
	if smallest ≠ i:
		then swap(A[i], A[smallest])
		     MIN-HEAPIFY(A, smallest)
