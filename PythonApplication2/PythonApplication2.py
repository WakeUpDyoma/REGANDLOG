﻿from Funktsioonid import *

users=loe_failist_listisse("users.txt")
passwords=loe_failist_listisse("passwords.txt")
print(users)
print(passwords)
while True:
	print("Reg - 1,Arv - 2,Välja - 3")
	v=int(input())
	if v==0:
		koik_kasutajad(users,passwords)		
	elif v==1:
			print("Registreerimine")
			while 1:
				log=input("Kasutajatunnus - ")
				if log not in users:
					print("Tunnus soobib")
					break
				else:
					print("See nimi juba on olemas listis")		
			v=input("Arvuti-A või ise-I loob parool - ")
			if v.upper()=="A":
				pas=passautomat()
			elif v.upper()=="I":			
				while 1:
					pas=input("Sisesta oma parool - ")
					tulemus=paskontroll(pas)
					if tulemus==True:
						users.append(log)
						passwords.append(pas)
						break
					
	elif v==2:
		print("Avtoriseerimine")
		if passwords.index(pas)==users.index(user):		
	elif v==3:
		print("Välja")
		faili_sisu_umberkirjutamine("users.txt",users)
		faili_sisu_umberkirjutamine("passwords.txt",passwords)
		quit()
		#valmis
	else:
		print("On vaja valida 1,2 või 3")# kõik on olemas
