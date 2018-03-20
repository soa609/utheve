def setTxt():
	global txt, txtlines
	f = open('txtfile.txt','r')
	txt = f.read()
	f.close()
	#f = open('txtfile.txt','r')
	#txtlines = f.readlines()
	#f.close()

def txtWords():
	


def consecSent():
	sentcount = 0
	sentcountarray = []
	if('...' in txt):
		sentcount = -2
	for i in txt:
		if(i == '.'):
			sentcount += 1
		elif(i == '!'):
			sentcount += 1
		elif(i == '?'):
			sentcount += 1
		if(i == '\n'):
			sentcountarray.append(sentcount)
			sentcount = 0

	return sentcountarray, sentcount


def txtLen():
	subcount = 0
	for i in txt:
		if(i == '\n'):
			subcount = subcount + 1
	return len(txt)-subcount

def adjectiveDB():
	badadj = ['veldig']




setTxt()
print(consecSent())
print(txtLen())


x = input('pause')
