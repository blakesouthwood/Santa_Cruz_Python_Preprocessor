#Dec 28th  adding features to switch case
# version 1.0
#currently only one switch works, working on infinite switch cases
#good news is switch works inside a function now

#need to add ability of doing numbers in switch
#finally have momentum

#Note for the switch case notice the indentation used
# It is based on 4 space tabs
# 1 tab for switch
# 2 tabs for case
# 3 tabs for code inside of case
# this format of tabs in the switch case is copied and used for the python generated switch
# so it's important and imperative that you adopt this format until I add auto-indent facilitated with lovely braces { }
# I completely  abhore the tab indentation rules in Python I think they are pure ballony
# so in the near future it's pure JavaScript/C  braces with automatic tabs added using fuzzy logic patterns
# I have wasted so much precious time with mindless indentation errors in my code in Python
# JavaScript doesn't care about indentation and neither should Python
# If you notice with this radical switch case in python I'm making a hybrid blend of Python that is
# going to be way more user-friendly and make sense to true programmers and will result in coding much faster

from switch_mod import *  #this is the switch case module


def cool():
	print("cool running now")
	clever('olaf') #this would change varholder[0] 
	sw = '''
	switch(exp) {
		case 'snoopy':  
		case 'linus':
			print(\"where's the dog house!\")
			print("first prize")
			break

		case 'olaf':  
		case 'tim':
			print(\"tennis wannabees!\")
			print("what is the score again")
			break
			
		case 'tomato':  
		case 'table':
			print("make some ketchup")
			print("== you gotta work===")
			break

		case 'tahoe':
		case 'donner':
			print("will I live there some day\")
			
			
		case 'fish':
		case 'marsbar':
			print('third  section')
			print('working on this')
			
		case 'panera':
		case 'peanuts':
			print('four try again')
		
		case 'bestwestern':
		case 'travelcenter':
			print('nice place to stay')
			break
			

		case 'alpine':
		case 'squaw':
			print('ski fast in the powder')
			break
			
		default:
			print('six walking duck de fa ul t')
			print("no matches")
			break
}
'''
	endswitch(sw)  #this calls the parser and codegenerator

	
cool()
#reset_clever()


