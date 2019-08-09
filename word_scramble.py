
def createString(args) :

	s1,s2,n,a,b,c,d = args
	
	x_pprev= ord(s1)
	x_prev = ord(s2)
	st_ref = ''.join([s1,s2])
	#print('first',st_ref)
	for i in range(n-2) :
		x = ( a * x_prev + b * x_pprev + c) % d
		str_c = chr(97+(x % 26))
		st_ref = ''.join([st_ref,str_c])
		#print(st_ref)
		x_pprev,x_prev = x_prev,x

	return st_ref 	

def getMatches(words,ref_string) :

	m_count = 0
	match_segs=[]
	

	for word in words :

		print('word',word)
		word_match = False
		first_ch = word[0]
		last_ch = word[-1]
		word_len = len(word)

		for j in range((len(ref_string)-word_len)+1) :
			if (ref_string[j] == first_ch and ref_string[j+word_len-1] == last_ch) :
				#match_segs.append((j,j+word_len-1))
				m = (j,j+word_len-1)
		#for m in match_segs:
				str1 = ''.join(sorted(ref_string[m[0]+1:m[1]]))
				str2 = ''.join(sorted(word[1:-1]))
				print('str', str1,str2)
				if (str1 == str2) :
					print('matches',m[0],m[1])
					word_match = True
					m_count += 1
					break

	return m_count




num_tests = input()

n_attempts = 3 


if num_tests.isdecimal() :
	print ('test cases :',num_tests)
	for i in range(int(num_tests)) :
		dict_count = int(input())
		word_list = input().split()
		if len(word_list) > dict_count :
			word_list = word_list[:dict_count]
		s1,s2 = ((input().lower()).split())
		n,a,b,c,d = (int (i) for i in input().split())
		args = (s1,s2,n,a,b,c,d)
		
		m_string = createString(args)
		print(m_string)
		match_count = getMatches(words=word_list,ref_string = m_string)		
		print('match_count',match_count)