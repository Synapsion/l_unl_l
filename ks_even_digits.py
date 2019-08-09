'''Finds out how many key presses on '+' or '-' keys requried to reach an even-digits-only number on a calculator-Google Kickstart 2018 PP '''


def findNearestEN(d_num) :

	dspl_num_i = int(d_num) 
	lead_digit_value = 0
	dn_length = len(d_num)
	

	for i in range(dn_length) :
		m_digit = int(d_num[i])
		if m_digit % 2 == 0 :
			print('in if',i)
			if i == dn_length - 1 :
				return 0 , True
			else :
				#lead_digit_value += m_digit * (10 ** (dn_length-i-1))
				continue
		elif i < dn_length - 1 :
			print('in elif',i)
			if m_digit ==9 :
				u_bound = (m_digit + 11) * (10 ** (dn_length-i-1))
			else :
				u_bound = (m_digit + 1) * (10 ** (dn_length-i-1))

			if dn_length-i-2 == 0 :
				factor = 2
			else :
				#factor = (10 ** (dn_length-i-2))+12
				factor = int('1'* (dn_length-i-1)) + 1

			l_bound = (m_digit * (10 ** (dn_length-i-1))) - factor
			print('l_bound',l_bound)

			u_bound_clks = u_bound - int(d_num[i:]) 
			l_bound_clks = int(d_num[i:]) - l_bound

			if u_bound_clks <= l_bound_clks :
				return u_bound_clks+lead_digit_value , True
			else :
				return l_bound_clks+lead_digit_value , False
		else :
			print('in else',i)
			return 1 , True		



num_tests = input()

n_attempts = 3 
if num_tests.isdecimal() :
	print ('test cases :',num_tests)
	for i in range(int(num_tests)) :
		for a in range(n_attempts) :
			dspl_num = input()
			if dspl_num.isdecimal() :
				key_press,key_type_plus = findNearestEN(d_num = dspl_num)
				print ('Press {} key {} times'.format(('+' if key_type_plus else '-'),key_press ))
				break
			else :
				print('Not a valid input, takes only integer')
				