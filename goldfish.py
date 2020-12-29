#Dec 28th  adding features to switch case
# version 1.0
#currently only one switch works, working on infinite switch cases
#good news is switch works inside a function now

#need to add ability of doing numbers in switch
#finally have momentum

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


