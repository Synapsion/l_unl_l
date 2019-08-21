def get_no_nines_bruteforce(l_num_s,h_num_s) :

	tot_count = -1
	l_num = int(l_num_s)
	h_num = int(h_num_s)
	num_diff = h_num - l_num
	l_bound = h_num
	count = 0
	do_count = True
	lsd_9_count = 0
	nlsd_9_count = 0 
	lsd_9_div = 0
	nlsd_9_div = 0
	lsd_nlsd_9_div = 0
	lsd_nlsd_overlaps = 0
	lsd_nlsd_9_div_overlaps = 0

	if ('9' in l_num_s) or ('9' in h_num_s) :
		return tot_count,False
	elif (l_num % 9 == 0) or (h_num % 9 == 0):
		return tot_count, False
	else:
		while l_bound >= l_num :
			do_count =True
			l_bound_s = str(l_bound)
			if ('9' in l_bound_s) :
				#l_bound -= 1
				do_count = False
				if l_bound_s[-1] == '9':

					lsd_9_count += 1
					if '9' in l_bound_s[:-1] :
						lsd_nlsd_overlaps += 1
						if (l_bound % 9 == 0) :
							lsd_nlsd_9_div_overlaps += 1

					if (l_bound % 9 == 0) :
						lsd_9_div += 1
				else :
					nlsd_9_count += 1	

					if (l_bound % 9 == 0) :
						nlsd_9_div += 1
			
			if (l_bound % 9 == 0) :
				#l_bound -= 1
				do_count = False
				lsd_nlsd_9_div += 1

			if do_count :
				count += 1

			l_bound -= 1 

			
			
		print('lsd_9_count={},lsd_9_div={},nlsd_9_count={},nlsd_9_div={},lsd_nlsd_overlaps={},'\
					'lsd_nlsd_9_div={},lsd_nlsd_9_div_overlaps={}'\
					.format(lsd_9_count,lsd_9_div,nlsd_9_count,nlsd_9_div,lsd_nlsd_overlaps,lsd_nlsd_9_div,lsd_nlsd_9_div_overlaps))	
		return count, True
			
num_tests = input()

n_attempts = 1 
if num_tests.isdecimal() :
	print ('test cases :',num_tests)
	for i in range(int(num_tests)) :
		for a in range(n_attempts) :
			dspl_num_in = input()
			lh_nums = dspl_num_in.split()
			l_num,h_num = lh_nums[0],lh_nums[1]
			print('nums',l_num,h_num)
			if l_num.isdecimal() and h_num.isdecimal() :
				'''
				key_press,key_type_plus = findNearestEN(d_num = dspl_num)
				print ('Press {} key {} times'.format(('+' if key_type_plus else '-'),key_press ))
				break
				'''
				if int(h_num) > 999999 :
					print ('High is too high')
					break
				tot_count,check_status = get_no_nines_bruteforce(l_num_s=l_num,h_num_s=h_num)
				if check_status :
					print('Case #{} : {}'.format(i,tot_count))
				else :
					print('Not valid input -  high,low or both contain digit 9 or divisible by 9')
			else :		
				print('Not a valid input, takes only integers')
				continue	