
def calcCafeVertices(args) :

	n,v,h,a,b,c,d,e,f,m = args

	vh_list = [(v,h)]
	v_cur,h_cur = v,h

	for i in range(1,n) :
		v_next = ( v_cur * a + b * h_cur + c) % m
		h_next = ( v_cur * d + e * h_cur + f) % m

		vh_list.append((v_next,h_next))

		v_cur,h_cur = v_next,h_next

	return vh_list

def getValidCircles(vertices) :

	val_circles = []

	if vertices:
		# same line pairs combo with another vertex
		slp_list= getSLPMatches(vertices)
		if slp_list:
			val_circles.extend(slp_list)

		non_slp_list = getNonSLPMatches(vertices)
		if non_slp_list:
			val_circles.extend(non_slp_list)

	return val_circles

def getNonSLPMatches(vertices_list):
	
	v_length = len(vertices_list)

	vortex_generator = getTrplVrtx(vertices_list)
	valid_triplet_count = 0

	for vortex in vortex_generator:
		#print(vortex)
		vrtx_1,vrtx_2,vrtx_3 = vortex
		z_vrtx = zip(vrtx_2,vrtx_3)
		if vrtx_1[0] in (vrtx_2[0],vrtx_3[0]) or vrtx_1[1] in (vrtx_2[1],vrtx_3[1]) or isVortxValid(vortex):
		#if (vrtx_1[0] in (*z_vrtx)[0]) or (vrtx_1[1] in (*z_vrtx)[1]) or isVortxValid(vortex):
			print(vortex,'forms valid circle')
			valid_triplet_count += 1
			continue

		print(vortex,'does not form valid circle')
			
	print('Total valids:',valid_triplet_count)	

def isVortxValid(vrtx) :
	
	s_vortices = sorted(vrtx,key=lambda v:v[0])		
	f_vortex = s_vortices[1]
	g_vortex_1,g_vortex_2 = s_vortices[0],s_vortices[2]

	if (g_vortex_1[1] > f_vortex[1] and g_vortex_2[1] > f_vortex[1]) or \
		(g_vortex_1[1] < f_vortex[1] and g_vortex_2[1] < f_vortex[1]):
		return True
	else :
		return False


def getTrplVrtx(vrtx_list):
	
	v_len = len(vrtx_list)

	for i in range(v_len-2):
		for g in range(1,v_len-i-1):
			for k in range(i+1,v_len-g):
				yield (vrtx_list[i],vrtx_list[k],vrtx_list[k+g])


if __name__ == "__main__" :

	while True:
		num_tests = input()

		if num_tests.isdecimal() :
			print ('test cases :',num_tests)
			for i in range(int(num_tests)) :
				
				n,v,h,a,b,c,d,e,f,m = (int (i) for i in input().split())
				args = (n,v,h,a,b,c,d,e,f,m)
				
				cafe_vertices = calcCafeVertices(args)
				print(cafe_vertices)
				getNonSLPMatches(cafe_vertices)
				'''
				valid_circles_list = getValidCircles(vertices=cafe_vertices)		
				print('valid circles count:',len(valid_circles_list))
				print('valid circles:',valid_circles_list)
				'''
		else:
			break