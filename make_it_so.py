import site_b   #toying around with site_b and site_c
from site_b  import * 



#### this one below is good onemay 27th
# official_switch_case_silver
#from official_switch_case_silver  import *  




################################################
#      soon drum roll macros module 
#import blender_macros
#from blender_macros  import *  #may 25th, 2021 
########################################################


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
	

#print('drinkcoffee file being used here"')
#print("==================")

#this is  input variable exp for switch(exp)
#print("===== FIRST 1st switch =====")
#print("===== FIRST 1st switch =====")
#print("===== FIRST 1st switch =====")


#print("now to string switch see what happens")

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



print("-------------------")
print("== switch 1 ==")
print("-------------------")

#clever('PALOMAR')




#right now it NEEDS to take strings to digest and parse it"
#I need to add my new code for this to work properly"
##=====================
#show_input_switch_string()   #input so what the string right below here
#hide_generated_code()

print("--------")

swan =''' 
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
			print(" third sitting in car at starbucks testing this sucker")
			print("testing this on january 5th, 2022 at Starbucks")
			print("deer and quail about")
			print("oh my god this fucking worked a single switch victory!!")
			
			
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
#endswitch(swan)

#exit()
#if switch numbers to transfer > length of snowtime
#smartlistlocations[13, 9, 6, 6, 7, 13, 9, 6, 6, 7]
#smartlistlocations= [13, 9, 6, 6, 7, 13, 9, 6, 6, 7, 13, 9, 6, 6, 6, 7]




#trythis()
##===================================================================

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
#33289

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
#33289



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


#print("on to the next one==5 test now ======")

#import time
#start_time = time.time()


#print(" === 1st test === nested==")
print("=====now trying a NESTEd SWITCH attempt====")
num = 1   
main_control_sequencer(num,red_robin)#red_robin  #this will be the the modifed endswitch eventually 
print("==yanks==testing 2 now ")
print('=======after first pass===before second pass ===')


#show_it_to_me()  

print(" === 2nd test === nested==")
num = 7   
main_control_sequencer(num,red_robin2)#red_robin  #this will be the the modifed endswitch eventually 
#print("====after second pass== before 3rd pass=== ")
#show_it_to_me()

print(" === 3rd test === nested==")
#print("about to do second call of a second nested switch string")
#print("this is the third PASS doing regular red_robon second now")
num = 1   
main_control_sequencer(num,red_robin3)#red_robin  #this will be the the modifed endswitch eventually 
#print("=====after 3rd pass ======")
#show_it_to_me()
#print("go I want to fly like superman")
print("================number 4 test ======")


num = 1   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 

print("last one now the 5th test ====")
num = 1   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 

##============...............

#cloudy_day =

# 	switch(exp) {  
# 		case 1 thru 3:
# 			print("where\'s the dog house!")
# 			print('first prize')
# 			print('you block head Charlie Brown')
# 			fallthru
# 			
# 		case 4 to 7:
# 			print('kangaroo hop hop!')
# 			exp='more'
# 			switch(exp){   # === line 10 beginning of single nested switch ======      
# 				case 'blable':
# 					print("inside of the inner sw here")
# 					print("yep")
# 					fallthru
# 				case 'more':
# 					print("nice")
# 					break
# 				default:
# 					print("we are done here")
# 			endswitch #this is key here =============line 20 end of nested switch ====
# 			print('taught me how to write code')
# 			fallthru
# 			
# 		 
# 		case 8 to 10:
# 			print('mocha blast')
# 			print('== baskin robins ice cream on El Camino Real===')
# 			fallthru
# 		
# 		default:
# 			print('the end')
# }
	


#num = 1#1    
#main_control_sequencer(num,cloudy_day)
#red_robin  #this will be the the modifed endswitch eventually 

#print("after doing SECOND nested switch")



#print("result of the seconds it took to run is..")
#print("--- %s seconds ---" % (time.time() - start_time))


