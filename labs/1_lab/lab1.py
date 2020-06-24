"""Lab assignment 1"""
from typing import List

def max_list_iter(int_list: List) -> int:
	"""finds the max of a list of numbers and returns the value (not the index)
	If int_list is empty, returns None. If list is None, raises ValueError"""
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return None
	while True:
		try:
			if int_list[0]<int_list[1]:
				int_list.remove(int_list[0])
			else:
				int_list.remove(int_list[1])
		except IndexError:
			return int_list[0]
			
def reverse_rec(int_list: List) -> List:
	"""recursively reverses a list of numbers and returns the reversed list
	If list is None, raises ValueError"""
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return [] 
	if len(int_list) == 1:
		return [int_list[0]]
	return [int_list[-1]]+reverse_rec(int_list[0:len(int_list)-1])
	
def bin_search(target: int, low: int, high: int, int_list: List) -> int:
	"""searches for target in int_list[low..high] and returns index if found
	If target is not found returns None. If list is None, raises ValueError """
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return None	
	if int_list[low] == target:
		return low
	if int_list[high] == target:
		return high
	if high - low <= 1:
		return None
	mid = (low + high)//2
	if int_list[mid] <= target:
		low = mid
	else:
		high = mid
	return bin_search(target,low,high,int_list)
