#dec 24, 2020 christmas eve testing module development of switch case
#computer has no intelligence, code has no intelligence
#the code doesn't know what it's doing

from new_yosemite_falls import *  #this is the switch case module


#this is  input variable exp for switch(exp)

clever('colin took the frosting off the cake') #this would change varholder[0] 

sw = '''
	switch(exp) {
		case 'snoopy has a doghouse':  
		case 'linus':
		case 'lucy':
			print(\"where's the dog house!\")
			print("first prize")
			print("you block head Charlie Brown")
			break

		case 'colin took the frosting off the cake':  
		case 'blake':
			print("from my birthday cake!!!!")
			break
			
		case 'tomato':  
		case 'table':
			print("make some ketchup")
			print("== you gotta work===")
			fallthrough

		case 'william':
	
			print("jet figher pilot extroideniare\")
			break
			
		case 'xmas':
		case 'newyears':
			print('christmas')
			print('new years eve')
			break
			
		case 'panera':
		case 'peanuts':
			print('four try again')
			fallthrough
			
		
		case 'motel6':
		case 'travelcenter':
			print('nice place to stay')
			break
			

		case 'alpine meadows':
		case 'squaw':
			print('ski fast in the powder')
			print("sweet powder snow, lovely snow")
			fallthru
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			
}
'''
endswitch(sw)


 
 


 









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