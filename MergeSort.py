# This program contains two functions that, together, perform a 'merge-sort'. Given an 
# unordered list of numbers, the program sorts it by breaking it into two lists of 
# roughly half the length of the original, and sorting those, recursively.


def merge_sort(list1):
	# splits a list of numbers into two lists of roughly equal size
	# then orders the sub-lists from small to large
	# then merges the ordered lists back into one
	# and returns the sorted list
	size = len(list1)
	if size <= 1:
		return list1
	else:
		half = int(round(size / 2,0))
		sublist1 = list1[:half]
		sublist2 = list1[half:]
		output1 = merge_sort(sublist1)
		output2 = merge_sort(sublist2)
		return merge(output1, output2)


def merge(list1, list2):
	# merges two ordered lists of numbers into a single list 
	output = []
	first_counter = 0
	second_counter = 0
	total_length = len(list1) + len(list2)
	for index in range(total_length):
		if first_counter == len(list1):
			output.append(list2[second_counter])
			second_counter += 1
		elif second_counter == len(list2):
			output.append(list1[first_counter])
			first_counter += 1
		elif list1[first_counter] <= list2[second_counter]:
			output.append(list1[first_counter])
			first_counter += 1
		elif list1[first_counter] > list2[second_counter]:
			output.append(list2[second_counter])
			second_counter += 1
		else:
			# this should not happen
			print("ERROR")
	return output





list = [1,1,0,0.4,3.2,3.6,4.8,12,21,21,12,12.4]
sorted_list = merge_sort(list)
print(sorted_list)
