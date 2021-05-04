# -*- coding: utf-8 -*-


#from snoopy1 import *     # case numbers
#from switch_module3 import *  #normal case words
#from switch_mod2backup import *  #normal case words
#from switchmod4gold import *

#import importlib
import switch_case_module
from switch_case_module  import *  #april 29th, 2021 flailing

#import switchmodtrial7  #the one I ahve been using
#import switch_module3
#from switchmodtrial7  import *  #april 29th, 2021 flailing

#import switch_mod2backup
#from switch_mod2backup  import *  #april 29th, 2021 flailing

#from pre_versionworkingfallsjan26th import *

######################
##   clear()
#######################
#reset switchmodtrial7 module
#def clear():#reset sw
#	importlib.reload(switchmodtrial7)
	



#this is  input variable exp for switch(exp)
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")

clever('rasberries and cream') #this would change varholder[0] 

sw = '''
	switch(exp) {
		case 'rasberries and cream':  
			print("wheres the cream house")
			print("tastes good")
			break
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche...")
			break
			
		case 'macbook pro':
			print('fast laptop')
			print("when will the code work...")
			fallthrough
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''
endswitch(sw)

print("========MIDDLE EARTH THERE ======")
print("========MIDDLE EARTH THERE ======")
print("========MIDDLE EARTH THERE ======")

print("duplicate switch doign first one a second time to see the difference")
print("=== tennis soon ===")

clever('gone fishing') #this would change varholder[0] 

sw = '''
	switch(exp) {
		case 'rasberries and cream':  
			print("where's the cream house!")
			print("tastes good")
			break
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche...")
			break
			
		case 'macbook pro':
			print('fast laptop')
			print("when will the code work...")
			fallthrough
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''
endswitch(sw)



clever('star wars') #this would change varholder[0] 

print("-----3rd switch -------")

sw ='''
	switch(exp) {
		case 'star trek':  
			print(\"energize!\")
			print("beam me up")
			print("Captain Kirk")
			break
	
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			fallthru
		
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)



#print("testing THIRD switch")


#clever('starbucks') #this would change varholder[0] 

print("3rd switch -------")

#sw =
'''
	switch(exp) {
		case 'cholpolty':  
			print(\"burrito!\")
			print("bowl")
			print("lemonade")
			break
	
		
		case 'panda express':
			print('good food')
			print("in hollister ")
			fallthru
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			break
			
		default:
			print('no results')
			print("that is all")
			break
}
'''
#endswitch(sw)





#clever('rasberries and cream') #this would change varholder[0] 

#print("=====  3nd switch =====")
#print("=====  3nd switch =====")
#print("=====  3nd switch =====")




#print("third times a charm")

#clever('ufos are real') #this would change varholder[0] 












#sw = 
'''
	switch(exp) {
		case 'fishy':  
		case 'two da':
		case 'three da':
			print(\"squirt gun!\")
			print("water everywhere")
			break

			
		case 'big bird':
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break

		case 'Israel canal':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case 'ufos are real':
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
#endswitch(sw);clear()






#print("========after second switch ends ======")
#print("========after second switch ends  ======")
#clever('big bird') #this would change varholder[0] 

#this is the code being run
#sw = 
'''
	switch(exp) {
		case 'fishy':  
		case 'two da':
		case 'three da':
			print(\"squirt gun!\")
			print("water everywhere")
			break

			
		case 'big bird':
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break

		case 'Israel canal':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case 'ufos are real':
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
#endswitch(sw)


#clever('12')

#number test faster just uncomment it and above comment endswitch(sw)#sw ='''

#sw_reset()


#clever('7') #this would change varholder[0] 




	
#sw = 
'''
	switch(exp) {  
		case 1 thru 5:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 6 to 10:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			break
			
		 
		case 11 to 15:
			print('mocha blast')
			print('== 31 flavors===')
			

			

		case 16 to 20:
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			
			
			
		case 26:
			print('oh yeah')
			print('tahoe here I come')
			break
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
            break
}
'''
#endswitch(sw)



    
    
    
#identical copy to see what happens     

'''
let's look in case_main_body_list 
['starter', 
'\t\tprint("wheres the cream house")\n\t\tprint("tastes good")\n\t\t',
"\t\tprint('fallen leaf lake')\n\t\t",
'\t\tprint(\'where is the gti\')\n\t\tprint("really a porsche...")\n\t\t',
'\t\tprint(\'fast laptop\')\n\t\tprint("when will the code work...")\n\t\t',
'\t\tprint(\'six walking duck de fa ul t\')\n\t\tprint("flying geese")']

'''
