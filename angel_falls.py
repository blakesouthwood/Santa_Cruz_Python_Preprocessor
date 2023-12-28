May 12th, 2022
Testing now for final release golden master of switch case for python.

NEW dec 27, 2023 I just realized I make it optional to use braces in the switch case
since Python doesn't use {  } braces in most of it's code and I was just reviewing my
switch case and I have a brace after each switch in the code and it just dawned on me 
that that violates the syntax structure of Python. Good thing that I just caught that.
So I will make the brace optional and just remove it if inserted and make it unnecessary
if a coder is writing the switch case it will accept it either way with or without.

May 10th, 2022
Was doing more testing on switch case in real-world situations.
Took out showing the input which was redundant and took out print statements that were unnecessary.

Cleaning up code right now. Running more tests with switch case inside of functions.
Doing testing today of nested switches.
Will add error messages to fail gracefully if a switch case is malformed or missing something
such as an endswitch. Within the switch case indentation matters.

Still need to write the style guide documentation paper.


May 6th, 2022
Converting the code so output is as originally designed.
This means I am turning off print statements that I used for debugging and commenting them out.
Also adding more documentation throughout the code base. 
I will also add a sequence list of functions called for each behavior.

This will take a few days. So the code runs but I need to make it market ready.
#=========================


May 5th, 2022
I will next work on adding the Error codes for the switch case 
And I will write the style guides with examples and style rules


In the file that you are going to use a badass true blue switch case (will make style guide this week)
you just need to put this at the top of each file that will use the NEW switch case for Python kicks ass over match case garbage.
It's based more on JavaScript which I adore way more than C.

import strawberry            
from strawberry  import *     

#=============================

Today is Tuesday, April 26th, 2022 and it's 12 noon (eerie) and I feel like I have been gone a year. I was a bit preoccupied.

Dam, sorry about the delay I got distracted for the past month with other things.
I had actually finished the nested switch case engine and I neglected to upload the final golden master code
which I still need to document and create a golden user guide - but all in good time.
I haven't posted here in centuries and even forgot how to log in.

So the module is based on what my parents grew in the back yard garden that was sweet.
The javascript/C style switch case with nesting and macros is called strawberry.

I will now update these files:
mocha.py
macros_exps.py
strawberry.py
official_switch_case_silver.py
running_switchcase_engine.py
snowflake.py
trex.py

Please bear with me the past month has been the most fascinating
and mentally draining and strange in my life. I wouldn't wish upon
anyone what I have experienced. Good music helps. KFJC, KKUP, KOHL, KZSU.


March 23rd, 2022 Wednesday, 10:22am PST
Just tested the switch module now called strawberry in Sublime Text and it runs beautifully.
I normally do my coding in BBEdit and occassionally in Visual Studio Code to step thru code when debugging.

March 18th 2022 10;25am Friday
Pure Nirvana.

#so this is a demonstration of the endswitch(stringname) method having some smarts
so it can sort thru the type  and kind of switch and if exps are at the top for a nested
switch it correctly first distributes them above each inner switch in sequence
and then generates the correct python code and executes it.
This utilizes the snowflake module.


this is parsed and runs now. what a rush.
dino[0]= 'ship'
starshiptest ='''
	exp= 'ship';
	exp= 'blable';
	exp= 'tahoe';
	exp= 'winter';
	exp= 'burger';
	exp= 'snow fire';

	switch(exp){  
		case 'lantern': 
			print("pigion point light house!")
			print('this green green green . it actually works')
			print('how green green green, yes way ')
			break
			
		case 'ship':
			print('are we nearly up at Tahoe yet  !')
			
			#############
			
			switch(exp)  
				case 'blable':
					print("inside of first nested swi tch here ")
					print("this is really working, fantastic...")
					result[0]="very cool stoopping here "
					#break
					####################
					
					switch(exp){ 
						case 'tahoe':
							print("we are inside of tahoe swi tch now")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							
							switch(exp){    
								case 'winter':
									print("ththis is inside of winter now")
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
			
			switch(exp)
				case 'burger':
					print("go to wendys today")
					####################
					
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("THIS IS SNOW FIRE HERE")
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
			print('taught me how to write code should be last line ')
			break
		case 'easter':
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			result[0]='sip some mocha now'
			print('result[0]=',result[0])
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	
endswitch(starshiptest)


== OUTPUT==

===NESTED SWITCH IS TRUE==
dino[0]= ship
====main_control_sequencer() called====

are we nearly up at Tahoe yet  !
inside of first nested swi tch here 
this is really working, fantastic...
we are inside of tahoe swi tch now
oh is this going to really work now ... really it is
nice
ththis is inside of winter now
listening to mit debugging session in summer
yep
nice kayaking race
yep
go to wendys today
THIS IS SNOW FIRE HERE
yep
nice
taught me how to write code should be last line 

==== END OF OUTPUT ====

Code Tree the relevant methods for the new code behaviors
status_of_exps=[]
status_of_exps.append(0)
##=================================================
## look_in_mystring_for_exps_at_top(mystring):
##=================================================
def look_in_mystring_for_exps_at_top(mystring):
	the_exps=False
	switch_location=''
	print("look in mystring for exps at top(mystring)")
	counter =0
	#or get line number with first switch in line
	print('stage 1  look for exps at top')
	for line in mystring.splitlines():
		#print(line)
		if "switch" in line:
			switch_location= counter
			break
		else:
			counter += 1
	print("switch_location=",switch_location)
	counter =0
	#determine if exp in line before first switch_location
	print('stage 2 look for exps before first switch')
	for line in mystring.splitlines():
		#print(line)
		if counter != switch_location:
			if "exp=" in line or "exp =" in line:
				print(line)
				the_exps = True
				break
			else:
				counter += 1
	print("the result of this jazz is the_exps=",the_exps)
	status_of_exps[0] = the_exps


##==============================
##  two_choices(mystring)
##==============================
def two_choices(mystring):
	#determines here if mystring is a nested switch or not 
	nested =count_switches_in_inputstring(mystring)  #method  count_switches_in_inputstring(mystring)
	#assert nested == True, "nested != True"
	if nested == True:
		print('nested is true===========::::')
	else:
		print('nested is false==========::::')
	##=========================
	if nested == True:
		print("nested is obviously TRUE this is necessary at this phase")
		look_in_mystring_for_exps_at_top(mystring)   #method look_in_mystring_for_exps_at_top(mystring)
		print("------------------------------")
		print("status of the_exps=",status_of_exps[0])
		print("------------------------------")
		if status_of_exps[0] == True: #means at least one exp= above first switch
			#this is then called to redistribute the exps below ONLY if they were at top
			mystring=prepare_my_string(mystring)     #method  prepare_my_string(mystring)
			###################################
			#print("let us look at the exps moved down from the top if this is really true")
			#for line in mystring.splitlines():
			#	print(line)
				
		else:
			pass
		# else skip it
		###########################################################
		smart_endswitch(mystring) #was (mystring)  #nested switch is in trex
	else:
		cool_endswitch(mystring)   #single switch is in official_switch_case_silver
	


##======= snowflake module code that redistributes the exp vars at top of nested switch string  ======
print('this is INSIDE of snowday')
   




soclever=[]
soclever.append(0)

partylist=[]

def mystacktrace(stringhere):
	partylist.append(stringhere)

def list_party_list_sequence():
	for item in partylist:
		print(item)


def loop_thru_the_string(stringname):
	for line in stringname.splitlines():
		print(line)
		
relay=[]
relay.append(0)
stopline=''
startline=''
gauge=[]
gauge.append(0)
collection=[]   #this gets the inputs exps for the NESTED SWITCHES INPUT
serious=[]
serious.append(0)
russia=[]
russia.append(0)

##============================================
## get_first_switch_location(instringname):
##============================================
def get_first_switch_location(instringname):
	#this gets the location of first switch ---------------
	fuel_level=''  #here it is initialized
	counter =0
	for line in instringname.splitlines():
		tabs = line.count("\t")
		#print("tabs =",tabs)
		if "switch(exp)" in line and tabs == 1:  
			grabit =counter 
			russia[0]=grabit #pouts grabit into russia[0]
			break
		else:
			counter += 1

##===========================================================
## copy_switch_string_from_first_switch_down(instringname):
##==========================================================			
def copy_switch_string_from_first_switch_down(instringname):
	# this copies the switch string from the first switch word down to the bottom of string
	counter = 0
	fuel_level =''
	grabit = russia[0] #here it puts var into grabit
	print("russia[0]=",russia[0])
	for line in instringname.splitlines():
		if counter >= grabit:   #only concatting from first switch line number forwards
			fuel_level += line + "\n"
			counter += 1
		else:
			counter += 1

	serious[0] = fuel_level

##==========================================
## remove_exps_at_top_now(instringname):
##==========================================
def remove_exps_at_top_now(instringname):
	mystacktrace("remove_exps_at_top_now(instringname)")
	get_first_switch_location(instringname)                  #method
	copy_switch_string_from_first_switch_down(instringname)  #method
	


##==========================================
##  detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(stringname): #above top of nested switch string
	mystacktrace("detect_input_exps_above_first_switch():")
	testing_switch_input_vars='';counter =0;switch_input_vars='';active = False
	#I can concat them to the growing string data
	for line in stringname.splitlines():  #looks in sample 3 line string above for testing
		if line.startswith("\texp="):
			#print(line)
			startline = counter;active = True;
			switch_input_vars += line
			#==== this adds the line number with exp= to list collection =======
			collection.append(counter) #adds line number
			counter += 1
		else:
			#this says if line doesn't start with "exp="" nor start with "switch(exp)"
			if "\texp=" not in line  or line.startswith("switch(exp)"):
				active = False
				stopline = counter -1 #the previous line obviously
 
	clean = switch_input_vars.replace(";",",") #replaces ; with ,
	switch_input_vars = clean
	switch_input_vars = switch_input_vars[:-1] #this cuts off the last char at end
	relay[0] = switch_input_vars 

	######################################################
	#THIS WOULD THEN NEXT FILL THE STRING switch_input_vars=
	#remember I will need " at front and " at the tail
	#remove the tabs now
	cute =testing_switch_input_vars.replace("\t"," ")
	cute =cute.replace(";",",")
	cute = cute[:-1]
	testing_switch_input_vars=cute
	testing_switch_input_vars= '"' + testing_switch_input_vars + '"'
	really=testing_switch_input_vars.count('"')


#work on this
#do replace of "exp =" change to 'exp='


##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing(stringname):
	mystacktrace(" manage_exps_prepare_for_processing()")
	concrete='';fool='';counter =0;
	#what this does is skip this switch(exp) line at the top 
	#so when it reaches the first switch it stops immediately
	for line in stringname.splitlines():
		if "switch(exp)" in line: #this should stop it
			break
		else:	#this means copy the line into string fool line by line
			if "exp" in line: 
				line = line[5:]  #cut off first 5 chars
				line = line[:-1] #cut off end char
				fool += line  + "\n"  

	#here it is building a string 
	concrete = concrete[:-2]         #gets rid of space and , at front
	concrete = '"' + concrete + '"'  # new on feb 21st monday
	new_switch_input_vars=concrete
	
	
	
#this would happen in the first phase scan of the string to grab the exps above first switch
#detect_input_exps_above_first_switch() #and fill var string automatically
##============================================================================

##==================================
##  add_line_to_string(stringname): 
##==================================
# what this does is look specifically for each line with switch with tabs more than 2
# and adds a new line above the switch moving the switch line down 1
# now actually since every line is moved down one from that point
# the next switch that a line is added above means it moved down 2 and not 1
# and so on and so forth

##====================================================
##  scan_thru_string_at_top_for_exps(stringname):
##====================================================
def scan_thru_string_at_top_for_exps(stringname):
	print(" ====scan_thru_string_at_top_for_exps(stringname): ==:::::===")
	mystring=''
	if "exp =" in stringname: #tests if exp = in string presumably at the top
		for line in stringname.splitlines():
			if "exp =" in line:
				#so concat and build new stirng
				#this changes (exp =) to (exp=) so that they are consistent
				fixedline = line.replace("exp =","exp=") #looks for exp = changes to exp=
				mystring += fixedline + "\n"
			else:
				mystring += line + "\n"
		soclever[0] = mystring
	else:
		soclever[0]= stringname



resultstring=[]
resultstring.append(0)
samplelist=[]

def do_first_stage(mytest_list):
	print("do first stage")
	counter =0
	print("look in mytest_list now", mytest_list)
	print("=========what the hell is in this list=================")
	for item in mytest_list: #loops thru list made from switch_input_vars string split up
		#this says look at the first char in this item
		if item[0].startswith(' ') == False: #meaning if var doesn't start with space
			answer = mytest_list[counter]
			answer = " " + answer             #adding one space to front of var for uniformity
			mytest_list[counter] = answer     #force feed the change
			counter += 1
		else:
			counter += 1


def do_second_stage(mytest_list):
	print("calling do second stage()======")
	counter=0 
	#chop off from before and including =
	for item in mytest_list: #now this takes out the front part with exp=f from '='
		txt = item
		x = txt.split('=')
		y = x[1]
		#print(y)
		mytest_list[counter] = y
		counter += 1
		

def do_third_stage(mytest_list):
	print("calling do second stage()======")
	counter =0
	for item in mytest_list:            #print("now mytest_list=",mytest_list)
		string = item
		string = string.strip()         #takes out spaces before and after string
		string = string[1:-1]           #cuts off first and last char whatever it may be 
		mytest_list[counter] = string   #puts string into mytest_list[counter]
		counter += 1
	
	print("show samplelist starting here=",samplelist)
	for item in mytest_list:
		samplelist.append(item)  #fills samplelist which is used to feed into adding
	print("at this point the contesnts of samplelist ??")



##=========================================================================
##  take_input_vars_for_switches_convert_to_list(switch_input_vars):
##=========================================================================
def take_input_vars_for_switches_convert_to_list(switch_input_vars):
	mystacktrace("take_input_vars_for_switches_convert_to_list(switch_input_vars):")
	mytest_list = switch_input_vars.split(",") #split at commas put into a list 
	do_first_stage(mytest_list)  #method
	do_second_stage(mytest_list) #method
	do_third_stage(mytest_list)  #method
	
	

##==================================================
##  add_exp_var_above_each_switch(stringname):
##==================================================
def add_exp_var_above_each_switch(stringname): #from samplelist
	mystacktrace("add_exp_var_above_each_switch(stringname):")
	manage_exps_prepare_for_processing(stringname)       #method
	cool = relay[0];samplelist.clear() 
	take_input_vars_for_switches_convert_to_list(cool)   #method
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =1
	for line in stringname.splitlines():
		tabcount = line.count("\t")
		if "switch(exp)" in line and tabcount > 2:  #if a line with switch(exp)at 3 or greater in it
			tabcount = line.count("\t")
			###========================================================
			#here the sameplelist contains just the number or word after the exp=
			word = samplelist[mycounter]
			tabs = tabcount * '\t'
			##========================
			if word[-1] == "'": #this says: if last char in word = '
				word= word[:-1] #cuts off last char of word
			else:
				pass
			##===========================
			adding_exp = "exp='" + str(word) + "'"   #this is the word after exp=
			#this is adding the exp='word' to line and putting switch on next line
			codeking += tabs + adding_exp + '\n' + line + '\n'
			mycounter += 1
		else:
			codeking += line  + '\n'
	resultstring[0]=  codeking
	
	
	
		

##==============================================
## show_list_resultstring_to_verify_output():
##==============================================
def show_list_resultstring_to_verify_output():
	mystacktrace("show_list_resultstring_to_verify_output():")
	
	

##======================================
##   take_out_first_line():
##======================================
def take_out_first_line():
	mystacktrace("take_out_first_line():")
	morebuilding=''
	#this is right::: it must be -1 for setting the counter
	counter = -1  #note this is now -1 it was 0 previously but first case was getting cut out
	for line in serious[0].splitlines():
		if counter == 1:
			pass
			counter += 1
		else:
			print(line)
			morebuilding += line + "\n"
			counter += 1
	
	serious[0]= morebuilding
	morebuilding=''


#sniffer to detect exp= above first switch
#and if so then call the transform method otherwise don't call tranform method
#===========  designed on Friday, February 25th, 2022 ==== 10:17 am ===
if_exps_at_top=[]
if_exps_at_top.append(0)
##======================================================
## determine_if_exps_above_first_switch(stringname):
##======================================================	
def determine_if_exps_above_first_switch(stringname): #sniffer
	print("=@@@@===determine_if_exps_above_first_switch(stringname): ===@@@@==")
	if_exps_at_top[0] = 'False' ;#sets default setting of if_exps_at_top[0] to 'False'
	counter =0; endpoint =''; #line number of first switch// also clears it out as reset here
	#get location of first switch( at tab depth 1 )	
	for line in stringname.splitlines():
		tabsdepth = line.count("\t")#how do I say if exp= above first switch
		if "\tswitch(" in line and tabsdepth == 1:
			endpoint = counter #sets endpoint to counter
			#print("endpoint =",endpoint)
			break
		else:
			counter += 1
	#this looks to determine if exp= ABOVE first switch at 1 tab depth
	counter =0  #the endpoint constant is the line number of the first switch at tab depth 1
	print("endpoint line number with first switch at 1 tab depth =",endpoint)
	for line in stringname.splitlines():
	#I can change it if exp = change to exp= #work on it
		if "\texp=" in line and counter < endpoint: #this is gleaned above
			if_exps_at_top[0] = 'True'; #sets if_exps_at_top[0] to 'True'
			#print('right here if_exps_at_top[0] should = True')
			break  #the moment this is True end this loop obviously
		else:
			counter += 1

##==============================
##  loop_thru_answer()
##==============================
def loop_thru_answer(answer):
	for line in answer.splitlines():
		print(line)

##==========================================================================
## take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
##==========================================================================
def take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
	print("==== take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):==")
	samplelist=[];samplelist.clear(); mytest_list=[]; mytest_list.clear();relay[0]=''
	loop_thru_the_string(stringname)                 #method
	detect_input_exps_above_first_switch(stringname) #method
	add_exp_var_above_each_switch(stringname)        #method
	show_list_resultstring_to_verify_output()        #method
	gauge[0]=resultstring[0]; trouble = gauge[0]
	remove_exps_at_top_now(trouble)                  #method
	take_out_first_line(); answer =serious[0]        #method
	loop_thru_answer(answer)                         #method
	return answer                                    #resulting concatted string
	guage[0]='';resultstring[0]='';trouble='';serious[0]='';answer='';samplelist=[]
	


finaloutput=[]
finaloutput.append(0)	

##=======================
## bottom_method()
##=======================
weasel=[]
weasel.append(0)
def bottom_method(stringname):
	if if_exps_at_top[0] == 'True':
		print("==exps at top True=>>>>>>>>>=")
		outputis=take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname)
		finaloutput[0] = outputis
		##==================================================
		# ====thursday march 17th, 2022 at 9:34 am=========
		print("now creating the radical= output string I need")
		#this changes the output by putting radical var at front
		# and putting the string into triple ''' front and tail
		radical='' #this should empty it and not concat it
		front = "radical='''\n"
		tail = "'''"
		smarter = front + outputis + tail
		weasel[0] = smarter
		print("this should be radical= full string")
		
		###=======================================
		print("this is the radical= string .")
		for line in smarter.splitlines():
			print(line)
	
	else:
		print("this switch string doesn't have exps at the top so original string")
		loop_thru_the_string(stringname)
		pass
		
		

##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser(stringname):
	print("===transform netsedswithdstring  ==")
	scan_thru_string_at_top_for_exps(stringname) #method
	stringname = soclever[0] #now this should fix it
	determine_if_exps_above_first_switch(stringname) #method sets if_exps_at_top[0] to True or False
	#if exp at top then use them otherwise skip
	bottom_method(stringname)
	#print('----------the output is in weasel[0]--------')
	#for line in weasel[0].splitlines():
	#	print(line)

#question is the output from this put back into stringname 
#if not then that is what I need to do next
# saturday morning coding fixing bugs and testing marathon		


##===============================
## prepare_string(stringname)
##===============================
def prepare_my_string(stringname):
	print('prepare_my_string() called in snowflake')
	print("=====prepare_string called in snowflake======")
	print("called from within SNOWDAY SMOWFLAKeS prepare string called inside of snowday.py")
	transform_nested_switch_string_for_parser(stringname)
	#output is in weasel[0]
	goodjob = weasel[0]
	return goodjob
	









dogged determination is what it takes
March 17th, 2022
I can parse a nested switch and move the exp vars at the top to the correct location above each nested switch
and then convert it into python and run it. That was a pain. Now works.



March 15th 2022 10:09 AM PST Morgan Hill, California
# example single switch and nested switch inside of functions running.



def make_it_happen():

	input_flow('ufos')
	s ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\")
			print('nimitz')
			print("==area 51==")
			fallthrough
	
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker =====")
			
		
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			print("all too easy===")
			break
			
		default:
			print('no results')
			print("that is all")
			break
	}
	'''
	endswitch(s)



def really_risky():
	num = 7   
	input_flow(num)
	r ='''
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
	endswitch(r)


print("this is the major test right here on Tuesday 10am right away")
print(".......=====single switch==========.......")
make_it_happen()
print("........===nested switch example========...")
really_risky()

exit() 
#OUTPUT
varholder[0] = ufos
['ufos']

the input exp in clever was::  ufos
we are inside of switch now ufos
case = ufos
ww2!
nimitz
==area 51==
we are inside of switch now star wars
case = star wars
return of the jedi
Luke Skywalker =====
we are inside of switch now darth vader
case = darth vader
flying in it tie-fighter
the force is strong in this one...
all too easy===
clearit()
a list
['starter']
........===nested switch example========...
dino[0]= 7
====main_control_sequencer() called====
IS THIS ONE CALLED build_list_input_list()  line 34132perhaps maybe march 8th 
inside of practice_list looping == EXPERIMENTAL = march 8th==







this is =====zebra black and white ====== 
pass Dutch Flat, Cisco, and Kings Beach thru NorthStar !
 this is 7 thru 10 here we are
this is the second string to try of sw itch 11 this is really cool 
this is really working, fantastic...
do THIS IS SO COOLinside of sw 15
oh is this going to really work now ... really it is
nice
this is possibly sw 25
listening to mit debugging session in summer
yep
morgan hill starbucks nesting works
yep
we are done here
this should be the last line here for output



March 11th Friday 2022
I know that this is considered sacrilegious but what this is does create THE BEHAVIOR of a goto jump to label.
There isn't actually a goto though it's a function call it's really manipulating a fallthru in a switch case that
can jump anywhere within the body of a switch case which is a lattice struture above python and the equivalent running
behaviors is created in python code that is generated. Again what is being used is a clever switch case to mimic
the behavior of a goto label to jump anywhere within a function.

Implimenting "goto label" in Python which is generated dynamically embedded within a switch case construct
goto label is in the following programming langauges.
##=============================
Assembly(1949)      JMP label
Cobol   (1959)      GOTO label
Ada     (1983)      goto label
LISP    (1984)      do, do*, dotimes, dolist, loop)  macros that expand into goto :note Common Lisp 
C       (1978)      goto label
C++     (1985)      goto label     
C#      (2000)      goto label
Go      (2007)      goto label   
Python  (2022)      goto label   #so proud to make this reality!
##===============================
The way it works is using a skeleton of the switch case underneath.
If inside of deeply nested for loops or while loops it actually puts nested loops within a separate function
and exits using a return and then the goto('label') is triggered, The goto label feature actually will use the fallthru('label') feature in the switch case.
The fallthru() actually calls switch(word) so it can jump up or down from anywhere in the switch case - pure genius.
By default it goes thru a starter 1st case above a function to enter the realm of the function and then behaves
at the whim of the goto flow logic. For flexibility the word jump can be substituted for goto.
Labels can be lower case, mixed case, or upper case. I tested it over a year ago but I just recently tamed the 
true switch case code. 
The way it works will be just like the switch case code that is in a var'd triple string docstring
Example:
	
some code here which would be within a chunk of code. 
   goto mylabel; #semicolon optional
   jump mylabel; #this will also be valid in hommage to Grace Hopper's preferred word when she designed 
	
mylabel:  #must be one tab from left margin to be valid
	some code here 
	
##=====================================
March 7th, 2022  9:51am PST Morgan Hill, California Starbucks 
endswitch(stringname) implimented successfully :: this is the trigger for activating a switch case string before it was
called two_choices() for testing since it did the 2 modes of single switch and nested switch.
This would be at the end of the input doc string var of the switch case code
which actually triggers the translation and execution of the switch case

I will upload the example working code Saturday. I have to tend to some other responsiblities now.


March 2nd 2022 found some bugs working on them.
For nested switch case if the first cases aren't numbers but words it crashes and can't digest the case words
so I'm working on a hybrid for that scenario.

Doing more testing of switch cases inside of functions too and then nested switches inside of functions.

At least the switch and nested switches finally work. The remaining bugs are small and can be conquored
with a few lines of fuzzy logic. 




tuesday march 1st, 2022
IT ALL WORKS!!! what a triumph.  two_choices method works initially.
Nested switches work as designed.

#this will all go into mocha #right now it worked in this format

import mocha  
from mocha  import * 

import snowday
from snowday import *
from snowday import fossil

num = 7   
feedinput(num);

z='''
	exp= '7';
	exp='orange';
	exp='green';
	
	switch(exp){
		case 1 thru 6:
			print("mocha morning!")
			print('a walk in the park')
			print('listening to neo music ')
			break
		
		case 7 thru 10: 
			print("two !")
			print('cold tennis victory is mine')
			print('who will win? ')
			fallthru
			
			switch(exp){
				case 'red':
					print("this is red we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("----------blue------------- ")
					print("----blue ----..")
					break
				case 'orange':
					print("=====ORANGE AID TANG== ")
					print("orange orang orange.")
					break
				default:
					print('this is default this was missing')
					print(' darn it')
			endswitch
			
			switch(exp){
				case 'green':
					print("green fireballs in ww2 ")
					print("gren aliesns green ")
					break
				case 'purple':
					print("----------purple--------  ====")
					print("---- purple-------..")
					break
				default:
					print('this is lower def ault this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''	

#this series of methods will all go into the top guts of endswitch()
too_smart(z)  #function too_smart() is in snowday
#z is string just above it here

#here 
real = fossil[0] #this is teh output from dolast after prepare string()
print("this is in runnig swith case engine looking in fossil[0]")
for line in real.splitlines():
    print(line)
    
two_choices(real)
exit()

##============================
#this is what is in snowday.py
#this is at the top
fossil=[]
fossil.append(0)


soclever=[]
soclever.append(0)

partylist=[]

def mystacktrace(stringhere):
	partylist.append(stringhere)

def list_party_list_sequence():
	for item in partylist:
		print(item)


def loop_thru_the_string(stringname):
	for line in stringname.splitlines():
		print(line)
		
relay=[]
relay.append(0)
stopline=''
startline=''
gauge=[]
gauge.append(0)
collection=[]   #this gets the inputs exps for the NESTED SWITCHES INPUT
serious=[]
serious.append(0)

##==========================================
## remove_exps_at_top_now(instringname):
##==========================================
def remove_exps_at_top_now(instringname):
	mystacktrace("remove_exps_at_top_now(instringname)")
	#print("=====remove_exps_at_top_now()=== this is called HERE 5:00 pm ====")
	fuel_level=''  #here it is initialized
	counter =0
	for line in instringname.splitlines():
		tabs = line.count("\t")
		#print("tabs =",tabs)
		if "switch(exp)" in line and tabs == 1: 
			grabit =counter 
			break
		else:
			counter += 1
	#this will start concatting the line with the first switch in it
	#only copy the string once it sees number in solution[0]
	
	counter = 0
	for line in instringname.splitlines():
		if counter >= grabit:   #only concatting from first switch line number forwards
			fuel_level += line + "\n"
			counter += 1
		else:
			counter += 1

	serious[0] = fuel_level
    


##==========================================
##  detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(stringname): #above top of nested switch string
	mystacktrace("detect_input_exps_above_first_switch():")
	testing_switch_input_vars='';counter =0;switch_input_vars='';active = False
	#I can concat them to the growing string daaaa
	for line in stringname.splitlines():  #looks in sample 3 line string above for testing
		if line.startswith("\texp="):
			#print(line)
			startline = counter;active = True;
			switch_input_vars += line
			collection.append(counter) #adds line number
			counter += 1
		else:
			if "\texp=" not in line  or line.startswith("switch(exp)"):
				active = False
				stopline = counter -1 #the previous line obviously
 
	clean = switch_input_vars.replace(";",",")
	switch_input_vars = clean
	switch_input_vars = switch_input_vars[:-1]
	relay[0] = switch_input_vars 

	######################################################
	#THIS WOULD THEN NEXT FILL THE STRING switch_input_vars=
	#remember I will need " at front and " at the tail
	#remove the tabs now
	cute =testing_switch_input_vars.replace("\t"," ")
	cute =cute.replace(";",",")
	cute = cute[:-1]
	testing_switch_input_vars=cute
	testing_switch_input_vars= '"' + testing_switch_input_vars + '"'
	really=testing_switch_input_vars.count('"')


#work on this
#do replace of "exp =" change to 'exp='


##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing(stringname):
	mystacktrace(" manage_exps_prepare_for_processing()")
	concrete='';fool='';counter =0;
	for line in stringname.splitlines():
	#what this does is skip this switch(exp) line at the top 
	#so when it reacheds the first switch it stops immediately
		if "switch(exp)" in line: #this should stop it
			break
		else:
			if "exp" in line:
				line = line[5:]  #cut off first 5 chars
				line = line[:-1] #cut off end char
				fool += line  + "\n"  

	#here it is building a string 
	concrete = concrete[:-2] #gets rid of space and , at front
	concrete = '"' + concrete + '"'  # new on feb 21st monday
	new_switch_input_vars=concrete
	
	
	
#this would happen in the first phase scan of the string to grab the exps above first switch
#detect_input_exps_above_first_switch() #and fill var string automatically
##============================================================================

##==================================
##  add_line_to_string(stringname): 
##==================================
# what this does is look specifically for each line with switch with tabs more than 2
# and adds a new line above the switch moving the switch line down 1
# now actually since every line is moved down one from that point
# the next switch that a line is added above means it moved down 2 and not 1
# and so on and so forth

##====================================================
##  scan_thru_string_at_top_for_exps(stringname):
##====================================================
def scan_thru_string_at_top_for_exps(stringname):
	#print(" ====scan_thru_string_at_top_for_exps(stringname): ==:::::===")
	mystring=''
	if "exp =" in stringname: #tests if exp = in string presumably at the top
		for line in stringname.splitlines():
			if "exp =" in line:
				#so concat and build new stirng
				fixedline = line.replace("exp =","exp=") #looks for exp = changes to exp=
				mystring += fixedline + "\n"
			else:
				mystring += line + "\n"
		soclever[0] = mystring
	else:
		soclever[0]= stringname



resultstring=[]
resultstring.append(0)
samplelist=[]
##=========================================================================
##  take_input_vars_for_switches_convert_to_list(switch_input_vars):
##=========================================================================
def take_input_vars_for_switches_convert_to_list(switch_input_vars):
	mystacktrace("take_input_vars_for_switches_convert_to_list(switch_input_vars):")
	mytest_list = switch_input_vars.split(",") #split at commas put into a list 
	counter =0
	#print("look in mytest_list now", mytest_list)
	#print("=========what the hell is in this list=========================================")
	for item in mytest_list: #loops thru list made from switch_input_vars string split up
		#this says look at the first char in this item
		if item[0].startswith(' ') == False: #meaning if var doesn't start with space
			answer = mytest_list[counter]
			answer = " " + answer             #adding one space to front of var for uniformity
			mytest_list[counter] = answer     #force feed the change
			counter += 1
		else:
			counter += 1
			
	#######==================================================================	
	counter=0 
	#chop off from before and including =
	for item in mytest_list: #now this takes out the front part with exp=f from '='
		txt = item
		x = txt.split('=')
		y = x[1]
		#print(y)
		mytest_list[counter] = y
		counter += 1
	##=======================================
	#take out spaces on both sides of string 
	#cut off first char and last char
	#feed each word into list myhtest_list
	counter =0
	for item in mytest_list:            #print("now mytest_list=",mytest_list)
		string = item
		string = string.strip()         #takes out spaces before and after string
		string = string[1:-1]           #cuts off first and last char whatever it may be 
		mytest_list[counter] = string   #puts string into mytest_list[counter]
		counter += 1
	
	#print("show samplelist starting here=",samplelist)
	for item in mytest_list:
		samplelist.append(item)  #fills samplelist which is used to feed into adding
	#print("at this point the contesnts of samplelist ??")
	
	

##==================================================
##  add_exp_var_above_each_switch(stringname):
##==================================================
def add_exp_var_above_each_switch(stringname): #from samplelist
	mystacktrace("add_exp_var_above_each_switch(stringname):")
	manage_exps_prepare_for_processing(stringname)
	cool = relay[0]
	samplelist.clear() #new here 
	take_input_vars_for_switches_convert_to_list(cool) 
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =1
	#loop_thru_the_string(stringname)
	#print("inside of add_exp_var_above_each_switch(stringname)")
	#print("samplelist=",samplelist)
	print("look right F'n here for the problem====@@@@@@@@@@@@@")
	print("samplelist=",samplelist)
	for line in stringname.splitlines():
		tabcount = line.count("\t")
		if "switch(exp)" in line and tabcount > 2:  #if a line with switch(exp)at 3 or greater in it
			tabcount = line.count("\t")
			###========================================================
			#here the sameplelist contains just the number or word after the exp=
			
			word = samplelist[mycounter]          
			tabs = tabcount * '\t'                
			##========================
			if word[-1] == "'": #this says: if last char in word = '
				word= word[:-1] #cuts off last char of word
			else:
				pass
			##===========================
			adding_exp = "exp='" + str(word) + "'"   #this is the word after exp=
			#this is adding the exp='word' to line and putting switch on next line
			codeking += tabs + adding_exp + '\n' + line + '\n'
			mycounter += 1
		else:
			codeking += line  + '\n'
	resultstring[0]=  codeking
	
		

##==============================================
## show_list_resultstring_to_verify_output():
##==============================================
def show_list_resultstring_to_verify_output():
	mystacktrace("show_list_resultstring_to_verify_output():")
	
	

##======================================
##   take_out_first_line():
##======================================
def take_out_first_line():
	mystacktrace("take_out_first_line():")
	morebuilding=''
	#this is right::: it must be -1 for setting the counter
	counter = -1  #note this is now -1 it was 0 previously but first case was getting cut out
	for line in serious[0].splitlines():
		if counter == 1:
			pass
			counter += 1
		else:
			#print(line)
			morebuilding += line + "\n"
			counter += 1
	
	serious[0]= morebuilding
	morebuilding=''


#sniffer to detect exp= above first switch
#and if so then call the transform method otherwise don't call tranform method
#===========  designed on Friday, February 25th, 2022 ==== 10:17 am ===
if_exps_at_top=[]
if_exps_at_top.append(0)
##======================================================
## determine_if_exps_above_first_switch(stringname):
##======================================================	
def determine_if_exps_above_first_switch(stringname): #sniffer
	#print("=@@@@===determine_if_exps_above_first_switch(stringname): ===@@@@==")
	if_exps_at_top[0] = 'False' ;#sets default setting of if_exps_at_top[0] to 'False'
	counter =0; endpoint =''; #line number of first switch// also clears it out as reset here
	#get location of first switch( at tab depth 1 )	
	for line in stringname.splitlines():
		tabsdepth = line.count("\t")#how do I say if exp= above first switch
		if "\tswitch(" in line and tabsdepth == 1:
			endpoint = counter #sets endpoint to counter
			#print("endpoint =",endpoint)
			break
		else:
			counter += 1
	#this looks to determine if exp= ABOVE first switch at 1 tab depth
	counter =0  #the endpoint constant is the line number of the first switch at tab depth 1
	#print("endpoint line number with first switch at 1 tab depth =",endpoint)
	for line in stringname.splitlines():
	#I can change it if exp = change to exp= #work on it
		if "\texp=" in line and counter < endpoint: #this is gleaned above
			if_exps_at_top[0] = 'True'; #sets if_exps_at_top[0] to 'True'
			#print('right here if_exps_at_top[0] should = True')
			break  #the moment this is True end this loop obviously
		else:
			counter += 1


##==========================================================================
## take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
##==========================================================================
def take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
	#print("==== take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):==")
	samplelist=[]
	samplelist.clear() #new
	mytest_list=[]
	mytest_list.clear() #new
	relay[0]=''
	loop_thru_the_string(stringname)
	detect_input_exps_above_first_switch(stringname)
	add_exp_var_above_each_switch(stringname)
	show_list_resultstring_to_verify_output()
	gauge[0]=resultstring[0];trouble = gauge[0]
	remove_exps_at_top_now(trouble)
	take_out_first_line() 
	answer =serious[0]
	#for line in answer.splitlines():
	#	print(line)
	return answer #resulting concatted string
	guage[0]='';resultstring[0]='';trouble='';serious[0]='';answer='';samplelist=[]
	


finaloutput=[]
finaloutput.append(0)	
##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser(stringname):
	#print("===is this even called ==")
	scan_thru_string_at_top_for_exps(stringname)
	#HERE 
	stringname = soclever[0] #now this should fix it
	determine_if_exps_above_first_switch(stringname) #sets if_exps_at_top[0] to True or False
	#if exp at top then use them otherwise skip
	outputis=''
	if if_exps_at_top[0] == 'True':
		print("==exps at top True=>>>>>>>>>=")
		outputis=take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname)
		finaloutput[0] = outputis
		loop_thru_the_string(outputis)
	
	else:
		print("this switch string doesn't have exps at the top")
		loop_thru_the_string(stringname)
		#pass

#question is the output from this put back into stringname 
#if not then that is what I need to do next
# saturday morning coding fixing bugs and testing marathon		

##================================
##  prepare_string(stringname):
##=================================
def prepare_string(stringname):
	transform_nested_switch_string_for_parser(stringname)
	
	


##====================
## do_last():
##====================
def do_last():
    print("====== do_last() called ...time 8;47....")
    print("LOOK HERE NOW::: let's see what the output string looks like.")
    #for line in finaloutput[0].splitlines():
    #    print(line)

    super="radical='''\n" + str(finaloutput[0]) + "'''"
    print("===result is this below here====")
    for line in super.splitlines():
        print(line)
    fossil[0] = super
    print('inside of snowday we have this in fossil with radical=')
    for line in fossil[0].splitlines():
        print(line)
    
#so output is in super


##============================
## too_smart()
##============================
def too_smart(astring):
    print("=====too_smart() called===time 8;47am ==input string is goldfish==")
    prepare_string(astring)  #testing goldfish input string here 
    do_last()
   
    

#exit()
   
#too_smart(z)
#prepare_string(z) #this should work now I hope
#courage = fossil[0] #finaloutput[0]
#two_choices(courage) 

#prepare_string(z) #this should work now I hope
      
#exit()





friday, feb 25th, 2022
added sniffer to detect if exps vars above first switch for trigger to 
cut them out and add them above each nested switch below.


#===========  designed on Friday, February 25th, 2022 ==== 10:17 am ===
if_exps_at_top=[]
if_exps_at_top.append(0)
##======================================================
## determine_if_exps_above_first_switch(stringname):
##======================================================	
def determine_if_exps_above_first_switch(stringname): #sniffer
	print("=@@@@===determine_if_exps_above_first_switch(stringname): ===@@@@==")
	if_exps_at_top[0] = 'False' #by default setting
	#get location of first switch( at tab depth 1 and know look before that line number
	counter =0
	endpoint ='' #line number of first switch// also clears it out as reset here
	print("=====starting first loop here ====")
	#this determines the line number of the first switch at 1 tab depth
	print("let us see what the input string actually looks like at this stage")
	for line in stringname.splitlines():
		print(line)
	print("=====****=======********========*******=======")	
	for line in stringname.splitlines():
		tabsdepth = line.count("\t")#how do I say if exp= above first switch
		if "\tswitch(" in line and tabsdepth == 1:
			print(line)
			endpoint = counter
			print("endpoint =",endpoint)
			break
		else:
			counter += 1
	#this looks to determine if exp= ABOVE first switch at 1 tab depth
	print("====stating second loop here====")
	counter =0  #the endpoint constant is the line number of the first switch at tab depth 1
	print("enpoint line number with first switch at 1 tab depth =",endpoint)
	for line in stringname.splitlines():
		if "\texp=" in line and counter < endpoint: #this is gleaned above
			print(line)
			if_exps_at_top[0] = 'True'
			print('right here if_exps_at_top[0] should = True')
			break  #the moment this is True end this loop obviously
		else:
			counter += 1
	#loop finished here
	print("at this point it  has =====", if_exps_at_top[0])
	
	
	#continue is implicit obviously


##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser(stringname):
	for line in stringname.splitlines():
		print(line)
	print(" === transform_nested_switch_string_for_parser(stringname): called ===")
	print("modified to detect if exps vars above first switch") 
	determine_if_exps_above_first_switch(stringname) #result in if_exps_at_top[0] True or False
	print("sniff if exps above first switch")
	print("result of sniff =",if_exps_at_top[0])
	print("-----------------------------------------")
	#this boolean is determined from running determine_if_exps_above_first_switch(stringname)
	if if_exps_at_top[0] == 'True': #exps above first switch then proceed
		print("THIS HAS BEEN TRIGGERED BECAUSE EXPS = TRUE")
		loop_thru_the_string(stringname)
		detect_input_exps_above_first_switch(stringname)
		add_exp_var_above_each_switch(stringname)
		show_list_resultstring_to_verify_output()
		gauge[0]=resultstring[0];trouble = gauge[0]
		remove_exps_at_top_now(trouble)
		take_out_first_line()  # I think it's mistakenly taking out wrong line
	
	else:
		
		print("if_exps_at_top[0] == 'False' ",if_exps_at_top[0])
		print("This switch case does not have exps at the top")
		print("if_exps_at_top[0] = False",if_exps_at_top[0])
		print("therefore not going to add nonexistent exps to nested switches")
	

transform_nested_switch_string_for_parser(inputstring)  





thursday feb 24th 2022  10:07 AM PST
In respect for C and C++ having vars at the top of the first switch in a nested switch
(the nested switch input vars) are now inserted automatically so the nested switches work correctly.

cleaned up code in snowday.py which preprocesses for nested switches
and scans the exp vars at top of the first switch designed to look and feel like C
and then adds the exp vars above each nested switch (line above) in sequential order.
Code totally cleaned up and efficient.

Next I will add it the TREX.py module so it will automatically
be called 

transform_nested_switch_string_for_parser(stringname)
#again it adds the exp='varname' above each nested switch and then makes nested switches work


Wed Feb 23rd 2022 9;32 AM PST 
progress.
https://www.youtube.com/watch?v=icgGyR3iusU  trance coding music

I can translate this now for input
elcapitan='''
	exp= '9';
	exp='orange';
	exp='purple';
	
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
			
			switch(exp)   
				case 'red':
					print("this is red we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("this is blue we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				case 'orange':
					print("this is orange saturday morning coding== ")
					print("figuring out where to apply next...")
					break
				default:
					print('this is default this was missing')
					print(' darn it')
			endswitch
			
			switch(exp)   
				case 'green':
					print("this is  green  now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("this is purple panama canal 3 levels ====")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this is lower def ault this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''	
Correctly transforms into this string now:
'''	
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
			
			exp='orange'
			switch(exp){
				case 'red':
					print("this is red we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("this is blue we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				case 'orange':
					print("orange orange orange orange orange this is orange saturday morning coding== ")
					print("figuring out where to apply next...")
					break
				default:
					print('this is default this was missing')
					print(' darn it')
			endswitch
			
			exp='purple'
			switch(exp){
				case 'green':
					print("this is  green  now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("purple purple purple purple ==== is purple panama canal 3 levels ====")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this is lower def ault this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''
print("THIS IS second attempt elcapitan test ======")
num = 9   
#main_control_sequencer(num,elcapitan)#
for line in elcapitan235.splitlines():  #was elcapitan2
    print(line)
feedinput(num)
two_choices(elcapitan235)

======  OUTPUT  =====
two !
cold tennis
who will win? 
orange orange orange orange orange this is orange saturday morning coding== 
figuring out where to apply next...
purple purple purple purple ==== is purple panama canal 3 levels ====
needs 4 lanes have printeded...
=========

		


saturday, feb 19th, 2022 10:52 am
code is flowing nicely
This is nearly working now.

elcapitan='''
	exp= '8';
	exp='red';
	exp='green';
	
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
			
			switch(exp)   
				case 'red':
					print("this is red we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("this is blue we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				case 'orange':
					print("this is orange saturday morning coding== ")
					print("figuring out where to apply next...")
					break
				default:
					print('this is default this was missing')
					print(' darn it')
			endswitch
			
			switch(exp)   
				case 'green':
					print("this is  green  now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("this is purple panama canal 3 levels ====")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this is lower def ault this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''	




friday, feb 18th, 2022 8:36 am
New implimentation works 

resultstring=[]
resultstring.append(0)

samplelist=[]
samplelist.append('red')
samplelist.append('green')
def add_line_to_string(stringname):  
	print("======add_line_to_string======")
	print("starting input string")
	for line in stringname.splitlines():
		print(line)
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =0
	for line in stringname.splitlines():
		tabcount = line.count("\t")
		#this is THIS LINE we are talking about =====
		if "switch(exp)" in line and tabcount > 2:
			#so we are adding the exp='word'  above the switch line
			print("mycounter =",mycounter)
			tabcount = line.count("\t")
			print('tabcount=',tabcount)
			word = samplelist[mycounter]
			print("word=",word)
			tabs = tabcount * '\t'  #multiplies the tabcount by tab symbol stored in tabs creating a string of tabs
			print('tabs=',tabs)
			adding_exp = "exp='" + str(word) + "'"
			codeking += tabs + adding_exp + '\n' + line + '\n' #this cleverly puts it on the line above the switch line
			mycounter += 1
			
		else:
			codeking += line  + '\n'
			#mycounter += 1
			
		
	print('AFTER INSERTING BLANK LINE ABOVE where inner switch line was what does the reuslt look like is there an empty line above switch(exp)')
	for line in codeking.splitlines():
		print(line)
	resultstring[0]=  codeking
	
	newcounter=0
	print("LOOK HERE FOR aCTUAL switch lines now ====::::::====")
	for line in codeking.splitlines():
		if "switch(exp)" in line:
			print("SWITCH in this line", newcounter)
			
			newcounter += 1
		else:
			newcounter +=1
	
	print("what can see now")       
	
	

add_line_to_string(elcapitan)  #verified works becomes codeking string


#exp1= 8, exp2='blue', exp3='green'
#it will skip the first switch(exp)
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
			
			switch(exp)   
				case 'red':
					print("we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			
			switch(exp)   
				case 'green':
					print("the green room now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("panama canal 3 levels ")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''	

is converted to this output to become the new input string modified
AFTER INSERTING BLANK LINE ABOVE where inner switch line was what does the reuslt look like is there an empty line above switch(exp)
Bear in mind that the first starting switch is fed exp separately so is skipped in implimentation.
Now I need to do the top part in the line below that is the input which just reads the line. Another victory.
Each new stage gets closer to the NATURAL look and feel of C for a switch case. 
exp1 = 8, exp2 = 'red', exp3 = 'green'
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
			
			exp='1'
			switch(exp)   
				case 'red':
					print("we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			
			exp='2'
			switch(exp)   
				case 'green':
					print("the green room now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("panama canal 3 levels ")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}

generated with red and green and instead of switch it will be a nested_switch(exp) function triggered
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
			
			exp='red'
			switch(exp)   
				case 'red':
					print("we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			
			exp='green'
			switch(exp)   
				case 'green':
					print("the green room now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("panama canal 3 levels ")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
	
thursday, feb 17th, 2022  3:10pm
I figured out how I will impliment the var exp expressions at the top of a nested switch
I am in the process of making this phase reality now.



Wednesday, Feb 16th, 2022 12:28pm PST
Single switches and nested switches now work inside of functions.


def an_internal_test():
	print("====an_internal_test()===!!!==")
	clever('gone fishing')
	swu2 = '''
	switch(exp) {
		case 'rasberries and cream':  
			print("==where's the cream house!")
			print("===tastes good====")
			varholder[0]= "Tahoe Cabin in BLIZZARD"
			print(varholder[0])
			break
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche GT...")
			varholder[0]= "Porsche GT sounds nice"
			print(varholder[0])
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
	''' #this calls the internal switch case 
	two_choices(swu2) #this will say endswitch(swu2)
	print(varholder[0])
	
	
an_internal_test()




def a_second_internal_test():
	print("====a_second_internal_test()==nested switch test=!!!==")
	num = 12   
	feedinput(num)
	red_robin4_brain ='''
	switch(exp){  
		case 1 thru 6: 
			print("====zebra black and white =====")
			print("====   zebra   =====")
			print("===    tahoe summiting    ======")
			print("sitting at starbucks analzying my code")
			varholder[0]= "tahoe is now in reach"
			break
			#it should stop here
		case 7 to 10:
			print("Lex Fridman MIT UFO investigations=== ")
			print('driving up to Tahoe on highway 80  !')
			print(" driving through snow ")
			varholder[0]= "driving up to Tahoe on highway 80"
			
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
	two_choices(red_robin4_brain) #this will be endswitch(stringname)
	print("bottom of the same function")
	print("now at the bottom of the Drake Equation")

print("testing nested switch switch in a function=====>>>>>")
def alien_civilization():
	varholder[0]=''
	print("testing alien civilization nested switch")
	a_second_internal_test()
	print("varholder[0]=",varholder[0])	
	
alien_civilization()



MOnday, Feb 14th, 2022
All switches - single and nested - running from same one method currently called two_choices()
which will become endswitch(stringname).

code music the moment switch ran inside of a function
https://www.youtube.com/watch?v=wAObbLeRIEQ
	
Just ran a single switch inside of a function.
Will now test running a nested switch inside of a function.

###################################################
###################################################
def an_internal_test():
	print("====an_internal_test()===!!!==")
	clever('gone fishing')
	swu2 = '''
	switch(exp) {
		case 'rasberries and cream':  
			print("==where's the cream house!")
			print("===tastes good====")
			varholder[0]= "Tahoe Cabin in BLIZZARD"
			print(varholder[0])
			break
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche GT...")
			varholder[0]= "Porsche GT sounds nice"
			print(varholder[0])
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
	''' #this calls the internal switch case 
	two_choices(swu2) #this will say endswitch(swu2)
	print(varholder[0])
	
	
an_internal_test()

##==========================================================================
NOTE: the implimentation of the switch case is completely dependent on tabs
which is necessary for the whole thing to work. So I have Text Display > Show Invisibles
in BBEdit to see the triangles representing the triangles for indentation.
##==========================================================================
::OUTPUT::
==at the very bottom now ====testing single switch inside of a function now ======
====an_internal_test()===!!!==
clever() on line 276
two_choices called 
=====make it so right now=====count_switches_in_inputstring called===feb 12th=====
this section uses the tab count to detect at least ONE inner switch at 3 tabs
tab test nested = False
verified NESTED SWITCH = False
==cool_endswitch() called =SILVER CODE ENDSWITCH===line 10017==
varholder[0]= gone fishing

varholder[0] = gone fishing
['gone fishing']

the input exp in clever was::  gone fishing
we are inside of switch now gone fishing
case = gone fishing
fallen leaf lake
we are inside of switch now driving car
case = driving car
where is the gti
really a porsche GT...
Porsche GT sounds nice
clearit()
a list
['starter']
Porsche GT sounds nice

============ FEB 14th Monday 9:38 AM ================
Working on bug with nested switch.
The parser is moving the break from it's position to after a case block that has nested switches.
Looking at the output code generation the break is AFTER where it should be below nested switches.
So it's a logic error so I will investigate it further.

##===========================================================================

Sun Feb 13, 2022 12:46 pm 
https://www.youtube.com/watch?v=TsTFVdcpLrE&list=RDveHqJSC-9Lo&index=10
I made a method to allow C style comments within the switch case code input
like this  in file commenting.py
/*
comment
comment
comment
*/

// and like this

#but you can't put /* inside of code */ that has actual code on each side; can only add side comment after on right
It replaces the block of code with # on the left side of each line


switch engine for python files for beta2
#================================
mocha.py
running_switch_case_engine.py
trex.py
official_switch_case_silver.py



Just tested newest code in Sublime Text 3 and it runs no bugs and hella fast.
I still need to do some refactoring and will cut out half of the code soon.

Figured out bug fixed it. 12:40pm Sun Feb 13, 2022
Grateful but definitely lucky through perseverance.

Found bug ( I had two conditions to determine if nested. reduced it to 1 which is if tab depth of as switch
is 3 then it's nested.
while processing elcapitan string detected that the fuzzy logic needs to be modified and I wasn't using two_choices method
	   
because it mistakenly thought that the nested switch was a single switch to fixing that now.
time 12:27pm Feb 13th, 2022  This proves the importance of continuous testing and print statements.


Feb 13th, 2022
SOLVED THE BUG - it works as designed PURE ECSTACY. WHAT A HIGH. High as a kite.
Wow. Sucker works. 

Right now it says two_choices(stringname) and I will change that to endswitch(stringname) next.
I am so thrilled that I solved it. Just fired up Visual Studio Code but realized I just needed to try what
should work and it worked. I was swapping methods around and it just messed it up and then I realized that
I need to add the key fork function in a separate file with the imported files and then import that one file
which is mocah.py and it worked - as if it was destined to work. I am speechless with happiness right now.

I will trigger this method to be done automatically next.
Right now it's forced fed with nestedswitch('True') before the function and that can be triggered
once it detects if it's either nested or not thru the endswitch beginning methods.




Feb 12th 2022 12:32 just got endswitch(stringname) to manage single and nested switches.
For testing it looks like this in alpha form.
So this means that I can use one method to call both single and nested strings and it just started working
This is a relief because it was a pain. Currently def two_choices(mystring): is in the running code file
and I will create a third import file next to put it into.
The good news is I finally solved the conflict of what was where and what was being called and when.


##  two_choices(mystring ##
####======== two_choices(mystring):============
def two_choices(mystring):  #this will become endswitch(mystring)
	print("==this is TWO_CHOICES testing this sucker===")
	nested =count_switches_in_inputstring(mystring)
	print("nested =",nested)
	if nested == True:
		smart_endswitch(mystring)  #nested switch is in trex module
	else:
		cool_endswitch(mystring)   #single switch is in silver module
	
	
	
##=============================================
##  count_switches_in_inputstring(thestring)
##=============================================
## modified on feb 12th 2022 at 9am
#  two conditional tests switch at 3 tabs and switchcount to verify a nested switch
def count_switches_in_inputstring(thestring):
	print("=====make it so right now=====count_switches_in_inputstring called===feb 12th=====")
	number_of_switches ='';number_of_endswitches=''
	number_of_switches =thestring.count("switch")
	#just remembered need to count if a switch at three tabs
	####################################
	print("this section uses the tab count to detect at least ONE inner switch at 3 tabs")
	nestedswitch= False #by default setting starting out
	for line in thestring.splitlines():
		print(line)
		tabcount = line.count("\t")
		if "switch" in line and tabcount == 3:
			print(line) #since seeing is believing
			print("this is by definition has a nested switch = TRUE")
			nestedswitch= True
			break
	if nestedswitch == True:
		print('tab test nested = True')
	else:
		print('tab test nested = False')
	###########################################=       
	number_of_endswitches=thestring.count("endswitch")
	print("extra counts this many switch(s) in  string",number_of_switches)
	print("extra counts this many endswitch(s) in  string",number_of_endswitches)
	if number_of_switches > 2 and number_of_endswitches > 1:
		switch_count_test= True
		print("yes it is a multi switch")
	else:
		print("nope just a single switcharoo")
		switch_count_test= False
	print("the result of second condition = ",switch_count_test)
	print("===at the bottom we determine with two conditions if Nested Switch===")
	#this is testing two conditions tab depth switch at 3 and switch count
	if nestedswitch == True and switch_count_test == True:
		print("verified NESTED SWITCH = True")
		return True
	else:
		print("verified NESTED SWITCH = False")
		return False
	#############################################
	

	
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




num = 1
feedinput(num) #puts num into dino[0] for testing purposes only
#this will just take in as input the string now not num,red_robin

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
two_choices(red_robin)

#smart_endswitch(red_robin)  #NESTEd in TREX



	

Feb 8th, 2022
Just got on-the-fly C comment changer to work in one pass. It has smart tabs so that
it places the comments at the tab depth that they were created to mirror the intent of the developer.
Of course this is for code inside of a doctstring.
#the goal is being able to copy and paste JavaScript code in and just have it run


fishyone2 ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\")
			print('nimitz')
			print("==area 51==")
			//testing this out

		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			/*
			c style comment her mult-line
			more comments here
			*/
		
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



razzle ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\")
			print('nimitz')
			print("==area 51==")
			//testing this out
			//this is so true 
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			/*
			fudge this is not fair
			way to go make it work
			right now on time
			*/
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		/*
		still testing this out
		to see how it works
		*/
		default:
			print('no results')
			print("that is all")
			break
			// some comments here for fun
}
'''

#the idea is go thru once actually
#the rule is if within /*  and */ then can't have // inside of it
def on_the_fly_comment_changer(stringname):
	print("==BIG CHANGE NOW=====on_the_fly_comment_changer()===big flies====")
	smarttabs=''
	buildstring=''
	series_comment= False  
	smarttabs='' 
	for line in stringname.splitlines():
		###=================================================================
		#checks if // in line  this chnages it into #
		if "//" in line: #presuming /* and */ are not in this line
			buildstring += line.replace("//", "#") + "\n" #for a single line obviously
		###=================================================================
		#checks if /* in line and changes it to # and sets series_comment to True
		if "/*" in line and "*/" not in line and "//" not in line and series_comment == False:
			series_comment = True  #notice set flag to True here 
			tabcount = line.count("\t")
			smarttabs = tabcount #this is new
			print('smarttabs=',smarttabs)
			buildstring += line.replace("/*", "#") + "\n" #top brilliant 
		###=================================================================
		#checks if */ in line and series_comment == True this puts # at front of line 
		if "*/" not in line and "/*" not in line and "//" not in line and series_comment == True:
			line = line.strip()
			#this is where it's putting in three tabs
			tabresult = smarttabs * '\t'
			aline = tabresult + "#" + line + '\n'  #the issue is 3 tabs by default
			buildstring += aline
		###=================================================================
		#check if line starts with */ which is closing multiline comment 
		# this puts # at the front of the line and sets flag back to False
		#THIS IS FOR ENDING MULTILINE COMMENT 
		if "*/" in line and series_comment == True:
			series_comment= False #this is where and when I set it to False here we set the flag back to False
			buildstring += line.replace("*/", "#") + "\n" 

		if series_comment == False and "//" not in line and "/*" not in line and "*/" not in line:
			#print(line)
			buildstring +=  line + "\n";

	print("cat bird time let's see what the resulting concatted string looks like now") 

	for line in buildstring.splitlines():
		print(line)
    ##################################
==OUTPUT GENERATED==   
this is the on-the-fly test
==BIG CHANGE NOW=====on_the_fly_comment_changer()===big flies====
smarttabs= 3
cat bird time let's see what the resulting concatted string looks like now

	switch(exp) {
		case 'ufos':  
			print("ww2!")
			print('nimitz')
			print("==area 51==")
			#testing this out

		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			#
			#c style comment her mult-line
			#more comments here
			#
		
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		default:
			print('no results')
			print("that is all")
			break
}
==BIG CHANGE NOW=====on_the_fly_comment_changer()===big flies====
smarttabs= 3
smarttabs= 2
cat bird time let's see what the resulting concatted string looks like now

	switch(exp) {
		case 'ufos':  
			print("ww2!")
			print('nimitz')
			print("==area 51==")
			#testing this out
			#this is so true 
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			#
			#fudge this is not fair
			#way to go make it work
			#right now on time
			#
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		#
		#still testing this out
		#to see how it works
		#
		default:
			print('no results')
			print("that is all")
			break
			# some comments here for fun
}

	

Feb 6th 2022
working on allowing C style comments // and /*  */ multiline
Works. Now refactoring the code. 


Demonstration beta of macros when,unless, until showing it's possible to add
macros and further exploration of adding more expressiveness to python to speed
up programming and increase comprehension. to avoid an uproar I showed restrating and
didn't use these macros in the implimentation of my switch case module because I didn't
want to cause any dicontent and outrage. 

https://github.com/blakesouthwood/Santa_Cruz_Python_Preprocessor/blob/master/macros_playing.py
	


Feb 4th 2022 8:40 am PST Morgan Hill, California
https://www.youtube.com/watch?v=HEe3xfWfkG8&list=RDMM&index=9
::IMPORTANT ANNOUNCEMENT::
https://www.youtube.com/watch?v=XWnEj9YwKVY&list=RDMM&index=12
Note: Just tested it in Sublime Text 3  Build 4126   it runs.
	
files:
running_switch_case_engine.py
trex.py
official_switch_case_silver.py

				
This is the beta but it's stable now and I will now clean it up and finish the last steps to make it presentable.
This is mind blowing.
https://www.youtube.com/watch?v=4Lv5Ag5hR98
I imported the single switch engine into the file that has the nested engine imported.
Now I can "suddenly" run nested and single switches. Previously singles worked fine. Then I ran some nested
that ran fine and then afterwards a single switch and it crashed.
So I tried importing the single switch engine and it works!!!!!!

The bug from hell is solved!!!!

IT WORKS!!!!!!!!!!!!!!!!
I can run both nested and single switches anywhere. What a rush. Pure nirvana.
https://www.youtube.com/watch?v=gGdGFtwCNBE&list=RDMM&index=5
	
	

Feb  3rd 2022
Since single switch works in it's module and nested switch works in it's module I will do a diff
to determine what subtle differences exist so that I can integrate them together so that they work flawlessly.
Currently each time I combine them they fail so this way I will know how to make them coexist together
to reduce the codebase.
Uploading the working single switch engine and the nested switch engine. 


Feb 2nd, 2022, 10:35 am PST Morgan Hill Starbucks on Cochrane California
Massive progress, massive momentum,tenacity, perseverance, fortitude, unstoppable.

This is a pretty song.
https://www.youtube.com/watch?v=WM7-PYtXtJM&list=RDMM&index=27
	
Merged single and nested nesteed switches together. Integrating the endswitch method to determine if nested or not
and call single switch or the bypass205. Have to go to work now so have to stop right now but added all of the code
but haven't tested it. Will figure out any issues(bugs) in this configuration since it will finally
be based on the original design of an endswitch(name) at bottom of a string and determine if it's nesteed or not
and parse it correctly. Still cleaning up the code and will likely do some refactoring. Exciting that the nested
switch functions actually work (mind boggling complexity) and single switch works. they will run independently.
What is cool is that I have proved that I can add the behavior and syntax from another programming language JavaScript, C
to Python (which is an illusion really) but it actually works. I can now impliment goto label and add macros from Lisp
when, unless, until, etc (they already work by the way)

Feeling good.
https://www.youtube.com/watch?v=xat1GVnl8-k&list=RDMM&index=21

https://www.youtube.com/watch?v=CC5ca6Hsb2Q&list=RDMM&index=22

https://www.youtube.com/watch?v=_ovdm2yX4MA&list=RDMM&index=34
	


bug when I do a single switch after a nested switch crashes so working on solving that.
time 10:29am feb 1st, 2022

https://www.youtube.com/watch?v=wAObbLeRIEQ
	
Feb 1st, 2022 Neo class
I can at will run a single switch caseand a nested switch case togethe in a sequence  in the same file.
My sensor fuzzy logic works. So I am now running single switches and nested switches in the same file.
Pure nirvana. This morning I hoped but i wondered if it would work. I made a flag and next I will add
my code to determine if it's a nested or single switch. Quite thrilling actually.




Feb 1st, 2022 8:06am
Working on getting single switch and nested switch to work together independently in same file today.



January 31st, 2022 time 5:17pm 
Took out a great deal of the print statements.
uploaded lastest files:  make_it_so.py and site_b.py (the nested switch module)
	
doing many nested switches test. 20 just worked. 

25 nested switches in a row worked. in BBEDit
result of the seconds it took to run is..
--- 3.1333439350128174 seconds ---

In sublime TExt 3  doing 25 nested switches in a row (sequence)
result of the seconds it took to run is..
--- 2.941403865814209 seconds ---
[Finished in 3.0s]



January 31st, 2022 Gilroy, California time 2:42 pm PST
Trance music today: https://www.youtube.com/watch?v=TsTFVdcpLrE&list=RDzc8hbSM1zVo&index=2
		
The big news is that the module for nested switches works and doesn't need to ever reload.
Still working on refining it but it works so I essentially climbed El Capitan at Yosemite National Park in a blizzard to get it working.
That was a massive accomplishment. And any number of nested switches can be used.
If the reader is curious how this *magic* works it's just a PARSER and CODEGENERATOR (I designed and wrote both)
I did look in the blue dragon book but did it all from my design - that parses JavaScript switch cases
and converts it into python code. Each nested switch is put into a function that is the trick. The other issue is that
Python is quite militant about indentation and tabs so I hemmed and hawwed and chose to use tabs for determining
the location and count of nested switches. Each NESTED switch is indented 3 tabs. So the JavaScript/C switch case
behavior is mimicked but sadly Python actually doesn't have these REALLY COOL switch case RUNNING BEHAVIORS so
I figured out how they would work. So using sly and clever Python code the EXPECTED JAVASCRIPT/C SWITCH CASE BEHAVIORS
ARE REALIZED - though it's all an illusion. But I started thinking what else is done in C with switch case.
Macros. So I figured out how to do macros (hella tricky) but they work. I created to and thru macros to do a series
of numbers in cases. I was reading through the Yale University C style guide and the prof did tumbling math so 
I added an add() method and it can be duplicated to do multiplication and whatever else the developer wants
but I did add() for now that works like a fallthru.
The initial idea was to copy and paste JavaScript switch case code and it would work in Python. That is still the goal.
The issue is that for it to work the switch case needs to be built using tabs.

commented out overflow_manager_quail() 
and 
overflow_manager_stanford() 
not needed now.

Taking out print statements from program.
Still need to add the var exp inputs at top of switch at top (working) not implimented in this yet.
##=======================================================================================



Finally sucker works for nested any number. I just ran it in sublime text 3 it worked.
I will quickly modify it to work like the single switch case so that the programmer/developer
has endswitch(stringname) at the bottom so it's called automatically.
I was using mission_control_sequence(num,inputstring) for testing purposes only.
So just relax and chill. And I will condense the code and document it more.

I am pretty dam stubborn which helps. I feel weightless and like I'm flying through the clouds now.
I'm extremely persistent. Again I will take out the thousands of print statements and clean up the code in the next
two weeks. Happy happy, joy joy.
Why did I tackle making a JavaScript/C switch case that has macros work in Python?
Because I read that biologists were using Python and I figured they would like to have a JavaScript/C switch case to use
in Python, now they can.

January 30th, 2022 . I had a bad function messing everything up. 
#take_out_extraneous_white_spaces_on_the_left_of_each_line()
it's commented out for now. I just need to take out the print statements now.
I just tested 11 nested switches in a sequence worked.

files are make_it_so.py and site_b.py
Next I will test single switches with it intermixed with nested to see how it goes.

january 27th, 2022 9:30am
4 nested switches just ran now in a sequence
taking out print statements and cleaning up the code.
Will test this engine with single switch string next which should work
Will reduce some functions down into smaller methods to streamline it.

##===================================
##   quail_overflow_manager():  #this reduces teh quail list taking out residue from past runs
##===================================
def quail_overflow_manager():
    #print("=====quail_overflow_manager()======")
    total = len(snowtime) + 2  #snowtime is the pairs list of switch - endswitch pairs
    if len(quail) > total: 
        thecount=1
        for item in quail:   
            if thecount < total: #so does because we know it's 6 and 18 - 12 = 6 
                quail.pop(0) #delete first slot
                thecount += 1
            else:
                break 
		
#######################################################
## stanford_overflow_manager() ###### january 27th 2022  #this takes out residue from previous runs
#######################################################
def stanford_overflow_manager(): #this deletes previous data
    print("===stanford_overflow_manager()====")
    total = len(snowtime) + 2
    if len(stanford) > total: #this is a new conditional test 
        stanford.reverse() #reversing it
        thecount=1
        for item in stanford:  #this is 'loop number two' #get length based on pairs + 1 + 1
            if thecount < total:  #snowtime length = 5 + 1 for main and +1 to be more so 7
                stanford.pop(0) #delete first slot
                thecount += 1
            else:
                break #breaks out of this 'loop number two'
        stanford.reverse() #reversing it back
               
		

##=============================================================================

jan 26th 2022 7:01 pm  Will upload code within an hour
tested 3 nested switch cases (separate nested switches)
Has a bug (though works). Working on bug will but will upload it since it does technically work.
I am working on a work around for the bug currently. 

January 25th 2022 Today is a happy day! 10:58am PST Morgan Hill, California Starbucks
https://www.youtube.com/watch?v=Kt-tLuszKBA
	Guardians of the Galaxy music
	
By the way I zerod in and found thse bugs using print statements and NOT with VSC or Spyder or PyDev
Isolated 2 bugs and now infinite nested switches will work.
quail list bug had residue of previous nested switch pass
stanford list had resideue of previous nested switch pass
Put in temp fix for both bugs to ensure there were no more bugs.
Temp fix works voodoo programming fix and will replace with granite fuzzy logic.
https://www.youtube.com/watch?v=i9SznpVAack
	trance music to code effectively and achieve FLOW STATE ====
	That's the only time I am NEO and deep sea scuba diving thru the code and everything
	is crystal clear and I'm 60 feet under water.
	
Next I will work on turning on the official bypass and cutting out dead code not called and duplicate methods.
persaverance wears the crown.



Jan 24th Monday 9:25 am 2022
Looking at source of bug that is doing an overflow residue from first nested switch into second nested switch.
Using Visual Studio Code and Spyder in Anaconda.
Stepping thru the code. Need bigger screen. Dam. But at least now I can see it misbehave and 
zero on fixing it. Next two days off from work so I can solve it tuesday and wednesday. 
Everything is the process of elimination.



January 19th, 2022 8:33am PST nested module works. Cleaning it up so that I can do multipe nested switches
by clearing out the lists and vars after completing a nested switch generation.
First successful run with the module was at 3pm yesterday.

Guaridans of the Galaxy soundtrack
https://www.youtube.com/watch?v=Kt-tLuszKBA
	
	
	
Top gun opening music...
https://www.youtube.com/watch?v=5OSMqSPmfVA
	
No WAY. TOTAL SHOCK. It works.  tahoe_dream1_working_bliss.py # does nested switching
I need to add reset to it next which would empty the lists and vars.

I can call it from the bottom so I can do endswitch now.
I was thinking about it yesterday and put my first_module just above bypass205() and that did the trick.
Tested it in BBEdit, Sublime Text 3, Visual Studio Code. Works in all of them.
Uploading it. I am about to test different switch strings now. I am shaking with disbelief right now.



jan 18th, tuesday 7:30am , 2022
Taking out duplicate functions
I managed to connect stage 2 and stage 3 together successfully and about to add stage 1 directly
in front of stage 2 so that I can call the nested switch module thru a main at the bottom
simulating the endswitch()
It's been a good boxing fight. Isolated module 1 and taking out print statements right now and then will
add it  and call it directly before bypass205() in the main at the bottom of the file so it will stop crashing.


jan 16th saturday 2022 8;52 am
pinpointed bug!!! so happy



Was flailing then then had a thought and it worked.
I had a function that had to be called where it was located otherwise it wouldn't work.
I was at my wits end to solve the problem. Then I thought what if I dynamically called the function
with differnet inputs, (number or word and string name) at first with eval and then without eval.
The issue was I need to have a nested switch called with an endswitch(stringname) at the bottom
of a nested switch to trigger the nested switch code.
But whenever I moved the trigger method mission_control it wouldn't work and it got scary.
the hard coded method would only work correctly where it was and also the bypass205() nethod
is hard coded and the bottom_sequence() at the bottom.
The only change occurring when I called the module are the input number or word and the stringname.
So I realized what if I dyanmically call the mission_control method without moving it since its hardwired.
and I need to call it automatically which means it's always on. It's the trigger for the first section of the 
translation of the input switch into python code parsing and generating python and conccatting it.
This whole module will be in the background imported and everything can happen in the background but I was in  tizzy
over being able to call it multiple times. Running once it's fine. And now it should work multiple times.
More testing tomorrow.

I had hit a wall and my unconscious solved it. This is soooo awesome.

for testing I am calling it mrendswitch(string) 

##====== javascript hack trick ===
variableinput=[]
variableinput.append(0)
stringlist=[]
stringlist.append(0)
##==========================================
variableinput[0]= 1
#stringlist[0] = red_robin

#this grabs the switch string name as input  and puts it into list stringlist[0]
##=========================
def mrendswitch(string): #this would run above in the file  <<====endswitch(stringname) will be in other file
    print("=== mrendswitch called ====")    #everything in *this* file is invisible will be imported
    stringlist[0]=string
    print(stringlist[0])
    stringname =stringlist[0]

mrendswitch(red_robin) #this is called and triggeres filling the two lists
##missioncontrol is called 
#stringlist[0] =stringname #from above   THIS IS NOW DYNAMIC JAN 13, 2022 but doesn't move
anumber = variableinput[0]  #I can change the inputs with changing what is in the lists it reads
stringname=red_robin        #I will fill the lists with the endwitch call

mission_control(anumber,stringname)  #this function must stay RIGHT HERE 

#exec(sweet)
#it did say missioncontrol(1,redrobin) #this was hardcoded for testing
#===============
#what if I dynamically change it






https://www.youtube.com/watch?v=fDWFVI8PQOI&list=RDMM&start_radio=1&rv=-yOZEiHLuVU
jan 13th thursday 2022  4:39 pm PST Morgan Hill Starbucks, California
	
My code was one module and to work I need to call it from the bottom (or so I thought).
I couldn't move the mission_control() method trigger because it wouldn't work right and I didn't want to spend
two weeks refactoring all the code. Then I thought of JavaScript and thought, hey what if...
I dynamically build the called trigger method and fill it and it ran. I am blown away that it worked.
So I couldn't move the trigger method otherwise I got all kinds of list errors and nothing worked.
So I was splitting up the huge module into 4 smaller modules and I couldn't call the trigger at the bottom.
I then thought what if I dynamically fill the trigger method and. it worked. wow. Blew my mind.
SO HAPPY.So, this means I can can call the working nested switch code with an endswitch() and it should work.
endswitch is a method that holds a string which is the nested switch input
endswitch will pass the string name into a field (a list) and the input value such as 1 is in another list
above each switch. The issue is calling the switch once is fine. But it is not possible (right now) to call another one.
Now it should call any number of nested switches. Like all of my brilliance it came to me in a flash of insight just now.



jan 13th 2022  10:02 AM
seperated monster file into 4 separate modules which will be accessed by one file
and this way I can control the vars and lists and thus clear them after each run (hopefully)
which is how the single switch works.
I will make the first attempt today. I have the code in 4 parts now and I'm testing and
verifying each seperated module works independently and then I will import the output lists
from each from a main file. The point of this design change is to be able to call nested switches
any time and do many like I do with single switches. The problem was resetting it since it's a massive
file and unwieldy and I need to clear the lists and vars. So I have each module feed it's output
as input into the next module below it with the main function in the top file.
taking out all of the prints I used for debugging. I will first test and verify each separate
module still works after cutting them apart.
This will eventually be triggered by endswitch(stringname) at the bottom of a C style switch doc string.


jan 13th, 2022
Visual Studio Code debugger stepping thru code to follow it's path.

Jan 10th, 2022 3:23 pm
Designing a main for nested switches
with methods in order within it to fix bug preventing from doing many nested switches
since right now it's not currently in a true sequence. This should make it behave and work properly.
I went on a drive today and the obvious solution occurred to me . 
Just like in the single switch I use a main sequence for the complicated methodical steps.
It's so obvious to me now. I got a posterboard this morning to flow chart the sequence and that
got me thinking of a simpler and more elegant solution.


10:29 am jan 8th
testing and cutting out dead code (not called)
https://www.youtube.com/watch?v=daa9pZDxfIY  #I'm going to DisneyLand


Jan 8th, 2022 9;23 am
organzing and modularing the nested switch engine so that I can do multiple nested switch strings
in a sequence just as I can with single switches. Still speechless nested switch works.
The ordering of the mini modules is crucial to avoid having to do a reload so clearing the lists
and vars is imperative. So right now dealing with the organization of the flow of control
and cutting up sections into separate modules so I can eventually but it all into one file for simplicity
flowing top down .


just checked and both scenarios switch and nested switches work in Sublime Text.
wed jan 5, 2022 7;36 pm.
currently I can run n number of single swtiches no probs
when I run more than 1 nested switch it crashes so I am working on clearing out the vars and lists states to virgin state
just like I did (apparently properly) in the single switch scenario and I will incorporate that into the much more complex
nested switch.
The single switch is lightning fast. The nested switch has a ton of print statements which I'm quickly commenting out
to make it faster.

Also the code size will be drammatically reduced so as to reuse the same single switch parser and codegen that I am using for the single
switch scenario. I currentlly have a modified and greatly added onto parser and code gen engine for the nested switch
behavior generator. Thrilled to death that it works though. Mind blowing complexity. 

I am still in total shock it works. It was mind bending to solve it and impliment my design.
The design was the key to success.

just reviewed how I cleared out the vars and lists for the single switch which I call 15 times
in the beta demo I finished in June and now I will use the same technique for the nested switches
so that a series of nesteed switches can be used.

The nested switch is a beast for it's codegen tricks and I apprently wasn't clearling each list and var just in time
so I will work on that engineering tomorrow.

Next after that I will activate the bypass205() method so that if at least one nested switch is detected
in a switch string it will do the nested_switch scenario otherwise it will do the one switch scenario.

##====================================================

jan 5th Wednesday, 2022 5:58 pm
Uploaded starship10.py and red_flying_reindeer.py
which is beta of working nested switches. Issue I am trying to solve is
merely resetting the lists and vars so for the next nested switch stringe its
empty for all values.

mission_control(2,red_robin) #number for input of main switch and name of nested switch string


red_robin ='''
	switch(exp){  
		case 1 thru 3: 
			print("can we be more specific !")
			print('first prize')
			print('Lucy and Schroeder at the piano')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("we are  inside of sw itch 11 good show ")
					print("this is really working, fantastic...")
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do inside of sw 15")
							print("oh this is just wonderful ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake'
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("do chinquapin for tennis in summer")
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

output of running the nested switch
input to mainswitch= 2

can we be more specific !
first prize
Lucy and Schroeder at the piano
kangaroo hop hop!
we are  inside of sw itch 11 good show 
this is really working, fantastic...
do inside of sw 15
oh this is just wonderful ... really it is
nice
this is possibly sw 25
do chinquapin for tennis in summer
yep
nice kayaking race
yep
nice
we are done here
taught me how thru write code
mocha blast
== 31 flavors===
the end
outputstring= 
string_name= 
result[0] = fallen leaf lake
##========================================================
jan 4th Tuesday. 2022  8:58 am 
	
Releasing Beta in a few days of switch and nested switch module with specs and tutorial how to use.

Still trying to figure out how to get nested switch to work as a module.
I did combine the imported file to the main module is now inside of the main module so it doesn't have to be imported.
Nested switches works but hasn't been added to the regular switch as yet.
I am currently using the Spyder debugger to step thru my code to figure out why it is getting hung up in the concat stage.




Input string.
red_robin ='''
	switch(exp){  
		case 1 thru 3: 
			print("red white and blue is what we are talking about !")
			print('first prize')
			print('you bad ass coder Charlie Brown christmas')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("we are  inside of sw itch 11 good show ")
					print("this is really working, fantastic...")
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do inside of sw 15")
							print("oh this is just wonderful ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake'
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("do chinquapin for tennis in summer")
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
print('go now')


mission_control(1,red_robin)


The bug error message when trying to run the nested switch code generator

class 'int'>
what is it??
what is in the line above
inside of modern tab shifter to left we have this for n
n= 6
<class 'int'>
what is it??
what is in the line above
var pair= 
var pair= 
var pair= 
var pair= 
var pair= 
var pair= 
var pair= 
var pair= 
Traceback (most recent call last):
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/testing_nests.py", line 101, in <module>
    mission_control(1,red_robin)
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/running_reindeer.py", line 491, in mission_control
    holiday(someinput,thestring)
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/running_reindeer.py", line 478, in holiday
    phase_one_of_nested_switches_procedures(thestring) #wafffles2
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/running_reindeer.py", line 353, in phase_one_of_nested_switches_procedures
    convert_nested_switch_string_to_strings_in_quail_list(inputstring) #from starship
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2478, in convert_nested_switch_string_to_strings_in_quail_list
    waterfall_chain_methods_gold_master() 
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2382, in waterfall_chain_methods_gold_master
    do_the_blender_chain_methods()
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2355, in do_the_blender_chain_methods
    take_out_the_inner_switch_bodies_leaving_switch()  # method 2 cut out switch bodies leaving switch
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2155, in take_out_the_inner_switch_bodies_leaving_switch
    take_out_switch_body(item)
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2064, in take_out_switch_body
    build_trial_inputlist()	 #this is new 
  File "/Users/blakesouthwood/Desktop/dark_side_of_moon/little engine that could/tahoe is in reach/starship.py", line 2015, in build_trial_inputlist
    pair=[switch_list[counter],endswitch_list[counter]]
IndexError: list index out of range

	

more testing'
taking out print statements from the 30,000 lines of code.
jan 3 Monday, 2022 4:34 pm PST
I have one nested switch working and I am having trouble getting it to work when importing the file and  using a nesetd switch
and running it from the imported file.
It works fine in the same file. That's the only issue I have right now. 
With solitary switches with no nested switches that engine works fine importing the file. 
My nested switch works now but I import it and run it but it crashes at the concat stage trying to zero in on the bug.



11:09 am Fri Dec 31st, 2021 TOTALLY WORKS. PURE NIRVANA . crushed the bugs.This is the first time it ran all the way through.
I decided to reduce the test code to one main switch and one nested inner switch to reduce the problem set. Solved it.
# radical list is a copy of the quail output list in starship
# switch_numbers_to_transfer are actually the switch numbers which are the line numbers of each switch

# this list is utilized to number the switches after going thru the parser and codegen to be added as a comment
# which earlier were grabbed from the switch number comments after each switch in the quail list which is an entirely
# different animal then the stanford list. The quail list is the input string and it's various tranformations prepping
# before being fed to bypass205 where it is converted into python code. The generated python code representation of the
# switch strings is deposited into the stanford list.

from starship import *
from starship import switch_numbers_to_transfer
from starship import radical_list  

waffles ='''
	switch(exp){  
		case 1 thru 3: 
			print("to the moon Alice!")
			print('first prize')
			print('Charlie Brown and Snoopy flying against Red Baron')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp = 'blable'
			switch(exp)  
				case 'blable':
					print("we are inside of sw 11 now wildness")
					
					print("I just typed this like Snoopy")
					result[0]="snoopy"
					fallthru
				case 'more':
					print("and this fell thru from snoopy above")
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
	endswitch
'''
inputstring=''
inputstring = waffles 

print('THIS IS INSIDE OF RUDOLPH - WE IMPORTED  starship.py ')

convert_nested_switch_string_to_strings_in_quail_list(inputstring) #from starship

topvalue[0]='1'
clever_cat()

#output generated==============
input is  1
to the moon Alice!
first prize
Charlie Brown and Snoopy flying against Red Baron
kangaroo hop hop!
we are inside of sw 11 now wildness
I just typed this like Snoopy
and this fell thru from snoopy above
taught me how thru write code
mocha blast
== 31 flavors===
the end
result[0] = snoopy
 
let us see what we have here
 real_switch_numbers_to_transfer= ['1', '11']
======stop the presses=dam it======

I just need to put the methods in sequences to reduce the code more, but it .. works  ( 0  0 )
            

Starbucks WiFi is nice.
Friday, Dec 31 new year's eve, 2021 9:40 am 

on home stretch to home plate. dec 31st Friday. Working on last critical bug.
Good music capturing the moment of anticipation.
https://www.youtube.com/watch?v=TsTFVdcpLrE&list=RDsRvEwXDxz_I&index=10
	
The bug is when I run the methods that split up the input nested switch and chops it up into individual switches
and analyzes the data specifics and runs the chain methods on the individual switches to prepare them for the parser
and puts them back into the quail list it doesn't run. But my test code runs.
So paired down the 8 nested switches down to 2 switches to narrow down the scope of the bugs behavior to localize it.




wed dec 29th, 2021  11:36pm
Figured out the trick to import a file, run code in it, and fill a list from the imported resulting list.
So now I can finish rudolph file that will do everything for nested switches.
more testing tomorrow. What I did is call the starship file which splits up the nested switch string
and then runs each switch string thru the chain methods and fills the quail list. 
So that just worked. Great relief. I will have rudolph file (soon be nested_module) should be fully (finally)
working tomorrow. Greatly relieved I figured it out with trail and error.
Moving forward now.



Approaching the finish line.
Had one slight problem. I couldn't locate my single switch working code. then... I got lucky and found it
thanks to a github backup back in June I believe. This was a monumental relief because I couldn't find it amongst all of my backups.
Single switch (the originals) with switch module and test file
single_switch_core.py  and single_switch_beta_testing.py test single switch code
just uploaded both of these to github

time for music to celebrate: https://www.youtube.com/watch?v=fDWFVI8PQOI&list=RD63088Hhjexg&index=6  Rhythm is a dancer
My test does 15 single switch case strings individually using macros, numbers and UPPERCASE words and words in strings.
I will reupload them as a backup again, because they were difficult to find but I will rename them.

I will do testing of single switches and nested switches back to back and verify all is well.

##=============================


December 27th, Monday 11:57 am 2021 Menlo Park, California Santa Cruz Avenue
https://www.youtube.com/watch?v=eBG7P-K-r1Y
	
When my code works it feels like this: F16 smoke on
https://www.youtube.com/watch?v=UGDsooClz0k
		
		
Down to just two files now to make nested switches work.
I have starship which does the prepping of the input string for the parser is now in one file.
And rudolph is the nested switch engine(code name of course obviously) and they are not connected yet.
For maintenance I will likely just import Starship into Rudolph to reduce the complexity and make maintenance less
of a heartache.
Before uploading the two files to github I tested them and they both work. I was breathless when they ran perfectly.
Perseverance wears the crown.

Big rush of adrenaline when I reduced booster 1 and 2 into one file Starship. That was a pain due to dependencies.
####==================================================================
Uploaded rudolph.py and starship.py to github for safety in case my laptop dies after accidently spiling mocha all over it
in late night coding session. Still plugging away though.


Dec 23rd 2021 thursday 10:06am  Morgan Hill Starbucks 
NEO Class. BAMF
https://www.youtube.com/watch?v=TWJVgTeNljs&list=RDMM&index=9
	
I can do anything with code.

Currently playing with switch(true) but will figure it out later, no time right now
	
I have been reducing down the two last two minimodules that I am adding to the working code
1) get switch pairs and separate input strings into a list
2) chain methods converting each string for parser converting input prepped strings into python output numbered methods
3) run thru bypass205 concat output strings and execute code

Adding these two chunk to seperate input strings from initial string.
##===============================================================
##   ==this_makes_switch_and_endswitch_pairs_by_tab_levels() ====
##===============================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    #print("===THIS MAKES SWITCH AND ENDSWITCH PAIRS BY TAB LEVELS========")
    build_tab_depth(inputstring)                           #METHOD 1
    get_max_tab_number_in_list() #fills holding_themax[0]  #METHOD 2
    build_list_input_list()                                #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels()        #METHOD 4
    list_tabs_lists_by_depth()                             #METHOD 5
    combine_tabs_by_length_into_christmastree_list()       #METHOD 6 
    build_pairs_with_jazz()  #combines into sublist        #METHOD 7 
    loop_thru_pairs_in_snowtime()                          #METHOD 8
    #print("==bottom of this makes switch and endswitch pairs by tab levels()")
    #print("snowtime=",snowtime)
    #this will go into gold_list

##======================================================##=========================================
##  ==split_up_big_string_into_nested_switches(myinputstring)==
##======================================================##=========================================
def split_up_big_string_into_nested_switches(myinputstring):#this would only be called once
    #print(" ==  split_up_big_string_into_nested_switches(inputstring)  ==")
    water =add_comment_and_line_number_to_all_switches(myinputstring)               #METHOD 1
    show_switch_string_with_numbers_added_after_each_switch_with_a_comment(water)   #METHOD 2
    empty_columbia_river_list()                                                     #METHOD 3
    show_the_snowtime_list_of_pairs()                                               #METHOD 4
    add_main_switch_to_columbia_river(water)                                        #METHOD 5
    holding_string[0] = water
    loop_thru_snowtime_list_and_copy_switch_bodies_and_add_to_columbia_river()      #METHOD 6
    loop_thru_columbia_river() #prints out seperated switch bodies top down         #METHOD 7               
    ##==============
    print("the switch strings cut up are now printed out top down")
CREATES THIS:
	snowtime= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]
counter= 1

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

===========
counter= 2
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

===========
counter= 3
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

===========
counter= 4
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

===========
counter= 5
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

===========
counter= 6
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

===========
								
	
SECOND BIG PIECE testing before adding creates chain methods output and then pastes new nested methods
together and concats them
chain methods fun

#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
								
								
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
	passthis[0]= n;
	print("n =",n)



goldtime=[]
goldtime.append(0)
##===================================================================
##  modern_tab_shifter_to_left(the_nest_string):  nov 30th tested working
##  methods: starter_engine()
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
    print("I wanna see it")
    for line in buildstring.splitlines():
        print(line)
  


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
    print("=======ORANGE=====take_out_myendswitch===")
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
        chain_output_list.append(item) #ah this is where that is. 

##======================================================
## loop_thru_chain_output_list_and_fill_quail_list()
##======================================================          
def loop_thru_chain_output_list_and_fill_quail_list():
    print("here we are filling the QUAIL list officially -it's about time")
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
    print("=== end of blender chain methods() ==")    

								
								
##===================================================================================    
## ====  WATERFALL CHAIN METHODS GOLD MASTER OFFICIAL OFFICIAL OFFICAL OFFICIAL  =====       
##=====================================================================================
def waterfall_chain_methods_gold_master():  #THIS WILL TAKE IN THE QUAIL LIST FOR INPUT
    print("===WATERFALL CHAIN METHODS Gold Master 1.3()====THE REAL DEAL  REAL WORLD = ")
    print(" == Sunday, dec 12th, morgan hill starbucks 10:01 am ==")
    #loops thru testlist_of_strings
    for item in testlist_of_strings: #this displays each switch string starting out
        print(item)
        print("========")#formally apple, plum, peach, orange 
    #==chain methods called here=== 
    do_the_blender_chain_methods()
    #loop_thru_chain_output_list_and_fill_quail_list() #ultimately will need to feed quail list
    #    method above turned off for now
    show_list_switch_numbers_to_transfer()
    print("LINUS list switch_numbers_to_transfer at bottom of chain methods")
    print(switch_numbers_to_transfer)
    print(" ==end of line ... Sunday, dec 12th, morgan hill starbucks 10:07 am ==")
   
								
								
								
								
								

##===============================================================
## create_def_switch_methods_concatted_together_in_one_string()
##=============================================================
def create_def_switch_methods_concatted_together_in_one_string():
    #possibly empty stanford list here 
    print('=create_def_switch_methods_concatted_together_in_one_string()=')
    add_number_after_top_switch_into_stanford_list()#this is used to label out switches
    adding_def_methods_to_top_of_each_switch_string() #framing each python switch generated output
    stack_the_cake_combining_python_switch_methods_together()
    print("this is in snooopy_doghouse.py")
    print('output in toocool[0] ===')
    print(toocool[0])
    print("#end of big testaroo dec 9th thursday morning before 10am")
    #output is a string inside of list toocool[0]
    #fill_nested_switches_list[0]=toocool[0] ##0000000000 Modifications 
    print("dec SEVENTEENTH THIS MUST WORK ITS IMPERATIVE FOR SUCCESS THINK GTI VW this is now in fill_nested_switches_list[0] ")
    for line in fill_nested_switches_list[0].splitlines():
        print(line)
   			
After going thru chain_methods the input strings are prepped for the parser and cleaned up and shifted left.
								
								the length of stanford= 7
=-- looping thru quail ==

	switch(exp) #1
		case 1 thru 3:
			print("where's the dazzling dog house!")
			print('first prize')
			print('you block head Charlie Brown 9')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			exp = 'blable'
			nested_switch_11(exp) #11
			exp = 'burger'
			nested_switch_62(exp) #62
			##############
			print('taught me how to write code file called gold1')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
----------

	switch(exp) #11
		case 'blable':
			print("this is nested swith 11")
			####################
			exp = 'fallen leaf lake'
			nested_switch_15(exp) #15
			#############
			print("Blake testing again Southwood")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
}
----------

	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("Blake testing is nested switch 15")
			####################
			exp = 'tahoe'
			nested_switch_23(exp) #23
			#############
			break
		default:
			print("we are done here")
}
----------

	switch(exp) #23
		case 'tahoe':
			print("nested switch 23 tahoe")
			print("yep")
		case 'fallen leaf lake':
			print("blake testing here")
		####################
			nested_switch_31(exp) #31
			#############
			break
		default:
			print("we are done here")
}
----------

	switch(exp) #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'BLAKE TESTING now':
			print("nice")
			break
		default:
			print("we very done")
}
----------

	switch(exp) #62
		case 'burger':
			print("nested sw62")
			########testing ############
			a = "three"  #added this just playing around here testing 
			if a == "one":
				exp = 'snow fire'
			else:
				exp = 'Monday'
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
}
----------

	switch(exp) #66
		case 'fishy':
			print("do this is sw 66")
			print("yep")
			fallthru
		case 'snow fire':
			print("this is nested switch 66 cool")
			#############
			break
		default:
			print("we are done here no matches")
}
----------
after going thru bypass205 the input strings are now in python look like this in stanford list
						
						====looping thru Stanford as it is now===


caselist1 = ['1', '2', '3']
caselist2 = ['4', '5', '6', '7']
caselist3 = ['8', '9', '10']
caselist4 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['1', '2', '3']
		print("where's the dazzling dog house!")
		print('first prize')
		print('you block head Charlie Brown 9')
		fallthru('4')

	elif case in caselist2: # ['4', '5', '6', '7']
		print('kangaroo hop hop!')
		#############
		exp = 'blable'
		nested_switch_11(exp) #11
		exp = 'burger'
		nested_switch_62(exp) #62
		##############
		print('taught me how thru write code file called gold1')
		fallthru('8')

	elif case in caselist3: # ['8', '9', '10']
		print('mocha blast')
		print('== 31 flavors===')
		fallthru('default')

	elif case in caselist4: # ['default']
		print('the end')
		break

	else:
		print('the end')
		break




caselist1 = ['blable']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['blable']
		print("this is nested swith 11")
		####################
		exp = 'fallen leaf lake'
		nested_switch_15(exp) #15
		#############
		print("Blake testing again Southwood")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break




caselist1 = ['tahoe']
caselist2 = ['fallen leaf lake']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['tahoe']
		print("do something")
		print("yep")
		fallthru('fallen leaf lake')

	elif case in caselist2: # ['fallen leaf lake']
		print("Blake testing is nested switch 15")
		####################
		exp = 'tahoe'
		nested_switch_23(exp) #23
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break




caselist1 = ['tahoe']
caselist2 = ['fallen leaf lake']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['tahoe']
		print("nested switch 23 tahoe")
		print("yep")
		fallthru('fallen leaf lake')

	elif case in caselist2: # ['fallen leaf lake']
		print("blake testing here")
	####################
		nested_switch_31(exp) #31
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break




caselist1 = ['fishy']
caselist2 = ['blake testing now']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['fishy']
		print("do something")
		print("yep")
		fallthru('blake testing now')

	elif case in caselist2: # ['blake testing now']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we very done")
		break

	else:
		print("we very done")
		break




caselist1 = ['burger']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['burger']
		print("nested sw62")
		########testing ############
		a = "three"
		if a == "one":
			exp = 'snow fire'
		else:
			exp = 'Monday'
		nested_switch_66(exp) #66
		#############
		print("yep")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break




caselist1 = ['fishy']
caselist2 = ['snow fire']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['fishy']
		print("do this is sw 66")
		print("yep")
		fallthru('snow fire')

	elif case in caselist2: # ['snow fire']
		print("this is nested switch 66 cool")
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here no matches")
		break

	else:
		print("we are done here no matches")
		break


----------
						
then the output python strings are put into nested numbere methods in stanford list 
with main at the bottom
						def nested_switch_66(exp):	
	
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do this is sw 66")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("this is nested switch 66 cool")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here no matches")
			break
	
		else:
			print("we are done here no matches")
			break
	

-------------------
counter= 1
==========
def nested_switch_62(exp):	
	
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("nested sw62")
			########testing ############
			a = "three"
			if a == "one":
				exp = 'snow fire'
			else:
				exp = 'Monday'
			nested_switch_66(exp) #66
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

-------------------
counter= 2
==========
def nested_switch_31(exp):	
	
	caselist1 = ['fishy']
	caselist2 = ['blake testing now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('blake testing now')
	
		elif case in caselist2: # ['blake testing now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	

-------------------
counter= 3
==========
def nested_switch_23(exp):	
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("nested switch 23 tahoe")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("blake testing here")
		####################
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

-------------------
counter= 4
==========
def nested_switch_15(exp):	
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("Blake testing is nested switch 15")
			####################
			exp = 'tahoe'
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

-------------------
counter= 5
==========
def nested_switch_11(exp):	
	
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("this is nested swith 11")
			####################
			exp = 'fallen leaf lake'
			nested_switch_15(exp) #15
			#############
			print("Blake testing again Southwood")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

-------------------
counter= 6
==========


exp = varholder[0]
def main_switch(exp):	
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dazzling dog house!")
			print('first prize')
			print('you block head Charlie Brown 9')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			exp = 'blable'
			nested_switch_11(exp) #11
			exp = 'burger'
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code file called gold1')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	

-------------------
counter= 7
then they are concatted together into one string
						
this string is added on the top 
						
# =======  switch  =================================
def switch(x):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	x = str(x)
	global case
	case = x 
# =======  fallthru       =========================
def fallthru(y):
	eval("switch('" + y + "')")
#==================
#for inswitch
def inswitch(n):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	n = str(n)
	global case
	case = n 
#=====================
# for infallthru    
def infallthru(n):
	eval("inswitch('" + n + "')")

this is concatted at the bottom so it can call main
						
main_switch(varholder[0]) 
						
#then I concat it and exec(code)

###==================================
##  concat_items_in_list(x):
##===================================
def concat_items_in_list(x): #add_to_list added at top before this as input
	print('--------concat items in list(x)---------------------------')
	create_def_switch_methods_concatted_together_in_one_string() 
	print("=======the contents of fill_nestd_switches_list[0]========")
	for line in fill_nested_switches_list[0].splitlines():
		print(line)
	print("after printing out fill_nested_switches_list[0] ===>>>") 
	print("concat_items_in_list() called with input x",x)
	enter_value(x) #this is fed in from above 
	print("=====concat items in list()====")
	fireone[0]= True #when this is True it shows the code generated with print
	global superball
	print("after copying contents of fill_nested_switches_list[0] into")
	print("future_nested_switches we have...")
	future_nested_switches=fill_nested_switches_list[0]
	#===========================================================================
	superball =  method_defs + future_nested_switches + trigger + "\n"
	##==========================================================================
	superball=superball.replace("'''",'') #I think that this was the bug fix
	#===========================================================================
	print("we are printing out what superball looks like")
	print(superball)
	print("bottom underneath the pringting out of superball")
	if show_code == True:
		print(superball) #prints the generated switch code methods
	else:
		pass  #otherwise it prints nothing 
	#so at this juncture the global var superball has the combined stacked string




 
###=============================
### clever_cat()  triggers the concatting and executing of the python
### calls method: concat_items_in_list() filling superball and then executes it
###=============================
def clever_cat():
    print("====CLEVER CAT called==chesire cat test=")
    ### ==== executed here
    concat_items_in_list(topvalue[0])#this builds the concatted string superball
    print('input is ',varholder[0])
    #exit()
    #===========================
    exec(superball, globals()) #runs the switchcase
    #===========================
##################################

##=====================================
topvalue[0]='1'
clever_cat()						
						
						
						
						
						
Both big mini modules work indepently and now I am connecting them together in the same file 								
								
								
##============================================
I can now have (after testing it) input vars at top of switch case that 
are mapped to each nested switch input.
example:
	
	Nested-Switch Statement:

Nested-Switch statements refers to Switch statements inside of another Switch Statements.

Syntax:

switch(n)
{
  // code to be executed if n = 1;
  case 1: 
    
  // Nested switch
  switch(num) 
  {
    // code to be executed if num = 10
    case 10: 
      statement 1;
      break;
      
    // code to be executed if num = 20
    case 20: 
      statement 2;
      break;
      
    // code to be executed if num = 30
    case 30: 
      statement 3;
      break;
      
      // code to be executed if num 
      // doesn't match any cases
      default: 
  }
  
  
  break;
    
  // code to be executed if n = 2;
  case 2:
    statement 2;
    break;
  
  // code to be executed if n = 3;
  case 3: 
    statement 3;
    break;
  
   // code to be executed if n doesn't match any cases
   default: 
}
Example:


// Following is a simple program to demonstrate
// syntax of Nested Switch Statements.
https://www.geeksforgeeks.org/nested-switch-case/
#include <stdio.h>
  
int main()
{
    int x = 1, y = 2;  #<<========== this is what I am talking about implimenting right now, vars above switch
  
    // Outer Switch
    switch (x) {       #<<============== var x here inside of switch as param
  
    // If x == 1
    case 1:
  
        // Nested Switch
  
        switch (y) {    #<<=========== var y here inside of switch as param
  
        // If y == 2
        case 2:
            printf( "Choice is 2");
            break;
  
        // If y == 3
        case 3:
            printf( "Choice is 3");
            break;
        }
        break;
  
    // If x == 4
    case 4:
        printf( "Choice is 4");
        break;
  
    // If x == 5
    case 5:
        printf( "Choice is 5");
        break;
  
    default:
        printf( "Choice is other than 1, 2 3, 4, or 5");
        break;
    }
    return 0;
}



var1 = 'fun", var2= 'jazz', var3 = 'dino', var4 = 'trouble'
#these are put into a list in sequential order from left to right like the American number line
varholder[0] = var1
varholder[1] = var2
varholder[2] = var3
varholder[3] = var4
 
#it would be implimented after the code is generated and replace the switch(exp) based on location with varname
 
switch(exp) #1
    switch(exp) #2
    switch(exp) #3
        switch(exp) #4
#would result in generated code 
 switch(var1) #1
    switch(var2) #2
    switch(var3) #3
        switch(var4) #4
	'
#not showing code how it works not but it works but isn't implimented as yet; only testing if it would work and it does	
##===========================================================================================	
Dec 22nd, 2021 8:15 am 
testing.
I have the code for nested switches in one file module now
I am slowly hooking the pieces together.
I am testing each section independently from the running code as I gradually connect each piece together.
I have canned hard coded data that works and now I am replacing each section with the running code
by turning on each new module which are each running independently (outside realm of actual code) so in parallel,
for testing purposes for quality control.
So I am slowly cascading down works tip toeing down thru the flow of control. 

Dec 21st, 2021 8:17 am PST Morgan Hill, California

About to connect the two last pieces together.

I have been diligently testing the generated python (which works) and concatting it and executing it with exec(string)
and it works. I am speechless to have made it to this juncture. The rush is overwhelming.

I was setting the exp='word'  or exp='3' for the nested switches and have been researching how C style guide at Yale
and elsewhere describe the convention for setting vars for inputs of nested switches which is new to me so I will
incorporate that feature in a few days utilizing a list.

For nested switches the convention is apparently to set the vars for the nested switches above the entire nested switch case.
The way I was implimenting it (which will still work) is setting the vars for switch input params just above
each nested switch. 
a = '100', b = '200'
switch(a)
     switch(b)
	
Refactoring. Connecting it all together.
Trapeze act next connecting the two pieces now.

#these two sections do these behaviors representing the FIRST HALF of the mission
1 Scan thru the input nested switch string and get the switch and endswitch locations and build pairs 
predicated on the tab count and proximity of the switch and endswitch neighboring proximity.

2 Copy the switch body strings based on the switch/endswitch pairs
and put each of these switch bodies into a list

##===============================================
These two behaviors 1 and 2 now work together.

#input and output of what these two puzzle pieces do:
github messes it up so it's closer to the left margin than how it's portrayed and displayed here which is misleading..
INPUT:
'''
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
####==========================================================
#pairs list output shown here 
#numbers are pairs of switch, endswitch line numbers
snowtime= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]
counter= 1

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

===========
counter= 2
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

===========
counter= 3
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

===========
counter= 4
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

===========
counter= 5
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

===========
counter= 6
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

===========
the switch strings cut up are now printed out top down
								
The top half will fill the columbia_river list which is then fed into the quail list which runs thru bypass205()

The other half of the nested switch module is connecting this top half (above) to the rest of the nested project which takes these input strings
and runs each switch string thru the chain methods and then they are put into the quail list
and fed into bypass205() which then converts them from JavaScript into Python and finally executes the 
resulting concatted string after having converted each switch body into a unique method numbered.
        
## loops thru tabsubs and appends item to tabcount
#=========================
#  little_method(tabcount)            
#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    #print(" little_method() called")
    for item in tabsubs:
        tabcount.append(item)
    del tabsubs[:]
        
        
        
tabsubs=[]
threetabs=[]
fivetabs=[]
seventabs=[]
ninetabs=[]
eleventabs=[]
thirteentabs=[]
fifteentabs=[]

#used by the super duper function with 6 methods in it
#===============================

first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot
christmastree=[]
second=[]   #this takes an inputstring which is the combined switchcase big string
slydog=[]
snowtime=[]
mylistinput=[]
#===========================
super_listinput=[]

def put(x):
    listinput.append(x)



#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  #line 976
    #print('====================METHOD 3 ==== line 976===>>>')
    #print("this is .. build_list_input_list() ...")
    #print("it gopher sees right here ",holding_themax[0])
    #holding_themax[0]
    mx = holding_themax[0] #it's using this number 
    #print(type(holding_themax[0]))
    #print("is it REALLY say 7  above this line???")
    
    input= holding_themax[0]
    #cascading down is how it works
    if holding_themax[0] >= 3: put(3);
    if holding_themax[0] >= 5: put(5);
    if holding_themax[0] >= 7: put(7); 
    if holding_themax[0] >= 9: put(9); 
    if holding_themax[0] >= 11:put(11);
    if holding_themax[0] >= 13:put(13);
    if holding_themax[0] >= 15:put(15);
       
    #print("at bottom of ifs what is in listinput")
    #print(listinput)
    for item in listinput:
        super_listinput.append(item)
    #print("super_listinput =",super_listinput)
  
  
  
  
  
  
  
  
  
  
  
  
  
##=================================
##  list_tabs_lists_by_depth():
##================================== 
def list_tabs_lists_by_depth():
    pass
    #print("==list tabs lists by depth=====METHOD 5======>>")
    #print("threetabs=" ,threetabs); print("fivetabs="  ,fivetabs);
    #print("seventabs=" ,seventabs); print("ninetabs="  ,ninetabs);
    #print("eleventabs=",eleventabs);print("thirteentabs=",thirteentabs) 
    










#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    #print("")
    #print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
    #print("=== this is just sick bad ass ========")
    #print("inputstring",inputstring);print("tabsubs ",tabsubs, " ",x)
    counter=0
    for line in inputstring.splitlines():
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
        if tab_length == x: 
            if "switch" in line and "end" not in line:
                tabsubs.append(counter);counter += 1;continue
            if "endswitch" in line:
                tabsubs.append(counter);counter += 1;continue 
    #print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:
        pass
        #print("nada")
        #print("these are the tab lists from three to thirteen rudolph fly")
        #print("3 and 5 tabs =",threetabs ," ",fivetabs)    
        #print("7 and 9 tabs =",seventabs ," ",ninetabs)   
        #print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   







##==================================================
## make_switch_and_endswitch_pairs_by_tab_levels() 
##=================================================== 
def make_switch_and_endswitch_pairs_by_tab_levels(): 
    #print("make_switch_and_endswitch_pairs_by_tab_levels()")
    #print(":=============== METHOD 4 ======") 
    for item in super_listinput:     # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)
     
    #print("  make_switch_and_endswitch_pairs_by_tab_levels(): ")
    #print("listinput list =",listinput)
    #print("THIS IS CALLING INTERNAL_MACHINERY METHOD ")   
    #for item in listinput:     # listinput is dynamically made above
    #    x = item;
    #    internal_machinery(x,inputstring)   #METHOD internal_machinery()




###=============================== 
 
        #del tabsubs[:] #should clear it
###=================
rattabs=[]
##==== goldmedal test()  this just does threetabs 
def goldmedaltest(): #this makes stacks column switch endswith for 3 tabs
	#print("=======goldmedal test=== this one is correct== its gotta work now please ---")
	inputstring = red_robin
	#print("original working code for 3 tabs that worked previously")
	counter =0
	for line in inputstring.splitlines():
		print(line)
		#######################
		tab_length = line.count("\t")
		if tab_length != 3 or "switch" not in line:
			counter += 1;continue
		#######################
		if tab_length == 3:
			if "switch" in line and "end" not in line:
				#print("if switch called")
				#print("======switch in line===")
				rattabs.append(counter)
				print(rattabs)
				counter += 1;continue
			if "endswitch" in line:
				print("if endswitch called")
				print("======endswitch in line======")
				rattabs.append(counter)
				print(rattabs)
				counter += 1; continue

#print("result of goldmedal test =")
#goldmedaltest()



#was in experiemntal machinery below
'''
    for line in inputstring.splitlines():
        print(line)
        tab_length = line.count("\t")
        if tab_length != 3 or "switch" not in line:
            counter += 1;continue
        ##################
        if tab_length == 3:
            if "switch" in line and "end" not in line:
                print("if switch called")
                print("======switch in line===")
                dumbtabs.append(counter)
                print(threetabs)
                counter += 1;continue
            if "endswitch" in line:
                print("if endswitch called")
                print("======endswitch in line======")
                threetabs.append(counter)
                print(threetabs)
                counter += 1; continue
    print("this one blast time for 31 flavors THIS IS THREE TABS === ---")
    print("threetabs=",threetabs)
'''
    
    
    
    
    
#print('testing the internal machinery method engine now')
#threetabs=[]
#endtabslist=[]
#endswitchlinenumbers=[]
#dumbtabs=[]
##==============================
##  experimental_machinery
##===============================
def experimental_machinery(x,inputstring):
    #print("======experimental_machinery called==========")  
    counter =0
    #newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    #print(newstring)
    internal_machinery(x,inputstring)
 
    ###============
    #switches and endswitches at 3 tabs should be even number
#print("dumbtabs =",dumbtabs)

#print("== bees ==== this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ====")
#print("try_all_three(inputstring)")
#print("=====halloween ghosts trying all three 3 5 7 tabs now====")
#print(" === to the moon when will starship land ===")
#print("======= TESTING NEW CODE HERE WEDNESDAY to get the larget tab depth in string")
# this determines the highest tab count for a line with a switch
# which is used to create the listinput list

#try all three()  Did this one on Wednesday late sep

#threetabs=[[22,33],[44,66]]
#fivetabs =[[55,58],[77,86]]
#seventabs=[[88,99],[102,110]]

combined_tabs=[]
christmastree=[]

##============================================
## combine the lists together  #waterfall ifs
##=============================================
def combine_the_lists_together(x): 
    get_length_of_threetabs    = len(threetabs)
    get_length_of_fivetabs     = len(fivetabs)
    get_length_of_seventabs    = len(seventabs)
    get_length_of_ninetabs     = len(ninetabs)
    get_length_of_eleventabs   = len(eleventabs)
    get_length_of_thirteentabs = len(thirteentabs)
    #test if threetabs list is empty
    #print("testing if length of threetabs list GREATER THAN 0")
    if get_length_of_threetabs > 0: #then proceed there is at least one
        #print("YES length of threetabs IS GREATER THAN 0",get_length_of_threetabs)
        #this is a waterfall extending numbers to add to christmastree list
        if x >=  3:christmastree.extend(threetabs);
        if x >=  5:christmastree.extend(fivetabs);  
        if x >=  7:christmastree.extend(seventabs);
        if x >=  9:christmastree.extend(ninetabs); 
        if x >= 11:christmastree.extend(eleventabs);
        if x >= 13:christmastree.extend(thirteentabs);
    
    else:
        pass
        #print('all of the tab lists are empty')
        #print("don't bother trying to extend empty tab lists")
       
         
    #print('at le bottom of function combine_the_lists_together christmastree list now has')
    #print(christmastree)
    #print(":what is in the christmas list above here starbucks")
    #print("the chrsitmastree list is what should be whole at this point HER!!!")
    


##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    #print("=== build_tab_list_added_together(x)======>>>>")
    #print("this combines separate lists together into one list all be it clumsily")
    #print("larget_tab_number =",largest_tab_number)
    del christmastree[:] #clears out the combined_tabs list to erase it
    #print("about to call combine_the_lists_together wed nov 17th ")
    ## calling combine the lists together here 
    combine_the_lists_together(largest_tab_number) #<<==input is the largest tab number
    
    
    


 
 
fox=[]  #this is just a simple test 
def wildtest(themax):
    print("themax =",themax)
    print("called wildtest to add to list")
    if themax == 3: 
      fox.append(3) #.append(3)
      
    if themax == 5: 
      fox.append(5)
      
    if themax == 7: 
      fox.append(7)
      
      
    #if themax == 9: fox = [3,5,7,9]
    #if themax == 11:fox = [3,5,7,9,11]
    #if themax == 13:fox = [3,5,7,9,11,13]
    #if themax == 15:fox = [3,5,7,9,11,13,15]

#print("starting fox list =",fox)
#wildtest(3)   
#wildtest(5)   
#wildtest(7)  
#print("fox list =",fox)
#print("above it should say 3,5,7")
#print("road to tahoe is up hill")



#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    #print("== combine tabs by length into christmastree_list======")
    #print("======METHOD 6 ===  combine tabs by length into christmastree_list====>>>>")
    themax = holding_themax[0] #this gets the highest tab level (deeply nested)
    #print("where is my coffee now")
    #print('let us look in the three tabs list threetabs, fivetabs, seventabs')
    #print(threetabs,fivetabs,seventabs)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    #print("christmastree=",christmastree)
    #print("")
    

         



#================================= 
#  build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    #print("")
    #print("=== METHOD 7== build pairs with jazz =======>>>>")
    #print("")
    counter =0
    #print("inside of build pairs with jazz the christmastree list show")
    #print("christmastree=",christmastree)
    for x in christmastree: #loops thru at 2 at a time
       # print(christmastree[counter],christmastree[counter +1])
        jazz = [christmastree[counter],christmastree[counter+1]]
        #print("appending jazz to snowtime list now")
        #list snowtime starts virgin and then we append jazz pairs to it
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        ##=========================================================
        #prevents overflow error for out of range error
        #print("this is the resulting pair list that is so coveted")
        #print("this used the jazz pair pair system that works")
        #print("snowtime list=",snowtime)
        if counter >= len(christmastree):
            break
            
            
            
            
            
            
            
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    #print("")
    #print("build tab depth ==== METHOD 1 ==  build_tab_depth(=======>>")
    #print("")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")         #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth)    #this is for filling the list of each tab depth
        else:
            continue
    #print("add_tab_depth=",add_tab_depth)
    #print("max tab depth=",add_tab_depth[0])
            
      
      
      
      
      
            
            
def loop_thru_pairs_in_snowtime():
    #print(" ==== #method 8 ===  loop_thru_pairs_in_snowtime()=============")
    #print("snowtime list=",snowtime)
    for item in snowtime:  
        #print(item);
        rad1=item[0];rad2=item[1];
        #print(rad1,"and ",rad2)
    #print("this is the output list that was generated.") 
    print("snowtime list=",snowtime)




##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():  #this fills the max holding_themax[0]
     #print("====================  #METHOD 2 ========")
     #add_tab_depth = input
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     #print("themax=",themax)


#def goldtime():
#    print("goldtime callled goldtime goldtime")
#    for item in super_listinput:     # listinput is dynamically made above
#        x = item;
#        internal_machinery(x,inputstring)
# REFACTORED on nov 8th , 2021 to reduce the complexity modified nov 9th


##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
##========================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    #print("=======THIS MAKES SWITCH AND ENDSWITCH PAIRS BY TAB LEVELS========")
    #welcome to - time 10;43 am nov 9th-")
    #print("this is unreal; this_makes_switch_and_endswitch_pairs_by_tab_levels()")
    build_tab_depth(inputstring)                           #METHOD 1
    get_max_tab_number_in_list() #fills holding_themax[0]  #METHOD 2
    build_list_input_list()                                #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels()        #METHOD 4
    list_tabs_lists_by_depth()                             #METHOD 5
    combine_tabs_by_length_into_christmastree_list()       #METHOD 6 
    build_pairs_with_jazz()  #combines into sublist        #METHOD 7 
    loop_thru_pairs_in_snowtime()                          #METHOD 8
    #this will go into gold_list
        
        
print("======================================")
print("make it so star trek")
print("using red_robin for our input string")
inputstring = red_robin
#print("what red_robin looks like before calling try_all_three=====")
print(red_robin)
#print("see how it looks above if there are double switches and endswitches yet")
this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)

#exit()
print("the output is snowtime list")
print(snowtime)

##==================================================================================================
# output is to inputstring[0]
#############################################################
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
##  this does this:   switch(exp)    becomes switch(exp) #22    for example based on the line number of each switch
##  returns newstring which is concatted together changed switch string with numbered switches in the comment after each
##===================================================
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	#print(" add_comment_and_line_number_to_all_switch()....this was just called .. ")
	#print(" == directive 1 ==    ADD  comment and line number after each switch ")
	awesome='';counter =0;newstring='';
	#print('baseline is red_robin starting appearance testing purposes')
	#print(inputstring)
	
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			# NEED TO HANDLE BOTH SCENARIOS switch with brace and switch without a brace 
			#############################################
			#switch is in this line definitely
			if "{" in line and "switch" in line and "end" not in line:
			### new surgery ===dec 20th monday bug fix out of the blue =======
				#if counter == 1: #modified for bu on dec 20th monday each number was off by 1 except first
				newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
				#else: #if counter > 1
					#counter = counter + 1 #adding 1 to counter
					#newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
			
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
	#print("=== jump off the cliff and fly in hang glider ==")
	#for line in newstring.splitlines(): #was redrobin.splitlines()
	#	print(line)
	#print("AFTER ADDING the line number as comments to the switches in red robin baby ")	
	#print(newstring)   #it prints red_robin switch combo string with the line numbers added in comments
	#print("smart_switch_numbers=",smart_switch_numbers)  #this is new here too 
	return newstring #this way I can capture the changed string
##===================================================================================
#print("add comment and line number after each switch in autumnleaf")
#print('one, two, three, here we go.')

	
	
##============================================
##  inputs_pair_to_copy_a_string()
##============================================
def inputs_pair_to_copy_a_string(start,finish):
    #print("inputs pair to copy a string")
    del start_and_finish[:] #this clears it out initializing it
    start_and_finish.append(0) 
    start_and_finish.append(start) #position [1]
    start_and_finish.append(finish) #position [2]
    #start_and_finish[1] = x
    #start_and_finish[2] = y
    #print("x=",start_and_finish[1])
    #print("y=",start_and_finish[2])
    
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



columbia_river=[]
gold_list=[]
###############################
## copy_a_nested_switch(r):   # what this does is copy one nested switch 
###############################
def copy_a_nested_switch(r):  #copy just one nested string 
    #print("= copy_a_nested_switch() called== just now 10;43 am ====")
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    answer=start_and_finish[1]
    start_and_finish[1] = start_and_finish[1] - 1 #added this on dec 20th to show switch word
    #print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
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
    #print(":the result COPY OF NESTED SWITCH  ")        
    #print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner #result of copied string goes in makeitwork[0]

################################################################################

#I need to fill this list (populate it from get switch engineswitch pairs
#print("testing looping thru gold_list")
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]
print("=======begin Sunday Morning Brew Testing=======")


def show_switch_string_with_numbers_added_after_each_switch_with_a_comment(water):
    for line in water.splitlines():
        print(line)


def show_the_snowtime_list_of_pairs():
    print("snowtime=",snowtime)   
    
def empty_columbia_river_list():
    del columbia_river[:] 
    
def add_main_switch_to_columbia_river(water):
    columbia_river.append(water)  

    
holding_string=[]
holding_string.append(0) 

##============================================================================
##  loop_thru_snowtime_list_copy_switch_bodies_and_add_to_columbia_river():
##============================================================================   
def loop_thru_snowtime_list_and_copy_switch_bodies_and_add_to_columbia_river():
    for item in snowtime:#was gold_list #loop that gets switch,endswitch pair from goldlist
        num1 = item[0];
        num2 = item[1];
        inputs_pair_to_copy_a_string(num1,num2) # get input string from goldlist
        copy_a_nested_switch(holding_string[0]) # copy string based on switch,endswitch pair 
                                                # puts resulting string into makeitwork[0] and output
        output = makeitwork[0]                  # put nested string into columbia_river list
        columbia_river.append(output)
    #print("length of columbia river =",len(columbia_river))
    #counter =1  #adding here the initial string which will be used to make the main switch


    
##=================================  
## loop_thru_columbia_river() 
##================================= 
def loop_thru_columbia_river():
    #print("now loop thru ====== COLUMBIA RIVER === to see the switch bodies seperated")
    counter =1
    for item in columbia_river:   #it is added just before looping thru i
        print("counter=",counter)
        print(item);
        print("===========");
        counter += 1    
    
          

#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]    

##==============================================

   #This takes in what has already split the mega nested switch into 
   #switch bodies
##=============================================================
##  split_up_big_string_into_nested_switches(myinputstring)
##=============================================================
def split_up_big_string_into_nested_switches(myinputstring):#this would only be called once
    print(" ==  split_up_big_string_into_nested_switches(inputstring)  ==")
    water =add_comment_and_line_number_to_all_switches(myinputstring)               #METHOD 1
    show_switch_string_with_numbers_added_after_each_switch_with_a_comment(water)   #METHOD 2
    empty_columbia_river_list()                                                     #METHOD 3
    show_the_snowtime_list_of_pairs()                                               #METHOD 4
    add_main_switch_to_columbia_river(water)                                        #METHOD 5
    holding_string[0] = water
    loop_thru_snowtime_list_and_copy_switch_bodies_and_add_to_columbia_river()      #METHOD 6
    loop_thru_columbia_river() #prints out seperated switch bodies top down         #METHOD 7               
    ##==============
    print("the switch strings cut up are now printed out top down")
  
##================================================================        
##================================================================
print("end of crucial test copying the strings and putting them into a list")
split_up_big_string_into_nested_switches(red_robin)
#this is new december 20th already my gosh.






	
	
	
Dec 19th 2021 10:06 am Sunday morning coding. 
KKUP Neptune Currents sunday mornings only = great trance music great music 91.5 FM Santa Clara
KZSU Stanford 90.1 FM both accessable using MyTuner Radio app on mac
	
#refactoring and testing the whole project regular switches and nested switches
# music:  https://www.youtube.com/watch?v=-CmadmM5cOk  Taylor Swift Style


This morning I refactored cleaning up errant spaces in front of the first word of each line in the input
switch case strings for each switch case body.


newlist=[]
newtime=''
thelist=[]
finaloutput=[]
finaloutput.append(0) #creates slot
'''
this cleans up input javascript code that is supposed to be 
governed by tabs in front ala Python and if a space is discovered
it is neutralized and deleted. 
This first counts the tabs in each line in the string.
second it cuts out all spaces and tabs from left of each line
then it concats a new string with the correct tab count in
front of each line so it's CLEANED UP essentially. 

'''
#bad input
examplestring='''
	      switch(exp){
	    	case 1 thru 3:
		  	print("where\'s the dog house!")
	  		    print('first prize')
	  		    print('you block head Charlie Brown')
			fallthru
	  	case 4 to 7:
	     		      print('first prize')
	     		print('you block head Charlie Brown')
		         case 9 thru 11:
'''
#cleaned up output becomes
'''
	switch(exp){
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
		case 4 to 7:
			print('first prize')
			print('you block head Charlie Brown')
		case 9 thru 11:
'''
finalstage=[]
finalstage.append(0)
##========================================
##  cut_out_left_side(inputstring):
##========================================
def cut_out_left_side(inputstring):
    print("cout out left side")
    fancy=''
    for line in inputstring.splitlines():
        #print(line)
        newline = line.lstrip() #I am using lstrip() look at that!!
        fancy += newline + "\n"
    finalstage[0] = fancy
    ## concatting tabs in front + line to redone


##========================================
##  concat_tabs_in_front(fancy):
##========================================
def concat_tabs_in_front(fancy):
    print("conctat_tabs_in_front()")
    redone='';counter=0
    for line in fancy.splitlines():
        #print(newlist[counter])
        print("bad assed")
        redone += newlist[counter] + line + "\n"
        counter += 1
        if counter >= len(newlist):#prevents out of range error
           break
    finaloutput[0]= redone
    print("right here the OUTPUT =",finaloutput[0])


#==================================
#   append_result()  pure genius   
#=================================  
def append_result(x):
    tab = "\t"
    result = tab * x;
    newlist.append(result)  
    #this replaces: #if item == 1:result = tab * 1;newlist.append(result)

#puts tab count in each line into thelist
##===============================================================
## count_tabs_in_each_line_and_put_into_thelist(inputstring):
##===============================================================
def count_tabs_in_each_line_and_put_into_thelist(inputstring): 
    del thelist[:];del finaloutput[:];finaloutput.append(0) #creats one slot space
    for line in inputstring.splitlines():
        answer =line.count("\t") 
        thelist.append(answer)
             
#made into a function on saturday, dec 4th morgan hill starbucks 
# refactored on dec 19th for efficiency and management
##=======================================================
##  take_out_junk_spaces_from_left_side(inputstring):
##=======================================================
def take_out_junk_spaces_from_left_side(inputstring):
    print("take out junk spaces from left side")
    print(inputstring)
    count_tabs_in_each_line_and_put_into_thelist(inputstring) # METHOD
    for item in thelist:  #fill a list with tabs corresponding to numberof tabs numbers
        x = item;
        append_result(x)                                      # METHOD
        
    cut_out_left_side(inputstring)#puts fancy in finalstage[0]# METHOD
    fancy =finalstage[0]
    concat_tabs_in_front(fancy)                               # METHOD 
 
#####################################################################
print("here we go big time test..........fireworks...")
##take_out_junk_spaces_from_left_side(coolinthegang)
#for line in finaloutput[0].splitlines():
#    print(line)
    
#### takes out bad data messing up tabs    
take_out_junk_spaces_from_left_side(examplestring) #<<===== function call 
for line in finaloutput[0].splitlines():           ## output is in finaloutput[0]
    print(line)
    
exit()    


What I worked on yesterday was generating the nested switch and running it from input strings of Javascript/C switch cases already split up
Today I found the code that creates the split separated input switch strings that are fed into quail.
I also just refactored a remove junk spaces from input strings to prevent disaster.
I still need to wire it all together (it has been joined in the past) and all should go well.

Need to work on some modifications in the generated code so that the nested switches get the proper input which was 
an earlier (past) but preventing the triggering of the nested switches.



#this will be renamed but is for testing.
the actual code is triggered by endswitch(string) at bottom of switch case.

but for testing it looks like this:
topvalue[0]='1' #input value for top of switch(x)
clever_cat() #this triggers the switch case parser and code gen concat generated strings and exec(code)


Real test output of jumping around nested switches in a main switch:
BBEdit
##========
input is  1
where's the dog house!
first prize
you block head Charlie Brown 9
kangaroo hop hop!
this is nested swith 11
this is nested switch 15
nested switch 23 tahoe
yep
nice
we very done
yep
nice
nested switch62
this is nested switch 66 cool
yep
nice
taught me how thru write code file called gold1
mocha blast
== 31 flavors===
the end
result[0] = 0
#=====================================
Sublime Text output


input is  1
where's the dog house!
first prize
you block head Charlie Brown 9
kangaroo hop hop!
this is nested swith 11
this is nested switch 15
nested switch 23 tahoe
yep
nice
we very done
yep
nice
nested switch62
this is nested switch 66 cool
yep
nice
taught me how thru write code file called gold1
mocha blast
== 31 flavors===
the end
result[0] = 0
[Finished in 265ms]


Saturday, Dec 18th. 2021 11:28 am Gilroy, California 

Inspired by: https://www.youtube.com/watch?v=_Yhyp-_hX2s&list=RDGMEMHDXYb1_DDSgDsobPsOFxpAVM_Yhyp-_hX2s&start_radio=1
Eminem Lose Yourself To Seize Everything You Wanted

Trance coding music:Dream State Logic:  https://www.youtube.com/watch?v=oJXksJxXjk4
coding music: Children  https://www.youtube.com/watch?v=CC5ca6Hsb2Q
		
As I just discussed with my brother, what just saved this project from failure was building it in sections and then
at the very end (the past month) I broke the project into two pieces that I worked on seperately. The end game plan
was to verify that the main bypass engine was working and that the code ran. The other part was concatting the strings together
accurately and then making sure that the generated code executed. I was watching Super Heavy Booster and Starship before they
were stacked and it gave me the idea to split the project at the end to make sure the two critical pieces work independently.

I failed when I made the frosty.py file that imported the files and I had to import lists and it was a mess. My mind set was
similar to a web app and it was not working properly so I restarted and then cut out the tron3 file to focus on concatting and
execu(code) seperately since the bugs were coming fast and furious which was raising my frustartion level and as I continued
to flail I decided to utilize divide and conquoer and finally I broke through and got it working. It was impossible to debug
altogether because I didn't know how to pinpoint the bugs and zero in on them. I then compared what was working
and gradually figured out the bugs with test code what was running and where it wasn't properly calling nested switches.

It was just last night that it started beginning working properly(as seperate parts individually) 
in the three piece set of mini modules all together in one file. And the starship section that concats worked after I solved
a string bug. And then I was able to successfully test the three module section with bypass that started with input
in the quail list of the seperated switch strings rather then starting with one big string and seperating it which already works.


#=========================================================================
Next I will test some javascript and C switch cases and make sure that this new python switch case
exhibits the identical running behavior of C and Javascript switch cases. I will get the C and JavaScript examples
off the web to avoid any bias. 

I will also add the free floating default from C (likely next week as side project) where default can be located anywhere within a switch case and not
necessarily at the bottom. Though for implimentation that is where the default ends up after parsing.

Saturday Software: Sat Dec 18th, 2021 8:05 am PST
Nested Switch works and runs thru bypass205().
Pure nirvana. All of the hardship to get it working is over with.
Disbelief. Fixed bug last night that held me up. As Alan Turning described bugs as snags - it's true.
Total dream seeing it working.
Will upload later tomorrow evening.



Tuz Dec 14th, 2021 11:29am PST Morgan Hill, California Starbucks free WiFi.
I just uploaded the critical files for the automated nested switching to work.

Nested switches took 6 months. First I modified the parser to handle (it's a tricky detour)
more than one input switch case string. I collect them in a list called quail (whom never travel alone)
then loop thru the quail list and use bypass205() to convert each string into python which is placed into the stanford list
The actual bypass205() design is utter genius that evolved over time to become extremely svelt. 

#inside of endswitch()  #an inner chunk of the critical code 
	print("length of quail =",len(quail))             #3
	print("number endswitches =",endswitch_number)    #2
	print("NUMBER OF SWITCHES  =",number_of_switches) #3
	##################
	## august 7th testing morgan hill starbvucks with dummy data to get this working
	print("about to try to TRIGGER  bypass205()")
	print("I will loop thru quail here for now to show that the strings exist ")
	print("already seperated split up")
	print("this is quail list")
	print("======================")
	for item in quail:
		print(item)
		print("=========")
	###============================
	print("I am right here where in test stage bypass205 is called using quail list")
	if len(quail) > 1:
		print("bypass205() called")
		bypass205(y) #add later (y) to it
	else:
		pass
		
######################
##  bypass205(y)	
######################
def bypass205(y): 							# runs input strings thru parser and  
	print("bypass205() called====is this working yet or not???=======");
	mytrace("bypass205()") 					# code gen puts in stanford list
	del stanford[:] 						# empties  stanford list 
	#takes out endswitch and replaces it with }
	swap_endswitch_with_curlybrace() #this loop thru quail list doing this
	print("quail list length=",len(quail))
	print("it goes thru the quail list which it applies the parser guts to each individual string")
	##  loops thru quail list ############
	for item in quail: #to see what's in quail list
		print(item)
	for item in quail: 						# loop thru quail list 
		y = item 							# this puts the contents of each string in quail into y 
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		show_input_switch_string() 			# flag for testing this shows the input string
		parser_guts(y)  					# does parser and codegen of each switch string        
		# automatically adding python translation to stanford list at bottom of codegen
###  end bypass205()  ##################  		
		
#parser guts is the same sequence of code in the endswitch above
# I am just trying to reduce code  that's all.
#################################
##     flow_valve_input(y)
##################################
def flow_valve_input1(y):  #this determines if switch case string is numbers or words
    print("Flow Valve input")
    mytrace("flow_valve_input()")                            # get first case in switch case string
    getline  = grab_first_case_of_switch_string(y)           # get first case line
    toocool  = grab_first_case_line_in_switch_case_string(y) # remove tabs from the case line
    toocool  = remove_tabs_from_string(toocool)              # test if number in first case line yes = True no = False
    valve[0] = check_if_number_in_string(toocool)            # looks in case line
    valve[1] = toocool                                       # put case name/number into valve[1]
    print("output from FLOW VALVE=",valve[0],"and",valve[1])
################################################
								      
								      
####============================
####      parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("parser_guts() called =======")
	check_if_uppercase_constant_cases(y)	#if UPPCASE this senses it and converts to string
	if baseline[0] != "nada":				#means it converted to uppercase
		y = baseline[0]
	flow_valve_input1(y)					#puts True or False into valve[0] added April 2nd, 2021
	print("if number in first case",valve[0])
	if valve[0] == True:					#marco expansion numbers like case 12:
		macro_expansion(y); 				#checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
	flush_lists() 
	parser_mode_1(y) 	

###==================================
###########################
##     parser_mode_1()
###########################
## testing April 3rd 2021 seeing if this works or not. 
def parser_mode_1(a):
	#print("a= ",a)
	mytrace('parser_mode_1 in switch_cat()') #was greatpumpkin
	#print('=======INSIDE OF PARSER in switch_cat for strings  =========')
	mountain2(a)    # this changes sw to switchcasetester #I can't beleive that this reverse number was being called 
	starter_sequence_mode_1()

##################################
## starter sequence mode 1
##################################
#this is for parsing and codegen of cases with words only
def starter_sequence_mode_1():
	print("it SEES in valve[0]",valve[0])
	#print("the if vavle[0] = False is the setting in here ")
	# valve[0] is False if words, it is True if numbers
	#this if means this can only run if valve[0] is False not numbers
	# I just made this change since both are now strings
	#########################################
	if valve[0] == True or valve[0] == False: #case numbers if True WAS False #means cases are words like "apple pie"
		mytrace('starter_sequence_mode_1()')
		
		convert_case_line_to_lowercase()  #right here for conformity all words lowercase
		badass()
		stage_one() 				## and if numbergs
		add_to_test_list()  #testing here
		#case_main_body_list.append("starter")
		stage_two()
		stage_three()
		stage_four()
		stage_five()
		stage_six()
		stage_seven()
		stage_eight()
		stage_nine()
		stage_ten()
		stage_eleven()
		#print('stopping just before switch_code_gen()')
		#quit() #see if this works
		switch_code_gen() #  <<<==============it's called right here the code generator
		######### testing this to do next stages 
		######### if nested switch with several strings
		######### so that I don't just tack it onto switch code gen
		######### and this way it's done after stanford is filled with output 
		######### python stings
		managing_nested_switch_scenario()
		
		stage_twelve()  # <== this resets the lists for next use of switch
		########=== added june 16th, 2021 #####
		#uppercase reset to default 
		#set these after exec
		#this resets defaults to turn off uppercase yes 
		
		#uppercase_test[0] = False:
		#baseline[0]="nada"
		#############################
		clearit()
		global woodstock
		#print("what we have in woodstock=",woodstock)
		#print("now we clear out woodstock list")
		woodstock=[]
		#print("woodstock=",woodstock)
		global candy
		#print('what we have in candy=',candy)
		#print("now we delete its contents")
		candy=[]
		#print("candy=",candy)
		#flush_lists()
		global sw 
		sw = ''
		global switchcasetester
		switchcasetester =''
		smartcasemanager=[]
		print("smartcasemanager=",smartcasemanager)
		british=[]
		#print("british=",british)
		penguin=[]
		#print("penguin=",penguin)
		clear_out_all_case_lists() #doing 16 for now
		#show_tron_trace_path()
	else:
		pass
		
	
	showit()
	empty_test() #test of global list
	
								      
								      
frosty.py
woodstock.py
Linus.py
snoopy_doghouse.py
tron3.py




I am now working on trapeze which takes in a raw string of switch case for input which is governed by tabs
for the switch to work. Currently I am using a canned switch case string to test. So it will fully work
connected together likely tomorrow. Right now it works just fine with the test code switch case for input.
Also, take note that the input string is run thru bypass205() and I still need to activate it by going thru
the regular parser which then in turn triggers bypass205() officially so I need to test that phase too.
The reality is that the impossible parts are working now and the cakewalk part that remains is trivial.
Just getting exec(code) to work within a function was a total nightmare journey through hell.
Never used extensive imported files and lists before this project and that thankfully went smoothly.

In the past python code I wrote in BBedit had difficulty running in Sublime but for this project
the code runs perfectly in Sublime Text 3 build 4121.



December 14th 2021  9:56am 
nested switches works. total disbelief.
Will upload code and begin cleaning it up. I stopped breathing when it ran. I thought there was some mistake.
Music playing when it first worked altogether.
Blade Runner 2049 - Tears In Rain Slowed Extended
#https://www.youtube.com/watch?v=X0Hyxq7iOwI

Tue Dec 14, 2021 11;21
Just tested the python code for frosty.py on Sublime Text 3 Build 4121  and it runs flawlessly.
I have also run it (and developed it) in BBEdit 13.5.7 runs flawlessly.
file name: frosty.py
###=== importing files ===================
from woodstock import *
from Linus import * 
from snoopy_doghouse import * 
from tron3 import *
#from ready_player_one import * 
#from drivethru import *

####====importing lists ====================
from Linus import switch_numbers_to_transfer
from snoopy_doghouse import output #list
from tron3 import topvalue #list
#############################################
#from Linus import switch_numbers_to_transfer# alist
# december 13th, 2021 Monday 10;35 am Morgan Hill Starbucks, California
print("== running from frosty.py ====")
varholder=[];
varholder.append(0)

red_robin ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you super smart head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  
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
							####################
							switch(exp){ #23  #third level deep   Level 3    
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
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #53  second level deep          Level 2    
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

inputstring =''

#print("======== STAGE 1 ====woodstock.py=================")
#inputstring = red_robin
#create_list_of_pairs_now(inputstring); #makes switch,endswitch line number pairs
#calling functions in linus uses gold_list
#this separates the switches built using copy body using pairs x,y  
#this needs to be called before filling the list obviously 

#print("======== STAGE 2 ====Linus.py =================")
#split_up_big_string_into_nested_switches(red_robin)  
#waterfall_chain_methods_gold_master() 
#should output the quail list of strings ready for bypass205()

#print("======== STAGE 3 ====snoopy_doghouse.py=================")
#create_def_switch_methods_concatted_together_in_one_string()
#print("after finishing snoopy_doghouse.py")
#output combined python switch methods ready to be executed.



#https://www.youtube.com/watch?v=X0Hyxq7iOwI



def stage(x):
    print("#=== STAGE "+str(x)+ "==")

colorfilm=[]
silver=''
def create_generated_python_switch_methods_concatted(inputstring):
   ##==============================================
   # stage 1 woodstock.py
   print("stage 1 called in frosty")
   create_list_of_pairs_now(inputstring);stage(1); 
   ##=================================================
   # stage 2 Linus
   print("stage 2 called in frosty")
   split_up_big_string_into_nested_switches(inputstring);stage(2);        # stage 2 Linus.py  
   waterfall_chain_methods_gold_master(); stage(2);  
   ##========================================
   #stage 3 snoopy_doghouse.py   
   print("stage 3 called in frosty ==")
   create_def_switch_methods_concatted_together_in_one_string();stage(3); # stage 3 snoopy_doghouse.py
   #print("length of stnaford",len(stanford))
   print("--dec 14th ---genersted docstring  python code-----")
   for line in toocool[0].splitlines():
      print(line)
    ##========================================
   #stage 4 tron3.py   
   print("====stage 4 frosty====")
   print("calling clever_cat() from frosty now to concat the")
   print("dynamically generated python switch cases that look like javascript")
   topvalue[0]='8'
   print('here we go')
   clever_cat(); stage(4) #this triggers indirectly the exec(string) of dynamic python!!


inputstring = red_robin    
create_generated_python_switch_methods_concatted(inputstring)    
    
    #create_def_switch_methods_concatted_together_in_one_string()
print('how did it do..finished in frosty.py.')

=====OUTPUT=====
input is  1
it sees for exp 1
===MAIN SWITCH== 1
where's the dog house!
first prize
you are so smart  Charlie Brown a genius
kangaroo hop hop!
=== NEST SWITCH 11== blable
do something yes Tahoe ski trip
==NEST SWITCH 15== tahoe
rafted down Truckee River Once.
yep
nice mocha in the morning
 kayaking at Fallen Leaf Lake
 ==NESTED SWITCH 23rd==  cold water
nice
==NESTED SWITCH 31== fishy
INSIDE CASE 1 OF NESTED SWITCH 31
yep
nice
yep
nice
just added this inbetween two nested switches
it will come thru here anyways and flow down
==NESTED SWITCH 62== burger
do something
 ==NESTED SWITCH 66== fishy
do something
yep
nice
yep
nice
taught me how thru write code
mocha blast
== 31 flavors===
#=== STAGE 4==





Dec 13th, 10:25 AM  Massive nested switch generation worked.
Nested Switch stages working together. Final test in a few minutes.
When it ran my jaw dropped because the files are huge.
from woodstock import *
from Linus import * 
from snoopy_doghouse import * 

print("== running from frosty.py ====")

red_robin ='''
	switch(exp) {  
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
					switch(exp){ # 15  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23  #third level deep   Level 3    
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
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #53  second level deep          Level 2    
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

inputstring =''

print("======== STAGE 1 ====woodstock.py=================")
inputstring = red_robin
create_list_of_pairs_now(inputstring);
#calling functions in linus uses gold_list
#this separates the switches built using copy body using pairs x,y  
#this needs to be called before filling the list obviously 

print("======== STAGE 2 ====Linus.py =================")
split_up_big_string_into_nested_switches(red_robin)  
waterfall_chain_methods_gold_master() 
#should output the quail list of strings ready for bypass205()

print("======== STAGE 3 ====snoopy_doghouse.py=================")
create_def_switch_methods_concatted_together_in_one_string()
print("after finishing snoopy_doghouse.py")
#output combined python switch methods ready to be executed.

print('how did it do..finished in frosty.py.')
Generates this before I add the switch and fallthru methods and input var and exec() it.

def nested_switch_66(exp):	
	exp = varholder[0]
	
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("nice")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_62(exp):	
	exp = varholder[0]
	
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_31(exp):	
	exp = varholder[0]
	
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('where now')
	
		elif case in caselist2: # ['where now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	
def nested_switch_23(exp):	
	exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
		####################
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_15(exp):	
	exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
			####################
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_11(exp):	
	exp = varholder[0]
	
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	


def main_switch(exp):	
	exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	


	


Thursday, DEc 9th, 2021 10:03 pm PST California.
Just successfully tested 4 level deep nested switch in Python.
This was code parsed, generarated and concatted together and executed.
There are three pieces of the puzzle and I am in the process of connecting them together.
I am combining sets of the methods to help manage the code for inevitable refracturing later.

concatting the code has three sections

#put this string into a list with just the string by itself in position 0
method_defs='''
# =======  switch  =================================
def switch(x):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	x = str(x)
	global case
	case = x.lower() 
# =======  fallthru       =========================
def fallthru(y):
	eval("switch('" + y + "')")
#==================
#for inswitch
def inswitch(n):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	n = str(n)
	global case
	case = n.lower() 
#=====================
# for infallthru    
def infallthru(n):
	eval("inswitch('" + n + "')")
'''
result=[]
result.append(0)



varholder=[]
varholder.append(0)

#it's one big string
nestswitches='''

def nested_switch_66(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 66==",exp)
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("nice")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_62(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 62==",exp)
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
			exp = 'fishy'
			nested_switch_66(exp) #66
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_31(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 31==",exp)
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("INSIDE CASE 1 OF NESTED SWITCH 31")
			print("yep")
			infallthru('where now')
	
		elif case in caselist2: # ['where now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	
	
def nested_switch_23(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 23rd== ",exp)
	caselist1 = ['tahoe']
	caselist2 = ['cold water']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['cold water']
			print("nice")
		####################
			exp='fishy'
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_15(exp):	
	#exp = varholder[0]
	print("==NEST SWITCH 15==",exp)
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
			exp = 'cold water'
			####################
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_11(exp):	
	#exp = varholder[0]
	print("=== NEST SWITCH 11==",exp)
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("do something")
			####################
			exp = 'fallen leaf lake'
			nested_switch_15(exp) #15
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	


def main_switch(exp):	
	print("===MAIN SWITCH==",exp)
	#exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			exp = "blable"
			nested_switch_11(exp) #11
			print("just added this inbetween two nested switches")
			print('it will come thru here anyways and flow down')
			exp = 'burger'
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			break
			#infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	
'''

output string concatted together main and nested switches generated
Note: I have modified it after it was generated to get it to work for testing.
I am force feeding it currently to trigger inner switches.
##==================================================


#the difference is x input for main_switch(x)
trigger='''\n
main_switch(varholder[0]) 
'''

alltheway=[]
# this concats the strings in the list and then executes the string code
##########################################################################
def concat_items_in_list(): #add_to_list
	print("=====concat items in list()====")
	global superball
	superball =  method_defs + nestswitches + trigger +"\n"
	print(superball) 
	

concat_items_in_list()#this builds the concatted string superball
varholder[0]= '1' #input into the main 
exec(superball) #runs the switchcase
#currently trying to figure out how to do exec(superball) inside of the function above



#print("input varholder[0]=",varholder[0])
print('result[0] =',result[0])




#it's one big string
nestswitches='''

def nested_switch_66(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 66==",exp)
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("nice")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_62(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 62==",exp)
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
			exp = 'fishy'
			nested_switch_66(exp) #66
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_31(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 31==",exp)
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("INSIDE CASE 1 OF NESTED SWITCH 31")
			print("yep")
			infallthru('where now')
	
		elif case in caselist2: # ['where now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	
	
def nested_switch_23(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 23rd== ",exp)
	caselist1 = ['tahoe']
	caselist2 = ['cold water']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['cold water']
			print("nice")
		####################
			exp='fishy'
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_15(exp):	
	#exp = varholder[0]
	print("==NEST SWITCH 15==",exp)
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
			exp = 'cold water'
			####################
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_11(exp):	
	#exp = varholder[0]
	print("=== NEST SWITCH 11==",exp)
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("do something")
			####################
			exp = 'fallen leaf lake'
			nested_switch_15(exp) #15
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	


def main_switch(exp):	
	print("===MAIN SWITCH==",exp)
	#exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			exp = "blable"
			nested_switch_11(exp) #11
			print("just added this inbetween two nested switches")
			print('it will come thru here anyways and flow down')
			exp = 'burger'
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			break
			#infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	
'''

##=================================



------------========================
===MAIN SWITCH== 1
where's the dog house!
first prize
you block head Charlie Brown
kangaroo hop hop!
=== NEST SWITCH 11== blable         #one level nested
do something
==NEST SWITCH 15== fallen leaf lake #two level nested
nice
 ==NESTED SWITCH 23rd==  cold water #three level nested
nice
==NESTED SWITCH 31== fishy          #four level nested
INSIDE CASE 1 OF NESTED SWITCH 31
yep
nice
yep
nice
just added this inbetween two nested switches
it will come thru here anyways and flow down
==NESTED SWITCH 62== burger
do something
 ==NESTED SWITCH 66== fishy
do something
yep
nice
yep
nice
taught me how thru write code
mocha blast
== 31 flavors===
result[0] = 0



Thurday, dec 9th, 2021 9:45 pm PST California
	
what a journey. Just ran a multi-nested switch case in python. Unreal. I don't believe it.
It's a dream come true. Testing right now and this is the first run testing jumping around.
ACTUAL TEST OUTPUT
===MAIN SWITCH== 1
where's the dog house!
first prize
you block head Charlie Brown
kangaroo hop hop!
=== NEST SWITCH 11== blable  #one level deep witch
do something
==NEST SWITCH 15== tahoe      #two levels deep switch
do something
yep
nice
we are done here
yep
nice
just added this inbetween two nested switches
it will come thru here anyways and flow down
==NESTED SWITCH 62== burger  #one level deep switch
do something
 ==NESTED SWITCH 66== fishy  #two levels deep switch 
do something
yep
nice
yep
nice
taught me how thru write code
mocha blast
== 31 flavors===
result[0] = 0



Wednesday Dec 8th 2021 11:09 am Gilroy
testing concatting the strings together.
When the code runs it does it's calculations but it's in a balloon in a combined string.
I added a feature to get the output result from anywhere in the switch case which would
be outside of the dynamically created switch case. Right now it's in result[0].
I will have a list with many slots to grab whatever data. I will dynamically have it fill
lists to make the results of a switch case malable outside the word of the dyanmic switch case.


Tuesday Dec 7, 2021 6:14pm PST updatd 7:02pm
The famous chain methods that didn't want to work going in a sequence so yesterday I tried
doing each chain method on all of the strings to debug it more easily .. and it worked.. got snagged on fourth method
and then I debugged it.

result_of_first_method=[]
result_of_second_method=[]
result_of_third_method=[]
result_of_fourth_method=[]

print("this is after the input stings have already been seperated")
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
    



##===================================================================
## change_switch_to_method_solved : switch to nested_switchX(exp) # 
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
    
    
    
##====================================================
##  waterfall_chain_methods()  formally called do_it()
##==================================================
#the way this works is each method does all of the switch strings as a set
def waterfall_chain_methods():
    print("===watefall_chain_methods()===== ")
    for item in testlist_of_strings:
        print(item)
        print("========")#formally apple, plum, peach, orange 
    move_string_to_left_side()
    take_out_the_inner_switch_bodies_leaving_switch()
    change_switch_to_nested_switch_method()
    replace_endswitch_with_close_brace()
    #exit():

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
  
##==============	
	

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



##==========
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
		
##======
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

	
###=======
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

##========
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


	##=========
	

Putting the puzzle pieces together and testing now 
Input switch string Showing the stages here.
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
						
The chain methods convert this into the format for the parser.
						result of 4th method on string

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
}

=========
counter= 1

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
}

=========
counter= 2

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
}

=========
counter= 3

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
}

=========
counter= 4

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
}

=========
counter= 5

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
}

=========
counter= 6

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
}


going through the special parser for nested switches
this is how it looks at the next stage after I add the switch line numbers as comments after top switch
This is the result of codegen() which is (at this stage) the same codegen uses for single switches.
So this is the resulting python generation to create the same identical behavior in a C/JavaScript switch case.

exp = varholder[0]

caselist1 = ['1', '2', '3']
caselist2 = ['4', '5', '6', '7']
caselist3 = ['8', '9', '10']
caselist4 = ['default']


switch(exp)#1
while True:

	if case in caselist1: # ['1', '2', '3']
		print("where's the dog house!")
		print('first prize')
		print('you block head Charlie Brown')
		fallthru('4')

	elif case in caselist2: # ['4', '5', '6', '7']
		print('kangaroo hop hop!')
		#############
		nested_switch_11(exp) #11
		exp = 3
		nested_switch_62(exp) #62
		##############
		print('taught me how thru write code')
		fallthru('8')

	elif case in caselist3: # ['8', '9', '10']
		print('mocha blast')
		print('== 31 flavors===')
		fallthru('default')

	elif case in caselist4: # ['default']
		print('the end')
		break

	else:
		print('the end')
		break



exp = varholder[0]

caselist1 = ['blable']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)#11
while True:

	if case in caselist1: # ['blable']
		print("do something")
		####################
		nested_switch_15(exp) #15
		#############
		print("yep")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



exp = varholder[0]

caselist1 = ['tahoe']
caselist2 = ['fallen leaf lake']
caselist3 = ['default']


switch(exp)#15
while True:

	if case in caselist1: # ['tahoe']
		print("do something")
		print("yep")
		fallthru('fallen leaf lake')

	elif case in caselist2: # ['fallen leaf lake']
		print("nice")
		####################
		nested_switch_23(exp) #23
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



exp = varholder[0]

caselist1 = ['tahoe']
caselist2 = ['fallen leaf lake']
caselist3 = ['default']


switch(exp)#23
while True:

	if case in caselist1: # ['tahoe']
		print("do something")
		print("yep")
		fallthru('fallen leaf lake')

	elif case in caselist2: # ['fallen leaf lake']
		print("nice")
	####################
		nested_switch_31(exp) #31
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



exp = varholder[0]

caselist1 = ['fishy']
caselist2 = ['where now']
caselist3 = ['default']


switch(exp)#31
while True:

	if case in caselist1: # ['fishy']
		print("do something")
		print("yep")
		fallthru('where now')

	elif case in caselist2: # ['where now']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we very done")
		break

	else:
		print("we very done")
		break



exp = varholder[0]

caselist1 = ['burger']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)#62
while True:

	if case in caselist1: # ['burger']
		print("do something")
		####################
		nested_switch_66(exp) #66
		#############
		print("yep")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



exp = varholder[0]

caselist1 = ['fishy']
caselist2 = ['snow fire']
caselist3 = ['default']


switch(exp)#66
while True:

	if case in caselist1: # ['fishy']
		print("do something")
		print("yep")
		fallthru('snow fire')

	elif case in caselist2: # ['snow fire']
		print("nice")
		#############
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break


##=================================
#then each switch is framed in a method
This is the method that frames each string
####=======================================================================
##   prepare_python_switch_string_for_baking(stringname):
##   #method used: result= get_switch_number_at_top_of_string(stringname)
##========================================================================= 
def prepare_python_switch_string_for_baking(stringname):
    print('===== prepare_python_switch_string_for_baking =====')
    buildstring='';
    the_answer_is= get_switch_number_at_top_of_string(stringname)
    mynumb = the_answer_is;
    #========================== added on Fri Dec 3rd ====================
    ## this  ADDS the function name to the top  of a switch string; not tabs in front here
    if mynumb == '1': 
        buildstring += "\n\n";
        buildstring += "def main_switch(exp):"; # only triggered for main switch scenario
    else:             
        buildstring += "def nested_switch_" + str(mynumb) +"(exp):" # meaning not  1 
    #====================================================================
    ## changes switch to inswitch and fallthru to infallthru
    for line in stringname.splitlines(): #if mynumber = 1 don't change switch in main scenario
        if "switch" in line and "nested" not in line and mynumb != '1': #if switch 1 skip this
            line = line.replace("switch","inswitch")
        if "fallthru" in line:
            line = line.replace("fallthru","infallthru")
        buildstring += '\t' + line +'\n' #this adds 1 tab  to front of each line after def definition
    xmastime[0] = buildstring; 
    print(" ")
    print(xmastime[0]); 
    print(" ")
    
 #I just generated this with the code    



#this is the first switch in the switch string and by default it's labelled main_switch
def main_switch(exp):	
	exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	

def nested_switch_11(exp):	
	exp = varholder[0]
	
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

def nested_switch_15(exp):	
	exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
			####################
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

def nested_switch_23(exp):	
	exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
		####################
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

def nested_switch_31(exp):	
	exp = varholder[0]
	
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('where now')
	
		elif case in caselist2: # ['where now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	

def nested_switch_62(exp):	
	exp = varholder[0]
	
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			infallthru('more')
	
		elif case in caselist2: # ['more']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	

def nested_switch_66(exp):	
	exp = varholder[0]
	
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("nice")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	


Tuesday, Dec 7th, 2021 10:14 am PST
Nested Switch cases works.


Monday, dec 6th, 2021 6:36 pm
Chain methods finally work correctly. The chaining was no big deal it was getting the methods to behave correctly.
I can now feed the list of prepped strings to bypass205() to run thru the parser.
I already made the framing for the python output so the completion could possibly happen tomorrow.
The example uses a triple nested switch and it looks identical to if it were written in C or JavaScript
with C's behavior and look and feel using braces. I use an endswitch at the bottom of each switch though.
Though going thru the parser it is converted into a closing brace. I had some issues with the chaining but that
was only due to bugs in the methods. This was quite frustrating but I overcame it.

For testing I did all seven input strings as  list thru the first method and then waterfalled it feeding
it into the second method creating a list then the third method. After more testing I will most likely
modify it to do each method in a sequence on one string which was the original idea (for coolness). However,
I did it this way in phases to test it to make sure that it was working correctly.
I am so happy. My goal is to finish and document the program before christmas. I hope to do some test runs thru
bypass205 tomorrow. I already ran three strings the other day. The bypass parser is identical to the regular one switch 
parser but it puts the output into a list instead of executing it.

Truth be told I will have a goto label working likely by Christmas. The way it works is 
underneath it works on top of the switch case I just built.

I have been messing around with when, until, unless, and loop too. The whole project has been a test of my fortitude
and endurance. This is by far the most complex program I've ever written.




thursday, December 2nd, 2021  10:35am
Reviewing test output code that I wrote back in June and July this year.
I once worked with a guy at Fry's from Pakistan and he told me some powerful words once.
Proper planning prevents poor performance. I took those words to heart and designed the end game to make sure
that the solution would work. That working prototype fueled me with hope till the very end.
I am really glad that I thought out and made the prototpye of finished output code that I could work towards.
This code has working example of the generated python code and how it will work. I am playing with this code
right now and it's like reaching the top of El Capitan. It's the end goal and it's so simple yet compicated and
yet it works. It's all about the design and engineering simplicity to do complex behaviors.
The rush I feel right now seeing the end goal and how close I am is hard to fathom. It is like seeing a dream
materialize before my eyes that seemed utterly unattainable. I also saved in these test files the modifications to the
generated code that I need to finish the project. 


December 1st, 2021 10:39am Morgan Hill, California  Starbucks
Today is a happy day!

I think that the nested switch case feature will be working in a few days, a week at the most.
Everything part is working right now.

The crux of the problem is managing the switches at different tab locations.


First I need to get the pair ranges for where each switch  to endswitch lives called a pair.
Then I copy the string from within those two inputs and put that concatted string into a list.
This is seen below. The next phase is what I have been working on diligently for months to 
transform the separated switches into individual switchs and the inner switches within each (if they have any)
into methods that are numbered by their original line number which is tagged to each switch with a following comment.

length of columbia river = 6
now loop thru columbia river to see the switch bodies seperated
counter= 1

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

===========
counter= 2
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

===========
counter= 3
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

===========
counter= 4
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

===========
counter= 5
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

===========
counter= 6
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
								

What I worked on yesterday and today was the chain methods to prepare a switch string with nested switches
into separate switch strings. This is managed by dealing with each switch at 1 tab indentation and
the inner switches at 3 tabs indentation. There is a lot going on but the design engineering happened back in July
and the implimentation was quite tricky. But I tested what the output would be before proceeding with the code.
I am happy to report that the transformation stage is working and I can now send it to the parser.

# output is to inputstring[0]
##===================================================
##  add comment and lin number to all switches ()   ## put switch line number in
##===================================================
passinputstring=[]
smart_switch_numbers=[]
loopstring=[]
loopstring.append(0)
#twinlist=[]
passinputstring.append(0)  #get line number of switch and add number with comment to after all switches
snowman=[]
snowman.append(0)
#############################################################
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	print(" add_comment_and_line_number_to_all_switch()....this was just called .. ")
	print(" == directive 1 ==    ADD the stupid comment and line number after each switch relaly simple")
	awesome='';counter =0;newstring='';
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




#this fills the together_pair list

def empty_switch_and_endswitch_list_locations():
    print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations    #this fills the together_pair list
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
	print("this is what is in together_pair at line 254")
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
	


def testing_pair_list(): # uses together_pair list 
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

	
##===================================================
##  add comment and lin number to all switches ()   ## put switch line number in
##===================================================
passinputstring=[]
smart_switch_numbers=[]
loopstring=[]
loopstring.append(0)
#twinlist=[]
passinputstring.append(0)  #get line number of switch and add number with comment to after all switches
snowman=[]
snowman.append(0)
#############################################################
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	print(" add_comment_and_line_number_to_all_switch()....this was just called .. ")
	print(" == directive 1 ==    ADD the stupid comment and line number after each switch relaly simple")
	awesome='';counter =0;newstring='';
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
	
# uses methods:
# add_comment_and_line_number_to_all_switches
# inputs_pair_to_copy_a_string(num1,num2) #get input string from goldlist
# copy_a_nested_switch(water)
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]] 
gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]       
##=============================================================
##  split_up_big_string_into_nested_switches(myinputstring)
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

print("end of crucial test copying the strings and putting them into a list")
split_up_big_string_into_nested_switches(red_robin)
     
print("okay from this point forwards I have access to the columbia_river with the strings in it") 
     
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

	
	
	
Input string successfully translated into strings to send thru bypass205() parser.
Note: this is after line numbers have previously already added after each switch which becomes their id.
The switches are governed by 3 tabs.
	
string_name= 
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
The chain methods transforms the switch string into this output in a list.
Not all nested strings will have nested strings with them which I dealt with today.
				
Not shown here but the indentation level on the left before the switch is just 1 tab. so this makes it look off.
Notice the inner switches are now numbered nested_switch methods
				
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
	} #100  

........ 1

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
	} #60   4..........endwitch 4  line 60 3 tabs 

........ 2

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
	} #51   3 ...

........ 3

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
	} #46  2.......

........ 4

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
	} 

........ 5

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

........ 6

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
	} #77 5 .....

........ 7

###==============
##   plan B 
##================  testing converting nest string testlist_of_strings
def planB():  #november 30th, tuesday 9:45 am morgan hill starbucks 
    print("never give up")
    print('===== welcome to planB ==== november 30th tuesday===')
    print("doing planB testing each nest_list doing chain_methods")
    print("length of testlist_of_strings =",len(testlist_of_strings))
    for item in testlist_of_strings:
        print(item)
    print("====now we do the chain methods on the switch strings====")
    counter=1
    print('======== calling simulated chain methods =========')
    for item in testlist_of_strings: #test string names numbered
        print("========================")
        simulated_chain_methods(item) #testing chain methods
        print("====== counter= ",counter)
        counter += 1
        

print("the big test begins")
planB()
print("now simply loop thru the finished changes in the list")
#the new finished strings should be in hollister list all cleaned up and reduced
print("was Snoopy right and Woodstock too?")
counter =1
for item in hollister_list:
    print(item)
    print("........",counter)
    counter += 1
    
holdthis=[]
holdthis.append(0)

#this swaps endswitch with }
######################################
## take_out_endswitch(stringname)  #from bottom of nested switch 
######################################
def take_out_endswitch(stringname):
	print("take_out_endswitch called")
	galaxy = stringname
	print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	#so the whole modified string after ripping out endswitch is now in holdthis[0]
	print(holdthis[0])
	galaxy = holdthis[0] #now galaxy gets what is in holdthis[0]
	return galaxy #and this is returned
	
print("testing taking out endswitch and putting in brace")
#take_out_endswitch(old_string_test)
#print(holdthis[0])

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
def prep_nest_list_of_switch_strings_for_bypass205():
    print("====prep_nest_list_of_switch_strings_for_bypass205() ====")
    go_thru_input_major_switch_string_and_make_list_of_pairs_switch_and_endswitches() # made above
    using_pair_list_make_seperate_switch_strings_and_put_into_nest_list()             # made above
    transform_string() #DOES CHAIN METHODS  loops thru  nest_list modifies each separated string
    loop_thru_finished_list_of_prepped_strings() #thru FINISHED nest_list
    #the end result will be in nest_list with the strings ready to feed into bypass205
    
#threetabs=[[22,33],[44,66]]
#fivetabs =[[55,58],[77,86]]
#seventabs=[[88,99],[102,110]]

combined_tabs=[]
christmastree=[]

		
		
#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("")
    print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
    print("=== this is just sick bad ass ========")
    print("inputstring",inputstring);print("tabsubs ",tabsubs, " ",x)
    counter=0
    for line in inputstring.splitlines():
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
        if tab_length == x: 
            if "switch" in line and "end" not in line:
                tabsubs.append(counter);counter += 1;continue
            if "endswitch" in line:
                tabsubs.append(counter);counter += 1;continue 
    print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:print("nada")
    print("these are the tab lists from three to thirteen rudolph fly")
    print("3 and 5 tabs    =",threetabs ," ",fivetabs)    
    print("7 and 9 tabs    =",seventabs ," ",ninetabs)   
    print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   



##=================================
##  list_tabs_lists_by_depth():
##================================== 
def list_tabs_lists_by_depth():
    print("==list tabs lists by depth=====METHOD 5======>>")
    print("threetabs=" ,threetabs); print("fivetabs="  ,fivetabs);
    print("seventabs=" ,seventabs); print("ninetabs="  ,ninetabs);
    print("eleventabs=",eleventabs);print("thirteentabs=",thirteentabs) 
    
#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  #line 976
    print('====================METHOD 3 ==== line 976===>>>')
    print("this is .. build_list_input_list() ...")
    print("it gopher sees right here ",holding_themax[0])
    #holding_themax[0]
    mx = holding_themax[0] #it's using this number 
    print(type(holding_themax[0]))
    print("is it REALLY say 7  above this line???")
    if holding_themax[0] >= 3: put(3)
    if holding_themax[0] >= 5: put(5)
    if holding_themax[0] >= 7: put(7) 
    if holding_themax[0] >= 9: put(9) 
    if holding_themax[0] >= 11:put(11)
    if holding_themax[0] >= 13:put(13)
    if holding_themax[0] >= 15:put(15)
       
    print("at bottom of ifs what is in listinput")
    print(listinput)
    for item in listinput:
        super_listinput.append(item)
    print("super_listinput =",super_listinput)
  
  
  ## loops thru tabsubs and appends item to tabcount
#=========================
#  little_method(tabcount)            
#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    print(" little_method() called")
    for item in tabsubs:
        tabcount.append(item)
    del tabsubs[:]
        
        
## fill_main_pear_list(listname):  #this build the combined list correctly 
#the lists threetabs,fivetabs,seventabs,ninetabs need to already be filled
#this is just combining them together adding them together
##=====================================
def fill_main_pear_list(listname):
    print("=====fill_main_pear_list called with listname======")
    counter=0 #this must be at 0
    for x in listname:
        print(listname[counter],listname[counter +1])
        jazz = [listname[counter],listname[counter+1]]
        startime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2
        if counter >= len(listname): #prevent from going out of bounds
            break
    print("startime list=",startime)
    print("what did this work.......or not ....did it")
    if holding_themax[0]>= 3:
        fill_main_pear_list(threetabs)
    if holding_themax[0]>= 5:
        fill_main_pear_list(fivetabs)
    if holding_themax[0]>= 7:
       fill_main_pear_list(seventabs)   
    if holding_themax[0]>= 9:
        fill_main_pear_list(ninetabs)
        		
		
##============================================
## combine the lists together  #waterfall ifs
##=============================================
def combine_the_lists_together(x): 
    print("blast off test of combine_the_lists_together(x)",x)
    print("at top of combine_the_lists_together use assertion x =",x)
    print("combine_the_lists_together CALLED of the wild combine the lists of tabs pairs together so sweet now ")
    print("ASSERTIONS times") #will either be 0 or a number
    get_length_of_threetabs  = len(threetabs)
    get_length_of_fivetabs   = len(fivetabs)
    get_length_of_seventabs  = len(seventabs)
    get_length_of_ninetabs   = len(ninetabs)
    get_length_of_eleventabs = len(eleventabs)
    get_length_of_thirteentabs = len(thirteentabs)
    print(" get_length_of_threetabs =", get_length_of_threetabs)
    print(" get_length_of_fivetabs =",  get_length_of_fivetabs)
    print(" get_length_of_seventabs =", get_length_of_seventabs)
    print(" get_length_of_ninetabs =",  get_length_of_ninetabs)
    print(" get_length_of_eleventabs =",get_length_of_eleventabs)
    print(" get_length_of_thirteentabs =",get_length_of_thirteentabs)
    #test if threetabs list is empty
    print("testing if length of threetabs list GREATER THAN 0")
    if get_length_of_threetabs > 0: #then proceed there is at least one
        print("YES length of threetabs IS GREATER THAN 0",get_length_of_threetabs)
        
        if x >=  3:
            christmastree.extend(threetabs);
        if x >=  5:
            christmastree.extend(fivetabs);  
        if x >=  7:
            christmastree.extend(seventabs);
        if x >=  9:
            christmastree.extend(ninetabs); 
        if x >= 11:
            christmastree.extend(eleventabs);
        if x >= 13:
            christmastree.extend(thirteentabs);
    else:
        print('all of the tab lists are empty')
        print("don't bother trying to extend empty tab lists")
        pass
         
    print('at bottom of function combine_the_lists_together christmastree list now has')
    print(christmastree)
    print("the chrsitmastree list is what should be whole at this point HER!!!")
    
    
 #testing purposes
# this adds the tabs lists like threetabs + fivetabs + seventabs into combined_tabs list
print("== snowmen having snowball fight==testing build_tab_list_added_together(x):======")



##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("=== build_tab_list_added_together(x)======>>>>")
    print("this combines separate lists together into one list all be it clumsily")
    print("larget_tab_number =",largest_tab_number)
    del christmastree[:] #clears out the combined_tabs list to erase it
    print("about to call combine_the_lists_together wed nov 17th ")
    combine_the_lists_together(largest_tab_number)
    

#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    print("== combine tabs by length into christmastree_list======")
    print("=================METHOD 6 ======>>>>")
    themax = holding_themax[0] #this gets the highest tab level (deeply nested)
    print("where is my coffee now")
    print('let us look in the three tabs list threetabs, fivetabs, seventabs')
    print(threetabs,fivetabs,seventabs)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    print("christmastree=",christmastree)
    print("")
    
    
#================================= 
# build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    print("")
    print("build pairs with jazz ======= METHOD 7=====>>>>")
    print("")
    counter =0
    print("inside of build pairs with jazz the christmastree list show")
    print("christmastree=",christmastree)
    for x in christmastree: #loops thru at 2 at a time
        print(christmastree[counter],christmastree[counter +1])
        jazz = [christmastree[counter],christmastree[counter+1]]
        print("appending jazz to snowtime list now")
        #list snowtime starts virgin and then we append jazz pairs to it
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        ##=========================================================
        #prevents overflow error for out of range error
        print("this is the resulting pair list that is so coveted")
        print("this used the jazz pair pair system that works")
        print("snowtime list=",snowtime)
        if counter >= len(christmastree):
            break
            
            
            
            
            
            
            
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    print("")
    print("build tab depth ======= METHOD 1 =========>>")
    print("")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    print("max tab depth=",add_tab_depth[0])
            
     
            
def loop_thru_pairs_in_snowtime():
    print(" ============= #method 8 ========")
    print("snowtime list=",snowtime)
    for item in snowtime:  
        print(item);
        rad1=item[0];rad2=item[1];
        print(rad1,"and ",rad2)




##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():  #this fills the max holding_themax[0]
     print("====================  #METHOD 2 ========")
     #add_tab_depth = input
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     print("themax=",themax)

    
      
          
		
		
##=================================
## change_slot_string(counter)    this changes content of each slot in nest_list
##=================================
def change_this_slot_string(counter): #requires output[0] finished string
    print("==== change_this_slot_string(counter) ====")
    counter = int(counter)
    nest_list[counter] = output[0] #I really need to test this one and see if it works 
    #this means that needs to have finished chained_methods put into output[0]
    
##============================
## transform_string()    uses nest_list with strings in it of switch case bodies
## methods: chain_methods()
## change_this_slot_string(counter)
##============================
def transform_string():  #this calls chain_method(item) # separate switch string input
    print("==== transform_string() =12561 line number = this loops thru nest_list==")
    counter =0  #loop #this modifies the nest_list
    for item in nest_list:  #loop thru nest_list and each loop does the chain_methods
        chain_methods(item) # takes in string and does sequence methods puts into output[0]
        change_this_slot_string(counter) #changes slot string from output[0]
        counter +=1

		
		
		##======================================================================================
#the result of each of these methods will put their result in output[0]
#swap_feed_data then puts what is currently in output[0] into input[0] so it's a handoff of the baton
#each of these methods takes in input[0] as input with the result going into output[0]
#after each method we call do_pipe() which puts output[0] into input[0]
# string --> m1(input) => m2(input) => m3(input) => m4(input) => m5(input) 

##====================================================
##  first_method : modern_tab_shifter_to_left  (left indent)
##====================================================
#manipulate_string left shift indentation
def first_method(astring): #this does the left shift 
    print("manipulate_string left margin indent ===first message called..")
    #shifts string left to indent it properly CHANGED on December 1st 2021 Morgan Hill
    modern_tab_shifter_to_left(astring) #I think that this does left shift indentation
    #return astring was: astring=manipulate_string
    theresult =goldtime[0]; #outpout is put into goldtime[0]
    return theresult

##==========================================
##  second method : take_out_switch_body  from inner switches
##  uses these methods:
##  get_switch_and_endswitch_locations_in_string(astring) 
##  build_trial_inputlist()
##  convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)
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
def chain_methods(item): #this modifies just one switch string at a time
    print("==OFFICIAL== chain_methods called ====")
    print("==OFFICIAL== chain_methods called ====")
    print("==OFFICIAL== chain_methods called ====")
    print("==OFFICIAL== chain_methods called ====")
    firstresult  = first_method(item)         # modern_tab_shifter_to_left(string)
    firstresult  = goldtime[0]                # output of first_method goes into goldtime[0]
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


		
		
##=========================================
##  simulated_chain_methods():
##===================================
def simulated_chain_methods(mystring): #starting point  
    count_endswitches=mystring.count("endswitch")
    print("number of endswitches in THIS  string",count_endswitches)
    
    if count_endswitches > 1:
        print("TRUE countswitches =",count_endswitches)
        
        print("simulated_chain_methods() Rudolph the red nosed reindeer")
        print("simulated_chain_methods() Rudolph the red nosed reindeer")
        fizz  = dafirst_method(mystring) #modern_tab_shifter_to_left()
        fizzy = dasecond_method(fizz)    #take_out_switch_body()
        fuzzy = dathird_method(fizzy)    #change_switch_to_method_solved()
        frac  = dafourth_method(fuzzy)   #take_out_endswitch()
        hollister_list.append(frac)      #added to list here
    else: 
        print("count_endswitches=",count_endswitches)
        #no nested switch in this switch string
        modern_tab_shifter_to_left(mystring)#modern_tab_shifter_to_left() shift indentation
        astring = goldtime[0] #its output
        finalresult=take_out_endswitch(astring)#take_out_endswitch()
        mystring=finalresult
        hollister_list.append(mystring) #added to list here		

#chain methods below 
#manipulate_string left shift indentation
def dafirst_method(astring): #this does the left shift 
    print("first message called..modern_tab_shifter_to_left")
    #shifts string left to indent it properly
    modern_tab_shifter_to_left(astring) #I think that this does left shift indentation
    astring = goldtime[0]
    return astring
    
#take_out_switch_body
def dasecond_method(astring): #cuts out switch body leaving switch word in all occurances
    print("seconed method called...take_out_switch_body")
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #this is new to see if it works=========
    return astring


#change_switch_to_method_solved
def dathird_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method called...change_switch_to_method_solved")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    return finalresult


#take_out_endswitch(stringname)
def dafourth_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method called..take_out_endswitch().")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring)
    return finalresult
    
hollister_list=[]				


		
		
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
	passthis[0]= n
	print("n =",n)

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
    # concatting the buildstring here 
        for line in the_nest_string.splitlines():
            buildstring += line[n:] +'\n' #this cuts out n tabs from the front of this line
    goldtime[0] = buildstring #output is in goldtime[0]
    #this prints out the result of the concatted uildstring
    for line in buildstring.splitlines():
        print(line)
    print('testing it now after changing the string')


##=================================
## take_out_switch_body(astring):  #def foxnews(astring):
##================================
def take_out_switch_body(astring): #this was foxnews
    print("take_out_switch_body      today is november 28th sunday  4:29 pm ")
    get_switch_and_endswitch_locations_in_string(astring) #for this switch string
    build_trial_inputlist()	 #this is new 
    convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)		

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
	print("string_name=",string_name)
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
			print(line) #it won't print the switch word since it's skipping it
			counter += 1; continue
		else: 
			concatthis += line + "\n"; counter += 1; continue
	print('it created this SILLY STRING === multi colored silly string=')
	print(concatthis)
	print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
	weasel=string_after_cutting_out_inner_switch_body[0]
	for line in weasel.splitlines():
		print(line)
	#return weasel  #I need to return from each for the piping to work correctly
	lightning[0] = concatthis
	for line in lightning[0].splitlines():
	    print(line)

		
##=========
Tuesday, November 30th, 2021  2:10 PM PST Hollister,California Starbucks.
Previous version of indenting to left works without errors after extensive testing.

Fixed bug in cutting out body of inner switches. 
I can now run chain_methods on each string to prepare each of the input switch strings for bypass205().
This section started back in August. It's the last day of November and with persaverance I got it working.
Relieved. 

separating the switch strings from the main initial switch with nested switches here
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
##========================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("THIS MAKES SWITCH AND ENDSWITCH PAIRS BY TAB LEVELS")
    #welcome to - time 10;43 am nov 9th-")
    print("this is unreal; this_makes_switch_and_endswitch_pairs_by_tab_levels()")
    build_tab_depth(inputstring)                           #METHOD 1
    get_max_tab_number_in_list() #fills holding_themax[0]  #METHOD 2
    build_list_input_list()                                #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels()        #METHOD 4
    list_tabs_lists_by_depth()                             #METHOD 5
    combine_tabs_by_length_into_christmastree_list()       #METHOD 6 together
    build_pairs_with_jazz()  #combines into sublist        #METHOD 7 in christmas list
    loop_thru_pairs_in_snowtime()                          #METHOD 8
    
        
     
 
fox=[]  #this is just a simple test 
def wildtest(themax):
    print("themax =",themax)
    print("called wildtest to add to list")
    if themax == 3: 
      fox.append(3) #.append(3)
      
    if themax == 5: 
      fox.append(5)
      
    if themax == 7: 
      fox.append(7)
      
      
    #if themax == 9: fox = [3,5,7,9]
    #if themax == 11:fox = [3,5,7,9,11]
    #if themax == 13:fox = [3,5,7,9,11,13]
    #if themax == 15:fox = [3,5,7,9,11,13,15]

print("starting fox list =",fox)
#wildtest(3)   
#wildtest(5)   
#wildtest(7)  
print("fox list =",fox)
print("above it should say 3,5,7")
print("road to tahoe is up hill")



#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    print("== combine tabs by length into christmastree_list======")
    print("=================METHOD 6 ======>>>>")
    themax = holding_themax[0] #this gets the highest tab level (deeply nested)
    print("where is my coffee now")
    print('let us look in the three tabs list threetabs, fivetabs, seventabs')
    print(threetabs,fivetabs,seventabs)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    print("christmastree=",christmastree)
    print("")
    
    
    '''
    if input == 3:
        print('3 total in themax')
        christmastree = threetabs
    if input == 5:
        print('5 total in themax')
        christmastree=threetabs +fivetabs
    if input == 7:
        print('7 total in themax')
        christmastree=threetabs +fivetabs + seventabs
    if input == 9:
        print('9 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs
    if input == 11:
        print('11 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs  + eleventabs 
    if input == 13:
        print('13 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs + eleventabs + thirteentabs
     '''
       
         



#================================= 
# build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    print("")
    print("build pairs with jazz ======= METHOD 7=====>>>>")
    print("")
    counter =0
    print("inside of build pairs with jazz the christmastree list show")
    print("christmastree=",christmastree)
    for x in christmastree: #loops thru at 2 at a time
        print(christmastree[counter],christmastree[counter +1])
        jazz = [christmastree[counter],christmastree[counter+1]]
        print("appending jazz to snowtime list now")
        #list snowtime starts virgin and then we append jazz pairs to it
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        ##=========================================================
        #prevents overflow error for out of range error
        print("this is the resulting pair list that is so coveted")
        print("this used the jazz pair pair system that works")
        print("snowtime list=",snowtime)
        if counter >= len(christmastree):
            break
            
            
            
            
            
            
            
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    print("")
    print("build tab depth ======= METHOD 1 =========>>")
    print("")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    print("max tab depth=",add_tab_depth[0])
            
      
      
      
      
      
            
            
def loop_thru_pairs_in_snowtime():
    print(" ============= #method 8 ========")
    print("snowtime list=",snowtime)
    for item in snowtime:  
        print(item);
        rad1=item[0];rad2=item[1];
        print(rad1,"and ",rad2)




##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():  #this fills the max holding_themax[0]
     print("====================  #METHOD 2 ========")
     #add_tab_depth = input
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     print("themax=",themax)

		
		
combined_tabs=[]
christmastree=[]

##============================================
## combine the lists together  #waterfall ifs
##=============================================
def combine_the_lists_together(x): 
    print("blast off test of combine_the_lists_together(x)",x)
    print("at top of combine_the_lists_together use assertion x =",x)
    print("combine_the_lists_together CALLED of the wild combine the lists of tabs pairs together so sweet now ")
    print("ASSERTIONS times") #will either be 0 or a number
    get_length_of_threetabs  = len(threetabs)
    get_length_of_fivetabs   = len(fivetabs)
    get_length_of_seventabs  = len(seventabs)
    get_length_of_ninetabs   = len(ninetabs)
    get_length_of_eleventabs = len(eleventabs)
    get_length_of_thirteentabs = len(thirteentabs)
    print(" get_length_of_threetabs =", get_length_of_threetabs)
    print(" get_length_of_fivetabs =",  get_length_of_fivetabs)
    print(" get_length_of_seventabs =", get_length_of_seventabs)
    print(" get_length_of_ninetabs =",  get_length_of_ninetabs)
    print(" get_length_of_eleventabs =",get_length_of_eleventabs)
    print(" get_length_of_thirteentabs =",get_length_of_thirteentabs)
    #test if threetabs list is empty
    print("testing if length of threetabs list GREATER THAN 0")
    if get_length_of_threetabs > 0: #then proceed there is at least one
        print("YES length of threetabs IS GREATER THAN 0",get_length_of_threetabs)
        
        if x >=  3:
            christmastree.extend(threetabs);
        if x >=  5:
            christmastree.extend(fivetabs);  
        if x >=  7:
            christmastree.extend(seventabs);
        if x >=  9:
            christmastree.extend(ninetabs); 
        if x >= 11:
            christmastree.extend(eleventabs);
        if x >= 13:
            christmastree.extend(thirteentabs);
    else:
        print('all of the tab lists are empty')
        print("don't bother trying to extend empty tab lists")
        pass
         
    print('at bottom of function combine_the_lists_together christmastree list now has')
    print(christmastree)
    print("the chrsitmastree list is what should be whole at this point HER!!!")
    
    
 #testing purposes
# this adds the tabs lists like threetabs + fivetabs + seventabs into combined_tabs list
print("== snowmen having snowball fight==testing build_tab_list_added_together(x):======")



##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("=== build_tab_list_added_together(x)======>>>>")
    print("this combines separate lists together into one list all be it clumsily")
    print("larget_tab_number =",largest_tab_number)
    del christmastree[:] #clears out the combined_tabs list to erase it
    print("about to call combine_the_lists_together wed nov 17th ")
    combine_the_lists_together(largest_tab_number)
    
		
	
##==================================================
## make_switch_and_endswitch_pairs_by_tab_levels() 
##=================================================== 
def make_switch_and_endswitch_pairs_by_tab_levels(): 
    print("make_switch_and_endswitch_pairs_by_tab_levels()")
    print(":=============== METHOD 4 ======") 
    for item in super_listinput:     # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)
		
		


#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("")
    print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
    print("=== this is just sick bad ass ========")
    print("inputstring",inputstring);print("tabsubs ",tabsubs, " ",x)
    counter=0
    for line in inputstring.splitlines():
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
        if tab_length == x: 
            if "switch" in line and "end" not in line:
                tabsubs.append(counter);counter += 1;continue
            if "endswitch" in line:
                tabsubs.append(counter);counter += 1;continue 
    print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:print("nada")
    print("these are the tab lists from three to thirteen rudolph fly")
    print("3 and 5 tabs    =",threetabs ," ",fivetabs)    
    print("7 and 9 tabs    =",seventabs ," ",ninetabs)   
    print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   
		
        
## loops thru tabsubs and appends item to tabcount
#=========================
#  little_method(tabcount)            
#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    print(" little_method() called")
    for item in tabsubs:
        tabcount.append(item)
    del tabsubs[:]
        
        
        
tabsubs=[]
threetabs=[]
fivetabs=[]
seventabs=[]
ninetabs=[]
eleventabs=[]
thirteentabs=[]
fifteentabs=[]

#used by the super duper function with 6 methods in it
#===============================

first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot
christmastree=[]
second=[]   #this takes an inputstring which is the combined switchcase big string
slydog=[]
snowtime=[]
mylistinput=[]
#===========================
super_listinput=[]

def put(x):
    listinput.append(x)

#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  #line 976
    print('====================METHOD 3 ==== line 976===>>>')
    print("this is .. build_list_input_list() ...")
    print("it gopher sees right here ",holding_themax[0])
    #holding_themax[0]
    mx = holding_themax[0] #it's using this number 
    print(type(holding_themax[0]))
    print("is it REALLY say 7  above this line???")
    if holding_themax[0] >= 3: put(3)
    if holding_themax[0] >= 5: put(5)
    if holding_themax[0] >= 7: put(7) 
    if holding_themax[0] >= 9: put(9) 
    if holding_themax[0] >= 11:put(11)
    if holding_themax[0] >= 13:put(13)
    if holding_themax[0] >= 15:put(15)
       
    print("at bottom of ifs what is in listinput")
    print(listinput)
    for item in listinput:
        super_listinput.append(item)
    print("super_listinput =",super_listinput)
  
  
		
plums=[]
plums_data=[]
endswitchlinenumbers=[]
endtabslist=[]

print("did we make it here......")
##=============================================================
## magic_potion   saturday september 18th, 2021 time 11:14 am
##=============================================================
def magic_potion(inputstring):
    print("============== magic_potion() called ============")
    print("================....===========")
    print("  ===== switch matrix adding...")
    for line in inputstring.splitlines():
        print(line)
    #switch_count=0    
    switch_count = 0 #for first
    #switchlinenumbers.append(0) #skips 0 not counted
    counter =0
    newstring='data on analyzing a multinested string to number the switches and tabs' + "\n"
    collosal=''
    print("This  finds the switch locations ----")
    for line in inputstring.splitlines():
        if "switch" in line and "endswitch" not in line:
            print(line)
            tabsnow= line.count("\t")
            tabslist.append(tabsnow)
            switchlinenumbers.append(counter)
            switch_count += 1
            bump =''
            if tabsnow == 1:
                bump = " "
            else:
                pass
            newstring +=  "sw_order_num= " + str(switch_count) + " " + "switch_line=" + str(counter) + bump + " tabs =" + str(tabsnow) +  "\n" 
            collosal = [str(switch_count),str(counter),str(tabsnow)]
            peach_data.append(collosal)
            counter += 1
        else:
            #newstring += "\n"
            counter += 1
    #del switchlinenumbers[0]        
    print("switchlinenumbers",switchlinenumbers)
    print("tabslist=",tabslist) 
    print("now we will print out what it sees")
    print("switch counter,switch line number,tab length")
    print(peach_data)
    print("=======")
    print("insert 000 in first data ")
    peach_data.insert(0,[0,0,0]) #this is to eliminate computer math with 0
    for item in peach_data: #already filled
        print(item)
    		
		
		
		
		
		
		
		
		
		
		
		

Tron Rises. Sat Nov 27th, 2021 5:19pm
Finally got taking out inner switch bodies at 3 tabs working. 
Now I will test changing to nested_switch method numbered . What an ordeal to get it stable. Works now.


9:22am Nov 23rd, 2021 PST
Tron Music
https://www.youtube.com/watch?v=I22AqV9zV50
	
Testing the chains methods thoroughly and chaining them together today.
They are each verified to be correct for all scenarios.
Total rush seeing it all come together.
This section deals with setting up the input switch strings for the parser bypass205() to handle a switch
with unknown numbers of nested switches initially at unknown depths until they are analyzed.


#testing
#INPUT STRING
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
#OUTPUT String
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 ==========
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 ===============
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====

stringname=spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start=1,finish=1)
print("did this sucker work tuesday november 23?")

#this was redesigned and modified on sunday november 21st at 8:30am to 
# work with skipping some lines with no known locations of inner switches at 3 tabs
# and it calls method build_pair_list to find them and reverse them for input for skipping_some_lines
# and I have to subtract 1 from start and finsh
#this one is used to get the main switch and take out switches at 3 tab depth
##===========================================================================
##  modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
def modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    ###======= this is ingenius=========
    #METHOD BUILD_PAIR_LIST(STRINGNAME) 
    # and loops thru list feeding start and finish  params and calling skipping_some_lines()
    #the input for start and finish will be 1 by default but they will be overwritten
    #by the build pair list on-the-fly.
    build_pair_list(stringname)           # goes thru thenewpairs list and
    for item in thenewpairs:              # fills start and finish into skipping_some_lines params
        start = item[0];finish = item[1]; # print("start,finish=",start," ",finish)
        skipping_some_lines(stringname,start-1,finish-1)#so close now 
    #this means that the output string should be placed into never_defeated[0]
    print("let us see what we have jazz blues.")
    for line in never_defeated[0].splitlines(): #prints it after takening out. 
        print(line)
	

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
	############################
	#REVERSE THE NEWPAIRS LIST BECAUSE IT HAS TO BE DONE BOTTOM UP TO THE STRING 
	############################
	thenewpairs.reverse() #they have to be skipped bottom up to work properly
	print("thenewpairs=",thenewpairs)	



##===========================================
##  skipping_some_lines() #this works
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("======= skipping_some_lines() ================called",start,finish)
	# if I have a flag that it's been triggered then afterewards 
	# print("this is the input string used stating skipping_some_lines")
	# for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
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
		
	for line in x.splitlines(): #smart = x
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
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
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

	
	
	
	
	


9:26 am PST testing piping between chain methods now.
	
Piping works. Nov 20th, 2021  11:00am PST So chaining methods works. This means feeding the output from a method
as input for the next method in a chain (a line of methods).

Saturday, Nov 20th, 2021  9:06 am
Last major chain method confirmed working!

Flow Zone Trance concentration music:
https://www.youtube.com/watch?v=veHqJSC-9Lo
		

I will now pipe the methods together and apply them to each input string in list.
The rest is gravy and simple to impliment. Likely tomorrow morning the pre-parser code will be golden.
The half after the parser dealing with the python code is simple to put together with the methods already working.
INPUT sample strings looked like this:
		switch(exp) #11
		case 'blable':
			print("do something")
			####################
			switch(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47
=======testing if { taken out of string=======
confirmed switchh in line and tabdepth3
===== oh yeah =====

	switch(exp){ #49
		case 'burger':
			print("do something")
			####################
			switch(exp){ #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73

				
OUTPUT:
	===== oh yeah =====
we made it to the top of the Donnor Summit 
counter= 1

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
			nested_switch_49(exp) #49

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
counter= 2

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
	endswitch #47
counter= 3

	switch(exp) #49
		case 'burger':
			print("do something")
			####################
			nested_switch_53(exp) #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73
counter= 4

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
	endswitch #38
counter= 5

	switch(exp) #53
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
counter= 6

	switch(exp) #23
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
end of the show time movie trailer

### code below

##===================================================
## change_switch_to_method_solved(inputstring):
##====================================================

#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    print("====== change_switch_to_method_solved(inputstring)=== get the money now====")
    innerswitch=''
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default se tting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
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
        for line in inputstring.splitlines():
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
                thisline= thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else:
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
    ### end of function =======================================================
    

    



###================== cold brew linus and snoopy ================== saturday morning software  november 20th, 2021 ====
#this is testing adding the nested switch 
linus_and_snoopy=[]
##==================================
##   add_nested_switch_methods():
##==================================
def add_nested_switch_methods():
    print("add nested_switch_methods() in catching_first_change list")
    for item in catching_first_change:
        print(item)
        #here calling method chaning_switch_to_method_solved swaps switch for nested_method_numbered
        fizz =change_switch_to_method_solved(item)
        print("===== oh yeah =====")
        linus_and_snoopy.append(fizz)
       



##================================================
##print_out_result_of_adding_nested_switch():
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




Fri Nov 19th, 2021
Utter disbelief. Just fixed some code and got more working.
Adding working functionality on the fly to chain methods
shift to left works
cut out inner switch bodies works
both on the fly applied to a list.

https://www.youtube.com/watch?v=I22AqV9zV50   Tron music - pretty dam good.
getting cutting out the inner switch bodies had some simple but slightly perplexing logic bugs but
I ironed them out.

The rush is phenomenal seeing the nested switch starting to come to life. It's alive!

the first two methods were challenging. The second one was a real mother of a bitch. I just kept breaking
the code down to smaller methods to manage the complexity.

three more methods to go for chain methods. They work. Just making them work on their own now with no help.

#output looping thru list

now big test of second chain method #taking out switch bodies
this should print out 6 stritngs
counter= 1

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
			exp = 3
			switch(exp){ #49

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

=========
counter= 2

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
	endswitch #47

=========
counter= 3

	switch(exp){ #49
		case 'burger':
			print("do something")
			####################
			switch(exp){ #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73

=========
counter= 4

	switch(exp){ #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #23
			#############
			break
		default:
			print("we are done here")
	endswitch #38

=========
counter= 5

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

=========
counter= 6

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

=========
code working for taking out inners witch bodies before sending it to parser.
Will test convert inner switch to nested method next.
		
Raw code that works before cleaning it up. Fully worked just now.
		
		

flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
##===========================================
##            skipping_some_lines() #this works
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("skipping_some_lines() called",start,finish)
	#if I have a flag that it's been triggered then afterewards 
	#print("this is the input string used stating skipping_some_lines")
	#for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
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
	for line in x.splitlines(): #smart = x
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		# if counter is between start and finish #just after start and less than = to finish
		#just added start +1 and finish + 1
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
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
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
		
	#print(ibm[0])
		#just moved this over one tab	
#end skipping_some_lines  ========================================================
print("Levels TEST on wonderful Monday winter wonderland ")
print("this will take out the inner switch between") 
never_defeated=[]
never_defeated.append(0)

for line in skitahoe.splitlines():
    print(line)

##===========================================================================
##  cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    skipping_some_lines(stringname,start,finish)
    #this means that the output string should be placed into never_defeated[0]
    for line in never_defeated[0].splitlines():
        print(line)
        
stringname=skitahoe; start=7; finish = 14; #this sucker was moving....    
cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)

print(" RED RED RED cut out switch body leave only switch word baby red alert testing cut out switch body leaving switch word tesitng 4 ..")    
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
		skipping_some_lines(thestring,start,finish)
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
	#do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring):
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
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	print("THIS NEEDS TO WORK NOW==")
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("did this baby finally get called  1")
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
	## adding resultof output of methods of taking out inner switches into never_defeated[0]
	## which is put into list fullhouse using append
	fullhouse.append(never_defeated[0])
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""
	



#print("====STARTING ATTEMPT 1====== charlie brown music is the best jazz ====")


#take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)


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

#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
def try_the_mocha():
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    print("let us see the strings in this list")
    for item in catching_first_change:
        print(item)
    print("===== okay is this it ===")
    
    print("length of catching first change should be 6",len(catching_first_change))
    counter=0  #this is running the method for second stage of chain_methods
    for item in catching_first_change: #funtestlist: #strings in funtest list
        weasel = item
        ## determines if there is an inner switch in THIS string ==========
        determine_if_inner_switch_inside_of_this_switch_string(weasel)
        #print("determine if inner switch at 3 tabs depth in this switch string ")
        innerswitch= result_of_check_if_inner_switch[0]
        print('innerswitch if true or false it is .. =',innerswitch)
        if innerswitch == True:  #if there is an inner switch then apply the method below  
            take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
        else:
            #this is new as of fri nov 19th 
            #if no inner switch then just add the switch string to fullhouse list
            #print("just added this in situation where no inner switches in string in list")
            print("========= nov 19th friday debugging ==")
            print("this is new ")
            print("if inner switch == False then add weasel to fullhouse")
            fullhouse.append(weasel)
            #this means no innerswitch in this switch string 
            pass  #it's False no inner switch
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




	
	


Monday, Nov 15th, 2021
What this does is prep the string before it is fed into bypass205() which calls the parser individually
for each input switch string.
I already tested and verified that my pair list of switch endswitches works and that 
a list made up of the pairs is correct.

Testing chain methods individually then will test as a chain using piping now called do_pipe()
All of the methods in chain methods now verified to work.
do_pipe() works. Note. Python has a pipe() method for the os therefore I changed my pipe name to do_pipe().
Will next test chain_methods() together with all cylinders running. time 9:40 am. Nov 15th
	
	
Afterwards I will then work on post parser on python switch stings output combining.



Sunday morning nov 14th, 2021 working on method chaining still.

input=[]
input.append(0)

output=[]
output.append(0)


##=====================
##   get_final_finished_string()
##=====================
def get_final_finished_string():
    print("output[0]=",output[0])
    print("=== result is in output[0] ===")
    for line in output[0].splitlines():
	print(line)
    
##=====================
##   do_pipe()
##=====================
def do_pipe():
    input[0] =''
    input[0] = output[0]


##=====================
##   initialize_lists()
##=====================
def initialize_lists():
    input[0] =''
    output[0]=''
   
    
##=================================
## change_this_slot_string(counter)
##=================================
def change_this_slot_string(counter):
    counter = int( counter)
    nest_list[counter] = output[0]
   
    
##============================
## transform_string()    uses nest_list with strings in it of switch case bodies
##============================
def transform_string():
    counter =0
    for item in nest_list:
        chain_methods(item)           #this does the sequence of methods to one string 
        change_this_slot_string(counter) #this replaces the string in the slot with the modified string
        counter +=1

##==================================================
## loop_thru_finished_list_of_prepped_strings():
##==================================================
def loop_thru_finished_list_of_prepped_strings():
    counter =0
    for item in nest_list:
        print(item)
        print("counter=",counter)
        print("===========")
        #this will then append and build the quail list for input to bypass205()

# code name waterfall
##=======================
##  chain_methods()
##========================
#using descriptive names not true method names yet
def chain_methods(item):
    print("==== chain_methods called ====")
    initialize_lists() #clears out input[0] and output[0]
    input[0] = item #this captures the string 
    add_comment_with_number_to_top_switch(input[0]);do_pipe()
    shift_string_to_left_by_reducing_tabs(input[0]);do_pipe()
    cut_out_switch_bodies_at_3_tabs_depth(input[0]);do_pipe()
    swap_switch_with_nested_switch_number(input[0]);do_pipe()
    replace_the_last_endswitch_with_brace(input[0]) 
    get_final_finished_string() #in output[0] prints it out to see it










##=================================================================================

saturday morning, nov 13th, 2021
== Method Chaining ==
# I knew that Ruby had method chaining and thought it would be cool if Python could do chaining.
# of course it uses a some fancy code but it will work. It's a matter of how its implimented.
indent_to_left.add_comment_to_switch.cut_out_switch_bodies.swap_switch_with_nest_method.add_brace()
# it will be implimented like this:
method_chaining("method1.method2.method3.method4.method5()") #only way I can get away with using dots(.)
# put into a list in the same order as in the argument param
# it is fed the starting var data in list input[0]
# and the resulting result string is in  output[0]

I was thinking about applying each method individually to the list and looping thru 
it and thought that was inefficient and wondered if there was a way to simulate chaining to 
get the same effect and gain the efficiency and elegance of doing a chain of methods and 
just how it would work and be possible to impliment. 

Late last night an idea popped into my head and I quickly figured out how to make it work.
Chaining methods. For the pre-parser I need to call up to ten methods that are applied individually
to each string and that would have meant looping through all of the strings in a  list each time.
With this solution I just do one loop and apply the method chain to each string just once.
Wrote code at midnight last night and will test it today.

#Raw design code last night at midnight.
##======================================
## change_slot_string(counter)
##======================================
def change_slot_string(counter):
  counter = int( counter)
  nest_list[counter] = output[0] #nest_list is name of list that can become an input param

	
#A method that calls a series of methods really utilizing output from previous method
##======================================
## transform_string()
##======================================
def transform_string():
    counter =0
    for item in nest_list:
      chain_method(item)
      change_slot_string(counter)
      counter +=1

##======================================
## feed_data()
##======================================
def feed_data():
  input[0] =“”
  input[0] = output[0]


	
# waterfall #this will be generated
##======================================
## chain_method(item) 
##======================================
def chain_method(item):
  input[0] = item
  output[0] = method1(input[0]);feed_data()
  output[0] = method2(input[0]);feed_data()
  output[0] = method3(input[0]);feed_data()
  output[0] = method4(input[0]);feed_data()
  output[0] = method5(input[0]) 

	
#Result in output[0]
Indent to left margine
Add comment to switch
Cut out switch body at 3 tabs deoth
Swap switch with nested switch
Replace bottom endswitch with brace

Each method stage all five in sequence to a string

Chain the methods output to list[0]
Then that list is input to next method
Input[0] string method name
Put change into output[0]
Transfer then input[0] = output[0]





fri, nov 12th, 2021 11:30am
	
coding music today: https://www.youtube.com/watch?v=ckmh6FvHidQ
		
I need to loop thru the quail string list of nested switches and take out the inner switch bodies
and then replace the switch word that is an inner switch with a nested_method numbered.

Almost forgot. Found my code to indent initial switch strings that are deeply indented and reduces the
tab count so it is aligned correctly to the left margine with the proper indentation.

	
There are two phases involved here. The preparation of a switch string before it goes into bypass205
and secondly taking the output python generated code (for each switch string) from the parser and
combining them together for a switch with nested switches which is then finally executed.
First half is modifying the input JavaScript style switch string and preparing it for the parser.
Second half is adding elements to the output python switches strings and combining them.
I had to break the problem in half to manage the complexity. The first half I thought would take a week.
It has taken three months but I solved it so I am nonetheless still ecstatically happy.
The second half is super easy and works. I have done extensive testing of how and what the code will do
so I am 100 percent confident it will all work. The speed bumps have been the limitations of Python so I 
have been making methods to simplify the obfuscated nature and bizzare way that python does things.

#this is a sample of output python code generated by the parser 
#what remains is adding the def methodname at the top - added to the top of the string
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
	
Full steam ahead dash to the finish line in 5th gear.
Working on the transformation of the output python switch code which is a while True loop with ifs.
Reviewed my code and found and then rewrote code to add  "def nested_switch + number + (exp)" on top of
output python switch code. I then modified get number after inswitch() after # . That works smoothly now.

I still have a few more items to modify the switchcode to prepare it before it goes into the parser.
in quail list of separated string things to do (steps)
have to replace inner switches (cut out inner switch bodies leaving just switch word)
get number from  comment after switch of line number (that works)
Need to replace inner switch word with nested_switch method + number
take out excess tabs in front of switch cases so it's uniform
Have to make the main switch string with nested switches at 3 tabs replaced by methods

In review the parser is designed to do only one switch string and convert it into python representation.
Therefore I use a special extension called bypass205 that does any number of inputs switch strings
in a list and fills the stanford list but does not execute the code. They are each managed separately.

##======================================================================================================

Nested switches (that look just like C switch cases ... will be working by 
this weekend and the whole modules for switch and nested switch
will be on github. It's been a wild ride. What a roller coaster. So much logic. 

Massive momentum today after solving bugs late last night till midnight to outthink Python's peculiarities.
Super progress this morning got me over the hump and now I am going full speed ahead.
https://www.youtube.com/watch?v=sRvEwXDxz_I
	
https://www.youtube.com/watch?v=ZwY4YPxTufs
	
https://www.youtube.com/watch?v=FbbCHWQZ70o

I will start sending the seperated strings to the parser in bypass205 likely tomorrow. What a rush. I am so thrilled
by my recent progress. 

Thursday, Nov 11th, 2021  10:36am PST
What a rush. By the way it also takes out braces if they exist. Next I will loop thru the list of seperated strings and apply this to each switch string
that has more than one switch within it meaning at least 1 switch. So it will test for if string.count("switch") >= 2 and string.count("endswitch") > 1
swap inner switches to methods works automatically for all switches at 3 tabs length in a string.
I wrote it on halloween and just retested it.
INPUT example 

jazz6='''
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
			####################
			switch(exp){ #77  
			#############
			break
		case 'what':
			print("nice")
			####################
			switch(exp){ #88  
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''
OUTPUT
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
			####################
			nested_switch_77(exp) #77
			#############
			break
		case 'what':
			print("nice")
			####################
			nested_switch_88(exp) #88
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86
Yes, I know wait what about the input for (exp) for each switch. I will add that line above later. it's trivial.

Code to do the magic.
print("about to do thorough testing of chnage_switch_to_method_solved()")
#solved october 29th, 2021  NEXT get the number after comment just in time
'''
this builds a string called newstring replacing switches
at 3 tabs depth with nested_switch
with the comment id after # tacked onto
 the end of the nested_switch_22(exp) like so.
'''
#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    print("====== change_switch_to_method_solved(inputstring)=== ====")
    innerswitch=''
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default se tting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    if innerswitch == True:
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
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():
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
                thisline= thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else:
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
        #this is what we return the inputstring
        return inputstring; #no changes made 
    ### end of function ===============================
    
print("where is my mocha brainfreeze test october 30th...")

print("==========testing string da===================")
print("=============================")


And testing code here:
	
inputstring=''
inputstring = da         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
    
print("=============================")
print("======= testing string data1======================")
    
    
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





thursday, nov 11th, 2021 9:09 am Pacific Time
Cutting out inner switch bodies at 3 tabs works on-the-fly automatically. sweet. 
This is yet another victory in the tranformation of the input switch code to prepare it for the parser.
Next I will swap out the inner remaining inner switch words with a nested_switch numbered.
This morning had some weird bugs and they were only rectified by using listname.clear() 
The method loops thru a list of the strings which are in a list of the separated switch strings.
#I will beautify the code later. Just getting it all working right now.

funtestlist=[samplestring,samplestringzoo1] #samplestringzoo1
#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
def try_the_mocha():
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    counter=0
    for item in funtestlist:
        take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
        counter += 1
    print("len(fullhouse)=",len(fullhouse))
    for item in fullhouse:
        print(item)
	
try_the_mocha() ##<<===== method called
##============================================================================
##  take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word
##----------------------------------------------------------------------------
##  Methods: make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
##  Methods: loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
##  Methods: skipping_some_lines(x,start,finish)
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("did this baby finally get called  1")
	print("called ....take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)") 
	make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
	loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
	print("list_of_inner_switches_at_three_tabs=", list_of_inner_switches_at_three_tabs)
	print("list_of_inner_endswitches_at_three_tabs=", list_of_inner_endswitches_at_three_tabs)
	print("pairset=",pairset)
	fullhouse.append(never_defeated[0])
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""

##====================================================================
##  make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring)
##====================================================================
def make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):
	print("did this baby finally get called  2")
	print("METHOD make_Pair_set_of #### called  ... make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):")
	counter =0
	for line in inputstring.splitlines(): #smart = x
		#print(line) the line still exists even if I don't print it out
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
	print("now I need to make pairs")
	get_number = len(list_of_inner_endswitches_at_three_tabs)
	if get_number > 1:
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	else:
		pass #print("there is only one switch endswitch so do regular mode just one inner switch at 3 tabs ")
	pairset.reverse()
	print(pairset)
	print("loop thru pairset") #to go thru input string and reduce inner switches to just switch word bottom up
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
		
		
##========================================================
## loop_thru_pair_set_and_call_skiplines(samplestring)
##=========================================================
def loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring):
	print("did this baby finally get called  3")
	print(" =============== the waving American Flag ===========")
	print('right here never_defeated length = 0 meaning it is empty')
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
		skipping_some_lines(thestring,start,finish)
		#doing this to see if it cut out the inner switch body 
		print("this is showing the changes reducing switches in never_defeated[0]")
		mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
		print("this is what the switch string looks like after taking out a switch body")
		counter += 1
	

	
pairset=[]
genius=[]
genius.append(0)

never_defeated=[]
never_defeated.append(0)
list_of_inner_switches_at_three_tabs=[]
list_of_inner_endswitches_at_three_tabs=[]


flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
##===========================================
##            skipping_some_lines()
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("skipping_some_lines() called",start,finish)
	#if I have a flag that it's been triggered then afterewards 
	#print("this is the input string used stating skipping_some_lines")
	#for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
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
	for line in x.splitlines(): #smart = x
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		# if counter is between start and finish #just after start and less than = to finish
		#just added start +1 and finish + 1
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
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
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
		
	#print(ibm[0])
		#just moved this over one tab	
#end skipping_some_lines  ========================================================


#INPUT

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

#OUTPUT


	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
			print('taught me how to write code')
			fallthru
			
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======28       
			fallthru
		
		default:
			print('the end')
}


	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
			print('taught me how to write code')
			fallthru
			print('hello world')
			switch(exp){  # ===== 24===== 3 tabs, 2nd case , line 2 in this case, 1 in series
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======39       
			fallthru
		
		default:
			print('the end')
}

#did it work razzle dazzle pumpkins

Wednesday, November 10th, 2021
PUtting code up on github in case my laptop dies. As an emergency backup.
Lots of files. Code nearly done, days away, but I don't want to risk losing it if my laptop crashes.

Gaining Steam and accelerating. I now have momentum and it feels great seeing it reach completion.
I have the following working and connected.
Go thru input multi switch string
make pairs list of switch and endswitches by tab depth
add sublists together for one list of switch, endswitch pairs
separate switch strings using pairlist and put nested string into a list

if a switch string has a nested switches at three tab depth then reduce switch bodies to just switch word.
Next I will add the methods to replace inner switch with nested_switch_numbered making it into a method.
This now works using fuzzy logic and can deal will multiple inner switches. I used my macro trick
and change the string from bottom up so that the pair numbers are still valid that I used to access the string.

#hardest parts over, the rest I have working methods and functions so I'm just methodically putting it together.
#greatly relieved it's going well and coming together and crystalizing nicely. 
Past few days have been tremendously productive in THE ZONE. Likely it will be all working by this weekend at this point
and uploaded to the web on github. Grateful I have not given up. The key for me was reading from the Practical Programmer
and testing with "made it here, etc" that helped localize bugs faster. And I read that Elon Musk used to write big functions
and his new programmers' task was managing the code better putting parts into methods. So I started breaking down massive 5 
page functions down to half a page and creating methods. I really like methods they are easier to grasp their mechanics.
This has helped me tremendously to manage the complexity and reuse more code more easily.
I am 100% confident that the nested switch feature will work now. Again all of the working code exists. I'm just
connecting the modules and testing it to death and adding error detection.



Friday, November 5th, 2021 11:34 am Morgan Hill, California Starbucks
	
Methodically going thru code pieces to verify everything is working.
The first objective is taking the big string of switches and cutting it up and putting
each switch case body into a list as a string.
I also have to get the switch, endswitch pairs for the whole string and put those line numbers into a list.
Initially it was in a dictionary.

Copying a switch body works given params starting line and ending line within a string
(this is key since I need to cut out each switch body and put it into a list for further transformation)
Cutting out switch body using skipping and keeping switch word works.
Create pair set of switch ,endswitch works.
I have a working dictionary but decided to use a list of sublists instead for absolute simplicty.
Adding comment and line number after each switch works.
Creating threetabs, fivetabs,seventabs,ninetabs switches works.
Combing all of the tab lists works using extend()

I decided I will construct it in sections in a separate file to reduce the code complexity.
I will do this rather than trying to have the whole thing work together which would not go well.
I am doing the gradual construction this way to isolate bugs that are localized by design.

I am working on the construction of the working code in stages to reduce the complexity and reduce the juggling.



12:20 PM  Nov 4th 2021
	
I will add all of the code in one file in a few days to github for the nested module.
This was a bit more complex than I ever imagined to get it to perfectly mimic C switch cases.
I will add the feature of the floating default anywhere within a switch case later.

https://www.youtube.com/watch?v=ZRSNy8DcIDk
	
	
	
SUMMARY OF PLAN OF ATTACK #all of the functions and methods work for this to happen. 

Each puzzle piece component currently works right now

determine if switch string has more than 1 switch in it

loop thru switch string and add comment with line number after each switch

create range list of pairs of switch endswitch line numbers from initial string of nested switches

using range list(pairs)  COPY each switch at it's tab depth to endswitch and put into quail list

loop thru quail list and CUT out inner nested switches bodies leaving just switch word (referred to as SKIPPING) thru concatting

loop thru quail list and replace inner switch with nested_method + line number in the comment that it grabs on the fly

##=====================================

#what I worked on this morning was creating a method to grab the commented line number from the first switch in a string
in quail list which will then be accessed in the same order in the stanford list where the python output string will be
I will then add indentation and use the number in the list to put into the def nested_switch_ (number) that completes
the construction of each nested string. I have the cake layer code that concats all of the methods together bottom up and
then it's executed and *should* fully work as it (has been) in testing preparing for this moment.

These are the steps that will be welded together likely tonight.

going thru the entire mega switch string a comment is added after each switch like so:  switch(exp){ # 33  
and the number added using replace is the respective line number within the mega initial strating switch string
	
the triggering of the nested switch functionality (gear box) is triggered by bypass205() omage to bypass of Portland in Oregon
if switch count in string is > 1 and endswitch count > 1; if True then proceed with bypass205()
and all bypass205 does really is call the same methods to convert a string into python but appends it to a list
instead of executing it.

	
first part = create list of pairs of switch, endswitch numbers called rangelist and referred to as pairs also
this involves taking the big combo switch string with nested strings and locating the location of each switch and endswitch pairs
based on their respective tab depth before the word switch and endswitch
the pairs list looks like pairslist=[[1,100], [22,33],[44,56]]
the key is that the pairslist is organized in a specific prescribed fashion of one tab, three tabs, five tabs etc
the reason for this is in case there are several (branches) starting at 3 tabs within the body of the main switch at tab 1.

using the rangelist several different methods will manipulate the switch strings in a sequence in stages.

#COPY switch strings and append to quail list
looping thru the rangelist copy each switch to endswitch at the same tab depth
and append each switch string to a list
	
#SKIP switch string body of inner switch strings (cut them out essentially) this is done by concatting the string to manipulate it

Next looping thru the list 
each switch string is reduced to only one level deep nesting by cutting out the inner switch body but leaving the inner switch word
#example
switch(exp){ #22
   case "will work":
	print("nice")
	exp = 2
	switch(exp){ # 33  <<=== notice only the switch word remains the body has been cut out
	print("every nice")  #also notice that the depth within a string is only at 1 tab and 3 tabs
	
Then the inner switch word is converted into a nestedswitch method with it's id number and braces are removed
switch(exp) #22
   case "will work":
	print("nice")
	exp = 2
	nested_switch_33(exp) # 33  <<=== notice only the switch word remains the body has been cut out
	print("every nice")

What is going on is that each set LEVEL is managed by representing a template copy in a sense of
one level switch with a 2nd level nested switch as a method
and this is repeated for each set and in python each switch is it's own separate nested method numbered to prevent name clashes.
however the method methods for the first switch at the top in a string have a nested method added after going thru the parser
		
	
	

Thursday, Nov 4th, 2021  10:40am Morgan Hill, California
	
https://www.youtube.com/watch?v=sRvEwXDxz_I
	
https://www.youtube.com/watch?v=jofkDRNetdw	
	
good coding music

I wrote some brilliant code yesterday that is beautiful and works. 7 hours straight.


peartree=[]
startime=[]
#loop thru threetabs
print("TEStING PeAR TREE backyward with plum tree to see if it works")
print("add result to final_pears_list")
print("does this one work and print x,y")
#my_list = [1,2,3,4,5,6,7,8,9,10]
print("about to see if christmas will come early this year or not")

##======================================
## fill_main_pear_list(listname):
##=====================================
def fill_main_pear_list(listname):
    print("=====fill_main_pear_list called with listname======")
    counter=0 #this must be at 0
    for x in listname:
        print(listname[counter],listname[counter +1])
        jazz = [listname[counter],listname[counter+1]]
        startime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 #notice counting by 2
        if counter >= len(listname): #prevent from going out of bounds
            break
    print("startime list=",startime)
    print("what did this work.......or not ....did it")
    #put in list highest tab number say 7
    if holding_themax[0]== 7:
        fill_main_pear_list(threetabs)
        fill_main_pear_list(fivetabs)
        fill_main_pear_list(seventabs)
    
    if holding_themax[0]== 5:
        fill_main_pear_list(threetabs)
        fill_main_pear_list(fivetabs)
    
    if holding_themax[0]== 3:
        fill_main_pear_list(threetabs)
       
       
       
print("final startime filled with three tabs, five tabs, seven tabs in pairs")
print("battle star galactica")
print("startime=",startime)

 
listinput=[]
first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot

second=[]   #this takes an inputstring which is the combined switchcase big string
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
#  this uses internal_machinery() method in loop below
##========================================================
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    themax = max(add_tab_depth) #gets the biggest number in the list  calculated
    holding_themax[0] = themax #stored to use elsewhere
    print("themax=",themax, "which is the highest tab number before a switch in string")
    #this dynamically creates listinput of tabs
    print("======")
    if themax == 3: listinput = [3]
    if themax == 5: listinput = [3,5]
    if themax == 7: listinput = [3,5,7]
    if themax == 9: listinput = [3,5,7,9]
    if themax == 11:listinput = [3,5,7,9,11]
    if themax == 13:listinput = [3,5,7,9,11,13]
    if themax == 15:listinput = [3,5,7,9,11,13,15]
    print("listinput=",listinput) # dynamically filled based on the max tab count #3,5,7
    for item in listinput: # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)  #calls internal_machinery()(
    print("==done==")
    print("threetabs="   ,threetabs); print("fivetabs="    ,fivetabs);
    print("seventabs="   ,seventabs); print("ninetabs="    ,ninetabs);
    print("eleventabs="  ,eleventabs);print("thirteentabs=",thirteentabs)
##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]

inputstring = red_robin
print("what red_robin looks like before calling try_all_three=====")
print(red_robin)
print("see how it looks above if there are double switches and endswitches yet")
this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)


print("testing looping thru list")
#this represents a list of sublists of the switch,endswitch pairs
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

#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    for item in tabsubs:
        tabcount.append(item)
    del tabsubs[:]
        
        
        
tabsubs=[]
threetabs=[]
fivetabs=[]
seventabs=[]
ninetabs=[]
eleventabs=[]
thirteentabs=[]
fifteentabs=[]
#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("==========internal_machinery() called======")
    print("inputstring",inputstring);print("tabsubs ",tabsubs, " ",x)
    counter=0
    for line in inputstring.splitlines():
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
        if tab_length == x: 
            if "switch" in line and "end" not in line:
                tabsubs.append(counter);counter += 1;continue
            if "endswitch" in line:
                tabsubs.append(counter);counter += 1;continue 
    print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:print("nada")
    print("3 and 5 tabs    =",threetabs ," ",fivetabs)    
    print("7 and 9 tabs    =",seventabs ," ",ninetabs)   
    print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   
 
       

listinput=[]
first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot

second=[]   #this takes an inputstring which is the combined switchcase big string
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
#  this uses internal_machinery() method in loop below
##========================================================
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    themax = max(add_tab_depth) #gets the biggest number in the list  calculated
    holding_themax[0] = themax #stored to use elsewhere
    print("themax=",themax, "which is the highest tab number before a switch in string")
    #this dynamically creates listinput of tabs
    print("======")
    if themax == 3: listinput = [3]
    if themax == 5: listinput = [3,5]
    if themax == 7: listinput = [3,5,7]
    if themax == 9: listinput = [3,5,7,9]
    if themax == 11:listinput = [3,5,7,9,11]
    if themax == 13:listinput = [3,5,7,9,11,13]
    if themax == 15:listinput = [3,5,7,9,11,13,15]
    print("listinput=",listinput) # dynamically filled based on the max tab count #3,5,7
    for item in listinput: # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)  #calls internal_machinery()(
    print("==done==")
    print("threetabs="   ,threetabs); print("fivetabs="    ,fivetabs);
    print("seventabs="   ,seventabs); print("ninetabs="    ,ninetabs);
    print("eleventabs="  ,eleventabs);print("thirteentabs=",thirteentabs)
##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]




#twin list 
wrote code to get first switch id in the comment before it's sent thru the bypass205() and turned into python
the list of switch id numbers in order will be utilized for creating the nested_switch numbers

Oh. Yesterday I nixed the idea of using a dictionary which has weird rules and bugs so changed
back to using a list with sublists for managing the pairs of switch endswitch pairs.
I then made a get() method for grabbing pairs from the list.

worked on dynamically building the combininglist of tabs which is used throughout the code to manipulate switch strings.
example
it will take in the max tab length for a switch in a given string as input
and based on that number determines how many of the tablists to add
if just 3 then just threetabs
if it is 5 then it adds together threetabs and fivetabs
first time I've ever used the extend method and happy it worked, was vexing before discovering extend

combinedlist = threetabs + fivetabs + seventabs #this looks dirt simple but doesn't work like this in a function (oh darn)
this can handle up to fifteentabs but it can be as much as desired, artificial stop at fifteen tabs for switches initially.
		
The purpose of the combinedlist is is is utilized throughout the preparser to grab with the pairs
the switch strings which are seperated using the combinedlist itself.

example of the function in test mode
#dummy code for testing ....
threetabs=[[22,33],[44,66]]
fivetabs =[[55,58],[77,86]]
seventabs=[[88,99],[102,110]]

combined_tabs=[]

#testing purposes
# this adds the tabs lists like threetabs + fivetabs + seventabs into combined_tabs list
print("== snowmen having snowball fight==testing build_tab_list_added_together(x):======")
##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("called build tab list added together")
    print("larget_tab_number =",largest_tab_number)
    del combined_tabs[:] #clears out the combined_tabs list to erase it
    if largest_tab_number == 3:
       combined_tabs.extend(threetabs)
           
    if largest_tab_number == 5:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)
            
    if largest_tab_number == 7:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)        
    
    if largest_tab_number == 9:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs) 
        combined_tabs.extend(ninetabs)        
    
    if largest_tab_number == 11:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)
        combined_tabs.extend(ninetabs) 
        combined_tabs.extend(eleventabs) 
    
    if largest_tab_number == 13:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)
        combined_tabs.extend(ninetabs) 
        combined_tabs.extend(eleventabs)
        combined_tabs.extend(thirteentabs)         
    
#this calls it  
     
build_tab_list_added_together(3) #produces togetherlist=threetabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)
print("======= ")
 #clear it out 
build_tab_list_added_together(5) #produces togetherlist=threetabs + fivetabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)

build_tab_list_added_together(7) #produces togetherlist=threetabs + fivetabs + seventabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)






Wednesday, November 3rd, 2021 11:42 am
Home Strech. I nixed using a dictionary and am using a list with sublists for the switch endswitch pairs.
Making custom methods so it does the same thing as the dictionary methods. I find it simpler and cleaner than using the dictionary.

Testing each stage of the process of getting the switch and endswitch pairs. 
After the indendent stages work by themselves connecting them
will take just a few minutes.

Essentially doing massive testing and simplying and
slight refactoring right now. 

In summary working on testing and streamlining taking in the input code
and preparing it for the parser string before it's sent into bypass205() 
and the rest is gravy. I am thrilled it's going to work. 


Monday, November 1st, 2021 8:42 am
All Systems Green. 
When the code works it feels like this: 
https://www.youtube.com/watch?v=sX1Y2JMK6g8
	
All that is remaining is connecting the last few puzzle pieces(already working) that put the output python
switch strings into their respective methods and adds indentation and concats in cake layers and executed.


Worked on and refined replacing inner switch word with dynamically built nested_switch which uses the comment id line number
which is added on the fly. I also replace the endswitch with the } brace conforming to C and JavaScript.
Conversion of inner switches works for n number whether none, 1, or many - any amount flawlessly.

this:
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
	endswitch #86   
				
#######################################################	
is transformed into this: this is then as a string added to a list that is then
fed thru the parser which triggers bypass205(x) which translates each string seperately into python code
				
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
			



Thursday, October 28th, 2021 11:56am
Working on testing and ensuring that I can fill the dictionary(struct) record with data
and then access it on-the-fly accurately. The dictionary is loaded from a list of the switch pairs.
Recently worked on proof of concept walking thru steps and connecting parts to make sure that the chain of events
is accurate and in the right order. Testing with actual data to ensure that bypass205() is correct.
Working on the final stages now. at the point of the lunar module about to land on the moon. will continue testing
each separate stage to ensure it works independently (to avoid conflict) and then connect the constellation together.
Super close. I also need to work on next the cleaning up of the python string generated of switch code that
needs to be put into methods named by the switch id number. Just need to test it.
Unreal feeling making it this far. Unimaginable complexity so I had to continue breaking down sections into smaller parts
to manage the intense complexity.



Wednesday, October 27th, 2021   11:47am Morgan Hill, California Starbucks
In C for a switch case ... the default statement doesn't have to come at the end. It may appear anywhere in the body of the switch statement. 
I figured out how to make this behavior work so default can be anywhere in the switch case. Simple solution.
In summary, for the switch case implimentation in Python staying true to form of C the default can be anywhere within
a switch case and doesn't have to be at the bottom of the cases. It can be anywhere. I have previously thought it wasn't possible
and then today the simple solution popped into my head. Just move the default to the bottom of the switch case before putting it
thru the parser. It doesn't matter (really) where the default resides if there are no case matches it's irrelevant where the default is
but being able to represent the switch case wholly how it's represented in C is still a great honor. 

I have been walking through the transformation of the nested switches and feeding the split up combo swith string in seperate
file into the bypass205() parser and now working on putting those python output switch strings into the final stage.

Victory is within my grasp now.


#important code that is involved endswitch(), bypass205(), parserguts()
#Monday, Oct 25th, 2021 2:25pm
What I have been working on diligently  is making the code that will automatically split up a combo string
of multiple switches into separate switches and for this to work I had to figure out how to organize and manage
the location of each switch endswitch pair and add that to a dictionary which is used elsewhere.
To prepare the individual switches and the each switch so that it only has one level deep of nesting so
if a switch starts at 3 tabs it can only have five tab indentation switches so one level of depth within it
and then the nested switches within it at 5 tabs (for this example) need to have their switch bodies removed
(after copying them) and then just leave the switch word. All of the switches are numbered by their intitial line
number automatically with a comment which is used to track and manage them. So once the inner switch bodies is
taken out by copying the string and skipping after the position of the switch word down to and including its endswitch
then the remaining switch words needs to be replaced with a nested_method utilizing the unique initial line number comment
that was previously inserted. I am at this point where I replace the inner switch with a nested method that is numbered.
Though I have been a bit anxious to test that the bypass was still working flawlessly that I got working back in June of this
year since I had recently gained some momentum with progress.  And in the past few days I finished several monumentally
complex functions of code to make the transformation seamless preparing the nested switches to be cleaned up and formatted
before running through bypass205 which converts them into python code that next need to have the swich strings put into
the unique method names. 

#code to test bypass205 taking in 3 strings in quail list as input in JavaScript mode
#testing here running 3 strings in quail thru bypass205
print("============== red white and blue time ===========")
del quail[:]
print("length of quail list=",len(quail))
quail.append(str1)
quail.append(str2)
quail.append(str3)
print(" JAZZ MUSIC TIME code test of bypass205() it's been a long wait indeed")
print("printing what is in quail list right here for this test")
for item in quail:
    print(item)
    print("===++====++===")
y='' #normally this takes in the input string for testing I make it empty since the strings are fed into quail list
bypass205(y)    
print("then we look in the stanford list")
print("======output from Stanford List======")
for item in stanford:
    print(item)

print("======= end of stnaford going down Palm drive now=====") 
print("======== Code Blue Exit =====") 
print("  === end of red white and blue ========================")
exit()


nested_switches_count=[]
nested_switches_count.append(0) #so by default it's [0] in position 0
nested=[]
nested.append(False) #loaded with False in nested[0] by default starting

# so it would be True if nested is true
	#for this test we pretend that we have already seperated the big switch string
	# into sepeate strings and they ahve been placed into the quail list
	# #but I can do it here later, with y as input
	# for right now in this phase the quail list has already been filled
	# and we have determined that nestwich is True
########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	print("==== endswitch () called...======")
	print("let us see what is in y passed into endswitch")
	print("============")
	print(y)
	print("============")
	switchcasetester='';switchcasetester=None;
	del switchcasetester;switchcasetester='';
	mytrace("endswitch() in switch_cat called")
	show_input_switch_string() #flag for testing this shows the input string
	#check  if nested switches
	print("count how many endswitches in string")
	answer = y.count("endswitch") #it counts endswitches here 
	do_nested_switch_count()
	print("if answer = 0 continue moss beach one string test ")
	print("the number of endswitches in the input y string is",answer)
	nested_switches_count[0] = answer #maybe int(answer) counts endswitches in string y input to endswitch(y) 
	############### new nearly 9pm ###########################
	# Thursday, August 26th, 2021 12:27pm 
	# inside of original_stage1.py inside of left folder
	# still need to add the methods to make this section work
	# which fills up the quail list that will be fed into bypass205
	# #this is the section that I'm working on right now ===
	# WORKS not added yet : make pair_list here of pairs of switch endswitch 
	# WORKS not added yet : then  loop through pair_list to fill quail list
	# quail list of strings  using copy_string if at least one endswitch in input string
	# Need to fill quail list with these switch bodies strings
	#################
	#========================================================
	print('=====')
	###========= testing this august 4th 2021 ==================================
	print("here we go, leaping into the == Grand Canyon == will it fly?")
	## test to do bypass205 if nested switches > 1
	#bypass205 is only called if there  is at least one endswitch inside of the input string
	# for endswitch(x) above
	# requires nested[0] to be True or False (True to call bypass205(y)
	###########################################
	if nested_switches_count[0] > 1: #based on number of endswitch count
		nested[0] = True; 
		print("what is in nested[0]",nested[0])
		print("bypass 205 CALLED IN ENDSWITCH biggest test yet to make sure that his works----")
		#this goes thru the quail list that is filled beforehand above
		#this method is only called if there are nested switches
		print("quail list must have at least a length of 2")
		###############
		bypass205(y)  #<<== this manages nested switches  
		###############

	else:
		nested[0] = False; 
		print("===bypass205 NOT CaLLEd  only one string, no endswitches===")
		pass
	###===========================================
	#this section is only run if a string switch string NOT NESTED ONES
	print("so this would be skipped if nested switch string combo bypass")
	if nested[0] == False or answer == 0:#all of this below is skipped if nested = True
		print("the string will be parsed and codegened - it doesn't have any nested switches")
		check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
		if baseline[0] != "nada": #means it converted to uppercase
			y = baseline[0]
		#end if
		flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
		print("if number in first case",valve[0])
		if valve[0] == True:    #meaning numbers like case 12:
			macro_expansion(y); #checks if macros used and expands them and converts numb
