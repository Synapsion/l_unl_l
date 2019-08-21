def get_no_nines(l_num_s,h_num_s) :

	tot_count = -1
	l_num = int(l_num_s)
	h_num = int(h_num_s)
	num_diff = h_num - l_num

	if ('9' in l_num_s) or ('9' in h_num_s) :
		return tot_count,False
	elif (l_num % 9 == 0) or (h_num % 9 == 0):
		return tot_count, False
	else:
		l_dig_count = len(l_num_s)
		h_dig_count = len(h_num_s)
		m_nines_count = 0
		m_nines_ex_count = 0
		m_nines_overlaps = 0
		lsd_nines = 0

		lsd_add_factor = 0
		add_factor = 0
		overlap_add_factor = 0

		dig_diff = h_dig_count - l_dig_count

		#if dig_diff > 0 :
		m_n_p = h_dig_count - 2
		skip_d = dig_diff
	
		'''
		Loop to get the numbers with nines at positions other than at the end. Those with 9 at the end and those divisible 
		by 9 are excluded as those would be counted in the subsequent sections.
		Outer loop make it go through the number segments in the order of significance , from highest to lowest 
		and the inner loop adds up the actual count at every segment based on the position of the order of significance.
		'''
		for i in range(h_dig_count-2) :
			if i == 0 : 
				if skip_d > 0 :
					m_n_m = int(h_num_s[i])
				else :
					m_n_m = int(h_num_s[i]) - int(l_num_s[i])
			else :
				if skip_d > 0 :
					m_n_m = 9+int(h_num_s[i])
				else :
					m_n_m = (9 - int(l_num_s[i-dig_diff])) + int(h_num_s[i])

			#if m_n_m > 0 :
				
			p_factor = m_n_p
			p_factor_total_1 = 0
			p_factor_total_2 = 0

			p_factor_overlap_1 = 0
			p_factor_overlap_2 = 0

			
			lsd_nines_factor_1 = 0
			lsd_nines_factor_2 = 0
			for k in range(p_factor) :
				if k == 0 :
					p_factor_total_1 = (9**k) * (10**(m_n_p-k))
					p_factor_overlap_1 = (9**k) * ((10**(m_n_p-k)-1)/9+1)
					lsd_nines_factor_1 = (9**k) * (10**(m_n_p-k-1))
				else :
					p_factor_total_2 += (9**k) * (10**(m_n_p-k))
					p_factor_overlap_2 += (9**k) * ((10**(m_n_p-k)-1)/9+1)
					lsd_nines_factor_2 += (9**k) * (10**(m_n_p-k-1))

			if m_n_m >= 1 :		
				add_factor = (m_n_m * p_factor_total_1) + ((m_n_m-1) * p_factor_total_2)
				overlap_add_factor = (m_n_m * p_factor_overlap_1) + ((m_n_m-1) * p_factor_overlap_2)
				lsd_add_factor = (m_n_m * lsd_nines_factor_1) + ((m_n_m-1) * lsd_nines_factor_2)
			#else :
			#	add_factor = 0
							
			m_nines_count += add_factor
			m_nines_overlaps += overlap_add_factor
			lsd_nines += lsd_add_factor
			m_nines_ex_count = m_nines_count - (2 * lsd_nines)

			print('m_n_p,skip_d =>',m_n_p,skip_d)
			m_n_p -= 1
			skip_d -= 1

		print('m_nines_ex_count :',m_nines_ex_count,m_nines_count, lsd_nines)

		#Gets all the numbers with 9 at the end (i.e. as the least significant digit)

		s_nines_count = int(h_num/10) - int(l_num/10)
		
		print('s_nines_count :',s_nines_count)

		#Gets all the numbers divisible by 9
		d_nines_count = 0 

		next_h_l_div = l_num + (9 - (l_num%9))
		next_l_h_div = h_num - (h_num%9)

		d_nines_count = int(((next_l_h_div - next_h_l_div)/9)+1)
		print('d_nines_count :',d_nines_count)

		# Find the overlap where the numbers with 9 at the end are divisible by 9 too.

		lsd_next_hl = int(str(next_h_l_div)[-1])
		lsd_next_lh = int(str(next_l_h_div)[-1])

		if lsd_next_hl == 9 :
			lsd_9_next_h_l_div = next_h_l_div
		else :
			lsd_9_next_h_l_div = next_h_l_div + ((lsd_next_hl+1)*9)

		if lsd_next_lh == 9 :
			lsd_9_next_l_h_div = next_l_h_div
		else :
			lsd_9_next_l_h_div = next_l_h_div - ((9-lsd_next_lh)*9)

		print ('lsd 9 divs :',lsd_9_next_h_l_div,lsd_9_next_l_h_div)

		tot_div_lsd_overlaps = int((lsd_9_next_l_h_div - lsd_9_next_h_l_div)/90) + 1

		# Total valid turns (count) is calculated by reducing all those with 9s at end position or otherwise from all numbers
		# in the range, after adjusting for the overlaps from above.

		print('tot_div_lsd_overlaps :',tot_div_lsd_overlaps)	
		tot_count = (num_diff + 1) - (m_nines_ex_count+s_nines_count+d_nines_count - tot_div_lsd_overlaps)

		return tot_count,True


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
				tot_count,check_status = get_no_nines(l_num_s=l_num,h_num_s=h_num)
				if check_status :
					print('Case #{} : {}'.format(i,tot_count))
				else :
					print('Not valid input - high,low or both contain digit 9 or divisible by 9')
			else :		
				print('Not a valid input, takes only integers')
				continue	