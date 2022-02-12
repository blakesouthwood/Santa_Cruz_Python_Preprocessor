import trex  
from trex  import * 

import official_switch_case_silver
from official_switch_case_silver  import *  

##========================================
##  two_choices(mystring ##
####======== two_choices(mystring):============
def two_choices(mystring):
	print("==this is TWO_CHOICES testing this sucker===")
	nested =count_switches_in_inputstring(mystring)
	print("nested =",nested)
	if nested == True:
		smart_endswitch(mystring)  #nested switch
	else:
		cool_endswitch(mystring)   #single switch
	


print("I have tested these and they work inside of functions too")



nestedswitch('False')

clever('PALOMAR')

#show_input_switch_string()   #input so what the string right below here
#hide_generated_code()

print("----single switch 0----")

ducky =''' 
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
			print(" third  in backyard")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about")
			fallthru
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''
endswitch(ducky)


'''
print("-------------------")
print("=single = switch 1 ==")
print("-------------------")
'''
clever('PALOMAR')

#show_input_switch_string()   #input so what the string right below here
#hide_generated_code()

print("--------")

swan1 =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about fast cool humming birds blue jays")
			print("the quail go in single file across the lush green lawn!!")
			break
			
		case LAKE_TAHOE:
			print("now we are inside of Lake Tahoe good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''
endswitch(swan1)




'''
print("-------------------")
print("==single  switch 2 ==")
print("-------------------")
'''
clever('COYOTE')



print("--------")

swan2 =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			
			
		case PALOMAR:
			print("it actually works")
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about fast cool humming birds blue jays")
			print("the quail go in single file across the lush green lawn!!")
			
			
		case LAKE_TAHOE:
			print("now we are inside of Lake Tahoe good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''
endswitch(swan2)






red_robin ='''
	switch(exp){  
		case 1 thru 6: 
			print("green lantern green lantern green aliens!")
			print('this green green green . it actually works')
			print('how green green green, yes way ')
			
			
		case 7 to 10:
			print('green lantern green lantern green  between 7 and 10 !')
			
			#############
			exp ='blable'
			
			switch(exp)  
				case 'blable':
					print("we are blable here   inside of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice kayaking race")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#exp = 3
			print('this should write this line still within bounds of outer sw')
			switch(exp)
				case 'burger':
					print("do something")
					####################
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('taught me how to write code')
			fallthru
		case 11 to 15:
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	


red_robin2 ='''
	switch(exp){  
		case 1 thru 6: 
			print("====   red white blue    =====")
			print("====   white   =====")
			print("===    blue    ======")
			
			#it should stop here
		case 7 to 10:
			print("this is =======red white blue====== ")
			print('pass Dutch Flat, Cisco, and Kings Beach to NorthStar !')
			print(" this is 7 to 10 here we are")
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("morgan hill starbucks nesting works")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#exp = 3
			switch(exp)
				case 'burger':
					print("do something")
					####################
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('this should be the last line here for output')
			break #was f a l l t h r u
		case 11 to 15:
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	


red_robin3 ='''
	switch(exp){  
		case 1 thru 6: 
			print("====   purple    =====")
			print("====   purple   =====")
			print("===    poka dots    ======")
			print(" working on january 27th, 2022 8:56 am")
			print('== hamburger sounds good right about now')
			break
			#it should stop here
		case 7 to 10:
			print('pass drive in the snow to tahoe !')
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]=" did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do  of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("morgan hill starbucks nesting works")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#exp = 3
			switch(exp)
				case 'burger':
					print("do something")
					####################
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('this should be the last line here for output')
			break #was f a l l t h r u
		case 11 to 15:
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	



red_robin4 ='''
	switch(exp){  
		case 1 thru 6: 
			print("====zebra black and white =====")
			print("====   zebra   =====")
			print("===    tahoe summiting    ======")
			
			#it should stop here
		case 7 to 10:
			print("this is =====zebra black and white ====== ")
			print('pass Dutch Flat, Cisco, and Kings Beach to NorthStar !')
			print(" this is 7 to 10 here we are")
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("morgan hill starbucks nesting works")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#exp = 3
			switch(exp)
				case 'burger':
					print("do something")
					####################
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('this should be the last line here for output')
			break #was f a l l t h r u
		case 11 to 15:
			print("11 to 15 in ==zebra black and white==")
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			####################
			exp ='snow fire'
			switch(exp){   
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'snow fire':
					print("inside of snow fire from zeba black white")
					#############
					break
				default:
					print("we are done here")
			endswitch 
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	




red_robin5 ='''
	switch(exp){  
		case 1 thru 6: 
			print("grey aliens!")
			print('greys aliens')
			print('green aliens ')
			
			
		case 7 to 10:
			print('green lantern green lantern green  between 7 and 10 !')
			
			#############
			exp ='blable'
			
			switch(exp)  
				case 'blable':
					print("inside of an inner sw itch here we are blable here   inside of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice kayaking race")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#exp = 3
			print('this should write this line still within bounds of outer sw')
			switch(exp)
				case 'burger':
					print("do something")
					####################
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('taught me how to write code')
			fallthru
		case 11 to 15:
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	


print("-------------------")
print("==single  switch 3 ==")
print("-------------------")

clever('CASPER')



print("--------")

swan2 =''' 
	switch(exp) {
		case CASPER:  
			print(\"how to make money in one easy lesson!\")
			print("write code nobody else on earth can")
			
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about fast cool humming birds blue jays")
			print("the quail go in single file across the lush green lawn!!")
			break
			
		case LAKE_TAHOE:
			print("now we are inside of Lake Tahoe good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''

    
endswitch(swan2)

print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("===TEST TEST====TEST TEST====TEST TEST====TEST TEST====TEST TEST==")
print("-------------------")
print("==single  switch 4 ==")
print("-------------------")

clever2('PALOMAR') #so it calls clever in silver module
#need to share clever perhaps different name ah yes
#show_input_switch_string()   #input so what the string right below here
#hide_generated_code()

print("--------")

duck =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about fast cool humming birds blue jays")
			print("the quail go in single file across the lush green lawn!!")
			break
			
		case LAKE_TAHOE:
			print("now we are inside of Lake Tahoe good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory 
}
'''
print("=== duck changes =====testing if duck is single switch or multiswitch")
#count_switches_in_inputstring(duck) #testing on feb 12th 
#cool_endswitch(duck)  #inside of silver
two_choices(duck)

#=== feb 12th 2022 testing ==========================
#what if I call smart_endswitch
#and if it's a single switch which I check for
#call cool_endswitch(stringname)
##==============================

#dual_modes(duck)
#smart_endswitch(duck) #single string test 
#main_control_sequencer(num,red_robin)


####### FEBRUARY 12TH GOODNESS ##########################
#idea. I will put count_switches_in_inputstring(string)
#inside of endswitch(string)
#count_switches_in_inputstring(duck) 
#if nested == True
#    nestedswitch('True')
#    main_control_sequencer(num,red_robin)#
#else:
# regular endswitch code




#print("on to the next one==5 test now ======")

#import time
#start_time = time.time()

nestedswitch('True') #means True for nested



#exit()

#print(" === 1st test === nested==")
print("")
print("")
print("=====now trying a NESTEd SWITCH attempt===you cna do it =")
print("")
print("input 1")
print("")
print("=== beginning of test to make it to Tahoe looks like it will be C#====")
  
num = 1
feedinput(num) #puts num into dino[0] for testing purposes only

print("===///===testing if multi switch here===///=====")
#count_switches_in_inputstring(red_robin) #tested successfully 

#this will just take in as input the string now not num,red_robin
#main_control_sequencer(red_robin)#red_robin  #this will be the the modifed endswitch eventually 


#smart_endswitch(red_robin)  #NESTEd in TREX
two_choices(red_robin)

#dual_modes(red_robin)
#this calls TREX module for the nested switch 

#the idea is that it tests if nested switch
#and if so calls main_control_sequencer
# and if NOT nestd then calls regular endswitch

#######===================

clever2('LAKE_TAHOE') #this existgs only in the silver module 



print("--------")

swan2 =''' 
	switch(exp) {
		case CASPER:  
			print(\"how to make money in one easy lesson!\")
			print("write code nobody else on earth can")
			
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about fast cool humming birds blue jays")
			print("the quail go in single file across the lush green lawn!!")
			break
			
		case LAKE_TAHOE:
			print("now we are inside of Lake Tahoe good skiing")
			print(" alpine meadows")
			print("all of the stars and the milky way galaxy crisp air")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''

#dual_modes(swan2)    
#===========================
#cool_endswitch(swan2) #this exists only in teh silver module 
two_choices(swan2)

#this calls teh silver module for single switch 


	    
###=======================================
#this will only take in one input now print("==yanks==testing 2 now ")
print("prematurly quitting to see if it worked or not")
print("===END TEST=====")



	
exit()  #just to see where we stand at this point
#print('=======after first pass===before second pass ===')














elcapitan='''
	switch(exp){   
		case 1 thru 6: 
			print("mocha morning!")
			print('a walk in the park')
			print('listening to neo music ')
			break

		case 7 thru 10: 
			print("two !")
			print('cold tennis')
			print('who will win? ')
			fallthru
			
			exp ='red'
			switch(exp)   
				case 'red':
					print("we are red blood cells ")
					print("3 billionof them ...")
					break
				case 'blue':
					print("we are red blood cells ")
					print("3 billionof them ...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that chap')
			print(' ')
			
}
'''	

#nestedswitch('True') #means True for nested
print("==== testing elcapitan new switch string all kinds of probs why==")

num = 1   
main_control_sequencer(num,elcapitan)#

print("second attempt go high")
num = 7   
main_control_sequencer(num,elcapitan)#

# I was missing a : after a case and missing default: at bottom
#exit()


#show_it_to_me()  
print("")

print("input 7")
print("")
num = 7   
main_control_sequencer(num,red_robin2)#red_robin  #this will be the the modifed endswitch eventually 
#print("====after second pass== before 3rd pass=== ")
#show_it_to_me()
print("")
print("input 1")
print("")
print(" === 3rd test === nested==")
#print("about to do second call of a second nested switch string")
#print("this is the third PASS doing regular red_robon second now")

num = 1   
main_control_sequencer(num,red_robin3)#red_robin  #this will be the the modifed endswitch eventually 
#print("=====after 3rd pass ======")
#show_it_to_me()
#print("go I want to fly like superman")
print("")
print("input 1")
print("")
print("================number 4 test ======")

num = 1   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("input 1")
print("")
print("last one now the 5th test ====")

num = 1   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("input 7")
print("")
print("last one now the 6th test ====")

num = 7   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 7")
print("")
print("")
print("last one now the 7th test ====")

num = 7   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 7")
print("")
print("")
print("last one now the 8th test ====")

num = 7   
main_control_sequencer(num,red_robin3)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 7")
print("")
print("")
print("last one now the 9th test ====")

num = 7   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 

print("")
print("input 7")
print("")
print("last one now the 10th test ====")

num = 7   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 3")
print("")
print("")
print("last one now the 11th test ====")

num = 3   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 

print("===end of testing demonstration==")
print("rising torrain at 12 miles ...")
##=======================
print("what are the values of the lists that are clearly")
print("messing up the inputs for the single switch probably won't work again")

#was imported here initially and worked
print("trying something totally differentnow a different module attempt")
#import official_switch_case_silver
#from official_switch_case_silver  import *  


print("-------------------")
print("== switch 1 ==")
print("-------------------")
clever('PALOMAR')
#right now it NEEDS to take strings to digest and parse it"
#I need to add my new code for this to work properly"
##=====================
show_input_switch_string()   #input so what the string right below here
hide_generated_code()

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
			print(" third  in backyard")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about go blue origine")
			break
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''
endswitch(sw)

print("===now testing a nested switch again===")
num = 3   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 3")
print("")

print("now testing another single switch at bottom of tar pit")

print("-------------------")
print("=bottom = single switch 2 ==")
print("-------------------")
clever('LAKE_TAHOE')
#right now it NEEDS to take strings to digest and parse it"
#I need to add my new code for this to work properly"
##=====================
show_input_switch_string()   #input so what the string right below here
hide_generated_code()

print("--------")

swy =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			break
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("I SERIOUSLY DOUBT THIS WILL WORK EVEN")
			
			
		case PALOMAR:
			print("it actually works")
			print(" third  in backyard")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about go blue origine")
			break
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			print("==========")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			print("=========")
			
		case AMERICA:
			print('manure')
			print("no more horses")
			print("==========")
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break #mandatory break
}
'''
endswitch(swy)

####=== show me the money =========
##==========================

print("-------------------")
print("=bottom = switch 3 ==")
print("-------------------")
clever('rasberries and cream') #this would change varholder[0] 
show_input_switch_string()   #input so what the string right below here
hide_generated_code()

swi ='''
	switch(exp) {
		case 'rasberries and cream':  
			print("wheres the cream house only this first one works")
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
endswitch(swi)







#clever('3') #this would change varholder[0] 








##=========================
show_input_switch_string()   #input so what the string right below here
hide_generated_code()
print("-------------------")
print("=bottom = switch 4 ==")
print("-------------------")
clever('gone fishing') #this would change varholder[0] 

swu = '''
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
endswitch(swu)






##============================

print("-------------------")
print("== bottom switch 5 ==")
print("-------------------")
clever('star wars') #this would change varholder[0] 
show_input_switch_string()   #input so what the string right below here
hide_generated_code()
#hide_generated_code() #from this point forward


swt ='''
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
endswitch(swt)

print("=====================")
print('now doing more nested switches ')
num = 7   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 

print("")
print("input 7")
print("")
print("last one now the 10th test ====")

num = 7   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 
print("")
print("")
print("input 3")
print("")
print("")
print("last one now the 11th test ====")


#num = 1#1    
#main_control_sequencer(num,cloudy_day)
#red_robin  #this will be the the modifed endswitch eventually 

#print("after doing SECOND nested switch")
#print("trying a single switch here at teh bottom which will crash")
### this is crashign at the bottom 


#print("result of the seconds it took to run is..")
#print("--- %s seconds ---" % (time.time() - start_time))
clever('ufos') #this would change varholder[0] 
show_input_switch_string()   #input so what the string right below here
hide_generated_code()
#hide_generated_code() #from this point forward


swt ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\")
			print('nimitz')
			print("==area 51==")
			
	
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			
		
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
endswitch(swt) 

