#dec 24, 2020 christmas eve testing module development of switch case
#computer has no intelligence, code has no intelligence
#the code doesn't know what it's doing

from angel_falls import *  #this is the switch case module


#this is  input variable exp for switch(exp)

clever('5') #this would change varholder[0] 
# so when switch called in parser teh first test is to determine string or number
#if input number in clever for exp then cases will be not in strings
###  test  case 1 thru 3:
###  fuck I think I can use replace if "thru" in line
#make list after case position [1] is first number [2] is thru and [3] is end number
# so I would know  since words aren't in the casess
#but I would convert it to putting the numbers into strings which then works
# I can do that with a replace
sw = '''  
	switch(exp) {  
		case 1:
		case 2:
		case 3:
			print(\"where's the dog house!\")
			print("first prize")
			print("you block head Charlie Brown")
			break

		case 4:  
		case 5:
			print(\"keep going!\")
			print("taught me how to write code")
			break
			
		case 6:  
		case 7:
			print("make some ketchup")
			print("== you gotta work===")
			break

			

		case 8:
			print('ski fast in the powder')
			print("sweet powder snow, lovely snow")
			break
			
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