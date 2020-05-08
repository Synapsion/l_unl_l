import re

def get_l_palindrome(orig_str,sub_length) :
	l_palindrome = None
	os_length = len(orig_str)
	p_length = sub_length

	print('p_length',p_length)
	if sub_length > 2 :
		if os_length == p_length :
			if p_length % 2 == 0 :
				p_length -= 1
		
		init_runs = (os_length - p_length) + 1

		for run in range(init_runs):

			end_index = run + p_length
			print('end_index',end_index)
			sub_str = orig_str[run:end_index] 
			print('sub_str',sub_str)
			is_Palindrome = check_palindrome(p_string = sub_str )
			if is_Palindrome :
				l_palindrome = sub_str 
				return l_palindrome
		l_palindrome = get_l_palindrome(orig_str,sub_length = p_length-2)

	return l_palindrome

def check_palindrome(p_string) :
	is_Palindrome = False
	str_len = len(p_string)

	print (str_len,str_len % 2)

	if p_string :
		if str_len % 2 == 1 :
			mid_char_index = int((str_len + 1) / 2 ) - 1
			p_string_left = p_string[0:mid_char_index]
			p_string_right = p_string[mid_char_index+1:]

			print('p_string halves',p_string_left,p_string_right)

			if p_string_left == p_string_right[::-1] :
				is_Palindrome = True
	
	return is_Palindrome

if __name__ == "__main__":
	
	atttempts = 0


	while atttempts < 3 :
		input_str = input('Enter a text string(with no spaces/tabs):')
		mod_str = ''.join(re.split(r'\s|\?|\!|\.|\'|\"',input_str))

		if input_str :
			
			l_palindrome = get_l_palindrome(orig_str=mod_str,sub_length = len(mod_str))

			if l_palindrome :
				print('Longest Palindrome : ',l_palindrome)
			else :
				print('String does not contain any Palindromes')

			continue_flg = input('Press ''y'' to try again, \'n\' to stop')
			if continue_flg.lower() == 'y' :
				atttempts = 0
				core_str = ''
			else :
				break
		else :
			print ('Please enter a valid string. {} atttempts remain'.format(2-atttempts)) 

		atttempts += 1