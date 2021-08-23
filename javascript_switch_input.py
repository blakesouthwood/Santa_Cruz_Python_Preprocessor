#backup test_inputs_beta.py
#from github


#942 lines (695 sloc)  19 KB
  
# test_inputs_beta.py  showing proof of concept of C style switch case in python
# also demonstrating macros to and thru working with numbers cases
#######################################################
# official_switch_case_silver.py  works in conjuction with test file test_inputs_beta.py
# developed solely by Blake Southwood  this is version 1.0
# June 10th, 2021  I live in Silicon Valley south of San Jose in California
# southwood.blake@gmail.com
# I live in Gilroy, CA and will relocate.
# I am currently looking for a full time python developer job.
# I am in the process of refactoring this code base but wanted
# to get it working and stable first.
####################################################### 

# -*- coding: utf-8 -*-

import working_switch_module
from working_switch_module  import *  


	

print('drinkcoffee file being used here"')
print("==================")

#this is  input variable exp for switch(exp)
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")
print("===== FIRST 1st switch =====")


print("now to string switch see what happens")

#show_generated_code()
# I don't know if this works yet

#this is the code being run
#this needs to be sensed to turn it 
# into strings, just stringifying it
#triggered after determing it's NOT A NUMBER case
#it can be alphanumeric words3 example
#txt = "Company12"
#print(x)
#x = txt.isupper()
#x = txt.isalnum() #alphanumeric
# returns True
#txt = "compnay12"
#x = txt.islower() #lowercase

clever('STARBUCKS')
#right now it NEEDS to take strings to digest and parse it"
#I need to add my new code for this to work properly"
show_input_switch_string()   #input so what the string right below here
show_generated_code()
print("what does it show True or False to show input string")
print(show_input_string[0])
print("== switch 1 ==")
print("--------")

sw =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			break
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third attempt")
			print("deer and quail about")
			
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case AMERICA:
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break
}
'''
endswitch(sw)

#clever('LAKE_TAHOE') #might have to be lowercase lake_tahoeshow_generated_code()

#it might have to be converted to lowercase and _ removed to work
#see if this works 
#show_input_switch_string() #for testing this shows the input string
#hide_input_switch_string()
clever('COYOTE')	
show_input_switch_string()   #input so what the string right below here
show_generated_code()  #show_  hide_
# this example goes through strings since nonumber detected
# this works as is as regular string
print("catch the rabbit")
print("switch 2")
print("--------")


sw =''' 
	switch(exp) {
		case 'CASPER':
			print("squirt gun!")
			print("water everywhere")
			break
			
		case 'COYOTE':
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case 'LAKE_TAHOE':
			print("big dipper")
			print("constellation")
			print("milky way galaxy")
			print("fallen leaf lake")
			break
			
		case 'FRANCE':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case 'AMERICA':
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

print("===== end of first test of switch case with flags ====")
show_input_switch_string()   #input so what the string right below here
show_generated_code()

clever('rasberries and cream') #this would change varholder[0] 

#show_generated_code()

print("switch 3")
print("--------")

sw ='''
	switch(exp) {
		case 'rasberries and cream':  
			print("wheres the cream house")
			print("tastes good at cafe borrone")
			break
			
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







#clever('3') #this would change varholder[0] 









hide_input_switch_string()   #input so what the string right below here
show_generated_code()

clever('gone fishing') #this would change varholder[0] 

#show_generated_code()
print("switch 4")
print("--------")


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



show_input_switch_string()   #input so what the string right below here
show_generated_code()
#
clever('star wars') #this would change varholder[0] 

#hide_generated_code() #from this point forward

print("switch 5")
print("--------")

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


	
#then 7 to 8
#print("testing THIRD switch")


print("testing tumbler adding numbers and will concat strings using fallthru next")
print("today is may 21st, 2021")
print("today is may 27th thursday, 2021")


#

#print("3rd switch -------")

#I can do a function call brilliant concat('the') 
#this way it's outside the realm of the switch

targetlist[0] = 0
buildstringlist[0] = 0

def reset_sutter_and_buildstring():
	print("just reset adder and buildstring()")
	targetlist[0] = 0
	buildstringlist[0] = 0
	
	
###############
#sutter and buildstring
#adder(x) is adder
#buildstring(x) concats string thru fallthrus

reset_sutter_and_buildstring() #for adder() and buildstring()
clever('panda express')
#show_input_string()   #input so what the string right below here
#show_generated_code() #output


show_input_switch_string()   #input so what the string right below here
show_generated_code()

print("switch 6")
print("--------")

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
			adder(2)
			buildstring('merry')
			print('BARK')
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3) #this won't do anything until it is executed
			buildstring(' christmas')
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(7)
			buildstring(' and happy new year')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)

print("after the switch case we have... drum roll please")
#print("apple=",apple)
print("final result=")
#################
#these need to exist be initializedto be utilized

print("result of adder adding",targetlist[0])
print("result of buildstring concatting ",buildstringlist[0])
#targetlist[0] = 0
#buildstringlist[0] = 0


clever('panda express') #this would change varholder[0] 


targetlist[0] = 0
buildstringlist[0] = 0
reset_sutter_and_buildstring() #adder and buildstring



show_input_switch_string()   #input so what the string right below here
show_generated_code()
#hide_generated_code()	

print("switch 7")
print("--------")

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
			adder(1)
			buildstring('soon it')
			print('BARK')
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(2) #this won't do anything until it is executed
			buildstring(' will work')
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3)
			buildstring(' and I will celebrate')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)

print("after the switch case we have... drum roll please")
#print("apple=",apple)
print("final result=")
print("result of adder adding",targetlist[0])
print("result of buildstring concatting ",buildstringlist[0])
#targetlist[0] = 0
#buildstringlist[0] = 0



#clever('rasberries and cream') #this would change varholder[0] 

#print("=====  3nd switch =====")
#print("=====  3nd switch =====")
#print("=====  3nd switch =====")


#this runs by itself going through the string parser and codegen
#but currently it doesn't clean up (empty) the lists so then following switches fail.
# a word and this number switch ran but with bugs with numbers running first
#this is the scenario of the macros already unfurling the cases and to and thru macros expanded

print("now for the numbers test after a word test")


# print("line_numbers_with_first_cases",line_numbers_of_first_cases)
# print('this is after attempting to do a numbers switch in the string switch parser')
# print("=======///=======2222=====")
# print("list_of_rows_of_case_names ", list_of_rows_of_case_names )
# del list_of_rows_of_case_names[:]
# print("list_of_rows_of_case_names ", list_of_rows_of_case_names )
# 
# print("")
# print("case_main_body_list_with_tail",case_main_body_list_with_tail)
# print("smartcasemanager",smartcasemanager)
# print("royallist",royallist)
# print('candy',candy)
# print("digitalcandy",digitalcandy)
# print("drive_thru",drive_thru)
# print("wilecoyote",wilecoyote)
# print("seal",seal)
# print('british',british)
# print('penguin',penguin)
# print("case_main_body_list",case_main_body_list)
# print("palmtrees",palmtrees)
# print("roadrunner",roadrunner)
# print("starbuckslist",starbuckslist)
# print('cranberries',cranberries)
# print('einstein',einstein)
# print("caselist1",caselist1)
# print("caselist2",caselist2)
# print("caselist3",caselist3)
# print("caselist4",caselist4)
# print("caselist5",caselist5)
# print("caselist6",caselist6)
# print("caselist7",caselist7)
# print("caselist8",caselist8)
# print("caselist9",caselist9)
# print("caselist10",caselist10)

#print('star trek testing of phaser engines numbers')
#print('in already unfurled state no macros')
#print("this is going through the string parser1")
#print("and is treated like words thus the strings")

print("BIG TEST CAFE")
clever('7')

show_input_switch_string()   #input so what the string right below here
show_generated_code()

print("switch 8")
print("--------")

sw = '''
	switch(exp) {  
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
		case 6:
		case 7:
		case 8:
		case 9:
		case 10:
			print('kangaroo hop hop!')
			print('taught me how thru write code')
			break
					 
		case 11:
		case 12:
		case 13:
		case 14:
		case 15:
			print('mocha blast')
			print('== 31 flavors===')
			print('== at Starbucks in Gilroy ===')
					
		case 16:
		case 17:
		case 18:
		case 19:
		case 20:
			print('sweet sixteen ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		case 26:
			print('oh yeah')
			print('tahoe here I come')
			fallthru
			
		case 27:
			print('fuck yeah')
			print('go baby go fly dammit')
			break
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			
			break
}
'''
endswitch(sw)


#print("third times a charm")

clever('ufos are real') #this would change varholder[0] 

print("testing with: ufos are real")
#hide_generated_code()
hide_input_switch_string()   #input so what the string right below here
show_generated_code()

print("switch 9")
print("--------")

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
#clever('big bird') #this would change varholder[0] 

#print("testing with big bird")
hide_input_switch_string()   #input so what the string right below here
show_generated_code()
#this is the code being run
print("switch 10")
print("--------")


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


clever('big bird') #this would change varholder[0] 

#hide_generated_code()
#this is the code being run

print(" == switch 11 ==")
print("--------")

sw =''' 
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
endswitch(sw)
print("===========")
print("now we will test numbers switch case")
print("===========")
#print('THIS IS THE FAMOUSE MIDDLE EARTH TEST HERE')



#### this one is not turned on yet but is the format for the final version
#going up in a few days from May 13th so by the 15th.
clever('2') #this would change varholder[0] 

print("this is a REAL MACRO TEST ON THE REAL CODE ENGINE ")
#show_input_switch_string()   #input so what the string right below here
#show_generated_code()

show_input_switch_string()   #input so what the string right below here
show_generated_code()
#show_generated_code()
 
print("== switch 12 ==")
print("--------")
 
sw ='''
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
			print('Blake you did it a real good job')
			print('macros working in Python')
			print(' I did it - it works')
			
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
endswitch(sw)

#### this one is not turned on yet but is the format for the final version
#going up in a few days from May 13th so by the 15th.
#print("about to attempt 2nd numbers switch case")
clever('1') #this would change varholder[0] 

show_input_switch_string()   #input so what the string right below here
show_generated_code()
####=========== this is what the true input would look like"
#show_generated_code()
 	
print("== switch 13 ==")
print("--------")

sw ='''
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
endswitch(sw)



clever('fishy') #this would change varholder[0] 

#hide_generated_code()
hide_input_switch_string()   #input so what the string right below here
show_generated_code()
#this is the code being run

print("== switch 14 ==")
print("--------")

sw =''' 
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
endswitch(sw)



#not yet 

#clever('CASPER') #this would change varholder[0] 

#

#print("should be dog house first switch")
#print("========")
#print("should be  31 flavorst second numbers switch")
#print("---- time for popcorn and a movie and ribs-----")
    
clever('9') #this would change varholder[0] 

#print("this is a REAL MACRO TEST ON THE REAL CODE ENGINE ")
#show_generated_code()
show_input_switch_string()   #input so what the string right below here
show_generated_code()

print("== switch 15 ==")
print("--------")

sw ='''
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
			print('what bugs')
			print('== no bugs===')
			break
			
			
		case 21:
			print('Blake you did it a real good job')
			print('macros working in Python')
			print(' I did it - it works')
			break
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
endswitch(sw)

print("about to test FIRST nest switch detection...")
print("testing sensing a switch with another switch in it")
print("== switch 16 ==")
print("--------")

clever('1')
sw ='''
	switch(exp) { #first true test 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){          
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	
endswitch(sw)

#this doesn't execute these it is the preliminary stages of the translation

clever('one')
print("now will attempt to try a more impressive nested switch")
print("== switch 17 ==")
print("--------")
sw ='''
	switch(x) {                        
		case "one":
			print("this is the first  in the main ")
			###### nested inner  1 ##############
			switch(n) #nested sw 1   
				case "testa":
					print("dam did it work?")
					print("yes it's test == one")
					tahoe[0]='victory' 
					fallthru

				case "testb":
					print("this is inside of inners  test2")
					print(" n now!")
					fallthru        

				case "testc":        
					print ("go reindeer")
					break

				case "testd":
					print ("testi  first nested  ol...")
					tahoe[0]="sublime" #puts victory into tahoe[0]
				default:
					print("out of inner  1")
					break
			endswitch
			####### line below end sw #################################
			print("out of inner s 1")
			fallthru


		case 'google', 'fishfood', 'probability':
			print ("successful test in test1")       
			print("tahoe[0]=",tahoe[0]) #result of  running
			#what output is there from?? use a list to capture it
			fallthru

		case "word":
			print ("this is back in main now !")
			fallthru        
			                            
		case "rudolph":       
			print ("go reindeer")
			print("=== this is 2nd ne

		case "test7":
			print ("gui design")
		###### nested inner 2 ##############
			switch(n) {# nested sw 2             
				case "testa":
					print("second did it work?")
					print("yes it's test == one")
					tahoe[0]="victory" #puts victory into tahoe[0]
					fallthru

				case "snowmanb":	
					print("this is witch test2")
					print (" cthon now!")
					fallthru        

				case "testc":       
					print ("go reindeer")
					break
			
				case "rabbitd":
					print ("te what do we have here ool...")
					tahoe[0]="mickey mouse" 
					print("tahoe[0]",tahoe[0])
					fallthru

				default2:
					print('None')
					break   
				
			endswitch  #this should be the bottom  insanely cool
			print("out of  2")
			break
		########################===================
		 
		 case "trouble":
			print("ufo report damning")
			print("coverup")
			break
		default:
			print("sorry no matches")
			break
			  
}
'''
endswitch(sw)
