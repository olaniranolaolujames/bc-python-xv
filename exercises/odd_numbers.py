def odd_numbers(num1, num2):
	if (num1 > num2):
		return "The first argument is greater than the second argument"	
	elif type.num1 != int and type.num2 != int:
		return "Input only integers"
	else:
		list_of_odd_nums = []
		for i in range(num1, num2+1 ):
			if i%2 == 1:
				list_of_odd_nums.append(i)
		return list_of_odd_nums
