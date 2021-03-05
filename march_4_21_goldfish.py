#dec 24, 2020 christmas eve testing module development of switch case
#computer has no intelligence, code has no intelligence
#the code doesn't know what it's doing
#from importlib import reload


#from rescued_firefallsyosemitejan28 import *
from march_4_21_firefall_yosemite_falls import *  #this is the switch case module
#from pre_versionworkingfallsjan26th import *

    
#this is  input variable exp for switch(exp)
print("===== FIRST 1st switch =====")

clever('snoopy was flying') #this would change varholder[0] 
#maybe test put endswitch(sw) inside of clever function hidden
sw = '''
	switch(exp) {
		case 'snoopy was flying':  
		case 'linus':
		case 'lucy':
			print(\"where's the dog house!\")
			print("first prize")
			print("you block head Charlie Brown")
			

		case 'colin likes ice cream':  
		case 'blake':
			print("coding right now")
			print("================")
			
			
		case 'thank god':  
		case 'table':
			print("lucky to have bbedit")
			print("=for my backups=")
			print("----------------------")
			

		case 'william pilot':
			print("jet figher pilot extroideniare\")
			print("-------------")
			get('phantom jet')
			
			
			
		case 'xmas':
		case 'newyears':
			print('christmas')
			print('new years eve')
			
			
		case 'panera':
		case 'peanuts':
			print('four try again')
			
			
		
		case 'motel6 in gilroy':
		case 'travelcenter':
			print('nice place to stay')
			
			

		case 'alpine meadows':
		case 'squaw':
			print('ski fast in the powder')
			
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			
			
}
'''
endswitch(sw)

#print the starting values of each list for reference

# quote you already write your software twice 
#the first time is write it learn what you are doing
#the second time is what you intended to do the first time
#philosphy handling the unforeseen cirumstances
#series of practices
#the progarm (code) has to do what you say it has to do.

#the goal it does what it's suppposed to do concisely and readability
#to later read the code and undrestand what's going on

# bug preventation
 


print("==///***===in middle between two switch cases what happens===///***=====")
 #2nd switch attempt
 #from first switch case 

#print("result of switch in varholder[1]",varholder[1])


#reset()
#import importlib
#import firefall_yosemite_falls
#importlib.reload(firefall_yosemite_falls)

#print("===== SECOND 2nd switch =====")
#I used two words here instead of one that might trigger a bug
#clever('phantom') #this would change varholder[0] 

#sw = '''
#	switch(exp) {
#		case 'cat in the hat':  
#		case 'thing one':
#		case 'thing two':
#			print(\"dr seus!\")
#			print("funny trees")
#			print("grinch stole christmas")
#			break
#
#		
#			
#		case 'bicycle':  
#		case 'tricycle':
#v			print("keep pedaling")
#			print("=good bike=")
#			get('schwin')
#			print("----------------------")
#			break
#
#		case 'phantom':
#			print("now this is cool triggered")
#			print("from which case above")  
#			print("-pass thru--")
#			break
#			
#			
#		default:
#			print('six flying turkey')
#			print("flying turkey")
#			
#}
##'''
##endswitch(sw)
#'''
 


#print("===== THIRD 3rd switch =====")

#clever('rain') #this would change varholder[0] 

#sw = '''
#	switch(exp) {
#		case 'bird in the hat':  
#		case 'first one':
#		case 'second two':
#			print(\"dr seus!\")
#			print("funny trees")
#			print("grinch stole christmas")
#			break

#		
#			
#		case 'rain':  
#		case 'snow':
#v			print("big rain")
#			print("nice rain=")
#			get("week long storm")
#			print("----------------------")
#			
#
#		case 'porsche':
#			print("dream car")
#			print("---to Tahoe-----")
#			break
#			
#			
#		default:
#			print('five flying crows')
#			print("walking crows")
#			
#}
#'''
#endswitch(sw)





###=======
#this would go just above the switch case
#what if I have a function which is in yosemitefalls
#that has the string and instead of a docstring
#I am using a funciton and the switch is the argument
#we would see the switch code but it's attached so i could
#have a function call for function in yosemitefalls
#so I get the best of both worlds
# try it
###========================================
#this will be the switch case code 
#weird idea. we see the switch code here but it's a comment
#and the function converts it to the real code docstring long multiline
#variable inside of yosemite falls (so the twins solution)
#sow what we see here is fake 
#so this means it's fake imaginary
#and real switchcasetester is in yosemitefalls and
#what we see here is merely an illusion

### what we know is that the string for switch case
## must be in the yosemite_falls file. yet we are in
## the goldfish file.
##so the switchcase string must be in the other file
## so if the string here can manipulate the switch code
## through a function for writing to the file that might help

#galaxy('''print('test')''')

#the switch case javascript string is in yosemite_falls.py


########### dec 31st solution for "alpine meadows" it will become alpine_meadows
#I can do a band-aid solution for input into clever to have
#it add _ between words so it's treated as one word
#and go thru the input switch case input string and concat_ between case names
#and then it will work

#####################