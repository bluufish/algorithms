#time complexity nlog(n)
#uses pointers
def twoNumberSum(array, targetSum):
	sums = []
    #assuming not sorted
	sorted_array = sorted(array)

	left_index, right_index = (0,len(sorted_array)-1)
	
	while left_index < right_index:
		pair_sum = sorted_array[left_index] + sorted_array[right_index]
		if pair_sum == targetSum:
			sums += [sorted_array[left_index],  sorted_array[right_index]]
			left_index += 1
		elif pair_sum < targetSum: 
			left_index += 1
		else: 
			right_index -= 1
	
	return sums

#hash table solution
#time complexity log(n)

def twoNumberSum(array, targetSum):
    