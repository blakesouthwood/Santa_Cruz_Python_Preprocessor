from woodstock import gold_list


#Santa_Cruz_Python_Preprocessor/fourth_of_july2good.py /

def message_from_linus():
    print('hello from Linus file')
 
#message_from_linus()   
#import official_switch_case_silver
#from official_switch_case_silver  import *  
endswitch_location=[]
switch_location=[]
zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'
cat_scales=[]
cat_scales.append(0)
#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 
#make sure no space and it's switch(exp){
#first red robin here testing 
red_robin ='''
	switch(exp){  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp)  
				case 'blable':
					print("do something")
					####################
					switch(exp){ 
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			exp = 3
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
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	

autumnleaf='''
	switch(exp){  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  
				case 'blable':
					print("do something")
					####################
					switch(exp){       
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){      
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){    
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
										####################
											switch(exp){    
												case 'fishy':
													print("do something")
													print("yep")
													fallthru
												case 'where now':
													print("nice")
													break
												default:
													print("we very done")
											endswitch 
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   4..........endwitch 4  line 60 3 tabs 
			exp = 3
			switch(exp){   
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
					endswitch #77 5 .....
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86   
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
} endswitch #100  7 ........
'''




# output is to inputstring[0]

passinputstring=[]
smart_switch_numbers=[]
loopstring=[]
loopstring.append(0)
#twinlist=[]
passinputstring.append(0)  #get line number of switch and add number with comment to after all switches
snowman=[]
snowman.append(0)
##===================================================
##  add comment and lin number to all switches ()   ## put switch line number in
##===================================================
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	awesome='';counter =0;newstring='';
	print(inputstring)
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			# NEED TO HANDLE BOTH SCENARIOS switch with brace and switch without a brace 
			#############################################
			#switch is in this line definitely
			if "{" in line and "switch" in line and "end" not in line:
				newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
			#end if
			#this is necessary since the replace is quite specific and so no brace here
			# NOTE: I am adding gthe brace if it's missing to switch 
			if "{" not in line and "switch" in line and "end" not in line:
				newstring += line.replace("switch(exp)","switch(exp){ #" + str(counter) + "\n")  
			#end if  
			smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		    ####################################################
		elif "endswitch" in line: #just added comment number after endswitch 
			newstring += line.replace("endswitch","endswitch #" + str(counter) + "\n")
			counter += 1
		###################
		else:
			newstring += line + "\n"
			counter += 1
	awesome = newstring #it was concatted to newstring
	for line in newstring.splitlines(): #was redrobin.splitlines()
		print(line)
	print("AFTER ADDING the line number as comments to the switches in red robin baby ")	
	print(newstring)   #it prints red_robin switch combo string with the line numbers added in comments
	print("smart_switch_numbers=",smart_switch_numbers)  #this is new here too 
	return newstring #this way I can capture the changed string





def too_swift():
    print("==========too_swift() called=======")
    print("dirt stimple test showing lines with switch, end switch and }")
    for line in red_robin.splitlines():
        if "switch"in line:
            print(line)
        if "}" in line:
            print(line)
too_swift()

print('done for the exit sign')        


print("from the web trying this out")

quail=[]
# I am adding the quail list to practice filling it

print("testing add comment and line number after all switches")
add_comment_and_line_number_to_all_switches(red_robin)
print("REd ALERT critical test first method  test first method ...")
#exit()


def empty_switch_and_endswitch_list_locations():
    print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations 
##########################################
switch_location=[]
endswitch_location=[]
together_pair=[]
def get_switch_and_endswitch_locations(z): #from string z input parameter
	return
	#return we START BUILDING
	print("thbis is what I am testing now now now")
	print("  get switch and endswitch locations###  called line 322 #####")
	print("######get switch and endswitch locations########")
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	#print("=====get_switch_and_endswitch_locations(z) called ....")
	#print("====== THIS IS THE ONE THAT I NEED ======")	#this catalogues the switch and endswitch locations for an entire input string
	#print(" GET SWITCH AND ENDSWITCH LOCATIONS ADDED TO LIST")
	#print(" ========  MICKEY MOUSE HOUSE  =========")
	counter=0 #it was 0 starting counting from 1
	for line in z.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		#print(line) #this should be revealing
		#if line.isspace():
		#wrong='''	
		#rechecking to see if this works 
		if "switch" in line and "end" not in line:
			print("switch found",counter)
			switch_location.append(counter)
			counter += 1			
		#if "endswitch" in line:
		#	print("look right here endswitch found",counter)
		#	endswitch_location.append(counter)
		#	counter += 1
		else:
			counter += 1 
	
	counter=0
	for line in z.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line:
			print(line)
			print("look right here endswitch found",counter)
			endswitch_location.append(counter)
			counter += 1
		else:
			counter += 1 
		#'''
	print("at this point this is what we have...after testing BIG YELLOW BIRD go bird")
	del switch_location[0] #takes out first number not needed
	print("switch_location=",switch_location)
	print("endswitch_location=",endswitch_location)
	#test_string1exit()
	print("this over writes the contents of these two lists ")		
	#hard coding it in here why 
	#switch_location    =[1,11,15,23,31,62,66]
	#endswitch_location =[100,60,51,46,41,86,77]	#might hav eto resverse these 	
	
			#THIS DELETES THE FIRST SWITCH WHICH WE DON'T USE
	#del switch_location[0]	#empties it what am I doing here??? july 7th deleting first switch
	print(z)                #now I remember that is the first switch which doesn't matter
	print("I deleted the first switch since I'm not bothering with it")
	print("switchlocations=",switch_location)
	print("on line 180 endswitchlocation=",endswitch_location)
	
	print("the length of switch list =",len(switch_location))
	answer = len(switch_location)
	answer = answer -1
	print("this is how many nested switches are here")
	print("now we should have this many nested switches to contend with",answer)
	print("and the answer is above this line .....")
	#this prevents a bug if I don't have endswitch in the string
	#if len(endswitch_location) > 0: #this only proceeds if there is at least one endswitch
	#	print("endswitch locations =",endswitch_location)
	#	print("out of curiosity print the number of endswitches", len(endswitch_location))
	#else:
	#	pass
	print("I need to test that this part still works here in fourth of july 2 .py")	
	print("this might be simpler to test and use actually======/////???????//////===")
	print("======================================")
	print(" ===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === ")
	print("I need to delete teh first swithc location")
	
	#working on this on Saturday, October23, 2021 to get this stage done 
	#del switch_location[0] #ALREADY DELETING FIRST SWITCH ABOVE BECAUSE IT'S NOT NEEDED NOT NESTED
	print("does this look right testing on Sunday gloomy rainy day")
	print('switch_location=',switch_location)
	print('endswitch_location=',endswitch_location)
	#the input is above
	
	
	print("....")
	print("the input for filling the blueberries dictionary are the lists switch_location and endswitch_location")
	print("==================")
	print("the enchanting world of making blueberry pie")
	
	
	
	
	##################################################################################
	############## working on this on saturday, october 23rd, 2021 ###################
	##################################################################################
	print(" rain fall status ")
	counter=0
	#working on creating input list for blueberries dictionary: can't believe I didnt do this yet
	print("what the hell is going on here")
	#print("switch_location=",switch_location)
	#for item in switch_location:
	#	print(item)
	#print("so how did that go...")
	
	print("endswitch_location=",endswitch_location)
	#for item in endswitch_location:
	#	print(item)
	print("so how did that go...")
	
	
	counter=0
	print("starting at counter =0")
	
	print("=============== starbucks morgan hill =====")
	print(switch_location)
	print(endswitch_location)
	print("emptying together pair here")
	del together_pair[:] #delete it just in case to start with clear chalkboard
	print("=======") #THIS FILLS THE TOGETHER_PAIR LIST OF SWITCH,ENDSWITCH 
	print("this loop fills the together_pair list of switch,endswitch numbers")
	print("this is so much dam fun oh yeah")
	total1 = len(switch_location)
	total2 = len(endswitch_location)
	print("total1 =",total1)
	print("todal2=",total2)
	print("this is where we START BUILDING the ===TOGETHER PAIR =====")
	for item in switch_location:
		solution = "[" + str(switch_location[counter]) + "," + str(endswitch_location[counter]) + "]" 
		print("solution=",solution) #to see what it looks like 
		together_pair.append(solution)
		print("counter=",counter)
		counter += 1
		
		#this should prevent stack overflow of the list range added november 9th 
		if counter >= len(switch_location):
			print("stack overflow called since counter > = len(switch_location)")
			break
		else:
			continue
			
	print("now we will loop thru the together_pair to see that the pairs are in there")
	del endswitch_location[-1] #should delete 100
	print("this is what is in TOGETHER_PAIR at line 254")
	for item in together_pair:
		print(item)
		apple = item.split(",")
		print("======")
		print(apple[0])
		sweet1 = apple[0].replace("[",'')
		#print(sweet1)
		print(apple[1])
		sweet2 = apple[1].replace("]",'')
		print(sweet1,sweet2)
		print("where's the party")
	# I need to feed these into the pear dictionary now down below
	#I will feed the pears list with a loop thru the switch_location list
	########## WORKING ON THIS TODAY MONDAY TO MAKE SOME SERIOUS PROGRESS 
	##########  MONDAY JULY 19TH APPROACHING 12 NOON 
	
	#make pairs here
	#might have to delete teh first switch which throws everything off
	##################### end of method #################################3
#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]  	
	
	

print("what are they actually")
print("starbucks coding NEXT TO RED ROBIN===== big storm coming...")
#Sget_switch_and_endswitch_locations(red_robin) #yeah it's calling red robin!!!
print("result of switch and endswitch locations in red robin")
print("examine the contents of the lists switch_location and endswitch_location")
print('switch_location=',switch_location)
print('endswitch_location=',endswitch_location)




string = """
line1
line2
line3
line4
line5"""
str_list = string.split('\n')
print('changing line 3')
str_list[3] = "my new line value"
string = "\n".join(str_list)
print(string)

print("end of test from the web")
print("=========")
#this simulates after cutting out the inner switches but leaves the first line
#which is used for replacement of the nested method()
############################################################
########## august 5th testing what to use now #################=========$$$$$$$$$$$
############################################################
# this represents and input string with inner switches cut out
#what remains is just the switch word which will be replaced
old_coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here        representings stripped out inner nest
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){     #here    # represents already stripped out inner nest 
			fallthru
		default:
			print('the end')
}
'''
coffee_now='''
	switch(exp){ #1      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 
		default:
			print("we are done here")
	endswitch #this is key here 
'''
	
#this is coolstring with the nested switches already taken out for all levels+
coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			switch(exp){
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){   #here        representings stripped out inner nest
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			switch(exp){     #heret 
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){
			fallthru
			
		case 16 to 20:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){ 
			fallthru
			
		case 16 to 20:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){ 
			switch(exp){
			switch(exp){
			fallthru
		default:
			print('the end')
}
'''

#working on this July 15th, 2021 10:16am Starbucks
#get_switch_and_endswitch_locations(coolstring)
#output to these lists
#switch_location #skips the first main switch not included
#endswitch_location (if any)
#get_switch_and_endswitch_locations(coolstring)
print("done with test to get the nested switch locations within the big switch")

### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
switch_list=[]

#this accesses coolstring august 5th, 2021
#this is to set the inner switch positions in the main switch input strings
#after the bodies of the nested switches have been stripped out

##########################################
##  put_switch_locations_into_switch_list()  #this is making the nested_switch_ number  
##########################################
def put_switch_locations_into_switch_list(inputstring): #just added param
    print("##2### put_switch_locations_into_switch_list ###")
    print("##2## put switch locations into switch list ###")
    print("put switch locations into switch list")
    #### get swith and endswitch locations called here 
    get_switch_and_endswitch_locations(inputstring) #it's right here 
    for item in switch_location: #this is only going thru switch_location
        switch_list.append(int(item))  #was -1 on here #off by one in the string for some reason
    # print(" ");print("switch_list=")
    #print(switch_list)

#######################################
##  swap_switch_to_nested_method()  #this is making the nested_switch_ number  
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	print("============== swap_switch_to_nested_method() ==========")
	#print("input: linenumber", linenumber)
	#print("input: series_num", series_num)
	
	#print("##4## swap switch to nested method - numbered ###")
	#print("##4## swap switch to nested method - numbered ###")
	#print(" THIS IS BEING CALLED TO DO THE MAGICswap switch to nested method called....")
	str_list = stringname.split('\n')
	#print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)

######################################	

#this is the control center main that runs this operation
#this numbers the nested switch methods top down
#genius[0]=coolstring  #assignment here <<<==================


#######################################
##  loop_thru_switch_locations():
#######################################
def loop_thru_switch_locations(regularstring):  #looping thru  switch_list[10,18]
    print("##1##loop thru switch locations ## line number 276 ####")
    print("##1##loop thru switch locations ######")
    #trick put_switch_locations_into_switch_list
    #method called
    put_switch_locations_into_switch_list(regularstring) #method
    print('this filles switch_list of switch line numbers')
    #print(genius[0])
    print("what is the order of the switch_list I think it's reversed to do bottom up")
    print(switch_list)
    print("------------")
    print("switch_list=",switch_list)
    le_number=1 #default numbering nested string 
    for item in switch_list: #loops thru switch_list WITH SWITCH LOCATIONS (LINE NUMBERS)
        print("item in switch_list",item)
        #string,switch,line number
        # swap_switch_to_nested_method here 
        #method this one is the holy grail that actually works
        ###############################
        swap_switch_to_nested_method(genius[0],item,le_number) 
        coolstring =genius[0]
        le_number += 1  #adding to the nested number here
    print("#### end of loop thru switch locations() ####")
    print('the EXIT sign is green')
#######################################



print("STAR TREK TEST FULL PHOTON LASERS add numberednested method McCoy looks good now beam me up ")
print("starting with this input main string with nested switch bodies cut out")
print("tahoe dream")
##==========================================================|
## swap_nested_switches_with_methods_in_main_switch_string
##==========================================================|
def swap_nested_switches_with_methods_in_main_switch_string(inputstring):
    print("===swap_nested_switches_with_methods_in_main_switch_string()== line number 309=") 
    loop_thru_switch_locations(inputstring) 
    print("this is the output string of the transformation from input string")
    ## this is after loop thruw switch locations method is completed
    print("this is the main input switch string after adding nested methods")
    print("the output of this transformation of swapping switch for nested_method")
    #this is the input string transformed 

#this calls it
genius[0]=coffee_now  #assignment here <<<==================
print("about to call swap_nested_switches_with_methods_in_main_switch_string(coolstring)")
swap_nested_switches_with_methods_in_main_switch_string(coffee_now)
print("fter testing tron getting closer=== 1 ...2.....3  out the EXIT")
print(genius[0])

#this calls above
print("=== begin tron test ==line 323 =TESTING september 1st here we go=-=== to see if this sucker works === august 27th ==== please work ==")
print("this is testing the main switch string module changing nested switches")
print("that already had their bodies cut out and swaping in a nested method")
genius[0]=coolstring  #assignment here <<<==================
print("about to call swap_nested_switches_with_methods_in_main_switch_string(coolstring)")
swap_nested_switches_with_methods_in_main_switch_string(coolstring)
print("fter testing tron getting closer=== 1 ...2.....3  out the EXIT")
print(genius[0])
print('end of test of swap nesetd switches with methods in main switch string ')
print(" oh that's what this does...da ")
print("====line 332 ==end of this tron test september 1st=====")
print("======end of this tron test september 1st=====")
#exit()  #stop it here
	#string_change =coolstring
#stringname=coolstring
print("now change the inner switches to the nested method numbered")
#swap_switch_to_nested_method(coolstring,10,1)	  #####======

print("after first change ====>>>>>>>")
#coolstring =genius[0]                            #########==========

#series_num = number_series[0] 
#swap_switch_to_nested_method(coolstring,18,2)	  ########=========
print("after the 2nd change ...")
#coolstring =genius[0]
##print(genius[0])                                ################============
print("done with this test of the new method")
  #building the method to make this magic happen automatically


#-------------------  july 10th, 2021   11:03 pm  -------starbucks coding-------
#I am hard coding the location of the switch words. I need to have it search on it's own
# but I recall I have code that does that elsewhere
#now I need to find the code that makes the correct nested switch list locations

#they are being harded coded in here I should be getting them from above

#switch_list.append(11) #was 10,18,31
#switch_list.append(19)
#switch_list.append(32)## added a third switch to test it more thoroughly 

##============================================================================
print("here put switch_locations into switch_list")
## this is new added Thursday july 15th 2021 prevents off by one error
## it takes input of nested switch line number locations from switch_location
## and puts them into switch_list (but again not the first main switch)   

#this one just commented out
#put_switch_locations_into_switch_list()
print("about to test it with the loop thru switch method ====")
print("today is july 22nd, 2021 thursday refining the algorithms and methods")
## calling LOOP THRU SWITCH LOCATIONS (INNER)

######======================
#loop_thru_switch_locations() #where to find the inner switches to replace with a nest method
######======================


print("did it work=============MMMMMMMMMM----======MMMMMMMMM==========")
print("we called loop_thru_switch_locations() which calls swap_switch_to_nested_method()")
print("we should have successfully swapped out the inner switches with nested_method numbered")
print("today is july 15th, 2021 at Starbucks connecting the functions")
print(genius[0])    	
print("olympic gold medal to make it this far.")
print("==IT SHOULD BE ABOVE THIS LINE WITH THE NESTED NUMBERS METHODS INNER SWITCHES==")
print("now I need to work on copying the nested strings to a list")
print("and then taking out the nested strings from the main switch string except for switch")
    
#this one works just need to test it as a method above 
#str_list = coolstring.split('\n')
#print('changing line 11')
#str_list[10] = "\t\t\tnested_switch_1(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)

#print(string_change)
#stringname = string_change
#############
#str_list = coolstring.split('\n')
#str_list[18] = "\t\t\tnested_switch_2(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)


#what if I go thru a list to make teh changes
#=====================================================
#z = 'test4'

#choose to 'Update Now'
# when the newest MacOS Mojave 10.14. 6 Supplemental Update

#say we add it to first case 2nd line after case just bump down whatever
#is on that line. copy that line just for saftey and add it to the tail
#with \n at beginning and end of that line


### look for nested switch called    switch_nest()  
# get case number which case is it, first, second, third for this test
#then get line number of case section determine what line it's on.
#(the nested switch method)

output_string_test='''
 switch(x) #main switch    #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("this is the first case in the main switch")
            #switch_nest() #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')   
                     
        if case == "two":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word') 
            
        if case == "three":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
           
            
'''

######## testing 2nd and 3d level deep nested switch cases july 29th, 2021


# will mess around with this later. 

triple_nested_switchtest ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
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



cicelyalaska ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'music':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'coolish':
									print("do something")
									print("yep")
									fallthru
								case 'auburn':
									print("nice")
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
			fallthru
		
		default:
			print('the end')
}
'''	



snowman='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									#################### this one is new 
									switch(exp){  #fourth level deep   Level 4    
										case 'obama':
											print("do something")
											print("good")
											fallthru
										case 'ufos are real':
											print("better")
											break
										default:
											print("nice job")
									endswitch 
							#############
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== interesting test here for just 3 here ==')
			switch(exp){  #second level deep          Level 2    
				case 'sierra':
					print("do something")
					print("yep")
					fallthru
				case 'snow lake':
					print("nice")
				default:
					print("welcome to the party") 
			endswitch
		case 1 thru 3:
			print("where\'s this will be one match for 3, 5!")
			print('first prize')
			switch(exp){  #second level deep          Level 2    
				case 'sierra':
					print("do something")
					print("yep")
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
						default:
							print("welcome to the party") 
						endswitch
					fallthru
				case 'snow lake':
					print("nice")
				default:
					print("welcome to the party") 
			endswitch
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'music':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'coolish':
									print("do something")
									print("yep")
									fallthru
								case 'auburn':
									print("nice")
									####################
									switch(exp){  #fourth level deep   Level 4    
										case 'coolish':
											print("do something")
											print("yep")
											fallthru
										case 'auburn':
											print("nice")
											#######################
											switch(exp){  #fifth level deep   Level 5    
												case 'coolish':
													print("do something")
													print("yep")
													fallthru
												case 'auburn':
													print("nice")
													break
												default:
													print("we are done here")
											endswitch 
											break
										default:
											print("we are done here")
									endswitch 
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
			fallthru
		
		default:
			print('the end')
}
'''	

'''
loop thru string
get switch locations and tabs coount
then make list of numbers of switches inside tab 3 switch
only thing that I cna think of.
make list with sublists
'''

answer=triple_nested_switchtest.count("endswitch")
print('counting the nested switches to see how it goes ====Boo ')
print("the number of nested switches based on endswitch=",answer)
for line in triple_nested_switchtest.splitlines():
    print(line)
print("=== the end ====")
print("================")

#answer we seek is case section 2, line 2
################===============================
#33 june 28th, 2021 9:26 pm now 

#where I detect the nested switch  location and starting and ending point
# I copy the nested switch and delete it from the main switch
# I add a method where thes switch word is.
# My compromises to get it working faster are the nested switch
# must end with endswitch  and not a curly brace
# this makes it easier to get working and aids readability

#the switch main switch is chopped off at the begining of the inner switch
#the bottom after the nested switch ends with endswitch is copied
#to the top half but only after the nested method is added to th eline
#where the nested switch was 



# when code is running there is nothing to see.
# If we have moving behavior (which is invisible)
# that is what matters -but like what Fred Brooks says
# software is invisible. So I need to make it tangible and visable.

#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========



# starting testing here to see if I can reduce the code to make sense

 ####### august 10th 2021 testing commences.
 
find_nested_switch_game ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
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

gameday ='''
			switch(exp){   #1 === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					switch() #7
						case 'funny':
							print('fun')
						case "da":
							print('yeah')
						default:
							print('bye')
					endswitch #14
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
'''	

print("what we are starting with the switch with a nested switch")
print(find_nested_switch_game)
print("=====================")
#oh wait this needs to be the input C style switch that I search in
#maybe I need to go through the case list palmtrees
# so get line number of switches
#get linenumber of each case to determine which case section the inner switch is in
pacman=[]
pacman.append(0)


coollist=[]
print("this gets the line number of the line that the case starts")
print("that has the nested switch inside THIS Case")

endnestedswitchline=[]
endnestedswitchline.append(0)
#########################################
##  get_case_line_numbers(string_name):
#########################################
def get_case_line_numbers(string_name):
    linecounter =0
    casecounter = 0
    print('get line number of each case section')
    #just get first case line numbers print it
    for line in find_nested_switch_game.splitlines(): #be sure to put stringname.splitliens()
        #this looks for cases
        if "case" in line:  #grabs first line
            print(line)
            pacman.append(linecounter)
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
        #if "switch" in line:
    print("case line numbers",pacman)    
    #print(pacman[2])  
    print("number less than 10 that ")
    #I reverse the list order to find the first case less than 10 the line with switch in it
    pacman.reverse()

#calls method above
#####==========
#get_case_line_numbers(find_nested_switch_game)
#####========


#####################################
## get_larger_number_less_than_case()
#####################################
def get_larger_number_less_than_case():
    #this gets teh larger number less tahn the case
    for item in pacman:
        if item < 10: #I will need to put  (this cuts the possibilities to those less than 10)
            coollist.append(item)
            print(item)
            print("this must be the answer of the case that is on line 8")
            break #so after just the first one
    #get largest number in list
    print("this is new trying to get largest number only from list")
    superman = max(coollist) #worked June 28th MOnday 2021
    print("largest number =",superman)

#calls method above
#######========
#get_larger_number_less_than_case()
#######========




###$############===================-----0-0--=-=-=-=-=-=0-0-0-9=0--
### GET END OF SWITCH LINE  number
#######################################
## now looking for end of nested switch case
#june 28th, 2021
#####################################
## get_end_of_switch_line_number():  #  this gets endswitch line number
#####################################
def get_end_of_switch_line_number():
    linecounter=0 #this looks for the line number of endswitch for the nested switch
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "endswitch" in line:  #grabs first line
            print("we have a match")
            print(line)
            #linecounter += 1 if it's endswitch don't add one
            print(linecounter)
            endnestedswitchline[0]=str(linecounter)
            break
        else: #this looks for the  switch word
            linecounter += 1   
            continue
    print("the end of this nested switchis",endnestedswitchline[0])
    print("====should be 18 ====")

#calling method above this 
#####=========
#get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
#####=========

#and we know that the case number is 8
#and we know that the nested switch starts on line 10
#therefore we subtract 10-8 = 2
#so within the case the nestedswitchmethod will be on line 10 or the 2nd line within the case
###############=======================########################
print("copy inner switch")
#first trying to copy the inner switch and put it into a list

linecounter=0 #this looks for the line number of endswitch for the nested switch
print("testing getting a copy of nested switch")
### what I need to do is grab the numbers that I generated that I am using below
### I determine the line number that the first and only nested switch is on
### I then look for the first "endswitch" after the nested switch starts
### and it must be within the bounds of the case that it is residing within.
#here I am feeding it but I need to make it a method
#x = 11;
#y = 60;
#start  = 11  #hard coded beginning of nested switch
#finish = 60 
start_and_finish=[]


##============================================
##  inputs_pair_to_copy_a_string()
##============================================
def inputs_pair_to_copy_a_string(start,finish):
    print("inputs pair to copy a string")
    del start_and_finish[:] #this clears it out initializing it
    start_and_finish.append(0) 
    start_and_finish.append(start) #position [1]
    start_and_finish.append(finish) #position [2]
    #start_and_finish[1] = x
    #start_and_finish[2] = y
    print("x=",start_and_finish[1])
    print("y=",start_and_finish[2])
    
########################################################################
 #hard coded end of single nested switch 
## COPY A NESTED SWITCH
############################

#so we have

#############################
r=find_nested_switch_game #thats the name of a string fin_nested_switch_came
#linecounter=0
makeitwork=[]
makeitwork.append(0)
## function copy a nested switch()   ==== I just put this into a function

print("will do red robin string with the sets of pairs individually to verify it's right")
print("testing Sunday, NOvember 7th, just got 3rd booster shot ----")
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
################################################################################
################################################################################
################################################################################
################################################################################
columbia_river=[]
#gold_list=[]
################################################################################
################################################################################
################################################################################
################################################################################
###############################
## copy_a_nested_switch(r):   # what this does is copy one nested switch 
###############################
def copy_a_nested_switch(r):  #copy just one nested string 
    print("= copy_a_nested_switch() called== just now 10;43 am ====")
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
    for line in r.splitlines(): #if linecounter is between start and finish
    #this should copy a full (every line) of a nested switch from switch to and including endswitch
        # if lincounter >= 10 and linecounter <= 20; #this is what it means
        if linecounter >= int(start_and_finish[1]) and linecounter <= int(start_and_finish[2]):
            innerswitch += line + "\n"  #it's concatted to innerswitch string right here
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result COPY OF NESTED SWITCH  ")        
    #print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner #result of copied string goes in makeitwork[0]

################################################################################

#I need to fill this list (populate it from get switch engineswitch pairs
print("testing looping thru gold_list")
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]
print("=======begin Sunday Morning Brew Testing=======")

# uses methods:
# add_comment_and_line_number_to_all_switches
# inputs_pair_to_copy_a_string(num1,num2) #get input string from goldlist
# copy_a_nested_switch(water)
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]] 

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

print("testing looping thru gold_list which I imported at top of Linus from woodstock")
#from woodstock import gold_list
#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]0
print("did this get filled up or not gold_list=",gold_list)
for item in gold_list:
    print(item)
print("======")
#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]  
################################################################################
################################################################################
################################################################################
###3==============================
#it uses the gold_list to copy the nested strings      
##=============================================================
##  split_up_big_string_into_nested_switches(myinputstring)
##=============================================================
def split_up_big_string_into_nested_switches(myinputstring):#this would only be called once
    print("===split up big string into nested switches()===")
    water =add_comment_and_line_number_to_all_switches(myinputstring) #stringname goes here
    for line in water.splitlines():
        print(line)
    del columbia_river[:]  
    print("gold_list=",gold_list)
    columbia_river.append(water) #this adds the mega initial string first for the main string
    print('at this point the length of columbia_river should be 1 and it is',len(columbia_river))
    for item in gold_list: #loop that gets switch,endswitch pair from goldlist
        num1 = item[0];num2 = item[1];
        inputs_pair_to_copy_a_string(num1,num2) #get input string from goldlist
        copy_a_nested_switch(water)  #copy string based on switch,endswitch pair 
        print("====================")#puts resulting string into makeitwork[0] and output
        output = makeitwork[0]       #put nested string into columbia_river list
        columbia_river.append(output)
    print("length of columbia river =",len(columbia_river))
    counter =1
    #adding here the initial string which will be used to make the main switch
    print("now loop thru columbia river to see the switch bodies seperated")
    for item in columbia_river:
        print("counter=",counter)
        print(item);print("===========");counter += 1
##================================================================        
print("........mmmmm...time 10:20 am Sunday dec 12th")
print("end of crucial test copying the strings and putting them into a list")
split_up_big_string_into_nested_switches(red_robin)
#exit()   
print("okay from this point forwards I have access to the columbia_river with the strings in it") 
     
     
     
     
     
     
     
     
     
     
     
     
     
     
#######======================================== ## find_nested_switch_game
#the input is the whole string afgter having added comment of swithc line number in loopstring[0]
#x =11; y = 60;
##=======================================
##  testing_code_copying_string_adding_it_to_list()
##========================================
def testing_code_copying_string_adding_it_to_list(x,y):
    print("testing code copying string adding it to list")
    inputs_pair_to_copy_a_string(x,y)
    #water is the modified string with line number (but need to only add the line numbers once as comment
    copy_a_nested_switch(water) #this takes in switchstring with switch numbers added as comment
#######=========================================
    output = makeitwork[0]        #this would have to be after the call to copy a nested switch
    columbia_river.append(output)

#testing_code_copying_string_adding_it_to_list(11,60)


print("now printing out columbia river")
print("length of columbia river =",len(columbia_river))
for item in columbia_river:
    print(item)
    
#exit()
 





start  = 7  #hard coded beginning of nested switch
finish = 14  #hard coded end of single nested switch 
## COPY A NESTED SWITCH
############################
start_and_finish=[]
start_and_finish.append(0) #position [0] #ignore
start_and_finish.append(start) #position [1]
start_and_finish.append(finish) #position [2]
#so we have
start_and_finish[1] = 7
start_and_finish[2] = 14
#############################
r=gameday
#linecounter=0
makeitwork=[]
makeitwork.append(0)
print('======SECOND ATTEMPT======')
#######========================================
copy_a_nested_switch(r) #this gets put into r as a parameter
#######=========================================



#lines 1 thru 9 
 #this looks for the line number of endswitch for the nested switch
print("testing getting a COPY TOP HAT OF MAIN SWITCH")
print('this also grabs and displays the inner switch first line')
#the inner switch needs to be the last line of this string
##================================================
start = 1 #starting from 11 not 10
finish = 10
#linecounter=0
abovenestedswitch=''
print("this was put into a function on July 15th, 2021 ===")
####################################
## copy_top_hat_of_main_switch(): #this grabs the string of the main switch above 
# the first nested switch in this case there is only on 
####################################
terriblysmart=''
def copy_top_hat_of_main_switch(): #this is grabbing the top of 
    #the switch case just above the first nested switch 
    print("======copy top hat of main switch()====")
    global abovenestedswitch
    linecounter=0 #string name find_nested_switch_game
    for line in find_nested_switch_game.splitlines():
         # between >= 1 and <= 10
        if linecounter >= int(start) and linecounter <= int(finish):
            abovenestedswitch += line + "\n"
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result copy above  first nested switch case ")        
    print(abovenestedswitch)
    terriblysmart = abovenestedswitch

#copy_top_hat_of_main_switch()  #not called yet

print("end of copying top half above nested switch ")  
print("it should end with switch which we will edit")

mystringtest='''
	switch() #7
		case 'funny':
			print('fun')
		case "da":
			print('yeah')
		default:
			print('bye')
	endswitch #14
'''					
					

####################
#replace switch

#linecounter= 0
newlist=[]
newlist.append(0)
#newlist[0]
# I just put this into a function to have control over it 
#COPY COATTAILS BOTTOM OF BIG SWITCH AFTER NESTED SWITCH END
################################################################
## copy_coattails_bottom_of_big_switch_after_nested_switch_end():
################################################################
def copy_coattails_bottom_of_big_switch_after_nested_switch_end():
    print("copy_coattails_bottom_of_big_switch_after_nested_switch_end()")
    linecounter=0
    start = 21 #INPUT PARAMS TO GRB need to put these in a list for efficiency
    finish = 32
    outerswitch=''
    for line in find_nested_switch_game.splitlines(): #string looping thru
        #   IF BETWEEN line numbers 21 and 32 
        if linecounter >= int(start) and linecounter <= int(finish):
            outerswitch += line + "\n"
            linecounter += 1
        else:
            linecounter += 1
            continue   
        
    print("testing getting a COPY COATAILS BOTTOM OF BIG SWITCH")
    print(outerswitch)
    newlist[0]=outerswitch
##===================================================





#this is turning code into a function on july 15th, 2021
#######======
#copy_coattails_bottom_of_big_switch_after_nested_switch_end()
#######=======





#here is where i make this temporary list that I will put the
#input strings of the main switch and the one nested switch for testing

inputstringswitches=[]

###################
##    swap(a,b)
###################
def swap(a,b,c): #c = starbucks[1]
    cooler =c.replace(a,b)
    return cooler #starbucks[1] =string with changes made
    
    
  
#this puts the nest_method on the line selected in the tophalf of the string
#################################
## swap_switch_for_nest_method(n)
################################# 
def swap_switch_for_nest_method(n): # I will add more values later perhaps 3 or 4 for coordinates
    global abovenestedswitch
    abovenestedswitch=terriblysmart
    print("called swap_switch_for_nest_method(n)",n)
    abovenestedswitch = abovenestedswitch.replace("switch(exp){","nested_switch_" + str(n) + "(n)")
    print(abovenestedswitch)
    print("===================")

#june 29th, 2021


def scan_input_string_for_number_of_switches():
    print('work on this')#I have this figured out now elsewhere
    
    
#commented this out on august 3rd testing making big method 
   
#this needs to be put into a method and called below actually
def fishfood(): #necessary testing that's all
    print('about to try new swap method')    
    swap_switch_for_nest_method(2) #feeds it the number 2 for testing
    outerswitch=newlist[0]
    outerswitch= makeitwork[0]
    maybe=abovenestedswitch + outerswitch
    print('we have stripped the nested switch from the main switch')
    print("and inserted a method for now")
    print(maybe)
    ######### put first main switch into inputstringswitches
    print("adding main switch and nested switch taken out into list")
    print("the next step will be to run it thru the silve_module")
    print(" to create teh strings output in python")
    inputstringswitches.append(maybe) #should be position 0

    print("and the nested switch is here before it's converted")
    print(makeitwork[0]) #roadrunner
    #roadrunner = roadrunner.replace("endswitch","}")
    ######### put nested switch into inputstringswitches
    inputstringswitches.append(makeitwork[0]) #should be position 1
    print("====== go for the gold =======")
    print("this shows the resulting strings accessed thru the list that")
    print("they were put into so I can access them now for running silve module")
    print("==--------------==")
    print("here is the result now")
    print(inputstringswitches[0])
    print("now the nested switch")
    #print(inputstringswitches[1])
    galaxy=''
    galaxy = inputstringswitches[1]
    print(galaxy)
    print("Now I replace endswitch with }")### replace endswitch with }
    inputstringswitches[1] = galaxy.replace("endswitch","}")
    print("now looking into inputstringswitches[1] endswitch should be gone")
    print(inputstringswitches[1])
    print("==== end of first major step ==in process of transformation ==")

#################===========
#fishfood()
#################===========




#############################
##  get_inner_switch_line()
#############################
def get_inner_switch_line():
    print("can we get serious here I mean really")       
    bronze=0     
    linecounter=0
    secondswitchline=0  
    for line in find_nested_switch_game.splitlines():
        if "switch" in line: 
            print(line) 
            linecounter += 1 
            print("switch line number = ",linecounter)
            secondswitchline = linecounter
            break
        else:
            linecounter += 1  
            continue
    print("line with inner switch =",secondswitchline)
    print("==================")
#the inner nested switch will obviously end within the same case it starts in.

###########==============
#get_inner_switch_line()  
###########===============


                
###########################################################
print("")
print("====")
print("")
print("get line number of each switch")
print("each number after first switch is a nested switch")
print("get the line number of each switch")
switcharoo=[]
switcharoo.append(0)

linecounter=0





#######################################
##  get_number_of_nested_switches():
#######################################
def get_number_of_nested_switches():
    print("get_number_of_nested_switches()")
    linecounter=0
    #this looks for the line number of 2nd switch for now more later  
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "switch(" in line:  #grabs first line
            print(line)
            switcharoo.append(linecounter)
            
            linecounter += 1
            continue  
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
              
            #if "switch_nest()" in line:
            #   print(line)
    print("line number of switches",switcharoo)  
    print(switcharoo[2])                

casecounter=0
case_count=0

##########========================
#get_number_of_nested_switches()
##########========================
###############################################################
################ testing call of these methods at once
###========== august 3rd test Tuesday nice air conditioning ====
def nested_switch_trapeze_tricks():
    print("==== nested_switch_TRAPEZE_tricks() called=====")
    loop_thru_switch_locations()
    get_case_line_numbers(find_nested_switch_game)
    get_larger_number_less_than_case()
    get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
    copy_a_nested_switch(find_nested_switch_game)
    copy_coattails_bottom_of_big_switch_after_nested_switch_end() 
    fishfood()
    get_inner_switch_line() #not sure if I need this one
    switcharoo=[];switcharoo.append(0);linecounter=0
    print("the nubmer of nested switches=")
    get_number_of_nested_switches()  # here it is 

#this calls it right here 
#nested_switch_trapeze_tricks()
#print("end of running nested_switch_trapeze_tricks() Gee what does it do")

####=============================== end of the line here==========



################################
## get line number of cases()
################################
def get_line_number_of_cases():
    print("get_line_number_of_cases()")
    for line in find_nested_switch_game.splitlines():
    #get each case number 
    #check if switch in it
        if "case" in line:  #grabs first line
            case_count += 1
            print("case_count=",case_count)
            print(line)
        
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
     
#answer 2nd case section    
#nested switch on line 10        
 #answer line 2 inside of case
 #case section 2 starts on line 8
''' OUTPUT
 get line number of each case section
		case 1 thru 3:
1
		case 4 to 7:
2
			case blable:
3
			case more:
4
		case 8 to 10:
5
case line numbers [0, 2, 8, 11, 14, 23]
Line 8 is case second section
We therefeore know that if switch is on line 10
then switch is on the 2nd line after the case section starts
====
get line number of each switch
each number after first switch is a nested switch
get the line number of each switch
	switch(exp) {  
			switch(exp){
line number of switches [0, 1, 10] <<<=== line 10 nested switch
'''
'''
 print('kangaroo hop hop!')
			switch(exp){
			case blable:
			   print("do something")
			   print("yep")
			case more:
			   print("nice")
			default:
			   print("we are done here")
			}'''  
    
    
    
#Monday june 28th, 2021 thinking
#get switch line number and case it's in and line number inside of case
#and what line the switch ends with }
#which I need to know to copy it. I can set the loop to start
#on a particular line and to concat a string and stop
#after coping a set number of lines. 
#Based on line count between switch and } which I can do first
#if line.startswith("switch") do until line startswith("}")




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






   
#def fantastic(): #we would know case number and therefore line number
#   newcounter=0
#  for line in output_string_test.splitlines():
#       if "case" in line:
 #          line_number.append(newcounter) 
       
       #and
       
       #I think that for the parser thats analyzing the input string
       #but the outoput python is quite different.
       #the nested method will be one line
       #so it's really  just adding the one line string
       #to a set of say 5 lines and moving the existing lines down 1 line
       
   #say second line after case 
   #test if something on that line
   #inner_switch_1('test7')
print("what can I do with lists")
print("the night is still young. competing with harvard and stanford")
red=[]
orange=[]
blue=[]
pink=[]
pink.append("\tempty")
red.append("\tone")
orange.append("\tdam")
blue.append('\ttuna')

super = pink[0]  + '\n'  +red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)
red[0] = "\tnestedswitchmethod" 
pink[0]= "\tfunny"
super = pink[0]  + '\n' + red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)

print("========")
line_1=[]
line_2=[]
line_3=[]
line_4=[]
line_5=[]
line_6=[]
line_7=[]
extra_line_1=[]
extra_line_2=[]
extra_line_1.append(0)
extra_line_2.append(0)
football =[]
football.append(0) #method name 
football[0]="\tinner_switch_1('test4')"

line_1.append(0)
line_2.append(0)
line_3.append(0)  #for example nested switch is line 3
line_4.append(0)
line_5.append(0)
#line_6.append(0)

#line_7.append(0)
 #say it's 4 line case 
line_1[0]="\tprint satement line 1"
line_2[0]="\tprint satement line 2"
########################################
line_3[0]="\tprint satement line 3"
line_4[0]="\tprint satement line 4"
print("================")
#if it's on line 3 we take top off to separate it 
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
# new
print("beginning state")
extra_line_1[0]=line_3[0]
extra_line_2[0]=line_4[0]

print("copying that will be don")
print(extra_line_1[0])
print(extra_line_2[0])

print("====bit flipping==== ")
print("putting nested switch in position 3 which is line 3")
line_3[0]=football[0] #designated line for nested switch 
line_4[0]=extra_line_1[0] #this is a novel approach restarting from 1
line_5[0]=extra_line_2[0]

print("after adding the switch nested method in position 3")
print('we then have this:')
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
print(line_5[0])
print("=========== now adding teh strings to magic concatting them ")
magic=''
magic = line_1[0] +"\n" +line_2[0] +"\n" + line_3[0] +"\n"+ line_4[0] +"\n" + line_5[0]
print(magic)  
print("=====================")  
print("let teh games begin")    
print("done")
#line_5[0]="line 5"
#line_6[0]="line 6"
#line_7[0]="line 7"
#line_8[0]="line 7"
mylist=[]
mylist= ["starter","one","two","three","four","five"]




def sosmart():
    mylist.insert(0,"starter")
    mylist.insert(1,"one")
    mylist.insert(2,"two")
    mylist.insert(3,"three")
    mylist.insert(4,"four")
    mylist.insert(5,"five")
    
    
def put_nested_switch_into_line(x):
    mylist.insert(x,"nested_switch") #it replaces the whole line
    print(mylist)
    
def reset_list():
    for item in mylist:
        del item
    
    print(mylist)

print("333333333333======333===================")
print("new attempt here  Friday June 25th -0--")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

print("======= water tower see how well this works=======")
print(mylist)
put_nested_switch_into_line(2)
sosmart() #resets it
put_nested_switch_into_line(1)
sosmart() #resets it
put_nested_switch_into_line(3)
sosmart()
print("===000000000000100000000000======")

# I ahve to split it in half somewhere and we have top above nested switch line
#and then we have the nestline
#and we have the bottom 

#so if we have lists for each line number of case section up to say up to 10 lines for now
#say switch will go on line 3 of 6 lines for an exmaple
#line 1 and line 2 are top
#line 3 is nest_switch_method
#line 4 to n is the bottom




     
case_guts='''
\tprint("aaaaaa in the main switch")
\tprint("bbbbbb below")
\tprint("ccccc#result of innerswitch running
\t#what ddddddd?? use a list to capture it
\tfallthr eeeeeeeu('word'
'''
    
    #method inner switch withnumber (input will likely be from a list later)
add_this="\tinner_switch_1('test4')\n"
nested_method_name=[]
nested_method_name.append(add_this)
crystal=[]
crystal.append(0)# [0]


#get input string of case section
#
# I need to get the line number where the switch is supposed to go
# based on the input C style location of the nested switch
# based on which case it is in (the sequence starts from 1)
# then detect the line number in order within that case where the switch starts
#
#
  
#exmaple, we need to add nested switchmethod to line 2
#so we copy line1

top=[]
middle=[]
bottom=[] 
put_in_here=[]

#### fudge ########    
def fudge():
    #def copy_one_line_inside_case(x)
    astring=''
    soupstring=''
    line_counter =0
    print(case_guts)  
    
    print("===========STAGE 1=========")  
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == 1:  #grabs first line
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print('first line string=',astring)
    #################
    newstring=''
    coolstring=''
    line_counter =0
# copy from the line where we want to insert (line 2) 
# thru to last line in case section
    print("============STAGE 2===========")
    #this copies 2nd string to string n (the rest)
    
    for line in case_guts.splitlines():
        if line_counter >= 2:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
        
    print(newstring) #this copies all of the lines into newstring
    put_in_here.append(newstring)
    #this is the switch method string on top of rest of case body lines
    #copy from targetline insertion line thur last line
    # we then add the nested switch method to the rest of the case 
    ##########################################
    #this will be a new helper method
    
    #def add switchline to rest of case body()
    #this is necessary BEFORE adding first line
    print("=================STAGE 3=================")
    egg=[]
    nested_switch_method_name=[]
    fossil=[]
    #fossil.append(0)
    #fossil[0] = nested_switch_method_name[0] + put_in_here[0]
    coolstring = add_this + newstring#how so I insert to front of a string
    #higher =nested_method_name[0] + put_in_here[0]
    egg.append(coolstring) #egg[0]
    
    #middle.append(coolstring)
    print(coolstring)
    glory=''
    #this adds the first string followed by coolstring
    #########################
    #this adds the line(s) above the insertion line 
    #put first string ontop of rest of lines of 
    #this adds the first line which was skipped to the new switch line
    #with the rest of the case body
    
    
    #def add_top_above_lines_above_switch_line(a,b)
    #a = string with the switch_method name
    #b = rest of the lines
    print("==========STAGE 4==========")
    nested_switch_method_name.append(astring)
    glory = astring + coolstring#[0] #now it's a list
    print("glory shows")
    print(glory)
                #method name in list     #nested method name + rest of lines in case
    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
    print('from list now') #string add_this
    print(egg[0])
    #bottom.append(glory)
    #print("now printing from the list bottom[0]")
    #print(bottom[0])
#   def add

#then replace first line with new line methodnested name
#    then add paste first line to new beginning of string
print('copy string from line 2 bbs')
fudge()
#now I can insert in line 2

print("========= result of fudge  ============ ")
print("========= Fudge Happy Potter Hogwarts ========")

#convertList = ' '.join(map(str,list1)) 















###################################
## copy one line inside of case (x)
####################################
def copy_one_line_inside_case(x):
    print("copy one line inside case()")
    astring=''
    soupstring=''
    line_counter =0
    #print(case_guts)    
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == x:
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print(' line',x,' string=',astring)
 ####################   
 #copy just the line entered within the case body
copy_one_line_inside_case(1) 
copy_one_line_inside_case(2)
copy_one_line_inside_case(3)
copy_one_line_inside_case(4)
copy_one_line_inside_case(5)






#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========








################################################
##  get_below_after_method_insertion()
################################################
def get_below_after_method_insertion(y):
    newstring=''
    coolstring=''
    line_counter =0
    #this copies 2nd string to string n (the rest)
    for line in case_guts.splitlines():
        if line_counter >= y:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
    print('below after method insertion',y)   
    print(newstring) #this copies all of the lines into newstring
    #this is the switchm

#this grabs lines within the case after the input line number to the end
get_below_after_method_insertion(2)
get_below_after_method_insertion(3)
get_below_after_method_insertion(4)
get_below_after_method_insertion(5)
 
egg=[]
#def stage_three(a,newstring):#("====STAGE 3====")
#    print('stage_three called')
#    coolstring = add_this + newstring#how so I insert to front of a string
#    egg.append(coolstring) #egg[0]


#stage_three(add_this,newstring)

### stage four ########
#def stage_four():
#    print('stage-four called') #method name in list     #nested method name + rest of lines in case
#    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
#    print('from list now') #string add_this
#    print(egg[0])  
    
#stage_four()    
#it's going to be in the code gen phase actually where I add the
#one line (so much easier) to the particular case that it's in
#and on the line number within that case below a particular line
#But I the main switch is generated so it should have a marker
#like nested_switch_1_3('test4')
#case number in series and line number within that case

# 
# 
# x=1
# def paste_inner_switch_method_into_string(x):
#      print("===================")#this goes thru the string and detects a nested switch
#      case_counter =0
#      for line in output_string_test.splitlines():    #and copies it and puts it into 
#         case_counter += 1    #acgtaully it gets the start and stop location line numbers
#         if "case" in line:
#             print("case detected in line")
#             case_counter += 1
#             if case_counter == x:
#                 print("this should be our match")
#                 print("this is case number ",case_counter,"and x=",x)
#                 print("therefore we do the MAGIC SHIT HERE")
#                 fantastic()
#                 break
#         else:
#             continue
# 
# list1=[]
# list1.append(0)
# def test_this():
#  #put it into a list
#     list1[0]="inner_switch_1('test7')"
#     say it's line 
# 
# #possibly have it scan thru the output python generated
# I might need a marker  #comment where to put it based on
# just the case. I can finangle where in a case I add it 
# since it's just a method and after I get it placed
# then I can change where in the case it is since it's
# within the case body so I have latitude and the body case 
# will be isolated so there should be some leeway. 





happydays='''
line =""
varholder=[]
varholder.append('0')
###############################============
	
# ===== inswitch ========
def inswitch(n):
	if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
		n = str(n)
	global case
	case = n.lower() 
#=====================
# for infallthru    
def infallthru(n):
	eval("inswitch('" + n + "')")
global x
x = "one" #it was "one"     
tahoe=[]
tahoe.append(0)
victory=[]
victory.append(0)
#######################
### inner switch_1(n):
#######################
def inner_switch_1(n): #test2 is the test
	print("=======inner_switch called==1==",n)
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
	inswitch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			infallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			infallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			infallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
			#######################
			print("out of inner switch 1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break   
###================
inner_switch_1(zoo[1]) #this calls it with zoo[1]
'''
##========================
##  darkness()
##========================
def darkness():
    print("darkness() =========")
    print(happydays)
    touble=''
    print("darkness called=====>>>>>>>>>=====>>>>")
    print("happy days analyze the pattern for the tabs and how many ")
    counter =0
    print("===================")#this goes thru the string and detects a nested switch
    for line in happydays.splitlines():    #and copies it and puts it into 
        counter += 1    #acgtaully it gets the start and stop location line numbers
        if "\t" in line:
            print("tab detected in line")
            trouble =line.count("\t")
            print(line)
            print("tabs=",trouble," ",counter)
            trouble=''
        else:
            continue
            
darkness()
  
  
  
  
  
  
           
print("HERCULES TEST RIPPING OUT TABS FROM FRONT")   
'''
to set adding tabs i realized there are two modes
regular switch and nested switch
and to subtract a tab i need to cancel nuke tabs in a line then add the desired number
to get what i want
'''  
import re
myString = "\t\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
print(myString)
print("now rip out the tabs")
myString = re.sub(r"[\t]*", "", myString) #was * where I have 2
print(myString)   
print("now add a tab")

myString = "\t" + myString
print(myString)    
myString = "\t" + myString #add second tab
print(myString)              
            




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






##### this makes the input for zoo[1] lowercase
###############################
## make_input_lower_case() ####
###############################
def make_input_lower_case():
    answer = zoo[1]
    answer = answer.lower()
    zoo[1] = answer    

# what i doing here is putting the dynamic built inners switch python code into a list.
# this is just beautiful and brilliant.

fiddle=[]
fiddle.append(0)
fiddle.append(happydays) #appends the string and puts it into fiddle[1] and exec()
#print(fudge[1])
print("TESTING BLADE RUNNER SERIES =what does an innerswitch by itself need")
print('it is all in one big string about to execute it')
#THIS IS CRITICAL INPUT IN   zoo[1]
zoo[1] = 'test3'# testing (user input lower or upper)
make_input_lower_case() #this converts the input for nested
#see if it works
print(fiddle[1])

exec(fiddle[1]) #this is executing the nested switch method above




sewage = ''
#for item in fiddle[1]:
#    sewage += item
#print("sewage=",sewage)
#print("=====")   
#x =sewage.replace("\t","\t*") #this is so I can see the tabs



#right here 

## add this to it:  
#def inner_switch_3(n): # 
samplecode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
	inswitch(n) #3 
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			infallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			infallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			infallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			inner_switch_2('test7') #commented out
			#######################
			print("out of inner switch 1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break
'''

#modified on november 12th 2021 friday to get this sucker working 
##====================================
##  get_switch_number_in_comment()  it gets the switch number from FIRST LINE OF STRING then bails
##====================================
#this looks ofr the first switch at 3 tabs need to modify it to 1 tab depth. aha 
def get_switch_number_in_comment_in_output_python_code_string(stringname): #this might be for when
	print("get_switch_number_in_comment_in_output_python_code_string(stringname)")
	print("indian braves dancing for rain")
	# I create copies of the switch body strings
	print("get_switch_number_in_comment_in_output_python_code_string() called it's getting the first inner swithc at 3 tabs length ")
	awesome=''
	y = ''
	counter =0  #say it's 3
	print("this is what the string we are manipulating looks like")
	for line in stringname.splitlines():
		print(line)
	print("================-------===")
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter =0 #this looks for inswitch at 1 tab depth length 
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tablength= line.count("\t")
		if "inswitch" in line and "end" not in line and tablength == 1:#and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number ",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;



flynow=[]
###============================================================================
##  put_output_python_nested_switch_code_into_def_inner_switch_numbered(string):
##==============================================================================
#try this november 12th struggling here 
#I want to see this
'''
def inner_switch_3(n): 
    print("=======inner_switch called==3==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    inswitch(n)                           #<<====== inswitch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
'''

def put_output_python_nested_switch_code_into_def_inner_switch_numbered(stringname):
	print('===== TESTING RED ALERT ======')
	print("put outpout python nested switch code into def inner switch numbered")
	#this calls a method to get this switch number to use to number this nested switch
	thenumber= get_switch_number_in_comment_in_output_python_code_string(stringname) #use other code similar to this
	#print("the number it returned is",thenumber) #thenumber=22 #for testing
	string_to_add= "def inner_switch_" +thenumber.strip() +"_(n):\n"
	concatstring = string_to_add + stringname;
	#print("lets see if it actually worked or not and concatted it correctly")
	##################################
	for line in concatstring.splitlines():
		print(line)
	flynow.append(concatstring) #so the resulting string modified exists.
	#########################

#thenumber=22
#string_to_add= "def inner_switch_" + str(thenumber) + "(n):" 
put_output_python_nested_switch_code_into_def_inner_switch_numbered(samplecode)
#makeitso = string_to_add + samplecode;

def testit():
    print("testit called to see if I put def nested method at top of string")
    print("doing samplecode first in virgin form")
    for line in samplecode.splitlines(): #unchanged original output string
	    print(line)
    print(":")
    print("end of test run....")
    print(":")
    print("and now after putting def nestd switch numbere at top")
    print("did this sucker work....please...")
    #for line in makeitso.splitlines():
	#    print(line)
#testit() 
    
dumbstringcode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
			
	switch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			fallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print (" case behavior works in Python now!")
			print("")
			fallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			fallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested  ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
			#######################
			print("out of inner  1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break
'''


fridge=[]
fridge.append(0)


print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
#================================================
x =dumbstringcode.replace("switch","inswitch")
dumbstringcode=x
y = dumbstringcode.replace("fallthru","infallthru")
supergood = y
#=================================================
####### this fixes a bug of the inner switch getting an extra in and it's taken out
#######3=======
print("--------000000000000---testing changing switch and fallthru ====")
print("-------=0000000000000  into inswitch and infallthru ------")
print("testing conversion of a python string of a nested switch")
print("to tranform it into inswitch(), infallthru()")
print("this should be the working version of ")
print("have changing switch to inswitch and fallthru into infallthru")
print(supergood)
print("did it finally work or not===========>>>>>")
z = supergood  #this fixes a bug where the nested switch method is wrong
y = supergood.replace("inner_inswitch","inner_switch")
print("and this should fix the bug of accidentally namming inner_switch")
exam = y
print(exam)
print("===== end of good working code ==============")

#for line in dumbstringcode.splitlines(): #switch case in JS
 #   #print("smartcounter =",smartcounter)
 #   
 #   if "\t\t\tswitch" in line:
 #        umbrella += "inswitch(n)\n"
 #   if "fallthru" in line:
 #       umbrella += "infallthru(
 #       
 #              
       #this is the range I want to print



#this is where the swo string is I was looking for.

print("july 3rd test 2021 6:53 pm")
print("testing nested switch string BETA TESTING ====0")
#find_nested_switch_game ='''
#clever('4')
swo ='''
	switch(exp) { #first true test 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){     # inner s w i t c h      
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


#this one has two nested switches that I will try next. 
swo_next ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # inner s w i t c h     =============  
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #=========================
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 28    ===============   
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #38===================================
			fallthru
		
		default:
			print('the end')
}
'''	
# I seem to recall a bug usin

#this is testing sensing a multiline switch with more than one switch
####===============
#testing moved here for safety
# CHECK FOR THE NUMBER OF SWITCHES WITHIN THE INPUT STRING
nested_switch=[]
nested_switch.append(0)
nested_switch[0]= False # by default
################################################################################
#determines if a string input is a nested switch with at least one inner switch
################################################################################

###################
##  jumanji(y)       tests if string input has at least one nested switch
###################  sets nested_switch[0] = True
def jumanji(y):  #instead of this I just do a count for endswitch which is just one line of code. 
	print("--------------------------")
	print(" --- J U M A N J I -------")
	print("--------------------------")
	print("this determines if it's a nested switch with a nested switch or more in it")
	print("testing jumanji() counting switches and endswitches")
	#just some sample ifs to read what's the input look like 
	print("this is looking into the string below")
	#print(swo)
	print("--- end of string that we will analyze ---")
	print("")
	print("get count of lines startingwith switch in the string")
	#this counts switch number in the string
	switchcounter=0
	for line in y.splitlines(): #determine if switch is in line
	#this looks for switch in the line but endswitch can't be in this line
		if "switch" in line and "end" not in line:
			switchcounter += 1  ## SWITCH COUNTER
			#print("switchcounter=",switchcounter)
			print("yea this starts with switch")
			continue
		else:
			continue
	print("total switches =",switchcounter)
	
	##============================
	#this counts endswitch number in the string
	print("get count of lines startingwith endswitch in the string")
	endswitchcounter=0		
	for line in y.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line: 
			endswitchcounter += 1  #END SWITCH COUNTER
			#print("endswitchcounter=",endswitchcounter)
			print("yea this starts with endswitch")
			continue
		else:
			continue
	print("TOTAL endswitches =",endswitchcounter) #endswitchcounter
	print("end of this checker ===========")
	print(" total switches",switchcounter, "and total endswitches",endswitchcounter)
	
	#this sets the flag in nested_switch[0] if at least one nested switch
	#===============================================
	#if one or more switch and one or more endswitches
	if switchcounter > 1 and endswitchcounter >=1: #actually if endswitchcounter 1 it's True
		nested_switch[0] = True
	else:
		nested_switch[0] = False
	
	print("the result of this test for if this has nested switch(es)") 
	print("this is the list with the critical nested_switch[0] value")
	print("WHAT DOES THIS SAY --  it should be True")   
	print("nested_switch[0] = ",nested_switch[0])
	print("=================")
	print("=================")
	print("this  below this is dog breath that doesn't work")
	print("====== end of this initial switch counter filter that will eventually")
	print("=== trigger bypass205 to do multiple switches ====")
	
	
#end jumanji()  ===================||	
	
jumanji(swo)  #called here to test it
print("just called jumani with swo and if nested switches below will be True")
print(nested_switch[0])
#this should be the output the nested switch copied








#this is still using endswitch they aren't swopped out yet

## July 5th, 2021  testing Monday July 5th line number 1593
# July 18 added a second nested swithch to test on lines 28 to 38
samplestring ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch  #======== ============38
			fallthru
		
		default:
			print('the end')
}
'''	


samplestringzoo1 ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			print('hello world')
			switch(exp){  # ===== 24===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'rats':
					print("do autumns")
					print("yep")
					fallthru
				case 'more':
					print("badness")
					break
				default:
					print("we tesla done here")
			endswitch  #========== 34  ==========notice this for it is key 
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======39       
				case 'autumn':
					print("falling leaves")
					print("a night on the town ")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much cranberries")
			endswitch  #======== ============49
			fallthru
		
		default:
			print('the end')
}
'''	


#######################
#### testing ######
### samplestring with switches taken out ####
#### and nested methods replacing it ########
######## july 22 ###testing #####
##### this represents the accurate main switch with proper indentation
samplestring_main ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			nested_switch_1(n)
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			nested_switch_2(n)   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''	


#nested_switch_2(n)
#july 21st 2021 get teh number of lines in the string
# count endsswitches to get number of nested switches
# do the main switch last which erases(skips) the nested switches
#here I count the number of lines in the string to get last line 
# the tricky part was figuring out when to grab the main switch but I couuld actually
#do it first it doesn't matterand make a copy of it and modify the copy


#so I would add a third record to the pears dictionary 1, 44
######=== total lines in the string for the main switch =========
#using the whole string I know that the nested switches will be on the first line
thecounter=0
for line in samplestring.splitlines():
    print(line)
    thecounter += 1
    
print("the total lines =",thecounter)
print("================ wile e coyote =======")





tuna ='''
	exp = '4'
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp = 'blable'
			switch(exp){  #this one has input here         
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
			exp = 'fish' #and we have input here too. 
			switch(exp){          
				case 'fish':
					print("do something")
					print("yep")
					fallthru
				case 'trout':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			fallthru
		default:
			print('the end')
}
'''




# ibm list is used for holding switch strings 
ibm=[]
ibm.append(0)

use_number=[]
use_number.append(0) #[0]

#def between(x,condition,y):
    
#experimentatl copy the nested switch ignore the rest and only Do one.


#this only copies one nested switch within the main switch
#this i pased on knowing the input 
#these are hard coded here

#just put this here to see if it works correctly
# saturday july 17th, 10:11 am starbucks
print("STARBUCKS CRUCIAL testing saturday morning")
'''
this is first emptyhing the switch and endswitch locations lists
'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





print("the one below this line should produce 2 switches and one with 10,20")
#this find the location one one pair of a nested switch and end switch

#this gets the start and end from samplestring
#empty_switch_and_endswitch_list_locations()



#this has the output of filling these lists
#switch_location
#endswitch_location

print("stopping this now to see what it looks like with the switch list and endswitch list")
#return  # to stop the program
''' THIS IS THE OUTPUT OF RUNNING THE FUNCTION ABOVE
===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === 
I need to delete teh first swithc location
switch_location= [10, 28]
endswitch_location= [20, 38]
'''

print("=== shazam level about to try fancy stuff ====")

#loop
#pairlist is actually a list 
pairlist=[];theforce=[]
#this would just add the switch location
alpha='';beta ='';counter =0;jedi='';
#this reads in data from switch_location
#               and from endswitch_location
#======================================================
# fill_pairlist_with_switch_and_endswitch_pairs(yy):
#======================================================
def fill_pairlist_with_switch_and_endswitch_pairs(yy):
    print("====fill pairlist with switch and endswitch pairs()=====")
    print(" godzilla ruled over rodan ")
    get_switch_and_endswitch_locations(yy) #===== using sample stringh 
    print("this is grabbing the switch locations which are dynamically added to a dictionary for pairlist")
    print("the length of switch location =",len(switch_location))
    print("the length of end switch locatoin =",len(endswitch_location))
    print("==============...............============")
    # loop thru list switch_location ==============================
    counter =0;allpha='';beta='';           #so this is one small set switch and endswitch line numbers
    for item in switch_location: #this loops thru the list switch_location          
        alpha = switch_location[counter]
        beta  = endswitch_location[counter] #they should be the same length 
        #here the positions are appended to pairlist dictionary
        pairlist.append([alpha,beta])       #always in sets of 2 #adds alpha and beta as list into pairlist  list
        print("pairlist=",pairlist)
        counter += 1
    print("======================")
    newcounter=0
    print("the length of the pairs =",len(pairlist));print('let me see what is in pairlist')
    print("pairlist=",pairlist)
    for item in pairlist:  #this is the combined pairlist
        print(item)
        sosmart = pairlist[newcounter] #here I access first and second numbers in pairlist
        print(sosmart[0]);print(sosmart[1]) 
        print("====== JEDI TEST ========")#not to be confused with jumanji above 
        #this takes in data from switch_location list and endswitch_location
        # and glues them together into a new pair list into 
        # list called theforce
        #this is constructing filling the data in the dictionary pair values
        jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
        print('jedi=',jedi) #like this [12,16]
        
        #put pairs into list into jedi and append to theforce
        theforce.append(jedi) #the pair is added  to theforce list
        turbo  =theforce[newcounter]
        newcounter += 1
    print("theforce=",theforce)
    print("the length of theforce list =",len(theforce))
    print("did we make it this far... in a galaxy")
    #adding loop here to test this
    print("doing a newest test  christmas tree of the pairs in list theforce")
    acounter=0
    print("====magic brew time=====")
    print("== the filled list with pairs of switch endswitch is called theforce ===")
    for item in theforce:
        print(item)
        print("=======")
        cool =item
        print("cool=",cool)
       
        print("acounter=",acounter)
        x=''
        x = cool.split(",")  # see if this trick works
        print(x[0], x[1]) # see if this trick works
        print("end game")
        acounter += 1
        continue
    print("end of printing each item in theforce")
###=====





thisdict ={}


def cleanse(x):
    x = eval(x)
    return x;
    
#modified this method on august 11th wednesday, 1:11pm
############################################
##     adding data list to dictionary
############################################
def adding_data_list_to_dictionary(dictname,key,newdata_list):
    print("LOOK AT THOS at input params see if they are right first")
    print(dictname)
    print(key)
    print(newdata_list)
    return #temporarily halts this from running
    
    print("called adding data list to dictionary")
    #tryit =eval("" + dictname + "[" + key + "]" + "= " + newdata_list +"")
    #tryit =eval("" + 
    angel =dictname
    thekey= key
    newdata_list
    print(angel)
    print(thekey)
    print(newdata_list)
    print("====>>>====>>>end of games...")
    #print(tryit) #to see what it sees
    
    #thisdict["4"] = "[12,22]" #adding data list as string to dictionary
    
    #eventually I will add 1 to dictionary length
    
    ##########################################
    #dictname + key + [12,22] input format 
    ##########################################
    #dictionary name should be known
    print(thisdict)
    for item in thisdict.values():
        print(item)
    print("testing getting value in dictionary by key")
    x = thisdict["4"]
    
    #x = thisdict.get("4") #this should work also
    print(x) #together
    x = eval(x)#just dreamed this up and it worked
    print("this represents getting the x and y for a nested switch locations")
    print("first number",x[0])#seperate
    print("second number",x[1]) #separate
    
    
        
#OUTPUT
'''
called adding data list to dictionary
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, '4': '[12,22]'}
Ford
Mustang
1964
[12,22]
testing getting value in dictionary by key
[12,22]
first number 12
second number 22
'''
print("fast wile e coyote test  adding data list to a dictionary")
print("==========")
print("==========")

# october 28th, 2021 thirstday
# I need to go thru combined pair list three + five + seven and feed it into a dictionary

## its really get index pair in struct
#### get_number_in_struct(x)   THIS WORKS!!!!!!!!!!! oct 26th



pair_returned=[]

##======================================
##  get_number_in_struct(x):
##==================================
def get_number_in_struct(x):
    print("get_number_in_struct(x) called")
    print("the input was x",x)
    print("get_number_in_struct(x) called too cool")
    print("get ",x)
    #using eval() to do thisdict.get(x)===###################
    apple_pie=eval('thisdict.get(x)')
    print("=====///get number in struck(x) called---------///")
    print("get number ", str(x), " in struct with x called")
    print("apple-pie=",apple_pie)
    super = apple_pie
    if apple_pie == None:
        print("it is None")
    else:
        print("why not",super[0],super[1])
        print("now splitting it into the two numbers within the pair of switch endswitch")
        print(super[0])
        print(super[1])
        #doing this to have common lists for passing on to other functions later
        pair_returned.append(super[0])
        pair_returned.append(super[1])
        print("pair_returned at this point has",pair_returned)
#=============================================


    
#adding_data_list_to_dictionary(thisdict,'5','[12,22]')
print("washing machine time add this '5','[12,22]')")
print("thisdict",thisdict)
numb = '6'

thisdict[numb] = [23,47] #this worked
print("pretty autumn testing")
goaway=''
goaway = thisdict['6']
print("fishfood =",goaway)
print('dirt simple test')
'''
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now 
  "2": [11,60],
  "3": [15,51],
  "4": [23,46],
  "5": [31,41],
  "6": [62,86],
  "7": [66,77]
 #no comma after last data piece apparently
}
'''

#=======================
#add data to struct
#======================

print("no time for pumpkin carving")
#numb = number and aset = [start,stop]
aset=''
numb=''
# this method works on oct 26th 2021
##==============================================
## add_data_to_struct(thisdict,numb,aset)
##====================================================================
def add_data_to_struct(thisdict,numb,aset):
    return #abandoning this too confusing going with just a list of lists
    print("add data to struct")
    print("numb=",numb)
    print("aset=",aset)
    #numb='12' #the number will keep a rolling total and added automaticaly
    thisdict[numb] = aset  #this just seems too simple.
    print(thisdict) 
    
#add_data_to_struct(thisdict,numb,aset)
##============================

gooddata=[]
##==========================================
## get value in dict (name ofdict,x)
##==========================================
def get_value_in_dict(name_of_dict,x): # we will know the dict it won't change
    return #abandonning this for being too confusing and unworkable at this time
    print("plumtree=",plumtree)
    print(thisdict)
    print("get value in dict",x)
    nn = plumtree.get(str(x))
    print("================")
    print("using key",x,"it retrieved from the plumtree dictionary",nn)
    print("================")
    # I was assuming (wrongly) that all keys input would be in dictionary; unknown
    if x in thisdict: #it can't be this simple
        y=eval("plumtree[x]")
        print(y)
        del gooddata[:] #clears it out 
        print(y[0],y[1])
        gooddata.append(y[0])  #this returns with the index[0][1]
        gooddata.append(y[1])
    else:
        print('x',x,'is not in dictionary plumtree')
    
#this builds a new record
#numb='2'
#aset =[11,47]
#thisdict[numb] = data1
#print('input of 2 for [11,47]')
print("==tuesday testing ==add data to dictionary and then access it")
#add_data_to_struct(thisdict,numb,aset)
'''
if '2' in thisdict:
    print('yes 2 is in thisdict')
else:
    print("nope no 2 in thisdict")
#get_value_in_dict(thisdict,'1')
'''
##==========================

print('testing right here === bingo time === adding data to a struct')
#aset =[10,30]
#numb='2'
print('before adding the numbers pairs')
#add_data_to_struct(thisdict,numb,aset)
###=================================


#print(thisdict)
print("should have 2 and 11,47 added to it above")
print("==== boo ==========")
print("cool little test here getting data from dictionary struct")

# GET NUMBER IN STRUCT
#get_number_in_struct('2') #should be [11,47] #it really gets the pair data
#what exactly does this return
#print("output is this ========> ",pair_returned[0],pair_returned[1])
#print("should be  11 and 47")
##===========================
print("cafe borrone coding time")
#aset=[21,37]
#numb='12'
#dictname=thisdict
#add_data_to_struct(dictname,numb,aset) ###====================
#apple_pie=thisdict.get('12')
#apple_pie = aset
#print("should be 21, 37",apple_pie)
#aa = apple_pie[0]
#bb = apple_pie[1]

#print(aa)
#print(bb)
print("====")
print("get thisdict 9")
print("========= happy coding time ====")
#get_number_in_struct('9')
#get_number_in_struct('12') 
#print('should return [21,37]')
print("====== mocha ice drink ====")
#this retrieves the data based on 9
print('porsche time...........')



#apple_pie=thisdict.get('12')
#print("apple pie =",apple_pie)
print("where are we now")


print("stanford football test...")

#print(thisdict)
#print("======values======")
#for x in thisdict.values():
#    print(x)
#print("==========")
#print("=======items=====")
#for y in thisdict.items():
#    print(y)

#x='2' 
#get_number_in_struct(x)
#x='6' 
#get_number_in_struct(x) 
#x='9' 
#get_number_in_struct(x)
#x='12' 
#get_number_in_struct(x)       
#print("======= gameover ======")
#I will need to loop thru the dictionary blueberries
# so now I am on my way of loading the dictionary which will
#just happen once after the pairs are created.

#print(apple_pie) #should be [22,44]
#print("=====")


#x='9' 
#get_number_in_struct(x)   
#print("should return [22,44]")
#thisdict["GTI"] = [75,85]
#print(thisdict) #should include Cherry=[23,47]
#apple_pie=''
#print("below this it should be 23,47")

#x='6' 
#get_number_in_struct(x)   #should return [23,47]
#print(apple_pie[0])# = 23
#print(apple_pie[1]) # = 47
#apple_pie=thisdict.get('GTI') #should return [23,47]
#print(apple_pie)


#creating a dictionary with initial values (brilliant)
#this is new for oct 7 thursday, 2021 morgan hill starbucks
#data =dict() #create empty dictionary
#data =dict(a=1,b=2,c=3)   #short and sweet fill with initial values
#print(data)

#change a value in a dictionary
#thisdict["year"] = 2018

#if "model" in thisdict:
#    print("yes model is one of the keys in thisdict")
#    
#    #add item to dictionary
#    thisdict["color"] = "red"
#    
#update command
#thisdict.update({"color":"red"})


'''
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now 
  "2": [11,60],
  "3": [15,51],
  "4": [23,46],
  "5": [31,41],
  "6": [62,86],
  "7": [66,77]
 #no comma after last data piece apparently
}
'''
plumtree={} #new dictionary
####=======================================================
#feed list of pairs into dictionary (such as blueberries)
print("testing looping thru list")
#this represents a list of sublists of the switch,endswitch pairs
#I need to make testlist
testlist=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]

returnlist=[]
returnlist.append(0)
#I can make my own custom methods to get from list
#the list is actually referenced starting from 1 where I start the counter
##==============================================
##  get_pair_from_testlist(x):
##==============================================
def get_pair_from_testlist(x):
    print("=========get_pair_from_testlist=========")
    print("testing get_pair_from_testlist",x)
    counter = 1
    print("inside the loop we see for x this ",x)
    for item in testlist: #it doesn't really loop, it's a one pass loop
        #if number entered bigger then length of list warn then break    
        if x > len(testlist): #error detection bypass worked 
            print("ERROR went beyond number length in list")
            print("please enter a number less than ",len(testlist))
            break
        #if number entered less than 1 warn then break
        if x < 1: 
            print("ERROR number must be 1 or higher")
            break
        if counter == x: #it matched with a doable number
            print(item)
            alpha = item[0]
            beta  = item[1]
            print(alpha,beta)
            returnlist[0] = [alpha,beta]
            print("returnlist[0] =",returnlist[0])
            break
        else:
            break
##==============================================================

            
get_pair_from_testlist(1)
get_pair_from_testlist(1)
print("the pair is ",returnlist[0][0],"really cool",returnlist[0][1])
get_pair_from_testlist(-1)
get_pair_from_testlist(0)
get_pair_from_testlist(2)
get_pair_from_testlist(3)
get_pair_from_testlist(4)
get_pair_from_testlist(5)
get_pair_from_testlist(6)
get_pair_from_testlist(7)
get_pair_from_testlist(22)

#Okay. I need to fill the testlist from the threetabs, five tabs seven tabs nine tabs



#the list with the pairs is in testlist

#this dictionary is being abandoned for over complexity and confusion
# november 3ed 10:03 am morgan hill

#this reprents looping thru the testlist and filling data into the dictionary and populating it
##====================================================
##  fill_the_struct_dictionary_with_the_list()
##====================================================
def fill_the_struct_dictionary_with_the_list():
    return
    print('fill the struct dictionary with the list')
    counter=1
    # loop
    for item in testlist:
        print(item)
        aset=[item[0],item[1]]#this creats teh apirs 
        numb=str(counter) #making it a string here . clever
        thisdict=plumtree
        #add_data_to_struct()
        add_data_to_struct(thisdict,numb,aset) ###==============
        print("=======")
        counter += 1

        print("plumtree DICTIONARY now looks like this")    
        print(plumtree)
        print("here we go time to see it work===looping thru plumtree struct=====")
        for x in plumtree.values():
            print(x)
    
        print("===========")    
        for k, v in plumtree.items():
            print(k, v)
#what I am working on his dynmcially loading the 
#from the list to filling the blueberries dictionary
#this returns the index[0][1]
#THIS IS THE METHOD TO FILL A STRUCT RECORD HOLDER FROM A LIST 
#print("I need to empty plumtree dictionary first")
#plumtree.clear()
#print("just emptied plumtree dictionary")
#fill_the_struct_dictionary_with_the_list()




### MORE TESTING HERE ACCESSING THE DICTIOANRY PLUMTREE TO GET THE PAIRS DATA

#print("testing if this will actually work or it's an illusion")
#get_value_in_dict(plumtree,'1')


#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])
#print("====... did it work terrible =")



#get_value_in_dict(plumtree,'2')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'3')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'4')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'5')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'6')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'7')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])


#print('testing getting pair based on number in plumtree')
#apple_pie=plumtree.get('2') #notice it's not a string
#print("it is for '2' this",apple_pie)

#apple_pie=plumtree.get('1') #notice it's not a string
#print("it is for '1' this",apple_pie)

#apple_pie=plumtree.get('2') #notice it's not a string
#print("it is for '2' this",apple_pie)

#apple_pie=plumtree.get('3') #notice it's not a string
#print("it is for '3' this",apple_pie)

#apple_pie=plumtree.get('4') #notice it's not a string
#print("it is for '4' this",apple_pie)

#apple_pie=plumtree.get('5') #notice it's not a string
#print("it is for '5' this",apple_pie)


def testing_pair_list():
    return #not testing this right now
    print("length of theforce=",len(theforce))
    print("together_pair=",together_pair)
    print("======testing pair list() == fireworks time in tahoe ====")
    print("theforce[0]=",together_pair[0]) #first pair coordinates start stop
    print("theforce[1]=",together_pair[1]) # second pair coordinates start stop
    print("===starting loop thru list theforce =======")
    newcounter=0
    print("dog breath test")
    for item in together_pair:
        print(item)
        #this only works for two numbers 2 number long currently
        dog = together_pair[newcounter] #here I access first and second numbers in pairlist
        x = dog.split(",")  # see if this trick works
        print(x[0])
        print("doing surgery cutting off first character")
        charlie=''
        charlie = x[0]
        super=x[1]
        print("super=",super)
        print("=====")
        charlie = charlie[1:]
        print("charlie =",charlie)
       
        super =super[:-1]
        print("super=",super)
        print("===...=.=.=.=.=.=.=.=.=.=.")
        print("===...=.=.=.=.=.=.=.=.=.=.")
        charlie=''
        charlie = x[0]
        charlie = charlie[4:]
        print("charlie =",charlie)
        #print(x[1])
        print("==========")
        newcounter += 1 #python doesn't have ++
        
    print("=== end of looping thru list =======")
    
    
print("MAJOR TEST august 7th, 2021 morgan hill starbucks mocha time")    
print("testing this dam code again...")    

#=======================================================
## this makes the pair list for locations of nested switches august 7th, 2021 
print("DOING TEST of PAIRS of switch and endswitch necessary to do copy and skip comamnds")
print("===================== big test today wednesday =========")
print("what this entails is the mechanics of switch and endswitch locations")
print("which need to be dead on to work correctly for separating the nested strings")
print(" ---- THIS MUST WORK DEAD ON --- for the show of separating teh strings")
print("  --- so this creates the information needed to correctly separate the strings")
print(" === puff the magic dragon time here august 11th ===")
fill_pairlist_with_switch_and_endswitch_pairs(samplestring)
testing_pair_list() #this shows the outpout of grabbing the switch
# and endswitch pairs (sets)



#this way I can use the pair list to copy the nested switches
#========================================================

#print("oh wow does this actually PEAR TREE SHAKE  work pairlist below")
#print("number of pairs =",len(pairlist)) #this is beautiful!!!

#print("oh wow look at this pairlist I made=== starbucks mocha===...")
#print("the length of pairlist =", len(pairlist))
#print('after first attempt')
#sosmart =pairlist[0] #first position
#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])




#print("====== JEDI TEST ========")
#this is constructing filling the data in the dictionary pair values
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#this is building a pair [4, 8]   #an example 

#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)
#theforce.append(jedi)


#print("I simply add the jedi string which is a list (brilliant)
#print("to theforce list sooo nice")
#make a method here 

#fill jedi with one set 
#print("=======NEXt JEDI TEST ======")
#sosmart =pairlist[1] #second position meaning second nested switch 


#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])
#x = 10
#y = 20
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)

# feed jedi set of 2 numbers into the forcelist with an append
#was theforce
#theforce.append(jedi)

#print("theforce=",theforce)
#print("the length of theforce list =",len(theforce))

########################
#print("the =========== force here ========force shows",theforce)
#print("theforce[0]=",theforce[0]) #set one of pair of a switch start and endswitch
#print("theforce[1]=",theforce[1]) # set second pair of a switch and endswitch locations

# so this is building the pears lists of switch endswitch so then I would add the pearslist
#to a dictionary now I think. 

############













#this would just add the switch location


#I can createa  new list to make the pairs first
#go thru grabbing the first number first
#then on the second loop add the second the endswitch

#fill the pears dictionary now
#exit()


#print("switch_location=",switch_location)
#print("endswitch_location=",endswitch_location)

#what is the output???
print("snow man here ")
print("I need to have it flow into the range below lists")
#these are hard coded in here 
print("the output from get swtich and endswitchlocatin for samplestring")
print("right below this line")
print(" RODAN FLYING......")

#for some strange reason the get swithc and endswitch locations are off by 1

#switch_location[0] -=  1
#endswitch_location[0] -=  1
#print("what type is it switch_location[0]",type(switch_location[0]))
#test =switch_location[0] 
#test=test-1
#switch_location[0] = test
#print("switch_location now",switch_location)

#test =endswitch_location[0] 
#test=test-1
#endswitch_location[0] = test
#print("endswitch_location now",endswitch_location)

##============================================================
#these are in switch_location and in endswitch_location


######################################################
list_of_switch_range=[]
list_of_switch_range.append(0)
list_of_switch_range.append(0) #was 10 hard coded 
list_of_switch_range.append(0) #was 20 hard coded

#list_of_switch_range[1] = switch_location
#list_of_switch_range[2] = endswitch_location
##############################################################
## july 17th, 2021 11:12 am
print("IS THIS WORKING OR NOT ==========")
#here we feed the input switch and endswitch into range lists
#THIS WORKS FOR JUST ONE INNER NESTED SWITCH 

anest_string='''
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
'''
print("wild wild west test...")

###########################################============
#experimenting on nov 4th thursday 
get_first_switch_test='''
			switch(exp){ #21         
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
'''

get_first_switch_da='''
			switch(exp){ #  54         
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					switch(exp) # 98
					break
				default:
					print("we are done here")
			endswitch 
'''

# get first line with switch get the number after comment
# append that number to a list
#first_switch_list.append(number)
got_the_number=[]
##====================================================
##  get_switch_number_at_top_of_string(stringname):
##====================================================
def get_switch_number_at_top_of_string(stringname):
	awesome=''
	counter =0  #say it's 3
	#this will only get the number from the FIRST SWITCH it encounters
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		print(line)
		print("the counter here is",counter)
		if "switch" in line and "end" not in line and "#" in line: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number is",y)
			y=y.strip() 
			got_the_number.append(y)
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;


# here I would add the strings in quail after they have been separated
# and they are in the list mytestlist. I then apply a method to each
# string to get teh switch number at the top and append it 
# to the list got_the_number
 # I will need to loop thru the quail list of the seperated switch strings
 # and append the strings within to mytestlist
 #so actually I would loop thru quail list and call get switch number

mytestlist=[]
mytestlist.append(get_first_switch_test)
mytestlist.append(get_first_switch_da)
del got_the_number[:] #clear out this list at the beginning

#loop thru list with thes trings
#feed the strings into method get switch number at top first switch
##=====================================================
## get_first_switch_number_from_all_strings()  fly jets
##=====================================================
def get_first_switch_number_from_all_strings():
    print("get_first_switch_number_from_all_strings()")
    for item in mytestlist: #this will be quail list before parser
        get_switch_number_at_top_of_string(item)


get_first_switch_number_from_all_strings()
print("really got_the_number=",got_the_number)
# this will be my so-called twin list
# that I will use 
# for the python outoput strings in the stanford list
# to use to make the nested_method names for the defs


#exit();

#
'''
 this transfers the line location of switch and endswitch
 to list of switch range 1 and 2 from 
 switch_location and endswitch_location
'''
#28,38 for second string
# I am skipping using this now NOT using this method 
##################################################
##  get_one_nested_switch_start_and_finish()
##################################################
def get_one_nested_switch_start_and_finish():  # this gets the input from switch_location[0]
    print("get_one_nested_switch_start_and_finish()")
# and from  endswitch_location[0]

## this takes in the two lists of list_of_switch_range[1] and list_of_switch_range[2]
    print("=== ||=== get one nested switch start and finish line numbers")
    #force feeding it the second nested switch location input data 
    #these are hard coded for testing 
    #switch_location[0]    = 28  #july 18th testing 2nd nested switch
    #endswitch_location[0] = 38  #july 18th testing 2nd nested switch 
    list_of_switch_range[1] =switch_location[0] #force it in here
    list_of_switch_range[2] =endswitch_location[0]
    #list_of_switch_range[0]=0
    #list_of_switch_range[1]=10
    print(list_of_switch_range[1])
    print(list_of_switch_range[2])
    #list_of_switch_range[2]=20


the_nest_string= fridge[0] 



print("real string test from columbia river")

counter1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
			exp = 3
			switch(exp){ #49
				case 'burger':
					print("do something")
					####################
					switch(exp){ #53
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
			##############
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


#===========
counter2='''
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
'''
#===========
counter3='''
			switch(exp){ #49
				case 'burger':
					print("do something")
					####################
					switch(exp){ #53
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
'''

#===========
counter4='''
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
'''

#===========
counter5='''
					switch(exp){ #53
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
					endswitch #64
'''
#===========
counter6='''
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
'''

testing_string_list=[]
testing_string_list.append(counter1)
testing_string_list.append(counter2)
testing_string_list.append(counter3)
testing_string_list.append(counter4)
testing_string_list.append(counter5)
testing_string_list.append(counter6)
#this is what has the string_with_nested_switches in it
# THIS TAKES TABS OUT OF THE ENTIRE NESTED SWITCH 

teststringgonow='''
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
'''
funky='''
	switch(exp){ #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
	endswitch 
'''

###=================================================================
passthis=[]
passthis.append(0)
##
#this gets the tabdepth in front of top switch word
##==================================================
##  starter_engine(the_nest_string):   nov 30th tested working accurately
##==================================================
def starter_engine(the_nest_string):
	print("======starter engine called======")
	tabdepth='';n=''
	for line in the_nest_string.splitlines(): #nest_string
		if "switch" in line and "end" not in line: #had "not"
			tabdepth = line.count("\t")
			n= tabdepth;n = n-1  #need to have one tab in front
			break
	passthis[0]= n;print("n =",n)
goldtime=[]
goldtime.append(0)
##===================================================================
##  modern_tab_shifter_to_left(the_nest_string):  nov 30th tested working
###==================================================================
def modern_tab_shifter_to_left(the_nest_string):
    print("====modern tab shifter to left=======")
    starter_engine(the_nest_string)  #method call to get tabdepth on first switch line
    buildstring='';n = passthis[0] #filled from starter_engine method number of tabs in front of switch
    ### n is number of tabs in front of switch BEFORE CHANGING IT
    if n == 0: #means one(1) tab in front of switch do nothing
        buildstring =the_nest_string #no changes to indentation
    if n > 1: #more than one tab in front of switch so cut some tabs out
        for line in the_nest_string.splitlines():
            buildstring += line[n:] +'\n' #this cuts out n tabs from the front of this line
    goldtime[0] = buildstring
    print("output of concatted string in goldtime[0]")
    for line in buildstring.splitlines():
        print(line)
  


#modern_tab_shifter_to_left(get_first_switch_da)
print("===== intermission 1=====")
#modern_tab_shifter_to_left(teststringgonow)
print("===== intermission 2=====")


print("testing indenting all 7 strings using modern tab shifter to left()")
for item in testing_string_list:
    modern_tab_shifter_to_left(item)
    print("==== line =====")
print("let them play in the snow")    
#exit()
print("================================")
print("================================")
print("============go baby work ====================")
print("================================")
catching_first_change=[]
print("testing going thru loop and calling one method to start ")
print("TEST MODE NOW...")
for item in testing_string_list:
    print(item)

#=================================== friday nov 19th =============================
# this is where I am applying a method to each item in input switch strings list
###===============================================================================
## THIS IS GOING THRU LIST AND CALLING METHOD modern_tab_shift_to_left(item) to each string
## and then putting modified switch string into list catching_first_change
counter=1  #FILLING CHATCHING_FIRST_CHANGE LIST FROM TESTING_STRING_LIST
for item in testing_string_list: #just filled this above
    #print(item)
    #method shift string to left
    modern_tab_shifter_to_left(item) #now put it into a new list
    #result put into goldtime[0])
    #add modified string to list catching_first_change
    #result of method effects on string goes into goldtime[0]
    #which is then appended to new list
    catching_first_change.append(goldtime[0])
    print("counter =",counter)
    print("=========================")
    
print("the exit sign is GREEN ....")  
print("the output change in list now..")
#print here we empty the original list and then refill it with inbetween list
del testing_string_list[:]   
print("this is filling the list testing_string_list from list catching_first_change")
for item in catching_first_change:
    print(item)
    testing_string_list.append(item)
print("================================")
print("=======strings modified in origional list testing_string_list ============")
##== here we see what's in the list

print("now blue orion looking thru original strings in list after being modified")
for item in testing_string_list:
    print(item)
 
  
#exit()










##########################################
##  take_out_x_tabs_from_front_of_line(n):
##########################################
def take_out_x_tabs_from_front_of_line(the_nest_string):
	starter_engine(the_nest_string);n=passthis[0]
	print("take out ",n," tabs from front of line - of string")
	print("take_out_x_tabs_from_front_of_line(n)") #make this is into a method 
	print("n=",n)
	#get tab count in line with switch and counter =1
	#should be governed by the first line with switch 
	
				
	wildness=''
	print('half way down n =',n)
	for line in the_nest_string.splitlines(): #nest_string
		
		newline = line[1:]
		print(newline)
		
		if n == 4:
			wildness += line.replace("\t\t\t\t","\t") 
		if n == 3:
			wildness += line.replace("\t\t\t","\t") #strips one right
		if n == 2: #this leaves 1 tab in front of each line
			wildness += line.replace("\t\t","\t") #strips one right
		if n == 1: # we only one one tab in front of the switch word as the guidepost
			pass #do nothingwildness += line.replace("\t\t","\t") #strips one right
		wildness += "\n"
	print("after minor surgery see if this works")
	print(wildness)
	fridge[0] = wildness
	return wildness # this worked

#3 take out 2
the_string='''
				switch(exp){ #  54
					case 'blable':
						print("do something")
						print("yep")
						fallthru
					case 'more':
						print("nice")
						switch(exp) # 98
						break
					default:
						print("we are done here")
				endswitch 
'''

#2 take out 1
the_second_string='''
		switch(exp){ #  54
			case 'blable':
				print("do something")
				print("yep")
				fallthru
			case 'more':
				print("nice")
				switch(exp) # 98
				break
			default:
				print("we are done here")
		endswitch 
'''


toocool=the_string.replace("\t","",1)
for line in toocool.splitlines():
    print(line)
trythis=toocool    
print("after first reduction")    
gonow=trythis.replace("\t","",1)
for line in gonow.splitlines():
    print(line)
    
print("did it twice")    
        
print("go away")
take_out_x_tabs_from_front_of_line(the_string)
print("road block here")
take_out_x_tabs_from_front_of_line(the_second_string)
print("hiking up Loma Road")
#exit()

#store in a dictionary each pair of switch and end switch params
# then I loop thru it with the numbers

####============ july 19th 2021  Monday ===================
# I already have the code to build a list of all switches and endswitches
# but I need to put them into a dictionary when I do that search to capture them as pairs

##================================

'''
swtich endswitch location
for trackcing hwer eto grab each nested switch
list with nestd swithc method name with number loop thru it
alist=[]
so = "10,20"
alist.append(so)
thisdict={
"brand":"Ford",
"2":alist[0],
"year":1964
}
#grab content by number
x = thisdict.get("2")
print(x)
# macro between
# put n thru m in a list
# then just this
# if x in list_of_numbers
'''

print("testing dictionary to hold switch endswitch pairs (pear tree)")
print(" ==== testing using a dictionary now ==== mayflower ship===")
alist=[]
alist.append(0)
alist.append(10)
alist.append(20)
alist.append(30)
alist.append(40)

color_table={
    "brand":"mocha",
    "Red": [10,20],
    "3": [30,40]
}

coffee = color_table["Red"][0]
print(coffee)
coffee = color_table["Red"][1]
print(coffee)
#grab content by number
#coffee = thisdict.get("2")
#print(coffee) #it should print 10,20
#print("now another one")
#coffee = thisdict.get("3")
#print(coffee) #it should print 10,20


friend1=[]
friend2=[]

thisdict =	{
  "1": [4,7],
  "2": [10,20],
  "3": [21,30]
}
for x in thisdict.values():
  print(x)
  cool = x
  print(cool[0])
  print(cool[1])
  friend1.append(cool[0])
  friend1.append(cool[1])
  print("good times")
  print(friend1)
  





### successful test for between macro ################### july 19th, 2021 ########## 

print("testing between macro and how it will work")
mylist=[]

mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

testlist =[]
testlist=[1,2,3,4,5,6,7,8,9,10]
#####################
##  between test()
#####################
def between_test(): #between macro 
#it would have to be like this
#if a between(x,y)
    print("BETWEEN TEST HERE ----")
    print("bla bla bla")
    print("between test")
    #x = 7
    print("the final outcome..")
    # if x >= switchline and x <= end switchline  #meaning  from start number thru endnumber
    #if x is between switchnumber and endswitch number
    #the list would contain the start number thru the stop mumber 
    # if x is between startnumber and endnumber:
    counter=0 #the logic is to be between x and y it's inclusive of x and y also
    for item in testlist: #so we look for a narrow range within the large input range
        if item in mylist:
            print("yes",item)
            counter += 1
            
        else:
            print("nope",item)
            counter += 1

print("=====do test of between macro proof of concept=====")
between_test() #this tests if we have a list of numbers 1 to 6

print("testing this with between")
zoo = 4
#if zoo between 1 and 6:
alist=[]
alist=[1,2,3,4,5,6]
print("======= BEtWEEN TESt ========")
print("testing the replacement for using betwen")
print("if zoo(4) is between 1 and 6")
if zoo  in alist:
    print("yes it's between 1 and 6",zoo)
else:
    print("nope",zoo)


###=========================
##   between() macro
##==========================
def between(x,y,z):
    print("between called for if x in list between y and z")
    if x in alist: #1 thru 6
        print("True yes ",x, "between ", y, " and ",z)
    else:
        print("False,",x," is not between ",y," and ",z)



print("doing between macro tests....")
between(4,1,6)
between(10,1,6)
between(0,10,25)


#also next add
##==================
##  after macro
##  before macro
##================

############## testing using  a dictinary to store
############## pears of switch and endswitch pairs

#this will be generated. but I think that
# I might have the dictionary pears already existing.

###====================== dictionary storage area =================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================

#dictionary called pears
peartree = {}  


#given name peartree of dictionary
def get_value_of_key_original(x): #peartree hardcoded in
    car=eval("peartree.get('" + str(x) +"')")
    print(car)
    return car #so if it is a list it should return a list right?z

#given name peartree of dictionary
def get_value_of_key(dict,x):
    car=eval("" + dict +".get('" + str(x) +"')") #maybe
    print(car)
    return car #so if it is a list it should return a list right?z


########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists
####################################################################||
### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  
#####################
## do this baby 

#what I need to do is add to a dictionary dynamically 
#####################
def do_this_baby():
    print("do this baby caled")
    print("===do this baby() adding data to peartree dictionary called ......====")
    print("practicing ADDING data to see if it works (this will be done dynamically later")
    peartree['1'] = [10,20]
    peartree['2'] = [28,38]  #uses small anonymous list for data
    print(peartree)
    x = peartree.get("1")
    print("x=",x)
    
    
def add_data_to_peartree(x,z):
    answer =''
    answer = "peartree['" + str(x) +"'] = z " #[10,20]
    print("just before exec add data to peartree")
    print(answer)
    exec(answer)
    
fool_on_hill= '[10,20]'
print("TESTING adding data to a dictionary")
add_data_to_peartree(1,fool_on_hill)
print("peartree has in its contents=")
print(peartree) 







#testing adding data record to dictionary dynamically.
#Declare a dictionary (empty) 
print("dynamiclaly add data to dictionary = DRIVE THRU ")
print("testing dynanmically adding data to a dictionary Drive Thru")
data = {'a': 1, 'b': 2, 'c': 3}
print(data)
data.update({'d':3,'e':4})  # Updates 'c' and adds 'd'
print("====after adding d and e dictioanry data======")
print(data)

fun={} #dictionary called fun
print("first the fun dictionary is empty")
print(fun)
#input values to dynamically add data for teh switch endswitch to dictionary

print("adding data to drivethru dictionary ")
print(" RED WHITE AND BLUE ")
drivethru={}
#drivethru.update('1': '[10,20]')
#drivethru.update('2': '[30,40]')
#3drivethru.update('3': '[50,60]')
#drivethru.update('4': '[70,80]')
#print(drivethru)

#zerohour=get_value_of_key(3)
#print("zerohour=",zerohour)

cherish=[10,20]
skyblue =[28,38]

def get_dictionary_size(x): #length
    shit= len(x)
    print("size of this dictionary",x," is",shit)
    print("so the result is ",shit)
    return shit;
    


print("This is doing an update here --->")
fun.update({'1':cherish,'2':skyblue})
print("hard coded here printing out the dictionary fun")
print(fun)
print("========")
num1='3'
num2='4'
silver =[42,46]
gold =[50,52]

#put these into a list also
crystal=[]
crystal.append(0)
crystal.append(num1)
crystal.append(num2)

dust=[]
dust.append(0)
dust.append(silver)
dust.append(gold)



#=
##==============================
def dynamically_add_data_to_dictionary(a,x,y):
    print("testing... dynmically add data to dictionary a, x, y")
    print("Tesitng using lists now which are changeable on the fly")
    a.update({crystal[1]:dust[1],crystal[2]:dust[2]}) #totally dynamic attempt here
    print(a)
print('did this work adding to dictionary')
##################################################################
print("here dynamic attempt --boo scoopy doo van does this work----->>")
dynamically_add_data_to_dictionary(fun,gold,silver)
print("3  =[42,46]")
print("4  =[50,52]")

print('after updating fun dictionary dynamically  strawberry fields===')
print(fun)
print(fun.get("1"))
rat=fun.get("1")
print("below should be 10 and 20 for the result")
print(rat[0])
print(rat[1])

print(fun.get("3"))
rat=fun.get("3")
print("below should be 42 and 46 for the result")
print(rat[0])
print(rat[1])

print(fun.get("4"))
rat=fun.get("4")
print("below should be 50 and 52 for the result")
print(rat[0])
print(rat[1])

print("==== end of adding to data to dictionary dynamically ===")
for k,v in fun.items():
    print(k, v)
    print(v[0],v[1])
    print("----------")

#modidfy this get value to use dictoinary name as parameter  
print("here we are testing get_value_of_key(dictname,keynumber)  (fun,3)")  
#note dictionary name as param MUST BE A STRING in quotes 
love=get_value_of_key('fun',3) #dictionary name and key number

print('the value of key  in fun =',love)
print("should return 42, 46")
print(love[0]) #42
print(love[1]) #46

print("testing getting the length of the fun dictionary")
golddust=''
golddust =get_dictionary_size(fun) #so I would call this before adding to it so
print("so now we can get the number for number of items in a dictionary")
print("we have ", golddust," as the length for dictionary fun")
#that I can add just the new data list [3,4] example and not think about key number
# basedon the length I just add 1 to it
print("above this line should be the size of the dictionary fun pumpkins")
######################################################################
print("now to empty dictionary called fun")
fun.clear() #empties dictionary
print(fun)
    
##===============================
## get_size_of_dictionary  (name of dictionary)
##===============================
def get_size_of_dictionary(zoo):  #this is so I know what next record should be
    print("get_size_of_dictionary")
    answer = len(zoo)
    print("get size of dictionary zoo",answer)
    #how do I loop thru a dictionary
    print(":this is printing out peartree ")
    for x in peartree:
        print(x)
    print("====")
    print("")
    print("this loops thru dictionary thisdict")
    for x in thisdict.values():
        print(x)
    print("")   
    print("===loop thru dictionary== this.dict ==")
    for x, y in thisdict.items():
        print(x, y)




car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def playing_with_dictionary_structs():
    print("playing with dictionary access...")
    x = car.get("model")
    print("testing getting car model")
    print(x)

playing_with_dictionary_structs()

   
#but I just thought I can have a running total in a list too
def do_something():
    print("Muppets Animal")
    result=''
    do_this_baby() # I think that the list peartree was empty when I was testing it
    print(peartree)
    print("get size of dictionary ... a test")
    #how do I determine if a list is empty
    if len(peartree) > 0:
        result= len(peartree)
        print("length of peartree =",result)
    else:
        print("peartree is empty and equal to 0")
        print(len(peartree))
    print(result)
    return result
######################################
do_something()

    


print("doing simple test here to get value of key number in peartree dictionary")
print("====Domino's Pizza= dominios pizza dominios pizza=")
firstone=get_value_of_key_original(1) #its using peartree
print('the value of key 1 in peartree =',firstone)
print("does this work or not???")
print(firstone[0])
print(firstone[1])

print("===== pizza hut ===has terrible pizza =")
secondone=get_value_of_key_original(2)
print('the value of key 1 in peartree =',secondone)
print("peartree[2][0] =",secondone[0])
#print(type(secondone[0]))
#print(str(secondone[0]))
#print(type(secondone[0]))
super = secondone[0]
#this force it into becoming a string actually 
#print(eval('secondone[0] == ' + str(super)))
print(super)
print("where is it")
print("type=",type(super))
if secondone[0] == 28: #int actually
    print("this tests :  if secondone[0] == 28:")
    print('too funny no chance in hell====it will never work ')
else:
    print("no way will it work")
    
print("peartree[2][1]=",secondone[1])
foolish = secondone[1]
foolish = str(foolish)
print(type(foolish))
print("now it's a string")
print("end of htis test")
 #peartree['1'] = [10,20]
 #peartree['2'] = [28,38] 
    

#example getting the size of dictionary peartree    
get_size_of_dictionary(peartree)




###############################################
## dnanmically add one record to dictionary
###############################################
def dynamically_add_one_record_to_dictionary():#will need some params
    print("starbucks morgan hill checking this out")
    print("dynamically add one record to dictionary ()") #what about input param
    #first pass go thru dictionary to determine it's current length put that into a list
    super=''
    super=get_size_of_dictionary(peartree)
    #so to add 1 to super for next record
    testtheory='[42,60]' #this is hardcoded here but testing at this stage so it's ok
    #super += 1
    #combine = firsthalf + secondhalf 
    #print(combine)
    #eval(combine)
    #print(combine) 
    #hard coded adding data to dictionary here obviously
    
    peartree['3'] = [42,60] #there would have to be 4 slots already to work
    print(peartree)
    get_size_of_dictionary(peartree)
    print("now yellow BIG BIRD test =========")
    ### look here this is correct below that owrks 
    fish =  "peartree['4'] = [66,80]"
    exec(fish)
    print("experimenting here adding new item to dictionary peartree for testing")
    ##======================================
    thenumber = 5; 
    y1 = 82; 
    y2 = 94
    salmon =  "peartree['" + str(thenumber) + "'] = [" + str(y1) +","+ str(y2) + "]" 
    #this would be blueberries 
    print("salmon=",salmon)
    #salmon= "peartree['5'] = [82,94]"
    #salmon= peartree['5'] = [82,94] #this one is correct
    exec(salmon)
    
    #and I can use 'peartree' as a var and connect it will try that next. 
    #what I built up above needs to look like this string 
    
    ###==========================
    #I need a database for each function that is searchable
    #with a tag of what it does - behavior
    #I could do it in javascript with my switch case
    ###=============================
    
    
    get_size_of_dictionary(peartree)
    print("is peartree 4 here with 66,80")
    print("looping thru dictionary peartree here on oct 23rd")
    for x, y in peartree.items():
        print(x, y)
    #output
    #output='''   
    #    1 [10, 20]
    #    2 [28, 38]
    #3 [42, 60]
    #4 [66, 80]
    #5 [82, 94]
    ##########################
    num = 5
    numb1 = 200
    numb2 = 280
    firsthalf  = "peartree['" + str(num) + "'] ="
    secondhalf = "[" + str(numb1) + "," + str(numb2) + "]"
    print('look here very carefully....')
    print('secondhalf=',secondhalf)
    together = firsthalf + secondhalf
    print("look at below this line does it look right GROUCH")
    print(together)
    exec(together)
    
    
    
    get_size_of_dictionary(peartree)
    #print(peartree['5'])
    print("get value of 5",peartree.get('5'))
    ###########################
    '''
    loop thru peartree:
        print(item)
    '''
    for item in peartree:
        print(item)
        
    for x in peartree.values():
        print(x)
        
    print("chocolate somores. ")
    sweet =get_value_of_key_original(1)
    print("sweet key 1 =",sweet)
    
    get_value_of_key_original(2)
    get_value_of_key_original(3)
    get_value_of_key_original(4)   
    get_value_of_key_original(5)
   

#this will be used to take in a set of two numbers switch endswitch
#to add to the pears dictionary
#### makes [24,34] from ab and returns it
#### make list with two pieces of data (ab)
def make_list_with_two_pieces_of_data(a,b):
    jedi=''
    jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail
    return jedi
    
#making peartree['1'] is not tough

#what about this
#dynamically build it [10,20]
x = 10
y = 20
jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail

print("")
print(" lightning round")
print("testing dynamically creating a two slot list to add to a dictionary")
x = 22
y = 33
raz=make_list_with_two_pieces_of_data(x,y)
#this does this
#  jedi = "[" + str(x) + "," + str(y) + "]," 
print("should return [22,33]")
print(raz)



print("celebration time it almost works completely fireworks")
print('jedi=',jedi) #creates [10,20],

print("interesting test to dynamically add a record to peartree dictionary")
print("KERMIT THE FROG test riding a bicycle")
run=get_size_of_dictionary(peartree)
print("size of dictionary before adding to it ",run)
dynamically_add_one_record_to_dictionary()
run=get_size_of_dictionary(peartree)
print("size of dictionary now is ",run)
#######################################################
do_this_baby()
print("did this work or not")
print("july 20th, 2021 wow time flies")
print(peartree)
###################################################################||

#######################
peartree = {}   #this will always exist and needs to exist to work.
buton=[]   #this is the passing of the buton in track and field relays
buton.append(0) #two positions here in this inner list
buton.append(0)
########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists

### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  


# test input
# this adds a datum to peartree
# this is the method to add a 
# new switch pair to dictionary peartree

#it was add_this <<=========
# now it's this
#####################################
## add_data_to_pears()
#####################################
### the dictionary name is hardcoded as peartree
# peartree is a dictionary
# buton is a list with two slots 

def add_data_to_pears(x,apple):
    print("add_data_to_pears()",x,apple)
    peartree[x]=apple  #this is where the list is added
    print(peartree)

#adding data to dictionary pears here 
 #july 21st 
 #simple var with data is a list anonymous which is what I will construct
apple = [10,20] #<<====== right here I need to produce this from the switch output
x = '1'    
add_data_to_pears(x,apple)  #feeding a new switch pair into peartree

##======
apple = [28,38]
x = '2'  #here I have to provide the number, now I can figure out what 
#it needs to be by getting the length of the dictionary and adding 1 to it.
#for th enext input of data to add to the dictionary. 
add_data_to_pears(x,apple)
##======

print('tahoe test')
print("testing getting a list out of the dictionary in terms of whats in it")
cd=get_value_of_key_original(2) #see if it returns [28,38]
print(cd)

################################################
###### TESTING FILLING A DICTIONARY ############
###############################################@

# I will nede a loop
# july 21st, 2021
#this looks into peartree for a key to return a value
# the values it put into buton[0]and buton[1]
 
# this is accessing the peartree
##############################
##  ACCESS_SWITCH_1_N
##############################
def access_switch_1_n(t):
  print("access_switch_1_n() called")
  print(peartree.get(t)) #was '1'
  one=peartree.get(t)
  print(one[0])
  print(one[1])
  #################
  # added July 21st
  buton[0]= one[0]
  buton[1]= one[1]
  print("this is looking into buton list")
  print("================//================")
  print("buton[0]=",buton[0])
  print("buton[1]=",buton[1])
  print("================//================")
  ##################
  print("I can now grab")
  print("the nest switch params")
  print("from the pear tree")
  print("to feed  copy nest method")
  print("first",one[0],"second",one[1])

#this is accessing the pears dictionary to get the data by the key
### this calls the method above   
t='1' 
access_switch_1_n(t) #accesses key 1


t='2' 
access_switch_1_n(t) #accesses key 2


###############################

# output 
'''
add_this called
{'1': [10, 20]}
add_this called
{'1': [10, 20], '2': [28, 38]}
access switch called
[10, 20]
10
20
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 10 second 20
access switch called
[28, 38]
28
38
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 28 second 38
'''
#<href="https://discover.cs.ucsb.edu/commonerrors/pythonerrors.html"> python common errors UC Santa Barabara</a>

########
b=''
##############################################
## ACCESSING DATA IN PEARTREE DICTIONARY #####
##############################################
def accessing_data_in_peartree_dictionary():
    print("====accessing data in peartree dictionary ==")
    print("====Accessing data  from peartree dictionary()....====")
    print("accessing keys in the peartree  which I would do with a loop later.")
    #print now accessing the dictionary that has been filled with data
    #x = peartree("1")
    print(peartree)
    x =peartree['1']  #adding data to a dictionary
    print(x)
    print(x[0],x[1])
    print("============")
    #x = peartree("2")
    x=peartree['2']  #adding data to a dictionary 
    print(x)
    print(x[0],x[1])
    print("how did it go Hogwarts after flying the car over London")
    
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    
    #this is where I access the dictionary
    # and call the code to get the nested swith
    # based on the switch and endswitch location params
    
    print("==== now trying a LOOP thru peartree =====")
    counter =1  #starting from 1
    for item in peartree: #looks in peartree in this example and splits pair set to display
        x = str(counter)
        b = peartree[x] #this was "1"
        print(b[0],b[1]) #these will always be the same 
        counter += 1
## output is correct
'''
==== now trying a LOOP thru peartree =====
10 20
28 38
'''
#this is for the numbering and access to the nested switches
# and governing them and number the nested_switches and managing it all perfectly.
#================ thursday, august 19th, 2021 solution =============================
#so with this approach number is simple 1 to n for each tab level
#only thing that I change is level depth of indentation
#so if we have main switch and then 3tab depth then 5tab depth
#level0, level1, level2
#level stands for nested switch depth
#so I can use the numbering 1 thru n for each switch
#and use the numbering system and just add the level[0] in a list
#level[0] is main 1, 2, 3, 4, 5 #nested numbering
#level[1] tab depth 5 is first level nested switch if nested within 1, 2, 3
#level[2] tab depth 7 is second level nested with , 1, 2, 3
#level[3] tab depth 9 is third level 
#def loop thru pears dictionary and call  nested switch
#==================================================================

#this calls the method above:        
accessing_data_in_peartree_dictionary()

### this would be after filling this with switch_location and endswitch_location method

print("practicing with this hardcoded input data for switch and endswitch to prove it works")
print("down at pears tree here hard coded ")
# this represents a dictionary called pears already loadded with data
#=================================================
########################
##  PEARS DICTIONARY
########################
#pears =	{  #for pear tree in backyard (2 of them)
#  "1": [10,20], # I can make these now 
#  "2": [28,38],
#  "3": [1,44]
#}

#testing with this new data multiple nested switches

#this hardcoded I put this in here. it's not automated yet
pears =	{  #for pear tree in backyard (2 of them)
  "1": [11,47], # I can make these now 
  "2": [49,73],
  "3": [15,38],
  "4": [53,64],
  "5": [23,33] #no comma after last data piece apparently

}

#for red_robin
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now  1 tab level start and stop
  "2": [11,60], #3 tabs
  "3": [15,51], #5 tabs
  "4": [23,46], #7 tabs # yes it is a stacked at 3 tab level already 
  "5": [31,41], #9 tabs
  "6": [62,86], #3 tabs
  "7": [66,77]  #5 tabs
 #no comma after last data piece apparently
}


#nest_string has pears
#and then blueberries added. 
#solved it.
 
#da = blueberries.get("2")
#print("getting data in blueberries")
#print(da)

'''
11 is in 1
62 is in 1
15 is in 11
23 is in 15
31 is in 23
66 is in 62
'''


def lametest():
    print("doing lametest()")
    if 11 in range(1,86):
        print("true")
    else:
        print("false")
    
lametest()

#new pears

#creates this

#this string already has numbered switches with comments 
#note that the numbering of the switches isn't starting from 1 down.
#testing this sep 30  #switch11 is the main switch
foolish='''
			switch(exp){  #11  first level deep                   Level 1... 3tabs
				case 'blable':
					print("do something") #formula is switch number + 1 thru second number
					#################### cut out 16 thru 38
					switch(exp){ # 15  #second level deep          Level 2    5 tabs=================
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23  #third level deep   Level 3   7 tabs  
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33 === 7 tabs 
							#############
							break
						default:
							print("we are done here")
					endswitch #38   # 5 tabs========================
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
			exp = 3  #note that this switch is stacked below the bottom stack at 3 tabs
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  # 53second level deep          Level 2    
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
'''
#end result will be .......
##=======================
''' main string is 11 thru 73
        pair   tab count
  "1": [11,47],[3] # I can make these now #but it has two starting points SECTIONS
  "2": [49,73],[3]
  
  "3": [15,38],[5] 
  "4": [53,64],[5]
  
  "5": [23,33] [7]
#main 1  to 3 tab depth level 1 ONE
only switches at 3 tabs 
#it should be 
###########
mainswitch number followed by it's nested switches which will be methods
====switch numbers two columns===
first position [0] is first switch id line number for that string
second list can have more than one number represents the switchnest numbers
now figure out how I calculate this and fill it as a listwith sublists
[1] [11,49]
[11][15]
[49][53]
[15][23]
[23][0]
'''
# what this does is add ..  # 66  the line number after each switch(exp){

print("TWIN LIST let's take a look and see what's in it")
#print("let's look inside of twinlist",twinlist)
#they have to be in the same order as the actual switch cases

'''
##================
======1:3==========                   switch1 > switch11 and switch49  =========
switch1
     switch11 method 3 tabs first number from pair 11,47
     switch49 method 3 tabs first number from pair 49.73
end73
#==============================       switch11 > switch15  =======
only switch at 5 tabs between 11 and 47
#minor 3 tab to 5 tabs  Copy 11 thru 47 TWO
switch 11  3 tabs
     switch 15#method  5 tabs   must be between 11 and 47
switchend47
#=============================         switch49 > switch53    ======
#minor 3 tab to 5 tab   THREE
only switch at 5 tabs between 49 and 73
switch 49
     switch 53 method must be between 
endswitch73
##====================  FOUR           switch15  > 23 =======
#minor  5 to 7 tabs   
only swith at 7 tabs between 15 and 38
switch 15
     switch 23 method
##====================  FIVE           switch23  none ======== by itself
#minor none 7 tabs not nested because no 9 tabs its an end tail
switch 23      
$$$$$$$===================================================$$$$$$$$
# I need to be able to generate the pattern
if tab depth == 3 then
first number of pair[0] is nested switch 11 and 49
     switch11 method  first number from pair 11,47
     switch49 method 
     
=======3:5
if tab depth == 5 then
first number of pair[0] 15 goes inside minor 
three tabs to five tabs
switch 11
     switch 15#method   must be between 11 and 47
switchend47
===== 3:5
[49,73],[3]=== [53,64],[5] if secondpair[0] > firstpair[0] and 
switch 49
     switch 53 method must be between 
endswitch73
#testing this
combinedtabs=[]
combined_tabs = threetabs + fivetabs + seventabs
#threetabs= [11, 47, 49, 73] done 
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]
'''
print("testing merry christmas code")
print("obviously this is a thinking and engineering problem")
threetabs = [[1, 2],[3, 4]] 
fivetabs  = [[5, 6],[7, 8]]
seventabs = [[9, 10]]
#testing this
fuel=[threetabs,fivetabs,seventabs]
combinedtabs_jazz=[]
combine=''
fulllist=["threetabs","fivetabs","seventabs","ninetabs","eleventabs","thirteentabs","fifteentabs"]

#def grab_these_tabs(x):
    


upto7 = "threetabs + fivetabs + seventabs"
combined_tabs_jazz = eval(upto7)
print("combined_tabs_jazz=",combined_tabs_jazz)
for item in combined_tabs_jazz:
    print(item)
    

#laketahoe
combined_tabs=[]
##========================================================
threetabs= [[11, 47],[49, 73]] 
fivetabs = [[15, 38],[53, 64]]
seventabs= [[23, 33]]
#this combines the theetabs, fivetabs and seventabs
combined_tabs = threetabs + fivetabs + seventabs

counter=1 #looping thru combined_tabs list
for item in combined_tabs:
    alpha = item[0];beta  = item[1]
    print("pair=",item," "," counter=",counter,", first=",alpha,", second= ",beta)
    print("=========================")
    counter += 1
print("did she work")

for item in combined_tabs:
    print(item)
    
#output
'''
pair= [11, 47]    counter= 1 , first= 11 , second=  47
=========================
pair= [49, 73]    counter= 2 , first= 49 , second=  73
=========================
pair= [15, 38]    counter= 3 , first= 15 , second=  38
=========================
pair= [53, 64]    counter= 4 , first= 53 , second=  64
=========================
pair= [23, 33]    counter= 5 , first= 23 , second=  33
=========================
did she work
'''
    
#this is what is in combined_tabs now
print("showing off combined tabs list")
for item in combined_tabs:
    print(item)
print("===================")    
#see if this works
#=================================================


table=[]
table.append(0)
#============================================================
## check_if_nested_switch_inside_this_switch(astring): 
## returns table[0] = False or True
# coded on dec 6th monday 12:== noon ish

#==========================================================
def check_if_nested_switch_inside_this_switch(astring):
    print("check if nested switch inside this switch")
    counter=0
    table[0] = False
    for line in astring.splitlines():
        tabcount=line.count("\t")
        if tabcount == 3  and "switch" in line and "end" not in line:
            table[0] = True
            print(line) #proof is in the pudding - how good is it
            break
            
            
            
            
            
##### this does absolutely nothing 
# I need to make a method to add main switch to string list
def add_main_switch_params_to_dictionary():
    print("how it will work")
    #methods count end switches
    #Take answer add 1
    #loop thru input switch string get total number of lines
    #"3" : [1,44],  #is the result
    #call method to add it to dictionary


#pears['3'] = [4,7] #example
# 38-15+ 1=24  formula end number - first number = x then x + 1
#first number keep, skip out to 23 lines (length of string of nested switch)

print("====dictionary pears====")
print(pears)
print("==========")
print("====dictionary peartree====")
print(peartree)

print("==== practicing with dictionary called pears ========")
#access the dictionary one key in particular to get the value
#print('pears[3] which is the key number')
#x = pears["3"]
#print("x = ",x) #this should be 4,7
#print("============")
 
 
def say_something(x):
    print("say something test here")
    print('cool[0]=',x[0], "cool[1]=",x[1])
     


print("PRACTICING LOOP THRU THE PEAR DICTIONARY WITH HARD CODED DATA FOR TESTING")
print("============")
print("== PEARS  dictionary now LOOPING THRU IT===")
print("listening to teh Beach Boys to see if it works ----")
#looping thru dictionary called thisdict
'''
for x in pears.values(): #looping thru pears dictionary holding switch and end switch pairs locations
    
    print(x)
    cool = x
    #print(cool[0])
    #print(cool[1])
    print(cool[0],cool[1])
    #say_something(cool)
    copy_one_nested_switch_string(m82)
    print("========================")
       
''' 
#this will be a method but of course
'''
for line in inputstring.splitlines(): #	
		#this will be the second loop======
		# if counter is between start and finish #just after start and less than = to finish
		if counter > start and counter <= finish: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
	print("===output from skipping some lines====")
	print('it created this string')
	print(concatthis)
'''	
	


#######=========================================
#
##==============================================
def do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring):
	print("do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up")
	#this 
	genius[0] = inputstring
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		skipping_some_lines(genius[0],start,finish)
	#it goes thru the string and makes list of switch,endswitches
	
	
	


#testing
spilled_coffee ='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 ==========
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #14
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 ===============
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #26 ==============
			
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====
'''	



skitahoe ='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #14
			print("nicely")
		case 'more1':
			switch(exp) 16
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #23
			print('party time')
			switch(exp) #25
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #32
		case 'more2':
			print('more parties')
			switch(exp) #34
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #41
			print('are we there yet')
			switch(exp) #43
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #50
			print('how many this week')
			switch(exp) #52
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
				print('bye')
			endswitch #59
			print('what the..')
			break
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====
'''	



flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
switch_list=[]
endswitch_list=[]
thenewpairs=[]

##============================
##  buildpairlist()  created nov 21st, sunday to manage doing the main switch 
##============================  and cutting out switches at three tabs for main switch 
def build_pair_list(stringname):
	print("====== build_pair_list called ======")
	counter =0
	#flush lists
	switch_list=[]
	endswitch_list=[] #should reset them both 
	#thenewpairs=[]
	#del endswitch_list[:]
	#this fills up the switch_list line
	#===================================
	# LOOP FILLS UP SWITCH_LIST 
	#===================================
	#loop thru stringname and fill up switch list
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "switch" in line and "end" not in line:
			switch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	counter =0
	#loop thru stringname and fill up endswitch list
	#this fills up the switch_list line
	# =======================================
	# LOOP FILLS ENDSWITCH LIST 
	#========================================
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "endswitch" in line :
			endswitch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	del switch_list[0]     #delete first switch number which is on line 1
	del endswitch_list[-1] #delete last number endswitch which is end of entire string
	print("after deleting first and last switch we have..")
	print("switch_list=",switch_list);print("endswitch_list=",endswitch_list)
	counter=0 #build the pairs and put them into sweet; then append sweet to thenewpairs list
	#===================================================================================
	# LOOP FILLS THENEWPAIRS LIST WITH SWEET WHICH HAS SWITCH,ENDSWITCH LINE NUMBERS
	#===================================================================================
	for item in switch_list:
		sweet=[switch_list[counter],endswitch_list[counter]]
		thenewpairs.append(sweet)
		counter += 1
	print("this is what we want to see at starbucks")
	print("thenewpairs=",thenewpairs)
	#==================================
	# LOOP PRINTS OUT THE NEWPAIRS LIST
	#==================================
	for item in thenewpairs:
		print(item)
		print('stop here for now')
		#exit()
	#REVERSE THE NEWPAIRS LIST BECAUSE IT HAS TO BE DONE BOTTOM UP TO THE STRING 
	thenewpairs.reverse() #they have to be skipped bottom up to work properly
	print("thenewpairs=",thenewpairs)	
	print("resulting list of thenewpairs =",thenewpairs)



pinkpanther=''
##===========================================
##  skipping_some_lines() #this works
##===========================================
def skipping_some_lines(thestring,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	return
	print("METHOD  skipping_some_lines() called==========")
	print("======= skipping_some_lines() ================called",start,finish)
	# if I have a flag that it's been triggered then afterewards 
	# print("this is the input string used stating skipping_some_lines")
	# for the first pass flag_test[0]= False and then it's flipped to True
	#print("flag_test[0]=",flag_test[0]) =============================
	#if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
	smart=thestring;
	baton[0]=thestring #this is new
		#change it to True now
	flag_test[0] = True #this should now be tru e========================
	#else: #meaning TRUE this is run after first run of skipping_some_lines()======
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
	thestring = baton[0]#====================
	#print('what is in baton[0]',baton[0])
	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
	# because the numbering system of the string starts from 1 too.
	### look that we have the counter here set to 1 by default 
	counter=1; concatthis =''; #finish = finish + 1 
	print("start=",start,"finish=",finish) #I took out x = 
	#smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	#print(smart)
	print("=== ah now I get it these are the lines that it MUST SKIP and we want what is before and after this range to create the modified string =")
	print("it sees in start",start)   #this is a number
	print("it sees in finish",finish) #this is a number too
	##=================
	#so I would build pair list of inner switches at 3 tabs and then loop thru them to skip them
	#this is new on sunday november 21st 2021
	#what I want to skip on the fly without range data
	
	#------------------------------------------------
	#from switch at 3 tabs until endswitch at 3 tabs
	#skip the lines inbetween leaving switch word
	##----------------------------------------------
	
	
	##=============== this is a new addition to automate the grabbing of inner switches ====
	# this creates pairs of the switch, endswitch pairs 
	#if start == 1 and finish == 1: #meaning figure out pairs on the fly
	
		
	#exit()
	counter=0
	#for item in thenewpairs:
	#	start  = item[0]; print("start=",start)
	#	finish = item[1]; print("finish=",finish)
	#check thype
	print("checking tyhpe of thestring")
	print(type(thestring))
	print(thestring)  #it shows 0
	print("what is it?")
	print("starting baton[0] has teh initital input string in it")
	for line in thestring.splitlines(): #smart = x
			#this preserves the switch word and skips the rest of nested switch body including endswitch
			# if counter is between start and finish #just after start and less than = to finish
			#just added start +1 and finish + 1
			#tabdepth= line.count("\t")
			#if tabdepth == 3 and "switch" in line and "end" not in line:
			#		start = counter
			# use while loop of course
			#so it's upside down and backwards to create the same meaning.
			# probably need to do a prescan but maybe i can do it without doing prescan
			#get location of switch and endswitch at 3 tabs
			#while "endswitch" not in line:
			#####################==================
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
		##=======================================
	baton[0]=concatthis;
	print("===output from skipping some lines====")
	#print('it created this string')
	#print(concatthis)
	print("how does it look===>>> by lettuce field")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	#this has red_robin hardwired into the code 
	#just commented out line below november 10th, 2021 to see wehat happens 
	#toosmart[0]= red_robin #it did say toosmart[0] = red_robin
	#just commented these out thanksgiving
	#baton[0] = concatthis  #here the concatthis has been put into baton[0]=======
	#pinkpanther=concatthis==============
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= baton[0]  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	print("now the result is here....!!!!@@@@@$$$$$")
	print(never_defeated[0])
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
	#exit()	
	#print(ibm[0])
		#just moved this over one tab	
#exit()
#end skipping_some_lines  ========================================================
print("Levels TEST on wonderful Monday winter wonderland ")
print("this will take out the inner switch between") 
never_defeated=[]
never_defeated.append(0)

#for line in skitahoe.splitlines():
#   print(line)




#it was previously this
def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    return
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    skipping_some_lines(stringname,start,finish)
    #this means that the output string should be placed into never_defeated[0]
    for line in never_defeated[0].splitlines(): #prints it after takening out. 
        print(line)
        

##===========================================================================
##  modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
#this was redesigned and modified on sunday november 21st at 8:30am to 
# work with skipping some lines with no known locations of inner switches at 3 tabs
# and it calls method build_pair_list to find them and reverse them for input for skipping_some_lines
# and I have to subtract 1 from start and finsh
#this one is used to get the main switch and take out switches at 3 tab depth

# and loops thru list feeding start and finish  params and calling skipping_some_lines()
# #  the input for start and finish will be 1 by default but they will be overwritten
# #  by the build pair list on-the-fly.
print('this one is sooo critical')
def modified2_cut_out_inner_switch_body_leaving_switch_word(stringname):
    #it is modified so it can change more than one inner switch into a switch, infinite
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    ###======= this is ingenius=========
    #METHOD BUILD_PAIR_LIST(STRINGNAME) 
    if len(thenewpairs) > 0:
        print("==TRUE thenewpairs >0 it is ===== ",len(thenewpairs))
        del thenewpairs[:] #delete contents of thenewpairs list if it's not empty yet
    #end if
    #if len(never_defeated[0]) > 0:
    never_defeated[0]='' #deletes it
    build_pair_list(stringname)           # goes thru thenewpairs list and
    for item in thenewpairs:              # fills start and finish into skipping_some_lines params
        start  = item[0];
        finish = item[1]; # print("start,finish=",start," ",finish)
        skipping_some_lines(stringname,start-1,finish-1)#so close now 
        #the result of the concatting goes into never_defeated[0]
    #this means that the output string should be placed into never_defeated[0]
    print("let us see what we have jazz blues line 6166 ....")
    #so it's output is in  never_defeated[0]
    thisstring = never_defeated[0]
    return thisstring; #see if this works  it is important that we return the string
    print("let's see what it has in it and if it converts the inner switch bodies to switch word...")
    for line in thisstring.splitlines(): #prints it after takening out. 
        print(line)
    cat_scales[0]= never_defeated[0]
    print("now loop thru pinkpanther")
  
        
#manipulate_string(item) #shifts it to the left

# this is the one that is new as of november 21st and it does the main switch with
# inner switches at 3 tabs that it takes out leaving just the switch word.
#============ original============ modified2
output_list=[]
output_list.append(0)
# testing spilled_coffee string 
stringname=spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print("input string is spilled_coffee  =========")
print("doing first attempt of converting inner switch bodies to just the switch word")
mybaby =''
mybaby = modified2_cut_out_inner_switch_body_leaving_switch_word(stringname)
print("did this sucker work tuesday november 23?")
print("now loop thru the output if it generated it")
print("this is the resulting output processed by the modified2_cut_out... function")
for line in mybaby.splitlines():
    print(line)
    #print("======") 
print("end of first string test for reducing switch bodies to switch word") 
print("=== made it to this point after first attempt completed ===")  
print("now a SECOND ATTEMPT AT CALLING THIS METHOD NOW. WEIRD AT LEAST FIRST PASS WORKS ==")
## testing skitahoe string
#stringname=skitahoe;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print("just testing 2nd one with skitahoe string to see if it works ==input sstring is spilled_coffee")
mybaby =''
#worked by itself
print("doing skithaoe string now=============")
stringname=skitahoe
mybaby = modified2_cut_out_inner_switch_body_leaving_switch_word(stringname)

for line in mybaby.splitlines():
    print(line)
#exit()   
    
print("===end of show on thanksgiving==attempt 2 =")    
#exit()


#exit()

print("catscales=",cat_scales[0])
print("=====rats======")
print("never_defeated[0]",never_defeated[0])

goldring = never_defeated[0]
print("is this going to finally work or not")
output_list.append(goldring)
print("WHAT IS BELOW THIS DAM LINE")
print(output_list[0])
print("now loop thru goldring s")
for line in goldring.splitlines():
    print(line)

print("seeing if this works")
for line in never_defeated[0].splitlines():
    print(line)
    
#ram = never_defeated[0].replace("switch","rocks")
#never_defeated[0]= ram
#for line in never_defeated[0].splitlines():
#    print(line)
#exit()
#==================================
print("end of deifnitely working modifies2 cut out inner switch body.()")


#stringname=skitahoe; start=7; finish = 14; #this sucker was moving....    
#cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
print("let us see what we have.")

#need to indent it I think.
#produces this output it is NOT indented yet 
goldfish='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7
			print("nicely")
			break
		default:
			print("we are done here")
	endswitch 
'''
			
			
			

print(" RED RED RED cut out switch body leave only switch word baby")
print(" red alert testing cut out switch body leaving switch word tesitng 4 ..")    
#exit()

#this is testing with dummy data above in test_code_now
#taking out the inner switch body
print("halloween is coming snoopy and woodstock test")

#print(test_code_now)
#the inner switch is at 9 (which we keep) so we start from +1 meaning 10
#and the endswitch is at 19 but we need to nuke that too so it's endswitch + 1
print("take out 10 thru 20") #but actually keep 10 and takeout including20
#x = test_code_now
#the number system starts from 1 for the switch numbering
#because it starts counting from 0 and not 1 we need to subtract 1 from it
#so it was originally 10, 19

#if switch is #9 and endswitch is 19
#Add 1 to each number start and finish
print("rose test")








#modified so it doesn't matter where the inner switch is 
# they will all be at 3 tabs
#the first switch must be at 1 tab and inner switches need to be at 3 tabs one depth in
#THIS IS NEW CODE WEDNESDAY CODING...november 10th ........
##########################################################################################
#####################################################################################
 #creates first slot in list for string
	#print("actually this builds lists of switch and endswitch locations and makes pairs")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print(" checking to see if more than ONE inner switch at three tabs and ")
	#print("if so then put them into a list")
	#print("the first loop determines how many inner switches at 3 tabs")
	#print("the second loop will go thru a list of the pairs - ah yes but ")
	#print("not implimented yet ")
	
	#print("it sees in finish",finish) #this is a number too
	

# "actually this builds lists of switch and endswitch locations and makes pairs")
# what it does: creates pairs set of start, finish after getting list of switch and endswitch lines
# then it will loop thru pairs set in reverse order and cut out switch bodies bottom up 


## new november 10th 2021 !!:37am
#JUST TRY IT


#this requires this function below to be called first though
#  smart_cut_out_inner_switch_bodies_at_three_tabs(samplestring)
pairset=[]
genius=[]
genius.append(0)

never_defeated=[]
never_defeated.append(0)
list_of_inner_switches_at_three_tabs=[]
list_of_inner_endswitches_at_three_tabs=[]




##========================================================
## loop_thru_pair_set_and_call_skiplines(samplestring)
##=========================================================
def loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring):
	print("len(never_defeated) =",len(never_defeated))
	#never_defeated[0] = thestring #this takes the initial string put into never_defeated[0]
	never_defeated.append(thestring) #maybe this is what I need to do to fix this bug
	print(never_defeated[0]) 
	counter =0
	#loop thru pairset of sets of switch,endswitch (already reversed to go bottom up)
	for item in pairset: #the pairset list was filled in smart_cut_out_inner_switch_bodies_at_three_tabs
		alpha = item[0];beta  = item[1];print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		#METHOD skipping_some_lines()============= uses never_defeated[0] stirng in list
		skipping_some_lines(thestring,start-1,finish-1) #added -1 on Mon Nov 22nd 2021 9:00 AM
		#doing this to see if it cut out the inner switch body 
		print("this is showing the changes reducing switches in never_defeated[0]")
		mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
		print("this is what the switch string looks like after taking out a switch body")
		counter += 1
	








##====================================================================
##  make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring)
##====================================================================
def make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):
	print("METHOD make_Pair_set_of #### called  ... make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):")
	counter =0
	print('let us look at this string to see what it sees')
	print("========//////////==========///////==============")
	for line in inputstring.splitlines():
		print(line)
	print("========//////////==========///////==============")
	for line in inputstring.splitlines(): #smart = x
		#this preserves the switch word and skips the rest of nested switch body including endswitch
		#for this line get tab_depth
		#print("this is where I add the switch line number to list of inner switches at three tabs")
		tab_depth= line.count("\t") #but this presumes just one inner switch there could be more
		#if 3 tabs True AND switch in line and end not in line and counter > 1 
		if tab_depth == 3 and "switch" in line and "end" not in line and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_switches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)		
	#second new loop but looks for endswitch locations at 3 tabs 
	counter =0
	for line in inputstring.splitlines(): #smart = x
		print(line)		
		tab_depth= line.count("\t")
		#print("this is where I add the endswitch line number to list of inner switches at three tabs")
		if tab_depth == 3 and "endswitch" in line  and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_endswitches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("==================")
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)	
	print("list_of_inner_endswitches_at_three_tabs=",list_of_inner_endswitches_at_three_tabs)		
	print("===================")
	print("===== end of phase 1 =====")
	##======================================================================================
	print('doing Friday debugging oh what fun it is to ride in a one horse open sleigh')
	if len(list_of_inner_switches_at_three_tabs) == 1:
		print("this means only ONE dam pair")
	else:
		print("the length is =",len(list_of_inner_switches_at_three_tabs))
		cat = len(list_of_inner_switches_at_three_tabs)
		print("the length of inner switches at three tabs is ",cat)
	###=================================================================	
	print("now I need to make pairs")
	get_number = len(list_of_inner_endswitches_at_three_tabs)
	
	if get_number == 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	##3=======================================================================		
	if get_number > 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	else:
		pass #print("there is only one switch endswitch so do regular mode just one inner switch at 3 tabs ")
	if get_number > 1:
		pairset.reverse()  # REVERSE PAIRSET SO THAT I CAN CHANGE THE INNER SWITCHES BOTTOM UP
	
	print(pairset)
	print("loop thru pairset") #to go thru input string and reduce inner switches to just switch word bottom up
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
	##======================================
	print("method to go thru pairset and call skipping_some_lines(start,finish)")
	do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring)
	#########====================================
		#skipping_some_lines(genius[0],start,finish)
	#it goes thru the string and makes list of switch,endswitches
	
	#skipper needs to cut out from bottom up 
	#skipping_some_lines(x,start,finish):
	#it will call a method

#this must be called after one switch string has had it's inner switches reduced to switch word
#def reset_to_initial_conditions(): #brainchild on NOv 11th, Thursday morning#
#	print(" ====reset_to_initial_conditions()======"#)
#	never_defeated[0] =""
#	list_of_inner_switches_at_three_tabs=[]
#	list_of_inner_endswitches_at_three_tabs=[]
#	pairset=[]
#	baton[0]= "" #should clear it out
    

#def show_output_string_after_changes():
#    mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
#		print("this is what the switch string looks like after taking out a switch body")
#		print('resulting string change is for counter',counter)
#		for line in mouse.splitlines():
#			print(line)    
#this makes pairset list of switch and endswitch 
#this is only run ONCE
fullhouse=[]
##============================================================================
##  take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word
##----------------------------------------------------------------------------
##  Methods: make_pair_set_of_inner_switches_at_three_tabs_depth(thestring) oh wow genius here
##  Methods: loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
##  Methods: skipping_some_lines(x,start,finish)
##  Methods: determine_if_inner_switch_inside_of_this_switch_string(weasel)
##  result of modified string put into  fullhouse.append(never_defeated[0])
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	return
	print("THIS NEEDS TO WORK NOW==")
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("called ....take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)") 
	make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
	print("this is scenario where if one inner switch it's not filling the pairset")
	print("pairset=",pairset)
	loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
	print("list_of_inner_switches_at_three_tabs=", list_of_inner_switches_at_three_tabs)
	print("list_of_inner_endswitches_at_three_tabs=", list_of_inner_endswitches_at_three_tabs)
	print("pairset=",pairset)
	print("this should be the result of the switch with inner switches cut to just switch word, bodies gone")
	for line in never_defeated[0].splitlines():
	    print(line)
	##################################################
	## adding resultof output of methods of taking out inner switches into never_defeated[0]
	## which is put into list fullhouse using append
	### this is where the result of the change string put into never_defeated[0]
	### is appended to list fullhouse
	fullhouse.append(never_defeated[0]) #needs to be here obviously
	#-------------------------------------
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""
	



print("====STARTING ATTEMPT 1====== charlie brown music is the best jazz ====")


take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(spilled_coffee)


#exit() 
print("this is after the first string and taking out inner switch bodies...")
#print("====STARTING ATTEMPT 2====== charlie brown music is the best jazz ====")
#reset_to_initial_conditions()
	##==========================

##=======================
#take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestringzoo1)


#reset_to_initial_conditions() #this must be done after each transformation
print("the final OUTPUT is here ...")
print("length of fullhouse should be 2 is now",len(fullhouse))


#for item in fullhouse:
#    print(item)

####################################################
#print("size of FULLHOUSE is..",len(fullhouse))
#for item in fullhouse:
#    print(item)

print("time to go sledding")
#exit()


print("now I will try to do a few stings with it.") 
print("end of this initial test of ")
result_of_check_if_inner_switch=[]
result_of_check_if_inner_switch.append(0)

#coded on november 19th friday at 10:48 am morgan hill starbucks
##====================================================================
## determine_if_inner_switch_inside_of_this_switch_string(weasel):
##====================================================================
def determine_if_inner_switch_inside_of_this_switch_string(weasel):
    print("determine_if_inner_switch_inside_of_this_switch_string(weasel):")
    ## START INNER LOOP ======= devised on nov 19th friday 10L30 am ===========
    innerswitch= False #this must be set to False before each call below 
    result_of_check_if_inner_switch[0] = False
    for line in weasel.splitlines(): #this looks for an inner switch at 3 tabs depth
        tabdepth = line.count("\t")
        if tabdepth == 3 and "switch" in line:
            print("where's the party THIS string has an inner switch ")
            innerswitch = True
            result_of_check_if_inner_switch[0] = True
            break
        else:
            continue
        print("....")
    print('this has to be called after the loop is done')
    print("result_of_check_if_inner_switch[0]=",result_of_check_if_inner_switch[0])
    #end loop ===================


funtestlist=[]

print("big bird for prez")
print("testing in my mind wed november 10th test ..going thru list and calling take out switch bodies.")
funtestlist=[samplestring,samplestringzoo1] #samplestringzoo1
#use the list I made earlier catching_first_change

# what this does is loop thru the seperated switch strings and 
# applies a method take out nested switch bodies leaving switch word


#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
# method determine_if_inner_switch_inside_of_this_switch_string(stringname)
# method take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
#=====================
def try_the_mocha(): #this has the separated strings in it (that's helpful)
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    print("let us see the SEPARATED strings in this list")
    for item in catching_first_change:
        print(item)
    print("===== okay is this it ===")
    
    print("length of catching first change should be 6",len(catching_first_change))
    counter=0  #this is running the method for second stage of chain_methods
    for item in catching_first_change: #funtestlist: #strings in funtest list
        weasel = item
        ## determines if there is an inner switch in THIS string ==========
        determine_if_inner_switch_inside_of_this_switch_string(weasel)
        innerswitch= result_of_check_if_inner_switch[0]
        print('innerswitch if true or false it is .. =',innerswitch)
        if innerswitch == True:  #if there is an inner switch then apply the method below  
            ######## this method  cuts out all inner switch bodies ######################
            take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
            #fullhouse.append(never_defeated[0]) this line is at bottom of method take_out_nested..
            #never_defeated[0] #this string is the result of the method above in never_defeated[0]
            #############################################################################
        else:
            fullhouse.append(weasel) #so the original string unchanged is added to fullhouse llist
            #this means no innerswitch in this switch string 
            #it's False no inner switch
        counter += 1
        
        ###=========================================================
    print(" end of double loop ")
    print("after going thru catching first change list it should be 6 for counter")
    print("counter =",counter)
    print("len(fullhouse)=",len(fullhouse))
    print("let us look in here if switch stirngs with no inner switches okay and exist at least")
    for item in fullhouse:
        print(item)
    del catching_first_change[:]
    #this fills the output list into catching_first_change list 
    for item in fullhouse:
        catching_first_change.append(item)
        
    print("now big test of second chain method #taking out switch bodies")
    print("this should print out 6 stritngs")
    counter=1
    for item in catching_first_change:
        print("counter=",counter)
        print(item)
        print('=========')
        counter += 1
        
    

print("this is for all of the marbles out of style")
try_the_mocha()    
print('did it work razzle dazzle pumpkins')



#exit()





#modified to get nested switch #so after the first switch in the string 
#so it gets the switch that is nested.
###============================
## get second switch number
##=============================
def get_second_switch_number(stringname): #this might be for when
# I create copies of the switch body strings
	print(" ..get_switch_number.. ")
	awesome=''
	counter =0  #say it's 3
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		if "switch" in line and "end" not in line and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number is",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;
	
	
#input1 = rose[0]
#input2 = rose[1]
#print(input1)
#print(input2)
bigstringtest='''
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
    										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch #tail
							
									break
								default:
									print("we are done here")
							endswitch #46  2
'''

print('output should be it shoud return this string')
'''
							switch(exp){ #23
      								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2
							'''
							
print('october 12th testing doing actually test taking out inner switch')

bigstringtest1='''
	switch(exp){ #1
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #9
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'where now':
					print("nice")
					break
				default:
					print("we very done")
			endswitch #tail
							
			break
		case 'tahoe bound':
				print('fun time now')
				exp ='fishy'
				switch(exp){ #25
					case 'fishy':
						print("do something")
						print("yep")
						fallthru
					case 'where now':
						print("nice")
						break
					default:
					print("we very done")
				endswitch #tail
				print('end of the game time')	
		default:
			print("we are done here")
	endswitch #46  2
'''

start = 10 #rose[0]+1
finish=20 #rose[1]+1
total = finish -start; #gives us 10
x= bigstringtest  #string name to cut out the range from 10 to 20 
skipping_some_lines(x,start,finish)
print(toosmart[0])
print('leaving this November 10th test now for skipping lines in string')
#exit()







peachtree=[]
several_three_tab_switches_list=[]
## get second switch numbers check if many #returns list of inner switch id numbers
##########################################################
## get_second_switch_numbers_check_if_many(stringname):
############################################################
def get_second_switch_numbers_check_if_many(stringname): #this might be for when
	print("get_second_switch_numbers_check_if_many(stringname): Grinch stole christmas")
	print(" ..get_switch_number.. ")
	awesome=''
	counter =0  #say it's 3
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter=0
	targetswitch =0
	for line in stringname.splitlines():
		tablength = line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3:
			targetswitch += 1 
			counter += 1
		else:
			counter += 1
	#end loop
	print("this should return 2")
	print("number of switches at 3 tabs meaning first level =",targetswitch)
	
	#first check if tab length == 3
	counter=0
	smart=False #default setting
	for line in stringname.splitlines():
		tablength=line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3 and counter > 1 and "#" in line:
			x = line.split("#")  
			y = x[1];print(y)
			if ":" in y:
				y=y.replace(":","")
			print(y)
			several_three_tab_switches_list.append(y)
			peachtree.append(several_three_tab_switches_list)
			smart= True
			counter += 1
			continue
		else:
			counter += 1
			continue
		#print if the list is empty put a 0 in it
		print("special case test")
	if smart != True:	
		several_three_tab_switches_list.append(0)
		peachtree.append(several_three_tab_switches_list)
	#end loop
	print("this is key its NOT LOOKING FOR DEEPLY nested but only at 3 tabs >>")
	print("we are here now after filling switch list with inner switches at level 3 tabs")
	#print("several_three_tab_switches_list=",several_three_tab_switches_list)
	#print("this should return a list whith these two numbers in it 11 62")
	#for item in several_three_tab_switches_list:
	#    weasel=get_switch_number(testcode)
	#   


##==========================================================
# the issue is that on the second pass it is using the original string
# and it needs to be using the modified string
# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
# because the numbering system of the string starts from 1 too.
	
# what to work on today thursday, october 14th, 2021 ,,,,,,,,,
# so I would feed in just a param to look for "#" AND "switch" AND "31" and get tabdepth
# I need to try calling and looking for switch in line and # and the number 31
# and loop thru to endswitch at same tab depth.
# get tab depth on switch   tab_depth1 = line.count("\t")
# and then the first line with "endswitch" in line and this_tab_depth == tab_depth1	
##========================================================================
##  def next_metamorphosis_take_out_inner_switch(stringname,switch_number):
##=========================================================================
baton=[]
baton.append(0) #this creates the first slot 0
start=''
finish=''
string_name=''
switch_tab_depth=''
stringname=bigstringtest1
#this gets the endswitch line number that we need
#then I will call skip rope to finish the cutting out of the inner switch case


input_to_get_inner_switch=[]
string_after_cutting_out_inner_switch_body=[]
string_after_cutting_out_inner_switch_body.append(0)

hp=[]
hp.append(0)
lightning=[]
lightning.append(0)
#global concatthis;
	#this just might work 
	#this is a flag to pass the existing concatted string to be used fresh for next switch
	#this list is preset at False 
	#so this starts out false and passes thru it and then the list which used to have
	#FAlse in it has a string in it thereafter and the modified string from first pass
	#and subsequent passes is the new string to modify on the fly
	
#this requires the string name and start and finish to work
#this takes one nested switch with start and finish locations
#this method must be given start and finish in the params
#this prints out the new string after cutting out the nested switch except for the switch word
##===========================================================
## skip_rope_skipping_some_lines()  this cuts out ONE inner switch body
##===========================================================
def skip_rope_skipping_some_lines(string_name,start,finish):#start line nest switch and finish  endswitch
	print("start= ",start,"finish= ",finish)
	if string_after_cutting_out_inner_switch_body[0] == False: #starting
		print("it is False it is  empty ")
	else: 
		string_name = string_after_cutting_out_inner_switch_body[0]
		print('it is NOT False and therefore we fill the string from the list[0]')
	concatthis=''
	print("===skip_rope_skipping_some_lines(string_name,start,finish)====")
	#string_after_cutting_out_inner_switch_body[0]
	print(string_name)
	counter=0; #concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	print("string_name=",string_name,"start=",start,"finish=",finish)
	for line in string_name.splitlines(): 
		if counter > start  and counter <= finish: 
			#print(line) #it won't print the switch word since it's skipping it
			counter += 1; continue
		else: 
			concatthis += line + "\n"; counter += 1; continue
	#print('it created this SILLY STRING === multi colored silly string=')
	#print(concatthis)
	#print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
	weasel=string_after_cutting_out_inner_switch_body[0]
	#for line in weasel.splitlines():
	#	print(line)
	#return weasel  #I need to return from each for the piping to work correctly
	lightning[0] = concatthis
	#for line in lightning[0].splitlines():
	#    print(line)



def modern_take_out_endswitch(inputstring):
	print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			print("detected } in line")
			location = line.index("#")    #gets location from left where position of #
			line = line[:location] 
			print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			print("after left shift it is ",line)
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():




test_string1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru	
		case 4 to 7:
			print('kangaroo hop hop!')#
			#############1
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################5
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default
											print("we very done") 
									endswitch 
							#############k
									break
								default
									print("we are done here")
							endswitch #46  
							#############k
							break
						default
							print("we are done here")
					endswitch #51   
					#############)
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default
					print("we are done here") 
			endswitch #60  
			exp = 32
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default
					print("we are done here") 
			endswitch #86   
			##############)
			print('taught me how to write code')
			fallthru	
			 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru	
		default
			print('the end')
	endswitch #100  
'''
test_string2='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					####################
					switch(exp){ #23
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #31
								case 'fishy':
									print("do something")
									print("yep")
									fallthru
								case 'where now':
									print("nice")
									break
								default:
									print("we very done")
							endswitch 
					#############
							break
						default:
							print("we are done here")
					endswitch #46  2.......
					#############
					break
				default:
					print("we are done here")
			endswitch #51   3 ...
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs 
'''

test_string3='''
	switch(exp){ #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #23
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					####################
					switch(exp){ #31
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'where now':
							print("nice")
							break
						default:
							print("we very done")
					endswitch 
			#############
					break
				default:
					print("we are done here")
			endswitch #46  2.......
			#############
			break
		default:
			print("we are done here")
	endswitch #51   3 ...
'''

test_string4='''
	switch(exp){ #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################1
			switch(exp){ #31
				case 'fishy':
					print("do something")
					print("yep")
					fallthru:
				case 'where now':
					print("nice")
					break
				default:
					print("we very done") 
			endswitch 
			#############k
			break
		default
			print("we are done here")
	endswitch #46  .
'''

test_string5='''
	switch(exp){ #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
	endswitch #41
'''

test_string6='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66
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
			endswitch #77 5 .....
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86
'''

test_string7='''
	switch(exp){ #66
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
	endswitch #77 5 .....
'''
# instead what if I feel a list of switches at 3 tabs and endswitches at 3 tabs
# and make pairs and then use the skip robe which already works and that way 
# I will reuse working code and based on the length of the switch list I just
# look in both lists at the same location position 0 and then 1 etc.
print("big test....starbucks morgan hill ========")

switch_list=[]
endswitch_list=[]
total_switches_at_3tabs_depth=[]

#delete helper lists first
def delete_helper_lists_first():
	del total_switches_at_3tabs_depth[:]
	del switch_list[:]
	del endswitch_list[:]
	
#this gets the important switch and endswitch at 3 tabs length which is critical.
def get_switch_and_endswitch_locations_in_string(string_name):
	print("====||||  get switch and endswitch locations in string  ||||======")
	delete_helper_lists_first()
	#count how many switches at tab depth 3
	####=================
	switchcount=0
	counter = 0
	for line in string_name.splitlines():
	    tabdepth = line.count("\t")
	    if "switch" in line and "end" not in line and tabdepth == 3:
	        switchcount += 1 #doesn't have ++
	        total_switches_at_3tabs_depth.append(counter)
	        counter += 1
	        continue
	    else:
	        counter += 1
	        continue
	####===================
	print("total switch at 3 tabs in this string",len(total_switches_at_3tabs_depth))
	print("they start on these lines",total_switches_at_3tabs_depth)
	#count_switches_at_threetabs= string_name.count("
	counter=0; concatthis =''; #finish = finish + 1 
	print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'switch' in line and "end" not in line and tabdepth == 3: 
			switch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("phase 2 here ====")
	counter=0; concatthis =''; #finish = finish + 1 
	#print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'endswitch' in line and tabdepth == 3: 
			endswitch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	print("end of line...")
	########################======
	
	########################==========
print("calling get switch and endswitch locations (only one set) in string ")
#this needs to be done first ===== before calling the function

print("should be 1 for this test")
#del switch_list[:]
#del endswitch_list[:]
print('real test now i really need this puppy to work')





#del total_switches_at_3tabs_depth[:] #empty it first 
#del switch_list[:]
#del endswitch_list[:]
#print('real test now in string with more than one inner switch at 3 tabs should be 2')
get_switch_and_endswitch_locations_in_string(test_string1)
#mylist=[]
#mylist.append(5)
print("did it even work or not?!")
#exit()

'''
print("======experimenting with test_string1========")
if total_switches_at_3tabs_depth[0] > 1:
    number_to_loop = total_switches_at_3tabs_depth[0]
    print("number to loop=",number_to_loop)
else:
    print("nope only one inner switch at 3 tabs")   
if number_to_loop == 2:
    print("True that number to loop = 2")
    print("1st loop == ")
    x = 0
    start  = switch_list[x]
    finish = endswitch_list[x] 
    print("start=",start)
    print("finish=",finish)
    print("2nd loop === ")
    x=1
    start  = switch_list[x]
    finish = endswitch_list[x] 
    print("start=",start)
    print("finish=",finish)
#end if
'''      
#mylist.append(17)
print("doing test_string6")

print("halloween is nearly here test======..........")
print("switchlist =",switch_list)
print("endswitchlist =",endswitch_list)
print("==============")
#start  = switch_list[0]
#finish = endswitch_list[0]
#currently skip rope method only does one switch to endswitch set so I would use a loop
#and put skip rope in it to do multiple ones


# input 62, look in dictionary to get the 86
# input 11, look in dicitonary get the 60 
print('testing test_string2 ...')
#start = 5
#finish = 41
#this needs to be called first 
print('testing test_string2')
###====-=====================================================
print("this has to be done fifrst need to get switch and endswith lcoations")
print("=======")
#delete_helper_lists_first() #trying this out

print("this needs to be called first get_switch_and_endswitch_locations_in_string()")
get_switch_and_endswitch_locations_in_string(test_string2) #for this switch string

print('we have switch_list=',switch_list)
print("endswitch_list=",endswitch_list)
print('........... what do the lists say above ....')
start  = switch_list[0]  #5
finish = endswitch_list[0]  #41   #below this means that it's empty, False to set flag
string_after_cutting_out_inner_switch_body[0]= False #set this to False first
print("calling skip rope skipping some lines with inputs ",start,"and ",finish)
print("======testing string2======")
skip_rope_skipping_some_lines(test_string2,start,finish)
###=======================================================
#exit()
###======================================================================
print("=======testing test_string6======")
#this is only designed to cut out ONE inner switch 
print("calling skip rope skipping some lines with inputs ",start,"and ",finish)
skip_rope_skipping_some_lines(test_string6,start,finish)

print('now string1 with 2 nested switches=== star trek time====')
print("testing 1..")
#need to find the switches locations and work from the bottom up so do second inner switch first
#that's how the macros work bottom up that way I can use the numbering input correctly. 


### here it has to do the cutting out in reverse since more than one inner switch to cut out
### I learned this trick from my macros solution
#### relooking at this on oct 22nd friday, at 10:46 am 2021
###=========================================================================
#this will be a special method for dealing with reducing down 2 or more inner switches to switch word
print("PUFF THE MAGIC DRAGON === THIS SHOULD ALREADY WORK== ")

# need to make this into a method that has some fuzzy logic
print("TESTING WITH 62 AND 86 SKIPPING ROPE")
#this needs to be put into a method 
#this needs to be set to False to work correctly.
#first we set it to False


#what this does is go thru a list that is in reverse order to cut out thru skipping
# a string to take out inner switches at 3 tab level.  it actually works.
# I need to have a modified one if only one list 

#we will have a loop ::; put this together on Friday, October 22nd, 2021 at 11 am
#string_after_cutting_out_inner_switch_body[0]= False 
#if len(inputlist) == 1:  good if only one list and reverse calls it does nothin
#what this does is loop thru a list of switch endswitch at 3 tabs and does more than one


###========================================================================
## convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
###=========================================================================
def convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
    string_after_cutting_out_inner_switch_body[0]= False        #necessary default flag 
    counter=0 #where am I filling inputlist?
    for item in inputlist: #this grabs the params from item     #list of switches pairs start stop at 3 tabs depth
        start = item[0];
        finish = item[1];
        print('start=',start,'','finish=',finish)                       #62; finish=86 
        skip_rope_skipping_some_lines(stringname,start,finish)  #this copies the string skipping the range designated
        counter +=1
        print("counter=>>",counter)
        print("=====================")
    print("at bottom of converts  with more than one inner switch at 3 tabs")
    print("testing if weasel is returnable at the end of the function")
     #this is after it's done
    #for line in weasel.splitlines():
    #    print(line)
    #return weasel 

	
print("I am fillilng the inputlist right here manually force feeding it.")
#this calls it but right now I want to know where I fill th einputlist
inputlist =[]
inputlist.append([11,60])
inputlist.append([62,86])
print(inputlist)
inputlist.reverse() #reversing the list since the cutting out must be done bottom up to work properly

print("after reversing the list we now have===")
print(inputlist)
print("convert switch with more than one inner switch at 3 tabs(stringname)==== string1")
#get_switch_and_endswitch_locations_in_string(test_string1) #presumes one inner switch 
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("====real deal here ===GET SWITCH AND ENDSWITCH LOCATIONS========")
print("this needs to be called first get_switch_and_endswitch_locations_in_string()")
#get_switch_and_endswitch_locations_in_string(test_string1) #for this switch string
#print('we have switch_list=',switch_list)
#print("endswitch_list=",endswitch_list)
#it needs to make these [[11, 60], [62, 86]]
###testing nov 27th at 10:46am starbucks
print('important testing on Saturday morning')
trialinputlist=[]
inputlist =[]

#made nov 27th, satgurday 4:15pm morgan hill starbucks 
##===========================
## build_trail_inputlist()
##===========================
def build_trial_inputlist(): #this combines switch and endswitch into pair into trialinputlist
	del inputlist[:] #this empties the input list discarding previous data in it
	del trialinputlist[:]
	print("build_trail_inputlist()..")
	counter=0;
	for item in switch_list:
		pair=[switch_list[counter],endswitch_list[counter]]
		trialinputlist.append(pair)
		counter += 1
		
	print("look for the ball on the green")
	print("trialinputlist=",trialinputlist)
	for item in trialinputlist:
		inputlist.append(item)
	print("inputlist=",inputlist)
	for item in inputlist:
		print(item)
	inputlist.reverse() #is this needed here or not 

	
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string1)
print('end of the show sunday morning blues coding')
print("Super silly string 1 PHASE 1 taking out two nested switches at 3 tabs location bottom one first")
print('end of the show sunday morning blues turkey day 2')
print('doing the same string a 2nd time to see if it works')
print("............................................")
print("now trying test_string2")
#del switch_list[:]
#del endswitch_list[:]
print("do you see what I see??")
#inputstring=test_string1
outputstring=[]
outputstring.append(0)
snowboarding=[]
##=================================
## take_out_switch_body(astring):  #def foxnews(astring):
##================================
def take_out_switch_body(astring): #this was foxnews
	nestedswitch= False
	print("take_out_switch_body      today is november 28th sunday  4:29 pm ")
	#right here look if a switch at 3 tabs if not skip below
	####=== new as of monday december 6th, 2021 =========================
	#determine if 
	for line in astring.splitlines():
		tabcount =line.count("\t")
		if "switch" in line and tabcount == 3:
			print("yes switch at 3 tabs in line")
			print("frosty says switch at 3 tabs confirmed")
			nestedswitch= True
			break
	print("frosty the snow man light test for nested switch")
	print("nestedswitch=",nestedswitch)
	print("==================================")
	if nestedswitch == False: #what this does is put the input string into output
		#add input into output  this means no changes were done to the switch string
		print("this switch string DOES NOT have an inner switch")
		lightning[0]=astring 
	else:
	##======= this is down here now ========december 6th 2022 =========
		get_switch_and_endswitch_locations_in_string(astring) #for this switch string
		build_trial_inputlist()	 #this is new 
		convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)
	#end if
	##########================================================================
	print("frosty snowboarding")
	#december 6th looking where I am not adding31 and 66 
	
	print("this is new code now today is Monday november 29th now Dec 6th.")
	print("what is in lightning[0] now")
	#print(lightning[0])
	
	print("resulting final output of take_out_switch_body:") 
	snowboarding.append(lightning[0])  #this is new dec 6th monday
	for line in lightning[0].splitlines():
		print(line)


print("testing this 2nd method")
print("testing take_out_switch_body now") 
print("========TAKE OUT SWITCH BODY()========")
take_out_switch_body(test_string1) #the first one has more than one inner switch it takes out
take_out_switch_body(test_string2)
take_out_switch_body(test_string3)
take_out_switch_body(test_string4)
take_out_switch_body(test_string5)
take_out_switch_body(test_string6)
take_out_switch_body(test_string7)

#gotta take out } in switches 
print("big test if it works right or not")
print("printing out snowboarding list") 
#this should print out just the final product
print("SNOWBOARDING LIST OUTPUT")
counter=1
for item in snowboarding:
    print("counter=",counter)
    print(item)
    print("========")
    counter +=1
    
    

#exit()
   
#def finally_reduce_inner_switches_at_three_tabs_into_switch_word(inputstring):
print("where is the christmas tree test===== doing test_string  1 ===========")
get_switch_and_endswitch_locations_in_string(test_string1) #for this switch string
build_trial_inputlist()	 #this is new 
print("right here what is in inputlist=",inputlist) #needs to be reversed
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string1)
print("end of christmas tree test test string 1 with 2 nested switches at 3 tabs")
#exit()

print("where is the christmas tree test===== doing test_string   2 ===========")
get_switch_and_endswitch_locations_in_string(test_string2) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string2)
print("anotehr one 3")
print("where is the christmas tree test===== doing test_string  3 ===========")
get_switch_and_endswitch_locations_in_string(test_string3) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string3)


print("where is the christmas tree test===== doing test_string  4 ===========")
get_switch_and_endswitch_locations_in_string(test_string4) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string4)


print("testing another one now===== doing test_string  6 ==========")
get_switch_and_endswitch_locations_in_string(test_string6) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string6)

#exit()

# method chaining
# getone.getteo.getthree()

#=======
#Bottom of chain methods result if methods goes into
#output[0]

#Where is transform_string() called

#https://www.google.com/amp/s/nypost.com/2021/11/11/ufos-buzzing-us-warships-may-be-aliens-top-spy-chief/amp/

#Good stuff

#https://m.youtube.com/watch?v=azZ4XAZuVk4




print(inputlist)
#inputlist.reverse() #reversing the list since the cutting out must be done bottom up to work properly

print("after reversing the list we now have===")
#print(inputlist)
#get_switch_and_endswitch_locations_in_string(test_string2)
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string2)
print('pizza for dinner maybe')
#exit()

#inputlist =[]
#inputlist.append([10,36])


#get_switch_and_endswitch_locations_in_string(test_string3)
print('end of the show sunday morning blues turkey day 3')
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string3)

#rint('end of the show sunday morning blues turkey day 4')
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string4)
inputlist =[]
inputlist.append([5,16])
print('end of the show sunday morning blues turkey day 6')
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string6)
print("wow wow")


#string_after_cutting_out_inner_switch_body[0]= False  #just filler but a flag meaning empty

#exit()
#print("testing input 62, 86 skipping rope")
#start=62; finish=86  #[62,86] #input values fed into it 
#skip_rope_skipping_some_lines(test_string1,start,finish)#62,86

#start=11; finish=60  #[11,60]
#skip_rope_skipping_some_lines(test_string1,start,finish)#11,60

print(" super silly string 2 PHASE 2 taking out 2nd nested switch (the higher first one done second) at 3 tabs")
print("TESTING WITH 11 AND 60 SKIPPING ROPE")
print("testing 11,60 inputs for skip rope skipping some lines ")
print("testing 2...") 







print("after doing this which needs to be made into a function with a loop")
print("it will need input of [[11,60],[62,86]] that I reverse if more than one in it")
#listname.reverse()
#so I can use teh same string to do both cuts out of inner switches 
#first     62,86
#second is 11,60

#exit()
#skip_rope_skipping_some_lines(string_name,start,finish)
#critical_list= [[11, 62], [15], [23], [31], [0], [66], [0]]
#end of show

# tuesday, october 19th, 2021  time 9:52 morgan hill starbucks
#==================================
# cut_out_switch_body_no_params   october 19th tuesday
#==================================
#abandoned this appraoch 
# objective is to go through string and take out switch bodies without inputs
'''
def cut_out_switch_body_no_params(string_name):
	print("cut out switch body no params===")
	counter=1; concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	#start  = input_to_get_inner_switch[0]
	#finish = input_to_get_inner_switch[1]
	
	#what about a quick search for locations of switch and endswitch
	for line in string_name.splitlines(): 
		if "switch" not in line and "endswitch"  not in line and tabdepth != 3:
			print(line)
		#notice start +1 based on line number 
		tabdepth = line.count("\t")
		if "switch" in line and "end" not in line and tabdepth == 3:
		#actaully I don't want 
			concatthis += line + "\n"; counter += 1; continue
			print(line) #it won't print the switch word since it's skipping it
			
		 else: 
			 counter += 1; continue
		if "endswitch" in line and tabdepth == 3:
			print(line)#get current line then break
			concatthis += line + "\n"; counter += 1; continue
			#break
	print("===output from skipping some lines====")
	print('it created this SILLY STRING === multi colored silly string=')
	print(concatthis)
	for line in concatthis.splitlines():
		print(line)
	print("=======")
	print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
##========== new version 
	print("here we have the halloween special START SKIPPING ROPE...")
	print("the output string looks like this")
	weasel=string_after_cutting_out_inner_switch_body[0]
	for line in weasel.splitlines():
	    print(line)
'''	
	
	
print("testing cutting out the inner switch bodies to see if it works")	
#cut_out_switch_body_no_params(test_string6)
### this is now working correctly taking into account
# that lines start from 0 not 1 and I need to skip and include the switch word


#next go thru list of stirngs and take out inner switches bodies


#Never theorize before you have data.Invariably you end up twisting facts to suit theories instead of theories to suit facts. -Sherlock holmes.
#There is nothing more deceptive than an obvious fact


##================================= testing at starbucks gilroy christmas tree
#####transform_string() #12379






##========================================================================
##  def next_metamorphosis_take_out_inner_switch(stringname,switch_number):
##=========================================================================
def next_metamorphosis_take_out_inner_switch(string_name,switch_number):
	print("==next_metamorphosis_take_out_inner_switch)====")
	print("==next_metamorphosis_take_out_inner_switch)====")
	switch_tab_depth=''
	counter=1 #look we are starting to count from 1
	startcount =0
	endswitchline=0
	end_switch_tab_depth=''
	#get inner switch location all we know is the switch line number 31 in this case 
	#get switch_tab_depth
	print("the switch_number=",str(switch_number))
	for line in stringname.splitlines():   #switchnumber 31
		if "switch" in line and  "end" not in line and "#" in line and str(switch_number) in line:
			print("31 in line and switch in line and end not in line and # in line ALL TRUE")
			switch_tab_depth = line.count("\t") #gets tab depth
			startcount= counter
			end_switch_tab_depth=switch_tab_depth #see if this works now
			break
		else:
			counter += 1
			continue
	#get endswitch location
	print("startcount =",startcount) #targer switch line number 
	print("target switch_tab_depth =",switch_tab_depth)
	print("END OF PHASE 1 ...")
	
	#get endswitch tab depth
	print("============================")
	counter = 1 #get endswitch tab depth
	for line in string_name.splitlines():
		this_line_tabs= line.count("\t")
		if "endswitch" in line and counter > startcount:
			this_tab_depth = line.count("\t")
			if counter > startcount and this_tab_depth == switch_tab_depth: #this means endswitch must be AFTER switch
				endswitchline = counter
				#the tab depth MUST be the same as the target switch tab depth 
				break
			else:
				counter +=1
		else:
			counter += 1
			continue
			
	print("end_switch_tab_depth=",end_switch_tab_depth)
	print("the end switch line=",endswitchline)
	print("=============================")
	print("END of PHASE 2...")
	counter =1
	for line in string_name.splitlines():
		if "endswitch" in line and counter == endswitchline:
				endcount = counter
				break		
		else:
			counter += 1
	
	startcount = startcount-1 #because we skip switch and keep it. 	
	print("output of next_metamorphosis()")
	print("startcount=",startcount) #oh this is brilliant
	start = startcount
	print("the endswitch line =",endswitchline)
	finish = endswitchline
	print('start=',start)
	print('finish=',finish)
	input_to_get_inner_switch.append(start)  #[0]
	input_to_get_inner_switch.append(finish) #[1]
	print("start=",input_to_get_inner_switch[0])
	print("finish=",input_to_get_inner_switch[1])
	print("switch_tab_depth=",switch_tab_depth)
	#now I can run the skip lines code that requires the start and finish range numbers
	print(" END of PHASE 3 ...")
	print("again this doesn't modify the switch string it just gets input data")
	print("for the next phase which is skipping rope")
	
#notice start +1 based on line number 
#		#because numbers are off by 1 since starting at 0 not 1 in counting
#		#if counter > start +1 and counter <= finish: 
#		if "endswitch" not in line and this_tab_depth == switch_tab_depth: 
#			print(line) #it won't print the switch word since it's skipping it
#			counter += 1; continue
#		else: 
#			concatthis += line + "\n"; counter += 1; continue
#	print("===output from skipping some lines====")
#	print('it created this SILLY STRING ====')
#	print(concatthis)
	
#for the first pass flag_test[0]= False and then it's flipped to True
	#print("flag_test[0]=",flag_test[0])
	#if flag_test[0] == False or flag_test[0] == None: #meaning first pass  and what it's set to by DEFAULT
	#    smart=x;
	#    #change it to True now
	#    flag_test[0] = True #this should now be tru e
	#else: #meaning TRUE this is run after first run of skipping_some_lines()
	#    x = baton[0]
	### look that we have the counter here set to 1 by default 
	



#===========================
print("HERE WE START METAMORPHOSIS ENTERING THE MATRIX...")
#this one has to be called first since it creates the start and finish lines for this string
#based on what the switch number is in the comment which it will look for
#and the inner switch line numbers will be known beforehand
#because they are automatically added 

#def take_out_inner_switch_bodies(thestring):
#first I need to get the nested switch number (assuming one at this point)
## I need to make this into a method witht he two functions below
#working on this october 14th, 2021 gilroy 6:55pm

#I need to get the inner commented switch number 
###=====================================================
print("three, two,one, blast off===>>>")
string_name= bigstringtest # <=== string is in here 
#I need to put the method here that gets the switch comment number
#switch_number=31 #I need to get this number automatically
#this will be different if there are more than one inner switch at 3 tabs length
#I still need to clean up the copied switches so the first switch is at 1 tab
#and the next next level switches start at 3 tabs
#for this first attempt we will limit the inner switches to just one
axis=get_second_switch_number(bigstringtest) #returns 31
#should be 31 
print("axis should be 31",axis)
switch_number = axis #finally getting closer to victory
####===============================
#I have code that get the inner switch number if only one
#and I have code that can find all inner switches at 3 tab level depth 
#what this does is rip out the nested switch body leaving the switch
# word in the nest_list after separating the switch bodies
#this is an important step and I just figured out how to
# detect if more than one inner switch at the three tab level depth
## make this into a method now

# I also got the code to get the second switch in a string line number  in the comment
#which will invariably be different from the true line number, but that's okay.
#=================================================
#=================================================
#=================================================
#=================================================
##========== halloween darkness  oct 14th ===================


print("cinderella")

get_second_switch_numbers_check_if_many(foolish)
print("the result of the  if_many method is to put the inner switches numbers at 3 tabs")
print("into the list which is below")
print("several_three_tab_switches_list=",several_three_tab_switches_list)
print("")
print(" back to the future should be above for stirng foolish")

print("testing bigstringtest1")
print("let us see if this works...")
print("the dark knight is here")
del several_three_tab_switches_list[:]
print('here we go')
get_second_switch_numbers_check_if_many(bigstringtest1) #using bigstringtest1 now
start=''
finish =''

print('end of this test of get second swithc numbers check if many')
print('waiting to get it working')


#I need to go thru each string and count the switches at 3 tabs
#do the loop jazz too.
##=========================================================
##  count_inner_switches_at_first_level(inputstring)
##=========================================================
def count_inner_switches_at_first_level(inputstring):
	print("=====count inner switches at first level=== so at 3 tabs ==")
	counter =0
	innerswitch = 0
	for line in inputstring.splitlines():
		tabdepth = line.count("\t") #added and "end" not in line to eliminate endswitch bug
		if "switch" in line and "end" not in line and tabdepth == 3:
			print("the line number is ",counter)
			linewithswitch =counter
			innerswitch += 1
			counter += 1
		else:
			counter += 1
			
	print("innerswitch count at 3 tabs in this string=",innerswitch)
	print("the line number of the sole inner switch is",linewithswitch)
	return innerswitch;

inputstring = bigstringtest1
#this counts inner switches at 3 tabs indentation in a switch string
total=count_inner_switches_at_first_level(inputstring) #calls the method above


print(" we are done here, of the number of inner switches at 3 tabs = ",total)
#where do I get the inner switch number??
print("=========.........")
print("=========....halloween pumpkins are coming.....")
print("=========.........")
 #this calculates the start and finish of one nested switch 
string_name=bigstringtest1 #I need to find the get switch number for inner switch
switch_number=several_three_tab_switches_list[0] #this presumes only one inner switch
switch_number = int(switch_number) #right here a miracle occurs==== 
print(type(switch_number)) #this gets the start and finish numbers for inner switch to cut out
next_metamorphosis_take_out_inner_switch(string_name,switch_number)
print("it should be 9 and 20 and it shows...")
#all this does is create the start and finish line numbers of one inner switch
print(input_to_get_inner_switch[0])  
print(input_to_get_inner_switch[1])
print("string_name=",string_name,"start=",start,"finish=",finish)

print("go for the gold medal===================")
string_name= bigstringtest1
#I am feedingit 9 and 20 to start with here 
#here the inner start and finish of an inner switch is inserted
start =input_to_get_inner_switch[0]#9  #=input_to_get_inner_switch[0]  #9 #1 after switch line number so it really does 10 compensating 
finish=input_to_get_inner_switch[1]#)20 # =input_to_get_inner_switch[1] #=20
print("SKIPPING ROPE NOW to modify the string and cut out inner switch")
skip_rope_skipping_some_lines(string_name,start,finish)
#skip rope takes out the inners switch leaving the inner switch word.
print("The GREEN EXIT SIGN NOW")
#exit()
#=================================================
#=================================================
#=================================================
#=================================================
#=================================================
#=================================================

#skip_rope_skipping_some_lines(string_name,start,finish)
#it needs to return values to start and finish as input for 
#skip_rope_skipping_some_lines(string_name,start,finish)

#now I need to count switches in a string
#and as a backup safety count endswitches also.


#I can work on these separately actually 
################
teststring1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  
							#############
							break
						default:
							print("we are done here")
					endswitch #51   
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   
			exp = 3
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86   
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
	endswitch #100  
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [11, 60]
#counter= 2
teststring2='''
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   4..........endwitch 4  line 60 3 tabs 
'''
#==========-----------seperated nest strings -----------------
#getting data in blueberries [15, 51]
#counter= 3  THIS IS 5 TABS IN FIRST LINE 
teststring3='''
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
'''


#==========-----------seperated nest strings -----------------
#getting data in blueberries [23, 46]
#counter= 4 this one works 
#I have to reduce these downto first tab and then three tabs
teststring4='''
	switch(exp){ #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################
			switch(exp){ #31
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'where now':
					print("nice")
					break
				default:
					print("we very done")
			endswitch 
			#############
			break
		default:
			print("we are done here")
	endswitch #46  2.......
'''
#==========-----------seperated nest strings -----------------
#getting data in blueberries [31, 41]
#counter= 5
teststring5='''
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [62, 86]
#counter= 6
teststring6='''
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [66, 77]
#counter= 7   THIS IS 5 tabs in first switch line 
teststring7='''
					switch(exp){ #66
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
					endswitch #77 5 .....
'''

#==========-----------seperated nest strings -----------------
print("moving tabs out.")
print("testing moving extra tabs out of a string")
print("this is looping thru teststring3 ")
print("Grand Canyon test Friday")
print("I will take out 5 tabs from the front of each line")
for line in teststring3.splitlines():
    print(line)
print("end of test of printing out teststring3")
print(" ")
counter =0
switch_actual_tabs=[]
switch_actual_tabs.append(0)
import re
onetab="\t"  # here is onetab declared with one tab inside of it
fishbowl=[]
fishbowl.append(0)




#sunday confirmation number sundayoct 17th, 2021
holdon=[]
holdon.append(0)
holdthis=[]
holdthis.append(0)
galaxy=''
#this swaps endswitch with }
#what this does is replace endswitch with '}
###===================================
##  take_out_endswitch(stringname)
###===================================
def take_out_endswitch(stringname):
	print("take_out_endswitch()  called=====")
	answer=''
	galaxy = stringname
	print(galaxy)  #using replace endswitch with }
	#this replaces all endswitch(es) to }
	holdthis[0] = galaxy.replace("endswitch","}") #added here
	#bug what if there is already a curly brace but no endswitch
	print(holdthis[0])
	#move it to left
	answer = holdthis[0]
	newstring=''
	for line in holdthis[0].splitlines():
		if "}" in line and "\t" in line:
			line = line.lstrip()
			newstring += line
		else:
			newstring += line + "\n"
			
	holdthis[0] = newstring
	
	print(holdthis[0])
	for line in holdthis[0].splitlines():
		print(line)
		
	#return answer;
	
	#galaxy = holdthis[0]
	#holdon[0] =holdthis[0]
	#return galaxy
	
	
	
	
	

##==========================================
## shift_nest_string_to_left(stringname)   made on oct 15th, 2021 8:57 am
##==========================================
def shift_nest_string_to_left(stringname):   #cuts out tabs and adds new tabs automatically
    print("========= shift_nest_string_to_left(stringname ===... =====")
    for line in stringname.splitlines():
        print(line)
    #print("this is th einput string====")
    newline=''
    counter=0
    thismatters=''
    print("shift_nest_string_to_left() called")
    for line in stringname.splitlines():
        tabslength = line.count("\t") #this is set up for string3 initially. 
        print("tabslength=",tabslength)
        #counter +=1
        if counter == 1 and "switch" in line: #just added this oct 15th 
            #print(line)
            #print("we care about THIS ONE",tabslength)
            switch_actual_tabs[0] = tabslength
            #print("switch_actual_tabs[0]===",switch_actual_tabs[0])
        else:
            print("he well")
        print("=================>>>=======")
        #For teststring3  if 5 tabs in first line then tabslength-4  because it has 5
        ##==================================================================
        clever=0 #starting give it default value of 0 
        #this one works
        if switch_actual_tabs[0] == int(5): #5-4
            clever = 4
            #print("let's see if clever is an int here")
            #print(type(clever))  
            
        #for some reason this if below is not working right    
        if switch_actual_tabs[0] == int(3): #3 - 2 #reducing to 1 tab on first line
            clever = 1
            #print("let's see if clever is an int here")
            #print(type(clever))  
        #so if 5 -4 giving us 1
        #if 6 -5
        #if 7 -6 giving us 1
        #if 4 -3
        #if 3-2
        #if 1 do nothing
        #this is based on it having 5 tabs in line one and minus 4 tabs
        #if tabslength == 3:
        #    tabslength = 1; #which is -2
            
        #if tabslength == 5:
        #    tabslength = 1 #which is -4
        #I think what I need to do is determine indentation before first switch to gauge it    
        print(" switch_actual_tabs[0]=", switch_actual_tabs[0])
        #total_tabs_to_add=''
        ##########################################
        #if 5 tabs then -4
        #if 3 tabs then -2
        total_tabs_to_add=''   #this was 4 changed it to celver
        print("at this point what is the value of clever",clever)
        total_tabs_to_add =int(tabslength) - int(clever) # reducing it to 1 taking 4 tabs off  #right here 
        print("====")
        print("at this point what is the value of total tabs to add",total_tabs_to_add)
        #print("position 1 type test")
        #print(type(total_tabs_to_add))
       
        #this is what I took out above and replace with below 
        #total_tabs_to_add = ''
       # print("testing boolean condition here ....")
        print("tablength in first switch line =",tabslength)
        #====== if tablength = 5 -==========================
        if tabslength == 5:
            #print("TRUE HERE flying horse to locate this ")
            total_tabs_to_add = tabslength - 4 #TO GET 1
            print("total tabs to add right here =",total_tabs_to_add)
        #end if
        print("====")
        #number one rule code does exactly what you tell it to do. 
        #====== if tablength = 3 -==========================
        if tabslength == 3:
            #print("TRUE HERE flying horse to locate this ")
            total_tabs_to_add = tabslength - 2 #TO GET 1
            print("total tabs to add right here =",total_tabs_to_add)
            
        #print("position 2 type test")
        #print(type(total_tabs_to_add))
        
        #if tabslength == 3:
        #    total_tabs_to_add = tabslength - 2 
        #end if
        #print("=====")
        #print("position 3 type test")
        #print(type(total_tabs_to_add))
       
        #print("so this line will have this many tabs in front",total_tabs_to_add)
        total_tabs_to_add = total_tabs_to_add * onetab #times 1 tab #0 x 1 = 0
        print("RESULT= total_tabs_to_add to each line",total_tabs_to_add)
        myString = line
        output   = re.sub(r"[\t]*", "", myString)    #takes all tabs out of this line
        newline += total_tabs_to_add + output + "\n" #this puts the tabs in front of the stripped string line
        counter +=1
        continue
    #print('the result is..')
    print("this prints out the output what the changed indentation shift to left looks like")
    #return newline
    fishbowl[0] = newline  #the output of shifting to left 
    for line in newline.splitlines():
        print(line)
#print("drink coca-cola test")
#print("TESTING 3")    
#print("starbucks breakfast of friday testing..")
#print("testing indenting correclty teststring3")
#shift nest string to left
shift_nest_string_to_left(teststring3) #good 5 TABS DOWN TO 1
print("red alert test 3 shift nest stirng to left side ... test 3 ")
print("look carefully at this and make sure that it's right with just one tab at top")
print("testing with string skitahoe")
shift_nest_string_to_left(skitahoe) 
print('first we will do this simple test with no tabs see if it returns 0')
practicestring='''
switch(exp){
    case 1:
        print('hello')
'''
tabsinthisline =''
for line in practicestring.splitlines():
    if "switch" in line:
        tabsinthisline = line.count("\t")
        print("tabsinthisline=",tabsinthisline)
        break
        
print("TESTING string 7 now indenting it to the left")
shift_nest_string_to_left(teststring7) #good 5 TABS DOWN TO 1
print("red alert testing shift string to left")




	
	
	
#exit()

#exit()
print("end of testing of doing indentation shifting to string")
print("oct 26th nearly done with this.. line 6127 ")
#exit()

print("this is where I am indenting the switch strings already in a list")
print("I need to indent them to work on them further to prepare them for the parser")

gold_list_results=[]
newstring=[]
newstring.append(0)
##=================================
##  manipulate_string(addstring) #this appends the changed switch strings to gold_list_results
##=================================
print('testing taking out 2 ')
def manipulate_string(addstring):
    print("======manipulate_string() called line 8524=======")
     #the objective is to reduce tabs so only 1 tab in front of first switch in string
    cutout=''
    print("let us ORIGINLAL INPUT STRING HERE look at the starting input string before modifying it")
    for line in addstring.splitlines():
        print(line)

    print("== red white and blue ==============")
    print("=======pinpointing bug on november 30th =============================")
    print("getting tab count in front of first switch here")
    for line in addstring.splitlines():
        if "switch" in line and "end" not in line:
        #this determines the number of TABS in this line
            tabsinthisline = line.count("\t")
            print("tabsinthislines=",tabsinthisline)
            print("the tabs in front of first switch are",tabsinthisline)
            #the objective is to have only 1 tab in front of first switch
            # which then propogates down the length of the entire string
            if int(tabsinthisline) > 1:    #example
                cutout = tabsinthisline -1
                print("tabsinthisline =",tabsinthisline);
                print("cutout =",cutout)
                break
            if tabsinthisline == 1: #which means do nothing we want just 1 tab first
                cutout = -1; #this is using -1 as a flag
                break
            if tabsinthisline == 0:
                break
            # do nothing   193241613
     #take out just 2 tabs
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    super=''
    lastchar=''
    for line in addstring.splitlines():
        #if "switch" in line and "end" not in line:
        tabsinthisline = line.count("\t")
        #it does all lines of the string taking out the first 2 tabs which are chars
        if cutout != 0  or cutout > 0:#this handles if cutout = 0 meaning None
            sliced = line[cutout:] #this can be a variable
            print("sliced sees",sliced)
            #phase A ============================
            
            print("================================")
            print("======phase A sliced=",sliced)
            ### bug fix ##===========================
            #reput in on dec 5th sunday 
            print('this fixes the bug that was putting junk after each line')
            print('adding extra : ) u #')
            print('see if it works ... again')
            ###############################
            ###### testing bug fix dec 5th sunday ######################
            #this tests if last character is #,),u,:
            #print("the last char is sliced[-1]",sliced[-1])
            #tail = sliced[-1]
            #looklist=[]
            #looklist=["#",")","u",":"]
            #if tail in looklist: 
            #   print("yes last char is either #,),u,:")
            #   sliced=sliced[:-1]
            #else:
            #  print("none of the garbage characters are the last char")
            #   pass
            ################################
            ################################    
            ##========================================
            
            
            #if len(sliced) >0:
            #    lastchar=sliced[-1]
            #    #print("lastchar =",lastchar)
            #   # print("TRUE weird last character",lastchar)
            #    if lastchar == ":" or  ")" or  "u" or   "#":
            #        sliced=sliced[:-1]  
            #========================== bug fix on nov 30th Tuesday hollister starbucks===============================    
            #    sliced=sliced[:-1]
            #else:
            #    print("last char must be 0")
               # print("length of sliced =",len(sliced))
            #print("after teh change the line looks like ",sliced)
            #print("====did it work or not=============")
            
            
            ################################################################
            ## this takes out the last char at end of the line
            #get last character
            #=============================
            #sliced=sliced[:-1]
           # if any of these are True  :),u,#
            #print("====  testing if last character : ) u # ==== ")
            #if lastchar == ":" or  ")" or  "u" or   "#":
             #   print("TRUE weird last character",lastchar)
            #    sliced=sliced[:-1]
            #else:
            #    print('current last char is',lastchar)
                
               
                
            #if sliced[-1] == ":" or  sliced[-1] == ")": or sliced[1] == "u": #
            #    sliced=sliced[:-1]
            #end if
            #===============
            
            #sliced=sliced[:-1] #this is new but when does this occur and why?
            #this is new nov 30th, tuesday hollister starbucks
            
        else: #this means its equal to 0
            #scenario zero tabs in front of first switch starting
            if tabsinthisline == 0:#this handles if there are zero tabs in front of switch line
                sliced = "\t" + line; # add one tab if zero tabs.
                #phase B ============================
                
                print("================================")
                #print("=====phase B sliced=",sliced)
            else:
                #phase C ===================
                sliced =  line; #maning this has at least 1 tab already
                
                print("================================")
                #print("=====phase C sliced=",sliced)
        super += sliced + "\n" # this does all lines in the string
        #=== super 1 ==================
        #print("SUPER 1 =",super)
        #scenario if it's already perfect at 1 tab length in front of switch
        if cutout == -1:  #this means tabs in this line determined to be 1
            super += line 
            #super 2  =====================
            
            print("================================")
            #print("SUPER 2 sliced=",super)
        #end if
    print("================ taking out 2 tabs quickly and dirtily")    
    print("this is the output SUPER lines to see the result")
    print("THIS IS THE RESULTING STRING below this line in manipulate_string function...")
    for line in super.splitlines():
        print(line)
    return super #this should do it now this is what is returned a string called super
    
    
    newstring[0]= super #shift_nest_string_to_left(string)
    #this appends the super string to gold_list_results list 
    gold_list_results.append(super)
    #the string sare in gold_list_results
print('testing cutting out first two tabs from front of string')
print("===TESTING CUTTING OUT FIRST TWO TABS FROM FRONT OF EACH STRING OF CODE==")
print("moving everythign to left side for formatting this sucker see if gold nears")


print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
#output=[]
#output.append(0)
#myinput=[]
#myinput.append(0)
print(" chain methods test with 3 methods that hand off output as input to next method")
print('testing 3 methods in a row november 23rd santa cruz avenue menlo park ')
print("==================================")
print("first let us see the string in the starting representation") 
#for line in teststring6.splitlines():
#    print(line)
#print
#output[0]='' #to shift string identation to the left
print(" **  method 1  **  indent to left   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
#del myinput[:]
#myinput.append(teststring6)
#input[0] = teststring6
############===============
#manipulate_string(myinput[0]) #indent to left  what is the outpout put into 
############==========
#output[0]=newstring[0] 
#for line in output[0].splitlines():
#    print(line)
#print("........")
#razzle = output[0]
#myinput.append(razzle)
#3toosmart = razzle
#mystringname= toosmart #spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print(" **   method 2  ** cut out sitch bodies  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
#right here it can't read the stringname
print("==========starting point======================")
print("================================")
#print("stringname=",mystringname)
#for line in mystringname.splitlines():
#    print(line)
    
#print("checking cat scales list [0] now===========")
#for line in cat_scales[0].splitlines():
#    print(line)
    
#mycat = never_defeated[0]
###################==============
#stringname=mycat;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
#modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)

#print(never_defeated[0])
#start=1,finish=1;
#modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
###################==========
print("please work now did this sucker work tuesday november 23?") 
print('result of taking out inner switches ') 
#output[0]=cat_scales[0]    #outoput 
#for line in output[0].splitlines():
#    print(line)
#print("........")
#del myinput[:]
#myinput.append(output[0]) #does this one work  
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")

#################==========
#take_out_endswitch(input[0])
#################===========
#outoput in holdon[0]
#output[0] = holdon[0]
#print("result of taking out bottom endswitch ")
#for line in output[0].splitlines():
#    print(line)

print("above this line is the totally modified string from 3 chained methods ")


###============= test nov 24th wednesday 2021 target parking lot

test_string4='''
	switch(exp){ #44
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################1
			switch(exp){ #51
				case 'fishy':
					print("do something")
					print("yep")
					fallthru:
				case 'where now':
					print("nice")
					break
				default:
					print("we very done") 
			endswitch 
			#############k
			break
		default
			print("we are done here")
	endswitch #46  
'''

#You can use double or single quotes:
#testing on my iphone. last night. 
testingthis='''
	switch(exp) #23:
		case 'tahoe':)
			print("do something"))
			print("yep"):
		case 'fallen leaf lake':)
			print("nice")#
		####################1
			nested_switch_31:(exp) #31:
			#############k
			break:
		default:)
			print("we are done here").
} 
'''

moregarbage='''
	switch(exp) #1:
		case 1 thru 3:)
			print("where's the dog house!"))
			print('first prize'))
			print('you block head Charlie Brown')u
			fallthru	
			:
		case 4 to 7:)
			print('kangaroo hop hop!')#
			#############1
			nested_switch_22:(exp) #22:
			exp = 32
			nested_switch_33:(exp) #33:
			##############)
			print('taught me how to write code')u
			fallthru	
			 
		 :
		case 8 to 10:)
			print('mocha blast'))
			print('== 31 flavors===')u
			fallthru	
		:
		default:)
			print('the end') 
} 
'''

trythisone='''
	switch(exp) #1:
		case 1 thru 3:)
			print("where's the dog house!"))
			print('first prize'))
			print('you block head Charlie Brown')u
			fallthru	
			:
		case 4 to 7:)
			print('kangaroo hop hop!')#
			#############1
			nested_switch_11:(exp) #11:
			exp = 32
			nested_switch_62:(exp) #62:
			##############)
			print('taught me how to write code')u
			fallthru	
			 
		 :
		case 8 to 10:)
			print('mocha blast'))
			print('== 31 flavors===')u
			fallthru	
		:
		default:)
			print('the end') 
} 
'''

##==============================
##  remove_garbage_on_right_margine(inputstring):    called after manipulate_string
##==============================
#removes garbage on right margine and takes out : in nested_switch if it exists
def remove_garbage_on_right_margine(inputstring): #this fixes garbage characters afterwords
	print('----------cherry on top called----------------------')
	cutout=''
	print("let us ORIGINAL INPUT STRING HERE look at the starting input string before modifying it")
	for line in inputstring.splitlines():
		print(line)
	return  ##  this stops the method cold 
	counter=0
	print('starting to enter cherry on top really serious need to get it working')
	adder='';last_char=''; result = False
	for line in inputstring.splitlines():
		print(line) #if "switch" in line and "end" not in line:
		#need test if last line is a number then don't chop it off
		
		print("length of line=",len(line))
		#if length of this line is more than zero
		if len(line) > 0:
			last_char = line[-1]; #returns a character or number or space whatever it is 
		#ourstring = "switch(exp){ #22"
		last_char_in_line_is_number = last_char.isdigit()
		#  checks if last char in line is a number
		#############################
		if last_char_in_line_is_number == True:
			print("last character is definitely a number")
			##########################################
			print("last_char a number is",last_char)
			#if anumber == True:
			print("SECOND SCENARIOthe last character is a NUMBER")
			adder += line + "\n"
			print("last_char=",last_char)
			continue
		
    #need to ahve it check for "))"
		################if line ends with junk ==========================
		if last_char == ":" or last_char == ")" or last_char == "u" or  last_char == "#": #maybe any character
			#need to check if last 2 are )) only cut off one, otherwise
			# if it's only ) and then don't cut it off
			
			print("FIRST SCENARIO :, ),u, #")
			adder += line[:-1] + "\n" #this deletes the last character from the line
			print("last_char=",last_char)
			
			
		########### if line ends with a space 	
		if last_char == "": #meaning it is an empty space
			print("THIRD SCENARIOlast char is a SPACE")
			adder += line + "\n"
			print("last_char=",last_char)
			
			
			######## this handles if the line ends with a number
			#elif last_char.isdigit():   
			#	print("SECOND SCENARIOthe last character is a NUMBER")
			#	adder += line + "\n"
			#	print("last_char=",last_char)
		print("counter=",counter)
		counter += 1
	###########################################################
	############################################################	
	#decided to get rid of : inside of nested_switch here
	#this fixes this bug  >>  nested_switch_11:(exp) #11:
	print("NOW remove dots inside of nested_switch line if they exist")
	
	verycool=''	
	
	
	for line in adder.splitlines():
		#check if nested switch in this switch string
		if "nested_switch" in adder:
			#print("TRUE nested_switch in line")
		
			if "nested_switch" in line and ":" in line:
				#print("nested switch is True")
				verycool += line.replace(":","") + "\n"
			else:
				verycool += line + "\n"
			
		else:
			verycool += line + "\n"
			#print("no nested_switch in this switch string")
			pass	
	print("FINAL OUTPUT FOR THIS STRING======>>>>>")
	for line in verycool.splitlines():
		print(line)    
	print('afterwards not working yet just trying to get last char of each line')	
	print('resulting fixed removed garbage looks like this.....')
	
	
		#it does all lines of the string taking out the first 2 tabs which are chars
		#if cutout != 0  or cutout > 0:#this handles if cutout = 0 meaning None
	newstring[0]=verycool #bug was right here.	
	inputstring=''
 ################################ 
	#print("THIS IS THE RESULTING STRING below this line in manipulate_string function...")
	#for line in super.splitlines():
	#	print(line)
	#newstring[0]= super 
	#print('the final output with cleaned up garbage should be here')
	#print("outpout of cherry on top ==== attempt 1 ")
	#for line in newstring[0].splitlines():
	#	print(line)
	
print("STARTING test 1")
print("take care of garbage on right margine and remove : in inner nested_switch")
#remove_garbage_on_right_margine(moregarbage)
#for line in newstring[0].splitlines():
#    print(line)
#exit()    
    
#print("next one")
#print("STARTING test 2")
#remove_garbage_on_right_margine(trythisone)
#for line in newstring[0].splitlines():
#    print(line)

print('what about this one')
print("STARTING test 3")
#remove_garbage_on_right_margine(test_string4)
#for line in newstring[0].splitlines():
#    print(line)
#print("STARTING DONed")
#exit()









print("Hello")



def method1(inputstring):
     return;
     concat =''
     print("==method1==")
     concat += inputstring
     concat += " fish"
     print(concat)
     return concat

def method2(output1):
     return;
     concat =''
     print("==method2==")
     concat += output1
     concat += " mice "
     print(concat)
     return concat

def method3(output2):
     return;
     concat =''
     print('==method3==')
     concat += output2
     concat += " \nrain fall heavy"
     return concat

print("above the rocket launch")


####===========================================================
def try_these_chain_methods(inputstring):
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("looping through inputstring to see the starting state")
    for line in inputstring.splitlines():
        print(line)
    ##==========    
    print("==trying these three methods and see if it works or not==")
    output1 = manipulate_string(inputstring) #shift string to left
    print("reached after first method called")
    print("mOnday morning Blues testing of manipulate_string method")
    #print(newstring[0])
    
    #takes out extraneous :, ),#,u on right side AND removes : inside of nested_switch word
    remove_garbage_on_right_margine(output1) #this should work now Takes out garbage on far right
    output1 = newstring[0] #extranious #: ) empty lines have : u
    for line in output1.splitlines():
        print(line)
        
    #return    #stoppinghere 
    ##=========
    start =1; finish=1;
    output2 = modified2_cut_out_inner_switch_body_leaving_switch_word(output1,start,finish,)
    print("reached after second method called")
    ##=========
    output3 = take_out_endswitch(output2)
    print("reached after third method called")
    print("this is the final output string from the three chain methods",output3)
    ##=========
    for line in output3.splitlines():
        print(line)
print("serious three raptor engine test launch")        
inputstring= teststring6        
#try_these_chain_methods(inputstring)
print("finishing calling test chain methods")
print(" end of today's test ")
#exit()    
#starting teststring6
#take the string to test it
#shift_nest_string_to_left(string)
#manipulate_string(item) 







	


	
##=====================================
## swap_endswitch_with_curlybrace() this uses the method take_out_endswitch()
##======================================
##=presumes that quail list already filled up with seperated strings
devious_list=[]
peachtree=[]
#so this function loops thru quail list and checks if endswitch in a string in quail
def swap_endswitch_with_curlybrace(): #using testlist_of_strings
    print("=== swap_endswitch_with_curlybrace() ===========")
    print("this requires that quail list must already be filled with switch strings")
    counter=0
    #assert len(quail) > 0 #it did say quail list 
    if len(gold_list_results) > 0: #meaning there is something in quail list
        #looping thru quail list
        for item in gold_list_results:  #notice that this works by looping thru quail list and changing strings with endswitch
            if "endswitch" in item:
                print("yes endswitch is in this string")
                #it happens here TAKE OUT ENDSWITCH(ITEM)
                take_out_endswitch(item) #calling take_out_endswitch saved to holdon[0]
                #print(holdon[0])
                print("its appended to devious_list here via holdon[0]")
                devious_list.append(holdon[0])#this line just might not be working correctly need to look at it further
               # testlist_of_strings[counter] = holdon[0] #this puts it back into testlist slot
                holdon[0]=''
                counter += 1
                continue
            else:
                print("nope no endswitches")
                counter += 1
                continue
    else:
        print("testlist_of_strings list is empty so can't do swap endswitch with curylbrace")
    print("let's see if this works or not does this thing actually work")
    print('strawberrie fields are forever')
    # see if it takes endswitch out and puts } in its place
#end function



#three test in a row here of method calls 



  
testlist_of_strings=[]
testlist_of_strings.append(teststring1)
testlist_of_strings.append(teststring2)
testlist_of_strings.append(teststring3)
testlist_of_strings.append(teststring4)
testlist_of_strings.append(teststring5)
testlist_of_strings.append(teststring6)
testlist_of_strings.append(teststring7)

print("===== testing this using a loop =====")
print("this left shifts and indents each switch string to prepare for going thru bypass205()")
counter=0  #this shifts (indents) the whole switch string to the left with 1 tab in front of switch
print("this prints out the switch strings after left Red Shift== to one tab")
cow_hide=[]
fuel=''
##==============================================
##  starting_what_switch_strings_look_like():
##==============================================
def starting_what_switch_strings_look_like():
    print("starting we have...")
    for item in testlist_of_strings:
        print(item)

##==============================================
##  left_shift_all_switch_strings():
##==============================================    
def left_shift_all_switch_strings(): #this goes thru testlist_of_strings
    print("now we will shift the switch to the left margine")
    counter=0
    for item in testlist_of_strings:
        print("counter =",counter)
        manipulate_string(item) #this calls manipulate_string(item) to shift the switch string to the left
        #adds change to axis put into newloop appended 
        counter += 1
#output is in gold_list_results list
print("   ")
print(" this is AFTER the switch strings have been seperated and put into a list")
print(" called testlist_of_strings  ")
print(" testing  ==left shift jazz== ")
starting_what_switch_strings_look_like()
left_shift_all_switch_strings()



print("DID IT WORK OR NOT the changes stick is it still === LEFT SHIFTED=====")

print('we are here now nov 23rd tuesday morning morgan hill.')




#for item in devious_list:
 #   print(item)
critical_list=[]
print('plum tree test') #hours spent getting this tow ork oct 17th, 2021 9;52pm
def goodtimes():
    #requires gold_list
    print("good times()")
    print("looping thru gold list results list")
    for item in gold_list_results:
        print(item)
        del several_three_tab_switches_list[:] #delete it first to erase the chalkboard
        stringname=item
        get_second_switch_numbers_check_if_many(stringname) #output here
        print("several_three_tab_switches_list=",several_three_tab_switches_list)
        print(several_three_tab_switches_list)
        why= several_three_tab_switches_list
        print("why=",why)
        print(type(why)) #gets the type of var why is.
        results=list(map(int,why)) #changing the string numbers into ints then it works
        #this adds to this list the inner switch numbers for each switch string
        print('results=',results)
        #some will have none, some will have 1, and some will have more than 1
        critical_list.append(results)
        print('critical_list=',critical_list)
        #print(peachtree)
goodtimes()    
print("end of show")    
print("resulting three tab inner switches in each of the switch strings")


def cool():
    print('==========cool function==== is this working yet====')
    for item in critical_list:
        print(item)

cool()

   
    
    
    #holdthis[0] = galaxy.replace("endswitch","}")
#I need to replace the inner switches with methods now
####========== sunday october 17th, 2021 



#what is below here isn't working right for some odd reason

print("about to call swap_endswitch_with_curlybrace() ===")
print("this replaces each endswitch with } to prepare for bypass205()")
#this one is designed to go thru quail list
print("here we take out the endswitch in each string and replace it with }")
swap_endswitch_with_curlybrace() #have it work with gold_list input already left justified
print('about to loop thru devious_list to see if it swapped endswitch with } or not')
for item in devious_list:
        print(item) 
#print("now we will loop thru the testlist_of_strings to see the endswitch is gone now")
#for item in testlist_of_strings:
#    print("counter =",counter)
#    print(item)
#    counter += 1
    


print("TESTING string 1 now=======>>")
manipulate_string(teststring1)   
#exit()
'''
print("TESTING string 2 now========")
manipulate_string(teststring2)   
print("TESTING string 3 now========")
manipulate_string(teststring3)   
print("TESTING string 4 now=========")
manipulate_string(teststring4)   
print("TESTING string 5 now========")
manipulate_string(teststring5)   
print("TESTING string 6 now=========")
manipulate_string(teststring6)   
print("TESTING string 7 now=========")
manipulate_string(teststring7) 
#shift_nest_string_to_left(teststring6)  #3 tabs  DOWN TO 1
#this one is not working 
'''
print("test 2")
print("testing indenting correclty teststring1")
#shift_nest_string_to_left(teststring1) 

print("test 1")
print("testing indenting correclty teststring2")
#shift_nest_string_to_left(teststring2) 

#this doesn't work yet
#now to a loop 
#listtest=[]
#listtest=[teststring1,teststring2,teststring3,teststring4,teststring5,teststring6,teststring7]
#print("testing going thru all strings and indenting them ")
#counter =0
#print("====starting looping thru each teststring=====")
#for item in listtest:
#    shift_nest_string_to_left(item)
#    print("========")
#    print("counter=",counter)
#    counter += 1
    
      
# ==================================================================================
# what to work on today thursday, october 14th, 2021 ,,,,,,,,,
# so I would feed in just a param to look for "#" AND "switch" AND "31" and get tabdepth
# I need to try calling and looking for switch in line and # and the number 31
# and loop thru to endswitch at same tab depth.
# get tab depth on switch   tab_depth1 = line.count("\t")
# and then the first line with "endswitch" in line and this_tab_depth == tab_depth1
# =================== thursday coding ================================================

#so the formula is whatever never it starts from subtract that
#so if it starts at line number 11 at beginning of string with switch
#so if we do 31 down to 41 we subtract 11 from first number and second number
#so it's really 20 down to 31
#or I could have it start #31 in line and switch in line
#loop until same tab depth and "endswitch" in line


 #add item to dictionary
#pears['3'] = [4,7] #example
print(pears)
 #access dictionary
#x = pears("1")
 
 #remove item from dictionary
#thisdict.pop("model")
 
 
#now when I loop thru switch and endswithc lines
#have it fill the dictionary with the data



#######================================================================#########==========

#######================================================================#########==========
rose=[]
rose.append(0)
rose.append(0)

#######================================================================#########==========

#input1 = rose[0]
#input2 = rose[1]
#23,46

#start = rose[0]+1
#finish= rose[1]+1

#skipping_some_lines(x,start,finish)
#print(toosmart[0])


#always do one nest. Just change the switch start and stop sooo simple


## MAIN TRIGGER FOR TESTING THIS CODE OF EXTRACTING NESTED SWITCH STRINGS 
###################################################
## #this means I need to feed in the one switch location and one endswitch location
## that need to have been already figured out



##  copy_one_nested_switch_string(m82)   <<=======     this is the main trigger for the test july 18th 
##  I will need to add another paramter to determine which nestd switch is grabbed 
def extra(): # does nothing
	print("did it work??")
	
	print("#method  get_switch_and_endswitch_locations()")
	######### just commented out line below july 19th 1:10 pm
	
	#get_switch_and_endswitch_locations(m82) # presumes only one nested switch inside param would be passed here to to pass thru this is new  method call
	######## I will need to take out this method above out of this function
	######## this currenlty only takes in the first switch by design 
	#this builds a list of switch_location and endswitch_location all of them
	# but this function conpy one nested stirng ONLY USES the first switch and first endswitch
	###################################################################
	#this gets switch_location[0] and endswitch_location[0]
	print("copy one nested switch string ()")
	print("get start of nested switch and end of nested switch")
	print("#method get_one_nested_switch_start_and_finish()()")
	#get_one_nested_switch_start_and_finish() # method call 
	#this just copies the locations of switch and endswitch into 
	
	
	
nest_string=[]	
######################################################
##  def copy_one_nested_switch_string(m82,zebra,cow)
######################################################
#this fills nest_string list with copies of the switch body strings
#and takes out front two tabs from string
def copy_one_nested_switch_string(m82,zebra,cow): #so I would add a param to determine which nest to grab july 18th 
	print("==== copy_one_nested_switch_string() =====")
	print("===========.................==============")
	#print("let's look at the input")
	#print(m82)   #main string name
	print(zebra) #switch    location
	print(cow)   #endswitch location
	
	print("========COPY ONE NESTED SWITCH STRING()== called=====")
	#input_string[0]=samplestring
	counter=0		
	buildstring=''
	print("printing samplestring first")
	#print(m82)This ONLY GRABS the first position which is 0 for switch and endswitch
	#when I loop thru this in the peartree dictionary I will put the current pair into 
	#switch_location[0] and endswitch_location[0]
	######################################################
	print("WHAT ..... is in these two lists position 0 swith and endswitch")
	#print("it sees in y",y, "well how does it look")
	####################################
	print("passing the params for switch and endswion and endswitchlcoation")
	del switch_location[:] #these were passed as params that govern grabbing the right string
	switch_location.append(zebra)
	print(switch_location[0])
	del endswitch_location[:] 
	endswitch_location.append(cow)
	print(endswitch_location[0])
	#print("switch_location[0]",switch_location[0]) #10
	#print("endswitch_location[0]",endswitch_location[0]) #20
	#print("what it sees in switchlocation0 and endloaction0")
	print("===========================================")
	# LOOP thru string
	###=================
	fridge[0]='' #empty this sucker just in case oct 5th 2021
	#print("list_of_switch_range[1]",list_of_switch_range[1]) #10
	#print("list_of_switch_range[2]",list_of_switch_range[2]) #20
	for line in m82.splitlines(): #determine if "endswitch" is in line
		#this by default starts copying the string once line greater than 2
		#this says if counter between 10 and 20 including start number and finish number		
		#############################################
		#if "switch" in line and "endswitch" not in line: #this shows just switch
		#	print("switch in this line",counter)
		#if "endswitch" in line:
		#	print("endswitch in this line",counter)
		##############################################	
		#right here if counter is between min line number and max line number
		alpha = int(switch_location[0])
		beta  = int(endswitch_location[0])   
		#this loops thru string and copies lines to buildstring
		if counter >= alpha and counter <= beta: #if counter between(within) alpha and beta:
			buildstring += line + "\n" #I need to start at the 10th line
			counter += 1	
			continue
		else:
			counter += 1 #wasn't adding to counter
			continue #really
	print("the new creation concatted should be buildstring=")
	fridge[0]=buildstring  #here buildstring is stored in firdge[0]
	print("what is in the fridge[0] the nested switch copied")
	#print(fridge[0]) #the copied nested string is in here  fridge[0]
	#############################################
	#newstring='';cool_string = fridge[0]
	print("#method take_out_x_tabs_from_front_of_line()")
	#calls method take_out_x_tabs_from_front_of_line
	#it was cool_string which is now m82  was (2,cool_string)
	newstring=take_out_x_tabs_from_front_of_line(m82) #this is running #takes off 2 leading tabs
	fridge[0] = newstring
	
	#print("final outcome Tron")
	#print(fridge[0]) #this results in the nested switch string with  2 tabs taken off front of each line
	################################################
	# July 21st, 2021 4:16 pm Gilroy Starbucks
	#this copies the string just copied and put it into nest_string
	#its added to nest_string right here 
	#####################################################
	# the copied switch body string goes into fridge[0]
	# and then is added to nest_string list
	######################################################
	nest_string.append(fridge[0]) ##<<<===== right here the nested string is added to nest_string
	#this is filling nest_string with the contents of each nested string
	#then fridge[0] is added to the list nest_string
	print("nest_string length=", len(nest_string))
	#print("line 4315 nest_string here has this in it",nest_string)
	#print("trying to loop thru nest_string to figure this out")
	print("pumpkin pie")
	#for item in nest_string:
	#	print(item)
	#	print("==========")
	
	#need to delete teh first three tabs
	fridge[0] ='' #this empties fridge[0]
	print('trying to empty nest string here on line 4330 see what happens ')
	#del nest_string[:] 
	print("length of nest_string at this juncture is now",len(nest_string))
	#################################################
	print("copy a nested string and output it") #august 5th, 2021
	#print(nest_string)
	
print("====TESTING COPYING A NESTED STRING ======1 2 3 A  B C===....")	
print("====STAR TREK ENTERPRISE ===....")	
print("this is where I call the function to copy JUST ONE nested switch")
# july 18th I would need to add another paramter here like 2, for second nested switch 
#copy_one_nested_switch_string(samplestring) #reads sample string here 
#output into fridge[0]

#this should just call one nested string
# I will put the loop to go thru peartree dictionary
#and call copy_one_nested_switch_string(samplestring)
#and have it added to a list


# I will need to append it 


#this calls in order these methods
'''
pears =	{  #for pear tree in backyard (2 of them)
  "1": [10,20], # I can make these now 
  "2": [28,38],
}
'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========




smart_switch_numbers=[]
#the purpose of this is the switch ID number is it's initial line number
#NOTE: no spaces inbetween switch(exp){ otherwise replace doesn't work right 
#testing adding the comment and line number for switches

###=====================what I need to do =====================
# important sept 30th
# all I gotta do is make each nested switch like
# the main switch template and take out inner switch bodies
# then using the line number put in the generated method in it's place
# be sure that I add the line number as a comment I have that code
# and then make sure I get that switch line number to
# make the nested method to replace it
#####================================================================
#this one is all new and not tested september 30th musing
#testing adding the comment and line number for switches
#this is new not currently used or tested 

testcode='''
					switch(exp){ #53
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
'''
#I am testing with this string the inner swithc is at 3 tabs, first switch at one tab.
#this was teststring6 also added 0 to end
teststring60='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  this is what it will actually look like 
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''


#so I will know what switch body I am dealing with so I can juggle them and manage them					
#when I get a string that I have copied I just need the switch at the top
##====================================
##  get_switch_number()  it gets the switch number from FIRST LINE OF STRING then bails
##====================================
def get_switch_number(stringname): #this might be for when
	print("indian braves dancing for rain")
	# I create copies of the switch body strings
	print("get_switch_number() called it's getting the first inner swithc at 3 tabs length ")
	awesome=''
	y = ''
	counter =0  #say it's 3
	print("this is what the string we are manipulating looks like")
	for line in stringname.splitlines():
		print(line)
	print("================-------===")
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter =0
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tablength= line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3:#and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			print("switch number is==>>>>>",y) 
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;

#skip 16 thu 38
print('this is testing october 12th to get the inner switch line number as a comment ')
weasel=get_switch_number(teststring60) #so this figures out what switch is in a list slot
print("number of this switch string(should be 66 ..",weasel) 
print("ending program here....")



	#testing here 
axis=get_second_switch_number(teststring4)
print("you can always try..")
print("should be 31 ... ",axis)
# get second switch numbers check if many
#experimental new october 14th, thursday, 8:06pm 


print("get second MASH switch number (the comment number after teh inner switch")
print("testing to see if it correctly retrieves the number 66 in the nested switch")
weasel=get_second_switch_number(teststring60)
print("should return 66")
print("weaseL=",weasel)		


weasel=get_second_switch_number(teststring3)
print("should return 23")
print("weaseL=",weasel)		

weasel=get_second_switch_number(teststring2)
print("should return 15")
print("weaseL=",weasel)		



			
#keep line #15 del til = #38
################# creation of loopstring list to hold string that will hold the nested switch string

loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=red_robin #   what it was previously ==samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
'''
#########################################
## loop thru pears dictionary
## and calls copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])
## to copy one nested switch at a time
    #it might just have to go thru once to fill pears
    # going thru a dictionary I need to designate which pair 
   
    ##########################################
    ## this loops thru the dictionary pears
    ##########################################
    print("about to loop thru pear values")
    #looping through dictionary pears 
      #say_something(cool) #this way the switch and endswitch locations are passed into the function
        ##########################################################
        ## this calls COPY ONE NESTED SWITCH STRING()
        ##########################################################
        print("about to start copy_one_nested_switch_string()")
'''






#https://www.youtube.com/watch?v=qtpxiNvGCp4
#########################################
##   copy_one_nested_switch_case_body()
#########################################
def copy_one_nested_switch_case_body(): #uses pears.values()
    print("======copy one nested switch case body () ....=====.")
    print("make the impossible into reality VIKING SHIP  fish 1 ")
    print("show what is in ")
    print(blueberries) #what is pears have in in it
    counter = 1
    #using blueberries dictionary and not pears 
    #just changed this oct 6th wednesday 10am 2021 morgan hill starbucks
    
    # pears is a dictionary with values of start switch and end switch
    ## LOOP ######## this loops thru pears dictionary
    for x in blueberries.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        #print(x)
        cool = x #(which is a pair thus only two values)
        print("cool=",cool)
        print(cool[0],cool[1]) #this is switch and endswitch line numbers 
        print("copy one nested switch string")
        #this uses the pair location start switch and end switch numbers
        #the string is in loopstring[0] <<----------------
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #great where does this copy of the string put into??
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        print("========================")
    #end loop
   
        

###=== this goes thru pears dictionary  and copies the nested switch strings
print("=== GODZILLA Time  ===")
#uses pears dictionary
'''
pears =	{  #for pear tree in backyard (2 of them)
  "1": [11,47], # I can make these now 
  "2": [49,73],
  "3": [15,38],
  "4": [53,64],
  "5": [23,33] #no comma after last data piece apparently
}
'''

print("here we go ... copy_one_nested_switch_case_body_blueberries():")
##====================================================
## copy_one_nested_switch_case_body_blueberries()
##================================================
#########################################
#this is using the string red_robin for testing purposes. 
  # pears is a dictionary with values of start switch and end switch
    #this goes thru the blueberries dictionary set of switch end switch pairs ===========
    ##===================================================================================
    ## LOOP ######## this loops thru pears dictionary
    #del nest_string[:] #empty this list
    #this is the blueberry dictionary 
    #it loops thru blueberries to copy a string
    #looping thru blueberries dictionary here 
    


    
loopstring[0]=red_robin #testing on oct 5th Tuesday
def copy_one_nested_switch_case_body_blueberries(): #uses pears.values()
    print("======copy_one_nested_switch_case_body_blueberries() ....=====.")
    print("make the impossible into reality VIKING SHIP  fish 1 ")
    print("show what is in ")
    print(blueberries) #what is pears have in in it
    print("I think that at this point nest_string whould be empty")
    print("len(nest_string=",len(nest_string))
    #nest_string=[] #this reinitializes it 
    counter = 1
  
    #right here nov 6 2021 saturday change this to the list of sublists (time to ditch the dictionary
    print("showing contents of blueberries dictionary values the strings here.")
    for x in blueberries.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        print(x)
        cool = x #(which is a pair thus only two values)
        print("cool=",cool)
        print(cool[0],cool[1]) #this is switch and endswitch line numbers 
        print("copy one nested switch string")
        #this uses the pair location start switch and end switch numbers
        #the string is in loopstring[0] <<----------------
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #this copied string is added to nest_string list
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        print("========================")
    #end loop
##=============oct 5th musing how to maket his puppy work 
#I need to have switch numbers by line number
# associated with it's pair start stop
#===================   
print("testing blueberries dictionary list to get the string bodies printed out")
####################
#print("NEST_STRING line TAHOE CABIN Bears ione 4651 what is in nest_string at this point")
#print(nest_string)
counter =1  #so the nest_string would have the switch body strings in it
for item in nest_string:  #going thru nest_string of inputs I think
    print("counter=",counter)
    print(item)
    print("end of this switch string body")
    counter += 1
    print("======....=====")
    
    
del nest_string[:] #new just now putting this hear
print("is this thing turned on right now?")
print("the autumn leaves are falling now.")
print("let us see what red_robin looks like")
for line in red_robin.splitlines():
    print(line)
print("done printing out red_robin input to compare it with")
print("  this is the autumn LEAVES  test ==")
print("======after having added line numbers as comments to each switch ===========")
add_comment_and_line_number_to_all_switches(red_robin)
print("=======now do the next one=======")
print("=======now do the next one=======")
print("=======now do the next one=======")
add_comment_and_line_number_to_all_switches(autumnleaf) ##testing this right here oh yea

#put it into a list which holds the new string with switch lines added as comments
#here I add line numbers to switches
#inputstring[0] #input string will be in here
copy_one_nested_switch_case_body_blueberries() #which is uses red_robin
print("finishing blueberries")

print("let see this puppy work ..... great america babes ignored me ...")
#copy_one_nested_switch_case_body() # this calls the loop

#print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)




#this is the resulting output of copying the string embedded in the main switch

holdthis=[]
holdthis.append(0) #creates the space to store it


teststring_brace='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  this is what it will actually look like 
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''

#this swaps endswitch with }
# I need to count the "}" in the string, there should only be one, actually none
# if there is one it needs to be in the right place.
# I will have to loop thru the list to look if there is a brace in it already.
######################################
## take_out_endswitch(stringname)  #replaces endswitch with }
######################################
list_of_line_numbers_of_endswitches=[]
holdthis=[]
holdthis.append(0)
#the issue is that I need it to only do the bottom one 
def take_out_endswitch(stringname):
	print("==========take_out_endswitch()and put brace in called=======")
	x='';x=stringname.count("endswitch") #should be 1
	print(x)
	counter = 0
	for line in stringname.splitlines():
		if "endswitch" in line:
			list_of_line_numbers_of_endswitches.append(counter)
			counter += 1
			continue
		else:
			counter +=1
		continue
	print("list of line number of endswitches=",list_of_line_numbers_of_endswitches)
	coffee =list_of_line_numbers_of_endswitches[-1] #last one
	print("the last endswitch =",coffee)
	print(stringname) #this takes out endswitch and replaces it with }
	stringname=stringname.replace("endswitch","}")
	for line in stringname.splitlines():
		print(line)
	holdthis[0] = stringname#now galaxy gets what is in holdthis[0]
	print(holdthis[0])#return stringname #and this is returned
	
print("testing take out endswitch from string and replace it with a } ")
take_out_endswitch(teststring_brace)
#outpout to holdthis[0]
#for line in holdthis[0].splitlines():#
#	print(line)
	



###===================================================
##   show_list_of_nested_strings_separated()
###===================================================
## july 21st 2021 349pm gilroy starbucks
#oct 5th this is a list of thes copied switch ends witch stings in nest_string
###=== this shows the nest_string list of nested switches
#this just loops thru nest_string which has the seperated nested strings
def show_list_of_nested_strings_separated():
    print("======show list of nested strings separated=====")
    print(" == StayPuff Marshmellow Man ==")
    counter=1
    for item in nest_string: #this has the nest strings in it ALREADY nov 6, 2021
        print("counter=",counter)
        print(item)
        counter += 1
    print('end of first simple test ')   
    #===========================    
    counter =0
    print("loops thru nest_string that we filled up in copy_one_nested_switch_string(m82,zebra,cow)")
    #this requires nest_string which is looped thru
    print("length of nest_string=",len(nest_string))
    # loop thru nest_string list     to take out endswitch
    #for item in nest_string: #nest_string must have refined main switch with nest methods numbered already
    #    if "endswitch" in item: #swap endswitch with '}'
    #        print("== endswitch detected ==") #should be 2 of them
    #        print(counter) #takes out endswitch from this current string here
    #        holdthis[0]=take_out_endswitch(nest_string[counter])#takes out endswitch from each string
    #        nest_string[counter] = holdthis[0] #voodoo magic
    #        counter += 1
    #    else:
    #        print("oh good") #absolutely nothing happens here
    #        counter += 1
                
    print("see if it fixed it here")
    print("this is showing what's in nest_string list")
    #this loops thru nest_string to show after the changes were made
    print('this should be it right here the seperated nest strings')
    print("remember that the main switch string is totally different ")
    print(" this is the CRUCAL TEST OUTCOME RIGHT HERE TO SEE IF IT WORKED")
    print("what this does is print out the lists indiviudally after separating them")
    print("printing out the nest_string list right here play baseball Yankees")
    print("copied strings one by one")
    print("YANKEES need to show each copied switch body string")
    print("wow that worked")#da = blueberries.get("2")
    #print("getting data in blueberries")
    #print(da)
    mycounter =1
    nest_string_size= len(nest_string)
    print("length of blueberries =",len(blueberries))
    ###############
    #this makes sure that the nest_string is equal in size to blueberries
    # to counter a bug of overflow junk that I will figure out later
    # oct 5, 2021
    print("blueberries",blueberries)
    print("")
    #this deletes excess data that is appended to nest_string inexplicably
    #this simple fix was solved on oct 5th tuesday at 11:30pm 2021=======
    #temporary getting excess from nest_string
    #so 
    while len(nest_string) > len(blueberries):
        del nest_string[-1] #last element in list is deleted
    print("all done")
    print("length of nest_string=", len(nest_string))
    print("yes finally works NASA is born")
    #get length of blueberries
    #then reduce size of nest_string to that number (figure it out later) weird bug
    print("nest_string size = ",len(nest_string))
    for item in nest_string:  #nest_string
            da = blueberries.get(str(mycounter))#gets string at this position
            print("getting data in blueberries",da)
            print("counter=",mycounter)
            print(item)
            mycounter += 1
            
            print("==========-----------seperated nest strings -----------------")
    print("==========")
    #now delete extra slots in nest_string
    
    
print("===============================================================")
print("middle ground filler here to separate the change just made. fish 2 ")
print("===============================================================")
show_list_of_nested_strings_separated()
#now replace teh third string(the main string)
# this is to simulate cutting out the inner switches
## july 22nd, 2021 




####===========================================================###
####===========================================================###
####===========================================================###
print("july 22nd 2021 additions...====")
###============== this is working correctly now ==========
## more_testing()
##========================================================================

#sprint("checking number of nested switches at three tabs")
#stringname=testingstring1
#get_second_switch_numbers_check_if_many(stringname)


######################
##  more_testing()
######################
def more_testing():
    print("=== more_testing() == charisma ===method testing ")
    #this is adding samplestring with main to nest_string[2] to see what it will look like when working
    print("let's see what is already in nest_string ===> SpaceX pretest ")
    print("to see what is in nest_string")
    for item in nest_string:
        print(item)
    print("so slow 3 which is nest_string[2] has the main string in it")
    #let'see how it looks"
    print("==== after simple test of contents of nest_string")
    print("========")
    print("here we replace it with what will be after I modify it. this is dummy data testing")
    print("finished main string with nested methods added put into nest_string[2]")
    nest_string[2] = samplestring_main # the third one - putting in a different string premade
    #this is what is different right here in the line above
    
    #testing what the stages need to look like
    #to test what it should look like but doesn't yet
    print(" now we will try it again and see how it looks ")
    print(" after changing main string boo boo ")
    #loop thru nest_string
    for item in nest_string:
        print(item)
        print("===========///======oct 5 tuesday 2021 testing  ========")
        
        
###==================================== oct 5 thinking how to do this. 
#for each switch number I need to know what ranges of it's inner switches are
#I need the range of the inner switch numbers start and stop
#so inner switch ranges for switches by switch line number

#more_testing()

####===========================================================###
####===========================================================###
####===========================================================###


### this works this takes the copied nested switch
### and sets the proper indentation for it
#so it takes out 2 really but we have to say 3
## july 17th 10:12am 2021 starbucks

#the eye opening= make a list of the methods sequence
#tuesday, August 10th, 2021 ====,,,,,,,,,,,==========




loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
copy_one_nested_switch_case_body() # this calls the loop

print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)

show_list_of_nested_strings_separated()
more_testing()


###==========================================================

#def tab_swap(x,y):
#    replace(x,y)

########==============
#wilderness=
#def set_front_tabs(x):
#    wildness=''
#    for line in nest_string.splitlines():
#        wildness += line.tab_swap(3,1) #strips one right
#        wildness += "\n"
#    print("after minor surgery see if this works")
 #   print(wildness)






# copy line by line stripping all tabs
# and then based on if starts wwith swtich 1 tab
# if case 2 tabs
# if not switch and not case three tabs
# if endswitch one tab
# if default two tabs


#unless I make a new string _so I want to remove teh first 2 tabs only
alpha_string=''
str1=''
#for line in nest_string.splitlines(): 
#    #put line into list, del first three tabs then conver to string
#   aline = line.split() 
#    print(aline) 
#    str1 += str1.join(aline) + "\n"
#    #print(str1)
#    
#print("string now is...")
#for item in str1:
#    print(item)


 



#########################################==============
## === skipping_some_lines() ========   July 5th, 2021 ===============
#########################################
#this works for one nested switch right now
#this goes thru a nested switch and takes out the nested single switch.

### solution found for dealing with deeply nested switches
#I think that I can use this if I take out the innermost switch
## first and then it should work  
# so the plan of attack is to change(yes change) the inner most
# depth switch first
#and work back to the next level till I am at the first level of depth.


#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========

skip_range=[]
#skip_range.append(0);   
#skip_range.append(0) 
#july 5th, 2021
#so I still need to get the start and finish lines  switch and endswitch for input 
del ibm[:] #empties it
#print(ibm[0])
ibm.append(samplestring) #so in  ibm[0] this is putting samplestring into ibm[0]
print(ibm[0])
#===================print testing on july 24th saturday  2021 at 9:36am =================
print("at this point we have this in ibm[0] after taking out the first nested switch")
#del skip_range[:]
print("LOOP TEST THRU RANGE LIST Goofy dog")
range_list=[]
skip_range.append(0) #slot [0]
skip_range.append(0) #slot[1]


#string,start,finish
#first it will just detect one nested switch , soon it will detect many

#this loops thru a string and makes a copy of the string
# but skips over a range example lines 10 thru 20
toosmart=[]
toosmart.append(0)
flag_test=[]
flag_test.append(False) #flag_test[0] set to False right here 
baton=[] #this is used to hold the concatted string that is changed on each pass 
baton.append(0)
baton[0]= "nada" #to start with to test this monstrocity


rose=[]
rose.append(9)  #testing purposes 
rose.append(19)
test_code_now='''
					switch(exp){ 
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){   #9 
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch  #19
							#############
							break
						default:
							print("we are done here")
					endswitch 
'''








#this is testing with dummy data above in test_code_now
#taking out the inner switch body
print("halloween is coming snoopy and woodstock test")

print(test_code_now)
#the inner switch is at 9 (which we keep) so we start from +1 meaning 10
#and the endswitch is at 19 but we need to nuke that too so it's endswitch + 1

#the number system starts from 1 for the switch numbering
#because it starts counting from 0 and not 1 we need to subtract 1 from it
#so it was originally 10, 19

#if switch is #9 and endswitch is 19
#Add 1 to each number start and finish
print("===========rose test==== testing taking out inner switch body ===")
#the pair would go here 
input1 = rose[0]
input2 = rose[1]
print(input1)
print(input2)
print("take out 10 thru 20")
x = test_code_now
start = rose[0]+1 #10 #TO PRESERVE INNER SWITCH TO REMAIN THERE
finish= rose[1]+1 #20 #TO GO ONE BEYOND ENDSWITCH WORD
skipping_some_lines(x,start,finish)
print(toosmart[0])
print("=====end end end of show end of this dumb test==testing rose flowers ===")
# october 1st this will have to be a prescan first pass to get the locations 
# this will look for an inner switch after first line and get it's line number
# and find it's 'endswitch' or '}'
# and put the switch line number and endswitch line number into a pair
# and then append it and keep going and that way it figures out the location on it's own
coffee_switches=[]
end_coffee_switches=[]

combinedlist=[]
switchtabs=[]
endswitchtabs=[]

#this is not working right 
### mr coffee smart skipping lines 
## mr_coffee_smart_find_innerswitches bodies and skip them except for inner switch word


##======================================================
##  mr_coffee_smart_skipping_lines(inputstring):
##======================================================
def mr_coffee_smart_skipping_lines(inputstring):
	print("======= mr coffee smart skipping lines ..this =======")
	print(" makes pairs to find locations of switches and endswitches.")
	print(inputstring)
	counter =0
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			tabdepth= line.count("\t")
			coffee_switches.append(counter)
			switchtabs.append(tabdepth)
			
			counter += 1
		else:
			
			counter += 1
	del coffee_switches[0] #deletes the first switch which is at the top 
	###=================================
	count =0
	#this looks for endswitch locations
	for line in inputstring.splitlines():
		if "endswitch" in line or "}"  in line:
			tabdepth= line.count("\t")
			end_coffee_switches.append(counter)
			endswitchtabs.append(tabdepth)
			counter += 1
		else:
			counter += 1
	#=====================================
	counter =0
	for item in coffee_switches:
		combinedlist.append("[" + str(coffee_switches[counter]) + "," + str(end_coffee_switches[counter]) + "]")
		counter += 1

	print("zzzz the result list =",combinedlist)
	print("switch tabs=",switchtabs)
	print("endswitchtabs =",endswitchtabs)
	

print("testing this using string red_robin to see if it works")
print("this is only returning the range list of the switch endswitch pairs")	
print("GO GO GO what that dog go")
#mr_coffee_smart_skipping_lines(red_robin2)
## it's chopping off this from the bottom
'''
fallthru
		
		default:
			print('the end')
}
'''
print("TESTING SKIPPING LINES 16 THRU 38 IN RED ROBIN")
print("testing skipping nested switch in red robin")
print("today is thursday sept 30th...")
print("testing...... sept 30 skipping 16 thru 38")

#So loop thru string and 
#get line number with # and 15 put into start
#and get line number with
 # and #38 and put into finish
print("watching videos of starship. video time...")
print('length of nest_string',len(nest_string))
print("nest_string[1]) see if it works..") 
print(nest_string[0])
print("===============")
print(nest_string[1])
print("===============")
print(nest_string[2])
print("===============")
print(nest_string[3])
print("===============")
print(nest_string[4])
print("===============")
#print(nest_string[5])
#print("===============")

print("bottom after examining nest_string jazz")
start = 15
finish = 38
skipping_some_lines(red_robin,start,finish)
#see if the string is in ibm[0]
print('go for it 1')
#this is the lower section of the main switch now
print("and now we start phase 2 -====")
start  = 53-23 #subtract number after first cutting out skipping
finish = 65-23

skipping_some_lines(ibm[0],start,finish)
print("======= I have all of the code I need to make this miracle happen")
print("=====practicing cutting out inner switch guts leaving inner switch word==")
#
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
#now the string we have is missing the numbers above it 
print(nest_string[2])
start  = 10 #subtract number after first cutting out skipping
finish = 19
skipping_some_lines(nest_string[2],start,finish)

print(toosmart[0])
#this changes the contents of nest_string[2] #see if this puppy works
nest_string[2] = toosmart[0]
print("what does this string look like right now this instant")
print(nest_string[2])


#53 -65
print('go for it 2')
##########################################################################################
print("TESTING skipping_some_lines(ibm[0],skip_range[0],skip_range[1]")
print("10 thru 20 but keeping the first line on 10 which is switch")
print("then 28 thru 38 keeping first line on 28 which is switch")
print("well, how did it go ")
print(" skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip ")
print("=====")
print("==========")
print("================")
print("======================")

#this would be done separately and is filling the range_list with the switch to endswitch params
#this will be a separate method for range input for the switch endswitches
#here the sublists of the param of each nested switch are added to range_list
#this is hard coded here filling the nested switch numbers 


#range_list=[[10,20],28,38]]  #that's right I do this backwards from bottom up!!!

'''
this goes thru the main switch string and makes a copy
of the main string in stages copying the whole thing
except for the range for each nested switch.
'''
## this means delete nested switches bodies except leave inner switch word only
##===================================================
#  REDUCE MAIN NESTED SWITCHES TO JUST SWITCH WORD
# debugged on august 5th 2021 gilroy starbucks
##===================================================
## this makes teh final main switch with the inner switch bodies stripped out
## just leaving the switch word where the nested switch was.
#range_list.append([10,20]) #these are added in order and then reversed
 # so that the nested switches are erased bottom up
addthis=[]
addthis.append([10,20])
addthis.append([28,38])
##========================
## add_to_range_list()
##========================
def add_to_range_list(): #uses addthis list 
    print("add_to_range_list() this is necessary to work")
    for item in addthis:
        range_list.append(item) #adding to range list
        
    print("length of range list =",len(range_list))
 
 
 
 #i will need to add data to range list still 
##======================
##  feed_range_list()
##======================
def feed_range_list():
    print("=========feed_range_list() called=====>>>")
    print("=========feed_range_list() called=====>>>")
    range_list.append([11,24]) 
    range_list.append([26,38])
    print('range_list=',range_list)
    #the list has to be REVERSED to do the changes bottom up so the line numbers work correctly
    range_list.reverse()#reverses it NOTICE WE REVERS THE LIST TO CHANGE IT BOTTOM UP
    #this is so the bottom is done first 
    print("length of range list =",len(range_list))


    
#Yes I am reversing the range_list to do the changes bottom up so they don't lose their place
print('printing the range_list')
print(range_list) #should be [28,38],[10,20] to do from the bottom up

#this takes out the inner switches except for the switch word
#so what this means is it removes the body of the nested switch but leaves just switch word.
### this uses range_list!!!!!!!!!!!!!!!!!
#between 11 and 47
#if first switch detected keep going so use switch counter
#it needs to only include the switch word of tab depth 3 switches
#before doing any changes it looks like this 
REAL_STRING='''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			####################
			switch(exp){ # 15  #second level deep  (( 5 tabs ))depth 3 detector       Level 2    
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################==== this one should be deleted 
			switch(exp){ #23  #third level deep  (( 7 tabs ))   Level 3    =====
				case 'tahoe':=========
			print("do something")=======
			print("yep")
			fallthru
				case 'fallen leaf lake':
			print("nice")
			break
				default:
			print("we are done here")
			endswitch #33
			#############
			break
		default:
			print("we are done here")
			endswitch #38==========
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47
			exp = 3  #note that this switch is stacked below the bottom stack at 3 tabs
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
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
			endswitch #73
'''
'''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			####################
			switch(exp){ # 15  #second level deep          Level 2    
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					break
				default:
					print("we are done here")
			} #38
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #47
'''
	
#after changes it should look like this after getting rid of inner switch body one indentation

#this is what the end result should be
endresultshouldbe='''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			switch(exp){ # 15  #second level deep          Level 2    
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #47
'''
	

#I think that I need to go thru tab length3 first 
#then go thru tab length 5 
#then go thru tab length 7
#this is the input for the reduce_main_nested_switches_to_just_switch_word(

oldschool='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					#################### del after line with '#' and  '15' in it till 38 in it
					switch(exp){ #15
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			exp = 3  
			switch(exp){ #26
				case 'burger':
					print("do something")
					####################
					switch(exp){ #30
					print("gosh")
					fallthru
				case 'porsche':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
} #51
'''
#the output should be
'''
	switch(exp){
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #====
			exp = 3  
			switch(exp){ #====
			##############
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


starbucks_code_main_test ='''
	switch(exp) { #main 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					break
				case 'please work':
					print('nice')
					fallthru
			endswitch	 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	


#The change that I need to make here is to cut out switches greater than 3 tabs  tabdepth > 3
##======================================================
##   reduce_main_nested_switches_to_just_switch_word():  #I think that this does all switches no matter their depth
##=======================================================
def reduce_main_nested_switches_to_just_switch_word(astring): #11 - 23 and 25-37
    print("starting this method to see what is in the string")
    #for line in astring.splitlines():
    #    print(line)
    print("===reduce_main_nested_switches_to_just_switch_word()== Tron approaches")
    print("C3Po")
    print("=====reduce_main_nested_switches_to_just_switch_word()====0000000000000==>>")
    print("=====reduce_main_nested_switches_to_just_switch_word()======>>")
    print("=====reduce_main_nested_switches_to_just_switch_word()======>>")
    print("what is in astring the input param")
    print(astring)
    print("end of the input string to see what is going into the function")
    print("reduce main nested switches to just switch word()")
    
    #feeding range list()
    #add_to_range_list() #this is new to put switch and endswitch lines into range_list
    feed_range_list() #added on wednesday, September 15th, 2021
    flag_test[0]== False #this flag is new this is the default setting for this flag
    print("flag_test[0]=",flag_test[0])
    #when flag_test[0] = True that means it's doing 2nd and subsequent loops (changes) and use baton[0] for concatting string
    print("==reduce_main_nested_switches_to_just_switch_word(astring)==")
    print("= R2D2 ==## $$ ## == reduce main nested switches to just switch word()==========")
    print("this cuts out the nested switches bodies leaving just the word switch")
    print("starting ibm[0] with samplestring")
    print("what we are starting with for input in ibm[0]")
    #print(ibm[0])  #the key is the range_list
    print('range_list=',range_list)  ### this is the dependency the range_list necessary for this to work
    #loop thru range_list
    print("we loop thru the range_list here")
    print("let's see what RADAR is in the range_list",range_list) #see if it's reversed or not
    #loops thru range_list with pairs of switch end and endswitch
    print("length of range_list of pairs=",len(range_list))
    print("range_list=",range_list)
    counter=0
    # loop thru range_list
    print("before starting let's look into the range_list",range_list)
    print("============")
    print("perhaps I need to go thru the 7th tab first, then 5th tab, then 3rd tab")
    print("thinking outloud how to do this.")
    print("range_list=",range_list) #just added this sept 30 2021 testing cafe borrone
    
    for item in range_list: ##range_list=[[10,20],28,38]] ==========================
        print("**",item, item[0],item[1])
        print("inside of loop thru range_list :: COUNTER HERE=",counter)
        skip_range[0]= item[0]; 
        skip_range[1]= item[1]
        #item[0]='',item[1]=''
       # print(item[0],item[1])
        print("skip_range=",skip_range)
        #this builds a new string by skipping the nested switch sections
        #but leaves the inner switch (switch(x) word intact
        # skipping_some_lines() called here 
        # ibm[0] has the samplestring in it from above
        toosmart[0]=astring #this might work
        #this is called before skipping some lines
        #the problem is that on the secondpass it's not taking in the changed toosmart[0]
        #====================================
        #SKIPPING SOME LINES()===============
        #====================================
        #this is governed by flag_test[0] which is set to default False above the loop
        skipping_some_lines(astring,skip_range[0],skip_range[1]) #this makes a new string skipping guts of inner switch
        counter += 1
        
        #skip_range[0]='';skip_range[1] ='' #just added this to see if it helps
        #del skip_range[:] #this clear it out afterwords to wipe the slate clean
    print("this is the final output of the transformation halloween approaches")
    print("output of = R2D2 == taking inner nested switches body out and putting just keeping swithc word")
    print("the star destroyer was moving fast")
    print("should be only two nested switches and only switch word remaining NOT 3")
    print("end of this picture show")
    #print(ibm[0]) #this prints out the result 
    print("=====================")
##======================================================

#here we go  
print("the goofy dog test")  
print('we start with this string')

#print(ibm[0])
print("OLYMPICS BLAZING... gold medal time")
print("=====calling reduce main nested switches to just switch word(========)")
print("HERE NOW...this should be the sample string with the nested switches")
print(" cut out leaving just switch word")
print("we are ==== STARTING ==== with this dam string legal eagle")
#bypass here on thursday sept 30 testing at cafe borrone
#print("September 30th testing at cafe borrone")
#ibm[0] = red_robin
print(ibm[0])
inputnowstring= ibm[0]
print("starting input before doing changes")
print(inputnowstring)
print("about to reduce main nested swithces to just switch word which work previously without incident")
print("line numbe 4162")
print(" FIRE BREATHING DRAGON NOW ")
#flag_test[0]== False #see if this works 
# I am right here today  LOOK RIGHT HERE OCTOBER 1ST 2021 
## this is the key method here ====

reduce_main_nested_switches_to_just_switch_word(oldschool) # I didn't notice this way down here
print("red alert test 2 reduce main nestd swith to switch word test 2 ...")


print("good times saturday night live test ")
del range_list[:]
reduce_main_nested_switches_to_just_switch_word(starbucks_code_main_test)
print("look above frosty snowman here")
print("output from taking out nested switches in string inputnowstring")
print("output of removing both nested switches")
print("RIGHT HERE ====== OCTOBEr 1st what does this look like below this line")
print(ibm[0])
print("does it loop thru two times for that is how many times it should")
print("==============")
#exit()



print("this is what the main switch looks like after having taken out the inner switch bodies")
print("which means that we should only have the inner switch words remaining and nothing else")
print('super super major major critical test 4129 line number ')
print("this shoudl be the main switch with only remaining switch(exp){ and no inner switch bodies")
print("here we should have the two nested switches remaining with no bodies")
print("mocha at starbucks")
#print(ibm[0])
# print this skips the nested switch body and creates a different version of the main switch
# and takes out the nested switches but leaves the switch word
print('after the olympics end...')
print("stopping it here because it should have worked...")
print("remember that I am using and EXIT() here to stop the code running past what I am concentrating on")

#exit()  






#print(ibm[0])
print(" starting anew here doing it the old way")
ibm.append(samplestring) #in ibm[0]
print(ibm[0])
print("that's all lemon tree software ==")
print("about to exit the program after seeing the nested switches taken out of main string")
#exit()
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/ ghostly  /=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("this is the SECOND ATTEMPT")
#skip_range.append(0)
#skip_range.append(0)
print("does this work yet") #these are farther down  so I needto do them first 
skip_range[0] =11
skip_range[1] =24
print("=============")
print("skip_range=",skip_range)
print("=============")
print("====::::::::: after changing bottom nested switch to just switch word ::::::===")
print("====::::::::: after changing bottom nested switch to just switch word ::::::===")
print("what string is in ibm[0]=",ibm[0])
ibm[0]=oldschool
for line in ibm[0].splitlines():
    print(line)
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 28,38 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print("now swap out the top inner switch hopefully")
print("ibm[0]=",ibm[0])
skip_range[0] =10
skip_range[1] =20
print("=============")
print("skip_range=",skip_range)
print("=============")

skipping_some_lines(ibm[0],skip_range[0],skip_range[1])

#exit()

'''
skip_range[0] =10
skip_range[1] =20
print("=============")
print("skip_range=",skip_range)
print("=============")
skipping_some_lines(ibm[0],skip_range[0],skip_range[1]) 
'''

#print(ibm[0])
#fuse=[]
#fuse.append(0)

#del skip_range[:]

#skip_range.append(10)
#skip_range.append(20)

#I guess I can put the ranges into a list and then reverse it and 
#loop thru it.
print('at this juncture what is in ibm[0]')
print(ibm[0])
print("starting out we have this before stripping out the nested switches")
#ibm[0] = fuse[0] #to preserve changes made 
print("input values on 2nd pass =")
skip_range[0] =10
skip_range[1] =20
print(ibm[0])
print(skip_range[0])
print(skip_range[1])
print("========")
print("skip_range=",skip_range)
print("=========")

print('==== make it dam happen == ')
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 10,20 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print(ibm[0])
print(" where is it now lemonade stand ???")
del skip_range[:] #this has to be cleared out. 
#skip range needs to be cleared out for the next nest parameters here
##===============================
print("==== the end===both nested switches should only have the switch word reminaing ===")



print("===end of copying a string and skipping lines 10 thru 20===")   
print("in ibm[0] we have",ibm[0])
print("===== this is after running skipping_some_lines(smaplestring,10,20)")
print("===========")

smart_number=[]
smart_number.append('starter')
smart_number.append(0)
smart_number.append(0)
smart_number[1] = '1'
smart_number[2] = '2'
#switch is on line 10 need to change it this is looking for the switch

#this is changing ALL OCCURENCES of switch at the 
#same time just just the one I want it to change.
# I need to localize is it to one line number.

#have it change one and then break starting on the line above


#The problem I have is if I replace each switch with the nested numbers
#then the other code won't work so perhaps I need to add a comment
#the issue is making the main strings which should only have the first level inner switches
#which is governed by tab depth of 5 representing the second level
# since tab level 3 is the first main switch.
# I could do number 1 thru n for each level initally and then change them
# or I came up with the number top down 1 thru n but level list solves the problem 
#That was my genius

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#in terms of faster programming it's about communication and control
# the lollipop is the what level but above that are higher abstraction levels
# where yet more speed can be achieved and sustained
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========
#I think I will do the one nest level for now and add the other nest levels afterwords
#decision made august 22nd, 2021 9:08 am

# I have the main module which has nested methods
# I can use this for making nested switches with nested switch methods too
# but right now I want to get the nested feature working before implimenting it
#######3==================================
#Actually I can do the main and the nested that have inner switch words not changed yet
#And then apply the conversion to numbered switches
##=====================
''' from above just pasted it here to keep track of its contents
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,86], # I can make these now 
  "2": [11,47],
  "3": [15,38],
  "4": [23,33],
  "5": [49,73],
  "6": [53,64]
 #no comma after last data piece apparently
}
'''

danumber=''

#testing this here to make sure that it's right 
ibm[0] = '' #this should delete it
print("ibm length=",len(ibm))
stringname =teststring60
print('starting stage of string to manipulate')
for line in teststring60.splitlines():
    print(line)
danumber= 66

print("star wars begins now.")
##============================================
# swap_switch_for_nest_method_new(danumber)
#// inner switch(just the words) is swapped for nested method number")
#=============================================
#for this to work correctly I need to ahve already taken out the inner switch bodies that I copied
print("about to do OPTIMUS PRIME === GO BABY GO ===")
def swap_switch_for_nest_method_new(stringname,danumber): # I will add more values later perhaps 3 or 4 for coordinates
	print("#### ========= swap switch for nest method new  ========####")
	print(" =======OPTIMUS Prime======")
	global abovenestedswitch
	#stringname=ibm[0]
	#stringname=ibm[0] #loading from ibm[0] good
	print("called swap_switch_for_nest_method(n)")
	print("it is using this number in use_number[0]",use_number[0])
	acounter=0
	for line in stringname.splitlines(): #determine if "endswitch" is in line
		tabdepth = line.count("\t")
		print("the current tab depth in THIS line is",tabdepth)
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20 check to make sure that switch and the comment line number in this line
		#this way it can ONLY make changes to switches at tab depth 3
		if tabdepth == 3: #this way it can ONLY access changing the string at 3 depth once
			#this way only if the tab depth is 3 can it manipulate the string
			if  "switch" in line and str(danumber) in line: #line with switch in it  
				print(line)  #doing counter > 1 so it doesn't do the first line
				#this is where the string is changed
				stringname = stringname.replace("switch(exp){","nested_switch_" +str(danumber)  + "(n)")
				break
			else:
				acounter += 1
				continue
		else:
			acounter += 1
			continue
			
	print("the final outcome of the chagne is here:")
	for line in stringname.splitlines():
		print(line)
	

# this takes in what is in ibm[0] and the outputs it to ibm[0] also, quite clever.   
print("let the judge state this is truth") 
number_to_add=66 
swap_switch_for_nest_method_new(teststring60,number_to_add) 
ibm[0] = stringname
print(ibm[0]) 

#where is th eone that grabs teh number automatically though

da='''
	switch(exp){ # 15
		case "1":
			print('hi')
			switch(exp) #       22
			#isn't this special
			print('is this happening')
			switch(exp) #      36
			print("what do we have here")
        
'''

data1='''
	switch(exp){ # 15
		case "1":
			print('hi')
			#isn't this special
			print('is this happening')
			print("what do we have here")
			break
'''

data2='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''

#the innerswitch must be at 3 tabs and the first top switch must be at 1 tab.
data3='''
	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			switch(exp) #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''


jazz6='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #63  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #89  
			#############
			break
		case 'what':
			print("nice")
			####################
			switch(exp){ #455  
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''

jazz7='''
	switch(exp){ #1      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 
		default:
			print("we are done here")
	endswitch #this is key here 
'''
#replace_the_last_endswitch_with_brace
print("I found the code I need - I think - we shall see - if it is the right code indeed")

print("about to do thorough testing of chnage_switch_to_method_solved()")
#solved october 29th, 2021  NEXT get the number after comment just in time
'''
this builds a string called newstring replacing switches
at 3 tabs depth with nested_switch
with the comment id after # tacked onto
 the end of the nested_switch_22(exp) like so.
'''

   ##################################################            
       # if "}" in inputstring:  #have to cut "}" out of string      
       #     print("CONFIRMED there is a right brace in string")
       #     for line in templine.splitlines():
       #         if "}" in line:
       #             
       #              templine2 += line.replace("}","")
       #              templine2  +="\n" 
       #        else:
       #             templine2 += line +"\n"
       #    inputstring = templine2
       #     print("======testing if } taken out of string======")
       #    for line in inputstring.splitlines():
       #        print(line)
       #     print("======testing if } taken out of string======")
         #end if   
       # do nothing
       ######================================
       
''' ##################################################            
        if "}" in inputstring:  #have to cut "}" out of string      
            print("CONFIRMED there is a right brace in string")
            for line in templine.splitlines():
                if "}" in line:
                     templine2 += line.replace("}","") #this is where I was taking } out
                     templine2  +="\n"
                else:
                     templine2 += line +"\n"
            inputstring = templine2
            print("======testing if } taken out of string======")
            for line in inputstring.splitlines():
               print(line)
            print("======testing if } taken out of string======")
         #end if 
'''
        ########################################


innerswitchstatus=[]
innerswitchstatus.append(0)

castle1=[]
castle1.append(0)
##===================================================
## change_switch_to_method_solved(inputstring):
##====================================================
print("make the coffee magic coding happen working on this today charlie brown") 
#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    innerswitchstatus[0]= False #by default
    print("====== change_switch_to_method_solved(inputstring)=== get the money now====")
    print('this now takes out the { brace after switch if it is there')
    innerswitch=''
    print("this is what it sees when it starts change_switch_to_method_solved()")
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default setting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitchstatus[0]= True #this is new 
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    if innerswitch == False:
        print("this switch string DOESN'T HAVE an inner switch")
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    
    #### IF INNERSWITCH == TRUE:
    if innerswitch == True: #if a switch at 3 tabs depth  is True
    #check if { in this string if so take it out
        print('checking if left brace in string')
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine  +=   line.replace("{","") 
                    templine  +="\n"
                else:
                    templine += line +"\n"
            inputstring = templine
        #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
       #check if } in this string an if so take it out
      
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():#      getting tab depth
            tabdepth = line.count("\t") #gets tab count for this line
            #skips first switch by counter MUST BE AFTER 2nd line
            #this is where we swap switch(exp) with nested_switch_(number)(exp)
            if "switch" in line and tabdepth == 3 and "end" not in line and counter > 2: 
                print("confirmed switchh in line and tabdepth3")
                #this is new getting the switch id number after # on-the-fly
                #get string to right of #, get right side,remove spaces
                x = line.split("#"); y = x[1];y = y.strip();
                # replace switch with nested_switch + id number harvested from comment above
                thisline = line.replace("switch(exp)", "nested_switch_" + str(y) + "(exp)")
                #this removes the extra spaces after #
                location = thisline.index("#")    #gets location from left where position of #
                thisline = thisline[:location]    #this slices off the right side from # position
                thisline = thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else: #this MEANS NO INNER SWITCH IN THE INPUT STRING
        print("no inner switches in this string")
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine += line.replace("{","") #taking out left brace here
                    templine  +="\n"
                else:
                    templine += line +"\n"           #otherwise it doesn't replace anything 
            inputstring = templine
        else:
            print("=====no { in string  ======")
            #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
        #check if } in this string an if so take it out #I have deactivated this since it's not needed
        
        #this is what we return the inputstring
        return inputstring; #no changes made 
        castle1[0] =inputstring 
        innerswitchstatus[0] = False
    ### end of function =======================================================
    
print("where is my mocha brainfreeze test october 30th...")




print("==========testing string da===================")
print("=============================")
inputstring=''
inputstring = da         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
print("end of red alert change switch to method solved end of test 5..")    
print("=============================")
print("======= testing string data1======================")
 
print("testing goldfish which is NOT indented yet")
#testing a second method in chain right now for expiermentinting==
#the input string MUST BE indented and look like this LOOK LIKE THIS 
somedata2='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''


gofigureit='''
	switch(exp){ #77
		case 'burger':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is chnaged to brace later
'''



#just check if switch at 3 tabs to determine if nested switch
#monday dec 6th thinking 
####$#$$##############========================


            
            
check_if_nested_switch_inside_this_switch(somedata2)
print("inner switch in switch=",table[0] )
print("=======")
print("=========")

check_if_nested_switch_inside_this_switch(gofigureit)
print("inner switch in switch=",table[0] )
#exit()


print("wasn't that fun")
######======================================
# november 20th saturday just after 10am Morgan Hill 2021
inputstring=''
inputstring = goldfish    
    
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
   
print("see if this worked with goldfish accurately")
#exit()
    
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data1         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
    
print("=============================")
print("========testing string data2=====================")


inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data2     
#what I am doing here is returning the concatted string to the string fizz variable.    
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

##==================
print("about to test data3 and I can't have anything after the #22 after switch")
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data3         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

print("massive mammoth test here to see if mocha is ready")
print("does many changes from switch to nested switch with number ==testing jazz SIXAROO now jazz6 ")
inputstring = jazz6
print("testing jazz6")
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)



print("massive mammoth test here to see if mocha is ready")
print("does many changes from switch to nested switch with number ==testing jazz SIXAROO now jazz6 ")
inputstring = jazz7
print("testing jazz7")
print("calling method  change_switch_to_method_solved")
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

#exit()


###================== cold brew linus and snoopy ================== saturday morning software  november 20th, 2021 ====
#this is testing adding the nested switch 
linus_and_snoopy=[]
##==================================
##   add_nested_switch_methods():
##==================================
def add_nested_switch_methods():
    print("add nested_switch_methods() in catching_first_change list")
    for item in catching_first_change: #<== list with strings after taking out inner switch bodies
        #print(item)
        #here calling method chaning_switch_to_method_solved swaps switch for nested_method_numbered
        fizz =change_switch_to_method_solved(item)#this is applying the method to add nested_switch method
        print("===== oh yeah =====")
        linus_and_snoopy.append(fizz) #this is adding the changed string to linus_and_snoopy list
        
        #for line in fizz.splitlines():
        #    print(line)



##================================================
##print_out_result_of_adding_nested_switch() to each switch string:
##================================================
def print_out_result_of_adding_nested_switch():
    counter =1
    print('we made it to the top of the Donnor Summit ')
    for item in linus_and_snoopy:
        print("counter=",counter)
        for line in item.splitlines():
            print(line)
        counter +=1

print("here we go... let her rip")       
add_nested_switch_methods()
print_out_result_of_adding_nested_switch()
print('end of the show time movie trailer')



#test with one string and do piping

#cut_out_inner_switch_body_leaving_switch_word(teststring)
##===========================================================================
##  cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
#def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
#    print('this one is sooo critical')
#    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
#    skipping_some_lines(stringname,start,finish)
#    #this means that the output string should be placed into never_defeated[0]
#    for line in never_defeated[0].splitlines():
#        print(line)

inputlist=[]
inputlist.append(0)
outputlist=[]
outputlist.append(0)
 
print("this is a super critical test of piping two chain methods in sequence")
print("SUPER CRITICAL PIPING METHODS CHAINING TEST ===")
           
#put x in front so it's not used
#it must be indented properly to work daaaaa
xskitahoe ='''
		switch(exp){   #1 === line 10 beginning of single nested switch ======      
			case 'blable':
				print("do something")
				print("yep")
				fallthru
			case 'more':
				switch(exp) #7
					case 'funny':
						print('fun')
					case "da":
						print('yeah')
					default:
						print('bye')
				endswitch #14
				print("nicely")
				break
			default:
				print("we are done here")
		endswitch #this is key here =============line 20 end of nested switch ====
'''	


#testing 
print("testing printing out joy string")
joy='''
	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp) #23
			#############
			break
		default:
			print("we are done here")
	endswitch #38
'''

hotmocha='''
	switch(exp) #3
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #11
			exp = 32
			switch(exp){ #62
			#############
			break
		default:
			print("we are done here")
	endswitch #86
'''

for line in joy.splitlines():
    print(line)



#testing doing 2 methods back to back piping output from first to input to second
#first method   
###==================
##  do_the_pipe()
###==================    
def do_the_pipe():
    print("do the pipe() called pipe pipe PIPE PIPE PIPE")
    print("outputlist[0]=",outputlist[0])
    inputlist[0] = outputlist[0]
    print("now put it into inputlist[0]")
    print("inputlist[0]=",inputlist[0])
    
    

print('doing some pipe testing today')

#######################################
#######################################
#######################################
###====== saturday morning codeing ==november 20th, 2021 testing this puppy ====
## SHIFT NEST STRING TO LEFT INDENT THE PUPPY
print("this is doing shift nest string to left() ======")
print("=====================================================")

shift_nest_string_to_left(xskitahoe)   
resultis =fishbowl[0] 
print("this is after shifting input string to the left to be one tab in front")
print("of the top switch") 
for line in resultis.splitlines():
    print(line)
    
 #this is technically the output which we will now put into inputlist
inputlist[0] = fishbowl[0]   
print("this is testing cutting out switch body from a string")
stringname=xskitahoe; start=7; finish = 14; #this sucker was moving...
print("let us see what is in skitahoe string first")
for line in xskitahoe.splitlines():
    print(line)
print("done with input string to see the starting point")
################################################
#################################################
##  CUT OUT INNER SWITCH BODY LEAVING SWITH WORD
#this one does not work (november 28th this is the hold one)so don't worrya bout it it works elsewhere got it working
# skipping rope yesterday.


cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
outputstring=string_after_cutting_out_inner_switch_body[0]
print('after stage 1 first method call in chain we have this result')
for line in outputstring.splitlines():
    print(line)
print("end of first change to string")
outputlist[0] = outputstring
print("right here this is  after taking out th einner switch body")
#MUST INDENT LEFT 
do_the_pipe()
#print("do the pipe() called")
#item = inputlist[0]

#second method
print("experimenting with joy string simple convert to removing inner switch")
print("and adding a nested method nubered")
print("calling first method")
#this is what I am testing Sunday november 28th, 2021 3:51pm take 101 north instead next time

print("testing a method on change switch to numberedmethod with joy")
print("testing  change_switch_to_method_solved()")
print('================ this is the one ===============go for the gold now==================')
print('==================that I need to work now ===============================')
print('===== this changes an inner switch by itself into a nested_switch numbered============================================')
print('=======using the commented number next to it==================')
print(" === I am at starbucks next to frosty the snowman")
fizz =change_switch_to_method_solved(joy)#

print("========the result of 1 chain method using piping=======")
for line in fizz.splitlines():
    print(line)
outputlist[0] = fizz #just for testing here 

print("testing hotmocha now changing two nested switches into nested methods")
fizz =change_switch_to_method_solved(hotmocha)# testing 2 switches to change

print("========the result of 1 chain method using piping=======")
for line in fizz.splitlines():
    print(line)
outputlist[0] = fizz #j
print("end of the show, turn out the exit lights")
#exit()
print("line 11259")

do_the_pipe()
#list strings are mutable changeable. 
inputlist[0]=inputlist[0].replace("nested","mocha")
print("see if it sticks")
print("just called the pipe()")
print("now it whould be input[0]")
for line in inputlist[0].splitlines():
    print(line)
#`exit()

print("testing taking out endswitch at bottom of function and swapping it with a brace like in C")
## I am doing this because this is how the parser works so it conforms with JavaScript and C style.
print("TESTING it is already November taking out endswitch and putting in a brace at bottom of function")
#focus=take_out_endswitch(fizz)
#for line in focus.splitlines():#
#	print(line)
###=====================================================================================

#next need to swap endswitch to } (right brace)

#exit()


#playing with this
makeitso= '''
switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #86   
'''

newattempt='''
	switch(exp){ # 15
		case "1":
			print('hi')
			switch(exp) #       22
			#isn't this special
			print('is this happening')
			switch(exp) #      36
			print("what do we have here")
'''

##============================================
## get_top_switch_number_from_this_string(x)
##============================================
twinlist=[]
#testing with string directly above this line
def get_top_switch_number_from_this_string(inputstring):
    print("get_top_switch_number_from_this_string")
    print("there is NO REASON to send humans to Mars")
    counter=0
    x= y =''
    for line in inputstring.splitlines(): #it will be the first switch 06
        if "switch" in line and "#" in line and "nested" not in line  and counter < 2: 
            print("confirmed switchh in line ")
            #this is new getting the switch id number after # on-the-fly
            #get string to right of #, get right side,remove spaces
            x = line.split("#"); y = x[1];y = y.strip();
            print("no drama this is what we have..")
            print("y=",y)
            print("now adding y to twinlist below")
            twinlist.append(y)
            break
        else:
            if counter > 3: #time to bail =too deep can't exist after first line actually
                break
            else:
                continue
                counter += 1
#grab first id number aftger switch 

inputstring =makeitso
get_top_switch_number_from_this_string(inputstring)
print('in twinlist we have',twinlist)

inputstring =newattempt
get_top_switch_number_from_this_string(inputstring)
print('in twinlist we have',twinlist)









print(" ")
print("====end of show here turn the lights out====")
#exit()  #<<<<<<=================== this is where our exit is.


print("== end of show ==== ")
#exit()
string_egg='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #60 
'''


string_egg2='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #33 
			#############
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''


pumpkins='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			switch(exp){ #25
			#############
			print("yep")
			fallthru
		case 'more':
			switch(exp){ #34
			print("nice")
			switch(exp){ #45
			break
		default:
			switch(exp){ #66
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

brew='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			switch(exp){ #25
			#############
			print("yep")
			fallthru
		case 'more':
			
			print("nice")
			####################
			switch(exp){ #35
			#############
			print("yep")
			fallthru
			break
		default:
			
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

brew1='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			
			#############
			print("yep")
			fallthru
		case 'more':
			
			print("nice")
			
			break
		default:
			
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

#add ability to get the comment number 15 and put that in automatically 
##=======================
##  funtime(y,x)
##=======================
# this is replacing the switch that is nested into 
# a method with the switch number

#building blocks are legos that are small behaviors inside
#of a function that can be assembled and connected in different
#configurations to make new functions without coding
#so interactively combined with a gui
#so chained methods really




#=====================================
# get inner switch number ()  only at the 3 tabs level depth though
#======================================
#so do this multiple times I would have to go thru a loop with the length of the count of switches at three tabs in a string
add_to_list=[]#and call this method get_inner_switch_number(stringname) #and change the counter number
thisline=[] #this also implies only getting one inner switch
def get_inner_switch_number(stringname): #implies at 3 tabs depth
	print("======get inner switch number called=======")
	counter=0
	x=''
	#what this does is get the commented inner switch number after the # in switch
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tabdepth=line.count("\t")      #this is getting tabdepth for this line
		if "switch" in line and "end" not in line and tabdepth== 3:#and "#" in line and counter > 1: #just need to grab the first switch 
			x = line.split("#")  #this manipulates the current line
			y = x[1];
			print("switch number is...",y) 
			add_to_list.append(y)
			counter += 1
			print(stringname)
			#break  #after the if condition above it stops 
		else:
			counter += 1
	print("List add_to_list=",add_to_list)
	#del add_to_list[0] #should delete first one
	print('now we have ',add_to_list)
	#return y;


##===================================
##  funtime(stringname)
## this calls the method get_inner_switch_number()
##===================================
## this replaces the inners switch at 3 tabs with a netsed method name with the id comment number
#this right now only deals with one but I can modify it so that
#modified this and got it working correctly on friday, oct 22nd morgan hill 2021
print("I just don't believe I coded this back on oct 22nd")
print("morgan hill starbucks frosty74")
#===========================================================================
#  convert_inner_switches_into_nested_methods_numbered(stringname): 
#============================================================================
# it will access a list using a loop and they will be put in in sequential order top down
def convert_inner_switches_into_nested_methods_numbered(stringname): #this is feeding in the number looking for
	print("======convert_inner_switches_into_nested_methods_numbered=====")
	x='';concatthis='';counter =0
	# using method get_inner_switch_number(string)#which is grabbed from 3 tab depth only
	for line in stringname.splitlines():
		print(line)
	#modified this and got it working correctly on friday, oct 22nd morgan hill 2021
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if  tabdepth == 3  and "switch" in line:
		# I just moved what was in a method into the loop where the action happens
			x = line.split("#")  
			y = x[1];       #it was str(ournumber)
			y = y.replace(" ",'')
			filler ="nested_switch_" + str(y) +"(exp)" #has to be a string
			#### this is new december 5th #######
			print("inside of function convert_inner_switches_into_nested_methods_numbered")
			print("###====line 11729 ===========##")
			print("filler=",filler)
			if ":" in filler:
			    filler=filler.replace(":","")
			#end if
			print("after fix  -- filler=",filler)
			print("###===============##")
			######################################
			line = line.replace("switch(exp){",filler) #notice replace using var 
			concatthis += line + "\n"
			counter += 1
			continue
		else:
			concatthis += line  + "\n"
			counter += 1
			continue
	################	
	for line in concatthis.splitlines():
		print(line)	
		

print("testing this")
print("convert inner switches without bodies inot nested methods numbered")
convert_inner_switches_into_nested_methods_numbered(brew) #line number of inner switch is in thisline[0]
#exit()

#def plan_c(inputstring):


#so we wouldn't need to enter the 5 we an glean that
#and we don't need to know the 15 number either it will grab it
print('======= end of funtime code ==============')
print("now testing with 2 inner switches to change")
print("oasis in the desert -----")
#this is the one that we are playing with
print('=====those headlights are awefully bright - rude and dumb=====')
convert_inner_switches_into_nested_methods_numbered(string_egg2)
print('pumpkin express')
convert_inner_switches_into_nested_methods_numbered(pumpkins)

#try none and try one
convert_inner_switches_into_nested_methods_numbered(brew)
	
convert_inner_switches_into_nested_methods_numbered(brew1)

#exit()
# I think that I will go through a string and 
# return a list of the locations of switches 
# (skipping the first switch)
# switch and endswitch line numbers
# was just thinking that it's obviously a switch otherwise
# we wouldn't be here so NO NUMBER for main switch (brilliant)
#it still matters but it's obvious that it is there. It's actually
# the main switch and the frame for nested switches. 

ibm[0]=tuna #input of string into ibm[0]
list_of_nested_switches=[]
list_of_nested_switches.append(12) #these are just the line numbers here 12 and 32 
list_of_nested_switches.append(32)

#here I am using a list which has the line numbers of the inner switches locations
print(list_of_nested_switches)  #so it would look like this 
#this goes through the input main switch and changes nested "switch" into a nested_switch numbered

#this is used for managing the nested switches by getting their location to know
#where to copy them when extracting them from a main switch
# today is july 17th, 2021 9:33 am

print('testing this to make list of all switch locations and all endswitch locations')
print(tuna)
switch_location=[]
endswitch_location=[]
print("beginning === put location of switch and endswitch into lists")
print("====---------------------- saturday coding ----------===")

ourcounter=0
#for line in abovenestedswitch.splitlines(): 
for line in tuna.splitlines():
    
    if line.startswith("switch"):
        print("this lines starts with switch")
        switch_location.append(ourcounter)
    
    
    if line.startswith("endswitch"):
        print("this line starts with endswitch")
        endswitch_location.append(ourcounter)
        
    ourcounter += 1
        
print("====OUTPUT TO DETERMINE location of each switch and endswitch====")
print("")
print("switch_location=",switch_location)
print("endswitch_location=",endswitch_location)
print("")
print("===make your dreams reality===")
        



# july 24th, 2021 
#the input for this MUST be the already reduced main switch which
# has just the switch word in place where each nested switch thru endswitch was.


###  Thursday, August 19th, 2021 time 9:07 am
# I think that I just need to not worry about the other nested switches
# and just do the first level of nested switch since the others will just be in the other switches
# so let' say I have two nested switches deep
# I only have to have (for the main switch) the first level nestedswitch
# so then the situation becomes the numbering because in this first level of nested switches
# they would be numbered in sequence 1, 2, 3 etc  
# if say there are two nested in teh first main swith then sub1
# but for the inner levels (the next tab level) I would have to do 4,5,6 I suppose
# so continuing sequence or 1.1 and so forth
# I need to come up with a simple numbering system maybe Alpha first level Alph
###
#what if I have pairs, simple numbering but 
##===========================================	
## number_nested_switches_in_sequence()
##===========================================
#put the input I just created into ibm[0]
#this would be the main string after the nested switches are taken out  leaving switch word
forcedinputstring='''
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){     #  this would be 10  for line number      
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 18 but it said previously 28      
			fallthru
		
		default:
			print('the end')
}
'''
#this is input for add counter to switches
trouble=[]
trouble.append(forcedinputstring)


#this is using preset nested switch starting locations 11 and 29 for this test
# this is for making the nested switch numbered method 



#this swaps switch with nested_switch_" n
##########################################
## number_nested_switches_in_sequence():  #this is using hardcoded input for testing
##########################################
def number_nested_switches_in_sequence(): # list_of_nested_switches[11,29]
	print("=R2D2= NUMBER_nested_switches_in_sequence()  ====== ajax =====")
	newcount=1  #number of nested switches starts from 1
	## wait do I loopthru it get the position of the inner switches now why not
	## modification on july 24th 
	print("to see what it sees first")
	#this is string above called forcedinputstring
	print(trouble[0])  #it was ibm[0] which I will change it back to later
	mystring=''
	mystring = trouble[0] #putting the string into trouble[0]
	newcounter=0
	foundone=[]
	# this gets the inner switch locations after the inner switch bodies have been stripped out (deleted)
	##===============================
	for line in mystring.splitlines():  #this fills list foundone with switch line numbers
		if "switch(exp)" in line:
			print("true we found switch")
			foundone.append(newcounter) #this fills the foundone list of line numbers with switch in it
			newcounter += 1
			continue
		else:
			newcounter += 1
			continue
	#=== end loop ========================
	print("we are done looking for the inner switch locations")
	print("====================")
	print("thefoundone llist has",foundone)
	print("the length is", len(foundone))
	print("========........======")
	print(" ") #below we delete the first switch which is on line 1
	del foundone[0] #this should delete the first switch we don't need 
	print("now we have for foundone list",foundone)
	## end getting inner switch lcoations
	##======================================
	
	#shiney= ibm[0] #so it will skip the first few lines skipping the first switch 
	thecounter = 0 #tracking lines in the string   oh it's using preset numbers
	print('the list of nested switches starting line',foundone)
	switchcount=0
	magic_string=''
	seagull='' #WAS shiney.splitlines()
	for line in trouble[0].splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20 #IT HAS TO BE AFTER THE FIRST 2 LINES TO SKIP THE FIRST SWITCH
		#if  switchcount > 0  and thecounter in foundone:
		# if thecounter in founderone
		if  thecounter in foundone:  #this must be line numbers of inner switches
		#this line of code is absolutely beautiful and elegant 
			print("thecounter=",thecounter)
			print("switchcount=",switchcount)
			########We know the line numbers do it on one pass perhaps
			# it should only go to the lines in the list of nested switches
			gettabcount=line.count("\t")
			line = line.replace("switch(exp){","nested_switch_"  + str(newcount) +  "  " +str(gettabcount) + " tabs " +"(n)")
			magic_string += line + "\n"
			#NEW line above
			newcount += 1  #break #because we are only doing it once to replace only ONE switch #start  = thecounter #this resets the range n to skip what it just did.
			thecounter += 1 #this adds to the neste switch counter
			continue    
		else:
			magic_string += line + "\n"
			# new ling e
			thecounter += 1
			continue
	print("=====-----======-----======------=====----====----====---")
	print("magic_string=")
	print(magic_string)
	print("========")
	for line in magic_string.splitlines():
		print(line)
		
	print("were the changes made - this is kind of important at this stage RED ALERT")
	trouble[0] = magic_string #here it's fed into trouble[0] so it's in a list now
	print("did I rip out the nested switches or are they still intact???")
	print("trouble[0]=",trouble[0])	
	#ibm[0] = shiney
			
####================================			
print('about to call number-nested_switches_in_sequence() to test it extendo bus just passed')
number_nested_switches_in_sequence()
print("it should have ran already testing bugs bunny here ")
print("the nested switch words should be nested numbered methods now")
print("just ran this function number_nested_switches_in_sequence()")
print("original mac computer")
			
#exit()

print("we are at line 4434 now and after finishing doing number_nested_switches_in_sequence() ==>>")
print("this is where the exit() was.......1..2...3..4....5..555..666...777..8.8..9999.10 10==")













#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





			
###============== Sunday July 25th, 2021  10:19 am Cafe Borrone ===============
# the idea is to put the information for each nested switch case
# into the dictionary in terms of it's exact information
# so to fill the data into the nested switch dictionary I will need
# to loop thru the switch string and gather the data for each switch location
# and it's particulars and add it to the dictionary (this should be done first')
# the idea occurred to me since each nested switch has a specific location
# and juggling them can get quite confusing so this way I know which is which
# and where it is.
#=======================================================================
####################
## DICTIONARY HERE 
####################
#putting a named list inside of known dictionary
nest_data=[]
# I probably won't need this.
nested_switch_data =	{  #for pear tree in backyard (2 of them)
#key [level tab depth,number case,  line number, series number
"1": [3,2,23,1], # I can make these now 
"2": [3,3,43,2],
}

print(nested_switch_data)

result=[]
result.append(0)

###############################################################
## RAM LIST TO HOLD TEMPORARY DATA FROM LIST WITHIN DICTIONARY
###############################################################
ram_list=[]
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)

########################
## get_nest_data(key)
########################
def get_nest_data(x): #puts it temporarily into result[0]
	print("get nest data called",x)
	#this grabs the value from the key and puts it into result[0]
	#these are teh parameters for tehe signature for this nested switch
	result[0]=nested_switch_data.get(x)
	#s- there would be a list within result[0]
	#why not instead populate a list
	print("this is what is in result[0]")
	print(result[0])
	for item in result[0]:
	    ram_list.append(item) #see if this fills it or not
	print('ram_list=',ram_list)
#############################		

  #test data input
############################
##  add_to_nest_data(x,y)
############################
cool_list=[]

# what is missing is the meaning of the code and the beahvior that it creates
# when it's running and knowledge
# how it works and what it does at levels

x = cool_list
def add_to_nest_data(x,y):
	print("====add to nest data() called with ", x  ,"and",y)
	nested_switch_data["my_list_" + str(x) ] = y

#print("my_list_1[0]",my_list_1[0])
#print("gosh")
######====================================
########
print("working on access a dictionary in a precise positiion in a list")
print("that is in the dictionary")
my_dict={}
#add a dictionary #this might be just what I need actually 
my_dict["my_list"] =[3,1,4,1]
print('terrible')
print('trying mydict[0] see if it works')
print(my_dict["my_list"][0]) #the key
print(my_dict["my_list"][1]) #the key
print(my_dict["my_list"][2]) #the key
print(my_dict["my_list"][3]) #the key
alpha = my_dict["my_list"][0]
print("alpha sees =",alpha)
#check in the list


# 

my_list_1=[]
my_list_2=[]
my_list_3=[]
#####======================================
y = [1,2,3,4,5]
add_to_nest_data(1,y)

y = [23,26,34,42,52]
add_to_nest_data(2,y)

y = [63,66,64,72,72]
add_to_nest_data(3,y)
print("=================")
print(my_list_1)
print(my_list_2)
print(my_list_3)

#print(my_list_2)
#alpha = mylist_1[0] #should be 1
print("is this even working....",alpha)

print(" == looping through nested_switch_data to see the contents == ")
print("TESTING ship wreck the contents of the dictionary now,,,")
for key,value  in nested_switch_data.items():
	print(key,value)
	













################################
##  NESTED_SWITCH_INFO
###############################	
def nested_switch_info(x):
	get_nest_data(x)
	#this will get the info from the dictionary		
			
			
			
switch_location=[]
endswitch_location=[]
#  WE ARE HERE THIS IS WHERE THE BIG TEST BEGINS TO REPLACE INNER SWITCHES WITH METHODS ON THE FLY
##=================
#if we already have the numbers it should work, later I will have it find the locations first
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG ===BIG TEST here in the switch with 2 nested switches")
print("========")
print("this does the bottom half the bottom nested switch first ")
print("this is becuase it's governed by the corect line numbers")
print("and if I take out the top switch code then the numbers for the lower switch will be wrong")
print("I just realized that") #this is the purpose of experimentation
ibm[0] = tuna  #I am force feeding it into ibm[0]

# I have to tell it what number to use to number the nested method using
# use_number[0]= 2 example








################
# the skipping is done by the main switch when I cam copying it and taking out the 
# nested switches below but keeping the switch word that I then convert to a method nested numbered
#################
### TESTING 
#NUMBERING OF NESTED SWITCH HAS TO BE DONE BOTTOM UP SINCE WE ARE RIPPING OUT THE NESTED SWITCH AFTER THE SWITCH WORD
#oh I will have to do this bottom up so the line numbers are correct.
#first show what is in ibm[0]
print("====== testing main switch template ======tue sep 14, 2021 ================")
print("WE MADE IT HERE line 4691 it's tuesday today")
print("TUESDAY TERRIBLE TEST of main nested switch and adding methods for switches swapped out") 
print(ibm[0])
print("I am taking out the lower switch first (later I will copy it first)")
print("it does it upside down going bottom up to do this.")
'''
skipping_some_lines(ibm[0],28,38) #changes 2nd nested switch
use_number[0]=2
swap_switch_for_nest_method_new(21) #second number has the switch in it 
#the first number is the number for the nested_switch
print("this now does the top nested switch")
print("here I am taking out the first nested switch later I will copy it first")
skipping_some_lines(ibm[0],10,20) #changes first nested switch in the sequence
use_number[0]=1
swap_switch_for_nest_method_new(11) #second number has the line number with switch   #needs to be 1 not 2
print("this is the end of Godzill and King Kong testing")
'''






#this should be called only once and 
print("====++++now testing running number_nested_switches_in_sequence()")
#number_nested_switches_in_sequence()
print("we have just completed the first nesteed switch skipping and putting a nested method 1 in ")
print("ibm[0] should show the main switch with 2 methods where the inner switches were previously")
print("this is the output of the string ibm[0]")
print(ibm[0])
print("I am going to loop thru the switch and change the lines with nested_switch")
print("============= Godzilla =============")
print("END OF GODZILLA AND RODAN AND MOTHRA")


#go thru a number the switches numerically top down

























hawaii ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#######
			switch(exp){          
				case 'blable':
					print("do something")
					print("yep")
					######
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
						######
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			######
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			#######
			switch(exp){          
				case 'fish':
					print("do something")
					print("yep")
					fallthru
				case 'trout':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#######
			fallthru
		
		default:
			print('the end')
}
'''	
get_switch_and_endswitch_locations(hawaii)
print("this would have just gotton the switch and endswitch line number locations above...")
print("I found it, I was looking for this code")
#empty_switch_and_endswitch_list_locations()

get_switch_and_endswitch_locations(tuna)
###======================================================
#july 19th 2021 testing this feature now morgan hill starbucks
########################################################
#empty_switch_and_endswitch_list_locations()
#print("the one below this line should produce 2 switches and one with 10,20")
#print("why is this wrong")
#get_switch_and_endswitch_locations(samplestring) #samplestring 
#get switch and endswitch lcoations for one nest
#it's off by one says 11,21
#input is 10 and 20 and yet this says the line number is 11 and 21 for nested switch

empty_switch_and_endswitch_list_locations()
print("the one below this line should produce 2 switches and one with 10,20")
print("why is this wrong")
print("get result of get switch and endswitch locations from samplestring")
print("earth is over level ======")
print("earth is over level ======")
print("=== tea time =============")
get_switch_and_endswitch_locations(samplestring) # sammplestring


###  july 14th wednesday 2021 working on this
#real number is count endswitches and add 1 for total switches

#endswitches number is how many nested switches

# this empties the lists storing the switch and end switch locations

#del switch_location[:]
#del endswitch_location[:]

#get_switch_and_endswitch_locations(hawaii)

print("this is the string with two nested switches")
print("here we go wednesday coding - the bicycle gloves are great")
print("first clearing out the lists that hold the locations of the switch and endswitches")
print("this clears out the swith and endswitch locations in the list so it starts empty")

#I was deleting the crucial lists so the code down below couldn't behave correctly

#del switch_location[:]
#del endswitch_location[:]
#feed the string into the method to get the switch and endswitch locations
# but delete the first switch details which isn't important at this point.

#get_switch_and_endswitch_locations(tuna)
#this creates a list that can be of any size and then I can subtract the first switch
#and then divide the number by 2 to get teh number of switches or just count teh switches
'''
nest1=[]
nest1.append(switch_location[0])
nest1.append(endswitch_location[0])
nest2=[]
nest2.append(switch_location[1])
nest2.append(endswitch_location[1])
#wait a  second with each pass the output will be teh same unless I have 
#a list of say ten spaces tol hold locations to be proactive.
#####################################################
print("nest1=",nest1)
print("the two values in nest1 are",nest1[0],nest1[1])
print("nest2=",nest2)
print("the two values in nest2 are",nest2[0],nest2[1])
'''


#++++++++++=========================================================
### july 7th 2021 experimenting 
### testing cutting out two nested switches one at a time
### and replacing the switch location with the nested method with a number
# I need to do these separately first to make that they work
##===========================================
##===========================================
#skipping_some_lines(tuna,nest1[0],nest1[1])
#swap_switch_for_nest_method_new(1)

#and I need to make sure that the resulting string to modify the second phase is correct
#skipping_some_lines(tuna,nest2[0],nest2[1])
#swap_switch_for_nest_method_new(2)
##============================================
##============================================
# what I will attempt it going thru the double nested switch with two nests
# and delete the two nests and put nest methods in the location of the inner switches.
# and then after that is figured out I will first copy each inner switch
# Based on the nested switch locations I find I can determine how many nested switches
# espcially with teh endswitch count 



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========


















def end_program():
    print("ending program")
    return

## method chaining nov 13th, 2021 &:45 am
print("======= chaining methods =======")

'''
I was going to do method call
Loop thru all slots in list
====================
Then do next method call to all items in list
Chaining input to output is input fir next method
Then realized if i chained
Sequence of methods only go thru loop once (genius)
'''


# 48-C battery volvo 2002 s60
# 1 800 222 4357
# 
# 1041 Cochrane road, morgan hill starbucks

## chain methods code  chain methods chain methods CHAIN METHODS 



#A method that calls a series of methods really utilizing output from previous method

#these might have been created above but I am doing them again here just in case.
input=[]
input.append(0)

output=[]
output.append(0)


##=====================
##   get_final_finished_string()
##=====================
def get_final_finished_string():
    print("===get_final_finished_string():===")
    print("output[0]=",output[0])
    print("=== result is in output[0] ===")
    
# passing the baton in the relay race 
##=====================
##   so_pipe()   #this feeds output[0] into input[0] to be used with next method
##=====================
def do_pipe():
    print("==== do_pipe() ====")
    #put output[0] into input[0]
    input[0] = output[0] 


##=====================
##   initialize_lists()
##=====================
def initialize_lists():
    print("====initialize_lists(): ====")
    input[0] =''
    output[0]=''
   


old_string_test='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here        representings stripped out inner nest
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){     #here    # represents already stripped out inner nest 
			fallthru
		default:
			print('the end')
endswitch
'''

  
holdthis=[]
holdthis.append(0)

#this swaps endswitch with }
######################################
## take_out_endswitch(stringname)  #from bottom of nested switch 
######################################
def take_out_myendswitch(stringname):
	print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			print("detected } in line")
			#location = line.index("#")    #gets location from left where position of #
			#line = line[:location] 
			print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			print("after left shift it is ",line)
			#line[0] = first #this is new to slice off right of brace
			line = line[0]#first char
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():
	#    print(line)
	    
	##===========today sunday coding
	
	#then look for this } and reposition it
	'''
	testingthis=''
	for line in holdthis[0].splitlines():
	    
	    if "}" in line:
	        line= line.lstrip()
	        testingthis += line
	    else:
	        testingthis += line
	holdthis[0] =testingthis
	print("now testing if this change worked shifting } to far left")
	for line in holdthis[0].splitlines():
	    print(line)
	'''       
	#this is what I need to modify.
	#so the whole modified string after ripping out endswitch is now in holdthis[0]
	
	print(holdthis[0])
	galaxy = holdthis[0] #now galaxy gets what is in holdthis[0]
	return galaxy #and this is returned
	
print("testing taking out endswitch and putting in brace")
#take_out_endswitch(old_string_test)
print(holdthis[0])


    
##======================================================================================
#the result of each of these methods will put their result in output[0]
#swap_feed_data then puts what is currently in output[0] into input[0] so it's a handoff of the baton
#each of these methods takes in input[0] as input with the result going into output[0]
#after each method we call do_pipe() which puts output[0] into input[0]
# string --> m1(input) => m2(input) => m3(input) => m4(input) => m5(input) 

##====================================================
##  first_method : manipulate_string  (left indent)
##====================================================
#manipulate_string left shift indentation
def first_method(astring): #this does the left shift 
    print("manipulate_string left margin indent ===first message called..")
    #shifts string left to indent it properly
    astring=manipulate_string(astring) #I think that this does left shift indentation
    return astring

##==========================================
##  second method : take_out_switch_body  from inner switches
##=========================================    
#take_out_switch_body
def second_method(astring): #cuts out switch body leaving switch word in all occurances
    print("take_out_switch_body ...seconed method called...")
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #<== key this is new to see if it works=========
    #astring += " water"
    return astring


##=================================================
##  third method : change_switch_to_method_solved
##=================================================
#change_switch_to_method_solved
def third_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("change_switch_to_method_solved  swapto neested_switch method third method called...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    return finalresult

##======================================
##  fourth method  : take_out_endswitch
##======================================
#take_out_endswitch(stringname)
def fourth_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("take_out_endswitch  put in brace instead third method called...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring)
    #astring += " bright"
    return finalresult
    
    
##=======================================================================================
#using descriptive names not true method names yet
# what this is doing is modifying a string in stages in a sequence 
# code name waterfall
output=[]
output.append(0) #so we can use output[0] below
##========================================
##  chain_methods()   this just does a sequence of methods piped  
##                    together so each method passes its output as input for next method
##=====================================
def chain_methods(item):
    print("==OFFICIAL== chain_methods called ====")
    firstresult  = first_method(item)         # manipulate_string(string)
    secondresult = second_method(firstresult) # take_out_switch_body(string)
    thirdresult  = third_method(secondresult) # change_switch_to_method_solved(string)
    fourthresult = fourth_method(thirdresult) # take_out_endswitch(string)
    output[0]    = fourthresult #this puts the result into output[0]
    print("now we are looking in the frac output of fourth method")
    for line in output[0].splitlines():
        print(line)
    #the resulting string is put into output[0]
    
    
    # I still need to rename the actual methods and put them above this section 
    #add comment number to all switches at the very beginning of initial switch string(not here)
    #add_comment_with_number_to_top_switch(input[0]);do_pipe();  #switch # 22 <-- line number added
    #shift_string_to_left_by_reducing_tabs(input[0]);do_pipe();  #subtract tabs # works nov 19th
    #cut_out_switch_bodies_at_3_tabs_depth(input[0]);do_pipe();  #reduce switch body to just switch word
    #swap_switch_with_nested_switch_number(input[0]);do_pipe();  #change switch to nested_switch_22(exp)
    #replace_the_last_endswitch_with_brace(input[0])             # endswitch becomes  }
    #get_final_finished_string() #in output[0] prints it out nest_list to see it




##=================================
## change_slot_string(counter)    this changes content of each slot in nest_list
##=================================
def change_this_slot_string(counter): #requires output[0] finished string
    print("==== change_this_slot_string(counter) ====")
    counter = int( counter)
    nest_list[counter] = output[0] #I really need to test this one and see if it works 
    #this means that needs to have finished chained_methods put into output[0]
    
##============================
## transform_string()    uses nest_list with strings in it of switch case bodies
##============================
def transform_string():  #this calls chain_method(item) # separate switch string input
    print("==== transform_string() ====")
    counter =0  #loop
    for item in nest_list:  #loop thru nest_list and each loop does the chain_methods
        chain_methods(item) # takes in string and does sequence methods puts into output[0]
        change_this_slot_string(counter) #changes slot string from output[0]
        counter +=1


##==================================================
## loop_thru_finished_list_of_prepped_strings():
##==================================================
def loop_thru_finished_list_of_prepped_strings():
    print("==== loop_thru_finished_list_of_prepped_strings() ====")
    counter =0  #loop
    for item in nest_list:
        print(item)
        print("counter=",counter)
        print("===========")
        


# loop_thru_finished_list_of_prepped_strings() took this out
# this hasn't been tested yet. Today is Sunday, November 14th, 2021 10:58 am Pacific Standard Time
# this goes thru nest_list and modifies all of the switch strings
# and fixed the indentation, and adds nested methods and a comment after each switch 
# with the number after it and cuts out the switch bodies at three tabs depth
# and it uses chain methods in a sequence on each string so the loop only goes ONCE !!!!!
##====================================================
##  prep_nest_list_of_switch_strings_for_bypass205()   STAINED GLASS WINDOW SECTION
##====================================================
## ATTENTION: I have the code for this working but the names are new and I need to 
# put the first two methods lists below in these names. This is SOOO COOL NOW 
#dec 5th sunday I don't think that this is called yet.not tested yet then.
def prep_nest_list_of_switch_strings_for_bypass205():
    print("====prep_nest_list_of_switch_strings_for_bypass205() ====")
    go_thru_input_major_switch_string_and_make_list_of_pairs_switch_and_endswitches() # made above
    using_pair_list_make_seperate_switch_strings_and_put_into_nest_list()             # made above
    transform_string() #DOES CHAIN METHODS  loops thru  nest_list modifies each separated string
    loop_thru_finished_list_of_prepped_strings() #thru FINISHED nest_list
    #the end result will be in nest_list with the strings ready to feed into bypass205
    



holdingpattern=[]
holdingpattern.append(0)
##=========================================
## fixes_dots_in_nested_string(inputstring)
##=========================================
def fixes_dots_in_nested_string(inputstring):
    print('testing very_clever')
    #    print(item)
    newline =''   
    for line in inputstring.splitlines():
        if "nested_switch" in line:
            newline += line.replace(":","") + "\n"
        else:
            newline += line + "\n"
    print("this is the result of modifying and taking out : after nested_switch")        
    for line in newline.splitlines():
        print(line)
    holdingpattern[0] =newline
     #I still need to change the slot in the string though 







input=[]
output=[]
output.append(0)

mystring = "smile "

def get_one(astring):
    astring += " a"
    return astring
    
def get_two(astring):
    astring += " water"
    return astring

def get_three(astring):
    astring += " bright"
    return astring

fizz  = get_one(mystring)
fizzy = get_two(fizz)
fuzzy = get_three(fizzy)

print("fuzzy after my simulated piping =",fuzzy)
print("")
print("")
print("final test before sending it to bypass205()")
print("this should take in a string")
print("indent it to the left margine")
print("take out switch bodies")
print("swap switch with nested_switch numbered")
print("============== here we go rudolph ======")
print(" . ")
print('...................,.,.,.,.,.,.,.,.,.,.,.')



#for testing purposes of transforming an input string this one is teststring3
mystring = teststring3  #right here change it 
for line in mystring.splitlines():
    print(line)
   
   
   
    
#manipulate_string left shift indentation
def first_method(astring): #this does the left shift 
    print("=====first method started..")
    #shifts string left to indent it properly
    #LEAVE THIS DON"T MEDDLE THIS WORKS
    # MODERN TAB SHIFTER TO LEFT IS PURE GOLD
    modern_tab_shifter_to_left(astring) #I think that this does left shift indentation
    astring= goldtime[0] #output from modern_tab_shifter_to_left
    #removes garbage on right side of switch strings (still testing)
    ########################
    print("check right here frosty")
    #print("newstring[0]=",newstring[0])
    
  
    
    ##################################
    #print("calling: fixes_dots_in_nested_string() method")
    #fixes_dots_in_nested_string(astring) #when it is nested_switch_22:(exp) removes :
    #astring=holdingpattern[0]
    for line in astring.splitlines():
        print(line)
    
    #return astring
 ######################################   
#take_out_switch_body
def second_method(astring): #cuts out switch body leaving switch word in all occurances
    print("=======seconed method started.take_out_switch_body..")
    #astring =newstring[0] #from first method above outoput
    #TAKE OUT SWITCH BODY METHOD
    #print("see what we are passing does it have something in it")
    print(astring)
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #this is new to see if it works=========
    
    
    print("==output from second method take out switch body==")
    for line in astring.splitlines():
        print(line)
        
    print("================")
    #astring += " water"
    return astring




 #converts inner switch into a nested_switch method numbered
############################################
#change_switch_to_method_solved
def third_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("=======third method started...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    #converts inner switch into a nested_switch method numbered
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    print("===third method output==")
    print("outoput from change switch to method solved")
    #for line in finalresult.splitlines():
    #    print(line)
    
    print("what does it say right here")
    for line in finalresult.splitlines():
        print(line)
        
    return finalresult    
    
    
    
############################################

#take_out_endswitch(stringname)  #this would do all of them regardless of number
def fourth_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method startedc...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring) #replaces it with }
    #astring += " bright"
    return finalresult
    
hollister_list=[]
#take_out_endswitch(stringname)
##=========================================
##  simulated_chain_methods():  this is called for each switch string
#this is doing one string at a time. 
##===================================
def simulated_chain_methods(mystring): #starting point 
    print("SIMULATED CHAIN METHODS () Rudolph the red nosed reindeer")
    first_method(mystring)
    fizz=goldtime[0] #output from first_method()
    print("stage1 fizz =",fizz)
    
    print("FIZZ TESTING CRITICAL 1ST METHOD output of first_method() ")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fizz.splitlines():
        print(line)
    
    ##############################==================
    fizzy = second_method(fizz)  #missing 66
    print("stage 2 fizzy=",fizz)
    
    print("FIZZ  TESTING CRITICAL 2ND METHOD to see what's in frac")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fizz.splitlines():
        print(line)
    
    #return   
    ##############################
    fuzzy = third_method(fizzy)
    print("stage 3 fruzzy=",fuzzy)
    
    print("FUZZY  TESTING CRITICAL 3RD METHOD to see what's in ")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fuzzy.splitlines():
        print(line)
        
        
    ############################
    frac  = fourth_method(fuzzy)
    print("strage 4 frac=",frac)
    #############################
    print("now we are looking in the frac output of fourth method")
    for line in frac.splitlines():
        print(line)
    print('above this line is the Rudolph the red nosed reindeer final first test')    
    print("line number 12502")
    #frac is the result
    #look at frac to see when  switch 31 and 66 are missing
    print("FRAC  TESTING CRITICAL 4TH METHOD n frac")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in frac.splitlines():
        print(line)
        
    hollister_list.append(frac) #new on november 30th Tuesday 
    
    
    
    
###==============
##   plan B 
##================  testing converting nest string testlist_of_strings
def planB():  #november 30th, tuesday 9:45 am morgan hill starbucks 
    print("never give up")
    print("PLAN B called using simulated_chain_methods on each switch string")
    print('===== welcome to planB ==== november 30th tuesday===')
    print("doing planB testing each nest_list doing chain_methods")
    counter=1
    for item in testlist_of_strings: #test string names numbered
        print("========================")
        simulated_chain_methods(item) #testing chain methods
        print("====== counter= ",counter)
        counter += 1
        
    print("the HOLLISTER LIST of modified switch strings that started out seperated")
    for item in hollister_list:
        print(item)
        print("==== middle ground between methods ===")


#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########


#making this sucker work no matter what 

#print("the big test begins")
#planB()
#print("now simply loop thru the finished changes in the list")

#### stage 1 test ###############
#each fruit method will do the list of 7 input strings stop

result_of_first_method=[]
result_of_second_method=[]
result_of_third_method=[]
result_of_fourth_method=[]

print("this is after the input stings have already been seperated")
###=====FIRST METHOD OF CHAIN METHODS ============
##======================
##  move_string_to_left_side()        first method modern tab shifter to left 
##======================
def move_string_to_left_side():
    print("=====APPLE== modern_tab_shifter_to_left()=====")
    counter = 1
    for item in testlist_of_strings:
        print("=======")
        modern_tab_shifter_to_left(item)
        fizz=goldtime[0] #output from first_method()
        #print("apple stage1 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_first_method.append(fizz)
        print("===== counter =",counter)
        counter += 1
    ################################################    
    counter =1
    print("result of shifting input strings to left")
    print("=====APPLE==APPLE   APPLE   APPLE   APPLE   APPLE=====")
    for item in result_of_first_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    



###=====SECOND METHOD OF CHAIN METHODS ============
##======================================================
## take_out_the_inner_switch_bodies_leaving_switch()
##======================================================
def take_out_the_inner_switch_bodies_leaving_switch():
    print("=====PLUM == take_out_switch_body(item)====")
    counter = 1
    for item in result_of_first_method:
        take_out_switch_body(item)
        print("===== counter =",counter)
        counter += 1
        fizz =lightning[0]
        print("plum stage2 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_second_method.append(fizz)
    ###################################################
    counter =1
    print("result of taking out inner switch bodies")
    for item in result_of_second_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    

#good_plum()



###=====THIRD METHOD OF CHAIN METHODS ============

##===================================================================
## good_peach()  change_switch_to_method_solved : switch to nested_switchX(exp) # 
##=================================================================
def change_switch_to_nested_switch_method(): #swaps switch with nested_switch method
    print("=====PEACH===change_switch_to_method_solved===")
    counter = 1
    for item in result_of_second_method:
        fizz=change_switch_to_method_solved(item)
        print("peach fizz=",fizz)
        #append outputto result_of_first_method
        result_of_third_method.append(fizz)
        print("===== counter =",counter)
        counter += 1
    #########################################
    counter =1
    print('result of 3rd method on string')
    for item in result_of_third_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    
    
 ###=====FOURTH METHOD OF CHAIN METHODS ============   
##===================================================================
## replace_endswitch_with_close_brace     take_out_endswitch() 
##=================================================================
def replace_endswitch_with_close_brace():
    print("=======ORANGE=take_out_myendswitch===")
    counter = 1
    for item in result_of_third_method:
        take_out_myendswitch(item)  #other one is take_out_endswitch
        print("=======")
        fizz =  holdthis[0]
        print('orange fizz =',fizz)
        result_of_fourth_method.append(fizz) #this fills up result_of_fourth
        print("===== counter =",counter)
        counter += 1
   #########################################
    print('result of 4th method on string')
    counter=1
    for item in result_of_fourth_method:
        print(item)
#Santa_Cruz_Python_Preprocessor/fourth_of_july2good.py /

 
 
   
#import official_switch_case_silver
#from official_switch_case_silver  import *  
endswitch_location=[]
switch_location=[]
zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'
cat_scales=[]
cat_scales.append(0)
#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 
#make sure no space and it's switch(exp){
#first red robin here testing 
red_robin ='''
	switch(exp){  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp)  
				case 'blable':
					print("do something")
					####################
					switch(exp){ 
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			exp = 3
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
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	

autumnleaf='''
	switch(exp){  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  
				case 'blable':
					print("do something")
					####################
					switch(exp){       
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){      
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){    
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
										####################
											switch(exp){    
												case 'fishy':
													print("do something")
													print("yep")
													fallthru
												case 'where now':
													print("nice")
													break
												default:
													print("we very done")
											endswitch 
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   4..........endwitch 4  line 60 3 tabs 
			exp = 3
			switch(exp){   
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
					endswitch #77 5 .....
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86   
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
} endswitch #100  7 ........
'''




# output is to inputstring[0]

passinputstring=[]
smart_switch_numbers=[]
loopstring=[]
loopstring.append(0)
#twinlist=[]
passinputstring.append(0)  #get line number of switch and add number with comment to after all switches
snowman=[]
snowman.append(0)
##===================================================
##  add comment and lin number to all switches ()   ## put switch line number in
##===================================================
#############################################################
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	print(" add_comment_and_line_number_to_all_switch()....this was just called .. ")
	print(" == directive 1 ==    ADD the stupid comment and line number after each switch relaly simple")
	awesome='';counter =0;newstring='';smart_switch_numbers=[];#clears it out Dec 11th
	print('baseline is red_robin starting appearance testing purposes')
	print(inputstring)
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			# NEED TO HANDLE BOTH SCENARIOS switch with brace and switch without a brace 
			#############################################
			#switch is in this line definitely
			if "{" in line and "switch" in line and "end" not in line:
				newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
			#end if
			#this is necessary since the replace is quite specific and so no brace here
			# NOTE: I am adding gthe brace if it's missing to switch 
			if "{" not in line and "switch" in line and "end" not in line:
				newstring += line.replace("switch(exp)","switch(exp){ #" + str(counter) + "\n")  
			#end if  
			smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		####################################################
		elif "endswitch" in line: #just added comment number after endswitch 
			newstring += line.replace("endswitch","endswitch #" + str(counter) + "\n")
			#smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		###################
		else:
			newstring += line + "\n"
			counter += 1
	awesome = newstring #it was concatted to newstring which we now reassign to awesome then red_robin
	print("=== jump off the cliff and fly in hang glider ==")
	for line in newstring.splitlines(): #was redrobin.splitlines()
		print(line)
	print("AFTER ADDING the line number as comments to the switches in red robin baby ")	
	print(newstring)   #it prints red_robin switch combo string with the line numbers added in comments
	print("smart_switch_numbers=",smart_switch_numbers)  #this is new here too 
	return newstring #this way I can capture the changed string





def too_swift():
    print("==========too_swift() called=======")
    print("dirt stimple test showing lines with switch, end switch and }")
    for line in red_robin.splitlines():
        if "switch"in line:
            print(line)
        if "}" in line:
            print(line)
too_swift()

print('done for the exit sign')        


print("from the web trying this out")

quail=[]
# I am adding the quail list to practice filling it

print("testing add comment and line number after all switches")
add_comment_and_line_number_to_all_switches(red_robin)
print("REd ALERT critical test first method  test first method ...")
#exit()


def empty_switch_and_endswitch_list_locations():
    print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter

switch_location=[]
endswitch_location=[]
together_pair=[]
##########################################
#### get switch and endswitch locations 
##########################################
def get_switch_and_endswitch_locations(z): #from string z input parameter
	return
	#return we START BUILDING
	print("thbis is what I am testing now now now")
	print("  get switch and endswitch locations###  called line 322 #####")
	print("######get switch and endswitch locations########")
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	#print("=====get_switch_and_endswitch_locations(z) called ....")
	#print("====== THIS IS THE ONE THAT I NEED ======")	#this catalogues the switch and endswitch locations for an entire input string
	#print(" GET SWITCH AND ENDSWITCH LOCATIONS ADDED TO LIST")
	#print(" ========  MICKEY MOUSE HOUSE  =========")
	counter=0 #it was 0 starting counting from 1
	for line in z.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		#print(line) #this should be revealing
		#if line.isspace():
		#wrong='''	
		#rechecking to see if this works 
		if "switch" in line and "end" not in line:
			print("switch found",counter)
			switch_location.append(counter)
			counter += 1			
		#if "endswitch" in line:
		#	print("look right here endswitch found",counter)
		#	endswitch_location.append(counter)
		#	counter += 1
		else:
			counter += 1 
	
	counter=0
	for line in z.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line:
			print(line)
			print("look right here endswitch found",counter)
			endswitch_location.append(counter)
			counter += 1
		else:
			counter += 1 
		#'''
	print("at this point this is what we have...after testing BIG YELLOW BIRD go bird")
	del switch_location[0] #takes out first number not needed
	print("switch_location=",switch_location)
	print("endswitch_location=",endswitch_location)
	#test_string1exit()
	print("this over writes the contents of these two lists ")		
	#hard coding it in here why 
	#switch_location    =[1,11,15,23,31,62,66]
	#endswitch_location =[100,60,51,46,41,86,77]	#might hav eto resverse these 	
	
			#THIS DELETES THE FIRST SWITCH WHICH WE DON'T USE
	#del switch_location[0]	#empties it what am I doing here??? july 7th deleting first switch
	print(z)                #now I remember that is the first switch which doesn't matter
	print("I deleted the first switch since I'm not bothering with it")
	print("switchlocations=",switch_location)
	print("on line 180 endswitchlocation=",endswitch_location)
	
	print("the length of switch list =",len(switch_location))
	answer = len(switch_location)
	answer = answer -1
	print("this is how many nested switches are here")
	print("now we should have this many nested switches to contend with",answer)
	print("and the answer is above this line .....")
	#this prevents a bug if I don't have endswitch in the string
	#if len(endswitch_location) > 0: #this only proceeds if there is at least one endswitch
	#	print("endswitch locations =",endswitch_location)
	#	print("out of curiosity print the number of endswitches", len(endswitch_location))
	#else:
	#	pass
	print("I need to test that this part still works here in fourth of july 2 .py")	
	print("this might be simpler to test and use actually======/////???????//////===")
	print("======================================")
	print(" ===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === ")
	print("I need to delete teh first swithc location")
	
	#working on this on Saturday, October23, 2021 to get this stage done 
	#del switch_location[0] #ALREADY DELETING FIRST SWITCH ABOVE BECAUSE IT'S NOT NEEDED NOT NESTED
	print("does this look right testing on Sunday gloomy rainy day")
	print('switch_location=',switch_location)
	print('endswitch_location=',endswitch_location)
	#the input is above
	
	
	print("....")
	print("the input for filling the blueberries dictionary are the lists switch_location and endswitch_location")
	print("==================")
	#print("the enchanting world of making blueberry pie")
	
	
	
	
	##################################################################################
	############## working on this on saturday, october 23rd, 2021 ###################
	##################################################################################
	print(" rain fall status ")
	counter=0
	#working on creating input list for blueberries dictionary: can't believe I didnt do this yet
	print("what the hell is going on here")
	#print("switch_location=",switch_location)
	#for item in switch_location:
	#	print(item)
	#print("so how did that go...")
	
	print("endswitch_location=",endswitch_location)
	#for item in endswitch_location:
	#	print(item)
	print("so how did that go...")
	
	
	counter=0
	print("starting at counter =0")
	
	print("=============== starbucks morgan hill =====")
	print(switch_location)
	print(endswitch_location)
	print("emptying together pair here")
	del together_pair[:] #delete it just in case to start with clear chalkboard
	print("=======") #THIS FILLS THE TOGETHER_PAIR LIST OF SWITCH,ENDSWITCH 
	print("this loop fills the together_pair list of switch,endswitch numbers")
	print("this is so much dam fun oh yeah")
	total1 = len(switch_location)
	total2 = len(endswitch_location)
	print("total1 =",total1)
	print("todal2=",total2)
	print("this is where we START BUILDING the ===TOGETHER PAIR =====")
	for item in switch_location:
		solution = "[" + str(switch_location[counter]) + "," + str(endswitch_location[counter]) + "]" 
		print("solution=",solution) #to see what it looks like 
		together_pair.append(solution)
		print("counter=",counter)
		counter += 1
		
		#this should prevent stack overflow of the list range added november 9th 
		if counter >= len(switch_location):
			print("stack overflow called since counter > = len(switch_location)")
			break
		else:
			continue
			
	print("now we will loop thru the together_pair to see that the pairs are in there")
	del endswitch_location[-1] #should delete 100
	print("this is what is in TOGETHER_PAIR at line 254")
	for item in together_pair:
		print(item)
		apple = item.split(",")
		print("======")
		print(apple[0])
		sweet1 = apple[0].replace("[",'')
		#print(sweet1)
		print(apple[1])
		sweet2 = apple[1].replace("]",'')
		print(sweet1,sweet2)
		print("where's the party")
	# I need to feed these into the pear dictionary now down below
	#I will feed the pears list with a loop thru the switch_location list
	########## WORKING ON THIS TODAY MONDAY TO MAKE SOME SERIOUS PROGRESS 
	##########  MONDAY JULY 19TH APPROACHING 12 NOON 
	
	#make pairs here
	#might have to delete teh first switch which throws everything off
	##################### end of method #################################3
#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]  	
	
	

print("what are they actually")
print("starbucks coding NEXT TO RED ROBIN===== big storm coming...")
#Sget_switch_and_endswitch_locations(red_robin) #yeah it's calling red robin!!!
print("result of switch and endswitch locations in red robin")
print("examine the contents of the lists switch_location and endswitch_location")
print('switch_location=',switch_location)
print('endswitch_location=',endswitch_location)
print("RIGHT HERE DANGER WILL ROBINSON=====")
#print('switch_location=',switch_location)
#print('endswitch_location=',endswitch_location)
print("next I will fill the blueberries dictionary not yet on oct 23rd, 2021 saturday")
 ####<<========
#switch 1, 10,29
#endswitch  20, 38

#switch_location

string = """
line1
line2
line3
line4
line5"""
str_list = string.split('\n')
print('changing line 3')
str_list[3] = "my new line value"
string = "\n".join(str_list)
print(string)

print("end of test from the web")
print("=========")
#this simulates after cutting out the inner switches but leaves the first line
#which is used for replacement of the nested method()
############################################################
########## august 5th testing what to use now #################=========$$$$$$$$$$$
############################################################
# this represents and input string with inner switches cut out
#what remains is just the switch word which will be replaced
old_coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here        representings stripped out inner nest
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){     #here    # represents already stripped out inner nest 
			fallthru
		default:
			print('the end')
}
'''
coffee_now='''
	switch(exp){ #1      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 
		default:
			print("we are done here")
	endswitch #this is key here 
'''
	
#this is coolstring with the nested switches already taken out for all levels+
coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			switch(exp){
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){   #here        representings stripped out inner nest
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			switch(exp){     #heret 
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){
			fallthru
			
		case 16 to 20:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){ 
			fallthru
			
		case 16 to 20:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){ 
			switch(exp){
			switch(exp){
			fallthru
		default:
			print('the end')
}
'''

#working on this July 15th, 2021 10:16am Starbucks
#get_switch_and_endswitch_locations(coolstring)
#output to these lists
#switch_location #skips the first main switch not included
#endswitch_location (if any)
#get_switch_and_endswitch_locations(coolstring)
print("done with test to get the nested switch locations within the big switch")

### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
switch_list=[]

#this accesses coolstring august 5th, 2021
#this is to set the inner switch positions in the main switch input strings
#after the bodies of the nested switches have been stripped out

##########################################
##  put_switch_locations_into_switch_list()  #this is making the nested_switch_ number  
##########################################
def put_switch_locations_into_switch_list(inputstring): #just added param
    print("##2### put_switch_locations_into_switch_list ###")
    print("##2## put switch locations into switch list ###")
    print("put switch locations into switch list")
    #### get swith and endswitch locations called here 
    get_switch_and_endswitch_locations(inputstring) #it's right here 
    for item in switch_location: #this is only going thru switch_location
        switch_list.append(int(item))  #was -1 on here #off by one in the string for some reason
    # print(" ");print("switch_list=")
    #print(switch_list)

#######################################
##  swap_switch_to_nested_method()  #this is making the nested_switch_ number  
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	print("============== swap_switch_to_nested_method() ==========")
	#print("input: linenumber", linenumber)
	#print("input: series_num", series_num)
	
	#print("##4## swap switch to nested method - numbered ###")
	#print("##4## swap switch to nested method - numbered ###")
	#print(" THIS IS BEING CALLED TO DO THE MAGICswap switch to nested method called....")
	str_list = stringname.split('\n')
	#print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)

######################################	

#this is the control center main that runs this operation
#this numbers the nested switch methods top down
#genius[0]=coolstring  #assignment here <<<==================


#######################################
##  loop_thru_switch_locations():
#######################################
def loop_thru_switch_locations(regularstring):  #looping thru  switch_list[10,18]
    print("##1##loop thru switch locations ## line number 276 ####")
    print("##1##loop thru switch locations ######")
    #trick put_switch_locations_into_switch_list
    #method called
    put_switch_locations_into_switch_list(regularstring) #method
    print('this filles switch_list of switch line numbers')
    #print(genius[0])
    print("what is the order of the switch_list I think it's reversed to do bottom up")
    print(switch_list)
    print("------------")
    print("switch_list=",switch_list)
    le_number=1 #default numbering nested string 
    for item in switch_list: #loops thru switch_list WITH SWITCH LOCATIONS (LINE NUMBERS)
        print("item in switch_list",item)
        #string,switch,line number
        # swap_switch_to_nested_method here 
        #method this one is the holy grail that actually works
        ###############################
        swap_switch_to_nested_method(genius[0],item,le_number) 
        coolstring =genius[0]
        le_number += 1  #adding to the nested number here
    print("#### end of loop thru switch locations() ####")
    print('the EXIT sign is green')
#######################################



print("STAR TREK TEST FULL PHOTON LASERS add numberednested method McCoy looks good now beam me up ")
print("starting with this input main string with nested switch bodies cut out")
print("tahoe dream")
##==========================================================|
## swap_nested_switches_with_methods_in_main_switch_string
##==========================================================|
def swap_nested_switches_with_methods_in_main_switch_string(inputstring):
    print("===swap_nested_switches_with_methods_in_main_switch_string()== line number 309=") 
    loop_thru_switch_locations(inputstring) 
    print("this is the output string of the transformation from input string")
    ## this is after loop thruw switch locations method is completed
    print("this is the main input switch string after adding nested methods")
    print("the output of this transformation of swapping switch for nested_method")
    #this is the input string transformed 

#this calls it
genius[0]=coffee_now  #assignment here <<<==================
print("about to call swap_nested_switches_with_methods_in_main_switch_string(coolstring)")
swap_nested_switches_with_methods_in_main_switch_string(coffee_now)
print("fter testing tron getting closer=== 1 ...2.....3  out the EXIT")
print(genius[0])

#this calls above
print("=== begin tron test ==line 323 =TESTING september 1st here we go=-=== to see if this sucker works === august 27th ==== please work ==")
print("this is testing the main switch string module changing nested switches")
print("that already had their bodies cut out and swaping in a nested method")
genius[0]=coolstring  #assignment here <<<==================
print("about to call swap_nested_switches_with_methods_in_main_switch_string(coolstring)")
swap_nested_switches_with_methods_in_main_switch_string(coolstring)
print("fter testing tron getting closer=== 1 ...2.....3  out the EXIT")
print(genius[0])
print('end of test of swap nesetd switches with methods in main switch string ')
print(" oh that's what this does...da ")
print("====line 332 ==end of this tron test september 1st=====")
print("======end of this tron test september 1st=====")
#exit()  #stop it here
	#string_change =coolstring
#stringname=coolstring
print("now change the inner switches to the nested method numbered")
#swap_switch_to_nested_method(coolstring,10,1)	  #####======

print("after first change ====>>>>>>>")
#coolstring =genius[0]                            #########==========

#series_num = number_series[0] 
#swap_switch_to_nested_method(coolstring,18,2)	  ########=========
print("after the 2nd change ...")
#coolstring =genius[0]
##print(genius[0])                                ################============
print("done with this test of the new method")
  #building the method to make this magic happen automatically


#-------------------  july 10th, 2021   11:03 pm  -------starbucks coding-------
#I am hard coding the location of the switch words. I need to have it search on it's own
# but I recall I have code that does that elsewhere
#now I need to find the code that makes the correct nested switch list locations

#they are being harded coded in here I should be getting them from above

#switch_list.append(11) #was 10,18,31
#switch_list.append(19)
#switch_list.append(32)## added a third switch to test it more thoroughly 

##============================================================================
print("here put switch_locations into switch_list")
## this is new added Thursday july 15th 2021 prevents off by one error
## it takes input of nested switch line number locations from switch_location
## and puts them into switch_list (but again not the first main switch)   

#this one just commented out
#put_switch_locations_into_switch_list()
print("about to test it with the loop thru switch method ====")
print("today is july 22nd, 2021 thursday refining the algorithms and methods")
## calling LOOP THRU SWITCH LOCATIONS (INNER)

######======================
#loop_thru_switch_locations() #where to find the inner switches to replace with a nest method
######======================


print("did it work=============MMMMMMMMMM----======MMMMMMMMM==========")
print("we called loop_thru_switch_locations() which calls swap_switch_to_nested_method()")
print("we should have successfully swapped out the inner switches with nested_method numbered")
print("today is july 15th, 2021 at Starbucks connecting the functions")
print(genius[0])    	
print("olympic gold medal to make it this far.")
print("==IT SHOULD BE ABOVE THIS LINE WITH THE NESTED NUMBERS METHODS INNER SWITCHES==")
print("now I need to work on copying the nested strings to a list")
print("and then taking out the nested strings from the main switch string except for switch")
    
#this one works just need to test it as a method above 
#str_list = coolstring.split('\n')
#print('changing line 11')
#str_list[10] = "\t\t\tnested_switch_1(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)

#print(string_change)
#stringname = string_change
#############
#str_list = coolstring.split('\n')
#str_list[18] = "\t\t\tnested_switch_2(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)


#what if I go thru a list to make teh changes
#=====================================================
#z = 'test4'

#choose to 'Update Now'
# when the newest MacOS Mojave 10.14. 6 Supplemental Update

#say we add it to first case 2nd line after case just bump down whatever
#is on that line. copy that line just for saftey and add it to the tail
#with \n at beginning and end of that line


### look for nested switch called    switch_nest()  
# get case number which case is it, first, second, third for this test
#then get line number of case section determine what line it's on.
#(the nested switch method)

output_string_test='''
 switch(x) #main switch    #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("this is the first case in the main switch")
            #switch_nest() #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')   
                     
        if case == "two":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word') 
            
        if case == "three":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
           
            
'''

######## testing 2nd and 3d level deep nested switch cases july 29th, 2021


# will mess around with this later. 

triple_nested_switchtest ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
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



cicelyalaska ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'music':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'coolish':
									print("do something")
									print("yep")
									fallthru
								case 'auburn':
									print("nice")
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
			fallthru
		
		default:
			print('the end')
}
'''	



snowman='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									#################### this one is new 
									switch(exp){  #fourth level deep   Level 4    
										case 'obama':
											print("do something")
											print("good")
											fallthru
										case 'ufos are real':
											print("better")
											break
										default:
											print("nice job")
									endswitch 
							#############
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== interesting test here for just 3 here ==')
			switch(exp){  #second level deep          Level 2    
				case 'sierra':
					print("do something")
					print("yep")
					fallthru
				case 'snow lake':
					print("nice")
				default:
					print("welcome to the party") 
			endswitch
		case 1 thru 3:
			print("where\'s this will be one match for 3, 5!")
			print('first prize')
			switch(exp){  #second level deep          Level 2    
				case 'sierra':
					print("do something")
					print("yep")
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
						default:
							print("welcome to the party") 
						endswitch
					fallthru
				case 'snow lake':
					print("nice")
				default:
					print("welcome to the party") 
			endswitch
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'music':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'coolish':
									print("do something")
									print("yep")
									fallthru
								case 'auburn':
									print("nice")
									####################
									switch(exp){  #fourth level deep   Level 4    
										case 'coolish':
											print("do something")
											print("yep")
											fallthru
										case 'auburn':
											print("nice")
											#######################
											switch(exp){  #fifth level deep   Level 5    
												case 'coolish':
													print("do something")
													print("yep")
													fallthru
												case 'auburn':
													print("nice")
													break
												default:
													print("we are done here")
											endswitch 
											break
										default:
											print("we are done here")
									endswitch 
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
			fallthru
		
		default:
			print('the end')
}
'''	

'''
loop thru string
get switch locations and tabs coount
then make list of numbers of switches inside tab 3 switch
only thing that I cna think of.
make list with sublists
'''

answer=triple_nested_switchtest.count("endswitch")
print('counting the nested switches to see how it goes ====Boo ')
print("the number of nested switches based on endswitch=",answer)
for line in triple_nested_switchtest.splitlines():
    print(line)
print("=== the end ====")
print("================")

#answer we seek is case section 2, line 2
################===============================
#33 june 28th, 2021 9:26 pm now 

#where I detect the nested switch  location and starting and ending point
# I copy the nested switch and delete it from the main switch
# I add a method where thes switch word is.
# My compromises to get it working faster are the nested switch
# must end with endswitch  and not a curly brace
# this makes it easier to get working and aids readability

#the switch main switch is chopped off at the begining of the inner switch
#the bottom after the nested switch ends with endswitch is copied
#to the top half but only after the nested method is added to th eline
#where the nested switch was 



# when code is running there is nothing to see.
# If we have moving behavior (which is invisible)
# that is what matters -but like what Fred Brooks says
# software is invisible. So I need to make it tangible and visable.

#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========



# starting testing here to see if I can reduce the code to make sense

 ####### august 10th 2021 testing commences.
 
find_nested_switch_game ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
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

gameday ='''
			switch(exp){   #1 === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					switch() #7
						case 'funny':
							print('fun')
						case "da":
							print('yeah')
						default:
							print('bye')
					endswitch #14
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
'''	

print("what we are starting with the switch with a nested switch")
print(find_nested_switch_game)
print("=====================")
#oh wait this needs to be the input C style switch that I search in
#maybe I need to go through the case list palmtrees
# so get line number of switches
#get linenumber of each case to determine which case section the inner switch is in
pacman=[]
pacman.append(0)


coollist=[]
print("this gets the line number of the line that the case starts")
print("that has the nested switch inside THIS Case")

endnestedswitchline=[]
endnestedswitchline.append(0)
#########################################
##  get_case_line_numbers(string_name):
#########################################
def get_case_line_numbers(string_name):
    linecounter =0
    casecounter = 0
    print('get line number of each case section')
    #just get first case line numbers print it
    for line in find_nested_switch_game.splitlines(): #be sure to put stringname.splitliens()
        #this looks for cases
        if "case" in line:  #grabs first line
            print(line)
            pacman.append(linecounter)
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
        #if "switch" in line:
    print("case line numbers",pacman)    
    #print(pacman[2])  
    print("number less than 10 that ")
    #I reverse the list order to find the first case less than 10 the line with switch in it
    pacman.reverse()

#calls method above
#####==========
#get_case_line_numbers(find_nested_switch_game)
#####========


#####################################
## get_larger_number_less_than_case()
#####################################
def get_larger_number_less_than_case():
    #this gets teh larger number less tahn the case
    for item in pacman:
        if item < 10: #I will need to put  (this cuts the possibilities to those less than 10)
            coollist.append(item)
            print(item)
            print("this must be the answer of the case that is on line 8")
            break #so after just the first one
    #get largest number in list
    print("this is new trying to get largest number only from list")
    superman = max(coollist) #worked June 28th MOnday 2021
    print("largest number =",superman)

#calls method above
#######========
#get_larger_number_less_than_case()
#######========




###$############===================-----0-0--=-=-=-=-=-=0-0-0-9=0--
### GET END OF SWITCH LINE  number
#######################################
## now looking for end of nested switch case
#june 28th, 2021
#####################################
## get_end_of_switch_line_number():  #  this gets endswitch line number
#####################################
def get_end_of_switch_line_number():
    linecounter=0 #this looks for the line number of endswitch for the nested switch
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "endswitch" in line:  #grabs first line
            print("we have a match")
            print(line)
            #linecounter += 1 if it's endswitch don't add one
            print(linecounter)
            endnestedswitchline[0]=str(linecounter)
            break
        else: #this looks for the  switch word
            linecounter += 1   
            continue
    print("the end of this nested switchis",endnestedswitchline[0])
    print("====should be 18 ====")

#calling method above this 
#####=========
#get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
#####=========

#and we know that the case number is 8
#and we know that the nested switch starts on line 10
#therefore we subtract 10-8 = 2
#so within the case the nestedswitchmethod will be on line 10 or the 2nd line within the case
###############=======================########################
print("copy inner switch")
#first trying to copy the inner switch and put it into a list

linecounter=0 #this looks for the line number of endswitch for the nested switch
print("testing getting a copy of nested switch")
### what I need to do is grab the numbers that I generated that I am using below
### I determine the line number that the first and only nested switch is on
### I then look for the first "endswitch" after the nested switch starts
### and it must be within the bounds of the case that it is residing within.
#here I am feeding it but I need to make it a method
#x = 11;
#y = 60;
#start  = 11  #hard coded beginning of nested switch
#finish = 60 
start_and_finish=[]


##============================================
##  inputs_pair_to_copy_a_string()
##============================================
def inputs_pair_to_copy_a_string(start,finish):
    print("inputs pair to copy a string")
    del start_and_finish[:] #this clears it out initializing it
    start_and_finish.append(0) 
    start_and_finish.append(start) #position [1]
    start_and_finish.append(finish) #position [2]
    #start_and_finish[1] = x
    #start_and_finish[2] = y
    print("x=",start_and_finish[1])
    print("y=",start_and_finish[2])
    
########################################################################
 #hard coded end of single nested switch 
## COPY A NESTED SWITCH
############################

#so we have

#############################
r=find_nested_switch_game #thats the name of a string fin_nested_switch_came
#linecounter=0
makeitwork=[]
makeitwork.append(0)
## function copy a nested switch()   ==== I just put this into a function

print("will do red robin string with the sets of pairs individually to verify it's right")
print("testing Sunday, NOvember 7th, just got 3rd booster shot ----")
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')
print('=======copy_a_nested_switch() called=====)=====')

columbia_river=[]
gold_list=[]
###############################
## copy_a_nested_switch(r):   # what this does is copy one nested switch 
###############################
def copy_a_nested_switch(r):  #copy just one nested string 
    print("= copy_a_nested_switch() called== just now 10;43 am ====")
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
    for line in r.splitlines(): #if linecounter is between start and finish
    #this should copy a full (every line) of a nested switch from switch to and including endswitch
        # if lincounter >= 10 and linecounter <= 20; #this is what it means
        if linecounter >= int(start_and_finish[1]) and linecounter <= int(start_and_finish[2]):
            innerswitch += line + "\n"  #it's concatted to innerswitch string right here
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result COPY OF NESTED SWITCH  ")        
    #print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner #result of copied string goes in makeitwork[0]

################################################################################

#I need to fill this list (populate it from get switch engineswitch pairs
print("testing looping thru gold_list")
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]
print("=======begin Sunday Morning Brew Testing=======")

# uses methods:
# add_comment_and_line_number_to_all_switches
# inputs_pair_to_copy_a_string(num1,num2) #get input string from goldlist
# copy_a_nested_switch(water)
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]] 
gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]       
##=============================================================
##  split_up_big_string_into_nested_switches(myinputstring)
#  dependency requires gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]  
##=============================================================
# I am adding comment with line number to all switches wonderful news.
def split_up_big_string_into_nested_switches(myinputstring):#this would only be called once
    print("===boom boom boomsplit up big string into nested switches()===")
    water =add_comment_and_line_number_to_all_switches(myinputstring) #stringname goes here
    print("need to see that the comment and line number added after each switch")
    for line in water.splitlines():
        print(line)
    print("that is how we shall know")
    del columbia_river[:] #empties columbia_river; the inputstring name is now called water 
    #gold_list is prefilled here 
     #before the input string is modified  but after comment numbers added ; this is the original input string which is used for the main later
    print("gold_list=",gold_list)
    columbia_river.append(water) #this adds the mega initial string first for the main string
    print('at this point the length of columbia_river should be 1 and it is',len(columbia_river))
    for item in gold_list: #loop that gets switch,endswitch pair from goldlist
        num1 = item[0];num2 = item[1];
        inputs_pair_to_copy_a_string(num1,num2) #get input string from goldlist
        copy_a_nested_switch(water)  #copy string based on switch,endswitch pair 
        print("====================")#puts resulting string into makeitwork[0] and output
        output = makeitwork[0]       #put nested string into columbia_river list
        columbia_river.append(output)
    print("length of columbia river =",len(columbia_river))
    counter =1
    #adding here the initial string which will be used to make the main switch
      #it is added just before looping thru i
    print("now loop thru columbia river to see the switch bodies seperated")
    for item in columbia_river:
        print("counter=",counter)
        print(item);print("===========");counter += 1
##================================================================        


     
print("okay from this point forwards I have access to the columbia_river with the strings in it") 
     
     
     
     
     
     
     
     
     
     
     
     
     
     
#######======================================== ## find_nested_switch_game
#the input is the whole string afgter having added comment of swithc line number in loopstring[0]
#x =11; y = 60;
##=======================================
##  testing_code_copying_string_adding_it_to_list()
##========================================
def testing_code_copying_string_adding_it_to_list(x,y):
    inputs_pair_to_copy_a_string(x,y)
    #water is the modified string with line number (but need to only add the line numbers once as comment
    copy_a_nested_switch(water) #this takes in switchstring with switch numbers added as comment
#######=========================================
    output = makeitwork[0]        #this would have to be after the call to copy a nested switch
    columbia_river.append(output)

#testing_code_copying_string_adding_it_to_list(11,60)


print("now printing out columbia river")
print("length of columbia river =",len(columbia_river))
for item in columbia_river:
    print(item)
    
#exit()
 





start  = 7  #hard coded beginning of nested switch
finish = 14  #hard coded end of single nested switch 
## COPY A NESTED SWITCH
############################
start_and_finish=[]
start_and_finish.append(0) #position [0] #ignore
start_and_finish.append(start) #position [1]
start_and_finish.append(finish) #position [2]
#so we have
start_and_finish[1] = 7
start_and_finish[2] = 14
#############################
r=gameday
#linecounter=0
makeitwork=[]
makeitwork.append(0)
print('======SECOND ATTEMPT======')
#######========================================
copy_a_nested_switch(r) #this gets put into r as a parameter
#######=========================================



#lines 1 thru 9 
 #this looks for the line number of endswitch for the nested switch
print("testing getting a COPY TOP HAT OF MAIN SWITCH")
print('this also grabs and displays the inner switch first line')
#the inner switch needs to be the last line of this string
##================================================
start = 1 #starting from 11 not 10
finish = 10
#linecounter=0
abovenestedswitch=''
print("this was put into a function on July 15th, 2021 ===")
####################################
## copy_top_hat_of_main_switch(): #this grabs the string of the main switch above 
# the first nested switch in this case there is only on 
####################################
terriblysmart=''
def copy_top_hat_of_main_switch(): #this is grabbing the top of 
    #the switch case just above the first nested switch 
    print("======copy top hat of main switch()====")
    global abovenestedswitch
    linecounter=0 #string name find_nested_switch_game
    for line in find_nested_switch_game.splitlines():
         # between >= 1 and <= 10
        if linecounter >= int(start) and linecounter <= int(finish):
            abovenestedswitch += line + "\n"
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result copy above  first nested switch case ")        
    print(abovenestedswitch)
    terriblysmart = abovenestedswitch

#copy_top_hat_of_main_switch()  #not called yet

print("end of copying top half above nested switch ")  
print("it should end with switch which we will edit")

mystringtest='''
	switch() #7
		case 'funny':
			print('fun')
		case "da":
			print('yeah')
		default:
			print('bye')
	endswitch #14
'''					
					

####################
#replace switch

#linecounter= 0
newlist=[]
newlist.append(0)
#newlist[0]
# I just put this into a function to have control over it 
#COPY COATTAILS BOTTOM OF BIG SWITCH AFTER NESTED SWITCH END
################################################################
## copy_coattails_bottom_of_big_switch_after_nested_switch_end():
################################################################
def copy_coattails_bottom_of_big_switch_after_nested_switch_end():
    print("copy_coattails_bottom_of_big_switch_after_nested_switch_end()")
    linecounter=0
    start = 21 #INPUT PARAMS TO GRB need to put these in a list for efficiency
    finish = 32
    outerswitch=''
    for line in find_nested_switch_game.splitlines(): #string looping thru
        #   IF BETWEEN line numbers 21 and 32 
        if linecounter >= int(start) and linecounter <= int(finish):
            outerswitch += line + "\n"
            linecounter += 1
        else:
            linecounter += 1
            continue   
        
    print("testing getting a COPY COATAILS BOTTOM OF BIG SWITCH")
    print(outerswitch)
    newlist[0]=outerswitch
##===================================================





#this is turning code into a function on july 15th, 2021
#######======
#copy_coattails_bottom_of_big_switch_after_nested_switch_end()
#######=======





#here is where i make this temporary list that I will put the
#input strings of the main switch and the one nested switch for testing

inputstringswitches=[]

###################
##    swap(a,b)
###################
def swap(a,b,c): #c = starbucks[1]
    cooler =c.replace(a,b)
    return cooler #starbucks[1] =string with changes made
    
    
  
#this puts the nest_method on the line selected in the tophalf of the string
#################################
## swap_switch_for_nest_method(n)
################################# 
def swap_switch_for_nest_method(n): # I will add more values later perhaps 3 or 4 for coordinates
    global abovenestedswitch
    abovenestedswitch=terriblysmart
    print("called swap_switch_for_nest_method(n)",n)
    abovenestedswitch = abovenestedswitch.replace("switch(exp){","nested_switch_" + str(n) + "(n)")
    print(abovenestedswitch)
    print("===================")

#june 29th, 2021


def scan_input_string_for_number_of_switches():
    print('work on this')#I have this figured out now elsewhere
    
    
#commented this out on august 3rd testing making big method 
   
#this needs to be put into a method and called below actually
def fishfood(): #necessary testing that's all
    print('about to try new swap method')    
    swap_switch_for_nest_method(2) #feeds it the number 2 for testing
    outerswitch=newlist[0]
    outerswitch= makeitwork[0]
    maybe=abovenestedswitch + outerswitch
    print('we have stripped the nested switch from the main switch')
    print("and inserted a method for now")
    print(maybe)
    ######### put first main switch into inputstringswitches
    print("adding main switch and nested switch taken out into list")
    print("the next step will be to run it thru the silve_module")
    print(" to create teh strings output in python")
    inputstringswitches.append(maybe) #should be position 0

    print("and the nested switch is here before it's converted")
    print(makeitwork[0]) #roadrunner
    #roadrunner = roadrunner.replace("endswitch","}")
    ######### put nested switch into inputstringswitches
    inputstringswitches.append(makeitwork[0]) #should be position 1
    print("====== go for the gold =======")
    print("this shows the resulting strings accessed thru the list that")
    print("they were put into so I can access them now for running silve module")
    print("==--------------==")
    print("here is the result now")
    print(inputstringswitches[0])
    print("now the nested switch")
    #print(inputstringswitches[1])
    galaxy=''
    galaxy = inputstringswitches[1]
    print(galaxy)
    print("Now I replace endswitch with }")### replace endswitch with }
    inputstringswitches[1] = galaxy.replace("endswitch","}")
    print("now looking into inputstringswitches[1] endswitch should be gone")
    print(inputstringswitches[1])
    print("==== end of first major step ==in process of transformation ==")

#################===========
#fishfood()
#################===========




#############################
##  get_inner_switch_line()
#############################
def get_inner_switch_line():
    print("can we get serious here I mean really")       
    bronze=0     
    linecounter=0
    secondswitchline=0  
    for line in find_nested_switch_game.splitlines():
        if "switch" in line: 
            print(line) 
            linecounter += 1 
            print("switch line number = ",linecounter)
            secondswitchline = linecounter
            break
        else:
            linecounter += 1  
            continue
    print("line with inner switch =",secondswitchline)
    print("==================")
#the inner nested switch will obviously end within the same case it starts in.

###########==============
#get_inner_switch_line()  
###########===============


                
###########################################################
print("")
print("====")
print("")
print("get line number of each switch")
print("each number after first switch is a nested switch")
print("get the line number of each switch")
switcharoo=[]
switcharoo.append(0)

linecounter=0





#######################################
##  get_number_of_nested_switches():
#######################################
def get_number_of_nested_switches():
    print("get_number_of_nested_switches()")
    linecounter=0
    #this looks for the line number of 2nd switch for now more later  
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "switch(" in line:  #grabs first line
            print(line)
            switcharoo.append(linecounter)
            
            linecounter += 1
            continue  
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
              
            #if "switch_nest()" in line:
            #   print(line)
    print("line number of switches",switcharoo)  
    print(switcharoo[2])                

casecounter=0
case_count=0

##########========================
#get_number_of_nested_switches()
##########========================
###############################################################
################ testing call of these methods at once
###========== august 3rd test Tuesday nice air conditioning ====
def nested_switch_trapeze_tricks():
    print("==== nested_switch_TRAPEZE_tricks() called=====")
    loop_thru_switch_locations()
    get_case_line_numbers(find_nested_switch_game)
    get_larger_number_less_than_case()
    get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
    copy_a_nested_switch(find_nested_switch_game)
    copy_coattails_bottom_of_big_switch_after_nested_switch_end() 
    fishfood()
    get_inner_switch_line() #not sure if I need this one
    switcharoo=[];switcharoo.append(0);linecounter=0
    print("the nubmer of nested switches=")
    get_number_of_nested_switches()  # here it is 

#this calls it right here 
#nested_switch_trapeze_tricks()
#print("end of running nested_switch_trapeze_tricks() Gee what does it do")

####=============================== end of the line here==========



################################
## get line number of cases()
################################
def get_line_number_of_cases():
    print("get_line_number_of_cases()")
    for line in find_nested_switch_game.splitlines():
    #get each case number 
    #check if switch in it
        if "case" in line:  #grabs first line
            case_count += 1
            print("case_count=",case_count)
            print(line)
        
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
     
#answer 2nd case section    
#nested switch on line 10        
 #answer line 2 inside of case
 #case section 2 starts on line 8
''' OUTPUT
 get line number of each case section
		case 1 thru 3:
1
		case 4 to 7:
2
			case blable:
3
			case more:
4
		case 8 to 10:
5
case line numbers [0, 2, 8, 11, 14, 23]
Line 8 is case second section
We therefeore know that if switch is on line 10
then switch is on the 2nd line after the case section starts
====
get line number of each switch
each number after first switch is a nested switch
get the line number of each switch
	switch(exp) {  
			switch(exp){
line number of switches [0, 1, 10] <<<=== line 10 nested switch
'''
'''
 print('kangaroo hop hop!')
			switch(exp){
			case blable:
			   print("do something")
			   print("yep")
			case more:
			   print("nice")
			default:
			   print("we are done here")
			}'''  
    
    
    
#Monday june 28th, 2021 thinking
#get switch line number and case it's in and line number inside of case
#and what line the switch ends with }
#which I need to know to copy it. I can set the loop to start
#on a particular line and to concat a string and stop
#after coping a set number of lines. 
#Based on line count between switch and } which I can do first
#if line.startswith("switch") do until line startswith("}")




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






   
#def fantastic(): #we would know case number and therefore line number
#   newcounter=0
#  for line in output_string_test.splitlines():
#       if "case" in line:
 #          line_number.append(newcounter) 
       
       #and
       
       #I think that for the parser thats analyzing the input string
       #but the outoput python is quite different.
       #the nested method will be one line
       #so it's really  just adding the one line string
       #to a set of say 5 lines and moving the existing lines down 1 line
       
   #say second line after case 
   #test if something on that line
   #inner_switch_1('test7')
print("what can I do with lists")
print("the night is still young. competing with harvard and stanford")
red=[]
orange=[]
blue=[]
pink=[]
pink.append("\tempty")
red.append("\tone")
orange.append("\tdam")
blue.append('\ttuna')

super = pink[0]  + '\n'  +red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)
red[0] = "\tnestedswitchmethod" 
pink[0]= "\tfunny"
super = pink[0]  + '\n' + red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)

print("========")
line_1=[]
line_2=[]
line_3=[]
line_4=[]
line_5=[]
line_6=[]
line_7=[]
extra_line_1=[]
extra_line_2=[]
extra_line_1.append(0)
extra_line_2.append(0)
football =[]
football.append(0) #method name 
football[0]="\tinner_switch_1('test4')"

line_1.append(0)
line_2.append(0)
line_3.append(0)  #for example nested switch is line 3
line_4.append(0)
line_5.append(0)
#line_6.append(0)

#line_7.append(0)
 #say it's 4 line case 
line_1[0]="\tprint satement line 1"
line_2[0]="\tprint satement line 2"
########################################
line_3[0]="\tprint satement line 3"
line_4[0]="\tprint satement line 4"
print("================")
#if it's on line 3 we take top off to separate it 
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
# new
print("beginning state")
extra_line_1[0]=line_3[0]
extra_line_2[0]=line_4[0]

print("copying that will be don")
print(extra_line_1[0])
print(extra_line_2[0])

print("====bit flipping==== ")
print("putting nested switch in position 3 which is line 3")
line_3[0]=football[0] #designated line for nested switch 
line_4[0]=extra_line_1[0] #this is a novel approach restarting from 1
line_5[0]=extra_line_2[0]

print("after adding the switch nested method in position 3")
print('we then have this:')
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
print(line_5[0])
print("=========== now adding teh strings to magic concatting them ")
magic=''
magic = line_1[0] +"\n" +line_2[0] +"\n" + line_3[0] +"\n"+ line_4[0] +"\n" + line_5[0]
print(magic)  
print("=====================")  
print("let teh games begin")    
print("done")
#line_5[0]="line 5"
#line_6[0]="line 6"
#line_7[0]="line 7"
#line_8[0]="line 7"
mylist=[]
mylist= ["starter","one","two","three","four","five"]




def sosmart():
    mylist.insert(0,"starter")
    mylist.insert(1,"one")
    mylist.insert(2,"two")
    mylist.insert(3,"three")
    mylist.insert(4,"four")
    mylist.insert(5,"five")
    
    
def put_nested_switch_into_line(x):
    mylist.insert(x,"nested_switch") #it replaces the whole line
    print(mylist)
    
def reset_list():
    for item in mylist:
        del item
    
    print(mylist)

print("333333333333======333===================")
print("new attempt here  Friday June 25th -0--")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

print("======= water tower see how well this works=======")
print(mylist)
put_nested_switch_into_line(2)
sosmart() #resets it
put_nested_switch_into_line(1)
sosmart() #resets it
put_nested_switch_into_line(3)
sosmart()
print("===000000000000100000000000======")

# I ahve to split it in half somewhere and we have top above nested switch line
#and then we have the nestline
#and we have the bottom 

#so if we have lists for each line number of case section up to say up to 10 lines for now
#say switch will go on line 3 of 6 lines for an exmaple
#line 1 and line 2 are top
#line 3 is nest_switch_method
#line 4 to n is the bottom




     
case_guts='''
\tprint("aaaaaa in the main switch")
\tprint("bbbbbb below")
\tprint("ccccc#result of innerswitch running
\t#what ddddddd?? use a list to capture it
\tfallthr eeeeeeeu('word'
'''
    
    #method inner switch withnumber (input will likely be from a list later)
add_this="\tinner_switch_1('test4')\n"
nested_method_name=[]
nested_method_name.append(add_this)
crystal=[]
crystal.append(0)# [0]


#get input string of case section
#
# I need to get the line number where the switch is supposed to go
# based on the input C style location of the nested switch
# based on which case it is in (the sequence starts from 1)
# then detect the line number in order within that case where the switch starts
#
#
  
#exmaple, we need to add nested switchmethod to line 2
#so we copy line1

top=[]
middle=[]
bottom=[] 
put_in_here=[]

#### fudge ########    
def fudge():
    #def copy_one_line_inside_case(x)
    astring=''
    soupstring=''
    line_counter =0
    print(case_guts)  
    
    print("===========STAGE 1=========")  
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == 1:  #grabs first line
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print('first line string=',astring)
    #################
    newstring=''
    coolstring=''
    line_counter =0
# copy from the line where we want to insert (line 2) 
# thru to last line in case section
    print("============STAGE 2===========")
    #this copies 2nd string to string n (the rest)
    
    for line in case_guts.splitlines():
        if line_counter >= 2:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
        
    print(newstring) #this copies all of the lines into newstring
    put_in_here.append(newstring)
    #this is the switch method string on top of rest of case body lines
    #copy from targetline insertion line thur last line
    # we then add the nested switch method to the rest of the case 
    ##########################################
    #this will be a new helper method
    
    #def add switchline to rest of case body()
    #this is necessary BEFORE adding first line
    print("=================STAGE 3=================")
    egg=[]
    nested_switch_method_name=[]
    fossil=[]
    #fossil.append(0)
    #fossil[0] = nested_switch_method_name[0] + put_in_here[0]
    coolstring = add_this + newstring#how so I insert to front of a string
    #higher =nested_method_name[0] + put_in_here[0]
    egg.append(coolstring) #egg[0]
    
    #middle.append(coolstring)
    print(coolstring)
    glory=''
    #this adds the first string followed by coolstring
    #########################
    #this adds the line(s) above the insertion line 
    #put first string ontop of rest of lines of 
    #this adds the first line which was skipped to the new switch line
    #with the rest of the case body
    
    
    #def add_top_above_lines_above_switch_line(a,b)
    #a = string with the switch_method name
    #b = rest of the lines
    print("==========STAGE 4==========")
    nested_switch_method_name.append(astring)
    glory = astring + coolstring#[0] #now it's a list
    print("glory shows")
    print(glory)
                #method name in list     #nested method name + rest of lines in case
    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
    print('from list now') #string add_this
    print(egg[0])
    #bottom.append(glory)
    #print("now printing from the list bottom[0]")
    #print(bottom[0])
#   def add

#then replace first line with new line methodnested name
#    then add paste first line to new beginning of string
print('copy string from line 2 bbs')
fudge()
#now I can insert in line 2

print("========= result of fudge  ============ ")
print("========= Fudge Happy Potter Hogwarts ========")

#convertList = ' '.join(map(str,list1)) 















###################################
## copy one line inside of case (x)
####################################
def copy_one_line_inside_case(x):
    print("copy one line inside case()")
    astring=''
    soupstring=''
    line_counter =0
    #print(case_guts)    
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == x:
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print(' line',x,' string=',astring)
 ####################   
 #copy just the line entered within the case body
copy_one_line_inside_case(1) 
copy_one_line_inside_case(2)
copy_one_line_inside_case(3)
copy_one_line_inside_case(4)
copy_one_line_inside_case(5)






#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========








################################################
##  get_below_after_method_insertion()
################################################
def get_below_after_method_insertion(y):
    newstring=''
    coolstring=''
    line_counter =0
    #this copies 2nd string to string n (the rest)
    for line in case_guts.splitlines():
        if line_counter >= y:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
    print('below after method insertion',y)   
    print(newstring) #this copies all of the lines into newstring
    #this is the switchm

#this grabs lines within the case after the input line number to the end
get_below_after_method_insertion(2)
get_below_after_method_insertion(3)
get_below_after_method_insertion(4)
get_below_after_method_insertion(5)
 
egg=[]
#def stage_three(a,newstring):#("====STAGE 3====")
#    print('stage_three called')
#    coolstring = add_this + newstring#how so I insert to front of a string
#    egg.append(coolstring) #egg[0]


#stage_three(add_this,newstring)

### stage four ########
#def stage_four():
#    print('stage-four called') #method name in list     #nested method name + rest of lines in case
#    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
#    print('from list now') #string add_this
#    print(egg[0])  
    
#stage_four()    
#it's going to be in the code gen phase actually where I add the
#one line (so much easier) to the particular case that it's in
#and on the line number within that case below a particular line
#But I the main switch is generated so it should have a marker
#like nested_switch_1_3('test4')
#case number in series and line number within that case

# 
# 
# x=1
# def paste_inner_switch_method_into_string(x):
#      print("===================")#this goes thru the string and detects a nested switch
#      case_counter =0
#      for line in output_string_test.splitlines():    #and copies it and puts it into 
#         case_counter += 1    #acgtaully it gets the start and stop location line numbers
#         if "case" in line:
#             print("case detected in line")
#             case_counter += 1
#             if case_counter == x:
#                 print("this should be our match")
#                 print("this is case number ",case_counter,"and x=",x)
#                 print("therefore we do the MAGIC SHIT HERE")
#                 fantastic()
#                 break
#         else:
#             continue
# 
# list1=[]
# list1.append(0)
# def test_this():
#  #put it into a list
#     list1[0]="inner_switch_1('test7')"
#     say it's line 
# 
# #possibly have it scan thru the output python generated
# I might need a marker  #comment where to put it based on
# just the case. I can finangle where in a case I add it 
# since it's just a method and after I get it placed
# then I can change where in the case it is since it's
# within the case body so I have latitude and the body case 
# will be isolated so there should be some leeway. 





happydays='''
line =""
varholder=[]
varholder.append('0')
###############################============
	
# ===== inswitch ========
def inswitch(n):
	if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
		n = str(n)
	global case
	case = n.lower() 
#=====================
# for infallthru    
def infallthru(n):
	eval("inswitch('" + n + "')")
global x
x = "one" #it was "one"     
tahoe=[]
tahoe.append(0)
victory=[]
victory.append(0)
#######################
### inner switch_1(n):
#######################
def inner_switch_1(n): #test2 is the test
	print("=======inner_switch called==1==",n)
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
	inswitch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			infallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			infallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			infallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
			#######################
			print("out of inner switch 1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break   
###================
inner_switch_1(zoo[1]) #this calls it with zoo[1]
'''
##========================
##  darkness()
##========================
def darkness():
    print("darkness() =========")
    print(happydays)
    touble=''
    print("darkness called=====>>>>>>>>>=====>>>>")
    print("happy days analyze the pattern for the tabs and how many ")
    counter =0
    print("===================")#this goes thru the string and detects a nested switch
    for line in happydays.splitlines():    #and copies it and puts it into 
        counter += 1    #acgtaully it gets the start and stop location line numbers
        if "\t" in line:
            print("tab detected in line")
            trouble =line.count("\t")
            print(line)
            print("tabs=",trouble," ",counter)
            trouble=''
        else:
            continue
            
darkness()
  
  
  
  
  
  
           
print("HERCULES TEST RIPPING OUT TABS FROM FRONT")   
'''
to set adding tabs i realized there are two modes
regular switch and nested switch
and to subtract a tab i need to cancel nuke tabs in a line then add the desired number
to get what i want
'''  
import re
myString = "\t\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
print(myString)
print("now rip out the tabs")
myString = re.sub(r"[\t]*", "", myString) #was * where I have 2
print(myString)   
print("now add a tab")

myString = "\t" + myString
print(myString)    
myString = "\t" + myString #add second tab
print(myString)              
            




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






##### this makes the input for zoo[1] lowercase
###############################
## make_input_lower_case() ####
###############################
def make_input_lower_case():
    answer = zoo[1]
    answer = answer.lower()
    zoo[1] = answer    

# what i doing here is putting the dynamic built inners switch python code into a list.
# this is just beautiful and brilliant.

fiddle=[]
fiddle.append(0)
fiddle.append(happydays) #appends the string and puts it into fiddle[1] and exec()
#print(fudge[1])
print("TESTING BLADE RUNNER SERIES =what does an innerswitch by itself need")
print('it is all in one big string about to execute it')
#THIS IS CRITICAL INPUT IN   zoo[1]
zoo[1] = 'test3'# testing (user input lower or upper)
make_input_lower_case() #this converts the input for nested
#see if it works
print(fiddle[1])

exec(fiddle[1]) #this is executing the nested switch method above




sewage = ''
#for item in fiddle[1]:
#    sewage += item
#print("sewage=",sewage)
#print("=====")   
#x =sewage.replace("\t","\t*") #this is so I can see the tabs



#right here 

## add this to it:  
#def inner_switch_3(n): # 
samplecode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
	inswitch(n) #3 
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			infallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			infallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			infallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			inner_switch_2('test7') #commented out
			#######################
			print("out of inner switch 1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break
'''

#modified on november 12th 2021 friday to get this sucker working 
##====================================
##  get_switch_number_in_comment()  it gets the switch number from FIRST LINE OF STRING then bails
##====================================
#this looks ofr the first switch at 3 tabs need to modify it to 1 tab depth. aha 
def get_switch_number_in_comment_in_output_python_code_string(stringname): #this might be for when
	print("get_switch_number_in_comment_in_output_python_code_string(stringname)")
	print("indian braves dancing for rain")
	# I create copies of the switch body strings
	print("get_switch_number_in_comment_in_output_python_code_string() called it's getting the first inner swithc at 3 tabs length ")
	awesome=''
	y = ''
	counter =0  #say it's 3
	print("this is what the string we are manipulating looks like")
	for line in stringname.splitlines():
		print(line)
	print("================-------===")
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter =0 #this looks for inswitch at 1 tab depth length 
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tablength= line.count("\t")
		if "inswitch" in line and "end" not in line and tablength == 1:#and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number ",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;



flynow=[]
###============================================================================
##  put_output_python_nested_switch_code_into_def_inner_switch_numbered(string):
##==============================================================================
#try this november 12th struggling here 
#I want to see this
'''
def inner_switch_3(n): 
    print("=======inner_switch called==3==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    inswitch(n)                           #<<====== inswitch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
'''

def put_output_python_nested_switch_code_into_def_inner_switch_numbered(stringname):
	print('===== TESTING RED ALERT ======')
	print("put outpout python nested switch code into def inner switch numbered")
	#this calls a method to get this switch number to use to number this nested switch
	thenumber= get_switch_number_in_comment_in_output_python_code_string(stringname) #use other code similar to this
	#print("the number it returned is",thenumber) #thenumber=22 #for testing
	string_to_add= "def inner_switch_" +thenumber.strip() +"_(n):\n"
	concatstring = string_to_add + stringname;
	#print("lets see if it actually worked or not and concatted it correctly")
	##################################
	for line in concatstring.splitlines():
		print(line)
	flynow.append(concatstring) #so the resulting string modified exists.
	#########################

#thenumber=22
#string_to_add= "def inner_switch_" + str(thenumber) + "(n):" 
put_output_python_nested_switch_code_into_def_inner_switch_numbered(samplecode)
#makeitso = string_to_add + samplecode;

def testit():
    print("testit called to see if I put def nested method at top of string")
    print("doing samplecode first in virgin form")
    for line in samplecode.splitlines(): #unchanged original output string
	    print(line)
    print(":")
    print("end of test run....")
    print(":")
    print("and now after putting def nestd switch numbere at top")
    print("did this sucker work....please...")
    #for line in makeitso.splitlines():
	#    print(line)
#testit() 
    
dumbstringcode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
			
	switch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			fallthru('test2')
		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print (" case behavior works in Python now!")
			print("")
			fallthru('test3')         
		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			fallthru('test4')
		elif case in caselist4: #['test4']
			print ("testi  first nested  ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
			#######################
			print("out of inner  1")
			print("")
			break
		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break
		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break
		#default:
		else:
			print('None')
			break
'''


fridge=[]
fridge.append(0)


print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
#================================================
x =dumbstringcode.replace("switch","inswitch")
dumbstringcode=x
y = dumbstringcode.replace("fallthru","infallthru")
supergood = y
#=================================================
####### this fixes a bug of the inner switch getting an extra in and it's taken out
#######3=======
print("--------000000000000---testing changing switch and fallthru ====")
print("-------=0000000000000  into inswitch and infallthru ------")
print("testing conversion of a python string of a nested switch")
print("to tranform it into inswitch(), infallthru()")
print("this should be the working version of ")
print("have changing switch to inswitch and fallthru into infallthru")
print(supergood)
print("did it finally work or not===========>>>>>")
z = supergood  #this fixes a bug where the nested switch method is wrong
y = supergood.replace("inner_inswitch","inner_switch")
print("and this should fix the bug of accidentally namming inner_switch")
exam = y
print(exam)
print("===== end of good working code ==============")

#for line in dumbstringcode.splitlines(): #switch case in JS
 #   #print("smartcounter =",smartcounter)
 #   
 #   if "\t\t\tswitch" in line:
 #        umbrella += "inswitch(n)\n"
 #   if "fallthru" in line:
 #       umbrella += "infallthru(
 #       
 #              
       #this is the range I want to print



#this is where the swo string is I was looking for.

print("july 3rd test 2021 6:53 pm")
print("testing nested switch string BETA TESTING ====0")
#find_nested_switch_game ='''
#clever('4')
swo ='''
	switch(exp) { #first true test 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){     # inner s w i t c h      
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


#this one has two nested switches that I will try next. 
swo_next ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # inner s w i t c h     =============  
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #=========================
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 28    ===============   
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #38===================================
			fallthru
		
		default:
			print('the end')
}
'''	
# I seem to recall a bug usin

#this is testing sensing a multiline switch with more than one switch
####===============
#testing moved here for safety
# CHECK FOR THE NUMBER OF SWITCHES WITHIN THE INPUT STRING
nested_switch=[]
nested_switch.append(0)
nested_switch[0]= False # by default
################################################################################
#determines if a string input is a nested switch with at least one inner switch
################################################################################

###################
##  jumanji(y)       tests if string input has at least one nested switch
###################  sets nested_switch[0] = True
def jumanji(y):  #instead of this I just do a count for endswitch which is just one line of code. 
	print("--------------------------")
	print(" --- J U M A N J I -------")
	print("--------------------------")
	print("this determines if it's a nested switch with a nested switch or more in it")
	print("testing jumanji() counting switches and endswitches")
	#just some sample ifs to read what's the input look like 
	print("this is looking into the string below")
	#print(swo)
	print("--- end of string that we will analyze ---")
	print("")
	print("get count of lines startingwith switch in the string")
	#this counts switch number in the string
	switchcounter=0
	for line in y.splitlines(): #determine if switch is in line
	#this looks for switch in the line but endswitch can't be in this line
		if "switch" in line and "end" not in line:
			switchcounter += 1  ## SWITCH COUNTER
			#print("switchcounter=",switchcounter)
			print("yea this starts with switch")
			continue
		else:
			continue
	print("total switches =",switchcounter)
	
	##============================
	#this counts endswitch number in the string
	print("get count of lines startingwith endswitch in the string")
	endswitchcounter=0		
	for line in y.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line: 
			endswitchcounter += 1  #END SWITCH COUNTER
			#print("endswitchcounter=",endswitchcounter)
			print("yea this starts with endswitch")
			continue
		else:
			continue
	print("TOTAL endswitches =",endswitchcounter) #endswitchcounter
	print("end of this checker ===========")
	print(" total switches",switchcounter, "and total endswitches",endswitchcounter)
	
	#this sets the flag in nested_switch[0] if at least one nested switch
	#===============================================
	#if one or more switch and one or more endswitches
	if switchcounter > 1 and endswitchcounter >=1: #actually if endswitchcounter 1 it's True
		nested_switch[0] = True
	else:
		nested_switch[0] = False
	
	print("the result of this test for if this has nested switch(es)") 
	print("this is the list with the critical nested_switch[0] value")
	print("WHAT DOES THIS SAY --  it should be True")   
	print("nested_switch[0] = ",nested_switch[0])
	print("=================")
	print("=================")
	print("this  below this is dog breath that doesn't work")
	print("====== end of this initial switch counter filter that will eventually")
	print("=== trigger bypass205 to do multiple switches ====")
	
	
#end jumanji()  ===================||	
	
jumanji(swo)  #called here to test it
print("just called jumani with swo and if nested switches below will be True")
print(nested_switch[0])
#this should be the output the nested switch copied








#this is still using endswitch they aren't swopped out yet

## July 5th, 2021  testing Monday July 5th line number 1593
# July 18 added a second nested swithch to test on lines 28 to 38
samplestring ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch  #======== ============38
			fallthru
		
		default:
			print('the end')
}
'''	


samplestringzoo1 ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			print('hello world')
			switch(exp){  # ===== 24===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'rats':
					print("do autumns")
					print("yep")
					fallthru
				case 'more':
					print("badness")
					break
				default:
					print("we tesla done here")
			endswitch  #========== 34  ==========notice this for it is key 
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======39       
				case 'autumn':
					print("falling leaves")
					print("a night on the town ")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much cranberries")
			endswitch  #======== ============49
			fallthru
		
		default:
			print('the end')
}
'''	


#######################
#### testing ######
### samplestring with switches taken out ####
#### and nested methods replacing it ########
######## july 22 ###testing #####
##### this represents the accurate main switch with proper indentation
samplestring_main ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			nested_switch_1(n)
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			nested_switch_2(n)   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''	


#nested_switch_2(n)
#july 21st 2021 get teh number of lines in the string
# count endsswitches to get number of nested switches
# do the main switch last which erases(skips) the nested switches
#here I count the number of lines in the string to get last line 
# the tricky part was figuring out when to grab the main switch but I couuld actually
#do it first it doesn't matterand make a copy of it and modify the copy


#so I would add a third record to the pears dictionary 1, 44
######=== total lines in the string for the main switch =========
#using the whole string I know that the nested switches will be on the first line
thecounter=0
for line in samplestring.splitlines():
    print(line)
    thecounter += 1
    
print("the total lines =",thecounter)
print("================ wile e coyote =======")





tuna ='''
	exp = '4'
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp = 'blable'
			switch(exp){  #this one has input here         
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
			exp = 'fish' #and we have input here too. 
			switch(exp){          
				case 'fish':
					print("do something")
					print("yep")
					fallthru
				case 'trout':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			fallthru
		default:
			print('the end')
}
'''




# ibm list is used for holding switch strings 
ibm=[]
ibm.append(0)

use_number=[]
use_number.append(0) #[0]

#def between(x,condition,y):
    
#experimentatl copy the nested switch ignore the rest and only Do one.


#this only copies one nested switch within the main switch
#this i pased on knowing the input 
#these are hard coded here

#just put this here to see if it works correctly
# saturday july 17th, 10:11 am starbucks
print("STARBUCKS CRUCIAL testing saturday morning")
'''
this is first emptyhing the switch and endswitch locations lists
'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





print("the one below this line should produce 2 switches and one with 10,20")
#this find the location one one pair of a nested switch and end switch

#this gets the start and end from samplestring
#empty_switch_and_endswitch_list_locations()



#this has the output of filling these lists
#switch_location
#endswitch_location

print("stopping this now to see what it looks like with the switch list and endswitch list")
#return  # to stop the program
''' THIS IS THE OUTPUT OF RUNNING THE FUNCTION ABOVE
===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === 
I need to delete teh first swithc location
switch_location= [10, 28]
endswitch_location= [20, 38]
'''

print("=== shazam level about to try fancy stuff ====")

#loop
#pairlist is actually a list 
pairlist=[];theforce=[]
#this would just add the switch location
alpha='';beta ='';counter =0;jedi='';
#this reads in data from switch_location
#               and from endswitch_location
#======================================================
# fill_pairlist_with_switch_and_endswitch_pairs(yy):
#======================================================
def fill_pairlist_with_switch_and_endswitch_pairs(yy):
    print("====fill pairlist with switch and endswitch pairs()=====")
    print(" godzilla ruled over rodan ")
    get_switch_and_endswitch_locations(yy) #===== using sample stringh 
    print("this is grabbing the switch locations which are dynamically added to a dictionary for pairlist")
    print("the length of switch location =",len(switch_location))
    print("the length of end switch locatoin =",len(endswitch_location))
    print("==============...............============")
    # loop thru list switch_location ==============================
    counter =0;allpha='';beta='';           #so this is one small set switch and endswitch line numbers
    for item in switch_location: #this loops thru the list switch_location          
        alpha = switch_location[counter]
        beta  = endswitch_location[counter] #they should be the same length 
        #here the positions are appended to pairlist dictionary
        pairlist.append([alpha,beta])       #always in sets of 2 #adds alpha and beta as list into pairlist  list
        print("pairlist=",pairlist)
        counter += 1
    print("======================")
    newcounter=0
    print("the length of the pairs =",len(pairlist));print('let me see what is in pairlist')
    print("pairlist=",pairlist)
    for item in pairlist:  #this is the combined pairlist
        print(item)
        sosmart = pairlist[newcounter] #here I access first and second numbers in pairlist
        print(sosmart[0]);print(sosmart[1]) 
        print("====== JEDI TEST ========")#not to be confused with jumanji above 
        #this takes in data from switch_location list and endswitch_location
        # and glues them together into a new pair list into 
        # list called theforce
        #this is constructing filling the data in the dictionary pair values
        jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
        print('jedi=',jedi) #like this [12,16]
        
        #put pairs into list into jedi and append to theforce
        theforce.append(jedi) #the pair is added  to theforce list
        turbo  =theforce[newcounter]
        newcounter += 1
    print("theforce=",theforce)
    print("the length of theforce list =",len(theforce))
    print("did we make it this far... in a galaxy")
    #adding loop here to test this
    print("doing a newest test  christmas tree of the pairs in list theforce")
    acounter=0
    print("====magic brew time=====")
    print("== the filled list with pairs of switch endswitch is called theforce ===")
    for item in theforce:
        print(item)
        print("=======")
        cool =item
        print("cool=",cool)
       
        print("acounter=",acounter)
        x=''
        x = cool.split(",")  # see if this trick works
        print(x[0], x[1]) # see if this trick works
        print("end game")
        acounter += 1
        continue
    print("end of printing each item in theforce")
###=====





thisdict ={}


def cleanse(x):
    x = eval(x)
    return x;
    
#modified this method on august 11th wednesday, 1:11pm
############################################
##     adding data list to dictionary
############################################
def adding_data_list_to_dictionary(dictname,key,newdata_list):
    print("LOOK AT THOS at input params see if they are right first")
    print(dictname)
    print(key)
    print(newdata_list)
    return #temporarily halts this from running
    
    print("called adding data list to dictionary")
    #tryit =eval("" + dictname + "[" + key + "]" + "= " + newdata_list +"")
    #tryit =eval("" + 
    angel =dictname
    thekey= key
    newdata_list
    print(angel)
    print(thekey)
    print(newdata_list)
    print("====>>>====>>>end of games...")
    #print(tryit) #to see what it sees
    
    #thisdict["4"] = "[12,22]" #adding data list as string to dictionary
    
    #eventually I will add 1 to dictionary length
    
    ##########################################
    #dictname + key + [12,22] input format 
    ##########################################
    #dictionary name should be known
    print(thisdict)
    for item in thisdict.values():
        print(item)
    print("testing getting value in dictionary by key")
    x = thisdict["4"]
    
    #x = thisdict.get("4") #this should work also
    print(x) #together
    x = eval(x)#just dreamed this up and it worked
    print("this represents getting the x and y for a nested switch locations")
    print("first number",x[0])#seperate
    print("second number",x[1]) #separate
    
    
        
#OUTPUT
'''
called adding data list to dictionary
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, '4': '[12,22]'}
Ford
Mustang
1964
[12,22]
testing getting value in dictionary by key
[12,22]
first number 12
second number 22
'''
print("fast wile e coyote test  adding data list to a dictionary")
print("==========")
print("==========")

# october 28th, 2021 thirstday
# I need to go thru combined pair list three + five + seven and feed it into a dictionary

## its really get index pair in struct
#### get_number_in_struct(x)   THIS WORKS!!!!!!!!!!! oct 26th



pair_returned=[]

##======================================
##  get_number_in_struct(x):
##==================================
def get_number_in_struct(x):
    print("get_number_in_struct(x) called")
    print("the input was x",x)
    print("get_number_in_struct(x) called too cool")
    print("get ",x)
    #using eval() to do thisdict.get(x)===###################
    apple_pie=eval('thisdict.get(x)')
    print("=====///get number in struck(x) called---------///")
    print("get number ", str(x), " in struct with x called")
    print("apple-pie=",apple_pie)
    super = apple_pie
    if apple_pie == None:
        print("it is None")
    else:
        print("why not",super[0],super[1])
        print("now splitting it into the two numbers within the pair of switch endswitch")
        print(super[0])
        print(super[1])
        #doing this to have common lists for passing on to other functions later
        pair_returned.append(super[0])
        pair_returned.append(super[1])
        print("pair_returned at this point has",pair_returned)
#=============================================


    
#adding_data_list_to_dictionary(thisdict,'5','[12,22]')
print("washing machine time add this '5','[12,22]')")
print("thisdict",thisdict)
numb = '6'

thisdict[numb] = [23,47] #this worked
print("pretty autumn testing")
goaway=''
goaway = thisdict['6']
print("fishfood =",goaway)
print('dirt simple test')
'''
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now 
  "2": [11,60],
  "3": [15,51],
  "4": [23,46],
  "5": [31,41],
  "6": [62,86],
  "7": [66,77]
 #no comma after last data piece apparently
}
'''

#=======================
#add data to struct
#======================

print("no time for pumpkin carving")
#numb = number and aset = [start,stop]
aset=''
numb=''
# this method works on oct 26th 2021
##==============================================
## add_data_to_struct(thisdict,numb,aset)
##====================================================================
def add_data_to_struct(thisdict,numb,aset):
    return #abandoning this too confusing going with just a list of lists
    print("add data to struct")
    print("numb=",numb)
    print("aset=",aset)
    #numb='12' #the number will keep a rolling total and added automaticaly
    thisdict[numb] = aset  #this just seems too simple.
    print(thisdict) 
    
#add_data_to_struct(thisdict,numb,aset)
##============================

gooddata=[]
##==========================================
## get value in dict (name ofdict,x)
##==========================================
def get_value_in_dict(name_of_dict,x): # we will know the dict it won't change
    return #abandonning this for being too confusing and unworkable at this time
    print("plumtree=",plumtree)
    print(thisdict)
    print("get value in dict",x)
    nn = plumtree.get(str(x))
    print("================")
    print("using key",x,"it retrieved from the plumtree dictionary",nn)
    print("================")
    # I was assuming (wrongly) that all keys input would be in dictionary; unknown
    if x in thisdict: #it can't be this simple
        y=eval("plumtree[x]")
        print(y)
        del gooddata[:] #clears it out 
        print(y[0],y[1])
        gooddata.append(y[0])  #this returns with the index[0][1]
        gooddata.append(y[1])
    else:
        print('x',x,'is not in dictionary plumtree')
    
#this builds a new record
#numb='2'
#aset =[11,47]
#thisdict[numb] = data1
#print('input of 2 for [11,47]')
print("==tuesday testing ==add data to dictionary and then access it")
#add_data_to_struct(thisdict,numb,aset)
'''
if '2' in thisdict:
    print('yes 2 is in thisdict')
else:
    print("nope no 2 in thisdict")
#get_value_in_dict(thisdict,'1')
'''
##==========================

print('testing right here === bingo time === adding data to a struct')
#aset =[10,30]
#numb='2'
print('before adding the numbers pairs')
#add_data_to_struct(thisdict,numb,aset)
###=================================


#print(thisdict)
print("should have 2 and 11,47 added to it above")
print("==== boo ==========")
print("cool little test here getting data from dictionary struct")

# GET NUMBER IN STRUCT
#get_number_in_struct('2') #should be [11,47] #it really gets the pair data
#what exactly does this return
#print("output is this ========> ",pair_returned[0],pair_returned[1])
#print("should be  11 and 47")
##===========================
print("cafe borrone coding time")
#aset=[21,37]
#numb='12'
#dictname=thisdict
#add_data_to_struct(dictname,numb,aset) ###====================
#apple_pie=thisdict.get('12')
#apple_pie = aset
#print("should be 21, 37",apple_pie)
#aa = apple_pie[0]
#bb = apple_pie[1]

#print(aa)
#print(bb)
print("====")
print("get thisdict 9")
print("========= happy coding time ====")
#get_number_in_struct('9')
#get_number_in_struct('12') 
#print('should return [21,37]')
print("====== mocha ice drink ====")
#this retrieves the data based on 9
print('porsche time...........')



#apple_pie=thisdict.get('12')
#print("apple pie =",apple_pie)
print("where are we now")


print("stanford football test...")

#print(thisdict)
#print("======values======")
#for x in thisdict.values():
#    print(x)
#print("==========")
#print("=======items=====")
#for y in thisdict.items():
#    print(y)

#x='2' 
#get_number_in_struct(x)
#x='6' 
#get_number_in_struct(x) 
#x='9' 
#get_number_in_struct(x)
#x='12' 
#get_number_in_struct(x)       
#print("======= gameover ======")
#I will need to loop thru the dictionary blueberries
# so now I am on my way of loading the dictionary which will
#just happen once after the pairs are created.

#print(apple_pie) #should be [22,44]
#print("=====")


#x='9' 
#get_number_in_struct(x)   
#print("should return [22,44]")
#thisdict["GTI"] = [75,85]
#print(thisdict) #should include Cherry=[23,47]
#apple_pie=''
#print("below this it should be 23,47")

#x='6' 
#get_number_in_struct(x)   #should return [23,47]
#print(apple_pie[0])# = 23
#print(apple_pie[1]) # = 47
#apple_pie=thisdict.get('GTI') #should return [23,47]
#print(apple_pie)


#creating a dictionary with initial values (brilliant)
#this is new for oct 7 thursday, 2021 morgan hill starbucks
#data =dict() #create empty dictionary
#data =dict(a=1,b=2,c=3)   #short and sweet fill with initial values
#print(data)

#change a value in a dictionary
#thisdict["year"] = 2018

#if "model" in thisdict:
#    print("yes model is one of the keys in thisdict")
#    
#    #add item to dictionary
#    thisdict["color"] = "red"
#    
#update command
#thisdict.update({"color":"red"})


'''
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now 
  "2": [11,60],
  "3": [15,51],
  "4": [23,46],
  "5": [31,41],
  "6": [62,86],
  "7": [66,77]
 #no comma after last data piece apparently
}
'''
plumtree={} #new dictionary
####=======================================================
#feed list of pairs into dictionary (such as blueberries)
print("testing looping thru list")
#this represents a list of sublists of the switch,endswitch pairs
#I need to make testlist
testlist=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]

returnlist=[]
returnlist.append(0)
#I can make my own custom methods to get from list
#the list is actually referenced starting from 1 where I start the counter
##==============================================
##  get_pair_from_testlist(x):
##==============================================
def get_pair_from_testlist(x):
    print("=========get_pair_from_testlist=========")
    print("testing get_pair_from_testlist",x)
    counter = 1
    print("inside the loop we see for x this ",x)
    for item in testlist: #it doesn't really loop, it's a one pass loop
        #if number entered bigger then length of list warn then break    
        if x > len(testlist): #error detection bypass worked 
            print("ERROR went beyond number length in list")
            print("please enter a number less than ",len(testlist))
            break
        #if number entered less than 1 warn then break
        if x < 1: 
            print("ERROR number must be 1 or higher")
            break
        if counter == x: #it matched with a doable number
            print(item)
            alpha = item[0]
            beta  = item[1]
            print(alpha,beta)
            returnlist[0] = [alpha,beta]
            print("returnlist[0] =",returnlist[0])
            break
        else:
            break
##==============================================================

            
get_pair_from_testlist(1)
get_pair_from_testlist(1)
print("the pair is ",returnlist[0][0],"really cool",returnlist[0][1])
get_pair_from_testlist(-1)
get_pair_from_testlist(0)
get_pair_from_testlist(2)
get_pair_from_testlist(3)
get_pair_from_testlist(4)
get_pair_from_testlist(5)
get_pair_from_testlist(6)
get_pair_from_testlist(7)
get_pair_from_testlist(22)

#Okay. I need to fill the testlist from the threetabs, five tabs seven tabs nine tabs



#the list with the pairs is in testlist

#this dictionary is being abandoned for over complexity and confusion
# november 3ed 10:03 am morgan hill

#this reprents looping thru the testlist and filling data into the dictionary and populating it
##====================================================
##  fill_the_struct_dictionary_with_the_list()
##====================================================
def fill_the_struct_dictionary_with_the_list():
    return
    print('fill the struct dictionary with the list')
    counter=1
    # loop
    for item in testlist:
        print(item)
        aset=[item[0],item[1]]#this creats teh apirs 
        numb=str(counter) #making it a string here . clever
        thisdict=plumtree
        #add_data_to_struct()
        add_data_to_struct(thisdict,numb,aset) ###==============
        print("=======")
        counter += 1

        print("plumtree DICTIONARY now looks like this")    
        print(plumtree)
        print("here we go time to see it work===looping thru plumtree struct=====")
        for x in plumtree.values():
            print(x)
    
        print("===========")    
        for k, v in plumtree.items():
            print(k, v)
#what I am working on his dynmcially loading the 
#from the list to filling the blueberries dictionary
#this returns the index[0][1]
#THIS IS THE METHOD TO FILL A STRUCT RECORD HOLDER FROM A LIST 
#print("I need to empty plumtree dictionary first")
#plumtree.clear()
#print("just emptied plumtree dictionary")
#fill_the_struct_dictionary_with_the_list()




### MORE TESTING HERE ACCESSING THE DICTIOANRY PLUMTREE TO GET THE PAIRS DATA

#print("testing if this will actually work or it's an illusion")
#get_value_in_dict(plumtree,'1')


#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])
#print("====... did it work terrible =")



#get_value_in_dict(plumtree,'2')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'3')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'4')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'5')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'6')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])

#get_value_in_dict(plumtree,'7')
#print("gooddata[0]=",gooddata[0],"gooddata[1] =",gooddata[1])


#print('testing getting pair based on number in plumtree')
#apple_pie=plumtree.get('2') #notice it's not a string
#print("it is for '2' this",apple_pie)

#apple_pie=plumtree.get('1') #notice it's not a string
#print("it is for '1' this",apple_pie)

#apple_pie=plumtree.get('2') #notice it's not a string
#print("it is for '2' this",apple_pie)

#apple_pie=plumtree.get('3') #notice it's not a string
#print("it is for '3' this",apple_pie)

#apple_pie=plumtree.get('4') #notice it's not a string
#print("it is for '4' this",apple_pie)

#apple_pie=plumtree.get('5') #notice it's not a string
#print("it is for '5' this",apple_pie)


def testing_pair_list():
    return #not testing this right now
    print("length of theforce=",len(theforce))
    print("together_pair=",together_pair)
    print("======testing pair list() == fireworks time in tahoe ====")
    print("theforce[0]=",together_pair[0]) #first pair coordinates start stop
    print("theforce[1]=",together_pair[1]) # second pair coordinates start stop
    print("===starting loop thru list theforce =======")
    newcounter=0
    print("dog breath test")
    for item in together_pair:
        print(item)
        #this only works for two numbers 2 number long currently
        dog = together_pair[newcounter] #here I access first and second numbers in pairlist
        x = dog.split(",")  # see if this trick works
        print(x[0])
        print("doing surgery cutting off first character")
        charlie=''
        charlie = x[0]
        super=x[1]
        print("super=",super)
        print("=====")
        charlie = charlie[1:]
        print("charlie =",charlie)
       
        super =super[:-1]
        print("super=",super)
        print("===...=.=.=.=.=.=.=.=.=.=.")
        print("===...=.=.=.=.=.=.=.=.=.=.")
        charlie=''
        charlie = x[0]
        charlie = charlie[4:]
        print("charlie =",charlie)
        #print(x[1])
        print("==========")
        newcounter += 1 #python doesn't have ++
        
    print("=== end of looping thru list =======")
    
    
print("MAJOR TEST august 7th, 2021 morgan hill starbucks mocha time")    
print("testing this dam code again...")    

#=======================================================
## this makes the pair list for locations of nested switches august 7th, 2021 
print("DOING TEST of PAIRS of switch and endswitch necessary to do copy and skip comamnds")
print("===================== big test today wednesday =========")
print("what this entails is the mechanics of switch and endswitch locations")
print("which need to be dead on to work correctly for separating the nested strings")
print(" ---- THIS MUST WORK DEAD ON --- for the show of separating teh strings")
print("  --- so this creates the information needed to correctly separate the strings")
print(" === puff the magic dragon time here august 11th ===")
fill_pairlist_with_switch_and_endswitch_pairs(samplestring)
testing_pair_list() #this shows the outpout of grabbing the switch
# and endswitch pairs (sets)



#this way I can use the pair list to copy the nested switches
#========================================================

#print("oh wow does this actually PEAR TREE SHAKE  work pairlist below")
#print("number of pairs =",len(pairlist)) #this is beautiful!!!

#print("oh wow look at this pairlist I made=== starbucks mocha===...")
#print("the length of pairlist =", len(pairlist))
#print('after first attempt')
#sosmart =pairlist[0] #first position
#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])




#print("====== JEDI TEST ========")
#this is constructing filling the data in the dictionary pair values
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#this is building a pair [4, 8]   #an example 

#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)
#theforce.append(jedi)


#print("I simply add the jedi string which is a list (brilliant)
#print("to theforce list sooo nice")
#make a method here 

#fill jedi with one set 
#print("=======NEXt JEDI TEST ======")
#sosmart =pairlist[1] #second position meaning second nested switch 


#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])
#x = 10
#y = 20
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)

# feed jedi set of 2 numbers into the forcelist with an append
#was theforce
#theforce.append(jedi)

#print("theforce=",theforce)
#print("the length of theforce list =",len(theforce))

########################
#print("the =========== force here ========force shows",theforce)
#print("theforce[0]=",theforce[0]) #set one of pair of a switch start and endswitch
#print("theforce[1]=",theforce[1]) # set second pair of a switch and endswitch locations

# so this is building the pears lists of switch endswitch so then I would add the pearslist
#to a dictionary now I think. 

############













#this would just add the switch location


#I can createa  new list to make the pairs first
#go thru grabbing the first number first
#then on the second loop add the second the endswitch

#fill the pears dictionary now
#exit()


#print("switch_location=",switch_location)
#print("endswitch_location=",endswitch_location)

#what is the output???
print("snow man here ")
print("I need to have it flow into the range below lists")
#these are hard coded in here 
print("the output from get swtich and endswitchlocatin for samplestring")
print("right below this line")
print(" RODAN FLYING......")

#for some strange reason the get swithc and endswitch locations are off by 1

#switch_location[0] -=  1
#endswitch_location[0] -=  1
#print("what type is it switch_location[0]",type(switch_location[0]))
#test =switch_location[0] 
#test=test-1
#switch_location[0] = test
#print("switch_location now",switch_location)

#test =endswitch_location[0] 
#test=test-1
#endswitch_location[0] = test
#print("endswitch_location now",endswitch_location)

##============================================================
#these are in switch_location and in endswitch_location


######################################################
list_of_switch_range=[]
list_of_switch_range.append(0)
list_of_switch_range.append(0) #was 10 hard coded 
list_of_switch_range.append(0) #was 20 hard coded

#list_of_switch_range[1] = switch_location
#list_of_switch_range[2] = endswitch_location
##############################################################
## july 17th, 2021 11:12 am
print("IS THIS WORKING OR NOT ==========")
#here we feed the input switch and endswitch into range lists
#THIS WORKS FOR JUST ONE INNER NESTED SWITCH 

anest_string='''
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
'''
print("wild wild west test...")

###########################################============
#experimenting on nov 4th thursday 
get_first_switch_test='''
			switch(exp){ #21         
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
'''

get_first_switch_da='''
			switch(exp){ #  54         
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					switch(exp) # 98
					break
				default:
					print("we are done here")
			endswitch 
'''

# get first line with switch get the number after comment
# append that number to a list
#first_switch_list.append(number)
got_the_number=[]
##====================================================
##  get_switch_number_at_top_of_string(stringname):
##====================================================
def get_switch_number_at_top_of_string(stringname):
	awesome=''
	counter =0  #say it's 3
	#this will only get the number from the FIRST SWITCH it encounters
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		print(line)
		print("the counter here is",counter)
		if "switch" in line and "end" not in line and "#" in line: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number is",y)
			y=y.strip() 
			got_the_number.append(y)
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;


# here I would add the strings in quail after they have been separated
# and they are in the list mytestlist. I then apply a method to each
# string to get teh switch number at the top and append it 
# to the list got_the_number
 # I will need to loop thru the quail list of the seperated switch strings
 # and append the strings within to mytestlist
 #so actually I would loop thru quail list and call get switch number

mytestlist=[]
mytestlist.append(get_first_switch_test)
mytestlist.append(get_first_switch_da)
del got_the_number[:] #clear out this list at the beginning

#loop thru list with thes trings
#feed the strings into method get switch number at top first switch
##=====================================================
## get_first_switch_number_from_all_strings()  fly jets
##=====================================================
def get_first_switch_number_from_all_strings():
    print("get_first_switch_number_from_all_strings()")
    for item in mytestlist: #this will be quail list before parser
        get_switch_number_at_top_of_string(item)


get_first_switch_number_from_all_strings()
print("really got_the_number=",got_the_number)
# this will be my so-called twin list
# that I will use 
# for the python outoput strings in the stanford list
# to use to make the nested_method names for the defs


#exit();

#
'''
 this transfers the line location of switch and endswitch
 to list of switch range 1 and 2 from 
 switch_location and endswitch_location
'''
#28,38 for second string
# I am skipping using this now NOT using this method 
##################################################
##  get_one_nested_switch_start_and_finish()
##################################################
def get_one_nested_switch_start_and_finish():  # this gets the input from switch_location[0]
    print("get_one_nested_switch_start_and_finish()")
# and from  endswitch_location[0]

## this takes in the two lists of list_of_switch_range[1] and list_of_switch_range[2]
    print("=== ||=== get one nested switch start and finish line numbers")
    #force feeding it the second nested switch location input data 
    #these are hard coded for testing 
    #switch_location[0]    = 28  #july 18th testing 2nd nested switch
    #endswitch_location[0] = 38  #july 18th testing 2nd nested switch 
    list_of_switch_range[1] =switch_location[0] #force it in here
    list_of_switch_range[2] =endswitch_location[0]
    #list_of_switch_range[0]=0
    #list_of_switch_range[1]=10
    print(list_of_switch_range[1])
    print(list_of_switch_range[2])
    #list_of_switch_range[2]=20


the_nest_string= fridge[0] 



print("real string test from columbia river")

counter1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
			exp = 3
			switch(exp){ #49
				case 'burger':
					print("do something")
					####################
					switch(exp){ #53
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
			##############
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


#===========
counter2='''
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
'''
#===========
counter3='''
			switch(exp){ #49
				case 'burger':
					print("do something")
					####################
					switch(exp){ #53
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
'''

#===========
counter4='''
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
							#############
							break
						default:
							print("we are done here")
					endswitch #38
'''

#===========
counter5='''
					switch(exp){ #53
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
					endswitch #64
'''
#===========
counter6='''
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33
'''

testing_string_list=[]
testing_string_list.append(counter1)
testing_string_list.append(counter2)
testing_string_list.append(counter3)
testing_string_list.append(counter4)
testing_string_list.append(counter5)
testing_string_list.append(counter6)
#this is what has the string_with_nested_switches in it
# THIS TAKES TABS OUT OF THE ENTIRE NESTED SWITCH 

teststringgonow='''
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
'''
funky='''
	switch(exp){ #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
	endswitch 
'''

###=================================================================
passthis=[]
passthis.append(0)
##
#this gets the tabdepth in front of top switch word
##==================================================
##  starter_engine(the_nest_string):   nov 30th tested working accurately
##==================================================
def starter_engine(the_nest_string):
	print("======starter engine called======")
	tabdepth='';n=''
	for line in the_nest_string.splitlines(): #nest_string
		if "switch" in line and "end" not in line: #had "not"
			tabdepth = line.count("\t")
			n= tabdepth;n = n-1  #need to have one tab in front
			break
	passthis[0]= n;print("n =",n)
goldtime=[]
goldtime.append(0)
##===================================================================
##  modern_tab_shifter_to_left(the_nest_string):  nov 30th tested working
###==================================================================
def modern_tab_shifter_to_left(the_nest_string):
    print("====modern tab shifter to left=======")
    starter_engine(the_nest_string)  #method call to get tabdepth on first switch line
    buildstring='';n = passthis[0] #filled from starter_engine method number of tabs in front of switch
    ### n is number of tabs in front of switch BEFORE CHANGING IT
    if n == 0: #means one(1) tab in front of switch do nothing
        buildstring =the_nest_string #no changes to indentation
    if n > 1: #more than one tab in front of switch so cut some tabs out
        for line in the_nest_string.splitlines():
            buildstring += line[n:] +'\n' #this cuts out n tabs from the front of this line
    goldtime[0] = buildstring
    print("output of concatted string in goldtime[0]")
    for line in buildstring.splitlines():
        print(line)
  


#modern_tab_shifter_to_left(get_first_switch_da)
print("===== intermission 1=====")
#modern_tab_shifter_to_left(teststringgonow)
print("===== intermission 2=====")


print("testing indenting all 7 strings using modern tab shifter to left()")
for item in testing_string_list:
    modern_tab_shifter_to_left(item)
    print("==== line =====")
print("let them play in the snow")    
#exit()
print("================================")
print("================================")
print("============go baby work ====================")
print("================================")
catching_first_change=[]
print("testing going thru loop and calling one method to start ")
print("TEST MODE NOW...")
for item in testing_string_list:
    print(item)

#=================================== friday nov 19th =============================
# this is where I am applying a method to each item in input switch strings list
###===============================================================================
## THIS IS GOING THRU LIST AND CALLING METHOD modern_tab_shift_to_left(item) to each string
## and then putting modified switch string into list catching_first_change
counter=1  #FILLING CHATCHING_FIRST_CHANGE LIST FROM TESTING_STRING_LIST
for item in testing_string_list: #just filled this above
    #print(item)
    #method shift string to left
    modern_tab_shifter_to_left(item) #now put it into a new list
    #result put into goldtime[0])
    #add modified string to list catching_first_change
    #result of method effects on string goes into goldtime[0]
    #which is then appended to new list
    catching_first_change.append(goldtime[0])
    print("counter =",counter)
    print("=========================")
    
print("the exit sign is GREEN ....")  
print("the output change in list now..")
#print here we empty the original list and then refill it with inbetween list
del testing_string_list[:]   
print("this is filling the list testing_string_list from list catching_first_change")
for item in catching_first_change:
    print(item)
    testing_string_list.append(item)
print("================================")
print("=======strings modified in origional list testing_string_list ============")
##== here we see what's in the list

print("now blue orion looking thru original strings in list after being modified")
for item in testing_string_list:
    print(item)
 
  
#exit()










##########################################
##  take_out_x_tabs_from_front_of_line(n):
##########################################
def take_out_x_tabs_from_front_of_line(the_nest_string):
	starter_engine(the_nest_string);n=passthis[0]
	print("take out ",n," tabs from front of line - of string")
	print("take_out_x_tabs_from_front_of_line(n)") #make this is into a method 
	print("n=",n)
	#get tab count in line with switch and counter =1
	#should be governed by the first line with switch 
	
				
	wildness=''
	print('half way down n =',n)
	for line in the_nest_string.splitlines(): #nest_string
		
		newline = line[1:]
		print(newline)
		
		if n == 4:
			wildness += line.replace("\t\t\t\t","\t") 
		if n == 3:
			wildness += line.replace("\t\t\t","\t") #strips one right
		if n == 2: #this leaves 1 tab in front of each line
			wildness += line.replace("\t\t","\t") #strips one right
		if n == 1: # we only one one tab in front of the switch word as the guidepost
			pass #do nothingwildness += line.replace("\t\t","\t") #strips one right
		wildness += "\n"
	print("after minor surgery see if this works")
	print(wildness)
	fridge[0] = wildness
	return wildness # this worked

#3 take out 2
the_string='''
				switch(exp){ #  54
					case 'blable':
						print("do something")
						print("yep")
						fallthru
					case 'more':
						print("nice")
						switch(exp) # 98
						break
					default:
						print("we are done here")
				endswitch 
'''

#2 take out 1
the_second_string='''
		switch(exp){ #  54
			case 'blable':
				print("do something")
				print("yep")
				fallthru
			case 'more':
				print("nice")
				switch(exp) # 98
				break
			default:
				print("we are done here")
		endswitch 
'''


toocool=the_string.replace("\t","",1)
for line in toocool.splitlines():
    print(line)
trythis=toocool    
print("after first reduction")    
gonow=trythis.replace("\t","",1)
for line in gonow.splitlines():
    print(line)
    
print("did it twice")    
        
print("go away")
take_out_x_tabs_from_front_of_line(the_string)
print("road block here")
take_out_x_tabs_from_front_of_line(the_second_string)
print("hiking up Loma Road")
#exit()

#store in a dictionary each pair of switch and end switch params
# then I loop thru it with the numbers

####============ july 19th 2021  Monday ===================
# I already have the code to build a list of all switches and endswitches
# but I need to put them into a dictionary when I do that search to capture them as pairs

##================================

'''
swtich endswitch location
for trackcing hwer eto grab each nested switch
list with nestd swithc method name with number loop thru it
alist=[]
so = "10,20"
alist.append(so)
thisdict={
"brand":"Ford",
"2":alist[0],
"year":1964
}
#grab content by number
x = thisdict.get("2")
print(x)
# macro between
# put n thru m in a list
# then just this
# if x in list_of_numbers
'''

print("testing dictionary to hold switch endswitch pairs (pear tree)")
print(" ==== testing using a dictionary now ==== mayflower ship===")
alist=[]
alist.append(0)
alist.append(10)
alist.append(20)
alist.append(30)
alist.append(40)

color_table={
    "brand":"mocha",
    "Red": [10,20],
    "3": [30,40]
}

coffee = color_table["Red"][0]
print(coffee)
coffee = color_table["Red"][1]
print(coffee)
#grab content by number
#coffee = thisdict.get("2")
#print(coffee) #it should print 10,20
#print("now another one")
#coffee = thisdict.get("3")
#print(coffee) #it should print 10,20


friend1=[]
friend2=[]

thisdict =	{
  "1": [4,7],
  "2": [10,20],
  "3": [21,30]
}
for x in thisdict.values():
  print(x)
  cool = x
  print(cool[0])
  print(cool[1])
  friend1.append(cool[0])
  friend1.append(cool[1])
  print("good times")
  print(friend1)
  





### successful test for between macro ################### july 19th, 2021 ########## 

print("testing between macro and how it will work")
mylist=[]

mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

testlist =[]
testlist=[1,2,3,4,5,6,7,8,9,10]
#####################
##  between test()
#####################
def between_test(): #between macro 
#it would have to be like this
#if a between(x,y)
    print("BETWEEN TEST HERE ----")
    print("bla bla bla")
    print("between test")
    #x = 7
    print("the final outcome..")
    # if x >= switchline and x <= end switchline  #meaning  from start number thru endnumber
    #if x is between switchnumber and endswitch number
    #the list would contain the start number thru the stop mumber 
    # if x is between startnumber and endnumber:
    counter=0 #the logic is to be between x and y it's inclusive of x and y also
    for item in testlist: #so we look for a narrow range within the large input range
        if item in mylist:
            print("yes",item)
            counter += 1
            
        else:
            print("nope",item)
            counter += 1

print("=====do test of between macro proof of concept=====")
between_test() #this tests if we have a list of numbers 1 to 6

print("testing this with between")
zoo = 4
#if zoo between 1 and 6:
alist=[]
alist=[1,2,3,4,5,6]
print("======= BEtWEEN TESt ========")
print("testing the replacement for using betwen")
print("if zoo(4) is between 1 and 6")
if zoo  in alist:
    print("yes it's between 1 and 6",zoo)
else:
    print("nope",zoo)


###=========================
##   between() macro
##==========================
def between(x,y,z):
    print("between called for if x in list between y and z")
    if x in alist: #1 thru 6
        print("True yes ",x, "between ", y, " and ",z)
    else:
        print("False,",x," is not between ",y," and ",z)



print("doing between macro tests....")
between(4,1,6)
between(10,1,6)
between(0,10,25)


#also next add
##==================
##  after macro
##  before macro
##================

############## testing using  a dictinary to store
############## pears of switch and endswitch pairs

#this will be generated. but I think that
# I might have the dictionary pears already existing.

###====================== dictionary storage area =================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================

#dictionary called pears
peartree = {}  


#given name peartree of dictionary
def get_value_of_key_original(x): #peartree hardcoded in
    car=eval("peartree.get('" + str(x) +"')")
    print(car)
    return car #so if it is a list it should return a list right?z

#given name peartree of dictionary
def get_value_of_key(dict,x):
    car=eval("" + dict +".get('" + str(x) +"')") #maybe
    print(car)
    return car #so if it is a list it should return a list right?z


########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists
####################################################################||
### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  
#####################
## do this baby 

#what I need to do is add to a dictionary dynamically 
#####################
def do_this_baby():
    print("do this baby caled")
    print("===do this baby() adding data to peartree dictionary called ......====")
    print("practicing ADDING data to see if it works (this will be done dynamically later")
    peartree['1'] = [10,20]
    peartree['2'] = [28,38]  #uses small anonymous list for data
    print(peartree)
    x = peartree.get("1")
    print("x=",x)
    
    
def add_data_to_peartree(x,z):
    answer =''
    answer = "peartree['" + str(x) +"'] = z " #[10,20]
    print("just before exec add data to peartree")
    print(answer)
    exec(answer)
    
fool_on_hill= '[10,20]'
print("TESTING adding data to a dictionary")
add_data_to_peartree(1,fool_on_hill)
print("peartree has in its contents=")
print(peartree) 







#testing adding data record to dictionary dynamically.
#Declare a dictionary (empty) 
print("dynamiclaly add data to dictionary = DRIVE THRU ")
print("testing dynanmically adding data to a dictionary Drive Thru")
data = {'a': 1, 'b': 2, 'c': 3}
print(data)
data.update({'d':3,'e':4})  # Updates 'c' and adds 'd'
print("====after adding d and e dictioanry data======")
print(data)

fun={} #dictionary called fun
print("first the fun dictionary is empty")
print(fun)
#input values to dynamically add data for teh switch endswitch to dictionary

print("adding data to drivethru dictionary ")
print(" RED WHITE AND BLUE ")
drivethru={}
#drivethru.update('1': '[10,20]')
#drivethru.update('2': '[30,40]')
#3drivethru.update('3': '[50,60]')
#drivethru.update('4': '[70,80]')
#print(drivethru)

#zerohour=get_value_of_key(3)
#print("zerohour=",zerohour)

cherish=[10,20]
skyblue =[28,38]

def get_dictionary_size(x): #length
    shit= len(x)
    print("size of this dictionary",x," is",shit)
    print("so the result is ",shit)
    return shit;
    


print("This is doing an update here --->")
fun.update({'1':cherish,'2':skyblue})
print("hard coded here printing out the dictionary fun")
print(fun)
print("========")
num1='3'
num2='4'
silver =[42,46]
gold =[50,52]

#put these into a list also
crystal=[]
crystal.append(0)
crystal.append(num1)
crystal.append(num2)

dust=[]
dust.append(0)
dust.append(silver)
dust.append(gold)



#=
##==============================
def dynamically_add_data_to_dictionary(a,x,y):
    print("testing... dynmically add data to dictionary a, x, y")
    print("Tesitng using lists now which are changeable on the fly")
    a.update({crystal[1]:dust[1],crystal[2]:dust[2]}) #totally dynamic attempt here
    print(a)
print('did this work adding to dictionary')
##################################################################
print("here dynamic attempt --boo scoopy doo van does this work----->>")
dynamically_add_data_to_dictionary(fun,gold,silver)
print("3  =[42,46]")
print("4  =[50,52]")

print('after updating fun dictionary dynamically  strawberry fields===')
print(fun)
print(fun.get("1"))
rat=fun.get("1")
print("below should be 10 and 20 for the result")
print(rat[0])
print(rat[1])

print(fun.get("3"))
rat=fun.get("3")
print("below should be 42 and 46 for the result")
print(rat[0])
print(rat[1])

print(fun.get("4"))
rat=fun.get("4")
print("below should be 50 and 52 for the result")
print(rat[0])
print(rat[1])

print("==== end of adding to data to dictionary dynamically ===")
for k,v in fun.items():
    print(k, v)
    print(v[0],v[1])
    print("----------")

#modidfy this get value to use dictoinary name as parameter  
print("here we are testing get_value_of_key(dictname,keynumber)  (fun,3)")  
#note dictionary name as param MUST BE A STRING in quotes 
love=get_value_of_key('fun',3) #dictionary name and key number

print('the value of key  in fun =',love)
print("should return 42, 46")
print(love[0]) #42
print(love[1]) #46

print("testing getting the length of the fun dictionary")
golddust=''
golddust =get_dictionary_size(fun) #so I would call this before adding to it so
print("so now we can get the number for number of items in a dictionary")
print("we have ", golddust," as the length for dictionary fun")
#that I can add just the new data list [3,4] example and not think about key number
# basedon the length I just add 1 to it
print("above this line should be the size of the dictionary fun pumpkins")
######################################################################
print("now to empty dictionary called fun")
fun.clear() #empties dictionary
print(fun)
    
##===============================
## get_size_of_dictionary  (name of dictionary)
##===============================
def get_size_of_dictionary(zoo):  #this is so I know what next record should be
    print("get_size_of_dictionary")
    answer = len(zoo)
    print("get size of dictionary zoo",answer)
    #how do I loop thru a dictionary
    print(":this is printing out peartree ")
    for x in peartree:
        print(x)
    print("====")
    print("")
    print("this loops thru dictionary thisdict")
    for x in thisdict.values():
        print(x)
    print("")   
    print("===loop thru dictionary== this.dict ==")
    for x, y in thisdict.items():
        print(x, y)




car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def playing_with_dictionary_structs():
    print("playing with dictionary access...")
    x = car.get("model")
    print("testing getting car model")
    print(x)

playing_with_dictionary_structs()

   
#but I just thought I can have a running total in a list too
def do_something():
    print("Muppets Animal")
    result=''
    do_this_baby() # I think that the list peartree was empty when I was testing it
    print(peartree)
    print("get size of dictionary ... a test")
    #how do I determine if a list is empty
    if len(peartree) > 0:
        result= len(peartree)
        print("length of peartree =",result)
    else:
        print("peartree is empty and equal to 0")
        print(len(peartree))
    print(result)
    return result
######################################
do_something()

    


print("doing simple test here to get value of key number in peartree dictionary")
print("====Domino's Pizza= dominios pizza dominios pizza=")
firstone=get_value_of_key_original(1) #its using peartree
print('the value of key 1 in peartree =',firstone)
print("does this work or not???")
print(firstone[0])
print(firstone[1])

print("===== pizza hut ===has terrible pizza =")
secondone=get_value_of_key_original(2)
print('the value of key 1 in peartree =',secondone)
print("peartree[2][0] =",secondone[0])
#print(type(secondone[0]))
#print(str(secondone[0]))
#print(type(secondone[0]))
super = secondone[0]
#this force it into becoming a string actually 
#print(eval('secondone[0] == ' + str(super)))
print(super)
print("where is it")
print("type=",type(super))
if secondone[0] == 28: #int actually
    print("this tests :  if secondone[0] == 28:")
    print('too funny no chance in hell====it will never work ')
else:
    print("no way will it work")
    
print("peartree[2][1]=",secondone[1])
foolish = secondone[1]
foolish = str(foolish)
print(type(foolish))
print("now it's a string")
print("end of htis test")
 #peartree['1'] = [10,20]
 #peartree['2'] = [28,38] 
    

#example getting the size of dictionary peartree    
get_size_of_dictionary(peartree)




###############################################
## dnanmically add one record to dictionary
###############################################
def dynamically_add_one_record_to_dictionary():#will need some params
    print("starbucks morgan hill checking this out")
    print("dynamically add one record to dictionary ()") #what about input param
    #first pass go thru dictionary to determine it's current length put that into a list
    super=''
    super=get_size_of_dictionary(peartree)
    #so to add 1 to super for next record
    testtheory='[42,60]' #this is hardcoded here but testing at this stage so it's ok
    #super += 1
    #combine = firsthalf + secondhalf 
    #print(combine)
    #eval(combine)
    #print(combine) 
    #hard coded adding data to dictionary here obviously
    
    peartree['3'] = [42,60] #there would have to be 4 slots already to work
    print(peartree)
    get_size_of_dictionary(peartree)
    print("now yellow BIG BIRD test =========")
    ### look here this is correct below that owrks 
    fish =  "peartree['4'] = [66,80]"
    exec(fish)
    print("experimenting here adding new item to dictionary peartree for testing")
    ##======================================
    thenumber = 5; 
    y1 = 82; 
    y2 = 94
    salmon =  "peartree['" + str(thenumber) + "'] = [" + str(y1) +","+ str(y2) + "]" 
    #this would be blueberries 
    print("salmon=",salmon)
    #salmon= "peartree['5'] = [82,94]"
    #salmon= peartree['5'] = [82,94] #this one is correct
    exec(salmon)
    
    #and I can use 'peartree' as a var and connect it will try that next. 
    #what I built up above needs to look like this string 
    
    ###==========================
    #I need a database for each function that is searchable
    #with a tag of what it does - behavior
    #I could do it in javascript with my switch case
    ###=============================
    
    
    get_size_of_dictionary(peartree)
    print("is peartree 4 here with 66,80")
    print("looping thru dictionary peartree here on oct 23rd")
    for x, y in peartree.items():
        print(x, y)
    #output
    #output='''   
    #    1 [10, 20]
    #    2 [28, 38]
    #3 [42, 60]
    #4 [66, 80]
    #5 [82, 94]
    ##########################
    num = 5
    numb1 = 200
    numb2 = 280
    firsthalf  = "peartree['" + str(num) + "'] ="
    secondhalf = "[" + str(numb1) + "," + str(numb2) + "]"
    print('look here very carefully....')
    print('secondhalf=',secondhalf)
    together = firsthalf + secondhalf
    print("look at below this line does it look right GROUCH")
    print(together)
    exec(together)
    
    
    
    get_size_of_dictionary(peartree)
    #print(peartree['5'])
    print("get value of 5",peartree.get('5'))
    ###########################
    '''
    loop thru peartree:
        print(item)
    '''
    for item in peartree:
        print(item)
        
    for x in peartree.values():
        print(x)
        
    print("chocolate somores. ")
    sweet =get_value_of_key_original(1)
    print("sweet key 1 =",sweet)
    
    get_value_of_key_original(2)
    get_value_of_key_original(3)
    get_value_of_key_original(4)   
    get_value_of_key_original(5)
   

#this will be used to take in a set of two numbers switch endswitch
#to add to the pears dictionary
#### makes [24,34] from ab and returns it
#### make list with two pieces of data (ab)
def make_list_with_two_pieces_of_data(a,b):
    jedi=''
    jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail
    return jedi
    
#making peartree['1'] is not tough

#what about this
#dynamically build it [10,20]
x = 10
y = 20
jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail

print("")
print(" lightning round")
print("testing dynamically creating a two slot list to add to a dictionary")
x = 22
y = 33
raz=make_list_with_two_pieces_of_data(x,y)
#this does this
#  jedi = "[" + str(x) + "," + str(y) + "]," 
print("should return [22,33]")
print(raz)



print("celebration time it almost works completely fireworks")
print('jedi=',jedi) #creates [10,20],

print("interesting test to dynamically add a record to peartree dictionary")
print("KERMIT THE FROG test riding a bicycle")
run=get_size_of_dictionary(peartree)
print("size of dictionary before adding to it ",run)
dynamically_add_one_record_to_dictionary()
run=get_size_of_dictionary(peartree)
print("size of dictionary now is ",run)
#######################################################
do_this_baby()
print("did this work or not")
print("july 20th, 2021 wow time flies")
print(peartree)
###################################################################||

#######################
peartree = {}   #this will always exist and needs to exist to work.
buton=[]   #this is the passing of the buton in track and field relays
buton.append(0) #two positions here in this inner list
buton.append(0)
########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists

### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  


# test input
# this adds a datum to peartree
# this is the method to add a 
# new switch pair to dictionary peartree

#it was add_this <<=========
# now it's this
#####################################
## add_data_to_pears()
#####################################
### the dictionary name is hardcoded as peartree
# peartree is a dictionary
# buton is a list with two slots 

def add_data_to_pears(x,apple):
    print("add_data_to_pears()",x,apple)
    peartree[x]=apple  #this is where the list is added
    print(peartree)

#adding data to dictionary pears here 
 #july 21st 
 #simple var with data is a list anonymous which is what I will construct
apple = [10,20] #<<====== right here I need to produce this from the switch output
x = '1'    
add_data_to_pears(x,apple)  #feeding a new switch pair into peartree

##======
apple = [28,38]
x = '2'  #here I have to provide the number, now I can figure out what 
#it needs to be by getting the length of the dictionary and adding 1 to it.
#for th enext input of data to add to the dictionary. 
add_data_to_pears(x,apple)
##======

print('tahoe test')
print("testing getting a list out of the dictionary in terms of whats in it")
cd=get_value_of_key_original(2) #see if it returns [28,38]
print(cd)

################################################
###### TESTING FILLING A DICTIONARY ############
###############################################@

# I will nede a loop
# july 21st, 2021
#this looks into peartree for a key to return a value
# the values it put into buton[0]and buton[1]
 
# this is accessing the peartree
##############################
##  ACCESS_SWITCH_1_N
##############################
def access_switch_1_n(t):
  print("access_switch_1_n() called")
  print(peartree.get(t)) #was '1'
  one=peartree.get(t)
  print(one[0])
  print(one[1])
  #################
  # added July 21st
  buton[0]= one[0]
  buton[1]= one[1]
  print("this is looking into buton list")
  print("================//================")
  print("buton[0]=",buton[0])
  print("buton[1]=",buton[1])
  print("================//================")
  ##################
  print("I can now grab")
  print("the nest switch params")
  print("from the pear tree")
  print("to feed  copy nest method")
  print("first",one[0],"second",one[1])

#this is accessing the pears dictionary to get the data by the key
### this calls the method above   
t='1' 
access_switch_1_n(t) #accesses key 1


t='2' 
access_switch_1_n(t) #accesses key 2


###############################

# output 
'''
add_this called
{'1': [10, 20]}
add_this called
{'1': [10, 20], '2': [28, 38]}
access switch called
[10, 20]
10
20
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 10 second 20
access switch called
[28, 38]
28
38
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 28 second 38
'''
#<href="https://discover.cs.ucsb.edu/commonerrors/pythonerrors.html"> python common errors UC Santa Barabara</a>

########
b=''
##############################################
## ACCESSING DATA IN PEARTREE DICTIONARY #####
##############################################
def accessing_data_in_peartree_dictionary():
    print("====accessing data in peartree dictionary ==")
    print("====Accessing data  from peartree dictionary()....====")
    print("accessing keys in the peartree  which I would do with a loop later.")
    #print now accessing the dictionary that has been filled with data
    #x = peartree("1")
    print(peartree)
    x =peartree['1']  #adding data to a dictionary
    print(x)
    print(x[0],x[1])
    print("============")
    #x = peartree("2")
    x=peartree['2']  #adding data to a dictionary 
    print(x)
    print(x[0],x[1])
    print("how did it go Hogwarts after flying the car over London")
    
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    
    #this is where I access the dictionary
    # and call the code to get the nested swith
    # based on the switch and endswitch location params
    
    print("==== now trying a LOOP thru peartree =====")
    counter =1  #starting from 1
    for item in peartree: #looks in peartree in this example and splits pair set to display
        x = str(counter)
        b = peartree[x] #this was "1"
        print(b[0],b[1]) #these will always be the same 
        counter += 1
## output is correct
'''
==== now trying a LOOP thru peartree =====
10 20
28 38
'''
#this is for the numbering and access to the nested switches
# and governing them and number the nested_switches and managing it all perfectly.
#================ thursday, august 19th, 2021 solution =============================
#so with this approach number is simple 1 to n for each tab level
#only thing that I change is level depth of indentation
#so if we have main switch and then 3tab depth then 5tab depth
#level0, level1, level2
#level stands for nested switch depth
#so I can use the numbering 1 thru n for each switch
#and use the numbering system and just add the level[0] in a list
#level[0] is main 1, 2, 3, 4, 5 #nested numbering
#level[1] tab depth 5 is first level nested switch if nested within 1, 2, 3
#level[2] tab depth 7 is second level nested with , 1, 2, 3
#level[3] tab depth 9 is third level 
#def loop thru pears dictionary and call  nested switch
#==================================================================

#this calls the method above:        
accessing_data_in_peartree_dictionary()

### this would be after filling this with switch_location and endswitch_location method

print("practicing with this hardcoded input data for switch and endswitch to prove it works")
print("down at pears tree here hard coded ")
# this represents a dictionary called pears already loadded with data
#=================================================
########################
##  PEARS DICTIONARY
########################
#pears =	{  #for pear tree in backyard (2 of them)
#  "1": [10,20], # I can make these now 
#  "2": [28,38],
#  "3": [1,44]
#}

#testing with this new data multiple nested switches

#this hardcoded I put this in here. it's not automated yet
pears =	{  #for pear tree in backyard (2 of them)
  "1": [11,47], # I can make these now 
  "2": [49,73],
  "3": [15,38],
  "4": [53,64],
  "5": [23,33] #no comma after last data piece apparently

}

#for red_robin
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,100], # I can make these now  1 tab level start and stop
  "2": [11,60], #3 tabs
  "3": [15,51], #5 tabs
  "4": [23,46], #7 tabs # yes it is a stacked at 3 tab level already 
  "5": [31,41], #9 tabs
  "6": [62,86], #3 tabs
  "7": [66,77]  #5 tabs
 #no comma after last data piece apparently
}


#nest_string has pears
#and then blueberries added. 
#solved it.
 
#da = blueberries.get("2")
#print("getting data in blueberries")
#print(da)

'''
11 is in 1
62 is in 1
15 is in 11
23 is in 15
31 is in 23
66 is in 62
'''


def lametest():
    print("doing lametest()")
    if 11 in range(1,86):
        print("true")
    else:
        print("false")
    
lametest()

#new pears

#creates this

#this string already has numbered switches with comments 
#note that the numbering of the switches isn't starting from 1 down.
#testing this sep 30  #switch11 is the main switch
foolish='''
			switch(exp){  #11  first level deep                   Level 1... 3tabs
				case 'blable':
					print("do something") #formula is switch number + 1 thru second number
					#################### cut out 16 thru 38
					switch(exp){ # 15  #second level deep          Level 2    5 tabs=================
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23  #third level deep   Level 3   7 tabs  
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch #33 === 7 tabs 
							#############
							break
						default:
							print("we are done here")
					endswitch #38   # 5 tabs========================
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
			exp = 3  #note that this switch is stacked below the bottom stack at 3 tabs
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  # 53second level deep          Level 2    
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
					endswitch #64
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #73
'''
#end result will be .......
##=======================
''' main string is 11 thru 73
        pair   tab count
  "1": [11,47],[3] # I can make these now #but it has two starting points SECTIONS
  "2": [49,73],[3]
  
  "3": [15,38],[5] 
  "4": [53,64],[5]
  
  "5": [23,33] [7]
#main 1  to 3 tab depth level 1 ONE
only switches at 3 tabs 
#it should be 
###########
mainswitch number followed by it's nested switches which will be methods
====switch numbers two columns===
first position [0] is first switch id line number for that string
second list can have more than one number represents the switchnest numbers
now figure out how I calculate this and fill it as a listwith sublists
[1] [11,49]
[11][15]
[49][53]
[15][23]
[23][0]
'''
# what this does is add ..  # 66  the line number after each switch(exp){

print("TWIN LIST let's take a look and see what's in it")
#print("let's look inside of twinlist",twinlist)
#they have to be in the same order as the actual switch cases

'''
##================
======1:3==========                   switch1 > switch11 and switch49  =========
switch1
     switch11 method 3 tabs first number from pair 11,47
     switch49 method 3 tabs first number from pair 49.73
end73
#==============================       switch11 > switch15  =======
only switch at 5 tabs between 11 and 47
#minor 3 tab to 5 tabs  Copy 11 thru 47 TWO
switch 11  3 tabs
     switch 15#method  5 tabs   must be between 11 and 47
switchend47
#=============================         switch49 > switch53    ======
#minor 3 tab to 5 tab   THREE
only switch at 5 tabs between 49 and 73
switch 49
     switch 53 method must be between 
endswitch73
##====================  FOUR           switch15  > 23 =======
#minor  5 to 7 tabs   
only swith at 7 tabs between 15 and 38
switch 15
     switch 23 method
##====================  FIVE           switch23  none ======== by itself
#minor none 7 tabs not nested because no 9 tabs its an end tail
switch 23      
$$$$$$$===================================================$$$$$$$$
# I need to be able to generate the pattern
if tab depth == 3 then
first number of pair[0] is nested switch 11 and 49
     switch11 method  first number from pair 11,47
     switch49 method 
     
=======3:5
if tab depth == 5 then
first number of pair[0] 15 goes inside minor 
three tabs to five tabs
switch 11
     switch 15#method   must be between 11 and 47
switchend47
===== 3:5
[49,73],[3]=== [53,64],[5] if secondpair[0] > firstpair[0] and 
switch 49
     switch 53 method must be between 
endswitch73
#testing this
combinedtabs=[]
combined_tabs = threetabs + fivetabs + seventabs
#threetabs= [11, 47, 49, 73] done 
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]
'''
print("testing merry christmas code")
print("obviously this is a thinking and engineering problem")
threetabs = [[1, 2],[3, 4]] 
fivetabs  = [[5, 6],[7, 8]]
seventabs = [[9, 10]]
#testing this
fuel=[threetabs,fivetabs,seventabs]
combinedtabs_jazz=[]
combine=''
fulllist=["threetabs","fivetabs","seventabs","ninetabs","eleventabs","thirteentabs","fifteentabs"]

#def grab_these_tabs(x):
    


upto7 = "threetabs + fivetabs + seventabs"
combined_tabs_jazz = eval(upto7)
print("combined_tabs_jazz=",combined_tabs_jazz)
for item in combined_tabs_jazz:
    print(item)
    

#laketahoe
combined_tabs=[]
##========================================================
threetabs= [[11, 47],[49, 73]] 
fivetabs = [[15, 38],[53, 64]]
seventabs= [[23, 33]]
#this combines the theetabs, fivetabs and seventabs
combined_tabs = threetabs + fivetabs + seventabs

counter=1 #looping thru combined_tabs list
for item in combined_tabs:
    alpha = item[0];beta  = item[1]
    print("pair=",item," "," counter=",counter,", first=",alpha,", second= ",beta)
    print("=========================")
    counter += 1
print("did she work")

for item in combined_tabs:
    print(item)
    
#output
'''
pair= [11, 47]    counter= 1 , first= 11 , second=  47
=========================
pair= [49, 73]    counter= 2 , first= 49 , second=  73
=========================
pair= [15, 38]    counter= 3 , first= 15 , second=  38
=========================
pair= [53, 64]    counter= 4 , first= 53 , second=  64
=========================
pair= [23, 33]    counter= 5 , first= 23 , second=  33
=========================
did she work
'''
    
#this is what is in combined_tabs now
print("showing off combined tabs list")
for item in combined_tabs:
    print(item)
print("===================")    
#see if this works
#=================================================


table=[]
table.append(0)
#============================================================
## check_if_nested_switch_inside_this_switch(astring): 
## returns table[0] = False or True
# coded on dec 6th monday 12:== noon ish

#==========================================================
def check_if_nested_switch_inside_this_switch(astring):
    print("check if nested switch inside this switch")
    counter=0
    table[0] = False
    for line in astring.splitlines():
        tabcount=line.count("\t")
        if tabcount == 3  and "switch" in line and "end" not in line:
            table[0] = True
            print(line) #proof is in the pudding - how good is it
            break
            
            
            
            
            
##### this does absolutely nothing 
# I need to make a method to add main switch to string list
def add_main_switch_params_to_dictionary():
    print("how it will work")
    #methods count end switches
    #Take answer add 1
    #loop thru input switch string get total number of lines
    #"3" : [1,44],  #is the result
    #call method to add it to dictionary


#pears['3'] = [4,7] #example
# 38-15+ 1=24  formula end number - first number = x then x + 1
#first number keep, skip out to 23 lines (length of string of nested switch)

print("====dictionary pears====")
print(pears)
print("==========")
print("====dictionary peartree====")
print(peartree)

print("==== practicing with dictionary called pears ========")
#access the dictionary one key in particular to get the value
#print('pears[3] which is the key number')
#x = pears["3"]
#print("x = ",x) #this should be 4,7
#print("============")
 
 
def say_something(x):
    print("say something test here")
    print('cool[0]=',x[0], "cool[1]=",x[1])
     


print("PRACTICING LOOP THRU THE PEAR DICTIONARY WITH HARD CODED DATA FOR TESTING")
print("============")
print("== PEARS  dictionary now LOOPING THRU IT===")
print("listening to teh Beach Boys to see if it works ----")
#looping thru dictionary called thisdict
'''
for x in pears.values(): #looping thru pears dictionary holding switch and end switch pairs locations
    
    print(x)
    cool = x
    #print(cool[0])
    #print(cool[1])
    print(cool[0],cool[1])
    #say_something(cool)
    copy_one_nested_switch_string(m82)
    print("========================")
       
''' 
#this will be a method but of course
'''
for line in inputstring.splitlines(): #	
		#this will be the second loop======
		# if counter is between start and finish #just after start and less than = to finish
		if counter > start and counter <= finish: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
	print("===output from skipping some lines====")
	print('it created this string')
	print(concatthis)
'''	
	


#######=========================================
#
##==============================================
def do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring):
	print("do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up")
	#this 
	genius[0] = inputstring
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		skipping_some_lines(genius[0],start,finish)
	#it goes thru the string and makes list of switch,endswitches
	
	
	


#testing
spilled_coffee ='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 ==========
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #14
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 ===============
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #26 ==============
			
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====
'''	



skitahoe ='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #14
			print("nicely")
		case 'more1':
			switch(exp) 16
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #23
			print('party time')
			switch(exp) #25
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #32
		case 'more2':
			print('more parties')
			switch(exp) #34
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #41
			print('are we there yet')
			switch(exp) #43
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #50
			print('how many this week')
			switch(exp) #52
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
				print('bye')
			endswitch #59
			print('what the..')
			break
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====
'''	



flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
switch_list=[]
endswitch_list=[]
thenewpairs=[]

##============================
##  buildpairlist()  created nov 21st, sunday to manage doing the main switch 
##============================  and cutting out switches at three tabs for main switch 
def build_pair_list(stringname):
	print("====== build_pair_list called ======")
	counter =0
	#flush lists
	switch_list=[]
	endswitch_list=[] #should reset them both 
	#thenewpairs=[]
	#del endswitch_list[:]
	#this fills up the switch_list line
	#===================================
	# LOOP FILLS UP SWITCH_LIST 
	#===================================
	#loop thru stringname and fill up switch list
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "switch" in line and "end" not in line:
			switch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	counter =0
	#loop thru stringname and fill up endswitch list
	#this fills up the switch_list line
	# =======================================
	# LOOP FILLS ENDSWITCH LIST 
	#========================================
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "endswitch" in line :
			endswitch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	del switch_list[0]     #delete first switch number which is on line 1
	del endswitch_list[-1] #delete last number endswitch which is end of entire string
	print("after deleting first and last switch we have..")
	print("switch_list=",switch_list);print("endswitch_list=",endswitch_list)
	counter=0 #build the pairs and put them into sweet; then append sweet to thenewpairs list
	#===================================================================================
	# LOOP FILLS THENEWPAIRS LIST WITH SWEET WHICH HAS SWITCH,ENDSWITCH LINE NUMBERS
	#===================================================================================
	for item in switch_list:
		sweet=[switch_list[counter],endswitch_list[counter]]
		thenewpairs.append(sweet)
		counter += 1
	print("this is what we want to see at starbucks")
	print("thenewpairs=",thenewpairs)
	#==================================
	# LOOP PRINTS OUT THE NEWPAIRS LIST
	#==================================
	for item in thenewpairs:
		print(item)
		print('stop here for now')
		#exit()
	#REVERSE THE NEWPAIRS LIST BECAUSE IT HAS TO BE DONE BOTTOM UP TO THE STRING 
	thenewpairs.reverse() #they have to be skipped bottom up to work properly
	print("thenewpairs=",thenewpairs)	
	print("resulting list of thenewpairs =",thenewpairs)



pinkpanther=''
##===========================================
##  skipping_some_lines() #this works
##===========================================
def skipping_some_lines(thestring,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	return
	print("METHOD  skipping_some_lines() called==========")
	print("======= skipping_some_lines() ================called",start,finish)
	# if I have a flag that it's been triggered then afterewards 
	# print("this is the input string used stating skipping_some_lines")
	# for the first pass flag_test[0]= False and then it's flipped to True
	#print("flag_test[0]=",flag_test[0]) =============================
	#if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
	smart=thestring;
	baton[0]=thestring #this is new
		#change it to True now
	flag_test[0] = True #this should now be tru e========================
	#else: #meaning TRUE this is run after first run of skipping_some_lines()======
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
	thestring = baton[0]#====================
	#print('what is in baton[0]',baton[0])
	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
	# because the numbering system of the string starts from 1 too.
	### look that we have the counter here set to 1 by default 
	counter=1; concatthis =''; #finish = finish + 1 
	print("start=",start,"finish=",finish) #I took out x = 
	#smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	#print(smart)
	print("=== ah now I get it these are the lines that it MUST SKIP and we want what is before and after this range to create the modified string =")
	print("it sees in start",start)   #this is a number
	print("it sees in finish",finish) #this is a number too
	##=================
	#so I would build pair list of inner switches at 3 tabs and then loop thru them to skip them
	#this is new on sunday november 21st 2021
	#what I want to skip on the fly without range data
	
	#------------------------------------------------
	#from switch at 3 tabs until endswitch at 3 tabs
	#skip the lines inbetween leaving switch word
	##----------------------------------------------
	
	
	##=============== this is a new addition to automate the grabbing of inner switches ====
	# this creates pairs of the switch, endswitch pairs 
	#if start == 1 and finish == 1: #meaning figure out pairs on the fly
	
		
	#exit()
	counter=0
	#for item in thenewpairs:
	#	start  = item[0]; print("start=",start)
	#	finish = item[1]; print("finish=",finish)
	#check thype
	print("checking tyhpe of thestring")
	print(type(thestring))
	print(thestring)  #it shows 0
	print("what is it?")
	print("starting baton[0] has teh initital input string in it")
	for line in thestring.splitlines(): #smart = x
			#this preserves the switch word and skips the rest of nested switch body including endswitch
			# if counter is between start and finish #just after start and less than = to finish
			#just added start +1 and finish + 1
			#tabdepth= line.count("\t")
			#if tabdepth == 3 and "switch" in line and "end" not in line:
			#		start = counter
			# use while loop of course
			#so it's upside down and backwards to create the same meaning.
			# probably need to do a prescan but maybe i can do it without doing prescan
			#get location of switch and endswitch at 3 tabs
			#while "endswitch" not in line:
			#####################==================
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
		##=======================================
	baton[0]=concatthis;
	print("===output from skipping some lines====")
	#print('it created this string')
	#print(concatthis)
	print("how does it look===>>> by lettuce field")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	#this has red_robin hardwired into the code 
	#just commented out line below november 10th, 2021 to see wehat happens 
	#toosmart[0]= red_robin #it did say toosmart[0] = red_robin
	#just commented these out thanksgiving
	#baton[0] = concatthis  #here the concatthis has been put into baton[0]=======
	#pinkpanther=concatthis==============
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= baton[0]  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	print("now the result is here....!!!!@@@@@$$$$$")
	print(never_defeated[0])
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
	#exit()	
	#print(ibm[0])
		#just moved this over one tab	
#exit()
#end skipping_some_lines  ========================================================
print("Levels TEST on wonderful Monday winter wonderland ")
print("this will take out the inner switch between") 
never_defeated=[]
never_defeated.append(0)

#for line in skitahoe.splitlines():
#   print(line)




#it was previously this
def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    return
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    skipping_some_lines(stringname,start,finish)
    #this means that the output string should be placed into never_defeated[0]
    for line in never_defeated[0].splitlines(): #prints it after takening out. 
        print(line)
        

##===========================================================================
##  modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
#this was redesigned and modified on sunday november 21st at 8:30am to 
# work with skipping some lines with no known locations of inner switches at 3 tabs
# and it calls method build_pair_list to find them and reverse them for input for skipping_some_lines
# and I have to subtract 1 from start and finsh
#this one is used to get the main switch and take out switches at 3 tab depth

# and loops thru list feeding start and finish  params and calling skipping_some_lines()
# #  the input for start and finish will be 1 by default but they will be overwritten
# #  by the build pair list on-the-fly.
print('this one is sooo critical')
def modified2_cut_out_inner_switch_body_leaving_switch_word(stringname):
    #it is modified so it can change more than one inner switch into a switch, infinite
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    ###======= this is ingenius=========
    #METHOD BUILD_PAIR_LIST(STRINGNAME) 
    if len(thenewpairs) > 0:
        print("==TRUE thenewpairs >0 it is ===== ",len(thenewpairs))
        del thenewpairs[:] #delete contents of thenewpairs list if it's not empty yet
    #end if
    #if len(never_defeated[0]) > 0:
    never_defeated[0]='' #deletes it
    build_pair_list(stringname)           # goes thru thenewpairs list and
    for item in thenewpairs:              # fills start and finish into skipping_some_lines params
        start  = item[0];
        finish = item[1]; # print("start,finish=",start," ",finish)
        skipping_some_lines(stringname,start-1,finish-1)#so close now 
        #the result of the concatting goes into never_defeated[0]
    #this means that the output string should be placed into never_defeated[0]
    print("let us see what we have jazz blues line 6166 ....")
    #so it's output is in  never_defeated[0]
    thisstring = never_defeated[0]
    return thisstring; #see if this works  it is important that we return the string
    print("let's see what it has in it and if it converts the inner switch bodies to switch word...")
    for line in thisstring.splitlines(): #prints it after takening out. 
        print(line)
    cat_scales[0]= never_defeated[0]
    print("now loop thru pinkpanther")
  
        
#manipulate_string(item) #shifts it to the left

# this is the one that is new as of november 21st and it does the main switch with
# inner switches at 3 tabs that it takes out leaving just the switch word.
#============ original============ modified2
output_list=[]
output_list.append(0)
# testing spilled_coffee string 
stringname=spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print("input string is spilled_coffee  =========")
print("doing first attempt of converting inner switch bodies to just the switch word")
mybaby =''
mybaby = modified2_cut_out_inner_switch_body_leaving_switch_word(stringname)
print("did this sucker work tuesday november 23?")
print("now loop thru the output if it generated it")
print("this is the resulting output processed by the modified2_cut_out... function")
for line in mybaby.splitlines():
    print(line)
    #print("======") 
print("end of first string test for reducing switch bodies to switch word") 
print("=== made it to this point after first attempt completed ===")  
print("now a SECOND ATTEMPT AT CALLING THIS METHOD NOW. WEIRD AT LEAST FIRST PASS WORKS ==")
## testing skitahoe string
#stringname=skitahoe;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print("just testing 2nd one with skitahoe string to see if it works ==input sstring is spilled_coffee")
mybaby =''
#worked by itself
print("doing skithaoe string now=============")
stringname=skitahoe
mybaby = modified2_cut_out_inner_switch_body_leaving_switch_word(stringname)

for line in mybaby.splitlines():
    print(line)
#exit()   
    
print("===end of show on thanksgiving==attempt 2 =")    
#exit()


#exit()

print("catscales=",cat_scales[0])
print("=====rats======")
print("never_defeated[0]",never_defeated[0])

goldring = never_defeated[0]
print("is this going to finally work or not")
output_list.append(goldring)
print("WHAT IS BELOW THIS DAM LINE")
print(output_list[0])
print("now loop thru goldring s")
for line in goldring.splitlines():
    print(line)

print("seeing if this works")
for line in never_defeated[0].splitlines():
    print(line)
    
#ram = never_defeated[0].replace("switch","rocks")
#never_defeated[0]= ram
#for line in never_defeated[0].splitlines():
#    print(line)
#exit()
#==================================
print("end of deifnitely working modifies2 cut out inner switch body.()")


#stringname=skitahoe; start=7; finish = 14; #this sucker was moving....    
#cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
print("let us see what we have.")

#need to indent it I think.
#produces this output it is NOT indented yet 
goldfish='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7
			print("nicely")
			break
		default:
			print("we are done here")
	endswitch 
'''
			
			
			

print(" RED RED RED cut out switch body leave only switch word baby")
print(" red alert testing cut out switch body leaving switch word tesitng 4 ..")    
#exit()

#this is testing with dummy data above in test_code_now
#taking out the inner switch body
print("halloween is coming snoopy and woodstock test")

#print(test_code_now)
#the inner switch is at 9 (which we keep) so we start from +1 meaning 10
#and the endswitch is at 19 but we need to nuke that too so it's endswitch + 1
print("take out 10 thru 20") #but actually keep 10 and takeout including20
#x = test_code_now
#the number system starts from 1 for the switch numbering
#because it starts counting from 0 and not 1 we need to subtract 1 from it
#so it was originally 10, 19

#if switch is #9 and endswitch is 19
#Add 1 to each number start and finish
print("rose test")








#modified so it doesn't matter where the inner switch is 
# they will all be at 3 tabs
#the first switch must be at 1 tab and inner switches need to be at 3 tabs one depth in
#THIS IS NEW CODE WEDNESDAY CODING...november 10th ........
##########################################################################################
#####################################################################################
 #creates first slot in list for string
	#print("actually this builds lists of switch and endswitch locations and makes pairs")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print(" checking to see if more than ONE inner switch at three tabs and ")
	#print("if so then put them into a list")
	#print("the first loop determines how many inner switches at 3 tabs")
	#print("the second loop will go thru a list of the pairs - ah yes but ")
	#print("not implimented yet ")
	
	#print("it sees in finish",finish) #this is a number too
	

# "actually this builds lists of switch and endswitch locations and makes pairs")
# what it does: creates pairs set of start, finish after getting list of switch and endswitch lines
# then it will loop thru pairs set in reverse order and cut out switch bodies bottom up 


## new november 10th 2021 !!:37am
#JUST TRY IT


#this requires this function below to be called first though
#  smart_cut_out_inner_switch_bodies_at_three_tabs(samplestring)
pairset=[]
genius=[]
genius.append(0)

never_defeated=[]
never_defeated.append(0)
list_of_inner_switches_at_three_tabs=[]
list_of_inner_endswitches_at_three_tabs=[]




##========================================================
## loop_thru_pair_set_and_call_skiplines(samplestring)
##=========================================================
def loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring):
	print("len(never_defeated) =",len(never_defeated))
	#never_defeated[0] = thestring #this takes the initial string put into never_defeated[0]
	never_defeated.append(thestring) #maybe this is what I need to do to fix this bug
	print(never_defeated[0]) 
	counter =0
	#loop thru pairset of sets of switch,endswitch (already reversed to go bottom up)
	for item in pairset: #the pairset list was filled in smart_cut_out_inner_switch_bodies_at_three_tabs
		alpha = item[0];beta  = item[1];print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		#METHOD skipping_some_lines()============= uses never_defeated[0] stirng in list
		skipping_some_lines(thestring,start-1,finish-1) #added -1 on Mon Nov 22nd 2021 9:00 AM
		#doing this to see if it cut out the inner switch body 
		print("this is showing the changes reducing switches in never_defeated[0]")
		mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
		print("this is what the switch string looks like after taking out a switch body")
		counter += 1
	








##====================================================================
##  make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring)
##====================================================================
def make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):
	print("METHOD make_Pair_set_of #### called  ... make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):")
	counter =0
	print('let us look at this string to see what it sees')
	print("========//////////==========///////==============")
	for line in inputstring.splitlines():
		print(line)
	print("========//////////==========///////==============")
	for line in inputstring.splitlines(): #smart = x
		#this preserves the switch word and skips the rest of nested switch body including endswitch
		#for this line get tab_depth
		#print("this is where I add the switch line number to list of inner switches at three tabs")
		tab_depth= line.count("\t") #but this presumes just one inner switch there could be more
		#if 3 tabs True AND switch in line and end not in line and counter > 1 
		if tab_depth == 3 and "switch" in line and "end" not in line and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_switches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)		
	#second new loop but looks for endswitch locations at 3 tabs 
	counter =0
	for line in inputstring.splitlines(): #smart = x
		print(line)		
		tab_depth= line.count("\t")
		#print("this is where I add the endswitch line number to list of inner switches at three tabs")
		if tab_depth == 3 and "endswitch" in line  and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_endswitches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("==================")
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)	
	print("list_of_inner_endswitches_at_three_tabs=",list_of_inner_endswitches_at_three_tabs)		
	print("===================")
	print("===== end of phase 1 =====")
	##======================================================================================
	print('doing Friday debugging oh what fun it is to ride in a one horse open sleigh')
	if len(list_of_inner_switches_at_three_tabs) == 1:
		print("this means only ONE dam pair")
	else:
		print("the length is =",len(list_of_inner_switches_at_three_tabs))
		cat = len(list_of_inner_switches_at_three_tabs)
		print("the length of inner switches at three tabs is ",cat)
	###=================================================================	
	print("now I need to make pairs")
	get_number = len(list_of_inner_endswitches_at_three_tabs)
	
	if get_number == 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	##3=======================================================================		
	if get_number > 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	else:
		pass #print("there is only one switch endswitch so do regular mode just one inner switch at 3 tabs ")
	if get_number > 1:
		pairset.reverse()  # REVERSE PAIRSET SO THAT I CAN CHANGE THE INNER SWITCHES BOTTOM UP
	
	print(pairset)
	print("loop thru pairset") #to go thru input string and reduce inner switches to just switch word bottom up
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
	##======================================
	print("method to go thru pairset and call skipping_some_lines(start,finish)")
	do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring)
	#########====================================
		#skipping_some_lines(genius[0],start,finish)
	#it goes thru the string and makes list of switch,endswitches
	
	#skipper needs to cut out from bottom up 
	#skipping_some_lines(x,start,finish):
	#it will call a method

#this must be called after one switch string has had it's inner switches reduced to switch word
#def reset_to_initial_conditions(): #brainchild on NOv 11th, Thursday morning#
#	print(" ====reset_to_initial_conditions()======"#)
#	never_defeated[0] =""
#	list_of_inner_switches_at_three_tabs=[]
#	list_of_inner_endswitches_at_three_tabs=[]
#	pairset=[]
#	baton[0]= "" #should clear it out
    

#def show_output_string_after_changes():
#    mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
#		print("this is what the switch string looks like after taking out a switch body")
#		print('resulting string change is for counter',counter)
#		for line in mouse.splitlines():
#			print(line)    
#this makes pairset list of switch and endswitch 
#this is only run ONCE
fullhouse=[]
##============================================================================
##  take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word
##----------------------------------------------------------------------------
##  Methods: make_pair_set_of_inner_switches_at_three_tabs_depth(thestring) oh wow genius here
##  Methods: loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
##  Methods: skipping_some_lines(x,start,finish)
##  Methods: determine_if_inner_switch_inside_of_this_switch_string(weasel)
##  result of modified string put into  fullhouse.append(never_defeated[0])
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	return
	print("THIS NEEDS TO WORK NOW==")
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("called ....take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)") 
	make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
	print("this is scenario where if one inner switch it's not filling the pairset")
	print("pairset=",pairset)
	loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
	print("list_of_inner_switches_at_three_tabs=", list_of_inner_switches_at_three_tabs)
	print("list_of_inner_endswitches_at_three_tabs=", list_of_inner_endswitches_at_three_tabs)
	print("pairset=",pairset)
	print("this should be the result of the switch with inner switches cut to just switch word, bodies gone")
	for line in never_defeated[0].splitlines():
	    print(line)
	##################################################
	## adding resultof output of methods of taking out inner switches into never_defeated[0]
	## which is put into list fullhouse using append
	### this is where the result of the change string put into never_defeated[0]
	### is appended to list fullhouse
	fullhouse.append(never_defeated[0]) #needs to be here obviously
	#-------------------------------------
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""
	



print("====STARTING ATTEMPT 1====== charlie brown music is the best jazz ====")


take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(spilled_coffee)


#exit() 
print("this is after the first string and taking out inner switch bodies...")
#print("====STARTING ATTEMPT 2====== charlie brown music is the best jazz ====")
#reset_to_initial_conditions()
	##==========================

##=======================
#take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestringzoo1)


#reset_to_initial_conditions() #this must be done after each transformation
print("the final OUTPUT is here ...")
print("length of fullhouse should be 2 is now",len(fullhouse))


#for item in fullhouse:
#    print(item)

####################################################
#print("size of FULLHOUSE is..",len(fullhouse))
#for item in fullhouse:
#    print(item)

print("time to go sledding")
#exit()


print("now I will try to do a few stings with it.") 
print("end of this initial test of ")
result_of_check_if_inner_switch=[]
result_of_check_if_inner_switch.append(0)

#coded on november 19th friday at 10:48 am morgan hill starbucks
##====================================================================
## determine_if_inner_switch_inside_of_this_switch_string(weasel):
##====================================================================
def determine_if_inner_switch_inside_of_this_switch_string(weasel):
    print("determine_if_inner_switch_inside_of_this_switch_string(weasel):")
    ## START INNER LOOP ======= devised on nov 19th friday 10L30 am ===========
    innerswitch= False #this must be set to False before each call below 
    result_of_check_if_inner_switch[0] = False
    for line in weasel.splitlines(): #this looks for an inner switch at 3 tabs depth
        tabdepth = line.count("\t")
        if tabdepth == 3 and "switch" in line:
            print("where's the party THIS string has an inner switch ")
            innerswitch = True
            result_of_check_if_inner_switch[0] = True
            break
        else:
            continue
        print("....")
    print('this has to be called after the loop is done')
    print("result_of_check_if_inner_switch[0]=",result_of_check_if_inner_switch[0])
    #end loop ===================


funtestlist=[]

print("big bird for prez")
print("testing in my mind wed november 10th test ..going thru list and calling take out switch bodies.")
funtestlist=[samplestring,samplestringzoo1] #samplestringzoo1
#use the list I made earlier catching_first_change

# what this does is loop thru the seperated switch strings and 
# applies a method take out nested switch bodies leaving switch word


#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
# method determine_if_inner_switch_inside_of_this_switch_string(stringname)
# method take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
#=====================
def try_the_mocha(): #this has the separated strings in it (that's helpful)
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    print("let us see the SEPARATED strings in this list")
    for item in catching_first_change:
        print(item)
    print("===== okay is this it ===")
    
    print("length of catching first change should be 6",len(catching_first_change))
    counter=0  #this is running the method for second stage of chain_methods
    for item in catching_first_change: #funtestlist: #strings in funtest list
        weasel = item
        ## determines if there is an inner switch in THIS string ==========
        determine_if_inner_switch_inside_of_this_switch_string(weasel)
        innerswitch= result_of_check_if_inner_switch[0]
        print('innerswitch if true or false it is .. =',innerswitch)
        if innerswitch == True:  #if there is an inner switch then apply the method below  
            ######## this method  cuts out all inner switch bodies ######################
            take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
            #fullhouse.append(never_defeated[0]) this line is at bottom of method take_out_nested..
            #never_defeated[0] #this string is the result of the method above in never_defeated[0]
            #############################################################################
        else:
            fullhouse.append(weasel) #so the original string unchanged is added to fullhouse llist
            #this means no innerswitch in this switch string 
            #it's False no inner switch
        counter += 1
        
        ###=========================================================
    print(" end of double loop ")
    print("after going thru catching first change list it should be 6 for counter")
    print("counter =",counter)
    print("len(fullhouse)=",len(fullhouse))
    print("let us look in here if switch stirngs with no inner switches okay and exist at least")
    for item in fullhouse:
        print(item)
    del catching_first_change[:]
    #this fills the output list into catching_first_change list 
    for item in fullhouse:
        catching_first_change.append(item)
        
    print("now big test of second chain method #taking out switch bodies")
    print("this should print out 6 stritngs")
    counter=1
    for item in catching_first_change:
        print("counter=",counter)
        print(item)
        print('=========')
        counter += 1
        
    

print("this is for all of the marbles out of style")
try_the_mocha()    
print('did it work razzle dazzle pumpkins')



#exit()





#modified to get nested switch #so after the first switch in the string 
#so it gets the switch that is nested.
###============================
## get second switch number
##=============================
def get_second_switch_number(stringname): #this might be for when
# I create copies of the switch body strings
	print(" ..get_switch_number.. ")
	awesome=''
	counter =0  #say it's 3
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		if "switch" in line and "end" not in line and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number is",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;
	
	
#input1 = rose[0]
#input2 = rose[1]
#print(input1)
#print(input2)
bigstringtest='''
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
    										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch #tail
							
									break
								default:
									print("we are done here")
							endswitch #46  2
'''

print('output should be it shoud return this string')
'''
							switch(exp){ #23
      								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2
							'''
							
print('october 12th testing doing actually test taking out inner switch')

bigstringtest1='''
	switch(exp){ #1
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #9
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'where now':
					print("nice")
					break
				default:
					print("we very done")
			endswitch #tail
							
			break
		case 'tahoe bound':
				print('fun time now')
				exp ='fishy'
				switch(exp){ #25
					case 'fishy':
						print("do something")
						print("yep")
						fallthru
					case 'where now':
						print("nice")
						break
					default:
					print("we very done")
				endswitch #tail
				print('end of the game time')	
		default:
			print("we are done here")
	endswitch #46  2
'''

start = 10 #rose[0]+1
finish=20 #rose[1]+1
total = finish -start; #gives us 10
x= bigstringtest  #string name to cut out the range from 10 to 20 
skipping_some_lines(x,start,finish)
print(toosmart[0])
print('leaving this November 10th test now for skipping lines in string')
#exit()







peachtree=[]
several_three_tab_switches_list=[]
## get second switch numbers check if many #returns list of inner switch id numbers
##########################################################
## get_second_switch_numbers_check_if_many(stringname):
############################################################
def get_second_switch_numbers_check_if_many(stringname): #this might be for when
	print("get_second_switch_numbers_check_if_many(stringname): Grinch stole christmas")
	print(" ..get_switch_number.. ")
	awesome=''
	counter =0  #say it's 3
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter=0
	targetswitch =0
	for line in stringname.splitlines():
		tablength = line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3:
			targetswitch += 1 
			counter += 1
		else:
			counter += 1
	#end loop
	print("this should return 2")
	print("number of switches at 3 tabs meaning first level =",targetswitch)
	
	#first check if tab length == 3
	counter=0
	smart=False #default setting
	for line in stringname.splitlines():
		tablength=line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3 and counter > 1 and "#" in line:
			x = line.split("#")  
			y = x[1];print(y)
			if ":" in y:
				y=y.replace(":","")
			print(y)
			several_three_tab_switches_list.append(y)
			peachtree.append(several_three_tab_switches_list)
			smart= True
			counter += 1
			continue
		else:
			counter += 1
			continue
		#print if the list is empty put a 0 in it
		print("special case test")
	if smart != True:	
		several_three_tab_switches_list.append(0)
		peachtree.append(several_three_tab_switches_list)
	#end loop
	print("this is key its NOT LOOKING FOR DEEPLY nested but only at 3 tabs >>")
	print("we are here now after filling switch list with inner switches at level 3 tabs")
	#print("several_three_tab_switches_list=",several_three_tab_switches_list)
	#print("this should return a list whith these two numbers in it 11 62")
	#for item in several_three_tab_switches_list:
	#    weasel=get_switch_number(testcode)
	#   


##==========================================================
# the issue is that on the second pass it is using the original string
# and it needs to be using the modified string
# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
# because the numbering system of the string starts from 1 too.
	
# what to work on today thursday, october 14th, 2021 ,,,,,,,,,
# so I would feed in just a param to look for "#" AND "switch" AND "31" and get tabdepth
# I need to try calling and looking for switch in line and # and the number 31
# and loop thru to endswitch at same tab depth.
# get tab depth on switch   tab_depth1 = line.count("\t")
# and then the first line with "endswitch" in line and this_tab_depth == tab_depth1	
##========================================================================
##  def next_metamorphosis_take_out_inner_switch(stringname,switch_number):
##=========================================================================
baton=[]
baton.append(0) #this creates the first slot 0
start=''
finish=''
string_name=''
switch_tab_depth=''
stringname=bigstringtest1
#this gets the endswitch line number that we need
#then I will call skip rope to finish the cutting out of the inner switch case


input_to_get_inner_switch=[]
string_after_cutting_out_inner_switch_body=[]
string_after_cutting_out_inner_switch_body.append(0)

hp=[]
hp.append(0)
lightning=[]
lightning.append(0)
#global concatthis;
	#this just might work 
	#this is a flag to pass the existing concatted string to be used fresh for next switch
	#this list is preset at False 
	#so this starts out false and passes thru it and then the list which used to have
	#FAlse in it has a string in it thereafter and the modified string from first pass
	#and subsequent passes is the new string to modify on the fly
	
#this requires the string name and start and finish to work
#this takes one nested switch with start and finish locations
#this method must be given start and finish in the params
#this prints out the new string after cutting out the nested switch except for the switch word
##========================================================================
## skip_rope_skipping_some_lines()  this cuts out ONE inner switch body
##========================================================================
def skip_rope_skipping_some_lines(string_name,start,finish):#start line nest switch and finish  endswitch
	print("start= ",start,"finish= ",finish)
	if string_after_cutting_out_inner_switch_body[0] == False: #starting
		print("it is False it is  empty ")
	else: 
		string_name = string_after_cutting_out_inner_switch_body[0]
		print('it is NOT False and therefore we fill the string from the list[0]')
	concatthis=''
	print("===skip_rope_skipping_some_lines(string_name,start,finish)====")
	#string_after_cutting_out_inner_switch_body[0]
	print(string_name)
	counter=0; #concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	print("string_name=",string_name,"start=",start,"finish=",finish)
	for line in string_name.splitlines(): 
		if counter > start  and counter <= finish: 
			#print(line) #it won't print the switch word since it's skipping it
			counter += 1; continue
		else: 
			concatthis += line + "\n"; counter += 1; continue
	#print('it created this SILLY STRING === multi colored silly string=')
	#print(concatthis)
	#print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
	weasel=string_after_cutting_out_inner_switch_body[0]
	#for line in weasel.splitlines():
	#	print(line)
	#return weasel  #I need to return from each for the piping to work correctly
	lightning[0] = concatthis
	#for line in lightning[0].splitlines():
	#    print(line)


##=====================================================
##  modern_take_out_endswitch(string):
##======================================================
def modern_take_out_endswitch(inputstring):
	print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			print("detected } in line")
			location = line.index("#")    #gets location from left where position of #
			line = line[:location] 
			print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			print("after left shift it is ",line)
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():




test_string1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru	
		case 4 to 7:
			print('kangaroo hop hop!')#
			#############1
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################5
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default
											print("we very done") 
									endswitch 
							#############k
									break
								default
									print("we are done here")
							endswitch #46  
							#############k
							break
						default
							print("we are done here")
					endswitch #51   
					#############)
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default
					print("we are done here") 
			endswitch #60  
			exp = 32
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default
					print("we are done here") 
			endswitch #86   
			##############)
			print('taught me how to write code')
			fallthru	
			 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru	
		default
			print('the end')
	endswitch #100  
'''
test_string2='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					####################
					switch(exp){ #23
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #31
								case 'fishy':
									print("do something")
									print("yep")
									fallthru
								case 'where now':
									print("nice")
									break
								default:
									print("we very done")
							endswitch 
					#############
							break
						default:
							print("we are done here")
					endswitch #46  2.......
					#############
					break
				default:
					print("we are done here")
			endswitch #51   3 ...
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs 
'''

test_string3='''
	switch(exp){ #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #23
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					####################
					switch(exp){ #31
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'where now':
							print("nice")
							break
						default:
							print("we very done")
					endswitch 
			#############
					break
				default:
					print("we are done here")
			endswitch #46  2.......
			#############
			break
		default:
			print("we are done here")
	endswitch #51   3 ...
'''

test_string4='''
	switch(exp){ #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################1
			switch(exp){ #31
				case 'fishy':
					print("do something")
					print("yep")
					fallthru:
				case 'where now':
					print("nice")
					break
				default:
					print("we very done") 
			endswitch 
			#############k
			break
		default
			print("we are done here")
	endswitch #46  .
'''

test_string5='''
	switch(exp){ #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
	endswitch #41
'''

test_string6='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66
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
			endswitch #77 5 .....
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86
'''

test_string7='''
	switch(exp){ #66
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
	endswitch #77 5 .....
'''
# instead what if I feel a list of switches at 3 tabs and endswitches at 3 tabs
# and make pairs and then use the skip robe which already works and that way 
# I will reuse working code and based on the length of the switch list I just
# look in both lists at the same location position 0 and then 1 etc.
print("big test....starbucks morgan hill ========")

switch_list=[]
endswitch_list=[]
total_switches_at_3tabs_depth=[]

#delete helper lists first
def delete_helper_lists_first():
	del total_switches_at_3tabs_depth[:]
	del switch_list[:]
	del endswitch_list[:]
	
#this gets the important switch and endswitch at 3 tabs length which is critical.
def get_switch_and_endswitch_locations_in_string(string_name):
	print("====||||  get switch and endswitch locations in string  ||||======")
	delete_helper_lists_first()
	#count how many switches at tab depth 3
	####=================
	switchcount=0
	counter = 0
	for line in string_name.splitlines():
	    tabdepth = line.count("\t")
	    if "switch" in line and "end" not in line and tabdepth == 3:
	        switchcount += 1 #doesn't have ++
	        total_switches_at_3tabs_depth.append(counter)
	        counter += 1
	        continue
	    else:
	        counter += 1
	        continue
	####===================
	print("total switch at 3 tabs in this string",len(total_switches_at_3tabs_depth))
	print("they start on these lines",total_switches_at_3tabs_depth)
	#count_switches_at_threetabs= string_name.count("
	counter=0; concatthis =''; #finish = finish + 1 
	print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'switch' in line and "end" not in line and tabdepth == 3: 
			switch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("phase 2 here ====")
	counter=0; concatthis =''; #finish = finish + 1 
	#print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'endswitch' in line and tabdepth == 3: 
			endswitch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	print("end of line...")
	########################======
	
	########################==========
print("calling get switch and endswitch locations (only one set) in string ")
#this needs to be done first ===== before calling the function

print("should be 1 for this test")
#del switch_list[:]
#del endswitch_list[:]
print('real test now i really need this puppy to work')





#del total_switches_at_3tabs_depth[:] #empty it first 
#del switch_list[:]
#del endswitch_list[:]
#print('real test now in string with more than one inner switch at 3 tabs should be 2')
get_switch_and_endswitch_locations_in_string(test_string1)
#mylist=[]
#mylist.append(5)
print("did it even work or not?!---00000000000000000 mocha")
#exit()

'''
print("======experimenting with test_string1========")
if total_switches_at_3tabs_depth[0] > 1:
    number_to_loop = total_switches_at_3tabs_depth[0]
    print("number to loop=",number_to_loop)
else:
    print("nope only one inner switch at 3 tabs")   
if number_to_loop == 2:
    print("True that number to loop = 2")
    print("1st loop == ")
    x = 0
    start  = switch_list[x]
    finish = endswitch_list[x] 
    print("start=",start)
    print("finish=",finish)
    print("2nd loop === ")
    x=1
    start  = switch_list[x]
    finish = endswitch_list[x] 
    print("start=",start)
    print("finish=",finish)
#end if
'''      
#mylist.append(17)
print("doing test_string6")

print("halloween is nearly here test======..........")
print("switchlist =",switch_list)
print("endswitchlist =",endswitch_list)
print("==============")
#start  = switch_list[0]
#finish = endswitch_list[0]
#currently skip rope method only does one switch to endswitch set so I would use a loop
#and put skip rope in it to do multiple ones


# input 62, look in dictionary to get the 86
# input 11, look in dicitonary get the 60 
print('testing test_string2 ...')
#start = 5
#finish = 41
#this needs to be called first 
print('testing test_string2')
###====-=====================================================
print("this has to be done fifrst need to get switch and endswith lcoations")
print("=======")
#delete_helper_lists_first() #trying this out

print("this needs to be called first get_switch_and_endswitch_locations_in_string()")
get_switch_and_endswitch_locations_in_string(test_string2) #for this switch string

print('we have switch_list=',switch_list)
print("endswitch_list=",endswitch_list)
print('........... what do the lists say above ....')
start  = switch_list[0]  #5
finish = endswitch_list[0]  #41   #below this means that it's empty, False to set flag
string_after_cutting_out_inner_switch_body[0]= False #set this to False first
print("calling skip rope skipping some lines with inputs ",start,"and ",finish)
print("======testing string2======")
skip_rope_skipping_some_lines(test_string2,start,finish)
###=======================================================
#exit()
###======================================================================
print("=======testing test_string6======")
#this is only designed to cut out ONE inner switch 
print("calling skip rope skipping some lines with inputs ",start,"and ",finish)
skip_rope_skipping_some_lines(test_string6,start,finish)

print('now string1 with 2 nested switches=== star trek time====')
print("testing 1..")
#need to find the switches locations and work from the bottom up so do second inner switch first
#that's how the macros work bottom up that way I can use the numbering input correctly. 


### here it has to do the cutting out in reverse since more than one inner switch to cut out
### I learned this trick from my macros solution
#### relooking at this on oct 22nd friday, at 10:46 am 2021
###=========================================================================
#this will be a special method for dealing with reducing down 2 or more inner switches to switch word
print("PUFF THE MAGIC DRAGON === THIS SHOULD ALREADY WORK== ")

# need to make this into a method that has some fuzzy logic
print("TESTING WITH 62 AND 86 SKIPPING ROPE")
#this needs to be put into a method 
#this needs to be set to False to work correctly.
#first we set it to False


#what this does is go thru a list that is in reverse order to cut out thru skipping
# a string to take out inner switches at 3 tab level.  it actually works.
# I need to have a modified one if only one list 

#we will have a loop ::; put this together on Friday, October 22nd, 2021 at 11 am
#string_after_cutting_out_inner_switch_body[0]= False 
#if len(inputlist) == 1:  good if only one list and reverse calls it does nothin
#what this does is loop thru a list of switch endswitch at 3 tabs and does more than one


###========================================================================
## convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
###=========================================================================
def convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
    print(" ====convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):==== ")
    string_after_cutting_out_inner_switch_body[0]= False        #necessary default flag 
    counter=0 #where am I filling inputlist?
    for item in inputlist: #this grabs the params from item     #list of switches pairs start stop at 3 tabs depth
        start = item[0];
        finish = item[1];
        print('start=',start,'','finish=',finish)                       #62; finish=86 
        skip_rope_skipping_some_lines(stringname,start,finish)  #this copies the string skipping the range designated
        counter +=1
        print("counter=>>",counter)
        print("=====================")
    print("at bottom of converts  with more than one inner switch at 3 tabs")
    print("testing if weasel is returnable at the end of the function")
     #this is after it's done
    #for line in weasel.splitlines():
    #    print(line)
    #return weasel 

	
print("I am fillilng the inputlist right here manually force feeding it.")
#this calls it but right now I want to know where I fill th einputlist
inputlist =[]
inputlist.append([11,60])
inputlist.append([62,86])
print(inputlist)
inputlist.reverse() #reversing the list since the cutting out must be done bottom up to work properly

print("after reversing the list we now have===")
print(inputlist)
print("convert switch with more than one inner switch at 3 tabs(stringname)==== string1")
#get_switch_and_endswitch_locations_in_string(test_string1) #presumes one inner switch 
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("THIS IS THE BIG CHRISTMAS TEST =====*******=====")
print("====real deal here ===GET SWITCH AND ENDSWITCH LOCATIONS========")
print("this needs to be called first get_switch_and_endswitch_locations_in_string()")
#get_switch_and_endswitch_locations_in_string(test_string1) #for this switch string
#print('we have switch_list=',switch_list)
#print("endswitch_list=",endswitch_list)
#it needs to make these [[11, 60], [62, 86]]
###testing nov 27th at 10:46am starbucks
print('important testing on Saturday morning')
trialinputlist=[]
inputlist =[]

#made nov 27th, satgurday 4:15pm morgan hill starbucks 
##===========================
## build_trail_inputlist()
##===========================
def build_trial_inputlist(): #this combines switch and endswitch into pair into trialinputlist
	del inputlist[:] #this empties the input list discarding previous data in it
	del trialinputlist[:]
	print("build_trail_inputlist()..")
	counter=0;
	for item in switch_list:
		pair=[switch_list[counter],endswitch_list[counter]]
		trialinputlist.append(pair)
		counter += 1
		
	print("look for the ball on the green")
	print("trialinputlist=",trialinputlist)
	for item in trialinputlist:
		inputlist.append(item)
	print("inputlist=",inputlist)
	for item in inputlist:
		print(item)
	inputlist.reverse() #is this needed here or not 

	
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string1)
print('end of the show sunday morning blues coding')
print("Super silly string 1 PHASE 1 taking out two nested switches at 3 tabs location bottom one first")
print('end of the show sunday morning blues turkey day 2')
print('doing the same string a 2nd time to see if it works')
print("............................................")
print("now trying test_string2")
#del switch_list[:]
#del endswitch_list[:]
print("do you see what I see??")
#inputstring=test_string1
outputstring=[]
outputstring.append(0)
snowboarding=[]


##=================================
## take_out_switch_body(astring):  #def foxnews(astring):
##================================
def take_out_switch_body(astring): #this was foxnews
	nestedswitch= False
	print("take_out_switch_body(string)      today is november 28th sunday  4:29 pm ")
	#right here look if a switch at 3 tabs if not skip below
	####=== new as of monday december 6th, 2021 =========================
	#determine if 
	for line in astring.splitlines():
		tabcount =line.count("\t")
		if "switch" in line and tabcount == 3:
			print("yes switch at 3 tabs in line")
			print("frosty says switch at 3 tabs confirmed")
			nestedswitch= True
			break
	print("frosty the snow man light test for nested switch")
	print("nestedswitch=",nestedswitch)
	print("==================================")
	if nestedswitch == False: #what this does is put the input string into output
		#add input into output  this means no changes were done to the switch string
		print("this switch string DOES NOT have an inner switch")
		lightning[0]=astring 
	else:
	##======= this is down here now ========december 6th 2022 =========
		get_switch_and_endswitch_locations_in_string(astring) #for this switch string
		build_trial_inputlist()	 #this is new 
		convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)
	#end if
	##########================================================================
	print("frosty snowboarding")
	#december 6th looking where I am not adding31 and 66 
	
	print("this is new code now today is Monday november 29th now Dec 6th.")
	print("what is in lightning[0] now")
	#print(lightning[0])
	
	print("resulting final output of take_out_switch_body:") 
	snowboarding.append(lightning[0])  #this is new dec 6th monday
	for line in lightning[0].splitlines():
		print(line)


print("testing this 2nd method")
print("testing take_out_switch_body now") 
print("========TAKE OUT SWITCH BODY()========")
take_out_switch_body(test_string1) #the first one has more than one inner switch it takes out
take_out_switch_body(test_string2)
take_out_switch_body(test_string3)
take_out_switch_body(test_string4)
take_out_switch_body(test_string5)
take_out_switch_body(test_string6)
take_out_switch_body(test_string7)

#gotta take out } in switches 
print("big test if it works right or not")
print("printing out snowboarding list") 
#this should print out just the final product
print("SNOWBOARDING LIST OUTPUT")
counter=1
for item in snowboarding:
    print("counter=",counter)
    print(item)
    print("========")
    counter +=1
    
    

#exit()
   
#def finally_reduce_inner_switches_at_three_tabs_into_switch_word(inputstring):
print("where is the christmas tree test===== doing test_string  1 ===========")
get_switch_and_endswitch_locations_in_string(test_string1) #for this switch string
build_trial_inputlist()	 #this is new 
print("right here what is in inputlist=",inputlist) #needs to be reversed
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string1)
print("end of christmas tree test test string 1 with 2 nested switches at 3 tabs")
#exit()

print("where is the christmas tree test===== doing test_string   2 ===========")
get_switch_and_endswitch_locations_in_string(test_string2) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string2)
print("anotehr one 3")
print("where is the christmas tree test===== doing test_string  3 ===========")
get_switch_and_endswitch_locations_in_string(test_string3) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string3)


print("where is the christmas tree test===== doing test_string  4 ===========")
get_switch_and_endswitch_locations_in_string(test_string4) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string4)


print("testing another one now===== doing test_string  6 ==========")
get_switch_and_endswitch_locations_in_string(test_string6) #for this switch string
build_trial_inputlist()	 #this is new 
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string6)

#exit()

# method chaining
# getone.getteo.getthree()

#=======
#Bottom of chain methods result if methods goes into
#output[0]

#Where is transform_string() called

#https://www.google.com/amp/s/nypost.com/2021/11/11/ufos-buzzing-us-warships-may-be-aliens-top-spy-chief/amp/

#Good stuff

#https://m.youtube.com/watch?v=azZ4XAZuVk4




print(inputlist)
#inputlist.reverse() #reversing the list since the cutting out must be done bottom up to work properly

print("after reversing the list we now have===")
#print(inputlist)
#get_switch_and_endswitch_locations_in_string(test_string2)
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string2)
print('pizza for dinner maybe')
#exit()

#inputlist =[]
#inputlist.append([10,36])


#get_switch_and_endswitch_locations_in_string(test_string3)
print('end of the show sunday morning blues turkey day 3')
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string3)

#rint('end of the show sunday morning blues turkey day 4')
#convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string4)
inputlist =[]
inputlist.append([5,16])
print('end of the show sunday morning blues turkey day 6')
convert_switch_with_more_than_one_inner_switch_at_3_tabs(test_string6)
print("wow wow")


#string_after_cutting_out_inner_switch_body[0]= False  #just filler but a flag meaning empty

#exit()
#print("testing input 62, 86 skipping rope")
#start=62; finish=86  #[62,86] #input values fed into it 
#skip_rope_skipping_some_lines(test_string1,start,finish)#62,86

#start=11; finish=60  #[11,60]
#skip_rope_skipping_some_lines(test_string1,start,finish)#11,60

print(" super silly string 2 PHASE 2 taking out 2nd nested switch (the higher first one done second) at 3 tabs")
print("TESTING WITH 11 AND 60 SKIPPING ROPE")
print("testing 11,60 inputs for skip rope skipping some lines ")
print("testing 2...") 







print("after doing this which needs to be made into a function with a loop")
print("it will need input of [[11,60],[62,86]] that I reverse if more than one in it")
#listname.reverse()
#so I can use teh same string to do both cuts out of inner switches 
#first     62,86
#second is 11,60

#exit()
#skip_rope_skipping_some_lines(string_name,start,finish)
#critical_list= [[11, 62], [15], [23], [31], [0], [66], [0]]
#end of show

# tuesday, october 19th, 2021  time 9:52 morgan hill starbucks
#==================================
# cut_out_switch_body_no_params   october 19th tuesday
#==================================
#abandoned this appraoch 
# objective is to go through string and take out switch bodies without inputs
'''
def cut_out_switch_body_no_params(string_name):
	print("cut out switch body no params===")
	counter=1; concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	#start  = input_to_get_inner_switch[0]
	#finish = input_to_get_inner_switch[1]
	
	#what about a quick search for locations of switch and endswitch
	for line in string_name.splitlines(): 
		if "switch" not in line and "endswitch"  not in line and tabdepth != 3:
			print(line)
		#notice start +1 based on line number 
		tabdepth = line.count("\t")
		if "switch" in line and "end" not in line and tabdepth == 3:
		#actaully I don't want 
			concatthis += line + "\n"; counter += 1; continue
			print(line) #it won't print the switch word since it's skipping it
			
		 else: 
			 counter += 1; continue
		if "endswitch" in line and tabdepth == 3:
			print(line)#get current line then break
			concatthis += line + "\n"; counter += 1; continue
			#break
	print("===output from skipping some lines====")
	print('it created this SILLY STRING === multi colored silly string=')
	print(concatthis)
	for line in concatthis.splitlines():
		print(line)
	print("=======")
	print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
##========== new version 
	print("here we have the halloween special START SKIPPING ROPE...")
	print("the output string looks like this")
	weasel=string_after_cutting_out_inner_switch_body[0]
	for line in weasel.splitlines():
	    print(line)
'''	
	
	
print("testing cutting out the inner switch bodies to see if it works")	
#cut_out_switch_body_no_params(test_string6)
### this is now working correctly taking into account
# that lines start from 0 not 1 and I need to skip and include the switch word


#next go thru list of stirngs and take out inner switches bodies


#Never theorize before you have data.Invariably you end up twisting facts to suit theories instead of theories to suit facts. -Sherlock holmes.
#There is nothing more deceptive than an obvious fact


##================================= testing at starbucks gilroy christmas tree
#####transform_string() #12379






##========================================================================
##  def next_metamorphosis_take_out_inner_switch(stringname,switch_number):
##=========================================================================
def next_metamorphosis_take_out_inner_switch(string_name,switch_number):
	print("==next_metamorphosis_take_out_inner_switch)====")
	print("==next_metamorphosis_take_out_inner_switch)====")
	switch_tab_depth=''
	counter=1 #look we are starting to count from 1
	startcount =0
	endswitchline=0
	end_switch_tab_depth=''
	#get inner switch location all we know is the switch line number 31 in this case 
	#get switch_tab_depth
	print("the switch_number=",str(switch_number))
	for line in stringname.splitlines():   #switchnumber 31
		if "switch" in line and  "end" not in line and "#" in line and str(switch_number) in line:
			print("31 in line and switch in line and end not in line and # in line ALL TRUE")
			switch_tab_depth = line.count("\t") #gets tab depth
			startcount= counter
			end_switch_tab_depth=switch_tab_depth #see if this works now
			break
		else:
			counter += 1
			continue
	#get endswitch location
	print("startcount =",startcount) #targer switch line number 
	print("target switch_tab_depth =",switch_tab_depth)
	print("END OF PHASE 1 ...")
	
	#get endswitch tab depth
	print("============================")
	counter = 1 #get endswitch tab depth
	for line in string_name.splitlines():
		this_line_tabs= line.count("\t")
		if "endswitch" in line and counter > startcount:
			this_tab_depth = line.count("\t")
			if counter > startcount and this_tab_depth == switch_tab_depth: #this means endswitch must be AFTER switch
				endswitchline = counter
				#the tab depth MUST be the same as the target switch tab depth 
				break
			else:
				counter +=1
		else:
			counter += 1
			continue
			
	print("end_switch_tab_depth=",end_switch_tab_depth)
	print("the end switch line=",endswitchline)
	print("=============================")
	print("END of PHASE 2...")
	counter =1
	for line in string_name.splitlines():
		if "endswitch" in line and counter == endswitchline:
				endcount = counter
				break		
		else:
			counter += 1
	
	startcount = startcount-1 #because we skip switch and keep it. 	
	print("output of next_metamorphosis()")
	print("startcount=",startcount) #oh this is brilliant
	start = startcount
	print("the endswitch line =",endswitchline)
	finish = endswitchline
	print('start=',start)
	print('finish=',finish)
	input_to_get_inner_switch.append(start)  #[0]
	input_to_get_inner_switch.append(finish) #[1]
	print("start=",input_to_get_inner_switch[0])
	print("finish=",input_to_get_inner_switch[1])
	print("switch_tab_depth=",switch_tab_depth)
	#now I can run the skip lines code that requires the start and finish range numbers
	print(" END of PHASE 3 ...")
	print("again this doesn't modify the switch string it just gets input data")
	print("for the next phase which is skipping rope")
	
#notice start +1 based on line number 
#		#because numbers are off by 1 since starting at 0 not 1 in counting
#		#if counter > start +1 and counter <= finish: 
#		if "endswitch" not in line and this_tab_depth == switch_tab_depth: 
#			print(line) #it won't print the switch word since it's skipping it
#			counter += 1; continue
#		else: 
#			concatthis += line + "\n"; counter += 1; continue
#	print("===output from skipping some lines====")
#	print('it created this SILLY STRING ====')
#	print(concatthis)
	
#for the first pass flag_test[0]= False and then it's flipped to True
	#print("flag_test[0]=",flag_test[0])
	#if flag_test[0] == False or flag_test[0] == None: #meaning first pass  and what it's set to by DEFAULT
	#    smart=x;
	#    #change it to True now
	#    flag_test[0] = True #this should now be tru e
	#else: #meaning TRUE this is run after first run of skipping_some_lines()
	#    x = baton[0]
	### look that we have the counter here set to 1 by default 
	



#===========================
print("HERE WE START METAMORPHOSIS ENTERING THE MATRIX...")
#this one has to be called first since it creates the start and finish lines for this string
#based on what the switch number is in the comment which it will look for
#and the inner switch line numbers will be known beforehand
#because they are automatically added 

#def take_out_inner_switch_bodies(thestring):
#first I need to get the nested switch number (assuming one at this point)
## I need to make this into a method witht he two functions below
#working on this october 14th, 2021 gilroy 6:55pm

#I need to get the inner commented switch number 
###=====================================================
print("three, two,one, blast off===>>>")
string_name= bigstringtest # <=== string is in here 
#I need to put the method here that gets the switch comment number
#switch_number=31 #I need to get this number automatically
#this will be different if there are more than one inner switch at 3 tabs length
#I still need to clean up the copied switches so the first switch is at 1 tab
#and the next next level switches start at 3 tabs
#for this first attempt we will limit the inner switches to just one
axis=get_second_switch_number(bigstringtest) #returns 31
#should be 31 
print("axis should be 31",axis)
switch_number = axis #finally getting closer to victory
####===============================
#I have code that get the inner switch number if only one
#and I have code that can find all inner switches at 3 tab level depth 
#what this does is rip out the nested switch body leaving the switch
# word in the nest_list after separating the switch bodies
#this is an important step and I just figured out how to
# detect if more than one inner switch at the three tab level depth
## make this into a method now

# I also got the code to get the second switch in a string line number  in the comment
#which will invariably be different from the true line number, but that's okay.
#=================================================
#=================================================
#=================================================
#=================================================
##========== halloween darkness  oct 14th ===================


print("cinderella")

get_second_switch_numbers_check_if_many(foolish)
print("the result of the  if_many method is to put the inner switches numbers at 3 tabs")
print("into the list which is below")
print("several_three_tab_switches_list=",several_three_tab_switches_list)
print("")
print(" back to the future should be above for stirng foolish")

print("testing bigstringtest1")
print("let us see if this works...")
print("the dark knight is here")
del several_three_tab_switches_list[:]
print('here we go')
get_second_switch_numbers_check_if_many(bigstringtest1) #using bigstringtest1 now
start=''
finish =''

print('end of this test of get second swithc numbers check if many')
print('waiting to get it working')


#I need to go thru each string and count the switches at 3 tabs
#do the loop jazz too.
##=========================================================
##  count_inner_switches_at_first_level(inputstring)
##=========================================================
def count_inner_switches_at_first_level(inputstring):
	print("=====count inner switches at first level=== so at 3 tabs ==")
	counter =0
	innerswitch = 0
	for line in inputstring.splitlines():
		tabdepth = line.count("\t") #added and "end" not in line to eliminate endswitch bug
		if "switch" in line and "end" not in line and tabdepth == 3:
			print("the line number is ",counter)
			linewithswitch =counter
			innerswitch += 1
			counter += 1
		else:
			counter += 1
			
	print("innerswitch count at 3 tabs in this string=",innerswitch)
	print("the line number of the sole inner switch is",linewithswitch)
	return innerswitch;

inputstring = bigstringtest1
#this counts inner switches at 3 tabs indentation in a switch string
total=count_inner_switches_at_first_level(inputstring) #calls the method above


print(" we are done here, of the number of inner switches at 3 tabs = ",total)
#where do I get the inner switch number??
print("=========.........")
print("=========....halloween pumpkins are coming.....")
print("=========.........")
 #this calculates the start and finish of one nested switch 
string_name=bigstringtest1 #I need to find the get switch number for inner switch
switch_number=several_three_tab_switches_list[0] #this presumes only one inner switch
switch_number = int(switch_number) #right here a miracle occurs==== 
print(type(switch_number)) #this gets the start and finish numbers for inner switch to cut out
next_metamorphosis_take_out_inner_switch(string_name,switch_number)
print("it should be 9 and 20 and it shows...")
#all this does is create the start and finish line numbers of one inner switch
print(input_to_get_inner_switch[0])  
print(input_to_get_inner_switch[1])
print("string_name=",string_name,"start=",start,"finish=",finish)

print("go for the gold medal===================")
string_name= bigstringtest1
#I am feedingit 9 and 20 to start with here 
#here the inner start and finish of an inner switch is inserted
start =input_to_get_inner_switch[0]#9  #=input_to_get_inner_switch[0]  #9 #1 after switch line number so it really does 10 compensating 
finish=input_to_get_inner_switch[1]#)20 # =input_to_get_inner_switch[1] #=20
print("SKIPPING ROPE NOW to modify the string and cut out inner switch")
skip_rope_skipping_some_lines(string_name,start,finish)
#skip rope takes out the inners switch leaving the inner switch word.
print("The GREEN EXIT SIGN NOW")
#exit()
#=================================================
#=================================================
#=================================================
#=================================================
#=================================================
#=================================================

#skip_rope_skipping_some_lines(string_name,start,finish)
#it needs to return values to start and finish as input for 
#skip_rope_skipping_some_lines(string_name,start,finish)

#now I need to count switches in a string
#and as a backup safety count endswitches also.


#I can work on these separately actually 
################
teststring1='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  
							#############
							break
						default:
							print("we are done here")
					endswitch #51   
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   
			exp = 3
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86   
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
	endswitch #100  
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [11, 60]
#counter= 2
teststring2='''
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   4..........endwitch 4  line 60 3 tabs 
'''
#==========-----------seperated nest strings -----------------
#getting data in blueberries [15, 51]
#counter= 3  THIS IS 5 TABS IN FIRST LINE 
teststring3='''
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  2.......
							#############
							break
						default:
							print("we are done here")
					endswitch #51   3 ...
'''


#==========-----------seperated nest strings -----------------
#getting data in blueberries [23, 46]
#counter= 4 this one works 
#I have to reduce these downto first tab and then three tabs
teststring4='''
	switch(exp){ #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################
			switch(exp){ #31
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'where now':
					print("nice")
					break
				default:
					print("we very done")
			endswitch 
			#############
			break
		default:
			print("we are done here")
	endswitch #46  2.......
'''
#==========-----------seperated nest strings -----------------
#getting data in blueberries [31, 41]
#counter= 5
teststring5='''
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [62, 86]
#counter= 6
teststring6='''
			switch(exp){ #62
				case 'burger':
					print("do something")
					####################
					switch(exp){ #66
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
					endswitch #77 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #86
'''

#==========-----------seperated nest strings -----------------
#getting data in blueberries [66, 77]
#counter= 7   THIS IS 5 tabs in first switch line 
teststring7='''
					switch(exp){ #66
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
					endswitch #77 5 .....
'''

#==========-----------seperated nest strings -----------------
print("moving tabs out.")
print("testing moving extra tabs out of a string")
print("this is looping thru teststring3 ")
print("Grand Canyon test Friday")
print("I will take out 5 tabs from the front of each line")
for line in teststring3.splitlines():
    print(line)
print("end of test of printing out teststring3")
print(" ")
counter =0
switch_actual_tabs=[]
switch_actual_tabs.append(0)
import re
onetab="\t"  # here is onetab declared with one tab inside of it
fishbowl=[]
fishbowl.append(0)




#sunday confirmation number sundayoct 17th, 2021
holdon=[]
holdon.append(0)
holdthis=[]
holdthis.append(0)
galaxy=''
#this swaps endswitch with }
#what this does is replace endswitch with '}
###===================================
##  take_out_endswitch(stringname)
###===================================
def take_out_endswitch(stringname):
	print("take_out_endswitch()  called=====")
	answer=''
	galaxy = stringname
	print(galaxy)  #using replace endswitch with }
	#this replaces all endswitch(es) to }
	holdthis[0] = galaxy.replace("endswitch","}") #added here
	#bug what if there is already a curly brace but no endswitch
	print(holdthis[0])
	#move it to left
	answer = holdthis[0]
	newstring=''
	for line in holdthis[0].splitlines():
		if "}" in line and "\t" in line:
			line = line.lstrip()
			newstring += line
		else:
			newstring += line + "\n"
			
	holdthis[0] = newstring
	
	print(holdthis[0])
	for line in holdthis[0].splitlines():
		print(line)
		
	#return answer;
	
	#galaxy = holdthis[0]
	#holdon[0] =holdthis[0]
	#return galaxy
	
	
	
	
	

##==========================================
## shift_nest_string_to_left(stringname)   made on oct 15th, 2021 8:57 am
##==========================================
def shift_nest_string_to_left(stringname):   #cuts out tabs and adds new tabs automatically
    print("========= shift_nest_string_to_left(stringname ===... =====")
    for line in stringname.splitlines():
        print(line)
    #print("this is th einput string====")
    newline=''
    counter=0
    thismatters=''
    print("shift_nest_string_to_left() called")
    for line in stringname.splitlines():
        tabslength = line.count("\t") #this is set up for string3 initially. 
        print("tabslength=",tabslength)
        #counter +=1
        if counter == 1 and "switch" in line: #just added this oct 15th 
            #print(line)
            #print("we care about THIS ONE",tabslength)
            switch_actual_tabs[0] = tabslength
            #print("switch_actual_tabs[0]===",switch_actual_tabs[0])
        else:
            print("he well")
        print("=================>>>=======")
        #For teststring3  if 5 tabs in first line then tabslength-4  because it has 5
        ##==================================================================
        clever=0 #starting give it default value of 0 
        #this one works
        if switch_actual_tabs[0] == int(5): #5-4
            clever = 4
            #print("let's see if clever is an int here")
            #print(type(clever))  
            
        #for some reason this if below is not working right    
        if switch_actual_tabs[0] == int(3): #3 - 2 #reducing to 1 tab on first line
            clever = 1
            #print("let's see if clever is an int here")
            #print(type(clever))  
        #so if 5 -4 giving us 1
        #if 6 -5
        #if 7 -6 giving us 1
        #if 4 -3
        #if 3-2
        #if 1 do nothing
        #this is based on it having 5 tabs in line one and minus 4 tabs
        #if tabslength == 3:
        #    tabslength = 1; #which is -2
            
        #if tabslength == 5:
        #    tabslength = 1 #which is -4
        #I think what I need to do is determine indentation before first switch to gauge it    
        print(" switch_actual_tabs[0]=", switch_actual_tabs[0])
        #total_tabs_to_add=''
        ##########################################
        #if 5 tabs then -4
        #if 3 tabs then -2
        total_tabs_to_add=''   #this was 4 changed it to celver
        print("at this point what is the value of clever",clever)
        total_tabs_to_add =int(tabslength) - int(clever) # reducing it to 1 taking 4 tabs off  #right here 
        print("====")
        print("at this point what is the value of total tabs to add",total_tabs_to_add)
        #print("position 1 type test")
        #print(type(total_tabs_to_add))
       
        #this is what I took out above and replace with below 
        #total_tabs_to_add = ''
       # print("testing boolean condition here ....")
        print("tablength in first switch line =",tabslength)
        #====== if tablength = 5 -==========================
        if tabslength == 5:
            #print("TRUE HERE flying horse to locate this ")
            total_tabs_to_add = tabslength - 4 #TO GET 1
            print("total tabs to add right here =",total_tabs_to_add)
        #end if
        print("====")
        #number one rule code does exactly what you tell it to do. 
        #====== if tablength = 3 -==========================
        if tabslength == 3:
            #print("TRUE HERE flying horse to locate this ")
            total_tabs_to_add = tabslength - 2 #TO GET 1
            print("total tabs to add right here =",total_tabs_to_add)
            
        #print("position 2 type test")
        #print(type(total_tabs_to_add))
        
        #if tabslength == 3:
        #    total_tabs_to_add = tabslength - 2 
        #end if
        #print("=====")
        #print("position 3 type test")
        #print(type(total_tabs_to_add))
       
        #print("so this line will have this many tabs in front",total_tabs_to_add)
        total_tabs_to_add = total_tabs_to_add * onetab #times 1 tab #0 x 1 = 0
        print("RESULT= total_tabs_to_add to each line",total_tabs_to_add)
        myString = line
        output   = re.sub(r"[\t]*", "", myString)    #takes all tabs out of this line
        newline += total_tabs_to_add + output + "\n" #this puts the tabs in front of the stripped string line
        counter +=1
        continue
    #print('the result is..')
    print("this prints out the output what the changed indentation shift to left looks like")
    #return newline
    fishbowl[0] = newline  #the output of shifting to left 
    for line in newline.splitlines():
        print(line)
#print("drink coca-cola test")
#print("TESTING 3")    
#print("starbucks breakfast of friday testing..")
#print("testing indenting correclty teststring3")
#shift nest string to left
shift_nest_string_to_left(teststring3) #good 5 TABS DOWN TO 1
print("red alert test 3 shift nest stirng to left side ... test 3 ")
print("look carefully at this and make sure that it's right with just one tab at top")
print("testing with string skitahoe")
shift_nest_string_to_left(skitahoe) 
print('first we will do this simple test with no tabs see if it returns 0')
practicestring='''
switch(exp){
    case 1:
        print('hello')
'''
tabsinthisline =''
for line in practicestring.splitlines():
    if "switch" in line:
        tabsinthisline = line.count("\t")
        print("tabsinthisline=",tabsinthisline)
        break
        
print("TESTING string 7 now indenting it to the left")
shift_nest_string_to_left(teststring7) #good 5 TABS DOWN TO 1
print("red alert testing shift string to left")




	
	
	
#exit()

#exit()
print("end of testing of doing indentation shifting to string")
print("oct 26th nearly done with this.. line 6127 ")
#exit()

print("this is where I am indenting the switch strings already in a list")
print("I need to indent them to work on them further to prepare them for the parser")

gold_list_results=[]
newstring=[]
newstring.append(0)
##=================================
##  manipulate_string(addstring) #this appends the changed switch strings to gold_list_results
##=================================
print('testing taking out 2 ')
def manipulate_string(addstring):
    print("======manipulate_string() called line 8524=======")
     #the objective is to reduce tabs so only 1 tab in front of first switch in string
    cutout=''
    print("let us ORIGINLAL INPUT STRING HERE look at the starting input string before modifying it")
    for line in addstring.splitlines():
        print(line)

    print("== red white and blue ==============")
    print("=======pinpointing bug on november 30th =============================")
    print("getting tab count in front of first switch here")
    for line in addstring.splitlines():
        if "switch" in line and "end" not in line:
        #this determines the number of TABS in this line
            tabsinthisline = line.count("\t")
            print("tabsinthislines=",tabsinthisline)
            print("the tabs in front of first switch are",tabsinthisline)
            #the objective is to have only 1 tab in front of first switch
            # which then propogates down the length of the entire string
            if int(tabsinthisline) > 1:    #example
                cutout = tabsinthisline -1
                print("tabsinthisline =",tabsinthisline);
                print("cutout =",cutout)
                break
            if tabsinthisline == 1: #which means do nothing we want just 1 tab first
                cutout = -1; #this is using -1 as a flag
                break
            if tabsinthisline == 0:
                break
            # do nothing   193241613
     #take out just 2 tabs
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    print("now doing ===== SECOND PHASE ======of manipulate_string")
    super=''
    lastchar=''
    for line in addstring.splitlines():
        #if "switch" in line and "end" not in line:
        tabsinthisline = line.count("\t")
        #it does all lines of the string taking out the first 2 tabs which are chars
        if cutout != 0  or cutout > 0:#this handles if cutout = 0 meaning None
            sliced = line[cutout:] #this can be a variable
            print("sliced sees",sliced)
            #phase A ============================
            
            print("================================")
            print("======phase A sliced=",sliced)
            ### bug fix ##===========================
            #reput in on dec 5th sunday 
            print('this fixes the bug that was putting junk after each line')
            print('adding extra : ) u #')
            print('see if it works ... again')
            ###############################
            ###### testing bug fix dec 5th sunday ######################
            #this tests if last character is #,),u,:
            #print("the last char is sliced[-1]",sliced[-1])
            #tail = sliced[-1]
            #looklist=[]
            #looklist=["#",")","u",":"]
            #if tail in looklist: 
            #   print("yes last char is either #,),u,:")
            #   sliced=sliced[:-1]
            #else:
            #  print("none of the garbage characters are the last char")
            #   pass
            ################################
            ################################    
            ##========================================
            
            
            #if len(sliced) >0:
            #    lastchar=sliced[-1]
            #    #print("lastchar =",lastchar)
            #   # print("TRUE weird last character",lastchar)
            #    if lastchar == ":" or  ")" or  "u" or   "#":
            #        sliced=sliced[:-1]  
            #========================== bug fix on nov 30th Tuesday hollister starbucks===============================    
            #    sliced=sliced[:-1]
            #else:
            #    print("last char must be 0")
               # print("length of sliced =",len(sliced))
            #print("after teh change the line looks like ",sliced)
            #print("====did it work or not=============")
            
            
            ################################################################
            ## this takes out the last char at end of the line
            #get last character
            #=============================
            #sliced=sliced[:-1]
           # if any of these are True  :),u,#
            #print("====  testing if last character : ) u # ==== ")
            #if lastchar == ":" or  ")" or  "u" or   "#":
             #   print("TRUE weird last character",lastchar)
            #    sliced=sliced[:-1]
            #else:
            #    print('current last char is',lastchar)
                
               
                
            #if sliced[-1] == ":" or  sliced[-1] == ")": or sliced[1] == "u": #
            #    sliced=sliced[:-1]
            #end if
            #===============
            
            #sliced=sliced[:-1] #this is new but when does this occur and why?
            #this is new nov 30th, tuesday hollister starbucks
            
        else: #this means its equal to 0
            #scenario zero tabs in front of first switch starting
            if tabsinthisline == 0:#this handles if there are zero tabs in front of switch line
                sliced = "\t" + line; # add one tab if zero tabs.
                #phase B ============================
                
                print("================================")
                #print("=====phase B sliced=",sliced)
            else:
                #phase C ===================
                sliced =  line; #maning this has at least 1 tab already
                
                print("================================")
                #print("=====phase C sliced=",sliced)
        super += sliced + "\n" # this does all lines in the string
        #=== super 1 ==================
        #print("SUPER 1 =",super)
        #scenario if it's already perfect at 1 tab length in front of switch
        if cutout == -1:  #this means tabs in this line determined to be 1
            super += line 
            #super 2  =====================
            
            print("================================")
            #print("SUPER 2 sliced=",super)
        #end if
    print("================ taking out 2 tabs quickly and dirtily")    
    print("this is the output SUPER lines to see the result")
    print("THIS IS THE RESULTING STRING below this line in manipulate_string function...")
    for line in super.splitlines():
        print(line)
    return super #this should do it now this is what is returned a string called super
    
    
    newstring[0]= super #shift_nest_string_to_left(string)
    #this appends the super string to gold_list_results list 
    gold_list_results.append(super)
    #the string sare in gold_list_results
print('testing cutting out first two tabs from front of string')
print("===TESTING CUTTING OUT FIRST TWO TABS FROM FRONT OF EACH STRING OF CODE==")
print("moving everythign to left side for formatting this sucker see if gold nears")


print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
print("=====testing in theory method chaining ======")
#output=[]
#output.append(0)
#myinput=[]
#myinput.append(0)
print(" chain methods test with 3 methods that hand off output as input to next method")
print('testing 3 methods in a row november 23rd santa cruz avenue menlo park ')
print("==================================")
print("first let us see the string in the starting representation") 
#for line in teststring6.splitlines():
#    print(line)
#print
#output[0]='' #to shift string identation to the left
print(" **  method 1  **  indent to left   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
print(" **  method 1  **   testing manipulate_string(string)")
#del myinput[:]
#myinput.append(teststring6)
#input[0] = teststring6
############===============
#manipulate_string(myinput[0]) #indent to left  what is the outpout put into 
############==========
#output[0]=newstring[0] 
#for line in output[0].splitlines():
#    print(line)
#print("........")
#razzle = output[0]
#myinput.append(razzle)
#3toosmart = razzle
#mystringname= toosmart #spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
print(" **   method 2  ** cut out sitch bodies  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
print(" **   method 2  **  modified2_cut_out_inner_switch_body_leaving_switch_word ===")
#right here it can't read the stringname
print("==========starting point======================")
print("================================")
#print("stringname=",mystringname)
#for line in mystringname.splitlines():
#    print(line)
    
#print("checking cat scales list [0] now===========")
#for line in cat_scales[0].splitlines():
#    print(line)
    
#mycat = never_defeated[0]
###################==============
#stringname=mycat;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
#modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)

#print(never_defeated[0])
#start=1,finish=1;
#modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
###################==========
print("please work now did this sucker work tuesday november 23?") 
print('result of taking out inner switches ') 
#output[0]=cat_scales[0]    #outoput 
#for line in output[0].splitlines():
#    print(line)
#print("........")
#del myinput[:]
#myinput.append(output[0]) #does this one work  
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")
print(" **  method 3  ** testing take_out_endswitch()")

#################==========
#take_out_endswitch(input[0])
#################===========
#outoput in holdon[0]
#output[0] = holdon[0]
#print("result of taking out bottom endswitch ")
#for line in output[0].splitlines():
#    print(line)

print("above this line is the totally modified string from 3 chained methods ")


###============= test nov 24th wednesday 2021 target parking lot

test_string4='''
	switch(exp){ #44
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################1
			switch(exp){ #51
				case 'fishy':
					print("do something")
					print("yep")
					fallthru:
				case 'where now':
					print("nice")
					break
				default:
					print("we very done") 
			endswitch 
			#############k
			break
		default
			print("we are done here")
	endswitch #46  
'''

#You can use double or single quotes:
#testing on my iphone. last night. 
testingthis='''
	switch(exp) #23:
		case 'tahoe':)
			print("do something"))
			print("yep"):
		case 'fallen leaf lake':)
			print("nice")#
		####################1
			nested_switch_31:(exp) #31:
			#############k
			break:
		default:)
			print("we are done here").
} 
'''

moregarbage='''
	switch(exp) #1:
		case 1 thru 3:)
			print("where's the dog house!"))
			print('first prize'))
			print('you block head Charlie Brown')u
			fallthru	
			:
		case 4 to 7:)
			print('kangaroo hop hop!')#
			#############1
			nested_switch_22:(exp) #22:
			exp = 32
			nested_switch_33:(exp) #33:
			##############)
			print('taught me how to write code')u
			fallthru	
			 
		 :
		case 8 to 10:)
			print('mocha blast'))
			print('== 31 flavors===')u
			fallthru	
		:
		default:)
			print('the end') 
} 
'''

trythisone='''
	switch(exp) #1:
		case 1 thru 3:)
			print("where's the dog house!"))
			print('first prize'))
			print('you block head Charlie Brown')u
			fallthru	
			:
		case 4 to 7:)
			print('kangaroo hop hop!')#
			#############1
			nested_switch_11:(exp) #11:
			exp = 32
			nested_switch_62:(exp) #62:
			##############)
			print('taught me how to write code')u
			fallthru	
			 
		 :
		case 8 to 10:)
			print('mocha blast'))
			print('== 31 flavors===')u
			fallthru	
		:
		default:)
			print('the end') 
} 
'''

##==============================
##  remove_garbage_on_right_margine(inputstring):    called after manipulate_string
##==============================
#removes garbage on right margine and takes out : in nested_switch if it exists
def remove_garbage_on_right_margine(inputstring): #this fixes garbage characters afterwords
	print('----------cherry on top called----------------------')
	cutout=''
	print("let us ORIGINAL INPUT STRING HERE look at the starting input string before modifying it")
	for line in inputstring.splitlines():
		print(line)
	return  ##  this stops the method cold 
	counter=0
	print('starting to enter cherry on top really serious need to get it working')
	adder='';last_char=''; result = False
	for line in inputstring.splitlines():
		print(line) #if "switch" in line and "end" not in line:
		#need test if last line is a number then don't chop it off
		
		print("length of line=",len(line))
		#if length of this line is more than zero
		if len(line) > 0:
			last_char = line[-1]; #returns a character or number or space whatever it is 
		#ourstring = "switch(exp){ #22"
		last_char_in_line_is_number = last_char.isdigit()
		#  checks if last char in line is a number
		#############################
		if last_char_in_line_is_number == True:
			print("last character is definitely a number")
			##########################################
			print("last_char a number is",last_char)
			#if anumber == True:
			print("SECOND SCENARIOthe last character is a NUMBER")
			adder += line + "\n"
			print("last_char=",last_char)
			continue
		
    #need to ahve it check for "))"
		################if line ends with junk ==========================
		if last_char == ":" or last_char == ")" or last_char == "u" or  last_char == "#": #maybe any character
			#need to check if last 2 are )) only cut off one, otherwise
			# if it's only ) and then don't cut it off
			
			print("FIRST SCENARIO :, ),u, #")
			adder += line[:-1] + "\n" #this deletes the last character from the line
			print("last_char=",last_char)
			
			
		########### if line ends with a space 	
		if last_char == "": #meaning it is an empty space
			print("THIRD SCENARIOlast char is a SPACE")
			adder += line + "\n"
			print("last_char=",last_char)
			
			
			######## this handles if the line ends with a number
			#elif last_char.isdigit():   
			#	print("SECOND SCENARIOthe last character is a NUMBER")
			#	adder += line + "\n"
			#	print("last_char=",last_char)
		print("counter=",counter)
		counter += 1
	###########################################################
	############################################################	
	#decided to get rid of : inside of nested_switch here
	#this fixes this bug  >>  nested_switch_11:(exp) #11:
	print("NOW remove dots inside of nested_switch line if they exist")
	
	verycool=''	
	
	
	for line in adder.splitlines():
		#check if nested switch in this switch string
		if "nested_switch" in adder:
			#print("TRUE nested_switch in line")
		
			if "nested_switch" in line and ":" in line:
				#print("nested switch is True")
				verycool += line.replace(":","") + "\n"
			else:
				verycool += line + "\n"
			
		else:
			verycool += line + "\n"
			#print("no nested_switch in this switch string")
			pass	
	print("FINAL OUTPUT FOR THIS STRING======>>>>>")
	for line in verycool.splitlines():
		print(line)    
	print('afterwards not working yet just trying to get last char of each line')	
	print('resulting fixed removed garbage looks like this.....')
	
	
		#it does all lines of the string taking out the first 2 tabs which are chars
		#if cutout != 0  or cutout > 0:#this handles if cutout = 0 meaning None
	newstring[0]=verycool #bug was right here.	
	inputstring=''
 ################################ 
	#print("THIS IS THE RESULTING STRING below this line in manipulate_string function...")
	#for line in super.splitlines():
	#	print(line)
	#newstring[0]= super 
	#print('the final output with cleaned up garbage should be here')
	#print("outpout of cherry on top ==== attempt 1 ")
	#for line in newstring[0].splitlines():
	#	print(line)
	
print("STARTING test 1")
print("take care of garbage on right margine and remove : in inner nested_switch")
#remove_garbage_on_right_margine(moregarbage)
#for line in newstring[0].splitlines():
#    print(line)
#exit()    
    
#print("next one")
#print("STARTING test 2")
#remove_garbage_on_right_margine(trythisone)
#for line in newstring[0].splitlines():
#    print(line)

print('what about this one')
print("STARTING test 3")
#remove_garbage_on_right_margine(test_string4)
#for line in newstring[0].splitlines():
#    print(line)
#print("STARTING DONed")
#exit()









print("Hello")



def method1(inputstring):
     return;
     concat =''
     print("==method1==")
     concat += inputstring
     concat += " fish"
     print(concat)
     return concat

def method2(output1):
     return;
     concat =''
     print("==method2==")
     concat += output1
     concat += " mice "
     print(concat)
     return concat

def method3(output2):
     return;
     concat =''
     print('==method3==')
     concat += output2
     concat += " \nrain fall heavy"
     return concat

print("above the rocket launch")


####===========================================================
def try_these_chain_methods(inputstring):
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("=====try_these_chain_methods=====")
    print("looping through inputstring to see the starting state")
    for line in inputstring.splitlines():
        print(line)
    ##==========    
    print("==trying these three methods and see if it works or not==")
    output1 = manipulate_string(inputstring) #shift string to left
    print("reached after first method called")
    print("mOnday morning Blues testing of manipulate_string method")
    #print(newstring[0])
    
    #takes out extraneous :, ),#,u on right side AND removes : inside of nested_switch word
    remove_garbage_on_right_margine(output1) #this should work now Takes out garbage on far right
    output1 = newstring[0] #extranious #: ) empty lines have : u
    for line in output1.splitlines():
        print(line)
        
    #return    #stoppinghere 
    ##=========
    start =1; finish=1;
    output2 = modified2_cut_out_inner_switch_body_leaving_switch_word(output1,start,finish,)
    print("reached after second method called")
    ##=========
    output3 = take_out_endswitch(output2)
    print("reached after third method called")
    print("this is the final output string from the three chain methods",output3)
    ##=========
    for line in output3.splitlines():
        print(line)
print("serious three raptor engine test launch")        
inputstring= teststring6        
#try_these_chain_methods(inputstring)
print("finishing calling test chain methods")
print(" end of today's test ")
#exit()    
#starting teststring6
#take the string to test it
#shift_nest_string_to_left(string)
#manipulate_string(item) 







	


	
##=====================================
## swap_endswitch_with_curlybrace() this uses the method take_out_endswitch()
##======================================
##=presumes that quail list already filled up with seperated strings
devious_list=[]
peachtree=[]
#so this function loops thru quail list and checks if endswitch in a string in quail
def swap_endswitch_with_curlybrace(): #using testlist_of_strings
    print("=== swap_endswitch_with_curlybrace() ===========")
    print("this requires that quail list must already be filled with switch strings")
    counter=0
    #assert len(quail) > 0 #it did say quail list 
    if len(gold_list_results) > 0: #meaning there is something in quail list
        #looping thru quail list
        for item in gold_list_results:  #notice that this works by looping thru quail list and changing strings with endswitch
            if "endswitch" in item:
                print("yes endswitch is in this string")
                #it happens here TAKE OUT ENDSWITCH(ITEM)
                take_out_endswitch(item) #calling take_out_endswitch saved to holdon[0]
                #print(holdon[0])
                print("its appended to devious_list here via holdon[0]")
                devious_list.append(holdon[0])#this line just might not be working correctly need to look at it further
               # testlist_of_strings[counter] = holdon[0] #this puts it back into testlist slot
                holdon[0]=''
                counter += 1
                continue
            else:
                print("nope no endswitches")
                counter += 1
                continue
    else:
        print("testlist_of_strings list is empty so can't do swap endswitch with curylbrace")
    print("let's see if this works or not does this thing actually work")
    print('strawberrie fields are forever')
    # see if it takes endswitch out and puts } in its place
#end function



#three test in a row here of method calls 



  
testlist_of_strings=[]
testlist_of_strings.append(teststring1)
testlist_of_strings.append(teststring2)
testlist_of_strings.append(teststring3)
testlist_of_strings.append(teststring4)
testlist_of_strings.append(teststring5)
testlist_of_strings.append(teststring6)
testlist_of_strings.append(teststring7)

print("===== testing this using a loop =====")
print("this left shifts and indents each switch string to prepare for going thru bypass205()")
counter=0  #this shifts (indents) the whole switch string to the left with 1 tab in front of switch
print("this prints out the switch strings after left Red Shift== to one tab")
cow_hide=[]
fuel=''
##==============================================
##  starting_what_switch_strings_look_like():
##==============================================
def starting_what_switch_strings_look_like():
    print("starting we have...")
    for item in testlist_of_strings:
        print(item)

##==============================================
##  left_shift_all_switch_strings():
##==============================================    
def left_shift_all_switch_strings(): #this goes thru testlist_of_strings
    print("now we will shift the switch to the left margine")
    counter=0
    for item in testlist_of_strings:
        print("counter =",counter)
        manipulate_string(item) #this calls manipulate_string(item) to shift the switch string to the left
        #adds change to axis put into newloop appended 
        counter += 1
#output is in gold_list_results list
print("   ")
print(" this is AFTER the switch strings have been seperated and put into a list")
print(" called testlist_of_strings  ")
print(" testing  ==left shift jazz== ")
starting_what_switch_strings_look_like()
left_shift_all_switch_strings()



print("DID IT WORK OR NOT the changes stick is it still === LEFT SHIFTED=====")

print('we are here now nov 23rd tuesday morning morgan hill.')




#for item in devious_list:
 #   print(item)
critical_list=[]
print('plum tree test') #hours spent getting this tow ork oct 17th, 2021 9;52pm
def goodtimes():
    print("good times()")
    print("looping thru gold list results list")
    for item in gold_list_results:
        print(item)
        del several_three_tab_switches_list[:] #delete it first to erase the chalkboard
        stringname=item
        get_second_switch_numbers_check_if_many(stringname) #output here
        print("several_three_tab_switches_list=",several_three_tab_switches_list)
        print(several_three_tab_switches_list)
        why= several_three_tab_switches_list
        print("why=",why)
        print(type(why)) #gets the type of var why is.
        results=list(map(int,why)) #changing the string numbers into ints then it works
        #this adds to this list the inner switch numbers for each switch string
        print('results=',results)
        #some will have none, some will have 1, and some will have more than 1
        critical_list.append(results)
        print('critical_list=',critical_list)
        #print(peachtree)
goodtimes()    
print("end of show")    
print("resulting three tab inner switches in each of the switch strings")


def cool():
    print('==========cool function==== is this working yet====')
    for item in critical_list:
        print(item)

cool()

   
    
    
    #holdthis[0] = galaxy.replace("endswitch","}")
#I need to replace the inner switches with methods now
####========== sunday october 17th, 2021 



#what is below here isn't working right for some odd reason

print("about to call swap_endswitch_with_curlybrace() ===")
print("this replaces each endswitch with } to prepare for bypass205()")
#this one is designed to go thru quail list
print("here we take out the endswitch in each string and replace it with }")
swap_endswitch_with_curlybrace() #have it work with gold_list input already left justified
print('about to loop thru devious_list to see if it swapped endswitch with } or not')
for item in devious_list:
        print(item) 
#print("now we will loop thru the testlist_of_strings to see the endswitch is gone now")
#for item in testlist_of_strings:
#    print("counter =",counter)
#    print(item)
#    counter += 1
    


print("TESTING string 1 now=======>>")
manipulate_string(teststring1)   
#exit()
'''
print("TESTING string 2 now========")
manipulate_string(teststring2)   
print("TESTING string 3 now========")
manipulate_string(teststring3)   
print("TESTING string 4 now=========")
manipulate_string(teststring4)   
print("TESTING string 5 now========")
manipulate_string(teststring5)   
print("TESTING string 6 now=========")
manipulate_string(teststring6)   
print("TESTING string 7 now=========")
manipulate_string(teststring7) 
#shift_nest_string_to_left(teststring6)  #3 tabs  DOWN TO 1
#this one is not working 
'''
print("test 2")
print("testing indenting correclty teststring1")
#shift_nest_string_to_left(teststring1) 

print("test 1")
print("testing indenting correclty teststring2")
#shift_nest_string_to_left(teststring2) 

#this doesn't work yet
#now to a loop 
#listtest=[]
#listtest=[teststring1,teststring2,teststring3,teststring4,teststring5,teststring6,teststring7]
#print("testing going thru all strings and indenting them ")
#counter =0
#print("====starting looping thru each teststring=====")
#for item in listtest:
#    shift_nest_string_to_left(item)
#    print("========")
#    print("counter=",counter)
#    counter += 1
    
      
# ==================================================================================
# what to work on today thursday, october 14th, 2021 ,,,,,,,,,
# so I would feed in just a param to look for "#" AND "switch" AND "31" and get tabdepth
# I need to try calling and looking for switch in line and # and the number 31
# and loop thru to endswitch at same tab depth.
# get tab depth on switch   tab_depth1 = line.count("\t")
# and then the first line with "endswitch" in line and this_tab_depth == tab_depth1
# =================== thursday coding ================================================

#so the formula is whatever never it starts from subtract that
#so if it starts at line number 11 at beginning of string with switch
#so if we do 31 down to 41 we subtract 11 from first number and second number
#so it's really 20 down to 31
#or I could have it start #31 in line and switch in line
#loop until same tab depth and "endswitch" in line


 #add item to dictionary
#pears['3'] = [4,7] #example
print(pears)
 #access dictionary
#x = pears("1")
 
 #remove item from dictionary
#thisdict.pop("model")
 
 
#now when I loop thru switch and endswithc lines
#have it fill the dictionary with the data



#######================================================================#########==========

#######================================================================#########==========
rose=[]
rose.append(0)
rose.append(0)

#######================================================================#########==========

#input1 = rose[0]
#input2 = rose[1]
#23,46

#start = rose[0]+1
#finish= rose[1]+1

#skipping_some_lines(x,start,finish)
#print(toosmart[0])


#always do one nest. Just change the switch start and stop sooo simple


## MAIN TRIGGER FOR TESTING THIS CODE OF EXTRACTING NESTED SWITCH STRINGS 
###################################################
## #this means I need to feed in the one switch location and one endswitch location
## that need to have been already figured out



##  copy_one_nested_switch_string(m82)   <<=======     this is the main trigger for the test july 18th 
##  I will need to add another paramter to determine which nestd switch is grabbed 
def extra(): # does nothing
	print("did it work??")
	
	print("#method  get_switch_and_endswitch_locations()")
	######### just commented out line below july 19th 1:10 pm
	
	#get_switch_and_endswitch_locations(m82) # presumes only one nested switch inside param would be passed here to to pass thru this is new  method call
	######## I will need to take out this method above out of this function
	######## this currenlty only takes in the first switch by design 
	#this builds a list of switch_location and endswitch_location all of them
	# but this function conpy one nested stirng ONLY USES the first switch and first endswitch
	###################################################################
	#this gets switch_location[0] and endswitch_location[0]
	print("copy one nested switch string ()")
	print("get start of nested switch and end of nested switch")
	print("#method get_one_nested_switch_start_and_finish()()")
	#get_one_nested_switch_start_and_finish() # method call 
	#this just copies the locations of switch and endswitch into 
	
	
	
nest_string=[]	
######################################################
##  def copy_one_nested_switch_string(m82,zebra,cow)
######################################################
#this fills nest_string list with copies of the switch body strings
#and takes out front two tabs from string
def copy_one_nested_switch_string(m82,zebra,cow): #so I would add a param to determine which nest to grab july 18th 
	print("==== copy_one_nested_switch_string() =====")
	print("===========.................==============")
	#print("let's look at the input")
	#print(m82)   #main string name
	print(zebra) #switch    location
	print(cow)   #endswitch location
	
	print("========COPY ONE NESTED SWITCH STRING()== called=====")
	#input_string[0]=samplestring
	counter=0		
	buildstring=''
	print("printing samplestring first")
	#print(m82)This ONLY GRABS the first position which is 0 for switch and endswitch
	#when I loop thru this in the peartree dictionary I will put the current pair into 
	#switch_location[0] and endswitch_location[0]
	######################################################
	print("WHAT ..... is in these two lists position 0 swith and endswitch")
	#print("it sees in y",y, "well how does it look")
	####################################
	print("passing the params for switch and endswion and endswitchlcoation")
	del switch_location[:] #these were passed as params that govern grabbing the right string
	switch_location.append(zebra)
	print(switch_location[0])
	del endswitch_location[:] 
	endswitch_location.append(cow)
	print(endswitch_location[0])
	#print("switch_location[0]",switch_location[0]) #10
	#print("endswitch_location[0]",endswitch_location[0]) #20
	#print("what it sees in switchlocation0 and endloaction0")
	print("===========================================")
	# LOOP thru string
	###=================
	fridge[0]='' #empty this sucker just in case oct 5th 2021
	#print("list_of_switch_range[1]",list_of_switch_range[1]) #10
	#print("list_of_switch_range[2]",list_of_switch_range[2]) #20
	for line in m82.splitlines(): #determine if "endswitch" is in line
		#this by default starts copying the string once line greater than 2
		#this says if counter between 10 and 20 including start number and finish number		
		#############################################
		#if "switch" in line and "endswitch" not in line: #this shows just switch
		#	print("switch in this line",counter)
		#if "endswitch" in line:
		#	print("endswitch in this line",counter)
		##############################################	
		#right here if counter is between min line number and max line number
		alpha = int(switch_location[0])
		beta  = int(endswitch_location[0])   
		#this loops thru string and copies lines to buildstring
		if counter >= alpha and counter <= beta: #if counter between(within) alpha and beta:
			buildstring += line + "\n" #I need to start at the 10th line
			counter += 1	
			continue
		else:
			counter += 1 #wasn't adding to counter
			continue #really
	print("the new creation concatted should be buildstring=")
	fridge[0]=buildstring  #here buildstring is stored in firdge[0]
	print("what is in the fridge[0] the nested switch copied")
	#print(fridge[0]) #the copied nested string is in here  fridge[0]
	#############################################
	#newstring='';cool_string = fridge[0]
	print("#method take_out_x_tabs_from_front_of_line()")
	#calls method take_out_x_tabs_from_front_of_line
	#it was cool_string which is now m82  was (2,cool_string)
	newstring=take_out_x_tabs_from_front_of_line(m82) #this is running #takes off 2 leading tabs
	fridge[0] = newstring
	
	#print("final outcome Tron")
	#print(fridge[0]) #this results in the nested switch string with  2 tabs taken off front of each line
	################################################
	# July 21st, 2021 4:16 pm Gilroy Starbucks
	#this copies the string just copied and put it into nest_string
	#its added to nest_string right here 
	#####################################################
	# the copied switch body string goes into fridge[0]
	# and then is added to nest_string list
	######################################################
	nest_string.append(fridge[0]) ##<<<===== right here the nested string is added to nest_string
	#this is filling nest_string with the contents of each nested string
	#then fridge[0] is added to the list nest_string
	print("nest_string length=", len(nest_string))
	#print("line 4315 nest_string here has this in it",nest_string)
	#print("trying to loop thru nest_string to figure this out")
	print("pumpkin pie")
	#for item in nest_string:
	#	print(item)
	#	print("==========")
	
	#need to delete teh first three tabs
	fridge[0] ='' #this empties fridge[0]
	print('trying to empty nest string here on line 4330 see what happens ')
	#del nest_string[:] 
	print("length of nest_string at this juncture is now",len(nest_string))
	#################################################
	print("copy a nested string and output it") #august 5th, 2021
	#print(nest_string)
	
print("====TESTING COPYING A NESTED STRING ======1 2 3 A  B C===....")	
print("====STAR TREK ENTERPRISE ===....")	
print("this is where I call the function to copy JUST ONE nested switch")
# july 18th I would need to add another paramter here like 2, for second nested switch 
#copy_one_nested_switch_string(samplestring) #reads sample string here 
#output into fridge[0]

#this should just call one nested string
# I will put the loop to go thru peartree dictionary
#and call copy_one_nested_switch_string(samplestring)
#and have it added to a list


# I will need to append it 


#this calls in order these methods
'''
pears =	{  #for pear tree in backyard (2 of them)
  "1": [10,20], # I can make these now 
  "2": [28,38],
}
'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========




smart_switch_numbers=[]
#the purpose of this is the switch ID number is it's initial line number
#NOTE: no spaces inbetween switch(exp){ otherwise replace doesn't work right 
#testing adding the comment and line number for switches

###=====================what I need to do =====================
# important sept 30th
# all I gotta do is make each nested switch like
# the main switch template and take out inner switch bodies
# then using the line number put in the generated method in it's place
# be sure that I add the line number as a comment I have that code
# and then make sure I get that switch line number to
# make the nested method to replace it
#####================================================================
#this one is all new and not tested september 30th musing
#testing adding the comment and line number for switches
#this is new not currently used or tested 

testcode='''
					switch(exp){ #53
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
'''
#I am testing with this string the inner swithc is at 3 tabs, first switch at one tab.
#this was teststring6 also added 0 to end
teststring60='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  this is what it will actually look like 
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''


#so I will know what switch body I am dealing with so I can juggle them and manage them					
#when I get a string that I have copied I just need the switch at the top
##====================================
##  get_switch_number()  it gets the switch number from FIRST LINE OF STRING then bails
##====================================
def get_switch_number(stringname): #this might be for when
	print("indian braves dancing for rain")
	# I create copies of the switch body strings
	print("get_switch_number() called it's getting the first inner swithc at 3 tabs length ")
	awesome=''
	y = ''
	counter =0  #say it's 3
	print("this is what the string we are manipulating looks like")
	for line in stringname.splitlines():
		print(line)
	print("================-------===")
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter =0
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tablength= line.count("\t")
		if "switch" in line and "end" not in line and tablength == 3:#and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			print("switch number is==>>>>>",y) 
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;

#skip 16 thu 38
print('this is testing october 12th to get the inner switch line number as a comment ')
weasel=get_switch_number(teststring60) #so this figures out what switch is in a list slot
print("number of this switch string(should be 66 ..",weasel) 
print("ending program here....")



	#testing here 
axis=get_second_switch_number(teststring4)
print("you can always try..")
print("should be 31 ... ",axis)
# get second switch numbers check if many
#experimental new october 14th, thursday, 8:06pm 


print("get second MASH switch number (the comment number after teh inner switch")
print("testing to see if it correctly retrieves the number 66 in the nested switch")
weasel=get_second_switch_number(teststring60)
print("should return 66")
print("weaseL=",weasel)		


weasel=get_second_switch_number(teststring3)
print("should return 23")
print("weaseL=",weasel)		

weasel=get_second_switch_number(teststring2)
print("should return 15")
print("weaseL=",weasel)		



			
#keep line #15 del til = #38
################# creation of loopstring list to hold string that will hold the nested switch string

loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=red_robin #   what it was previously ==samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
'''
#########################################
## loop thru pears dictionary
## and calls copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])
## to copy one nested switch at a time
    #it might just have to go thru once to fill pears
    # going thru a dictionary I need to designate which pair 
   
    ##########################################
    ## this loops thru the dictionary pears
    ##########################################
    print("about to loop thru pear values")
    #looping through dictionary pears 
      #say_something(cool) #this way the switch and endswitch locations are passed into the function
        ##########################################################
        ## this calls COPY ONE NESTED SWITCH STRING()
        ##########################################################
        print("about to start copy_one_nested_switch_string()")
'''






#https://www.youtube.com/watch?v=qtpxiNvGCp4
#########################################
##   copy_one_nested_switch_case_body()
#########################################
def copy_one_nested_switch_case_body(): #uses pears.values()
    print("======copy one nested switch case body () ....=====.")
    print("make the impossible into reality VIKING SHIP  fish 1 ")
    print("show what is in ")
    print(blueberries) #what is pears have in in it
    counter = 1
    #using blueberries dictionary and not pears 
    #just changed this oct 6th wednesday 10am 2021 morgan hill starbucks
    
    # pears is a dictionary with values of start switch and end switch
    ## LOOP ######## this loops thru pears dictionary
    for x in blueberries.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        #print(x)
        cool = x #(which is a pair thus only two values)
        print("cool=",cool)
        print(cool[0],cool[1]) #this is switch and endswitch line numbers 
        print("copy one nested switch string")
        #this uses the pair location start switch and end switch numbers
        #the string is in loopstring[0] <<----------------
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #great where does this copy of the string put into??
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        print("========================")
    #end loop
   
        

###=== this goes thru pears dictionary  and copies the nested switch strings
print("=== GODZILLA Time  ===")
#uses pears dictionary
'''
pears =	{  #for pear tree in backyard (2 of them)
  "1": [11,47], # I can make these now 
  "2": [49,73],
  "3": [15,38],
  "4": [53,64],
  "5": [23,33] #no comma after last data piece apparently
}
'''

print("here we go ... copy_one_nested_switch_case_body_blueberries():")
##====================================================
## copy_one_nested_switch_case_body_blueberries()
##================================================
#########################################
#this is using the string red_robin for testing purposes. 
  # pears is a dictionary with values of start switch and end switch
    #this goes thru the blueberries dictionary set of switch end switch pairs ===========
    ##===================================================================================
    ## LOOP ######## this loops thru pears dictionary
    #del nest_string[:] #empty this list
    #this is the blueberry dictionary 
    #it loops thru blueberries to copy a string
    #looping thru blueberries dictionary here 
    


    
loopstring[0]=red_robin #testing on oct 5th Tuesday
def copy_one_nested_switch_case_body_blueberries(): #uses pears.values()
    print("======copy_one_nested_switch_case_body_blueberries() ....=====.")
    print("make the impossible into reality VIKING SHIP  fish 1 ")
    print("show what is in ")
    print(blueberries) #what is pears have in in it
    print("I think that at this point nest_string whould be empty")
    print("len(nest_string=",len(nest_string))
    #nest_string=[] #this reinitializes it 
    counter = 1
  
    #right here nov 6 2021 saturday change this to the list of sublists (time to ditch the dictionary
    print("showing contents of blueberries dictionary values the strings here.")
    for x in blueberries.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        print(x)
        cool = x #(which is a pair thus only two values)
        print("cool=",cool)
        print(cool[0],cool[1]) #this is switch and endswitch line numbers 
        print("copy one nested switch string")
        #this uses the pair location start switch and end switch numbers
        #the string is in loopstring[0] <<----------------
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #this copied string is added to nest_string list
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        print("========================")
    #end loop
##=============oct 5th musing how to maket his puppy work 
#I need to have switch numbers by line number
# associated with it's pair start stop
#===================   
print("testing blueberries dictionary list to get the string bodies printed out")
####################
#print("NEST_STRING line TAHOE CABIN Bears ione 4651 what is in nest_string at this point")
#print(nest_string)
counter =1  #so the nest_string would have the switch body strings in it
for item in nest_string:  #going thru nest_string of inputs I think
    print("counter=",counter)
    print(item)
    print("end of this switch string body")
    counter += 1
    print("======....=====")
    
    
del nest_string[:] #new just now putting this hear
print("is this thing turned on right now?")
print("the autumn leaves are falling now.")
print("let us see what red_robin looks like")
for line in red_robin.splitlines():
    print(line)
print("done printing out red_robin input to compare it with")
print("  this is the autumn LEAVES  test ==")
print("======after having added line numbers as comments to each switch ===========")
add_comment_and_line_number_to_all_switches(red_robin)
print("=======now do the next one=======")
print("=======now do the next one=======")
print("=======now do the next one=======")
add_comment_and_line_number_to_all_switches(autumnleaf) ##testing this right here oh yea

#put it into a list which holds the new string with switch lines added as comments
#here I add line numbers to switches
#inputstring[0] #input string will be in here
copy_one_nested_switch_case_body_blueberries() #which is uses red_robin
print("finishing blueberries")

print("let see this puppy work ..... great america babes ignored me ...")
#copy_one_nested_switch_case_body() # this calls the loop

#print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)




#this is the resulting output of copying the string embedded in the main switch

holdthis=[]
holdthis.append(0) #creates the space to store it


teststring_brace='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  this is what it will actually look like 
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''

#this swaps endswitch with }
# I need to count the "}" in the string, there should only be one, actually none
# if there is one it needs to be in the right place.
# I will have to loop thru the list to look if there is a brace in it already.
######################################
## take_out_endswitch(stringname)  #replaces endswitch with }
######################################
list_of_line_numbers_of_endswitches=[]
holdthis=[]
holdthis.append(0)
#the issue is that I need it to only do the bottom one 
def take_out_endswitch(stringname):
	print("==========take_out_endswitch()and put brace in called=======")
	x='';x=stringname.count("endswitch") #should be 1
	print(x)
	counter = 0
	for line in stringname.splitlines():
		if "endswitch" in line:
			list_of_line_numbers_of_endswitches.append(counter)
			counter += 1
			continue
		else:
			counter +=1
		continue
	print("list of line number of endswitches=",list_of_line_numbers_of_endswitches)
	coffee =list_of_line_numbers_of_endswitches[-1] #last one
	print("the last endswitch =",coffee)
	print(stringname) #this takes out endswitch and replaces it with }
	stringname=stringname.replace("endswitch","}")
	for line in stringname.splitlines():
		print(line)
	holdthis[0] = stringname#now galaxy gets what is in holdthis[0]
	print(holdthis[0])#return stringname #and this is returned
	
print("testing take out endswitch from string and replace it with a } ")
take_out_endswitch(teststring_brace)
#outpout to holdthis[0]
#for line in holdthis[0].splitlines():#
#	print(line)
	



###===================================================
##   show_list_of_nested_strings_separated()
###===================================================
## july 21st 2021 349pm gilroy starbucks
#oct 5th this is a list of thes copied switch ends witch stings in nest_string
###=== this shows the nest_string list of nested switches
#this just loops thru nest_string which has the seperated nested strings
def show_list_of_nested_strings_separated():
    print("======show list of nested strings separated=====")
    print(" == StayPuff Marshmellow Man ==")
    counter=1
    for item in nest_string: #this has the nest strings in it ALREADY nov 6, 2021
        print("counter=",counter)
        print(item)
        counter += 1
    print('end of first simple test ')   
    #===========================    
    counter =0
    print("loops thru nest_string that we filled up in copy_one_nested_switch_string(m82,zebra,cow)")
    #this requires nest_string which is looped thru
    print("length of nest_string=",len(nest_string))
    # loop thru nest_string list     to take out endswitch
    #for item in nest_string: #nest_string must have refined main switch with nest methods numbered already
    #    if "endswitch" in item: #swap endswitch with '}'
    #        print("== endswitch detected ==") #should be 2 of them
    #        print(counter) #takes out endswitch from this current string here
    #        holdthis[0]=take_out_endswitch(nest_string[counter])#takes out endswitch from each string
    #        nest_string[counter] = holdthis[0] #voodoo magic
    #        counter += 1
    #    else:
    #        print("oh good") #absolutely nothing happens here
    #        counter += 1
                
    print("see if it fixed it here")
    print("this is showing what's in nest_string list")
    #this loops thru nest_string to show after the changes were made
    print('this should be it right here the seperated nest strings')
    print("remember that the main switch string is totally different ")
    print(" this is the CRUCAL TEST OUTCOME RIGHT HERE TO SEE IF IT WORKED")
    print("what this does is print out the lists indiviudally after separating them")
    print("printing out the nest_string list right here play baseball Yankees")
    print("copied strings one by one")
    print("YANKEES need to show each copied switch body string")
    print("wow that worked")#da = blueberries.get("2")
    #print("getting data in blueberries")
    #print(da)
    mycounter =1
    nest_string_size= len(nest_string)
    print("length of blueberries =",len(blueberries))
    ###############
    #this makes sure that the nest_string is equal in size to blueberries
    # to counter a bug of overflow junk that I will figure out later
    # oct 5, 2021
    print("blueberries",blueberries)
    print("")
    #this deletes excess data that is appended to nest_string inexplicably
    #this simple fix was solved on oct 5th tuesday at 11:30pm 2021=======
    #temporary getting excess from nest_string
    #so 
    while len(nest_string) > len(blueberries):
        del nest_string[-1] #last element in list is deleted
    print("all done")
    print("length of nest_string=", len(nest_string))
    print("yes finally works NASA is born")
    #get length of blueberries
    #then reduce size of nest_string to that number (figure it out later) weird bug
    print("nest_string size = ",len(nest_string))
    for item in nest_string:  #nest_string
            da = blueberries.get(str(mycounter))#gets string at this position
            print("getting data in blueberries",da)
            print("counter=",mycounter)
            print(item)
            mycounter += 1
            
            print("==========-----------seperated nest strings -----------------")
    print("==========")
    #now delete extra slots in nest_string
    
    
print("===============================================================")
print("middle ground filler here to separate the change just made. fish 2 ")
print("===============================================================")
show_list_of_nested_strings_separated()
#now replace teh third string(the main string)
# this is to simulate cutting out the inner switches
## july 22nd, 2021 




####===========================================================###
####===========================================================###
####===========================================================###
print("july 22nd 2021 additions...====")
###============== this is working correctly now ==========
## more_testing()
##========================================================================

#sprint("checking number of nested switches at three tabs")
#stringname=testingstring1
#get_second_switch_numbers_check_if_many(stringname)


######################
##  more_testing()
######################
def more_testing():
    print("=== more_testing() == charisma ===method testing ")
    #this is adding samplestring with main to nest_string[2] to see what it will look like when working
    print("let's see what is already in nest_string ===> SpaceX pretest ")
    print("to see what is in nest_string")
    for item in nest_string:
        print(item)
    print("so slow 3 which is nest_string[2] has the main string in it")
    #let'see how it looks"
    print("==== after simple test of contents of nest_string")
    print("========")
    print("here we replace it with what will be after I modify it. this is dummy data testing")
    print("finished main string with nested methods added put into nest_string[2]")
    nest_string[2] = samplestring_main # the third one - putting in a different string premade
    #this is what is different right here in the line above
    
    #testing what the stages need to look like
    #to test what it should look like but doesn't yet
    print(" now we will try it again and see how it looks ")
    print(" after changing main string boo boo ")
    #loop thru nest_string
    for item in nest_string:
        print(item)
        print("===========///======oct 5 tuesday 2021 testing  ========")
        
        
###==================================== oct 5 thinking how to do this. 
#for each switch number I need to know what ranges of it's inner switches are
#I need the range of the inner switch numbers start and stop
#so inner switch ranges for switches by switch line number

#more_testing()

####===========================================================###
####===========================================================###
####===========================================================###


### this works this takes the copied nested switch
### and sets the proper indentation for it
#so it takes out 2 really but we have to say 3
## july 17th 10:12am 2021 starbucks

#the eye opening= make a list of the methods sequence
#tuesday, August 10th, 2021 ====,,,,,,,,,,,==========




loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
copy_one_nested_switch_case_body() # this calls the loop

print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)

show_list_of_nested_strings_separated()
more_testing()


###==========================================================

#def tab_swap(x,y):
#    replace(x,y)

########==============
#wilderness=
#def set_front_tabs(x):
#    wildness=''
#    for line in nest_string.splitlines():
#        wildness += line.tab_swap(3,1) #strips one right
#        wildness += "\n"
#    print("after minor surgery see if this works")
 #   print(wildness)






# copy line by line stripping all tabs
# and then based on if starts wwith swtich 1 tab
# if case 2 tabs
# if not switch and not case three tabs
# if endswitch one tab
# if default two tabs


#unless I make a new string _so I want to remove teh first 2 tabs only
alpha_string=''
str1=''
#for line in nest_string.splitlines(): 
#    #put line into list, del first three tabs then conver to string
#   aline = line.split() 
#    print(aline) 
#    str1 += str1.join(aline) + "\n"
#    #print(str1)
#    
#print("string now is...")
#for item in str1:
#    print(item)


 



#########################################==============
## === skipping_some_lines() ========   July 5th, 2021 ===============
#########################################
#this works for one nested switch right now
#this goes thru a nested switch and takes out the nested single switch.

### solution found for dealing with deeply nested switches
#I think that I can use this if I take out the innermost switch
## first and then it should work  
# so the plan of attack is to change(yes change) the inner most
# depth switch first
#and work back to the next level till I am at the first level of depth.


#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========

skip_range=[]
#skip_range.append(0);   
#skip_range.append(0) 
#july 5th, 2021
#so I still need to get the start and finish lines  switch and endswitch for input 
del ibm[:] #empties it
#print(ibm[0])
ibm.append(samplestring) #so in  ibm[0] this is putting samplestring into ibm[0]
print(ibm[0])
#===================print testing on july 24th saturday  2021 at 9:36am =================
print("at this point we have this in ibm[0] after taking out the first nested switch")
#del skip_range[:]
print("LOOP TEST THRU RANGE LIST Goofy dog")
range_list=[]
skip_range.append(0) #slot [0]
skip_range.append(0) #slot[1]


#string,start,finish
#first it will just detect one nested switch , soon it will detect many

#this loops thru a string and makes a copy of the string
# but skips over a range example lines 10 thru 20
toosmart=[]
toosmart.append(0)
flag_test=[]
flag_test.append(False) #flag_test[0] set to False right here 
baton=[] #this is used to hold the concatted string that is changed on each pass 
baton.append(0)
baton[0]= "nada" #to start with to test this monstrocity


rose=[]
rose.append(9)  #testing purposes 
rose.append(19)
test_code_now='''
					switch(exp){ 
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){   #9 
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									break
								default:
									print("we are done here")
							endswitch  #19
							#############
							break
						default:
							print("we are done here")
					endswitch 
'''








#this is testing with dummy data above in test_code_now
#taking out the inner switch body
print("halloween is coming snoopy and woodstock test")

print(test_code_now)
#the inner switch is at 9 (which we keep) so we start from +1 meaning 10
#and the endswitch is at 19 but we need to nuke that too so it's endswitch + 1

#the number system starts from 1 for the switch numbering
#because it starts counting from 0 and not 1 we need to subtract 1 from it
#so it was originally 10, 19

#if switch is #9 and endswitch is 19
#Add 1 to each number start and finish
print("===========rose test==== testing taking out inner switch body ===")
#the pair would go here 
input1 = rose[0]
input2 = rose[1]
print(input1)
print(input2)
print("take out 10 thru 20")
x = test_code_now
start = rose[0]+1 #10 #TO PRESERVE INNER SWITCH TO REMAIN THERE
finish= rose[1]+1 #20 #TO GO ONE BEYOND ENDSWITCH WORD
skipping_some_lines(x,start,finish)
print(toosmart[0])
print("=====end end end of show end of this dumb test==testing rose flowers ===")
# october 1st this will have to be a prescan first pass to get the locations 
# this will look for an inner switch after first line and get it's line number
# and find it's 'endswitch' or '}'
# and put the switch line number and endswitch line number into a pair
# and then append it and keep going and that way it figures out the location on it's own
coffee_switches=[]
end_coffee_switches=[]

combinedlist=[]
switchtabs=[]
endswitchtabs=[]

#this is not working right 
### mr coffee smart skipping lines 
## mr_coffee_smart_find_innerswitches bodies and skip them except for inner switch word


##======================================================
##  mr_coffee_smart_skipping_lines(inputstring):
##======================================================
def mr_coffee_smart_skipping_lines(inputstring):
	print("======= mr coffee smart skipping lines ..this =======")
	print(" makes pairs to find locations of switches and endswitches.")
	print(inputstring)
	counter =0
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			tabdepth= line.count("\t")
			coffee_switches.append(counter)
			switchtabs.append(tabdepth)
			
			counter += 1
		else:
			
			counter += 1
	del coffee_switches[0] #deletes the first switch which is at the top 
	###=================================
	count =0
	#this looks for endswitch locations
	for line in inputstring.splitlines():
		if "endswitch" in line or "}"  in line:
			tabdepth= line.count("\t")
			end_coffee_switches.append(counter)
			endswitchtabs.append(tabdepth)
			counter += 1
		else:
			counter += 1
	#=====================================
	counter =0
	for item in coffee_switches:
		combinedlist.append("[" + str(coffee_switches[counter]) + "," + str(end_coffee_switches[counter]) + "]")
		counter += 1

	print("zzzz the result list =",combinedlist)
	print("switch tabs=",switchtabs)
	print("endswitchtabs =",endswitchtabs)
	

print("testing this using string red_robin to see if it works")
print("this is only returning the range list of the switch endswitch pairs")	
print("GO GO GO what that dog go")
#mr_coffee_smart_skipping_lines(red_robin2)
## it's chopping off this from the bottom
'''
fallthru
		
		default:
			print('the end')
}
'''
print("TESTING SKIPPING LINES 16 THRU 38 IN RED ROBIN")
print("testing skipping nested switch in red robin")
print("today is thursday sept 30th...")
print("testing...... sept 30 skipping 16 thru 38")

#So loop thru string and 
#get line number with # and 15 put into start
#and get line number with
 # and #38 and put into finish
print("watching videos of starship. video time...")
print('length of nest_string',len(nest_string))
print("nest_string[1]) see if it works..") 
print(nest_string[0])
print("===============")
print(nest_string[1])
print("===============")
print(nest_string[2])
print("===============")
print(nest_string[3])
print("===============")
print(nest_string[4])
print("===============")
#print(nest_string[5])
#print("===============")

print("bottom after examining nest_string jazz")
start = 15
finish = 38
skipping_some_lines(red_robin,start,finish)
#see if the string is in ibm[0]
print('go for it 1')
#this is the lower section of the main switch now
print("and now we start phase 2 -====")
start  = 53-23 #subtract number after first cutting out skipping
finish = 65-23

skipping_some_lines(ibm[0],start,finish)
print("======= I have all of the code I need to make this miracle happen")
print("=====practicing cutting out inner switch guts leaving inner switch word==")
#
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
print('trying blueberries and nest_string')
#now the string we have is missing the numbers above it 
print(nest_string[2])
start  = 10 #subtract number after first cutting out skipping
finish = 19
skipping_some_lines(nest_string[2],start,finish)

print(toosmart[0])
#this changes the contents of nest_string[2] #see if this puppy works
nest_string[2] = toosmart[0]
print("what does this string look like right now this instant")
print(nest_string[2])


#53 -65
print('go for it 2')
##########################################################################################
print("TESTING skipping_some_lines(ibm[0],skip_range[0],skip_range[1]")
print("10 thru 20 but keeping the first line on 10 which is switch")
print("then 28 thru 38 keeping first line on 28 which is switch")
print("well, how did it go ")
print(" skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip ")
print("=====")
print("==========")
print("================")
print("======================")

#this would be done separately and is filling the range_list with the switch to endswitch params
#this will be a separate method for range input for the switch endswitches
#here the sublists of the param of each nested switch are added to range_list
#this is hard coded here filling the nested switch numbers 


#range_list=[[10,20],28,38]]  #that's right I do this backwards from bottom up!!!

'''
this goes thru the main switch string and makes a copy
of the main string in stages copying the whole thing
except for the range for each nested switch.
'''
## this means delete nested switches bodies except leave inner switch word only
##===================================================
#  REDUCE MAIN NESTED SWITCHES TO JUST SWITCH WORD
# debugged on august 5th 2021 gilroy starbucks
##===================================================
## this makes teh final main switch with the inner switch bodies stripped out
## just leaving the switch word where the nested switch was.
#range_list.append([10,20]) #these are added in order and then reversed
 # so that the nested switches are erased bottom up
addthis=[]
addthis.append([10,20])
addthis.append([28,38])
##========================
## add_to_range_list()
##========================
def add_to_range_list(): #uses addthis list 
    print("add_to_range_list() this is necessary to work")
    for item in addthis:
        range_list.append(item) #adding to range list
        
    print("length of range list =",len(range_list))
 
 
 
 #i will need to add data to range list still 
##======================
##  feed_range_list()
##======================
def feed_range_list():
    print("=========feed_range_list() called=====>>>")
    print("=========feed_range_list() called=====>>>")
    range_list.append([11,24]) 
    range_list.append([26,38])
    print('range_list=',range_list)
    #the list has to be REVERSED to do the changes bottom up so the line numbers work correctly
    range_list.reverse()#reverses it NOTICE WE REVERS THE LIST TO CHANGE IT BOTTOM UP
    #this is so the bottom is done first 
    print("length of range list =",len(range_list))


    
#Yes I am reversing the range_list to do the changes bottom up so they don't lose their place
print('printing the range_list')
print(range_list) #should be [28,38],[10,20] to do from the bottom up

#this takes out the inner switches except for the switch word
#so what this means is it removes the body of the nested switch but leaves just switch word.
### this uses range_list!!!!!!!!!!!!!!!!!
#between 11 and 47
#if first switch detected keep going so use switch counter
#it needs to only include the switch word of tab depth 3 switches
#before doing any changes it looks like this 
REAL_STRING='''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			####################
			switch(exp){ # 15  #second level deep  (( 5 tabs ))depth 3 detector       Level 2    
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################==== this one should be deleted 
			switch(exp){ #23  #third level deep  (( 7 tabs ))   Level 3    =====
				case 'tahoe':=========
			print("do something")=======
			print("yep")
			fallthru
				case 'fallen leaf lake':
			print("nice")
			break
				default:
			print("we are done here")
			endswitch #33
			#############
			break
		default:
			print("we are done here")
			endswitch #38==========
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47
			exp = 3  #note that this switch is stacked below the bottom stack at 3 tabs
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
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
			endswitch #73
'''
'''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			####################
			switch(exp){ # 15  #second level deep          Level 2    
				case 'tahoe':
					print("do something")
					print("yep")
					fallthru
				case 'fallen leaf lake':
					print("nice")
					break
				default:
					print("we are done here")
			} #38
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #47
'''
	
#after changes it should look like this after getting rid of inner switch body one indentation

#this is what the end result should be
endresultshouldbe='''
	switch(exp){  #11  first level deep                   Level 1
		case 'blable':
			print("do something")
			switch(exp){ # 15  #second level deep          Level 2    
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #47
'''
	

#I think that I need to go thru tab length3 first 
#then go thru tab length 5 
#then go thru tab length 7
#this is the input for the reduce_main_nested_switches_to_just_switch_word(

oldschool='''
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					#################### del after line with '#' and  '15' in it till 38 in it
					switch(exp){ #15
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			exp = 3  
			switch(exp){ #26
				case 'burger':
					print("do something")
					####################
					switch(exp){ #30
					print("gosh")
					fallthru
				case 'porsche':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
} #51
'''
#the output should be
'''
	switch(exp){
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #====
			exp = 3  
			switch(exp){ #====
			##############
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


starbucks_code_main_test ='''
	switch(exp) { #main 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					break
				case 'please work':
					print('nice')
					fallthru
			endswitch	 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	


#The change that I need to make here is to cut out switches greater than 3 tabs  tabdepth > 3
##======================================================
##   reduce_main_nested_switches_to_just_switch_word():  #I think that this does all switches no matter their depth
##=======================================================
def reduce_main_nested_switches_to_just_switch_word(astring): #11 - 23 and 25-37
    print("starting this method to see what is in the string")
    #for line in astring.splitlines():
    #    print(line)
    print("===reduce_main_nested_switches_to_just_switch_word()== Tron approaches")
    print("C3Po")
    print("=====reduce_main_nested_switches_to_just_switch_word()====0000000000000==>>")
    print("=====reduce_main_nested_switches_to_just_switch_word()======>>")
    print("=====reduce_main_nested_switches_to_just_switch_word()======>>")
    print("what is in astring the input param")
    print(astring)
    print("end of the input string to see what is going into the function")
    print("reduce main nested switches to just switch word()")
    
    #feeding range list()
    #add_to_range_list() #this is new to put switch and endswitch lines into range_list
    feed_range_list() #added on wednesday, September 15th, 2021
    flag_test[0]== False #this flag is new this is the default setting for this flag
    print("flag_test[0]=",flag_test[0])
    #when flag_test[0] = True that means it's doing 2nd and subsequent loops (changes) and use baton[0] for concatting string
    print("==reduce_main_nested_switches_to_just_switch_word(astring)==")
    print("= R2D2 ==## $$ ## == reduce main nested switches to just switch word()==========")
    print("this cuts out the nested switches bodies leaving just the word switch")
    print("starting ibm[0] with samplestring")
    print("what we are starting with for input in ibm[0]")
    #print(ibm[0])  #the key is the range_list
    print('range_list=',range_list)  ### this is the dependency the range_list necessary for this to work
    #loop thru range_list
    print("we loop thru the range_list here")
    print("let's see what RADAR is in the range_list",range_list) #see if it's reversed or not
    #loops thru range_list with pairs of switch end and endswitch
    print("length of range_list of pairs=",len(range_list))
    print("range_list=",range_list)
    counter=0
    # loop thru range_list
    print("before starting let's look into the range_list",range_list)
    print("============")
    print("perhaps I need to go thru the 7th tab first, then 5th tab, then 3rd tab")
    print("thinking outloud how to do this.")
    print("range_list=",range_list) #just added this sept 30 2021 testing cafe borrone
    
    for item in range_list: ##range_list=[[10,20],28,38]] ==========================
        print("**",item, item[0],item[1])
        print("inside of loop thru range_list :: COUNTER HERE=",counter)
        skip_range[0]= item[0]; 
        skip_range[1]= item[1]
        #item[0]='',item[1]=''
       # print(item[0],item[1])
        print("skip_range=",skip_range)
        #this builds a new string by skipping the nested switch sections
        #but leaves the inner switch (switch(x) word intact
        # skipping_some_lines() called here 
        # ibm[0] has the samplestring in it from above
        toosmart[0]=astring #this might work
        #this is called before skipping some lines
        #the problem is that on the secondpass it's not taking in the changed toosmart[0]
        #====================================
        #SKIPPING SOME LINES()===============
        #====================================
        #this is governed by flag_test[0] which is set to default False above the loop
        skipping_some_lines(astring,skip_range[0],skip_range[1]) #this makes a new string skipping guts of inner switch
        counter += 1
        
        #skip_range[0]='';skip_range[1] ='' #just added this to see if it helps
        #del skip_range[:] #this clear it out afterwords to wipe the slate clean
    print("this is the final output of the transformation halloween approaches")
    print("output of = R2D2 == taking inner nested switches body out and putting just keeping swithc word")
    print("the star destroyer was moving fast")
    print("should be only two nested switches and only switch word remaining NOT 3")
    print("end of this picture show")
    #print(ibm[0]) #this prints out the result 
    print("=====================")
##======================================================

#here we go  
print("the goofy dog test")  
print('we start with this string')

#print(ibm[0])
print("OLYMPICS BLAZING... gold medal time")
print("=====calling reduce main nested switches to just switch word(========)")
print("HERE NOW...this should be the sample string with the nested switches")
print(" cut out leaving just switch word")
print("we are ==== STARTING ==== with this dam string legal eagle")
#bypass here on thursday sept 30 testing at cafe borrone
#print("September 30th testing at cafe borrone")
#ibm[0] = red_robin
print(ibm[0])
inputnowstring= ibm[0]
print("starting input before doing changes")
print(inputnowstring)
print("about to reduce main nested swithces to just switch word which work previously without incident")
print("line numbe 4162")
print(" FIRE BREATHING DRAGON NOW ")
#flag_test[0]== False #see if this works 
# I am right here today  LOOK RIGHT HERE OCTOBER 1ST 2021 
## this is the key method here ====

reduce_main_nested_switches_to_just_switch_word(oldschool) # I didn't notice this way down here
print("red alert test 2 reduce main nestd swith to switch word test 2 ...")


print("good times saturday night live test ")
del range_list[:]
reduce_main_nested_switches_to_just_switch_word(starbucks_code_main_test)
print("look above frosty snowman here")
print("output from taking out nested switches in string inputnowstring")
print("output of removing both nested switches")
print("RIGHT HERE ====== OCTOBEr 1st what does this look like below this line")
print(ibm[0])
print("does it loop thru two times for that is how many times it should")
print("==============")
#exit()



print("this is what the main switch looks like after having taken out the inner switch bodies")
print("which means that we should only have the inner switch words remaining and nothing else")
print('super super major major critical test 4129 line number ')
print("this shoudl be the main switch with only remaining switch(exp){ and no inner switch bodies")
print("here we should have the two nested switches remaining with no bodies")
print("mocha at starbucks")
#print(ibm[0])
# print this skips the nested switch body and creates a different version of the main switch
# and takes out the nested switches but leaves the switch word
print('after the olympics end...')
print("stopping it here because it should have worked...")
print("remember that I am using and EXIT() here to stop the code running past what I am concentrating on")

#exit()  






#print(ibm[0])
print(" starting anew here doing it the old way")
ibm.append(samplestring) #in ibm[0]
print(ibm[0])
print("that's all lemon tree software ==")
print("about to exit the program after seeing the nested switches taken out of main string")
#exit()
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/ ghostly  /=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("this is the SECOND ATTEMPT")
#skip_range.append(0)
#skip_range.append(0)
print("does this work yet") #these are farther down  so I needto do them first 
skip_range[0] =11
skip_range[1] =24
print("=============")
print("skip_range=",skip_range)
print("=============")
print("====::::::::: after changing bottom nested switch to just switch word ::::::===")
print("====::::::::: after changing bottom nested switch to just switch word ::::::===")
print("what string is in ibm[0]=",ibm[0])
ibm[0]=oldschool
for line in ibm[0].splitlines():
    print(line)
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 28,38 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print("now swap out the top inner switch hopefully")
print("ibm[0]=",ibm[0])
skip_range[0] =10
skip_range[1] =20
print("=============")
print("skip_range=",skip_range)
print("=============")

skipping_some_lines(ibm[0],skip_range[0],skip_range[1])

#exit()

'''
skip_range[0] =10
skip_range[1] =20
print("=============")
print("skip_range=",skip_range)
print("=============")
skipping_some_lines(ibm[0],skip_range[0],skip_range[1]) 
'''

#print(ibm[0])
#fuse=[]
#fuse.append(0)

#del skip_range[:]

#skip_range.append(10)
#skip_range.append(20)

#I guess I can put the ranges into a list and then reverse it and 
#loop thru it.
print('at this juncture what is in ibm[0]')
print(ibm[0])
print("starting out we have this before stripping out the nested switches")
#ibm[0] = fuse[0] #to preserve changes made 
print("input values on 2nd pass =")
skip_range[0] =10
skip_range[1] =20
print(ibm[0])
print(skip_range[0])
print(skip_range[1])
print("========")
print("skip_range=",skip_range)
print("=========")

print('==== make it dam happen == ')
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 10,20 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print(ibm[0])
print(" where is it now lemonade stand ???")
del skip_range[:] #this has to be cleared out. 
#skip range needs to be cleared out for the next nest parameters here
##===============================
print("==== the end===both nested switches should only have the switch word reminaing ===")



print("===end of copying a string and skipping lines 10 thru 20===")   
print("in ibm[0] we have",ibm[0])
print("===== this is after running skipping_some_lines(smaplestring,10,20)")
print("===========")

smart_number=[]
smart_number.append('starter')
smart_number.append(0)
smart_number.append(0)
smart_number[1] = '1'
smart_number[2] = '2'
#switch is on line 10 need to change it this is looking for the switch

#this is changing ALL OCCURENCES of switch at the 
#same time just just the one I want it to change.
# I need to localize is it to one line number.

#have it change one and then break starting on the line above


#The problem I have is if I replace each switch with the nested numbers
#then the other code won't work so perhaps I need to add a comment
#the issue is making the main strings which should only have the first level inner switches
#which is governed by tab depth of 5 representing the second level
# since tab level 3 is the first main switch.
# I could do number 1 thru n for each level initally and then change them
# or I came up with the number top down 1 thru n but level list solves the problem 
#That was my genius

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#in terms of faster programming it's about communication and control
# the lollipop is the what level but above that are higher abstraction levels
# where yet more speed can be achieved and sustained
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========
#I think I will do the one nest level for now and add the other nest levels afterwords
#decision made august 22nd, 2021 9:08 am

# I have the main module which has nested methods
# I can use this for making nested switches with nested switch methods too
# but right now I want to get the nested feature working before implimenting it
#######3==================================
#Actually I can do the main and the nested that have inner switch words not changed yet
#And then apply the conversion to numbered switches
##=====================
''' from above just pasted it here to keep track of its contents
blueberries =	{  #for pear tree in backyard (2 of them)
  "1": [1,86], # I can make these now 
  "2": [11,47],
  "3": [15,38],
  "4": [23,33],
  "5": [49,73],
  "6": [53,64]
 #no comma after last data piece apparently
}
'''

danumber=''

#testing this here to make sure that it's right 
ibm[0] = '' #this should delete it
print("ibm length=",len(ibm))
stringname =teststring60
print('starting stage of string to manipulate')
for line in teststring60.splitlines():
    print(line)
danumber= 66

print("star wars begins now.")
##============================================
# swap_switch_for_nest_method_new(danumber)
#// inner switch(just the words) is swapped for nested method number")
#=============================================
#for this to work correctly I need to ahve already taken out the inner switch bodies that I copied
print("about to do OPTIMUS PRIME === GO BABY GO ===")
def swap_switch_for_nest_method_new(stringname,danumber): # I will add more values later perhaps 3 or 4 for coordinates
	print("#### ========= swap switch for nest method new  ========####")
	print(" =======OPTIMUS Prime======")
	global abovenestedswitch
	#stringname=ibm[0]
	#stringname=ibm[0] #loading from ibm[0] good
	print("called swap_switch_for_nest_method(n)")
	print("it is using this number in use_number[0]",use_number[0])
	acounter=0
	for line in stringname.splitlines(): #determine if "endswitch" is in line
		tabdepth = line.count("\t")
		print("the current tab depth in THIS line is",tabdepth)
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20 check to make sure that switch and the comment line number in this line
		#this way it can ONLY make changes to switches at tab depth 3
		if tabdepth == 3: #this way it can ONLY access changing the string at 3 depth once
			#this way only if the tab depth is 3 can it manipulate the string
			if  "switch" in line and str(danumber) in line: #line with switch in it  
				print(line)  #doing counter > 1 so it doesn't do the first line
				#this is where the string is changed
				stringname = stringname.replace("switch(exp){","nested_switch_" +str(danumber)  + "(n)")
				break
			else:
				acounter += 1
				continue
		else:
			acounter += 1
			continue
			
	print("the final outcome of the chagne is here:")
	for line in stringname.splitlines():
		print(line)
	

# this takes in what is in ibm[0] and the outputs it to ibm[0] also, quite clever.   
print("let the judge state this is truth") 
number_to_add=66 
swap_switch_for_nest_method_new(teststring60,number_to_add) 
ibm[0] = stringname
print(ibm[0]) 

#where is th eone that grabs teh number automatically though

da='''
	switch(exp){ # 15
		case "1":
			print('hi')
			switch(exp) #       22
			#isn't this special
			print('is this happening')
			switch(exp) #      36
			print("what do we have here")
        
'''

data1='''
	switch(exp){ # 15
		case "1":
			print('hi')
			#isn't this special
			print('is this happening')
			print("what do we have here")
			break
'''

data2='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''

#the innerswitch must be at 3 tabs and the first top switch must be at 1 tab.
data3='''
	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			switch(exp) #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
'''


jazz6='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #63  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #89  
			#############
			break
		case 'what':
			print("nice")
			####################
			switch(exp){ #455  
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''

jazz7='''
	switch(exp){ #1      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 
		default:
			print("we are done here")
	endswitch #this is key here 
'''
#replace_the_last_endswitch_with_brace
print("I found the code I need - I think - we shall see - if it is the right code indeed")

print("about to do thorough testing of chnage_switch_to_method_solved()")
#solved october 29th, 2021  NEXT get the number after comment just in time
'''
this builds a string called newstring replacing switches
at 3 tabs depth with nested_switch
with the comment id after # tacked onto
 the end of the nested_switch_22(exp) like so.
'''

   ##################################################            
       # if "}" in inputstring:  #have to cut "}" out of string      
       #     print("CONFIRMED there is a right brace in string")
       #     for line in templine.splitlines():
       #         if "}" in line:
       #             
       #              templine2 += line.replace("}","")
       #              templine2  +="\n" 
       #        else:
       #             templine2 += line +"\n"
       #    inputstring = templine2
       #     print("======testing if } taken out of string======")
       #    for line in inputstring.splitlines():
       #        print(line)
       #     print("======testing if } taken out of string======")
         #end if   
       # do nothing
       ######================================
       
''' ##################################################            
        if "}" in inputstring:  #have to cut "}" out of string      
            print("CONFIRMED there is a right brace in string")
            for line in templine.splitlines():
                if "}" in line:
                     templine2 += line.replace("}","") #this is where I was taking } out
                     templine2  +="\n"
                else:
                     templine2 += line +"\n"
            inputstring = templine2
            print("======testing if } taken out of string======")
            for line in inputstring.splitlines():
               print(line)
            print("======testing if } taken out of string======")
         #end if 
'''
        ########################################


innerswitchstatus=[]
innerswitchstatus.append(0)

castle1=[]
castle1.append(0)
##===================================================
## change_switch_to_method_solved(inputstring):
##====================================================
print("make the coffee magic coding happen working on this today charlie brown") 
#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    innerswitchstatus[0]= False #by default
    print("====== change_switch_to_method_solved(inputstring)=== get the money now====")
    print('this now takes out the { brace after switch if it is there')
    innerswitch=''
    print("this is what it sees when it starts change_switch_to_method_solved()")
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default setting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitchstatus[0]= True #this is new 
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    if innerswitch == False:
        print("this switch string DOESN'T HAVE an inner switch")
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    
    #### IF INNERSWITCH == TRUE:
    if innerswitch == True: #if a switch at 3 tabs depth  is True
    #check if { in this string if so take it out
        print('checking if left brace in string')
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine  +=   line.replace("{","") 
                    templine  +="\n"
                else:
                    templine += line +"\n"
            inputstring = templine
        #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
       #check if } in this string an if so take it out
      
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():#      getting tab depth
            tabdepth = line.count("\t") #gets tab count for this line
            #skips first switch by counter MUST BE AFTER 2nd line
            #this is where we swap switch(exp) with nested_switch_(number)(exp)
            if "switch" in line and tabdepth == 3 and "end" not in line and counter > 2: 
                print("confirmed switchh in line and tabdepth3")
                #this is new getting the switch id number after # on-the-fly
                #get string to right of #, get right side,remove spaces
                x = line.split("#"); y = x[1];y = y.strip();
                # replace switch with nested_switch + id number harvested from comment above
                thisline = line.replace("switch(exp)", "nested_switch_" + str(y) + "(exp)")
                #this removes the extra spaces after #
                location = thisline.index("#")    #gets location from left where position of #
                thisline = thisline[:location]    #this slices off the right side from # position
                thisline = thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else: #this MEANS NO INNER SWITCH IN THE INPUT STRING
        print("no inner switches in this string")
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine += line.replace("{","") #taking out left brace here
                    templine  +="\n"
                else:
                    templine += line +"\n"           #otherwise it doesn't replace anything 
            inputstring = templine
        else:
            print("=====no { in string  ======")
            #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
        #check if } in this string an if so take it out #I have deactivated this since it's not needed
        
        #this is what we return the inputstring
        return inputstring; #no changes made 
        castle1[0] =inputstring 
        innerswitchstatus[0] = False
    ### end of function =======================================================
    
print("where is my mocha brainfreeze test october 30th...")




print("==========testing string da===================")
print("=============================")
inputstring=''
inputstring = da         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
print("end of red alert change switch to method solved end of test 5..")    
print("=============================")
print("======= testing string data1======================")
 
print("testing goldfish which is NOT indented yet")
#testing a second method in chain right now for expiermentinting==
#the input string MUST BE indented and look like this LOOK LIKE THIS 
somedata2='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''


gofigureit='''
	switch(exp){ #77
		case 'burger':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   look this is chnaged to brace later
'''



#just check if switch at 3 tabs to determine if nested switch
#monday dec 6th thinking 
####$#$$##############========================


            
            
check_if_nested_switch_inside_this_switch(somedata2)
print("inner switch in switch=",table[0] )
print("=======")
print("=========")

check_if_nested_switch_inside_this_switch(gofigureit)
print("inner switch in switch=",table[0] )
#exit()


print("wasn't that fun")
######======================================
# november 20th saturday just after 10am Morgan Hill 2021
inputstring=''
inputstring = goldfish    
    
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
   
print("see if this worked with goldfish accurately")
#exit()
    
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data1         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
    
print("=============================")
print("========testing string data2=====================")


inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data2     
#what I am doing here is returning the concatted string to the string fizz variable.    
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

##==================
print("about to test data3 and I can't have anything after the #22 after switch")
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data3         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

print("massive mammoth test here to see if mocha is ready")
print("does many changes from switch to nested switch with number ==testing jazz SIXAROO now jazz6 ")
inputstring = jazz6
print("testing jazz6")
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)



print("massive mammoth test here to see if mocha is ready")
print("does many changes from switch to nested switch with number ==testing jazz SIXAROO now jazz6 ")
inputstring = jazz7
print("testing jazz7")
print("calling method  change_switch_to_method_solved")
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

#exit()


###================== cold brew linus and snoopy ================== saturday morning software  november 20th, 2021 ====
#this is testing adding the nested switch 
linus_and_snoopy=[]
##==================================
##   add_nested_switch_methods():
##==================================
def add_nested_switch_methods():
    print("add nested_switch_methods() in catching_first_change list")
    for item in catching_first_change: #<== list with strings after taking out inner switch bodies
        #print(item)
        #here calling method chaning_switch_to_method_solved swaps switch for nested_method_numbered
        fizz =change_switch_to_method_solved(item)#this is applying the method to add nested_switch method
        print("===== oh yeah =====")
        linus_and_snoopy.append(fizz) #this is adding the changed string to linus_and_snoopy list
        
        #for line in fizz.splitlines():
        #    print(line)



##================================================
##print_out_result_of_adding_nested_switch() to each switch string:
##================================================
def print_out_result_of_adding_nested_switch():
    counter =1
    print('we made it to the top of the Donnor Summit ')
    for item in linus_and_snoopy:
        print("counter=",counter)
        for line in item.splitlines():
            print(line)
        counter +=1

print("here we go... let her rip")       
add_nested_switch_methods()
print_out_result_of_adding_nested_switch()
print('end of the show time movie trailer')



#test with one string and do piping

#cut_out_inner_switch_body_leaving_switch_word(teststring)
##===========================================================================
##  cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
#def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
#    print('this one is sooo critical')
#    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
#    skipping_some_lines(stringname,start,finish)
#    #this means that the output string should be placed into never_defeated[0]
#    for line in never_defeated[0].splitlines():
#        print(line)

inputlist=[]
inputlist.append(0)
outputlist=[]
outputlist.append(0)
 
print("this is a super critical test of piping two chain methods in sequence")
print("SUPER CRITICAL PIPING METHODS CHAINING TEST ===")
           
#put x in front so it's not used
#it must be indented properly to work daaaaa
xskitahoe ='''
		switch(exp){   #1 === line 10 beginning of single nested switch ======      
			case 'blable':
				print("do something")
				print("yep")
				fallthru
			case 'more':
				switch(exp) #7
					case 'funny':
						print('fun')
					case "da":
						print('yeah')
					default:
						print('bye')
				endswitch #14
				print("nicely")
				break
			default:
				print("we are done here")
		endswitch #this is key here =============line 20 end of nested switch ====
'''	


#testing 
print("testing printing out joy string")
joy='''
	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp) #23
			#############
			break
		default:
			print("we are done here")
	endswitch #38
'''

hotmocha='''
	switch(exp) #3
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #11
			exp = 32
			switch(exp){ #62
			#############
			break
		default:
			print("we are done here")
	endswitch #86
'''

for line in joy.splitlines():
    print(line)



#testing doing 2 methods back to back piping output from first to input to second
#first method   
###==================
##  do_the_pipe()
###==================    
def do_the_pipe():
    print("do the pipe() called pipe pipe PIPE PIPE PIPE")
    print("outputlist[0]=",outputlist[0])
    inputlist[0] = outputlist[0]
    print("now put it into inputlist[0]")
    print("inputlist[0]=",inputlist[0])
    
    

print('doing some pipe testing today')

#######################################
#######################################
#######################################
###====== saturday morning codeing ==november 20th, 2021 testing this puppy ====
## SHIFT NEST STRING TO LEFT INDENT THE PUPPY
print("this is doing shift nest string to left() ======")
print("=====================================================")

shift_nest_string_to_left(xskitahoe)   
resultis =fishbowl[0] 
print("this is after shifting input string to the left to be one tab in front")
print("of the top switch") 
for line in resultis.splitlines():
    print(line)
    
 #this is technically the output which we will now put into inputlist
inputlist[0] = fishbowl[0]   
print("this is testing cutting out switch body from a string")
stringname=xskitahoe; start=7; finish = 14; #this sucker was moving...
print("let us see what is in skitahoe string first")
for line in xskitahoe.splitlines():
    print(line)
print("done with input string to see the starting point")
################################################
#################################################
##  CUT OUT INNER SWITCH BODY LEAVING SWITH WORD
#this one does not work (november 28th this is the hold one)so don't worrya bout it it works elsewhere got it working
# skipping rope yesterday.


cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)
outputstring=string_after_cutting_out_inner_switch_body[0]
print('after stage 1 first method call in chain we have this result')
for line in outputstring.splitlines():
    print(line)
print("end of first change to string")
outputlist[0] = outputstring
print("right here this is  after taking out th einner switch body")
#MUST INDENT LEFT 
do_the_pipe()
#print("do the pipe() called")
#item = inputlist[0]

#second method
print("experimenting with joy string simple convert to removing inner switch")
print("and adding a nested method nubered")
print("calling first method")
#this is what I am testing Sunday november 28th, 2021 3:51pm take 101 north instead next time

print("testing a method on change switch to numberedmethod with joy")
print("testing  change_switch_to_method_solved()")
print('================ this is the one ===============go for the gold now==================')
print('==================that I need to work now ===============================')
print('===== this changes an inner switch by itself into a nested_switch numbered============================================')
print('=======using the commented number next to it==================')
print(" === I am at starbucks next to frosty the snowman")
fizz =change_switch_to_method_solved(joy)#

print("========the result of 1 chain method using piping=======")
for line in fizz.splitlines():
    print(line)
outputlist[0] = fizz #just for testing here 

print("testing hotmocha now changing two nested switches into nested methods")
fizz =change_switch_to_method_solved(hotmocha)# testing 2 switches to change

print("========the result of 1 chain method using piping=======")
for line in fizz.splitlines():
    print(line)
outputlist[0] = fizz #j
print("end of the show, turn out the exit lights")
#exit()
print("line 11259")

do_the_pipe()
#list strings are mutable changeable. 
inputlist[0]=inputlist[0].replace("nested","mocha")
print("see if it sticks")
print("just called the pipe()")
print("now it whould be input[0]")
for line in inputlist[0].splitlines():
    print(line)
#`exit()

print("testing taking out endswitch at bottom of function and swapping it with a brace like in C")
## I am doing this because this is how the parser works so it conforms with JavaScript and C style.
print("TESTING it is already November taking out endswitch and putting in a brace at bottom of function")
#focus=take_out_endswitch(fizz)
#for line in focus.splitlines():#
#	print(line)
###=====================================================================================

#next need to swap endswitch to } (right brace)

#exit()


#playing with this
makeitso= '''
switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #86   
'''

newattempt='''
	switch(exp){ # 15
		case "1":
			print('hi')
			switch(exp) #       22
			#isn't this special
			print('is this happening')
			switch(exp) #      36
			print("what do we have here")
'''

##============================================
## get_top_switch_number_from_this_string(x)
##============================================
twinlist=[]
#testing with string directly above this line
def get_top_switch_number_from_this_string(inputstring):
    print("get_top_switch_number_from_this_string")
    print("there is NO REASON to send humans to Mars")
    counter=0
    x= y =''
    for line in inputstring.splitlines(): #it will be the first switch 06
        if "switch" in line and "#" in line and "nested" not in line  and counter < 2: 
            print("confirmed switchh in line ")
            #this is new getting the switch id number after # on-the-fly
            #get string to right of #, get right side,remove spaces
            x = line.split("#"); y = x[1];y = y.strip();
            print("no drama this is what we have..")
            print("y=",y)
            print("now adding y to twinlist below")
            twinlist.append(y)
            break
        else:
            if counter > 3: #time to bail =too deep can't exist after first line actually
                break
            else:
                continue
                counter += 1
#grab first id number aftger switch 

inputstring =makeitso
get_top_switch_number_from_this_string(inputstring)
print('in twinlist we have',twinlist)

inputstring =newattempt
get_top_switch_number_from_this_string(inputstring)
print('in twinlist we have',twinlist)









print(" ")
print("====end of show here turn the lights out====")
#exit()  #<<<<<<=================== this is where our exit is.


print("== end of show ==== ")
#exit()
string_egg='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #60 
'''


string_egg2='''
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #33 
			#############
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''


pumpkins='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			switch(exp){ #25
			#############
			print("yep")
			fallthru
		case 'more':
			switch(exp){ #34
			print("nice")
			switch(exp){ #45
			break
		default:
			switch(exp){ #66
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

brew='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			switch(exp){ #25
			#############
			print("yep")
			fallthru
		case 'more':
			
			print("nice")
			####################
			switch(exp){ #35
			#############
			print("yep")
			fallthru
			break
		default:
			
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

brew1='''
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			
			#############
			print("yep")
			fallthru
		case 'more':
			
			print("nice")
			
			break
		default:
			
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
'''

#add ability to get the comment number 15 and put that in automatically 
##=======================
##  funtime(y,x)
##=======================
# this is replacing the switch that is nested into 
# a method with the switch number

#building blocks are legos that are small behaviors inside
#of a function that can be assembled and connected in different
#configurations to make new functions without coding
#so interactively combined with a gui
#so chained methods really




#=====================================
# get inner switch number ()  only at the 3 tabs level depth though
#======================================
#so do this multiple times I would have to go thru a loop with the length of the count of switches at three tabs in a string
add_to_list=[]#and call this method get_inner_switch_number(stringname) #and change the counter number
thisline=[] #this also implies only getting one inner switch
def get_inner_switch_number(stringname): #implies at 3 tabs depth
	print("======get inner switch number called=======")
	counter=0
	x=''
	#what this does is get the commented inner switch number after the # in switch
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tabdepth=line.count("\t")      #this is getting tabdepth for this line
		if "switch" in line and "end" not in line and tabdepth== 3:#and "#" in line and counter > 1: #just need to grab the first switch 
			x = line.split("#")  #this manipulates the current line
			y = x[1];
			print("switch number is...",y) 
			add_to_list.append(y)
			counter += 1
			print(stringname)
			#break  #after the if condition above it stops 
		else:
			counter += 1
	print("List add_to_list=",add_to_list)
	#del add_to_list[0] #should delete first one
	print('now we have ',add_to_list)
	#return y;


##===================================
##  funtime(stringname)
## this calls the method get_inner_switch_number()
##===================================
## this replaces the inners switch at 3 tabs with a netsed method name with the id comment number
#this right now only deals with one but I can modify it so that
#modified this and got it working correctly on friday, oct 22nd morgan hill 2021
print("I just don't believe I coded this back on oct 22nd")
print("morgan hill starbucks frosty74")
#===========================================================================
#  convert_inner_switches_into_nested_methods_numbered(stringname): 
#============================================================================
# it will access a list using a loop and they will be put in in sequential order top down
def convert_inner_switches_into_nested_methods_numbered(stringname): #this is feeding in the number looking for
	print("======convert_inner_switches_into_nested_methods_numbered=====")
	x='';concatthis='';counter =0
	# using method get_inner_switch_number(string)#which is grabbed from 3 tab depth only
	for line in stringname.splitlines():
		print(line)
	#modified this and got it working correctly on friday, oct 22nd morgan hill 2021
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if  tabdepth == 3  and "switch" in line:
		# I just moved what was in a method into the loop where the action happens
			x = line.split("#")  
			y = x[1];       #it was str(ournumber)
			y = y.replace(" ",'')
			filler ="nested_switch_" + str(y) +"(exp)" #has to be a string
			#### this is new december 5th #######
			print("inside of function convert_inner_switches_into_nested_methods_numbered")
			print("###====line 11729 ===========##")
			print("filler=",filler)
			if ":" in filler:
			    filler=filler.replace(":","")
			#end if
			print("after fix  -- filler=",filler)
			print("###===============##")
			######################################
			line = line.replace("switch(exp){",filler) #notice replace using var 
			concatthis += line + "\n"
			counter += 1
			continue
		else:
			concatthis += line  + "\n"
			counter += 1
			continue
	################	
	for line in concatthis.splitlines():
		print(line)	
		

print("testing this")
print("convert inner switches without bodies inot nested methods numbered")
convert_inner_switches_into_nested_methods_numbered(brew) #line number of inner switch is in thisline[0]
#exit()

#def plan_c(inputstring):


#so we wouldn't need to enter the 5 we an glean that
#and we don't need to know the 15 number either it will grab it
print('======= end of funtime code ==============')
print("now testing with 2 inner switches to change")
print("oasis in the desert -----")
#this is the one that we are playing with
print('=====those headlights are awefully bright - rude and dumb=====')
convert_inner_switches_into_nested_methods_numbered(string_egg2)
print('pumpkin express')
convert_inner_switches_into_nested_methods_numbered(pumpkins)

#try none and try one
convert_inner_switches_into_nested_methods_numbered(brew)
	
convert_inner_switches_into_nested_methods_numbered(brew1)

#exit()
# I think that I will go through a string and 
# return a list of the locations of switches 
# (skipping the first switch)
# switch and endswitch line numbers
# was just thinking that it's obviously a switch otherwise
# we wouldn't be here so NO NUMBER for main switch (brilliant)
#it still matters but it's obvious that it is there. It's actually
# the main switch and the frame for nested switches. 

ibm[0]=tuna #input of string into ibm[0]
list_of_nested_switches=[]
list_of_nested_switches.append(12) #these are just the line numbers here 12 and 32 
list_of_nested_switches.append(32)

#here I am using a list which has the line numbers of the inner switches locations
print(list_of_nested_switches)  #so it would look like this 
#this goes through the input main switch and changes nested "switch" into a nested_switch numbered

#this is used for managing the nested switches by getting their location to know
#where to copy them when extracting them from a main switch
# today is july 17th, 2021 9:33 am

print('testing this to make list of all switch locations and all endswitch locations')
print(tuna)
switch_location=[]
endswitch_location=[]
print("beginning === put location of switch and endswitch into lists")
print("====---------------------- saturday coding ----------===")

ourcounter=0
#for line in abovenestedswitch.splitlines(): 
for line in tuna.splitlines():
    
    if line.startswith("switch"):
        print("this lines starts with switch")
        switch_location.append(ourcounter)
    
    
    if line.startswith("endswitch"):
        print("this line starts with endswitch")
        endswitch_location.append(ourcounter)
        
    ourcounter += 1
        
print("====OUTPUT TO DETERMINE location of each switch and endswitch====")
print("")
print("switch_location=",switch_location)
print("endswitch_location=",endswitch_location)
print("")
print("===make your dreams reality===")
        



# july 24th, 2021 
#the input for this MUST be the already reduced main switch which
# has just the switch word in place where each nested switch thru endswitch was.


###  Thursday, August 19th, 2021 time 9:07 am
# I think that I just need to not worry about the other nested switches
# and just do the first level of nested switch since the others will just be in the other switches
# so let' say I have two nested switches deep
# I only have to have (for the main switch) the first level nestedswitch
# so then the situation becomes the numbering because in this first level of nested switches
# they would be numbered in sequence 1, 2, 3 etc  
# if say there are two nested in teh first main swith then sub1
# but for the inner levels (the next tab level) I would have to do 4,5,6 I suppose
# so continuing sequence or 1.1 and so forth
# I need to come up with a simple numbering system maybe Alpha first level Alph
###
#what if I have pairs, simple numbering but 
##===========================================	
## number_nested_switches_in_sequence()
##===========================================
#put the input I just created into ibm[0]
#this would be the main string after the nested switches are taken out  leaving switch word
forcedinputstring='''
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){     #  this would be 10  for line number      
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 18 but it said previously 28      
			fallthru
		
		default:
			print('the end')
}
'''
#this is input for add counter to switches
trouble=[]
trouble.append(forcedinputstring)


#this is using preset nested switch starting locations 11 and 29 for this test
# this is for making the nested switch numbered method 



#this swaps switch with nested_switch_" n
##########################################
## number_nested_switches_in_sequence():  #this is using hardcoded input for testing
##########################################
def number_nested_switches_in_sequence(): # list_of_nested_switches[11,29]
	print("=R2D2= NUMBER_nested_switches_in_sequence()  ====== ajax =====")
	newcount=1  #number of nested switches starts from 1
	## wait do I loopthru it get the position of the inner switches now why not
	## modification on july 24th 
	print("to see what it sees first")
	#this is string above called forcedinputstring
	print(trouble[0])  #it was ibm[0] which I will change it back to later
	mystring=''
	mystring = trouble[0] #putting the string into trouble[0]
	newcounter=0
	foundone=[]
	# this gets the inner switch locations after the inner switch bodies have been stripped out (deleted)
	##===============================
	for line in mystring.splitlines():  #this fills list foundone with switch line numbers
		if "switch(exp)" in line:
			print("true we found switch")
			foundone.append(newcounter) #this fills the foundone list of line numbers with switch in it
			newcounter += 1
			continue
		else:
			newcounter += 1
			continue
	#=== end loop ========================
	print("we are done looking for the inner switch locations")
	print("====================")
	print("thefoundone llist has",foundone)
	print("the length is", len(foundone))
	print("========........======")
	print(" ") #below we delete the first switch which is on line 1
	del foundone[0] #this should delete the first switch we don't need 
	print("now we have for foundone list",foundone)
	## end getting inner switch lcoations
	##======================================
	
	#shiney= ibm[0] #so it will skip the first few lines skipping the first switch 
	thecounter = 0 #tracking lines in the string   oh it's using preset numbers
	print('the list of nested switches starting line',foundone)
	switchcount=0
	magic_string=''
	seagull='' #WAS shiney.splitlines()
	for line in trouble[0].splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20 #IT HAS TO BE AFTER THE FIRST 2 LINES TO SKIP THE FIRST SWITCH
		#if  switchcount > 0  and thecounter in foundone:
		# if thecounter in founderone
		if  thecounter in foundone:  #this must be line numbers of inner switches
		#this line of code is absolutely beautiful and elegant 
			print("thecounter=",thecounter)
			print("switchcount=",switchcount)
			########We know the line numbers do it on one pass perhaps
			# it should only go to the lines in the list of nested switches
			gettabcount=line.count("\t")
			line = line.replace("switch(exp){","nested_switch_"  + str(newcount) +  "  " +str(gettabcount) + " tabs " +"(n)")
			magic_string += line + "\n"
			#NEW line above
			newcount += 1  #break #because we are only doing it once to replace only ONE switch #start  = thecounter #this resets the range n to skip what it just did.
			thecounter += 1 #this adds to the neste switch counter
			continue    
		else:
			magic_string += line + "\n"
			# new ling e
			thecounter += 1
			continue
	print("=====-----======-----======------=====----====----====---")
	print("magic_string=")
	print(magic_string)
	print("========")
	for line in magic_string.splitlines():
		print(line)
		
	print("were the changes made - this is kind of important at this stage RED ALERT")
	trouble[0] = magic_string #here it's fed into trouble[0] so it's in a list now
	print("did I rip out the nested switches or are they still intact???")
	print("trouble[0]=",trouble[0])	
	#ibm[0] = shiney
			
####================================			
print('about to call number-nested_switches_in_sequence() to test it extendo bus just passed')
number_nested_switches_in_sequence()
print("it should have ran already testing bugs bunny here ")
print("the nested switch words should be nested numbered methods now")
print("just ran this function number_nested_switches_in_sequence()")
print("original mac computer")
			
#exit()

print("we are at line 4434 now and after finishing doing number_nested_switches_in_sequence() ==>>")
print("this is where the exit() was.......1..2...3..4....5..555..666...777..8.8..9999.10 10==")













#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





			
###============== Sunday July 25th, 2021  10:19 am Cafe Borrone ===============
# the idea is to put the information for each nested switch case
# into the dictionary in terms of it's exact information
# so to fill the data into the nested switch dictionary I will need
# to loop thru the switch string and gather the data for each switch location
# and it's particulars and add it to the dictionary (this should be done first')
# the idea occurred to me since each nested switch has a specific location
# and juggling them can get quite confusing so this way I know which is which
# and where it is.
#=======================================================================
####################
## DICTIONARY HERE 
####################
#putting a named list inside of known dictionary
nest_data=[]
# I probably won't need this.
nested_switch_data =	{  #for pear tree in backyard (2 of them)
#key [level tab depth,number case,  line number, series number
"1": [3,2,23,1], # I can make these now 
"2": [3,3,43,2],
}

print(nested_switch_data)

result=[]
result.append(0)

###############################################################
## RAM LIST TO HOLD TEMPORARY DATA FROM LIST WITHIN DICTIONARY
###############################################################
ram_list=[]
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)

########################
## get_nest_data(key)
########################
def get_nest_data(x): #puts it temporarily into result[0]
	print("get nest data called",x)
	#this grabs the value from the key and puts it into result[0]
	#these are teh parameters for tehe signature for this nested switch
	result[0]=nested_switch_data.get(x)
	#s- there would be a list within result[0]
	#why not instead populate a list
	print("this is what is in result[0]")
	print(result[0])
	for item in result[0]:
	    ram_list.append(item) #see if this fills it or not
	print('ram_list=',ram_list)
#############################		

  #test data input
############################
##  add_to_nest_data(x,y)
############################
cool_list=[]

# what is missing is the meaning of the code and the beahvior that it creates
# when it's running and knowledge
# how it works and what it does at levels

x = cool_list
def add_to_nest_data(x,y):
	print("====add to nest data() called with ", x  ,"and",y)
	nested_switch_data["my_list_" + str(x) ] = y

#print("my_list_1[0]",my_list_1[0])
#print("gosh")
######====================================
########
print("working on access a dictionary in a precise positiion in a list")
print("that is in the dictionary")
my_dict={}
#add a dictionary #this might be just what I need actually 
my_dict["my_list"] =[3,1,4,1]
print('terrible')
print('trying mydict[0] see if it works')
print(my_dict["my_list"][0]) #the key
print(my_dict["my_list"][1]) #the key
print(my_dict["my_list"][2]) #the key
print(my_dict["my_list"][3]) #the key
alpha = my_dict["my_list"][0]
print("alpha sees =",alpha)
#check in the list


# 

my_list_1=[]
my_list_2=[]
my_list_3=[]
#####======================================
y = [1,2,3,4,5]
add_to_nest_data(1,y)

y = [23,26,34,42,52]
add_to_nest_data(2,y)

y = [63,66,64,72,72]
add_to_nest_data(3,y)
print("=================")
print(my_list_1)
print(my_list_2)
print(my_list_3)

#print(my_list_2)
#alpha = mylist_1[0] #should be 1
print("is this even working....",alpha)

print(" == looping through nested_switch_data to see the contents == ")
print("TESTING ship wreck the contents of the dictionary now,,,")
for key,value  in nested_switch_data.items():
	print(key,value)
	













################################
##  NESTED_SWITCH_INFO
###############################	
def nested_switch_info(x):
	get_nest_data(x)
	#this will get the info from the dictionary		
			
			
			
switch_location=[]
endswitch_location=[]
#  WE ARE HERE THIS IS WHERE THE BIG TEST BEGINS TO REPLACE INNER SWITCHES WITH METHODS ON THE FLY
##=================
#if we already have the numbers it should work, later I will have it find the locations first
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG ===BIG TEST here in the switch with 2 nested switches")
print("========")
print("this does the bottom half the bottom nested switch first ")
print("this is becuase it's governed by the corect line numbers")
print("and if I take out the top switch code then the numbers for the lower switch will be wrong")
print("I just realized that") #this is the purpose of experimentation
ibm[0] = tuna  #I am force feeding it into ibm[0]

# I have to tell it what number to use to number the nested method using
# use_number[0]= 2 example








################
# the skipping is done by the main switch when I cam copying it and taking out the 
# nested switches below but keeping the switch word that I then convert to a method nested numbered
#################
### TESTING 
#NUMBERING OF NESTED SWITCH HAS TO BE DONE BOTTOM UP SINCE WE ARE RIPPING OUT THE NESTED SWITCH AFTER THE SWITCH WORD
#oh I will have to do this bottom up so the line numbers are correct.
#first show what is in ibm[0]
print("====== testing main switch template ======tue sep 14, 2021 ================")
print("WE MADE IT HERE line 4691 it's tuesday today")
print("TUESDAY TERRIBLE TEST of main nested switch and adding methods for switches swapped out") 
print(ibm[0])
print("I am taking out the lower switch first (later I will copy it first)")
print("it does it upside down going bottom up to do this.")
'''
skipping_some_lines(ibm[0],28,38) #changes 2nd nested switch
use_number[0]=2
swap_switch_for_nest_method_new(21) #second number has the switch in it 
#the first number is the number for the nested_switch
print("this now does the top nested switch")
print("here I am taking out the first nested switch later I will copy it first")
skipping_some_lines(ibm[0],10,20) #changes first nested switch in the sequence
use_number[0]=1
swap_switch_for_nest_method_new(11) #second number has the line number with switch   #needs to be 1 not 2
print("this is the end of Godzill and King Kong testing")
'''






#this should be called only once and 
print("====++++now testing running number_nested_switches_in_sequence()")
#number_nested_switches_in_sequence()
print("we have just completed the first nesteed switch skipping and putting a nested method 1 in ")
print("ibm[0] should show the main switch with 2 methods where the inner switches were previously")
print("this is the output of the string ibm[0]")
print(ibm[0])
print("I am going to loop thru the switch and change the lines with nested_switch")
print("============= Godzilla =============")
print("END OF GODZILLA AND RODAN AND MOTHRA")


#go thru a number the switches numerically top down

























hawaii ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#######
			switch(exp){          
				case 'blable':
					print("do something")
					print("yep")
					######
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
						######
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			######
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			#######
			switch(exp){          
				case 'fish':
					print("do something")
					print("yep")
					fallthru
				case 'trout':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			#######
			fallthru
		
		default:
			print('the end')
}
'''	
get_switch_and_endswitch_locations(hawaii)
print("this would have just gotton the switch and endswitch line number locations above...")
print("I found it, I was looking for this code")
#empty_switch_and_endswitch_list_locations()

get_switch_and_endswitch_locations(tuna)
###======================================================
#july 19th 2021 testing this feature now morgan hill starbucks
########################################################
#empty_switch_and_endswitch_list_locations()
#print("the one below this line should produce 2 switches and one with 10,20")
#print("why is this wrong")
#get_switch_and_endswitch_locations(samplestring) #samplestring 
#get switch and endswitch lcoations for one nest
#it's off by one says 11,21
#input is 10 and 20 and yet this says the line number is 11 and 21 for nested switch

empty_switch_and_endswitch_list_locations()
print("the one below this line should produce 2 switches and one with 10,20")
print("why is this wrong")
print("get result of get switch and endswitch locations from samplestring")
print("earth is over level ======")
print("earth is over level ======")
print("=== tea time =============")
get_switch_and_endswitch_locations(samplestring) # sammplestring


###  july 14th wednesday 2021 working on this
#real number is count endswitches and add 1 for total switches

#endswitches number is how many nested switches

# this empties the lists storing the switch and end switch locations

#del switch_location[:]
#del endswitch_location[:]

#get_switch_and_endswitch_locations(hawaii)

print("this is the string with two nested switches")
print("here we go wednesday coding - the bicycle gloves are great")
print("first clearing out the lists that hold the locations of the switch and endswitches")
print("this clears out the swith and endswitch locations in the list so it starts empty")

#I was deleting the crucial lists so the code down below couldn't behave correctly

#del switch_location[:]
#del endswitch_location[:]
#feed the string into the method to get the switch and endswitch locations
# but delete the first switch details which isn't important at this point.

#get_switch_and_endswitch_locations(tuna)
#this creates a list that can be of any size and then I can subtract the first switch
#and then divide the number by 2 to get teh number of switches or just count teh switches
'''
nest1=[]
nest1.append(switch_location[0])
nest1.append(endswitch_location[0])
nest2=[]
nest2.append(switch_location[1])
nest2.append(endswitch_location[1])
#wait a  second with each pass the output will be teh same unless I have 
#a list of say ten spaces tol hold locations to be proactive.
#####################################################
print("nest1=",nest1)
print("the two values in nest1 are",nest1[0],nest1[1])
print("nest2=",nest2)
print("the two values in nest2 are",nest2[0],nest2[1])
'''


#++++++++++=========================================================
### july 7th 2021 experimenting 
### testing cutting out two nested switches one at a time
### and replacing the switch location with the nested method with a number
# I need to do these separately first to make that they work
##===========================================
##===========================================
#skipping_some_lines(tuna,nest1[0],nest1[1])
#swap_switch_for_nest_method_new(1)

#and I need to make sure that the resulting string to modify the second phase is correct
#skipping_some_lines(tuna,nest2[0],nest2[1])
#swap_switch_for_nest_method_new(2)
##============================================
##============================================
# what I will attempt it going thru the double nested switch with two nests
# and delete the two nests and put nest methods in the location of the inner switches.
# and then after that is figured out I will first copy each inner switch
# Based on the nested switch locations I find I can determine how many nested switches
# espcially with teh endswitch count 



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========


















def end_program():
    print("ending program")
    return

## method chaining nov 13th, 2021 &:45 am
print("======= chaining methods =======")

'''
I was going to do method call
Loop thru all slots in list
====================
Then do next method call to all items in list
Chaining input to output is input fir next method
Then realized if i chained
Sequence of methods only go thru loop once (genius)
'''


# 48-C battery volvo 2002 s60
# 1 800 222 4357
# 
# 1041 Cochrane road, morgan hill starbucks

## chain methods code  chain methods chain methods CHAIN METHODS 



#A method that calls a series of methods really utilizing output from previous method

#these might have been created above but I am doing them again here just in case.
input=[]
input.append(0)

output=[]
output.append(0)


##=====================
##   get_final_finished_string()
##=====================
def get_final_finished_string():
    print("===get_final_finished_string():===")
    print("output[0]=",output[0])
    print("=== result is in output[0] ===")
    
# passing the baton in the relay race 
##=====================
##   so_pipe()   #this feeds output[0] into input[0] to be used with next method
##=====================
def do_pipe():
    print("==== do_pipe() ====")
    #put output[0] into input[0]
    input[0] = output[0] 


##=====================
##   initialize_lists()
##=====================
def initialize_lists():
    print("====initialize_lists(): ====")
    input[0] =''
    output[0]=''
   


old_string_test='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here        representings stripped out inner nest
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){     #here    # represents already stripped out inner nest 
			fallthru
		default:
			print('the end')
endswitch
'''

  
holdthis=[]
holdthis.append(0)

#this swaps endswitch with }
######################################
## take_out_endswitch(stringname)  #from bottom of nested switch 
######################################
def take_out_myendswitch(stringname):
	print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			print("detected } in line")
			#location = line.index("#")    #gets location from left where position of #
			#line = line[:location] 
			print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			print("after left shift it is ",line)
			#line[0] = first #this is new to slice off right of brace
			line = line[0]#first char
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():
	#    print(line)
	    
	##===========today sunday coding
	
	#then look for this } and reposition it
	'''
	testingthis=''
	for line in holdthis[0].splitlines():
	    
	    if "}" in line:
	        line= line.lstrip()
	        testingthis += line
	    else:
	        testingthis += line
	holdthis[0] =testingthis
	print("now testing if this change worked shifting } to far left")
	for line in holdthis[0].splitlines():
	    print(line)
	'''       
	#this is what I need to modify.
	#so the whole modified string after ripping out endswitch is now in holdthis[0]
	
	print(holdthis[0])
	galaxy = holdthis[0] #now galaxy gets what is in holdthis[0]
	return galaxy #and this is returned
	
print("testing taking out endswitch and putting in brace")
#take_out_endswitch(old_string_test)
print(holdthis[0])


    
##======================================================================================
#the result of each of these methods will put their result in output[0]
#swap_feed_data then puts what is currently in output[0] into input[0] so it's a handoff of the baton
#each of these methods takes in input[0] as input with the result going into output[0]
#after each method we call do_pipe() which puts output[0] into input[0]
# string --> m1(input) => m2(input) => m3(input) => m4(input) => m5(input) 

##====================================================
##  first_method : manipulate_string  (left indent)
##====================================================
#manipulate_string left shift indentation
def first_method(astring): #this does the left shift 
    print("manipulate_string left margin indent ===first message called..")
    #shifts string left to indent it properly
    astring=manipulate_string(astring) #I think that this does left shift indentation
    return astring

##==========================================
##  second method : take_out_switch_body  from inner switches
##=========================================    
#take_out_switch_body
def second_method(astring): #cuts out switch body leaving switch word in all occurances
    print("take_out_switch_body ...seconed method called...")
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #<== key this is new to see if it works=========
    #astring += " water"
    return astring


##=================================================
##  third method : change_switch_to_method_solved
##=================================================
#change_switch_to_method_solved
def third_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("change_switch_to_method_solved  swapto neested_switch method third method called...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    return finalresult

##======================================
##  fourth method  : take_out_endswitch
##======================================
#take_out_endswitch(stringname)
def fourth_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("take_out_endswitch  put in brace instead third method called...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring)
    #astring += " bright"
    return finalresult
    
    
##=======================================================================================
#using descriptive names not true method names yet
# what this is doing is modifying a string in stages in a sequence 
# code name waterfall
output=[]
output.append(0) #so we can use output[0] below
##========================================
##  chain_methods()   this just does a sequence of methods piped  
##                    together so each method passes its output as input for next method
##=====================================
def chain_methods(item):
    print("==NOT ANY MORE OFFICIAL== chain_methods called ====")
    firstresult  = first_method(item)         # manipulate_string(string)
    secondresult = second_method(firstresult) # take_out_switch_body(string)
    thirdresult  = third_method(secondresult) # change_switch_to_method_solved(string)
    fourthresult = fourth_method(thirdresult) # take_out_endswitch(string)
    output[0]    = fourthresult #this puts the result into output[0]
    print("now we are looking in the frac output of fourth method")
    for line in output[0].splitlines():
        print(line)
    #the resulting string is put into output[0]
    
    
    # I still need to rename the actual methods and put them above this section 
    #add comment number to all switches at the very beginning of initial switch string(not here)
    #add_comment_with_number_to_top_switch(input[0]);do_pipe();  #switch # 22 <-- line number added
    #shift_string_to_left_by_reducing_tabs(input[0]);do_pipe();  #subtract tabs # works nov 19th
    #cut_out_switch_bodies_at_3_tabs_depth(input[0]);do_pipe();  #reduce switch body to just switch word
    #swap_switch_with_nested_switch_number(input[0]);do_pipe();  #change switch to nested_switch_22(exp)
    #replace_the_last_endswitch_with_brace(input[0])             # endswitch becomes  }
    #get_final_finished_string() #in output[0] prints it out nest_list to see it




##=================================
## change_slot_string(counter)    this changes content of each slot in nest_list
##=================================
def change_this_slot_string(counter): #requires output[0] finished string
    print("==== change_this_slot_string(counter) ====")
    counter = int( counter)
    nest_list[counter] = output[0] #I really need to test this one and see if it works 
    #this means that needs to have finished chained_methods put into output[0]
    
##============================
## transform_string()    uses nest_list with strings in it of switch case bodies
##============================
def transform_string():  #this calls chain_method(item) # separate switch string input
    print("==== transform_string() ====")
    counter =0  #loop
    for item in nest_list:  #loop thru nest_list and each loop does the chain_methods
        chain_methods(item) # takes in string and does sequence methods puts into output[0]
        change_this_slot_string(counter) #changes slot string from output[0]
        counter +=1


##==================================================
## loop_thru_finished_list_of_prepped_strings():
##==================================================
def loop_thru_finished_list_of_prepped_strings():
    print("==== loop_thru_finished_list_of_prepped_strings() ====")
    counter =0  #loop
    for item in nest_list:
        print(item)
        print("counter=",counter)
        print("===========")
        


# loop_thru_finished_list_of_prepped_strings() took this out
# this hasn't been tested yet. Today is Sunday, November 14th, 2021 10:58 am Pacific Standard Time
# this goes thru nest_list and modifies all of the switch strings
# and fixed the indentation, and adds nested methods and a comment after each switch 
# with the number after it and cuts out the switch bodies at three tabs depth
# and it uses chain methods in a sequence on each string so the loop only goes ONCE !!!!!
##====================================================
##  prep_nest_list_of_switch_strings_for_bypass205()   STAINED GLASS WINDOW SECTION
##====================================================
## ATTENTION: I have the code for this working but the names are new and I need to 
# put the first two methods lists below in these names. This is SOOO COOL NOW 
#dec 5th sunday I don't think that this is called yet.not tested yet then.
def prep_nest_list_of_switch_strings_for_bypass205():
    print("====prep_nest_list_of_switch_strings_for_bypass205() ====")
    go_thru_input_major_switch_string_and_make_list_of_pairs_switch_and_endswitches() # made above
    using_pair_list_make_seperate_switch_strings_and_put_into_nest_list()             # made above
   # transform_string() #DOES CHAIN METHODS  loops thru  nest_list modifies each separated string
    #loop_thru_finished_list_of_prepped_strings() #thru FINISHED nest_list
    #the end result will be in nest_list with the strings ready to feed into bypass205
    

print("testing if this prep nest list is even called or not on dec 12th, 2021")
#prep_nest_list_of_switch_strings_for_bypass205()
print('after calling prep nest list of switch strings for bypass205')

#exit()





holdingpattern=[]
holdingpattern.append(0)
##=========================================
## fixes_dots_in_nested_string(inputstring)
##=========================================
def fixes_dots_in_nested_string(inputstring):
    print('testing very_clever')
    #    print(item)
    newline =''   
    for line in inputstring.splitlines():
        if "nested_switch" in line:
            newline += line.replace(":","") + "\n"
        else:
            newline += line + "\n"
    print("this is the result of modifying and taking out : after nested_switch")        
    for line in newline.splitlines():
        print(line)
    holdingpattern[0] =newline
     #I still need to change the slot in the string though 







input=[]
output=[]
output.append(0)

mystring = "smile "

def get_one(astring):
    astring += " a"
    return astring
    
def get_two(astring):
    astring += " water"
    return astring

def get_three(astring):
    astring += " bright"
    return astring

fizz  = get_one(mystring)
fizzy = get_two(fizz)
fuzzy = get_three(fizzy)

print("fuzzy after my simulated piping =",fuzzy)
print("")
print("")
print("final test before sending it to bypass205()")
print("this should take in a string")
print("indent it to the left margine")
print("take out switch bodies")
print("swap switch with nested_switch numbered")
print("============== here we go rudolph ======")
print(" . ")
print('...................,.,.,.,.,.,.,.,.,.,.,.')



#for testing purposes of transforming an input string this one is teststring3
mystring = teststring3  #right here change it 
for line in mystring.splitlines():
    print(line)
   
   
   
##=============================================    
#manipulate_string left shift indentation
def first_method(astring): #this does the left shift 
    print("=====first method started..")
    #shifts string left to indent it properly
    #LEAVE THIS DON"T MEDDLE THIS WORKS
    # MODERN TAB SHIFTER TO LEFT IS PURE GOLD
    modern_tab_shifter_to_left(astring) #I think that this does left shift indentation
    astring= goldtime[0] #output from modern_tab_shifter_to_left
    #removes garbage on right side of switch strings (still testing)
    ########################
    print("check right here frosty")
    #print("newstring[0]=",newstring[0])
    
  
    
    ##################################
    #print("calling: fixes_dots_in_nested_string() method")
    #fixes_dots_in_nested_string(astring) #when it is nested_switch_22:(exp) removes :
    #astring=holdingpattern[0]
    for line in astring.splitlines():
        print(line)
    
    #return astring
 ######################################   
#take_out_switch_body
def second_method(astring): #cuts out switch body leaving switch word in all occurances
    print("=======seconed method started.take_out_switch_body..")
    #astring =newstring[0] #from first method above outoput
    #TAKE OUT SWITCH BODY METHOD
    #print("see what we are passing does it have something in it")
    print(astring)
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #this is new to see if it works=========
    
    
    print("==output from second method take out switch body==")
    for line in astring.splitlines():
        print(line)
        
    print("================")
    #astring += " water"
    return astring




 #converts inner switch into a nested_switch method numbered
############################################
#change_switch_to_method_solved
def third_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("=======third method started...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    #converts inner switch into a nested_switch method numbered
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    print("===third method output==")
    print("outoput from change switch to method solved")
    #for line in finalresult.splitlines():
    #    print(line)
    
    print("what does it say right here")
    for line in finalresult.splitlines():
        print(line)
        
    return finalresult    
    
    
    
############################################

#take_out_endswitch(stringname)  #this would do all of them regardless of number
def fourth_real_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method startedc...")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring) #replaces it with }
    #astring += " bright"
    return finalresult
    
hollister_list=[]
#take_out_endswitch(stringname)
##=========================================
##  simulated_chain_methods():  this is called for each switch string
#this is doing one string at a time. 
##===================================
def simulated_chain_methods(mystring): #starting point 
    print("SIMULATED CHAIN METHODS () Rudolph the red nosed reindeer")
    first_method(mystring)
    fizz=goldtime[0] #output from first_method()
    print("stage1 fizz =",fizz)
    
    print("FIZZ TESTING CRITICAL 1ST METHOD output of first_method() ")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fizz.splitlines():
        print(line)
    
    ##############################==================
    fizzy = second_real_method(fizz)  #missing 66
    print("stage 2 fizzy=",fizz)
    
    print("FIZZ  TESTING CRITICAL 2ND METHOD to see what's in frac")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fizz.splitlines():
        print(line)
    
    #return   
    ##############################
    fuzzy = third_method(fizzy)
    print("stage 3 fruzzy=",fuzzy)
    
    print("FUZZY  TESTING CRITICAL 3RD METHOD to see what's in ")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in fuzzy.splitlines():
        print(line)
        
        
    ############################
    frac  = fourth_method(fuzzy)
    print("strage 4 frac=",frac)
    #############################
    print("now we are looking in the frac output of fourth method")
    for line in frac.splitlines():
        print(line)
    print('above this line is the Rudolph the red nosed reindeer final first test')    
    print("line number 12502")
    #frac is the result
    #look at frac to see when  switch 31 and 66 are missing
    print("FRAC  TESTING CRITICAL 4TH METHOD n frac")
    print("==looking for missing switch 31 and missing switch 66=======")
    for line in frac.splitlines():
        print(line)
        
    hollister_list.append(frac) #new on november 30th Tuesday 
    
    
    
    
###==============
##   plan B 
##================  testing converting nest string testlist_of_strings
def planB():  #november 30th, tuesday 9:45 am morgan hill starbucks 
    print("never give up")
    print("PLAN B called using simulated_chain_methods on each switch string")
    print('===== welcome to planB ==== november 30th tuesday===')
    print("doing planB testing each nest_list doing chain_methods")
    counter=1
    for item in testlist_of_strings: #test string names numbered
        print("========================")
        simulated_chain_methods(item) #testing chain methods
        print("====== counter= ",counter)
        counter += 1
        
    print("the HOLLISTER LIST of modified switch strings that started out seperated")
    for item in hollister_list:
        print(item)
        print("==== middle ground between methods ===")


#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########


#making this sucker work no matter what 

#print("the big test begins")
#planB()
#print("now simply loop thru the finished changes in the list")

#### stage 1 test ###############
#each fruit method will do the list of 7 input strings stop
#these are the REAL CHAIN METHODS AS OF DEC 11 SATURDAY 2021 8:10 AM ====
result_of_first_method=[]
result_of_second_method=[]
result_of_third_method=[]
result_of_fourth_method=[]

print("this is after the input stings have already been seperated")
##======================
##  move_string_to_left_side()        first method modern tab shifter to left 
##======================
#output: result_of_first_method all switch strings modified
def move_string_to_left_side():
    print("=====APPLE== modern_tab_shifter_to_left()=====")
    counter = 1
    for item in testlist_of_strings:
        print("=======")
        modern_tab_shifter_to_left(item)
        fizz=goldtime[0] #output from first_method()
        #print("apple stage1 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_first_method.append(fizz)
        print("===== counter =",counter)
        counter += 1
    ################################################    
    counter =1
    print("result of shifting input strings to left")
    print("=====APPLE==APPLE   APPLE   APPLE   APPLE   APPLE=====")
    for item in result_of_first_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    




##======================================================
## take_out_the_inner_switch_bodies_leaving_switch()
# output result_of_second_method
# method used: take_out_switch_body(string)
##======================================================
def take_out_the_inner_switch_bodies_leaving_switch():
    print("=====PLUM == take_out_switch_body(item)====")
    counter = 1
    for item in result_of_first_method:
        take_out_switch_body(item)
        print("===== counter =",counter)
        counter += 1
        fizz =lightning[0]
        print("plum stage2 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_second_method.append(fizz)
    ###################################################
    counter =1
    print("result of taking out inner switch bodies")
    for item in result_of_second_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    

#good_plum()





##===================================================================
## good_peach()  change_switch_to_method_solved : switch to nested_switchX(exp) # 
## output: result_of_third_method
##=================================================================
def change_switch_to_nested_switch_method(): #swaps switch with nested_switch method
    print("=====PEACH===change_switch_to_method_solved===")
    counter = 1
    for item in result_of_second_method:
        fizz=change_switch_to_method_solved(item)
        print("peach fizz=",fizz)
        #append outputto result_of_first_method
        result_of_third_method.append(fizz)
        print("===== counter =",counter)
        counter += 1
    #########################################
    counter =1
    print('result of 3rd method on string')
    for item in result_of_third_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    
    
    
##===================================================================
## replace_endswitch_with_close_brace     take_out_endswitch() 
## output: result_of_fourth_method
##=================================================================
def replace_endswitch_with_close_brace():
    print("=======ORANGE=take_out_myendswitch===")
    counter = 1
    for item in result_of_third_method:
        take_out_myendswitch(item)  #other one is take_out_endswitch
        print("=======")
        fizz =  holdthis[0]
        print('orange fizz =',fizz)
        result_of_fourth_method.append(fizz) #this fills up result_of_fourth
        print("===== counter =",counter)
        counter += 1
   #########################################
    print('result of 4th method on string')
    counter=1
    for item in result_of_fourth_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1


#######################################################

    
#this gets the numbers and fills up the list switch_numbers_to_transfer  
switch_numbers_to_transfer=[]
cell=[]
cell.append(0)
##==================================== created dec 6th monday 2021
##  get_switch_number_now(lestring): from quail list before bypass205 is called
##====================================
def get_switch_number_now(lestring): #fills list switch_numbers_to_transfer
    print("====get_switch_number_now()=====") #gets it from quail list
    counter =0
    for line in lestring.splitlines():
        if  counter == 1 and "switch" in line and "#" in line and "end" not in line:
             x =line.index("#");
             x=x+1;answer=line[x:];cell[0]=answer;
             switch_numbers_to_transfer.append(answer) #fills up this list
             break;
        else:
             counter +=1
    
    
            
#this fills up the switch_numbers_to_tranfer list used in bypass205 to
#use in the numbering of the switches with a # after each
##====================================================
##  fill_switch_numbers_list_to_transfer():
##  method: get_switch_number_now()
##==================================================  
def fill_switch_numbers_list_to_transfer():
    print("=======fill switch nubmers list to transfer()====")
    #this is where each switch number in the comment #11 example is put
    #into the list switch_numbers_to_transfer the baton to python output string put in number
    for item in result_of_fourth_method:
         get_switch_number_now(item) #fills list switch_numbers_to_transfer
    #there will be no changes to this switch string   
    print('result of 5th method on string is filling the switch_nubmers_to_transfer')
    print('no changes to the result of the fourth method')
    counter=1
    for item in result_of_fourth_method:
        print(item)
        print("=========")
        print("counter=",counter)
        counter += 1
    print("let's see the (switch_numbers_to_transfer) list now")
    print(switch_numbers_to_transfer)
    #this gets the switch number from each first switch in a string
    # and put is tinot switch_numbers_to_transfer 


#print("=========== get switch numbmer in quail list") 
##=============================================
## get the switch_numbers_to_transfer():
#this is trapeze to get the switch number for first switch in each string
#which will be used for make the def nested_switch and main_switch in python mode
##=============================================
def get_the_switch_numbers_to_transfer():
    counter=1
    for item in chain_output_list:
        get_switch_number_now(item) 
        print("number =",counter)
        print(cell[0]) 
        counter += 1          
    print("switch_numbers_to_transfer",switch_numbers_to_transfer)
  
  
  
  
  
chain_output_list=[]
##===================================================
## fill_chain_output_list():
##==-================================================
def fill_chain_output_list():
    del chain_output_list[:] #empty it to be sure
    print("====fill chain output list()====")
    for item in result_of_fourth_method:
        print(item)
        chain_output_list.append(item)

##======================================================
## loop_thru_chain_output_list_and_fill_quail_list()
##======================================================          
def loop_thru_chain_output_list_and_fill_quail_list():
    del quail[:] #empties quail list
    for item in chain_output_list:
        quail.append(item)
    print("====Quail List Output========== ")
    print("quail output now is this which will be fed into bypass205() parser")
    for item in quail:
        print(item)        
    print(" ")
   # print("==switch_numbers_to_transfer list==")
    #print(switch_numbers_to_transfer)
##=============================================
## show_list_switch_numbers_to_transfer()
##=============================================
def show_list_switch_numbers_to_transfer():
    print("===switch numbers to transfer== stage2 Linus==")
    print(switch_numbers_to_transfer)
    #print("")
    #for item in switch_numbers_to_transfer:
    #    print(item)     

##====================================
##  do_the_blender_chain_methods()
##====================================
def do_the_blender_chain_methods():
    print("==the blender chain methods()==")
    move_string_to_left_side()                         #indents to left
    take_out_the_inner_switch_bodies_leaving_switch()  #cut out switch bodies leaving switch
    change_switch_to_nested_switch_method()            #switch becomes nested_switchX
    replace_endswitch_with_close_brace()               #endswitch becomes }
    fill_switch_numbers_list_to_transfer()             #list generated used for codegen
    fill_chain_output_list()  
         

##  waterfall_chain_methods_gold_master()  formally called do_it()  #this is the one actually being used.
## uses testlist_of_strings for input
##==================================================
#the way this works is each method does all of the switch strings as a set
#each of these methods does all of the switch strings in the list at once 
#and the results are passed downward cascading for the next method to modify.
#========WATERFALL CHAIN METHODS GOLD MASTER THE REAL DEAL=======
##===================================================================================    
## ====  WATERFALL CHAIN METHODS GOLD MASTER OFFICIAL OFFICIAL OFFICAL OFFICIAL  =====       
##=====================================================================================
def waterfall_chain_methods_gold_master():  #THIS WILL TAKE IN THE QUAIL LIST FOR INPUT
    print("===WATERFALL CHAIN METHODS Gold Master 1.3()====THE REAL DEAL  REAL WORLD = ")
    print(" == Sunday, dec 12th, morgan hill starbucks 10:01 am ==")
    for item in testlist_of_strings: #this displays each switch string starting out
        print(item)
        print("========")#formally apple, plum, peach, orange 
    #==chain methods called here=== 
    do_the_blender_chain_methods()
    loop_thru_chain_output_list_and_fill_quail_list()
    show_list_switch_numbers_to_transfer()
    print("LINUS list switch_numbers_to_transfer at bottom of chain methods")
    print(switch_numbers_to_transfer)
    print(" ==end of line ... Sunday, dec 12th, morgan hill starbucks 10:07 am ==")
   
    #new as of dec 9th  2021 #this fills the switch_numbers_list_to_tranfer 
    #of the switch id numbers which are utilized in the stanford string list
    #and added to each first switch in the stanford list and then accessed
    #to use to make the nested_switch_number or main_switch if it's 1.
    #exit():

print("new starting point just 2 function calls===") 
print("serious fireworks star spangled banner")  
print("end of crucial test copying the strings and putting them into a list")
#this separates the switches built using copy body using pairs x,y  
#this needs to be called before filling the list obviously  

#comemnted these out for testing purposes..
#split_up_big_string_into_nested_switches(red_robin)  
waterfall_chain_methods_gold_master()  #<<=== this calls the chain_methods to run
#





#print("quail list output")
#the strings below are after the waterfall chain methods modified the strings
#to prepare them for the bypass205() parser 
##=========================

#outpout code from code above 
gold1='''
	switch(exp) #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_62(exp) #62
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}'''

#=========
#counter= 1
gold2='''
	switch(exp) #11
		case 'blable':
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
}'''

#=========
#counter= 2
gold3='''
	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			nested_switch_23(exp) #23
			#############
			break
		default:
			print("we are done here")
}'''

#=========
#counter= 3
gold4='''
	switch(exp) #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################
			nested_switch_31(exp) #31
			#############
			break
		default:
			print("we are done here")
}'''

#=========
#counter= 4
gold5='''
	switch(exp) #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
}'''


gold6='''
	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
}'''


gold7='''
	switch(exp) #66
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
}'''


#chain_output_list.append(gold1)
#chain_output_list.append(gold2)
#chain_output_list.append(gold3)
#chain_output_list.append(gold4)
#chain_output_list.append(gold5)
#chain_output_list.append(gold6)
#chain_output_list.append(gold7)


#WATERFALL CHAIN METHODS CALLED HERE  




#



#fill_chain_output_list()
        
#print("end result of running chain methods on input switch nested code.")
#for item in chain_output_list:
#    chain_output_list.append(item)
#    print(item)

    
output='''

get switch number now
cell[0]=1  1
get switch number now
cell[0]=2  11
get switch number now
cell[0]=3  15
get switch number now
cell[0]=4  23
get switch number now
cell[0]=5  31
get switch number now
cell[0]=6  62
get switch number now
cell[0]=7  66
'''
#testing_with_new_list=[]
#testing_with_new_list.append(gold1)
#testing_with_new_list.append(gold2) 
#testing_with_new_list.append(gold3) 
#testing_with_new_list.append(gold4) 
#testing_with_new_list.append(gold5) 
#testing_with_new_list.append(gold6) 
#testing_with_new_list.append(gold7) 

print("linus ends here ha ha ====")
  
#exit(); 
 
  