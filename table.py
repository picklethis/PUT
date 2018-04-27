#! bin/bash/python3

def primes(n): # simple Sieve of Eratosthenes 
	odds = range(3, n+1, 2)
	sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds],[]))
	return [2] + [p for p in odds if p not in sieve]
   
  
data_list = []   
start_num = int(input("Enter the starting Number 1-?: "))
counter = start_num
meta_data_list = []
stop_num = int(input('Enter the stopping point:  '))

while counter <= stop_num:
	rout_list = []
	num = counter
	# Prime Check
	if num in primes(num):
		rout_list.append('x')
	else:
		rout_list.append('-')
	# Super Prime Check
	sp = (2 * num - 1)
	if num in primes(num) and (sp) in primes(sp):
		rout_list.append('x')
	else:	
		rout_list.append('-')
	# Left Inflection Point Check	
	if num in primes(num) and num+2 in primes(num+2):
		rout_list.append('x')
	else:
		rout_list.append('-')	
	# Right Inflection point
	if num in primes(num) and num-2 in primes(num-2):
		rout_list.append('x')
	else:
		rout_list.append('-')
	
	rout_list.append(counter)
	data_list.append(rout_list)
	text = 'Prime: {}, Super-Prime: {}, LinPoint: {}, RinPoint: {}, Number: {}'
	print(text.format(rout_list[0],rout_list[1],rout_list[2],rout_list[3],rout_list[4]))	
	
	counter = counter + 1 	
	
print('Finished tabulamating...now meta')
if data_list:
	lp_ctr = 0	
	dlp_ctr = 0
	dist_list = []
	sp_ctr = 0
	dsp_ctr = 0
	dsp_dist_list = []
	sp_infpoint = 0
	pm_ctr = 0
	
	for num_data in data_list:
		if num_data[0] == 'x':
			pm_ctr = pm_ctr + 1
		if num_data[1] == 'x':
			sp_ctr = sp_ctr + 1
			dsp_dist_list.append(dsp_ctr)
			dsp_ctr = 0
		if num_data[2] == 'x':
			if num_data[1] == 'x':
				sp_infpoint = sp_infpoint + 1
			lp_ctr = lp_ctr + 1
			dist_list.append(dlp_ctr)
			dlp_ctr = 0
		if num_data[3] == 'x' and num_data[1] == 'x':
			sp_infpoint = sp_infpoint + 1
	
		dlp_ctr = dlp_ctr + 1 
		dsp_ctr = dsp_ctr + 1
		
	#space for making file with dataset, sig numbers, start/stop
	#line1 = 'Start: {} , Stop: {} , #IP: {} , #SP: {} , #SPIP 
	#repo_path = '/home/pi/Coding/PUT/work_files/latest.txt'
	#repo _obj = open(repo_path,'w')
	
	
	print('Inflection points in sample: {0}, Super Primes in Sample: {1}, SP Inflection Points: {2}'.format(lp_ctr,sp_ctr,sp_infpoint))
	print('Primes in Sample: {}'.format(pm_ctr))
	print('LipDistances... {}'.format(dist_list))
	print('SpDistances...  {}'.format(dsp_dist_list))



print("Complete, :-)")







