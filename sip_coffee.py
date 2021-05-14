

# -*- coding: utf-8 -*-


#from snoopy1 import *     # case numbers
#from switch_module3 import *  #normal case words
#from switch_mod2backup import *  #normal case words
#from switchmod4gold import *

#import importlib
import mrcoffee_mocha
from mrcoffee_mocha  import *  #april 29th, 2021 flailing

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
	

print('drinkcoffee file being used here"')
print("==================")

#this is  input variable exp for switch(exp)
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")


print("now to string switch see what happens")

clever('rasberries and cream') #this would change varholder[0] 

sw = '''
	switch(exp) {
		case 'rasberries and cream':  
			print("wheres the cream house")
			print("tastes good at cafe borrone")
			
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche...")
			
			
		case 'macbook pro':
			print('fast laptop')
			print("when will the code work...")
			break
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''
endswitch(sw)






clever('14')

sw = '''
	switch(exp) {  
		case '1':
		case '2':
		case '3':
		case '4':
		case '5':
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru

		case '6':
		case '7':
		case '8':
		case '9':
		case '10':
			print('kangaroo hop hop!')
			print('taught me how thru write code')
			break
					 
		case '11':
		case '12':
		case '13':
		case '14':
		case '15':
			print('mocha blast')
			print('== 31 flavors===')
			print('== at Starbucks in Gilroy ===')
				

		case '16':
		case '17':
		case '18':
		case '19':
		case '20':
			print('sweet sixteen ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
			
		case '21':
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		case '26':
			print('oh yeah')
			print('tahoe here I come')
			fallthru
			
		case '27':
			print('fuck yeah')
			print('go baby go fly dammit')
			fallthrough
			
		case 'default':
			print('six walking duck de fa ul t')
			print('flying geese')
			
			break
}
'''
endswitch(sw)




print("duplicate switch doign first one a second time to see the difference")
print("=== tennis soon ===")



print("========MIDDLE EARTH THERE ======")
print("========MIDDLE EARTH THERE ======")
print("========MIDDLE EARTH THERE ======")

print("remember for testing the macro expansions should already")
print("be completed for it to work in the strings parser")




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




#
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


clever('starbucks') #this would change varholder[0] 

#print("3rd switch -------")

sw ='''
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
endswitch(sw)





#clever('rasberries and cream') #this would change varholder[0] 

#print("=====  3nd switch =====")
#print("=====  3nd switch =====")
#print("=====  3nd switch =====")


#this runs by itself going through the string parser and codegen
#but currently it doesn't clean up (empty) the lists so then following switches fail.
# a word and this number switch ran but with bugs with numbers running first
#this is the scenario of the macros already unfurling the cases and to and thru macros expanded

print("now for the numbers test after a word test")


print("line_numbers_with_first_cases",line_numbers_of_first_cases)
print('this is after attempting to do a numbers switch in the string switch parser')
print("=======///=======2222=====")
print("list_of_rows_of_case_names ", list_of_rows_of_case_names )
del list_of_rows_of_case_names[:]
print("list_of_rows_of_case_names ", list_of_rows_of_case_names )

print("")
print("case_main_body_list_with_tail",case_main_body_list_with_tail)
print("smartcasemanager",smartcasemanager)
print("royallist",royallist)
print('candy',candy)
print("digitalcandy",digitalcandy)
print("drive_thru",drive_thru)
print("wilecoyote",wilecoyote)
print("seal",seal)
print('british',british)
print('penguin',penguin)
print("case_main_body_list",case_main_body_list)
print("palmtrees",palmtrees)
print("roadrunner",roadrunner)
print("starbuckslist",starbuckslist)
print('cranberries',cranberries)
print('einstein',einstein)
print("caselist1",caselist1)
print("caselist2",caselist2)
print("caselist3",caselist3)
print("caselist4",caselist4)
print("caselist5",caselist5)
print("caselist6",caselist6)
print("caselist7",caselist7)
print("caselist8",caselist8)
print("caselist9",caselist9)
print("caselist10",caselist10)



clever('26')

sw = '''
	switch(exp) {  
		case '1':
		case '2':
		case '3':
		case '4':
		case '5':
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru

		case '6':
		case '7':
		case '8':
		case '9':
		case '10':
			print('kangaroo hop hop!')
			print('taught me how thru write code')
			break
					 
		case '11':
		case '12':
		case '13':
		case '14':
		case '15':
			print('mocha blast')
			print('== 31 flavors===')
			print('== at Starbucks in Gilroy ===')
					

		case '16':
		case '17':
		case '18':
		case '19':
		case '20':
			print('sweet sixteen ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
			
		case '21':
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		case '26':
			print('oh yeah')
			print('tahoe here I come')
			fallthru
			
		case '27':
			print('fuck yeah')
			print('go baby go fly dammit')
			break
			
		case 'default':
			print('six walking duck de fa ul t')
			print('flying geese')
			
			break
}
'''
endswitch(sw)


#print("third times a charm")

clever('ufos are real') #this would change varholder[0] 

print("testing with: ufos are real")

sw = '''
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
			
		case 'ufos are real':
			print('navy tic tac ufos')
			print("havy flying pyramids with night vision hovering")
			break
			
		case 'israel canal': 
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
endswitch(sw);



print('first a string swith test')


#print("========after second switch ends ======")
#print("========after second switch ends  ======")
clever('big bird') #this would change varholder[0] 

#print("testing with big bird")

#this is the code being run
sw = '''
	switch(exp) {
		case 'fishy':  
		case 'two da':
		case 'three da':
			print(\"squirt gun!\")
			print("water everywhere")
			
			
		case 'big bird':
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			
			
		case 'israel canal':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			break
			
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
endswitch(sw)
#this is what the input will look like after the macros expand
#this is trying to run numbers through string paraser and codegen
#may 11th 2021  attempt
#it ran perfectly by itself until I tried a string switch before it.




#clever('12')

#number test faster just uncomment it and above comment endswitch(sw)#sw ='''

#sw_reset()


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
print("===========")
print("now we will test numbers switch case")
print("===========")
#print('THIS IS THE FAMOUSE MIDDLE EARTH TEST HERE')



#### this one is not turned on yet but is the format for the final version
#going up in a few days from May 13th so by the 15th.
#clever('21') #this would change varholder[0] 


	
#sw =
'''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			fallthru
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
#endswitch(sw)

#### this one is not turned on yet but is the format for the final version
#going up in a few days from May 13th so by the 15th.
#print("about to attempt 2nd numbers switch case")
#clever('1') #this would change varholder[0] 

####=========== this is what the true input would look like"
	
#sw =
'''
switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			fallthru
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
#endswitch(sw)





print("should be dog house first switch")
print("========")
print("should be  31 flavorst second numbers switch")
print("---- time for popcorn and a movie and ribs-----")
    
    