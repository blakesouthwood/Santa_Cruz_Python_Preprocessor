import method_calls
from method_calls  import *  
from Linus import switch_numbers_to_transfer
#from Linus import switch_numbers_to_transfer

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
tahoetest=[] #initalized here
tahoetest.append('starter') #position 0 holds just starter

# empty_tahoetest()
switch_count=[]
del switch_count[:] #empties list in case residue from previous runs

#############################
##    empty_tahoetest()
#############################
def empty_tahoetest():
    del tahoetest[:] #this erases the list completely if called 

########################################
## show_the_nested_strings_in_memory()
########################################
def show_the_nested_strings_in_memory():
    for item in tahoetest:
        print("=======")
        print(item)
        print("=======")
           
           
disney_tron_trace_list=['starter']

######## show tron trace path
def show_tron_trace_path():
	#print("#######==== showing TRON TRACE path list =====#####")
	counter=0
	last =''
	disney_tron_trace_list.pop(0) #delete's starter position 0
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number

#### mytrace
def mytrace(x): #just checks if first item is the same if slo don't load it
	disney_tron_trace_list.append(x)
	
#import sw_module_extra
digitalcandy=[]
line_numbers_of_first_cases=[]

#########==============================
### added June 3rd, 2021 
## initialization 
show_code=[]
show_code.append(False)
#show_code[0]= False
#print('starting out what the flag for show code shows')
#print("default setting for show_code[0]",show_code[0])
#show_code.append(False) # by default
#############################################
#to show or hide the docstring switch input in C style
### show input switch string
show_input_string=[]
show_input_string.append(False)
#show_input_string[0]= False
def show_input_switch_string():
    del show_input_string[:] #empty it first
    show_input_string.append(True) #then add True to position [0]
################################
### hide input switch string
def hide_input_switch_string():
    del show_input_string[:] #empty it first
    show_input_string.append(False)

### show_generated_code
def show_generated_code():
    show_code[0]= True
    
### hide_generated_code
def hide_generated_code():  #test this if it really works
    show_code[0]= False
    
#the dilimma is resetting it to default of False
#actually they would probably want them all on or all off honestly
#and they -the settings - show stay in that state  (makes sense)    



    
########## woodstock here may 29th ===============


disney_tron_trace_list=['starter']
######## show tron trace path
def show_tron_trace_path():
	#print("#######==== showing TRON TRACE path list =====#####")
	counter=0
	last =''
	disney_tron_trace_list.pop(0) #delete's starter position 0
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number

#### mytrace
def mytrace(x): #just checks if first item is the same if slo don't load it
	disney_tron_trace_list.append(x)


############################=============
varholder=[]
#def flush_lists():
#	varholder=[]
varholder.append("zilch") #if nothing changes it's default



def is_number(inputString):
	return any(char.isdigit() for char in inputString)
valve=[]
###############################===========


#####################		
newlist =[];count =''  # these are used
######################
####################################################
##      swap_thru_lines_with_expanded_cases()     ##  this is for number cases
####################################################
def swap_thru_lines_with_expanded_cases():
	mytrace('swap_thru_lines_with_expanded_cases()')
	global switchcasetester
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			# this is where it gets number that is now a string
			cat =is_number(smart[1])  #calling method to check if  #the case name is a number
									 
			#print(cat)
			cool = smart[1][:-1]  #chops off : from end last char
			holder = "'" + cool + "'"  #this puts the number in quotes
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			#print("\t\t" + newline)  #adds tabs to front of it
			#print("next I will use replace to each case line")
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal
			#HERE is where the changed case numbers as strings are put into switchcasetester
			#will use a replace here to the switchcasetester string
			mycounter += 1
		else:
			mycounter += 1
			continue
	#print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings


############################
list_with_thru_macros=[]
list_with_thru_macros.append(0) #position 0 nothing
backwards_thru_list =[]  #initializing the list




#############################
################ case 1 to 10: becomes case 1 thru 10:######################
################################
#### change to into thru ()       created friday feb 5th, 2021 morning
################################
def change_to_into_thru():  #this is a simple way of doing it
	mytrace('change_to_into_thru()')
	#print("change macro to into thru")
	global switchcasetester
	mycounter = 0; banana=''
	for line in switchcasetester.splitlines():
		simple = mycounter-1
		if "case" and "to" in line:  #this means the macro to
			banana=switchcasetester.replace(" to "," thru ")  #just addded spaces
			switchcasetester=''; switchcasetester = banana
			#print(switchcasetester)
		else:
			pass


###########################################		
## make_list_of_lines_using_thru_macro():		
###########################################
def make_list_of_lines_using_thru_macro():
	mytrace('make_list_of_lines_using_thru_macro()')
	#print("=====WARNING WILL ROBINSON LOST IN SPACE====")
	#print("* * * * WORKING ON FUNCTION make_list_of_lines_using_thru_macro()")
	#print("===----------=== make list of lines using thru macros() ====--------=")
	#go thru list and if thru in line add that line to list
	global switchcasetester #just added this 
	#how comes this works without global switchcasetester?

	#global switchcasetester #it should work now
	thru_counter = 0
	for line in switchcasetester.splitlines():
		#just added the word to that means the same thing as thru
		if  "case" and "thru" in line:  #on
			list_with_thru_macros.append(thru_counter)
			thru_counter += 1
		else:
			thru_counter += 1
			continue
	#print(list_with_thru_macros)		
	#then I need to reverse the list
	backwards_thru_list=list_with_thru_macros
	backwards_thru_list.reverse()
	#print("backwards we have",backwards_thru_list)
	bottom_up_change_of_thru_line_test() #this just shows the result but really does nothing



##### testing january 10th to go to each case thru from bottom up and change line
##### to prove it's working
####################################################################
## what this does is change the thru macro line starting at the bottom
## by accessing the backwards list made above 
##  backwards_thru_list  that took in the line number of each thru line and reversed it
##########
def bottom_up_change_of_thru_line_test():
	mytrace('bottom_up_change_of_thru_line_test()')
	#global mouse
	global opal; opal = ''; mycounter = 0
	#print("value of mycounter should be zero",mycounter)
	#for item in backwards_thru_list: 
	#set mycounter to a number for line in mouse.splitlines() : #this goes thru the mouse string
	#	print(line)
		

###############==============
smart =''
beta =''
opal=''
import re
newline=''
#################==============


##############################################################################
#################### case_numbers_to_strings() ###############################
##############################################################################
######  converts numbers to strings case 1: to case '1': #####################
##############################################################################
def case_numbers_to_strings():
	mytrace('case_numbers_to_strings()')
	global switchcasetester
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	#print("========  CASE NUMBERS TO STRINGS  ====")#go thru the entire string
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	global switchcasetester ## just addded this may 27th
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			#print(line)
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			#print(cat)
			cool    = smart[1][:-1]  #chops off : from end
			holder  = "'" + cool + "'" #this puts the ' on both flanks of the number
			cool    = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal
			mycounter += 1
		else:
			mycounter += 1
			continue
	#print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings


#############################================


exp =''; case =''
exp = ""

mycounter=0


line =""
varholder=[]
varholder.append('0')
###############################============

#perhaps this is the clever() being called afterall june 9th 2021
#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
	print("clever() on line 276")
	varholder[0]='' #this should reset it to nothing
	mytrace('clever()')
	varholder[0]= i
	#===this works and it fills a list with input from an argument
	#print('varholder[0]=',varholder[0])
	#print(varholder[0]) #to actually see proof
	return varholder[0]
	angel = varholder[0]

###############################================


z =''
import re  #for regular expressions
acounter=0
x = 0;y =0
smart=''
res =[]
newlist=[]
switch_python_gen=''
###########################================




###==============================================================
###================  expand_thru_macro()  =======================
###==============================================================

inputnum = 1
def expand_thru_macro():
	mytrace('expand_thru_macro()')
	global switchcasetester
	change_to_into_thru()   #<======  "to macro" swapped with "thru" in switch case input
	newlist=[] #resets newlist
	global mouse; global ajax; global snowy; snowy=''
	mycounter = 0 ### mouse 
	for line in switchcasetester.splitlines():  #doing mouse not doing switchcasetester yet
		#beta = mycounter-1
										#reinitialize what I'm using with each loop iteration
		smart=[]; ajax=''; newlist  =[]
		#this is the bug fix so I say if "thru" in line but NOT "fallthru" in line.
		if "thru" in line and "case" in line and "fallthru" not in line:  #only used with numbers
			#print(line)
			if ":" in line and line.endswith(":"): #referring to one : in line
				line = chomp(line) #moved taking off colon here  line=line[:-1] 
				#print(line)
			else:  #so now if the line doesn't end with a colon it doesn't chomp it
				pass
			
			smart=line.split() #separates case from casename
			#print("what does smart list have",smart)  #fallthr  missing a u
			#print("smart alleck result for smart[3]",smart[3])
			#print("does thisfix   smart list now!! have",smart)  #fallthr  missing a u
			#print("this should be case", smart[0])
			#print("first number ",int(smart[1]) )     #first number  don't need int
			#print("this should be --thru--",smart[2]) #thru
			#print("last number", smart[3])            #last number 
			#print("will then write perhaps from list yes")
			#print("the input for this macros test")
			#print("=============================")
			#print(smart[0] + " " + smart[1] + " " + smart[2] + " " + smart[3] + ":")
			#print("")
			counter = smart[1]
			#this is filling up the newlist
			
			#### THIS FILLS newlist with the case info
			# ======LOOP  ==================
			for counter in range(int(smart[1]),int(smart[3]) + 1):
				newlist.append(counter)
				counter += 1
			
			ajax =''
			
			##==============================================================
			# LOOP ====================
			 
			for item in newlist:  #this list has the number in it
				ajax += "\t\tcase " +   str(item)   + ":" + "\n"
				#now delete last \n on end 
			#print("==== big test of replacing it ====")
			ajax = ajax.rstrip() #see if this works takes off last "\n" whcih was extra
			ajax = ajax[:-1] #chops off last char on end which is the :
			
			snowy=switchcasetester.replace(line, ajax)
			switchcasetester='';switchcasetester = snowy
			
			



######################################
##  convert_case_numbers_to_strings()
#######################################  #if no macros it just adds strings around numbers


def convert_case_numbers_to_strings():
	#print("we are here in convert case numbers to strings did this reach this far")
	#print("convert_case_numbers_to_strings() called ")
	mytrace('convert_case_numbers_to_strings()')
	global switchcasetester
	make_list_of_lines_using_thru_macro()
	expand_thru_macro()
	case_numbers_to_strings() #stringifies the numbers like this 3 becomes '3'



#this calls convert_case_numbers_to_strings
#this is reading numbers in cases NOT STRINGS and converting them into strings
##############================
cray=[] # this is used to hold the switchcasetester briefly when rewriting it
cray.append('starter')
##############=================

###########################################################
# if a multiple nested switch (at least one nested switch)
#added Mon June 28th, 2021 doing the engineering to make the impossible possible fuzzy logic
multi_switch_with_nested_switches=[]
multi_switch_with_nested_switches.append(0)
multi_switch_with_nested_switches[0] = False #by default
############################################################



##############################
##     macro_expansion()       
############################## # may 26th testing this 

def macro_expansion(y): #expands macros to and thru (if they exist)
	mytrace('macro_expansion()')
	#print("-----==macro_expansion ==-------")
	#print("macro_expansion called")
	if valve[0] == True:    #meaning numbers in cases detected
		#mytrace('starter_sequence_mode_2()')
		global switchcasetester; switchcasetester=y;
		#print("what is in switchcasetester before expanding macros if they exist")
		#print(switchcasetester)
		#################################
		convert_case_numbers_to_strings()  ## <<=== expands macros here 
		#################################
		#print(switchcasetester)
		cray[0] =switchcasetester  #this assigns the output string to cray[0]
	
############==============
# these are used 
coffee=[]  
valve=[]
valve.append("nada")# 0
valve.append("sway")# 1
#############==============


# this gets the line number of the first case in the switch case string
#################################################
##  grab_first_case_of_switch_string(y)
#################################################
def grab_first_case_of_switch_string(y): 
	mytrace("grab_first_case_of_switch_string()") 
	#global switchcasetester
	mycounter = 0
	#this takes in sw to test for finding out if numbers like case 2: or words case "apple"
	for line in y.splitlines():
		if "case" in line:
			#print("the counter for spotting word case is ")
			#print(mycounter)
			#print("coffee has in it at this point ",coffee)
			coffee.append(mycounter)
			#print(coffee[0]) #just added this 
			break  #here after getting the first instance of a case we leave the loop
		else:
			mycounter += 1
			continue




#####################################################
##  remove_tabs_from_string(y)
##################################################### 
def remove_tabs_from_string(y):
	mytrace("remove_tabs_from_string()") 
	y=y.replace("\t","")
	return y





#####################################################
##  grab_first_case_line_in_switch_case_string(y)
##################################################### 


def grab_first_case_line_in_switch_case_string(y):
	#global sw
	mytrace("grab_first_case_line_in_switch_case_string()") 
	#print(coffee[0])  #testing what's in this
	getline= eval("y.splitlines()[" + str(coffee[0]) + "]")
	#print(getline)
	return getline


##################################
##  check_if_number_in_string(x)
################################## 


def check_if_number_in_string(x):
	mytrace("check_if_number_in_string()") 
	theresult = any(char.isdigit() for char in x)  #this line from stackoverflow
	return theresult







################################
########    CHOMP(x)  ##########
################################
## this bites off the last character in a string ##
def chomp(x):
	mytrace('chomp()')
	#print("====== chomp called",x)
	x = x[:-1] 
	#print("x=",x)
	return x




##### end of woodstock code =========================




###=====================
##      adder(x)
##======================

targetlist=[] #just added this 
targetlist.append(0) #initializes it

#math demonstration adding numbers between cases using fallthru
############ adder() ############## added may 27th 2021
def adder(x): #this can be modified to do more
	#print("targetlist[0]=",targetlist[0])
	print("adder called with ",x)
	#first time thru
	if targetlist[0] == 0:    
		x = str(x)
		targetlist[0] = x
		#print(targetlist[0])
	else:   #already something in here
		x = str(x)
		targetlist[0] = int(targetlist[0]) + int(x)
	print(targetlist[0])
	#return(x)

##====================================================================
	
buildstringlist=[]
buildstringlist.append(0)
# this can be used to create a math formula on the fly too
# from my experience 
################################################
##### concatting a string in fallthrus in switch case
############ buildstring() ############## added may 27th

###=========================
##      buildstring(x)
##==========================
def buildstring(x): #this should be 3
	#print("buildstring called with ",x)
	if buildstringlist[0] == 0: #first time thru
		#x =x + 1
		x = str(x)
		buildstringlist[0] = x # example 'Cola'
	else:   #already something in here
		#targetlist[0] = targetlist[0] + x
		#x =x + 1
		x = str(x)
		buildstringlist[0] = str(buildstringlist[0]) + str(x)
	print(buildstringlist[0])
	#return(x)
		




###================================================================	
#bugsbunny.py
#march 18th, 2021
global sw
varholder=[]
baseline=[]
baseline.append('a') #holder for switch code
#def flush_lists():
#	varholder=[]
varholder.append("zilch")

case_main_body_list_with_tail=[]

#experimental

valve=[]
var2=[]
var2.append("zilch")
starbuckslist=[]

# I have cases lists up to 1000
# you can add more but they must be in order and spelled correctly.
# python won't correctly dynamically generate them unfortunately.

def sw_reset():
	return
	#print("sw_reset() was called!!!!!========")
	#importlib.reload(switchmodtrial7)
	
#empty_list method
def empty_list(name): #might need to have it take in with string
	del name[:] #this empties the list
		


############## june 8th attempt ###########========= works==============================
###################################################################
##  TOP OF CASE CONSTANT UPPERCASE AND CONVERSION TO STRINGS
###################################################################
if_strings_found=[]
if_strings_found.append(False) #to initialize it with something

#print(sw)

#endswitch(sw)
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

#june 5th 2021 coding test
uppercase_test=[]
uppercase_test.append(False) # by default
#uppercase_test[0]

found_number_in_case=[]
found_number_in_case.append(False)

#might have to change sw to switchcasetester



#####################################
##  detect_if_number_in_cases()
#####################################
def detect_if_number_in_cases():
	global sw
	#print(sw)
	mycounter = 0
	contains_digit= False
	#global sw ## just addded thismay 27th
	for line in sw.splitlines():
		beta = mycounter-1
		if "case" in line:  #all it does is test the first case and then bails
			contains_digit = any(map(str.isdigit, line))
			if contains_digit == True:
				#print("number found")
				found_number_in_case[0]= True
				break
			else:
				pass
	#this will be commented out later
	#print("===========================")
	#print("did we find numbers in cases?",found_number_in_case[0])
	#print("===========================")	    
 






###########################################
##     detect_if_no_quotes_around_word()
###########################################
def detect_if_no_quotes_around_word():
	#print("detect if no quotes aorund word called")
	global sw
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	#global sw ## just addded thismay 27th
	for line in sw.splitlines():
		beta = mycounter-1
		if "case" in line:  #all it does is test the first case and then bails
			if "'" not in line and '"' not in line:
				#print("no strings in line that we can see")
				#if_strings_found[0] == False:
				continue
					
			else:
				if "'"  in line or '"'  in line:
					if_strings_found[0]= True
					#if_strings_found[0] == True:
					break
					
	#this will be commented out later
	#print("===========================")
	#print("if_strings_found[0] =",if_strings_found[0])
	#print("===========================")
	
	
	
	
	
	
	
	
##########################################   
##    check if case word is uppercase()
##########################################
def check_if_case_word_is_uppercase():  #returns uppercase_test[0]
	global sw
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	global sw ## just addded thismay 27th
	for line in sw.splitlines():
		beta = mycounter-1
		if "case" in line:
			#print(line)
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			#cat =is_number(smart[1])  #calling method to check if the case name is a number
			##############################
			#print('smart[1]=',smart[1])
			#print("========================")
			#print("verify that it\'s all caps for the word ignoring _")
			cat = smart[1]
			#print("cat=",cat)
			#print(line)
			
			#print("verify that it's all uppercase constant")
			if cat.isupper() ==  True:
				#print("=====yes all UPPERCASE=====")
				uppercase_test[0] = True  #sets flag to True
				#print("===============")
				#print("uppercase_test[0]=",uppercase_test[0])
				#print("==============")
			else:
				pass #print("not all uppercase")
	###########################################				
	
	
	


###############################################
##  case_constant_uppercase_word_to_strings()
###############################################
def case_constant_uppercase_word_to_strings(): # case WORDINCAPS: becomes case 'WORDSHERE':
	#print("case constant uppercase word to strings() called")
	mytrace('case_numbers_to_strings()')
	#print("called case constant uppercase word to strings()")
	#print('starting this function we have this test view of uppercase',uppercase_test[0])
	global sw
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	global sw ## just addded thismay 27th
	for line in sw.splitlines():
		beta = mycounter-1
		if "case" in line:
			#print(line)
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			#cat =is_number(smart[1])  #calling method to check if the case name is a number
			##############################
			#print('smart[1]=',smart[1])
			#print("========================")
			#print("verify that it\'s all caps for the word ignoring _")
			cat = smart[1]
			#print("cat=",cat)
			#print(line)
			
			#print("verify that it's all uppercase constant")
			if cat.isupper()==  True:
				#print("=====yes all UPPERCASE=====")
				uppercase_test[0] = True
				#print("===============")
				#print("uppercase_test[0]=",uppercase_test[0])
				#print("==============")
			else:
				pass #print("not all uppercase")
				
			#print("=================")
			da = cat.isupper()
			#print("if upper",da)
			#print("=================")
			#looks like this test requires word in a string
			
			dog = "'" + cat + "'"
			#s = "abc1"
			#contains_digit = any(map(str.isdigit, s))
			#sclise off head and tail of cat now
			dog = cat[1:] 
			dog = cat[-1:]
			#print(cat) #to see what it sees now
			#print("=================")
			sa = cat.islower()
			#print("if lowercase",sa)
			#print("=================")
			
			################################
			# print("====verify that this is called to look for apostrophe and quotes")
# 			print("checking that case word not in quotes")
# 			print("maybe if it finds one take it out replace with nothing")
# 			print("testing if casename is in strings or not")
			#print("first char = cat[0]",cat[0])
			#print("check if first char is a number")
			#it can't be a number to start with only to end with
			#print("new test here if first char a number")
			#print("=====")
			fuel =cat[0].isdigit()
			#if fuel == True:
			#	print("===='''''=============")
			#	print("first char is a number")
			#else:
			#	print("first char is NOT a number")
				
			#print("last char = cat[-1]",cat[-1])
			#print("====this code removes strings IF THEY EXIST")
			
			if cat[0] == "'": 
				cat.replace("'",'' )
			if cat[-1] == "'":
				cat.replace("'",'' )
			#print(cat)	
			#####========
			if cat[0] == '"':
				cat.replace('"','' )
			if cat[-1] == '"':
				cat.replace('"','' )
			#print(cat)	
			###### new idea on Wednesday June 2nd
			#print("=====verify not single or double quotes in case line")
			if "'" not in line and '"' not in line:
				#print("true no quotes in line")
				#print("so quotes and apostrophe = False")
				#print(line)
				pass
			else:
				pass#print("true no quotes in line")
			######################################		
			#print('====this adds the strings to be sure that they are in the correct format')
			cool    = smart[1][:-1]  #chops off : from end
			holder  = "'" + cool + "'" #this puts the ' on both flanks of the number
			cool    = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			opal=sw.replace(line,"\t\t" +newline)
			sw=''
			sw = opal
			mycounter += 1
		else:
			mycounter += 1
			continue
						
	#print("this should print out the modified sw switch case with quotes for cases now")
	#print(sw)	
	#before this stage by default it will be 'nada' in baseline[0]
	baseline[0] = sw  #this means uppercase constant words
	#to see output after conversion
	#print("baseline[0] now")
	#print(baseline[0])





###############################################
##    check_if_uppercase_constant_cases()
###############################################
def check_if_uppercase_constant_cases(y):
    global sw
    sw = y
    detect_if_number_in_cases()
    detect_if_no_quotes_around_word()
    check_if_case_word_is_uppercase()
    
    if uppercase_test[0] == True:  #this does nothing now 
        pass #print("it is UPPERCASE")
    else:
        pass #print("it is lowercase")
    # this is if numbers in case and if strings found and if uppercase (3 booleans))
    ##===========================================
   # 

   ### BOOLEAN test to determine if case UPPERCASE: no numbers, no strings and uppercase True
    if found_number_in_case[0]  == False \
        and if_strings_found[0] == False \
        and uppercase_test[0]   == True:
    ### BOOLEAN test to determine if meets criteria of uppercase word for a case
    ##============================================
        ## this is where the case words are converted to strings
        ########################################
        case_constant_uppercase_word_to_strings()
        ########################################
        #print("MEETS criteria to convert inputs string uppercase constants to strings")
    else:
        baseline[0] = "nada"  # doesn't meet criteria of case UPPERCASE
        pass                  # do nothing if critiera not met for converting to strings
                              # later will add ability to handle lowercase and numbers 
                              # print("doesn't meet criterial to do uppercase to strings")
                              #	adds strings


#print("BIG TEST HERE ===>>")

############## end of june 8th attempt #########
############## end of june 8th attempt #########
############## end of june 8th attempt #########=========================================



	
caselist1=[]
caselist2=[]
caselist3=[]
caselist4=[]
caselist5=[]
caselist6=[]
caselist7=[]
caselist8=[]
caselist9=[]
caselist10=[]
caselist11=[]
caselist12=[]
caselist13=[]
caselist14=[]
caselist15=[]
caselist16=[]
caselist17=[]
caselist18=[]
caselist19=[]
caselist20=[]
caselist21=[]
caselist22=[]
caselist23=[]
caselist24=[]
caselist25=[]
caselist26=[]
caselist27=[]
caselist28=[]
caselist29=[]
caselist30=[]
caselist31=[]
caselist32=[]
caselist33=[]
caselist34=[]
caselist35=[]
caselist36=[]
caselist37=[]
caselist38=[]
caselist39=[]
caselist40=[]
caselist41=[]
caselist42=[]
caselist43=[]
caselist44=[]
caselist45=[]
caselist46=[]
caselist47=[]
caselist48=[]
caselist49=[]
caselist50=[]
caselist51=[]
caselist52=[]
caselist53=[]
caselist54=[]
caselist55=[]
caselist56=[]
caselist57=[]
caselist58=[]
caselist59=[]
caselist60=[]
caselist61=[]
caselist62=[]
caselist63=[]
caselist64=[]
caselist65=[]
caselist66=[]
caselist67=[]
caselist68=[]
caselist69=[]
caselist70=[]
caselist71=[]
caselist72=[]
caselist73=[]
caselist74=[]
caselist75=[]
caselist76=[]
caselist77=[]
caselist78=[]
caselist79=[]
caselist80=[]
caselist81=[]
caselist82=[]
caselist83=[]
caselist84=[]
caselist85=[]
caselist86=[]
caselist87=[]
caselist88=[]
caselist89=[]
caselist90=[]
caselist91=[]
caselist92=[]
caselist93=[]
caselist94=[]
caselist95=[]
caselist96=[]
caselist97=[]
caselist98=[]
caselist99=[]
caselist100=[]
caselist101=[]
caselist102=[]
caselist103=[]
caselist104=[]
caselist105=[]
caselist106=[]
caselist107=[]
caselist108=[]
caselist109=[]
caselist110=[]
caselist111=[]
caselist112=[]
caselist113=[]
caselist114=[]
caselist115=[]
caselist116=[]
caselist117=[]
caselist118=[]
caselist119=[]
caselist120=[]
caselist121=[]
caselist122=[]
caselist123=[]
caselist124=[]
caselist125=[]
caselist126=[]
caselist127=[]
caselist128=[]
caselist129=[]
caselist130=[]
caselist131=[]
caselist132=[]
caselist133=[]
caselist134=[]
caselist135=[]
caselist136=[]
caselist137=[]
caselist138=[]
caselist139=[]
caselist140=[]
caselist141=[]
caselist142=[]
caselist143=[]
caselist144=[]
caselist145=[]
caselist146=[]
caselist147=[]
caselist148=[]
caselist149=[]
caselist150=[]
caselist151=[]
caselist152=[]
caselist153=[]
caselist154=[]
caselist155=[]
caselist156=[]
caselist157=[]
caselist158=[]
caselist159=[]
caselist160=[]
caselist161=[]
caselist162=[]
caselist163=[]
caselist164=[]
caselist165=[]
caselist166=[]
caselist167=[]
caselist168=[]
caselist169=[]
caselist170=[]
caselist171=[]
caselist172=[]
caselist173=[]
caselist174=[]
caselist175=[]
caselist176=[]
caselist177=[]
caselist178=[]
caselist179=[]
caselist180=[]
caselist181=[]
caselist182=[]
caselist183=[]
caselist184=[]
caselist185=[]
caselist186=[]
caselist187=[]
caselist188=[]
caselist189=[]
caselist190=[]
caselist191=[]
caselist192=[]
caselist193=[]
caselist194=[]
caselist195=[]
caselist196=[]
caselist197=[]
caselist198=[]
caselist199=[]
caselist200=[]
caselist201=[]
caselist202=[]
caselist203=[]
caselist204=[]
caselist205=[]
caselist206=[]
caselist207=[]
caselist208=[]
caselist209=[]
caselist210=[]
caselist211=[]
caselist212=[]
caselist213=[]
caselist214=[]
caselist215=[]
caselist216=[]
caselist217=[]
caselist218=[]
caselist219=[]
caselist220=[]
caselist221=[]
caselist222=[]
caselist223=[]
caselist224=[]
caselist225=[]
caselist226=[]
caselist227=[]
caselist228=[]
caselist229=[]
caselist230=[]
caselist231=[]
caselist232=[]
caselist233=[]
caselist234=[]
caselist235=[]
caselist236=[]
caselist237=[]
caselist238=[]
caselist239=[]
caselist240=[]
caselist241=[]
caselist242=[]
caselist243=[]
caselist244=[]
caselist245=[]
caselist246=[]
caselist247=[]
caselist248=[]
caselist249=[]
caselist250=[]
caselist251=[]
caselist252=[]
caselist253=[]
caselist254=[]
caselist255=[]
caselist256=[]
caselist257=[]
caselist258=[]
caselist259=[]
caselist260=[]
caselist261=[]
caselist262=[]
caselist263=[]
caselist264=[]
caselist265=[]
caselist266=[]
caselist267=[]
caselist268=[]
caselist269=[]
caselist270=[]
caselist271=[]
caselist272=[]
caselist273=[]
caselist274=[]
caselist275=[]
caselist276=[]
caselist277=[]
caselist278=[]
caselist279=[]
caselist280=[]
caselist281=[]
caselist282=[]
caselist283=[]
caselist284=[]
caselist285=[]
caselist286=[]
caselist287=[]
caselist288=[]
caselist289=[]
caselist290=[]
caselist291=[]
caselist292=[]
caselist293=[]
caselist294=[]
caselist295=[]
caselist296=[]
caselist297=[]
caselist298=[]
caselist299=[]
caselist300=[]
caselist301=[]
caselist302=[]
caselist303=[]
caselist304=[]
caselist305=[]
caselist306=[]
caselist307=[]
caselist308=[]
caselist309=[]
caselist310=[]
caselist311=[]
caselist312=[]
caselist313=[]
caselist314=[]
caselist315=[]
caselist316=[]
caselist317=[]
caselist318=[]
caselist319=[]
caselist320=[]
caselist321=[]
caselist322=[]
caselist323=[]
caselist324=[]
caselist325=[]
caselist326=[]
caselist327=[]
caselist328=[]
caselist329=[]
caselist330=[]
caselist331=[]
caselist332=[]
caselist333=[]
caselist334=[]
caselist335=[]
caselist336=[]
caselist337=[]
caselist338=[]
caselist339=[]
caselist340=[]
caselist341=[]
caselist342=[]
caselist343=[]
caselist344=[]
caselist345=[]
caselist346=[]
caselist347=[]
caselist348=[]
caselist349=[]
caselist350=[]
caselist351=[]
caselist352=[]
caselist353=[]
caselist354=[]
caselist355=[]
caselist356=[]
caselist357=[]
caselist358=[]
caselist359=[]
caselist360=[]
caselist361=[]
caselist362=[]
caselist363=[]
caselist364=[]
caselist365=[]
caselist366=[]
caselist367=[]
caselist368=[]
caselist369=[]
caselist370=[]
caselist371=[]
caselist372=[]
caselist373=[]
caselist374=[]
caselist375=[]
caselist376=[]
caselist377=[]
caselist378=[]
caselist379=[]
caselist380=[]
caselist381=[]
caselist382=[]
caselist383=[]
caselist384=[]
caselist385=[]
caselist386=[]
caselist387=[]
caselist388=[]
caselist389=[]
caselist390=[]
caselist391=[]
caselist392=[]
caselist393=[]
caselist394=[]
caselist395=[]
caselist396=[]
caselist397=[]
caselist398=[]
caselist399=[]
caselist400=[]
caselist401=[]
caselist402=[]
caselist403=[]
caselist404=[]
caselist405=[]
caselist406=[]
caselist407=[]
caselist408=[]
caselist409=[]
caselist410=[]
caselist411=[]
caselist412=[]
caselist413=[]
caselist414=[]
caselist415=[]
caselist416=[]
caselist417=[]
caselist418=[]
caselist419=[]
caselist420=[]
caselist421=[]
caselist422=[]
caselist423=[]
caselist424=[]
caselist425=[]
caselist426=[]
caselist427=[]
caselist428=[]
caselist429=[]
caselist430=[]
caselist431=[]
caselist432=[]
caselist433=[]
caselist434=[]
caselist435=[]
caselist436=[]
caselist437=[]
caselist438=[]
caselist439=[]
caselist440=[]
caselist441=[]
caselist442=[]
caselist443=[]
caselist444=[]
caselist445=[]
caselist446=[]
caselist447=[]
caselist448=[]
caselist449=[]
caselist450=[]
caselist451=[]
caselist452=[]
caselist453=[]
caselist454=[]
caselist455=[]
caselist456=[]
caselist457=[]
caselist458=[]
caselist459=[]
caselist460=[]
caselist461=[]
caselist462=[]
caselist463=[]
caselist464=[]
caselist465=[]
caselist466=[]
caselist467=[]
caselist468=[]
caselist469=[]
caselist470=[]
caselist471=[]
caselist472=[]
caselist473=[]
caselist474=[]
caselist475=[]
caselist476=[]
caselist477=[]
caselist478=[]
caselist479=[]
caselist480=[]
caselist481=[]
caselist482=[]
caselist483=[]
caselist484=[]
caselist485=[]
caselist486=[]
caselist487=[]
caselist488=[]
caselist489=[]
caselist490=[]
caselist491=[]
caselist492=[]
caselist493=[]
caselist494=[]
caselist495=[]
caselist496=[]
caselist497=[]
caselist498=[]
caselist499=[]
caselist500=[]
caselist501=[]
caselist502=[]
caselist503=[]
caselist504=[]
caselist505=[]
caselist506=[]
caselist507=[]
caselist508=[]
caselist509=[]
caselist510=[]
caselist511=[]
caselist512=[]
caselist513=[]
caselist514=[]
caselist515=[]
caselist516=[]
caselist517=[]
caselist518=[]
caselist519=[]
caselist520=[]
caselist521=[]
caselist522=[]
caselist523=[]
caselist524=[]
caselist525=[]
caselist526=[]
caselist527=[]
caselist528=[]
caselist529=[]
caselist530=[]
caselist531=[]
caselist532=[]
caselist533=[]
caselist534=[]
caselist535=[]
caselist536=[]
caselist537=[]
caselist538=[]
caselist539=[]
caselist540=[]
caselist541=[]
caselist542=[]
caselist543=[]
caselist544=[]
caselist545=[]
caselist546=[]
caselist547=[]
caselist548=[]
caselist549=[]
caselist550=[]
caselist551=[]
caselist552=[]
caselist553=[]
caselist554=[]
caselist555=[]
caselist556=[]
caselist557=[]
caselist558=[]
caselist559=[]
caselist560=[]
caselist561=[]
caselist562=[]
caselist563=[]
caselist564=[]
caselist565=[]
caselist566=[]
caselist567=[]
caselist568=[]
caselist569=[]
caselist570=[]
caselist571=[]
caselist572=[]
caselist573=[]
caselist574=[]
caselist575=[]
caselist576=[]
caselist577=[]
caselist578=[]
caselist579=[]
caselist580=[]
caselist581=[]
caselist582=[]
caselist583=[]
caselist584=[]
caselist585=[]
caselist586=[]
caselist587=[]
caselist588=[]
caselist589=[]
caselist590=[]
caselist591=[]
caselist592=[]
caselist593=[]
caselist594=[]
caselist595=[]
caselist596=[]
caselist597=[]
caselist598=[]
caselist599=[]
caselist600=[]
caselist601=[]
caselist602=[]
caselist603=[]
caselist604=[]
caselist605=[]
caselist606=[]
caselist607=[]
caselist608=[]
caselist609=[]
caselist610=[]
caselist611=[]
caselist612=[]
caselist613=[]
caselist614=[]
caselist615=[]
caselist616=[]
caselist617=[]
caselist618=[]
caselist619=[]
caselist620=[]
caselist621=[]
caselist622=[]
caselist623=[]
caselist624=[]
caselist625=[]
caselist626=[]
caselist627=[]
caselist628=[]
caselist629=[]
caselist630=[]
caselist631=[]
caselist632=[]
caselist633=[]
caselist634=[]
caselist635=[]
caselist636=[]
caselist637=[]
caselist638=[]
caselist639=[]
caselist640=[]
caselist641=[]
caselist642=[]
caselist643=[]
caselist644=[]
caselist645=[]
caselist646=[]
caselist647=[]
caselist648=[]
caselist649=[]
caselist650=[]
caselist651=[]
caselist652=[]
caselist653=[]
caselist654=[]
caselist655=[]
caselist656=[]
caselist657=[]
caselist658=[]
caselist659=[]
caselist660=[]
caselist661=[]
caselist662=[]
caselist663=[]
caselist664=[]
caselist665=[]
caselist666=[]
caselist667=[]
caselist668=[]
caselist669=[]
caselist670=[]
caselist671=[]
caselist672=[]
caselist673=[]
caselist674=[]
caselist675=[]
caselist676=[]
caselist677=[]
caselist678=[]
caselist679=[]
caselist680=[]
caselist681=[]
caselist682=[]
caselist683=[]
caselist684=[]
caselist685=[]
caselist686=[]
caselist687=[]
caselist688=[]
caselist689=[]
caselist690=[]
caselist691=[]
caselist692=[]
caselist693=[]
caselist694=[]
caselist695=[]
caselist696=[]
caselist697=[]
caselist698=[]
caselist699=[]
caselist700=[]
caselist701=[]
caselist702=[]
caselist703=[]
caselist704=[]
caselist705=[]
caselist706=[]
caselist707=[]
caselist708=[]
caselist709=[]
caselist710=[]
caselist711=[]
caselist712=[]
caselist713=[]
caselist714=[]
caselist715=[]
caselist716=[]
caselist717=[]
caselist718=[]
caselist719=[]
caselist720=[]
caselist721=[]
caselist722=[]
caselist723=[]
caselist724=[]
caselist725=[]
caselist726=[]
caselist727=[]
caselist728=[]
caselist729=[]
caselist730=[]
caselist731=[]
caselist732=[]
caselist733=[]
caselist734=[]
caselist735=[]
caselist736=[]
caselist737=[]
caselist738=[]
caselist739=[]
caselist740=[]
caselist741=[]
caselist742=[]
caselist743=[]
caselist744=[]
caselist745=[]
caselist746=[]
caselist747=[]
caselist748=[]
caselist749=[]
caselist750=[]
caselist751=[]
caselist752=[]
caselist753=[]
caselist754=[]
caselist755=[]
caselist756=[]
caselist757=[]
caselist758=[]
caselist759=[]
caselist760=[]
caselist761=[]
caselist762=[]
caselist763=[]
caselist764=[]
caselist765=[]
caselist766=[]
caselist767=[]
caselist768=[]
caselist769=[]
caselist770=[]
caselist771=[]
caselist772=[]
caselist773=[]
caselist774=[]
caselist775=[]
caselist776=[]
caselist777=[]
caselist778=[]
caselist779=[]
caselist780=[]
caselist781=[]
caselist782=[]
caselist783=[]
caselist784=[]
caselist785=[]
caselist786=[]
caselist787=[]
caselist788=[]
caselist789=[]
caselist790=[]
caselist791=[]
caselist792=[]
caselist793=[]
caselist794=[]
caselist795=[]
caselist796=[]
caselist797=[]
caselist798=[]
caselist799=[]
caselist800=[]
caselist801=[]
caselist802=[]
caselist803=[]
caselist804=[]
caselist805=[]
caselist806=[]
caselist807=[]
caselist808=[]
caselist809=[]
caselist810=[]
caselist811=[]
caselist812=[]
caselist813=[]
caselist814=[]
caselist815=[]
caselist816=[]
caselist817=[]
caselist818=[]
caselist819=[]
caselist820=[]
caselist821=[]
caselist822=[]
caselist823=[]
caselist824=[]
caselist825=[]
caselist826=[]
caselist827=[]
caselist828=[]
caselist829=[]
caselist830=[]
caselist831=[]
caselist832=[]
caselist833=[]
caselist834=[]
caselist835=[]
caselist836=[]
caselist837=[]
caselist838=[]
caselist839=[]
caselist840=[]
caselist841=[]
caselist842=[]
caselist843=[]
caselist844=[]
caselist845=[]
caselist846=[]
caselist847=[]
caselist848=[]
caselist849=[]
caselist850=[]
caselist851=[]
caselist852=[]
caselist853=[]
caselist854=[]
caselist855=[]
caselist856=[]
caselist857=[]
caselist858=[]
caselist859=[]
caselist860=[]
caselist861=[]
caselist862=[]
caselist863=[]
caselist864=[]
caselist865=[]
caselist866=[]
caselist867=[]
caselist868=[]
caselist869=[]
caselist870=[]
caselist871=[]
caselist872=[]
caselist873=[]
caselist874=[]
caselist875=[]
caselist876=[]
caselist877=[]
caselist878=[]
caselist879=[]
caselist880=[]
caselist881=[]
caselist882=[]
caselist883=[]
caselist884=[]
caselist885=[]
caselist886=[]
caselist887=[]
caselist888=[]
caselist889=[]
caselist890=[]
caselist891=[]
caselist892=[]
caselist893=[]
caselist894=[]
caselist895=[]
caselist896=[]
caselist897=[]
caselist898=[]
caselist899=[]
caselist900=[]
caselist901=[]
caselist902=[]
caselist903=[]
caselist904=[]
caselist905=[]
caselist906=[]
caselist907=[]
caselist908=[]
caselist909=[]
caselist910=[]
caselist911=[]
caselist912=[]
caselist913=[]
caselist914=[]
caselist915=[]
caselist916=[]
caselist917=[]
caselist918=[]
caselist919=[]
caselist920=[]
caselist921=[]
caselist922=[]
caselist923=[]
caselist924=[]
caselist925=[]
caselist926=[]
caselist927=[]
caselist928=[]
caselist929=[]
caselist930=[]
caselist931=[]
caselist932=[]
caselist933=[]
caselist934=[]
caselist935=[]
caselist936=[]
caselist937=[]
caselist938=[]
caselist939=[]
caselist940=[]
caselist941=[]
caselist942=[]
caselist943=[]
caselist944=[]
caselist945=[]
caselist946=[]
caselist947=[]
caselist948=[]
caselist949=[]
caselist950=[]
caselist951=[]
caselist952=[]
caselist953=[]
caselist954=[]
caselist955=[]
caselist956=[]
caselist957=[]
caselist958=[]
caselist959=[]
caselist960=[]
caselist961=[]
caselist962=[]
caselist963=[]
caselist964=[]
caselist965=[]
caselist966=[]
caselist967=[]
caselist968=[]
caselist969=[]
caselist970=[]
caselist971=[]
caselist972=[]
caselist973=[]
caselist974=[]
caselist975=[]
caselist976=[]
caselist977=[]
caselist978=[]
caselist979=[]
caselist980=[]
caselist981=[]
caselist982=[]
caselist983=[]
caselist984=[]
caselist985=[]
caselist986=[]
caselist987=[]
caselist988=[]
caselist989=[]
caselist990=[]
caselist991=[]
caselist992=[]
caselist993=[]
caselist994=[]
caselist995=[]
caselist996=[]
caselist997=[]
caselist998=[]
caselist999=[]
caselist1000=[]

'''
def runthisnow():
	print("====caselists generated===")
	i = 128; j = 1000;
	while i  < j:
		print("caselist" + str(i) + "=[]")
		i += 1
		continue;
'''	
		

#runthisnow()


def clear_out_all_case_lists():
	#get last case list number like 14
	caselist1=[]
	caselist2=[]
	caselist3=[]
	caselist4=[]
	caselist5=[]
	caselist6=[]
	caselist7=[]
	caselist8=[]
	caselist9=[]
	caselist10=[]
	caselist11=[]
	caselist12=[]
	caselist13=[]
	caselist14=[]
	caselist15=[]
	caselist16=[]
	


#this resets all of the lists
##### flush_lists() ##############
def flush_lists():
	#print("===== flush lists() called =====")
	mytrace('flush_lists  =====')
	#switchcasetester = ''
	#sw=''
	#newest additions here april 7, 2021
	birdsong=[0]
	music=[0]
	colorful=[0]

	caseset=[]
	wilsonball=[]
	palmtrees=[]
	candy=[]
	digitalcandy=[]
	caselist =[]
	breaklist =[]
	einstein=[]
	smartcasemanager=[]
	british=[]
	cranberries=[]
	defaultlist =[]
	blanklines  =[]
	mixedlist   =[]
	batterondeck =[] #I can have item to comapore with in here
	seriestogether =[]
	res =[]
	getfirstword =[]
	casephrase =[]
	alphalist =  ["a", "b", "c","d", "e","f","g", "h", "i","j","k","l","m","n", "o","p","q","r", "s", "t", "u","v", "w","x","y",":",";","(",")","{","}"]
	casesections =[]
	casesectioncounter =[]
	breakposition =[]
	trontime =[]
	tronlinenumbers =[]
	fallthrulist = []
	smartlist =[]
	smartlistlocations=[]
	fallthrulocations=[]
	#theinputlist =[]
	digitalcandy=[]
	line_numbers_of_first_cases=[]
	#deepsea_line_numbers=[] 
	# print("==== showing the lists values now after flushing them clean ===")
# 	print("birdsong",birdsong)
# 	print("music",music)
# 	print("colorful",colorful)
# 	print("caseset",caseset)
# 	print("wilsonball",wilsonball)
# 	print("palmtrees",palmtrees)
# 	print("candy",candy)
# 	print("digitalcandy",digitalcandy)
# 	print("caselist",caselist)
# 	print("breaklist",breaklist)
# 	print("einstein",einstein)
# 	print("smartcasemanager",smartcasemanager)
# 	print("british",british)
# 	print("cranberries",cranberries)
# 	print("defaultlist",defaultlist)
# 	print("blanklines",blanklines)
# 	print("mixedlist",mixedlist)
# 	print("seriestogether",seriestogether)
# 	print("res",res)
# 	print("getfirstword",getfirstword)
	# print("casephrase",casephrase)
# 	print("alphalist",alphalist)
# 	print("casesections",casesections)
# 	print("casesectioncounter",casesectioncounter)
# 	print("breakposition",breakposition)
# 	print("trontime",trontime)
# 	print("tronlinenumbers",tronlinenumbers)
# 	print("fallthrulist",fallthrulist)
# 	print("smartlist",smartlist)
# 	print("smartlistlocations",smartlistlocations)
# 	print("fallthrulocations",fallthrulocations)
# 	#print("theinputlist",theinputlist)
# 	print("digitalcandy",digitalcandy)
# 	print("line_numbers_of_first_cases",line_numbers_of_first_cases)

#################  from woodstock_alpha which is the numbers code 
#################======== beginning of woodstock code added here at top =====
#################
show_py_switch=[]
show_py_switch.append(False)  #this is show_py_switch[0]

#to debug generated code you can see the generatedcode 
def view_code_turn_on():
    show_py_switch[0] = True
    
    
def view_code_turn_off():
    show_py_switch[0] = False

#what this does is show the output python code that is genereated from code gen
#and then executed

view_code_turn_on()  #if it says view_code_turn_off() it won't show the generated python
    
  



'''
reset_list_to_just_starter(listname)
this makes sure that a list is reset if already used recently to
the initial state with starter in the first list element with nothing else
so that it will have a lengthh of 1. It can be 0 or 'starter' in the first slot.
This was devised to clear out lists so that after the first switch is called
all subsequent switch calls have cleared lists so it's as if each call of a 
switch is the first switch call rather than calling reload module. 
'''
#april 27th, 2021  2:46pm
############################################
#   reset_list_to_just_starter(listname)
############################################
def reset_list_to_just_starter(listname):
	print("reset_list_to_just_starter() called")
	if len(listname) > 1:         # checks if list length greater than 1
		for item in listname:     # loop through entire list
			if len(listname) > 1: # if length of list > 1
				listname.pop()	  # delete last item of list
		#end loop
		if len(listname) == 2:    # if length of list equals 2
			listname.pop()		  # delete last item in list

		if len(listname) == 1:    # if list length = 1  all okay
			print('proceed',listname, ' length 1 is correct')
		else:
			print("this list", listname, "is wrong supposed to be length 1", len(listname))
	else:
		# length of list is 0 or 1 do nothing
		pass

#####################################
# reset_list_to_empty
#####################################
def reset_list_to_empty(listname):
	del listname[:]  #just changed this wednesday may 19th 

  
###++++$$$$$$$$$$$$$$$$$$$$$$$$$ working on this sunday january 10th $$$$$$$$$$$$$$$$$
###++++$$$$$$$$$$$$$$$$$$$$$$$$$ working on this sunday january 10th $$$$$$$$$$$$$$$$$
####////////////===========================================
## will use this one to replaceing the macro with the expanded macro
## which is a string I reference in a list by order number like string_1, string_2
## these will be
## I need to have my macroexpand function go thru a list of thru lines
## and dynamicallyh build each case thru expanded and the stringname
## added to a list
##  and change each case number  into a string for preparing for python handling
## this isn't called yet #go thru the entire string
####################################################
##      swap_thru_lines_with_expanded_cases()     ##  this is for number cases
####################################################
#def swap_thru_lines_with_expanded_cases():
#	## https://www.youtube.com/watch?v=_CzJ5bdRDU4
#	#import pudb; pu.db  #added at point you want to start debugger
#	
#	mytrace('swap_thru_lines_with_expanded_cases()')
#	global switchcasetester
#	print("=========testing case_numbers_to_strings===january 5th 2020====")
#	mycounter = 0
#	for line in switchcasetester.splitlines():
#		beta = mycounter-1
#		if "case" in line:
#			print(line)
#			print(" ")
#			smart=line.split() #separates case from casename
#			#checks if case name is a number returns True or False
#			# this is where it gets number that is now a string
#			cat =is_number(smart[1])  #calling method to check if 
#									  #the case name is a number
#			print(cat)
#			cool = smart[1][:-1]  #chops off : from end last char
#			holder = "'" + cool + "'"  #this puts the number in quotes
#			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
#			newline = cool
#			#print("\t\t" + newline)  #adds tabs to front of it
#			#print("next I will use replace to each case line")
#			opal=switchcasetester.replace(line,"\t\t" +newline)
#			switchcasetester=''
#			switchcasetester = opal
#			#HERE is where the changed case numbers as strings are put into switchcasetester
#			#will use a replace here to the switchcasetester string
#			mycounter += 1
#		else:
#			mycounter += 1
#			continue
#	#print(switchcasetester) #this is to see the switch case input string after the modification
#	#after the numbers have been converted into strings



###////////////////////////////////////////////===========
    

#list_with_thru_macros=[]
#list_with_thru_macros.append(0) #position 0 nothing
#backwards_thru_list =[]  #initializing the list

#### ### this needs to happen first 
################ case 1 to 10: becomes case 1 thru 10:######################
######################################################
#### change to into thru ()       created friday feb 5th, 2021 morning
######################################################

#########################################
#def change_to_into_thru():  #this is a simple way of doing it
#	mytrace('change_to_into_thru()')
#	print("change macro to into thru")
#	global switchcasetester
#	mycounter = 0; banana=''
#	for line in switchcasetester.splitlines():
#		simple = mycounter-1
#		if "case" and "to" in line:  #this means the macro to
#			banana=switchcasetester.replace(" to "," thru ")  #just addded spaces
#			switchcasetester=''; switchcasetester = banana
#			#print(switchcasetester)
#		else:
#			pass
		
		










		
	
	

####=========== test here concatting little chunks for the switch case







	


#varholder=[]
#varholder.append("walmart")  #position 0  varholder[0]
#varholder.append("0")      #position 1
# =======   testfunction    ========================
#exp=''








#coyote_list=[]  #initialize it
#trontime= ['empty', 'switch', 'case', 'case', 'code;', 'code;', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'break', 'empty', 'case', 'case', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'default', 'code;', 'code;', 'break', 'code;']


# I can simply fill it manually with a loop and append
#print(trontime)



#what I can do is have a simple true or false switch
#and leave the function calls where they are and if triggered true
#then they will be called otherwise they won't be called.


#start_trigger()


######################################
default_location=''
def get_default_location_2(): #line number location of the word default
	print("=============get default location called =================")
	mytrace('get_default_location_2')
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
			default_location = counter
			break
		else:
			counter += 1
			continue
	return default_location







	
########################################
##      get last break in string
########################################
listofbreaks=[]
def get_last_break_in_string_2():
	print("==============find last break in string============")
	mytrace('get_last_break_in_string_2()')
	counter=0
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			counter +=1
		else:
			counter += 1
			continue
	baby = listofbreaks[-1] #the last one
	return baby #which is a string
	
	
	
	
#############################


#I need to add a break if there isn't one saturday, December 5th
#it expects a break at bottom of default.
#and I just realized it requires a default but doesn't look for one
newton=''
orange=''
#this scans through input switch and changes default to case default
#switchcasetester=''
last_break=''
#this assumes that there is a default. I will just make it mandatory to have a default
################################################################################
### this does convert_default_case AND add break after default if it needs one
################################################################################
def convert_default_case_2(): #I got this working November 26th, 2020
	print("IS THIS BEING CALLED convert_default_case_2()")
	mytrace('convert_default_case_2')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location_2()
	last_break =get_last_break_in_string_2()
	
	
	############################################################
	global switchcasetester
	# IF default(LINE NUMBER) < last break(LINE NUMBER)  There is a break
	#########################################################################
	#this says: if default (line number) LESS than last break (line number)
	#in other words this says if "break" after "default" is True 
	if int(get_default) < int(last_break):  #### if default  < last break  
	
	#########################################################################
		
		#print("there is a break after default")
		#################################################################
		####  DEFAULT IS CHANGED TO CASE 'DEFAULT':            ########### 
		#################################################################
		#change default to case 'default':
		newton=switchcasetester.replace("default:","case 'default':")
		switchcasetester=''
		switchcasetester = newton
		#print("")
		#print(switchcasetester)
		
		make_list_of_first_cases()
		#print(switchcasetester)
		return switchcasetester
		
		# at this ELSE This is triggered if NO BREAK IS AFTER DEFAULT and therefore add a break
		#the else  is triggered if int(a)> int(b) meaning break number LESS THAN default line num
	else:
		#down below here it adds break after default and makes case deafult
		#print(switchcasetester)
		########################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		#######################################################################
		orange=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = orange
		#print(switchcasetester)
		#################################################################
		####  DEFAULT IS CHANGED TO CASE 'DEFAULT':            ########### 
		#################################################################
		#change default to case 'default':
		newton=switchcasetester.replace("default:","case 'default':")
		switchcasetester=''
		switchcasetester = newton
		#print("")
		#print(switchcasetester)
		
		make_list_of_first_cases()
		#print(switchcasetester)
		return switchcasetester
	
	






def testing_number_of_lines_in_string_2():
	mytrace('testing_number_of_lines_in_string_2()')
	count =0
	for line in switchcasetester.splitlines():
		count +=1
		#print(count)
	#print("there were ",count, "lines in string")
	return count




    #apple = "one"
###=================== nov 19th new code ============
###================ get_closing_brace (line number) ==============
closing_brace=''
def get_closing_brace_2():
	#print("get_closing_brace called")
	mytrace('get_closing_brace_2')
	counter =0
	closing_brace =testing_number_of_lines_in_string_2()
	return closing_brace

###=============================================
default_location=''
def get_default_location_2():
	mytrace('get_default_location_2')
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
			default_location = counter
		else:
			counter += 1
			continue
	return default_location



list1 =[]
list1.append("four")


#varholder[0] ="four"







print("this is actual generated code I am trying to run now....")
print("this is betterworknow in python generated previously")



list1=[]
exp =''; case =''
exp = ""

#exec(betterworknow)
print("=== executin betterwork now test bit")




####======== starts here ===============
#this is the function triggered to start the parser and codegen
def start_trigger_2():  #this converts the default case immediately
	#global switchcasetester  #just added this to hopefully fix bug
	trigger = True
	print("trigger =", trigger)
	if trigger == True:
		print("trigger =", True)
	else:
		print('trigger=',False)

	mytrace('start_trigger_2')
	convert_default_case_2()





caselist    =[]
breaklist   =[]
defaultlist =[]
blanklines =[]
mixedlist   =[]
batterondeck =[] #I can have item to comapore with in here
seriestogether =[]
res =[]
getfirstword =[]
casephrase =[]
alphalist =  ["a", "b", "c","d", "e","f","g", "h", "i","j","k","l","m","n", "o","p","q","r", "s", "t", "u","v", "w","x","y",":",";","(",")","{","}"]
casesections =[]
casesectioncounter =[]
breakposition =[]
trontime =[]
tronlinenumbers =[]
fallthrulist = []
smartlist =[]
smartlistlocations=[]
fallthrulocations=[]
#theinputlist =[]





###### how do I pass a list
#this might work
def get_first_list():
	mytrace('get_first_list()')





#this finds teh first case in each case section and works
#should be: starter,apple, bananas,chocolate, fish,default
#digitalcandy=[[3,7],[7,19],[19,26],[26,33],[33,43],[43,46]]
















mycounter=0
turtle_tab1=[]
turtle_tab2=[]
turtle_tab1.append('starter')
turtle_tab2.append('starter')
#print('looking for tabs in lines================')
#this is just testing in one case for now
#what I am trying to do is 2 loops one for each case section
#so for the second pass it should start at the next case occurrence
#so first I need to prescan it and get the line number of each case
#apparently the solution is using the digitalcandy list with
#the range of case line numbers which I already have calcualted
#this way I can reuse that and focus on just one case section at a time
#and loop through the digital candy list
#I should fill a two dimensional loop
#I can make each new loop and apppend it to the big loop

biglist=[]
testlist=[1,1,1,1,] #tabs for each line in a case
testlist2=[2,2,2,2,2,2]
biglist.append(testlist)
biglist.append(testlist2)

listofifs =[]

def big_gears_filling_list_with_case_bodies_2():
	mytrace('big_gears_filling_list_with_case_bodies_2')
	#mytrace('snowtime') #it calls snowtime() below
	#print("================  big gears filling list with case bodies called  ==========")
	counter=0
	for item in digitalcandy:  #=[[2,14],[14,26],[26,33],[33,3],[38,43],[43,47]]
		counter += 1
		snowtime(item[0],item[1])  #snowtime is called here





z =''
#this loopsthru the string of jsswitch between
#case numbers in line
mytablist=[]
sublist=[]
case_main_body_list=[]  #just added this oct 8th
#this copies the case body for each case section and addds it to case_main_body_list

def snowtime_2(x,y):  #this grabs the body from one case section at a time
	mytrace('snowtime()')
	global practicestring1
	practicestring1 = ""
	
	mycounter=0
	dog=''
	mytablist=[]
	for line in switchcasetester.splitlines():


		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line:

			if len(line) == 0: #this means that the line is empty

				mycounter += 1 #see if this is necessary here or not
				continue
			else:


				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
				sublist.append(dog)
				#print('the tabs are invisible and embeddd in the code string.')


		mycounter += 1
		#print(sublist)
	mytablist.append(sublist)
	#print("mytablist =",mytablist)

	case_main_body_list.append(practicestring1)  #the body case code is added here

	del practicestring1  #this nukes it
	practicestring1 ='' #clears it out

#=========================================================================






#===================================================
#global variable initialization here
#november 10th, 2020
theresult = ''
#testing_this_out function calls function input_string() which returns
#the docstring as a variable and is assigned to the global variable theresult



#=====================================================






















#line_numbers_of_first_cases
#look at this force feeding it input i need to find the generation of the inputlist


	#print("=======")

	#str = "'apple'"
	#print(str)
	#print(str.replace('"', ''))





#sunrise();

#what this does is take the input of teh [concatstring list] with line numbers
#which has the first case line number for each section
#I need the case number list name to feed it













#this_needs_to_work_badly();[2, 7, 17, 24, 34]
#theinputlist =[2,7,17,24,34]  #5 which is case_sections + 1 (default)
case_sections = 0
total = 5
#==========================
#I will have to dynamically initialize these


mainlist=[]
#diamonds=[[2,7],[7,19],[19,26],[26,36]]  what I am aiming to make
#these are lines of the first case line numbers and then the default line number


#theinputlist= [2, 7, 17, 24, 34]  #last one is default which is really a case


length_of_input_list = len(line_numbers_of_first_cases)   #question does this work because it's an even number
#output
mainlist= [] # [[2, 7], [7, 19], [19, 26], [26, 36]]



find_default=''
lastbrace=''

list_trex=[]
listcandy=[]
defaultlist=[]  #here defaultlist is declared as empty



	#digitalcandy.append(defaultlist)
###=============================================




## what this does is delete the existing last sublist from digitalcandy
## and then it replaces it with a new list appended that has the default line number and
## curly brace line number (can alternatively be the last line of string) both equal length





#==============
# this looks like good logic to check between default and closing brace/last line
# determined last line number also eventually
# december 7th, this is dependent on default word existing
# the point of this code section is to VERIFY that there IS a BREAK after default
# and if there isn't a break add one
#=========
#
#===============
#defaultlist=[]
'''

'''
###====================
####======== find_last_break_in_string  ========= in switchcasetester input switch
listofbreaks=[]
def find_last_break_in_string_2():
	mytrace('find_last_break')
	counter=0
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			counter +=1
		else:
			counter += 1
			continue
	baby = listofbreaks[-1] #the last one
	return baby #which is a string

#=========================
####### special addition to digital_candy 2
#############################################


#working on this December 17th new functions
'''

   
'''

######################
##  stage_four_2
#######################
def stage_four_2():
	mytrace('stage_four_2()')
	#print('stage four')
	#magictimenow_2()
	#convert_to_twin_list_2()
	#special_addition_to_digital_candy_2() #======added nov 25th, 2020
	#rule_the_earth_2()






#================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0


#this is a super important function I think I wrote it at the beach a few days ago
def testing_this_to_get_word_2():
    return
   



#testing_this_to_get_word()  #==================this should call it now
######################
##  stage_five_2
#######################
def stage_five_2():
    return#print('stage five')
    #testing_this_to_get_word_2()




    ###########################################################
    #these are the line number positions of first case for each section [2, 7, 19,26]
    #this looks in one section at a time for a break and fallthru
#diamonds =[]
    #this is all just raw code not even in a function
def does_this_run():
    mytrace("does_this_run")
    c = 1    #current case numbr section
    d = c + 1

    x = clever[0]
    y = clever[1]
             #this loops by default through the entire string
             #for line in splitline().switch:

     #=======================================================
     #this is looking between x and y which are in diamonds
     #========================================================

    counter =0
    case1 =[] #case number list to add fallthru
    case1findbreak=[]
    case1findfallthru=[]
    #print("testing getting the dam range to work")
    #print("looking for BREAK in this case section")
    smartcounter=0
    #look for BREAK in range of lines
    ##================================================
    ## LOOP LOOKING FOR BREAK IN CASE SECTION CODE
    ##================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "break" in line:
               # print("we found a break",smartcounter)
                case1findbreak.append("true")
            else:
                case1findbreak.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;


        #look for FALLTHRU in range of lines
    #print("starting 2nd loop now looking for FALLTHRU")
        #=========================
    smartcounter=0 #reset at zero
    ##=========================================================
    ## LOOP LOOKING FOR FALLTHRU IN CHUNK OF CODE INSIDE OF A CASE SECTION
    ##===========================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "fallthru" in line:  #what about fallthrough also to test for
                #print("we found a fallthru",smartcounter)
                case1findfallthru.append("true")
            else:
                case1findfallthru.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;



   #this is all so clever
   # looks inside of lists for breaks, fallthrus
    if "true" in case1findbreak:
        #print('break found')
        royallist.append('break');

    if "true" in case1findfallthru:
        #print('fallthru found')
        royallist.append('fallthru')

    if "true" not in case1findbreak and "true" not in case1findfallthru:
        #print("need to add a fallthru")
        royallist.append('fallthru')

    #print("royallist=",royallist)
###########






#//=========== iron curtain============================

 ##===============================================================
  ####=================== American River Methods ==================
  ##===============================================================


  #================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.







######################
##  grab_body_of_code_inside_case_sections_2
#######################
buildlist=[]
def grab_body_of_code_inside_case_sections_2():
    mytrace("grab_body_of_code_inside_case_sections")
    #print("grab body of code called== @@@@")
    smartcounter=0  #reset at zero

    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)

        if smartcounter > x and smartcounter < y:  #so get what's inbeteen
       #this should only print the body of this one case section
            if "case" not in line and "break" not in line and "fallthru" not in line:
                #print(line)
                buildlist.append(line,smartcounter);
                smartcounter += 1;
                #do I need continue?





#august 27 thurday coding test       this will be the sets of cases for each case section
caseset=[]
###############################
## create_case_name_lists_2
###############################

def create_case_name_lists_2(x,y):
    #print("==$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==")
    #print("================this is line 1615===CREATE CASE NAME LISTS=====================")
   # print("def create_case_name_lists:")
    #print("working on fix to solve bug if user uses more than one word for a case")
    #print("such as alpine meadows whereas right now its geared for one word cases")
    
    mytrace('create_case_name_lists')
    #print("=================create case name lists called == @@@@")

    smartcounter=0 #reset at zero
    genius = ''
     #need list of first cases that will work for input
    
    ##===================================================================
    ## LOOP LOOKING  CASE SECTION APPEND LINES FROM BODY AFTER CASES UNTIL NEXT FIRST CASE
    ##=======================================================================
    #print("here we get the words in each case section=====------")
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter < y:  #so get what's inbeteen
        #this should just look
            if "case"  in line:
                #print("did it take off front of line?")
                #print(line.split(' ',1)[1])
                #print(line,smartcounter)
               # print("=================================")
                genius =line.split()
                #print("genius =",genius)
                #print("======= len(genius) ==============")
                #print("WE ARE HERE==>>>>")
                #print('number of words in the line case = len(genius) ',len(genius))
                
                #print("number of words in this line =",len(genius))
                #print("it's current state is only grab the second word which is position [1] by default")
                ap=''
                #testing with more than one word the defualt was the first one
               #================  jan 3, 2021 code fix experimentiong case alpine meadows
                if len(genius) == 2:
                    #print('teh default was 1 word case and one word')
                    caseset.append(genius[1])
                    #print(caseset)
                    
                if len(genius) == 3:
                    #print('teh default was 3 words case and two words')
                    ap =genius[1] + genius[2]
                    caseset.append(ap)
                    #print(caseset)
                    
                if len(genius) == 4:
                   # print('teh default was 4 word case and 3 words')
                    ap =genius[1] + genius[2] + genius[3]
                    caseset.append(ap)
                    #print(caseset)
                    
                if len(genius) > 4:
                    #print("more than four words in this line detected")
                    #print("just do the default for now will fix later")
                    caseset.append(genius[1])
                    #print(caseset)
                
                #print("it looks like I'm just grabbing the first word of a case which I initially tested it with")
                #print('line 1632')
                #print(caseset)
                #buildlist.append(line);
                smartcounter += 1;

    #print("caseset list for one case section=",caseset);
    wilsonball=[]
    wilsonball.append('starter')
    wilsonball.append(caseset)
    #print("******** === wilsonball=",wilsonball)





#do bypass before even doing switch case

'''
if number quick check if number in list
get highest_number in list of numbers
if entered number > highest_number 
   goto default case
   print("msg your number is not in list")
'''








#this actually looks for breaks, missing beaks, and fallthrus
####=====================
##case_tail_list_maker_2() finds breaks, missing break detection, fallthrus
##========================
def case_tail_list_maker_2(x,y):
    #empty_list(royallist)
    mytrace('case_trail_list_maker_2')
    #print("=######	C A S E    T A I L   M A K E R called  ")
    smartcounter=0
    #this looks for "case" in the switch case string
    print("what the hell is in switchcasetester")
    print("///////////////////////")
    #print(switchcasetester)
    print("//////////////////////")
    for line in switchcasetester.splitlines(): #switch case in JS
        if "case" in line: #see if this puppy works
            firstline = line.split()
          #  print(firstline)
          # print(firstline[0])
            smartcounter += 1;
        else:
            smartcounter +=1;

    #here we get the location of the "default"
    smartcounter=0
    for line in switchcasetester.splitlines(): #switch case in JS
        if "default" in line: #see if this puppy works
            firstline = line.split()
            location_of_default = smartcounter
            break
            #smartcounter += 1;
        else:
            smartcounter +=1;



   #not sure if I am using c and d or not or if I switched to x, y instead
    c = 1    #current case numbr section
    d = c + 1



    #print("x",x,"y",y);
    counter =0
    case1 =[] #case number list to add fallthru
    case1findbreak=[]
    case1findfallthru=[]

    smartcounter=0
    #look for BREAK in range of lines
    ##================================================
    ## LOOP LOOKING FOR BREAK IN CASE SECTION CODE
    ##================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "break" in line:
               # print("we found a break",smartcounter)
                case1findbreak.append("true")
            else:
                case1findbreak.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;

     #we ARE STARTING A SECOND LOOP HERE -------------------
        #look for FALLTHRU in range of lines
    #print("starting 2nd loop now looking for FALLTHRU")
        #=========================
    smartcounter=0 #reset at zero
    ##=====================================================================
    ## LOOP LOOKING FOR FALLTHRU IN CHUNK OF CODE INSIDE OF A CASE SECTION
    ##======================================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "fallthru" in line:
                #print("we found a fallthru",smartcounter)
                case1findfallthru.append("true")
            else:
                case1findfallthru.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;
    #I think that this is the end of the for loop here



   #this is all so clever
   # looks inside of lists for breaks, fallthrus
    if "true" in case1findbreak:
        #print('break found')
        royallist.append('break');



    if "true" in case1findfallthru:
        #print('fallthru found')
        smart = len(royallist)  #new code
        smart += 1
        #before I add this one         so I am putting a number here which is used
        fall = "fallthru" + str(smart)  #to call the correct word in starbuckslist
        #print("we have",starbuckslist[smart]," added to fallthru")
        #I will need to do this
        #  fall = "fallthru('" + starbuckslist[smart] + "'")
        royallist.append(fall)
    wolf =''
    if "true" not in case1findbreak and "true" not in case1findfallthru:
        #print("need to add a fallthru")
        sosmart = len(royallist)
        sosmart += 1   #number below so it makes fallthru4 in example
        fall = "fallthru" + str(sosmart) #+ ")"  #just added this  thursday night
        #print("we have",starbuckslist[sosmart], "added to fallthru")
        #print("smart is length of royal list before adding fallthru",sosmart)
        wolf = "fallthru(" + "'" +  str(sosmart) + "'" + ")"  #this makes fallthru(4) which I need
        #because I can convert the number to a word in new list
        #print("wolf=",wolf)  #so this works
        royallist.append(fall)
    print("=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=00=0=0=0==")
    print("=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=00=0=0=0==")
    print("=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=00=0=0=0==")
    print("=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=00=0=0=0==")
    
    print("royallist=",royallist)
    #this changes the first position which is [0] fallthru1 to starter
    royallist[0] = "starter"
    print("now royallist has this in it")
    print(royallist)











tail_list=[]
cranberries=[]
cranberries.append('starter')
##===========================
##==== def p51_mustang_2() ===  adds the number to  fallthru(3) like that
##===========================
  #this makes the cranberries list which is the tail list used on codegen page
#diamonds=[[2,7],[7,17],[17,24],[24,34]]
#this makes the cranberries list
def p51_mustang_2(): #makes critical cranberries list which is the taillist for switch cases
	return


###############################
## stage_six_2
###############################
def stage_six_2():
    return#print('stage six')
    #p51_mustang_2()







#The purpose of this method == flyingcloud == is to
#fill small lists with
#the respective case names
#get case names in each set and add to list





#=====================================
#========== flyingcloud ==============  Thursday morning coding
#=====================================
#case1list=[]
#case2list=[]
#wilderness=''
#wild=''
#diamonds=[[2,7],[7,17],[17,24],[24,34]]

#this is used for the caselists that are generated for
#the python output for each case section there is a list
#and if the programmers writes more case sections and there
#isn't enough lists then the switch will fail
#so I started with ten case section lists and just expanded
#it to a thousands. You can always add more.


#forcing it to see what happens november 21st
#caselist7=['default']


#we will know before hand how many caselists will be filled 4

#this makes the first case list called starbucks which is used throughout the program
##==========================
##   flying fish 2            this loops through the dimaonds list of first cases
##==========================
def flyingfish_2():
	return




##==========================
##   flying cloud_2            this builds a list of the case names for each section
##==========================
#smartcasemanager=[]
#for x in smartcasemanager[:]:
		#smartcasemanager.remove(x)

#if smartcasemanager has anything in it empty it completely

#if len(smartcasemanager) > 0:
#	print('yep something in smartcasemanager length was',len(smartcasemanager))
#	del smartcasemanager[:]

#smartcasemanager.append("['starter']")

def flyingcloud_2(x,y,z):
	return
	
	


einstein=[] #resets einstein to empty
	#========================================
#this fills up smartcasemanager list
###############################
## nightowl_2
###############################
def nightowl_2():
	return
	


#this prints out the smartcasemanager list to verify that it worked and has the sublists

#=================================
def goodseason():
	mytrace('goodseason')



###############################
## stage_seven_2
###############################
def stage_seven_2():
    return#print('stage seven')
    #flyingfish_2()


#wilson=''
#mystring =''

#============================
#      wildgame
#============================
#or am I using the current case number or next case number for fallthru
#so does it represent the current location and then we add 1 to it or does fallthru(#) have
#the next number position embedded in it already
#this will go through the list and convert the fallthru(#) into names making the gold tail list
#which is used to build the case sections









goldtaillist =[]
#I need to loop through this list and create the new list for final gold tail list
def autumn_2():  #this builds the break fallthru(nextcasename) list
	mytrace('autumn_2')
	#print("autumn leaves falling")
	#print("autumn called to make new list of breaks and fallthrus final")
	#print("please work I need this to work")
	counter =0
	#print('starbucks =',starbuckslist)
	#print("mintlist =", mintlist)
	for item in starbuckslist:
		print(item)
		#goes through list


		if item == "break":
			#print('break found')
			goldtaillist.append("break") #how come it doesn't append this
			counter += 1


		if  "fall" in item:
			#print('fallthru found!')
			#print('counter=',counter)
			result =wildgame(counter)  #it wants a number use the counter
			#print("wildgame() result=",result)
			goldtaillist.append(result)
			counter += 1
		else:
			counter += 1

		if item == "starter":
			goldtaillist.append("starter")
			counter += 1
			continue

		if item == "default":
			goldtaillist.append("default")
			counter += 1
			continue

	#print("goldtaillist =",goldtaillist)




#autumn()



crushit =[]









#thurday, september 10, 2020 truck stop insight
#=============== stars() =============================
#=========== this goes thru dummy list with just starter fallthru and break and default
#==========/=== and adds the numbers of teh fallthru locations into cru0list
#=======================================================

miraclelist=[]
###############################
## stars_2
###############################
def stars_2():
	mytrace('stars')
    #print('STARS test of loking for words in list')
	#print('look for break default starter fallthru')
	#print("listnow =",listnow)
	counter =0
	#print("starting looking in loop")

	for item in listnow:
		if "break" == item:
			#print('break')
			crushit.append("break")
			counter += 1

		if  item.startswith("f") == True:
			#print('fallthru found')
			crushit.append("fallthru('" + str(counter) + "')")
			counter += 1

		if item.startswith('d') == True:
			#print("default found")
			crushit.append("default")
			counter += 1

		if item.startswith('s') == True:
			#print("starter found")
			crushit.append("starter")
			counter += 1



	#====
	#starter is 0 but not a case
	#first case is position 1 (if fallthru(1)) it becomes fallthru(2) for conversion
	#so it is based on current position for the current case and then the NEXT case is +1
	#==========================================
	#input must be 1 or higher but less than the length-1 can't be starter (0) or default(length-1)
	wilson=''
	newnumber=''
	counter =0
	for item in cru0:
		if item.startswith("f") == True:  #fallthru or fallthrough
			#print("fallthru found")
			mystring=item
			#print('mystring=',mystring)
			wilson=int(''.join(filter(str.isdigit, mystring)))   #this extracts the number from a string
			newnumber = wilson + 1
			newnumber = int(newnumber)
			answer =starbuckslist[newnumber] #this gets teh string word out of the starbucks list of case names
			ohbaby = "fallthru('"  + answer  + "')"
			ohbaby =ohbaby.strip()
			miraclelist.append(ohbaby)
			counter += 1

		if item.startswith('d') == True:  #default is last case needs to have break
				#print("default fuound")
				miraclelist.append("break")
				counter += 1

		if item.startswith('s') == True:
				#print("starter found")
				miraclelist.append("starter")
				counter += 1

		if item.startswith('b') == True:
				#print('break')
				miraclelist.append("break")
				counter += 1








#======== adderrsmill==============================
case_main_body_list=[]
case_main_body_list.append('starter')  #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code


###############################
## big_gears_filling_list_with_case_bodies_2()
###############################

def big_gears_filling_list_with_case_bodies_2():
	return

import re  #for regular expressions
#this one
handy_list_of_tabs=[]
dual_slots=[]
crummy =[]
fiasco =[]
n_count_per_section=''
case_section_lines_of_code=[]

#new idea have line count based on first line of code in THIS section after if case
#and the first line is 1 and not 0 so it's human math thinking

###############################
## smarty_2
###############################
def smarty_2(x,y):  #this grabs the body from one case section at a time
	mytrace('smarty_2')
	#print("=====/////======= smarty called ====2340=====//////=====")
	#print("line 818 snowtime(",x,y,")  S  N  O  W  T  I  M  E  ")
	#print("=====================  snowtime called", x, y," ===================")
	#print("smarty x y testing blank lines existence to delete them")
	global practicestring1
	practicestring1 = ""
	mycounter=0
	for line in switchcasetester.splitlines():
		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line  and "}" not in line \
		and "{" not in line:
		#this takes out the empty line by skipping it

			#added this sept 17 2020 to eliminate empty lines that do and mean nothing
			if len(line) == '\n': #this means that the line is empty
				#print("yes an empty line")
				#print(line.count("\n")) #just added this
				#del line #does this work
				mycounter += 1 #see if this is necessary here or not
				continue
			else:
				#I will already know ahead of time how many lines of code output
				#in each case section
				#print building practicestring1 adding lines of strings
				#if lastline == "true":
				#	practicestring1 += line

					#else:
					#by default each line will require 2 tabs in front of it
				line=line[1:] #takes off first tab off from front of line

				#We know the length so if last line no \n on end

					# ============== Glory =======================
				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
					#=============== Glory =======================
					#line 2386 where the fun is

					#Right here  flag whether to add  + "\n"





			####################
		mycounter += 1

	#this would be the string and nuke last line trailing \n which I know will be there
	practicestring1 = practicestring1.rstrip("\n")
	### and here the practice string is added (appended) to case_main_body_list
	case_main_body_list.append(practicestring1)  #the body case code is added here

	del practicestring1  #this nukes it
	practicestring1 =''  #here we nuke practicestring1 so I can reuse for each case section
	#print("=========")
	#print("list of tabs=",handy_list_of_tabs)
	#print("number of lines with code =",len(handy_list_of_tabs))
	#print("pairs tabs and line number ",fiasco)
	#print("number of lines in each section =", n_count_per_section)
	#case_section_lines_of_code.append(n_count_per_section)
	#print("=========")

def loop_thru_case_sections_2():
	#print("======== loop thru case sections =============")
	mytrace('loop_thru_case_sections_2')
	#print("loop thru cases sections which is a list")


#loop_thru_case_sections()  #=================

###############################
## stage_eight_2()
###############################
def stage_eight_2():
	mytrace('stage_eight()')
	#print('stage eight')
	#loop_thru_case_sections_2()


icecream=''
###############################
## herewego_2()
###############################
def herewego_2(): #loops and prints all main bodies
	return 
	
	

print("")

acounter=0
#for item in case_main_body_list:
#	print(len(item))
#	acounter += 1










#print("digitalcandy=",digitalcandy)
#big_gears_filling_list_with_case_bodies()
#herewego()  #==================================
###############################
## stage_nine_2()
###############################
def stage_nine_2():
	mytrace('stage_nine()')
	#print('stage nine')
	#big_gears_filling_list_with_case_bodies_2()
	#herewego_2()


#print("tail_list cranberries =",cranberries)
###=============================================================================
x = 0;y =0
smart=''
#cranberries=[]
list_of_rows_of_case_names=[]


#making case section sublists here
#this is for making the variable lists to fill the case sections of cases
# and to refer to each of these caselists with ifs and elifs




###############################
## make_case_sets_2()
###############################

def make_case_sets_2():
	mytrace('make_case_sets_2')
	#print("===== make_case_sets called ====")
	acounter = 0
	firstcasesectionlist=[]
	firstcasesectionlist.append("starter")
	 #this will be the case name
	#print("we have length of ", len(digitalcandy))
	#print(digitalcandy) #so we can see our input values of digitalcandy list
	for item in digitalcandy:
		x = None  #zap them out perhaps
		y = None
		#what = digitalcandy[acounter]
		x = item[0]; y = item[1]

		z = acounter
		partynation_2(x,y) #partynation called here------ PARTYNATION -----------
		acounter += 1
	#adding default to see if it works
	#firstcasesectionlist.append("default")
	#this happens after the loop has finished
	#print("what 9999 is this =",firstcasesectionlist)
	#print("----------")
	counter=0
	list_of_rows_of_case_names.append(firstcasesectionlist) #since this will be the last one
	castle_time_2()

smartcasemanager=[]  #creating the initializing smartcasemanager







###############################
## castle_time_2()
###############################

#this just prints it out the sets of the cases for each case section
def castle_time_2(): #fills up smartcasemanager
	mytrace('castle_time_2')

	#list_of_rows_of_case_names.append("[['default']") #trying this
	#print("============CASTLE_TIME called ===========")
	count=0
	while count < len(list_of_rows_of_case_names):
		if count == 0:
			count +=1
			continue
		#print(list_of_rows_of_case_names[count][1:])
		count += 1

	#print("more testing to get this right")
	#for item in list_of_rows_of_case_names:
	#	print(item)

	##################################################
	### SMARTCASEMANAGER LIST FILLED HERE ############
	##################################################

	#this fills up list smartcasemanager from list_of_rows_of_case_names
	#this is doing a brute force copy of a list
	for item in list_of_rows_of_case_names:
		smartcasemanager.append(item)


	#print(smartcasemanager)
	smartcasemanager.pop()
	#print('after deleting last item in list')
	#print(smartcasemanager)

	finallist = ['default'] #see if this works
	list_of_rows_of_case_names.append(finallist)
	#print("this should be default below======+++")
	#list_of_rows_of_case_names[-1]
	#smartcasemanager.append("['default']") #using a default case so it can be fallthrud from above
	#print(smartcasemanager) #now we add default to the end or do we need to or not
#==========================================================
#======================== partynation =====================


###############################
## partynation_2()
###############################
list_of_rows_of_case_names=['starter']
firstcasesectionlist=['starter']
def partynation_2(x,y):  #this grabs the body
	mytrace('partynation_2')
	#print("====partynation======")
	global practicestring1
	practicestring1 = ""
	mycounter=0
	firstcasesectionlist=[]
	firstcasesectionlist.append('starter')
	#start loop
	#this specifically is looking for the word case
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		if mycounter >= x and mycounter < y \
		and "case" in line:     #just added default
			genius = line.split()
			wild=genius[1].strip()
			wild = wild[:-1]
			wild = wild[1:-1]

			firstcasesectionlist.append(wild)  #adding this case name to firstcasesectionlist

		mycounter += 1
	#end loop
	#This is forcing default into firstcasesectionlist
	#wild = 'default'   #major test here
	#firstcasesectionlist.append(wild)
	for item in firstcasesectionlist:
		item.replace('"',' ' )


	firstcasesectionlist[1:-1]
	for item in firstcasesectionlist:
		item.replace('"',' ' )
	#here the currently newly minted case list is added to the big list
	#which is called list_of_rows_of_case_names
	list_of_rows_of_case_names.append(firstcasesectionlist)



	firstcasesectionlist= []
	#firstcasesectionlist.append('starter')



###############################
## testingthis_2()
###############################
def testingthis_2():
	mytrace('testingthis()')
	#print(" this prints out the contents of the important lists")

	#print("==============================================")
	#print("digitalcandy list ========")
	#for item in digitalcandy:
	#	print(item)

	#print("starbucks list ====of first case names in each section ====")
	#print(starbuckslist)

	#print("smartcasemanager list ========", len(smartcasemanager))
	#for item in smartcasemanager:#
	#	print(item)

	#print("case_main_body_list list ========", len(case_main_body_list))
	#for item in case_main_body_list:
	#	print(item)
	#=== code gen here ====

###############################
## stage_ten_2()
###############################
def stage_ten_2():
	mytrace('stage_ten_2()')
	#print('stage ten')
	#make_case_sets_2()
	#testingthis()



#I just need the lists to build my code generation now to generation
#the logic right

#codegen is using the output lists from the parser

#this is the taillist

#this is bringing it altogether simulating it creating the
#switch case in three parts
#with a counter and a loop

#trace()
#lists for starbuvks_drive_thru_code.py
caselist     =[]
breaklist    =[]
fallthrulist =[]
defaultlist  =[]
blanklines   =[]
mixedlist    =[]
batterondeck =[] #I can have item to comapore with in here
seriestogether =[]
res =[]


alphalist =  ["a", "b", "c","d", "e","f","g", "h", "i","j","k","l","m","n", "o","p","q","r", "s", "t", "u","v", "w","x","y",":",";","(",")","{","}"]

#this will be the first
#print("this will run at the top of the page and call the functions in sequence\n")
#cranberries=[]
my_godzilla_list=[]
newlist=[]
smartylist=[]
tryagain=[]
coollist=[]
#test data here it will be one file and just flow down with no imports
#rodan=[2,7,17,24,34]

tabs =['starter',"\t","\t\t","\t\t\t","\t\t\t\t","\t\t\t\t\t","\t\t\t\t\t\t"]






firstcaselist=[]

#digital_candy=[[2, 7], [7, 17], [17, 24], [24, 34]]

switch_python_gen=''










###=================================================================
###  below I get the location of default and closing curly brace for end of switch
###  this is to be used for determining the default case which is utilized for
###  the situation of a fallthru down into default
###  this also adds one more case tothe regular cases and I need these parameters

#print("============ surgery here S=================================")
#print("")
###############################
## make_default_case_2()
###############################
def make_default_case_2():
	mytrace('make_default_case()')
	find_default = get_default_location_2()
	#print("NEW location of default =",find_default)

	lastbrace = get_closing_brace_2()
	#print("NEW location of closing brace =", lastbrace)


	#digitalcandy.append
#november 21st coding
#make_default_case()

## what I still need to put together to have the body of the default case
## and that will be used for the default case and the body of the else:


 ##so if line is > default and line is < lastbrace
 ##and "break" not in line
 ##and fill practice string and append the pracietce sting to case_main_body_list
##use snow(x,y) and a loop to grab the lines of code inside of default
##make sure "


#print(" this prints out the contents of the important lists")

#print("==============================================")
#print("digitalcandy list ========")
#for item in digitalcandy:
#	print(item)



#print("they all need to start with 'starter' in position 0")
#print("the big 3 need to have the same number of elements for the length to be the same")

#=============================================================
# smartcasemanager list   #list of lists of case names
# case_main_body_list     #body python code for each case section
# tail_list               #breaks and fallthrus
# digitalcandy

#===== inputs ========
#firstcasesectionlist
#list_of_rows_of_case_names
#case_main_body_list
#cranberries #taillist

#=============================================================
# smartcasemanager list   #list of lists of case names
# case_main_body_list     #body python code for each case section
# tail_list               #breaks and fallthrus

#===== inputs ========
#firstcasesectionlist
#list_of_rows_of_case_names
#case_main_body_list
#cranberries #taillist

#what smartcasemanager output looks like in ufos file
#this was tyhe failed attempt at managing the indentation over to the left
#for the switch case output in python and I have a simpler solution I will end up using.




		#counter += 1














###############################
## parktime_2()
###############################

def parktime_2():

	mytrace('parktime')
	import re
	myString = "\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
	#print(myString)
	output   = re.sub(r"[\n\t]*", "", myString)



###############################
## stage_eleven_2()
###############################
def stage_eleven_2():
	mytrace('stage_eleven()')
	#print('stage eleven')
	#parktime_2()


#input for the switch case happens (above) the docstring JavaScript switch case interface




######===================================================================
###======== switch_code_gen here ============
# add error mistake if no input for exp it will do nothing
# this is good for me to think of adding
# also add break if no break in default for input from js switch
# monday dec 14th thinking
# need to add input stuff here that is in the top running betterworks

sw=''
sweet =''
switch_gen=''
#testing input here
  #this has to be above the generated code

testlist=[]
exp =''

############################################################
########  SWITCH CODE GENERATOR INTO PYTHON ################
############################################################

#======================================
#  ====== project mr coffee ========
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen_2():
	return
	
	


	#this is called in switch as a method from angel_falls
	#to put string into varholder[1]
def dothis(x):
	varholder.append(x)
	#print(varholder[1]) 
	
	
def lovely_output():
	print(varholder[1])
	#print("lovely_output called")
	#print("")
	







###############################
## stage_twelve_2()
###############################
#this executes the generated python switch code
def stage_twelve_2():
	mytrace('stage_twelve()')
	#pass

		
	for x in caselist1[:]:
		caselist1.remove(x)
	
	for x in caselist2[:]:
		caselist2.remove(x)
		
	for x in caselist3[:]:
		caselist3.remove(x)
		
	for x in caselist4[:]:
		caselist4.remove(x)
		
	for x in caselist5[:]:
		caselist5.remove(x)
		
	for x in einstein[:]:
		einstein.remove(x)
	
	smartcasemanager=[]
	print(smartcasemanager)
		
	for x in testlist[:]:
		testlist.remove(x)
		
	print("after emptying einstein list we have")
	print("einstein=",einstein)	
	#global switchcasetester #new
	#switchcasetester =''  #new
	#print(switchcasetester)
	#case_main_body_list=[] #nukes it
	resetting_up_case_body() #clears out case_main_body_list then appends('starter') to it
	#print("caselist",caselist)
	#print("smartcasemanager",smartcasemanager)
	print('printing out lists contents to see what is actually in them')
	print("this is to determine what is in the lists after a switch case has")
	print("been generated and it no long needs the data from the parser")
	empty_list(smartcasemanager)
	empty_list(einstein)
	empty_list(defaultlist)
	empty_list(candy)
	empty_list(digitalcandy)
	empty_list(palmtrees)
	empty_list(gti)
	empty_list(drive_thru)
	empty_list(mochalist)
	empty_list(case1findbreak)
	empty_list(case1findfallthru)
	empty_list(line_numbers_of_first_cases)  #missed s after number
	empty_list(case_main_body_list)
	#empty_list(case_main_body_list_with_tail)
	empty_list(starbuckslist)
	empty_list(wilecoyote)
	empty_list(birdsong)
	empty_list(cranberries)
	empty_list(royallist)
	empty_list(roadrunner)
	empty_list(penguin)
	empty_list(caselist1)
	empty_list(caselist2)
	empty_list(caselist3)
	empty_list(caselist4)
	empty_list(caselist5)
	empty_list(caselist6)
	empty_list(caselist7)
	empty_list(caselist8)
	empty_list(caselist9)
	empty_list(caselist10)
	empty_list(caselist11)
	empty_list(caselist12)
	empty_list(caselist13)
	empty_list(caselist14)
	empty_list(caselist15)
	empty_list(caselist16)
	empty_list(caselist17)
	empty_list(caselist18)
	empty_list(caselist19)
	empty_list(caselist20)
	

	
	
	print("defaultlist=",defaultlist)
	print("candy=",candy)
	print('digitalcandy=',digitalcandy)
	print("palmtrees=",palmtrees)
	print("how many of these have data in them after the first switch?")
	print("gti",gti)
	print("mochalist",mochalist)
	print("drive_thru",drive_thru)
	print("einstein",einstein)
	print("smartcasemanager",smartcasemanager)
	print("testlist",testlist)
	
	#funny
	print("case1findbreak",case1findbreak)
	print("case1findfallthru",case1findfallthru)
	print("seal",seal)
	print("line_numbers_of_first_cases",line_numbers_of_first_cases)
	print("case_main_body_list=",case_main_body_list)
	#print("case_main_body_list_with_tail",case_main_body_list_with_tail)
	
	
		
	smartcasemanager=[]
	#print("candy=",candy)
	#print("starbucklist=",starbuckslist)
	#print("digitalcandy=",digitalcandy)
	#print("einstein=",einstein)
	#print("wilecoyote=",wilecoyote)
	#print('birdsong=',birdsong)
	#print("cranberries =",cranberries)
	#print("royallist =",royallist)
	#print("roadrunner =",roadrunner)
	#print("penguin =",penguin)
	#print("british =",british)
	#print('stage twelve')

	#print("caselist1=",caselist1)
	#print("caselist2=",caselist2)
	#print("caselist3=",caselist3)
	#print("caselist4=",caselist4)
	#print("caselist5=",caselist5)
	#print("caselist6=",caselist6)
	#print("caselist7=",caselist7)
	#print("caselist8=",caselist8)
	#print("caselist9=",caselist9)
	#print("caselist10=",caselist10)
	#this seems to work whereas nothing above actually worked
	## only guaranteed way to empty lists completely 
	for item in range(0,len(palmtrees)):
		palmtrees.pop()

	for item in range(0,len(digitalcandy)):
		digitalcandy.pop()

	for item in range(0,len(einstein)):
		einstein.pop()

	for item in range(0,len(wilecoyote)):
		wilecoyote.pop()
		
	for item in range(0,len(candy)):
		candy.pop()
		
		
	for item in range(0,len(case_main_body_list)):
		case_main_body_list.pop()
		
	

	for item in range(0,len(birdsong)):
		birdsong.pop()
##3====================
	for item in range(0,len(caselist1)):
		caselist1.pop()

	for item in range(0,len(caselist2)):
		caselist2.pop()

	for item in range(0,len(caselist3)):
		caselist3.pop()

	for item in range(0,len(caselist4)):
		caselist4.pop()

	for item in range(0,len(caselist5)):
		caselist5.pop()

	for item in range(0,len(caselist6)):
		caselist6.pop()

	for item in range(0,len(caselist7)):
		caselist7.pop()

	for item in range(0,len(caselist8)):
		caselist8.pop()

	for item in range(0,len(caselist9)):
		caselist9.pop()

	for item in range(0,len(caselist10)):
		caselist10.pop()
##3==========
	for item in range(0,len(royallist)):
		royallist.pop()

	for item in range(0,len(cranberries)):
		cranberries.pop()
		
	for item in range(0,len(roadrunner)):
		roadrunner.pop()
		
	for item in range(0,len(penguin)):
		penguin.pop()
		
	for item in range(0,len(british)):
		british.pop()
		
		
	###############
	#print("gti",gti)
	for item in range(0,len(gti)):
		gti.pop()
		
	#print("mochalist",mochalist)
	for item in range(0,len(mochalist)):
		mochalist.pop()
		
	#print("drive_thru",drive_thru)
	for item in range(0,len(drive_thru)):
		drive_thru.pop()
	#funny
	#print("case1findbreak",case1findbreak)
	for item in range(0,len(case1findbreak)):
		case1findbreak.pop()
		
	#print("case1findfallthru",case1findfallthru)
	for item in range(0,len(case1findfallthru)):
		case1findfallthru.pop()
		
	#print("defaultlist",defaultlist)
	for item in range(0,len(defaultlist)):
		defaultlist.pop()
			
	#print("seal",seal)
	for item in range(0,len(seal)):
		seal.pop()
	#print("this one is the HOLY GRAIL one")
	#print("line_number_of_first_cases",line_numbers_of_first_cases)
	for item in range(0,len(line_numbers_of_first_cases)):
		line_numbers_of_first_cases.pop()	

	#print('==== after clearing them we have ======')
	
	if len(palmtrees) > 0:
		palmtrees.pop()
	#print('after checking the length of the list this deletes more if greater than 0')
	#print("palmtrees=",palmtrees)
	#print("starbucklist=",starbuckslist)
	for item in digitalcandy:
		digitalcandy.pop()

	#print("digitalcandy=",digitalcandy)
	
	if len(einstein) > 0:
		einstein.pop()
		
	
	#print("=========")
	for x in smartcasemanager[:]:
		smartcasemanager.remove(x)
	#print("contents of smartcasemanager=",smartcasemanager)
	
	#print("see if this helps empty it smartcasemanager")
	for item in smartcasemanager:
		smartcasemanager.pop()
		
		
	#print("candy=",candy)
	#print("defaultlist=",defaultlist)	
	#print("einstein=",einstein)
	#print("wilecoyote=",wilecoyote)
	#print('birdsong=',birdsong)

	#print('british=',british)
	#print('penguin=',penguin)
	#print('royallist=',royallist)
	#print('cranberries=',cranberries)
	#print('roadrunner=',roadrunner)
	#print('case_main_body_list=',case_main_body_list)
	#print('case_main_body_list_with_tail=',case_main_body_list_with_tail)

	#if len(caselist1) > 0:
	#	caselist1.pop()

	#print("caselist1=",caselist1)
	#print("caselist2=",caselist2)
	#print("caselist3=",caselist3)
	#print("caselist4=",caselist4)
	#print("caselist5=",caselist5)
	#print("caselist6=",caselist6)
	#print("caselist7=",caselist7)
	#print("caselist8=",caselist8)
	#print("caselist9=",caselist9)
	#print("caselist10=",caselist10)
	
	#print("are these empty now for a clean slate after first switch?")
	#print("gti",gti)
	#print("mochalist",mochalist)
	#print("drive_thru",drive_thru)
	#funny
	#print("case1findbreak",case1findbreak)
	#print("case1findfallthru",case1findfallthru)
	#print("seal",seal)
	#print("this one is the Big Deal line_numbers_of_first_cases needs to be empty")
	#print("It was previously not being emptied obviously ... now it is")
	#print("apparently this one REALLY needs to be empty or I am screwed")
	#print("line_number_of_first_cases",line_numbers_of_first_cases)
	#print("===== bottom of stage twelve reloading module if possible")
	#print("might have to call function from another function")
	#importlib.reload(switchmodtrial7)
	#print('stage twelve')
    
































#######################################
##  convert_case_numbers_to_strings()
#######################################
#def convert_case_numbers_to_strings():
#	print(y)
#	print("Palomar Drive windy road up")
#	#print("convert_case_numbers_to_strings() called ")
#	mytrace('convert_case_numbers_to_strings()')
#	global switchcasetester
#	make_list_of_lines_using_thru_macro()
#	expand_thru_macro()
#	case_numbers_to_strings() 

#this is reading numbers in cases NOT STRINGS and converting them into strings

#this is new but I haven't tried it yet december 5th
def starter_sequence_mode_2():
	return
	#mytrace('starter_sequence_mode_2()')
	#this ensures that these are ONLY called if valve[0] is True
	#if valve[0
		








	
daisy=''
def parser_mode_2(a):  #in snoopy1.py
	mytrace('parser_mode_2 in snoopy1()') #was greatpumpkin
	print('=======INSIDE OF PARSER in snoopy1  =========')
	return
	


##############  added April 2nd, 2021  ###############################################
# this is a pre scan of the switch case input string to determine if


# this gets the line number of the first case in the switch case string








	
#this will need to be called for each specific thru line
###==============================================================
###================  expand_thru_macro()  ===================
###==============================================================

#inputnum = 1
#def expand_thru_macro1():
#nt(switchcasetester) #was mouse here 
#return ajax
			
			








#this should only go through the first case and then leave the loop
#this grabs the first case line from the switch case looking for a number
#this looks in the string switchcasetester string using a loop
#and in first line with case to see if there is a number or are numbers

#######################  this is used by faucet_valve to detect numbers
##       finbar()    ##  tests first case in switch for numbers
#######################  and returns True if numbers are used else False
def finbar():
	mytrace('finbar()')
	toowild='';global switchcasetester;counter =0;
	numberflag = False # by default until otherwise determined 
	for line in switchcasetester.splitlines():
		if "case" in line and "'" not in line and '"' not in line:  
			#print("so I can see what it sees I am printing the line")
			#print(line)
			toowild = line
			break #get out of the dam loop 
		else:
			counter += 1
			continue
	#end loop
	money= hasNumbers(toowild)  #returns True or False
	if money == True: #means has number(s) in it
		print("yes number in the line")
	else:
		print("no number in line")
	return money 



icetea=''
valve=[]
##########################################
#             faucet_valve()  this fills valve[0] with True or False for numbers
##########################################
def faucet_valve():
	mytrace('faucet_valve()')
	#print("=====faucet VALVE=======")
	#print("=====faucet VALVE=======")
	#print("=====faucet VALVE=======")
	#here it calls finbar() which looks for number in the first case line
	icetea =finbar()  #method finbar() determines if case has a number like case 4:
	print("icetea =",icetea) #True if numbers
	#decided to just return True or False for now
	valve.append(icetea) #valve[0] = icetea
	firstcase = valve[0]  #True if number otherwise a string so False
	#print("contents of valve[0]",valve[0])
	



############################################
##             is_number()
############################################
def is_number(inputString):
	mytrace('is_number')
	return any(char.isdigit() for char in inputString)







#what if I go thru switchcasetester
#and each line with case is just converted to lowercase
#it should work because it's still a string
#make the whole thing lower case



newlist =[];count =''




####################################################
##      swap_thru_lines_with_expanded_cases()     ##
####################################################
def swap_thru_lines_with_expanded_cases():
	mytrace('swap_thru_lines_with_expanded_cases()')
	print("swap thru lines with exanded cases() called...")
	global switchcasetester
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			#print(line)
			#print(" ")
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			# this is where it gets number that is now a string
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			print(cat)
			cool = smart[1][:-1]  #chops off : from end last char
			holder = "'" + cool + "'"  #this puts the number in quotes
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			#print("\t\t" + newline)  #adds tabs to front of it
			#print("next I will use replace to each case line")
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal
			#HERE is where the changed case numbers as strings are put into switchcasetester
			#will use a replace here to the switchcasetester string
			mycounter += 1
		else:
			mycounter += 1
			continue
	#print(switchcasetester) #this is to see the switch case input string after the modification
	##=====
	#after the numbers have been converted into strings



### LISTS ####
list_with_thru_macros=[]
list_with_thru_macros.append(0) #position 0 nothing
backwards_thru_list =[]  #initializing the list






############################################
##        change_to_into_thru():
############################################
def change_to_into_thru():
	mytrace('change_to_into_thru()')
	#print("change to into thru() called...")
	global switchcasetester
	#print("=========looping thru looking for to===feb 5th 2020====")
	#print(switchcasetester)
	mycounter = 0
	for line in switchcasetester.splitlines():
		simple = mycounter-1
		
		if "case" and "to" in line:  #this means the macro to
			#print(line)
		
			banana=''
			banana=switchcasetester.replace(" to "," thru ")  #just addded spaces
			switchcasetester='' #this nukes it resets it
			switchcasetester = banana
			#print("the result of changing macro to to thru is this:")
			#print(switchcasetester)
		else:
			pass






############################################
##	bottom_up_change_of_thru_line_test():	
############################################
def bottom_up_change_of_thru_line_test1():
	#print("bottom up change of thru line test() called")
	mytrace('bottom_up_change_of_thru_line_test()')
	global mouse
	global opal
	opal = ''

	#go thru the entire string")
	#and change each case number  into a string for preparing for python handling
	## this uses backwards_thru_list
	mycounter = 0
	
	
	#for item in backwards_thru_list: 
	#set mycouter to a number for line in mouse.splitlines() : #this goes thru the mouse string
		#print(line)






###############################################
##   make_list_of_lines_using_thru_macro()
###############################################
def make_list_of_lines_using_thru_macro1():
	#print("we are in make_list_of_lines_using_thru_macro1")
	#print("make lis tof lines using thru macro() called")
	mytrace('make_list_of_lines_using_thru_macro()')
	# make list of lines using thru macros()
	#go thru list and if thru in line add that line to list
	global switchcasetester
	thru_counter = 0
	for line in switchcasetester.splitlines():
		#just added the word to that means the same thing as thru
		if  "case" and "thru" in line:  #on
			list_with_thru_macros.append(thru_counter)
			thru_counter += 1
		else:
			thru_counter += 1
			continue
	#THIS IS the list with thru macros line numbers====")
		
	#then I need to reverse the list
	backwards_thru_list = list_with_thru_macros
	backwards_thru_list = backwards_thru_list.reverse()  #list reversed right here
	bottom_up_change_of_thru_line_test1()






smart =''
beta =''
opal=''
import re
foolish =''
newline=''
#case_numbers_to_strings changes number cases to strings with the number inside
# I still need to sniff and detect if the cases are numbers before calling this 
##############################################################################
#this converts the numbers to strings such as case 1:  to case '1': ####






#######################################
##    case_numbers_to_strings()    ##
#######################################
def case_numbers_to_strings_1(str):
	#print("THIS one was called line 4194....")
	#print("case numbers to strings () called")
	mytrace('case_numbers_to_strings1()')
	global switchcasetester

	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			#print(line)
			#print(" ")
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			#print(cat)
			#print("HOW DOES IT LOOK HERE???-----====")
			cool = smart[1][:-1]  #chops off : from end
			holder = "'" + cool + "'"
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			#print("\t\t" + newline)  #adds tabs to front of it
			#print("next I will use replace to each case line")
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal
			
			#HERE is where the changed case numbers as strings are put into switchcasetester
			#will use a replace here to the switchcasetester string
			mycounter += 1
		else:
			mycounter += 1
			continue
	#this is to see the switch case input string after the modification
	#after the numbers have been converted into strings



#above and before stage_one()

#===================================



			
			
	




###########################################################
# I can't assume that there is a to or thru macro in use
# this checks if at least one to or one thru in the entire switch case since it will
# be scanned entirely.
############################################################





## march 15th, 2021 Monday
##################################
valve=[]

##################################
## checks if first case is number
##################################
def check_if_first_case_is_number():
	# I think I can test if there is a number in the line that determines it
	#print("check_if_first_case_is_number called")
	mytrace('check_if_first_case_is_number()')
	# loop through switchcasetester
	# this only looks for the first case that it encounters
	counter =0
	numberflag = False # by default until otherwise determined 
	for line in switchcasetester.splitlines():
		if "case" in line:  #error this doesn't account for using thru or to
			grabchunk = line
		# I will need it to specifically look for if "case" in line and not "thru" or not "to"
		# another situation is if case and line and 'thru' in line or 'to' in line
		# however, no matter what I can just look if number in line meaning it's a number
		# and then just grab what is after the word case before : or thru or to
		# I think I can check if two numbers are in line
		#this apparently tests if 2 numbers in the line
			#print("== TESTING HOW MANY NUMBERS IN CASE LINE == if 1 or 2 numbers")
			if sum(map(str.isdigit, line)) == 2 and "thru" or "to" in line:
				#this checks if thru in line 
				####### RIGHT HERE THE FLAG NUMBERS IS FLIPPED TO TRUE AFTER THIS TEST
				#######  NUMBERS
				numbers = True  #this is used for knowing there is likley to and thru in use in case
				numberflag = True  #2 numbers in line 
				if  "thru" in line:
					print("'thru' detected and there are 2 numbers in the line")
				else:
					pass
				#this checks if to in line
				if  "to" in line:
					print("'to' detected and there are 2 numbers in the line")
				else:
					pass

			else:
				print("there are not 2 numbers in the line")
				#this checks if only one number in line and no thru or to in line
				if sum(map(str.isdigit, line)) == 1 and "thru" not in line and "to" not in line:
					#print("there is only one number in the case line")
					#print("here we have discovered there is indeed a NUMBER in case line")
					numbers = False  #meaning ONLY one number in case not two numbers 
					numberflag = True
				else:
					numberflag = False
					pass

			#this scenario is for just  case 2:
			#if  " thru " and " to " not in line:
			
			#print('== TESTING GRABCHUNK == to have it grab a number in case')
			#print("grabchunk",grabchunk)
			if grabchunk.startswith('\t\tcase'):
				grabchunk = grabchunk[7:-1]
				print("now grabchunk=",grabchunk)

			#test here if empty space at end of string
			if grabchunk.endswith(':'):
				grabchunk.replace(":","") #so rediculously stupid
				#grabchunk = grabchunk[:-1]
				print("now grabchunk=",grabchunk)
				grabchunk = grabchunk.rstrip() #to remove leading and trailer spaces
			#print("we now have (will it work) for grabchunk",grabchunk[:-1])
			#print("what happens after this is strange")


			#grabchunk = line[5:] #this cuts off 'case ' and ':' at end
			#print("first test of grabchunk=",grabchunk)
			
			#print("numberflag either True number or False not number",numberflag) #was super
			if numberflag == True:  #it was super == True
				#print("the first case True is a number",numberflag) #was super
				valve.append(numberflag) #was super
			else:
				#print("the first case False is NOT a number",numberflag) #was super
				valve.append(numberflag) #was super
			break
		else:
			#print("no case in line", counter)
			counter += 1
			continue
		# end if
	# end loop
	
###############====





disney_tron_trace_list=['starter']


##################################
##  show tron trace path        ##
##################################
def show_tron_trace_path():
	print("#######==== showing TRON TRACE path list =====#####")
	counter=0
	last =''
	disney_tron_trace_list.pop(0) #delete's starter position 0
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number





#######################
##     mytrace     ##
#######################
def mytrace(x): #just checks if first item is the same if slo don't load it
	disney_tron_trace_list.append(x)


###====================================
# march 18th, 2021 testing 9:45 am

###############################
##  hasNumbers(string)
###############################
#def hasNumbers(inputString):
# 	return any(char.isdigit() for char in inputString)


disney_tron_trace_list=['starter']
######## show tron trace path
def show_tron_trace_path():
	#print("#######==== showing TRON TRACE path list =====#####")
	counter=0
	last =''
	disney_tron_trace_list.pop(0) #delete's starter position 0
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number

#### mytrace
def mytrace(x): #just checks if first item is the same if slo don't load it
	disney_tron_trace_list.append(x)


#also do this for reset below

#this alters a string so the case doesn't matter, (think it's all lowercase)
#for laster # make it suitable for caseless comparison 
#str = str.casefold() 
numbers = False #by default and is flipped to True in 
digitalcandy=[]
######################### reset()  the module ##########
####### this makes it possible to call multiple switch cases that start out empty
######################################

# march 15th, 2021 at the beach =============================
# this has the names of vars I need to empty when flush
# the names of the vars are constant and I should hard code them in
list_of_vars=[]

# this holds the names of the lists I used in parser and codegen
# that will be flushed after generating a switch case
# the names of the lists will be hardcoded since they are unchanging
# and this listoflists is now actually emptied - it's a guide rail
list_of_lists=[]



# this resets the sw and switchcasetester variables
def reset():  #this now does nothing.
	#print("reset() called but does nothing now ....")
	global sw
	global switchcasetester
	sw='' #this empties it
	switchcasetester='' #this empties it
	return sw;

#zap var method
def zap_var(y):
	eval("y=''")  #this empties the var
	return y    




def change_list(zoo):
    #print("change_list() calleed")
    switch_config.init()
    switch_subfile.stuff(zoo)
    print(switch_config.mylist[0])
    


###############===================================




###////////////////////////////////////////////===========
###   American Standard  Flush all vars and lists clean
##///////////////////////////////////////////////////////////

#print("========= together =========")
#print(" did I just quote our principal? ")

#print("purely testing this now ")

#list_of_lists=["applepie","peachpie","lemonpie"]

applepie =["one","two","three"]
peachpie =["fun","silly","iceplant"]
lemonpie =["lemon tree","plum tree", "pear tree"]

##===========================
#this was for testing   
list_of_lists=[['applepie'],['peachpie'],['lemonpie']]



###==============
#new "thursday march 18th, 2021 today "
#this is the format that works for names of lists stored in a list
#this means that the vars also use a list of lists  of length 1 with string inside
list_of_vars = [['chilis'],['mystarbucks'],['jungle']]

#solution put the string in a list
chilis = ["one flew over the cuckoos nest"]
mystarbucks = ["is the drive thru open or not"]
jungle = ["better get walking"]

#target = list_of_lists[0]  this represents a list in a list position 0
#print_out_a_list(target) 

def print_out_a_list(target):
	nicejob= " ".join(str(x) for x in target)
	nicejob = nicejob.lstrip()
	nicejob = nicejob.rstrip()
	for item in eval(nicejob):
		print(item)
	
#target = list_of_lists[0] #get name of list in list by position
#empty_a_list(target)
#target = list_of_lists[1] #get name of list in list by position
#empty_a_list(target)
def empty_a_list(target):
	nicejob= " ".join(str(x) for x in target)
	nicejob = nicejob.lstrip()
	nicejob = nicejob.rstrip()
	sweet = eval(nicejob) #applepie
	del sweet[:] # will this work
	print(sweet) #should be []


def clear_out_list(i): # clear_out_list('fox')
	#print("clear_out_list() called")
	#print('startingit has apps jacks popcorn mtv')
	print(i)
	nicejob = i
	nicejob = nicejob.lstrip()
	nicejob = nicejob.rstrip()
	sweet = eval(i) #fox
	print(sweet) #['apps','balls','craps']
	del sweet[:] # will this work
	print(sweet) #should be []

fox = ['apps','jacks','popcorn','mtv'] #so an outside free floating list not in a list




###### empty_this_list_now(x) list name
def empty_this_list_now(x): #param is listname
	print("x=",x)
	x=[]
	print("x=",x)

# this means view_all_list_contents()
################################
##  see_each_list_contents()
###############################
def see_each_list_contents():
	mytrace('see_each_list_contents()')
	#print("see_each_list_of_contents() testing this now")
	counter=0
	#print("====== list_of_lists ====")
	#print("=== testing so I have utter and complete control ====")
	#print(list_of_lists[0])
	cards = list_of_lists[0]
	#print("this is what we are starting with ")
	#print(cards)
	#print("what I am testing here is getting the name of a list")
	#print("so that I can manipulate it")
	L = list_of_lists[0]       
	nicejob= " ".join(str(x) for x in L)
	nicejob = nicejob.lstrip()
	nicejob = nicejob.rstrip()
	print(nicejob) #should be the name of the list applepie
	#print("testing looping thru the list of applepie useing eval")
	for item in eval(nicejob):
		print(item)
	#print("====end of looping ===")





#empty_lists_in_list_of_lists()




 # flush all vars and all lists which will be done after codegen completed
 # this flushes the lists to empty and vars set to ''
 #################################
 ##      american_standard()  couldn't not working
 #################################
def american_standard():
	#flush lists
	mytrace('american_standard()')
	print("american_standard() called")
	#empty lists used in parser and codegen
	#note the list_of_lists does not get emptied, these are necessary for the data structure
	for item in list_of_lists:
		weasel=item[counter]
		print("list name=",weasel)
		#this loops through the list item from list above
		for item in eval(weasel):
			print(item)
			empty_list(item) #calls method empty_list()
			print(item)
		print("------------")
		#empty_list(item) #this empties this list to []
	#flush vars 
    #empty vars used  in parser and codegen
    #the list_of_vars[] does not itself get cleared it is for the loops reference
	for item in list_of_vars:   #which have their names in a list for convenience
		vartime=item[counter]
		print("list name=",vartime)
		for item in eval(vartime):
			print(item)
			zap_var(item) #calls zap_var() erases contents of var
			print(item)
		 #this empties this var to ''




#print("testing view contents of lists")
see_each_list_contents()
#print("flush lists clean")
#american_standard()










###################################################################
## this determines if numbers are used in switch case
## such as case 3 thru 30:  and case 1: etc and case 35 to 50:
## however odd case if a person uses case "4": that is a string though a number
## oh just thought what if someone enters numbers as strings!!!?? 
## dam another filter to add.
## THIS DETERMINES IF CASES USE NUMBERS NOT WORDS
## IT LOOKS IN FIRST CASE LINE IF NUMBER(S) ARE USED LIKE case 5:
#######################  this is used by faucet_valve to detect numbers
##       finbar()    ##  tests first case in switch for numbers
#######################  and returns True if numbers are used else False
def finbar():
	mytrace('finbar()')
	toowild=''
	#print("FINBAR ====$$$$ ===== called to test if detecting a number in string")

	#print("FINBAR ====$$$$ ===== called ")
	#print("FINBAR ====$$$$ ===== called ")
	global switchcasetester
	counter =0
	#this should only go through the first case and then leave the loop
	#this grabs the first case line from the switch case looking for a number
	#this looks in the string switchcasetester string using a loop
	#and in first line with case to see if there is a number or are numbers
	numberflag = False # by default until otherwise determined 
	print("ABOUT TO LOOK IN SWITCH STRING FIRST CASE FOR WORD")
	for line in switchcasetester.splitlines():
		#this will be the first case it test
		#just added "'" not in line and '"' not in line:
		################################################################
		if "case" in line and "'" not in line and '"' not in line:  
			#print("so I can see what it sees I am printing the line")
			print(line)
			toowild = line
			#print("this has to be the first case line the FIRST LINE")
			#print(line)
			#print("###################################")
			break #get out of the dam loop 
		else:
			counter += 1
			continue
	#end loop
	#uses method hasNumbers to determine if a string has number in it.
	money= hasNumbers(toowild)  #returns True or False
	print("is there a number in the string",money)
	if money == True:
		print("yes number in the line")
	else:
		print("no number in line")
	return money 
	#######
	









#this will need to be called for each specific thru line
###==============================================================
###================  expand_thru_macro()  ===================
###==============================================================















	


valve=[]
#def is_number(inputString):
#	return any(char.isdigit() for char in inputString)

# this has mode 1 to do words by default but if numbers calls methods to
# convert the numbers into strings and expand the macros to and thru and 
# create lists of cases if macros used
# # ex case 1:    #if firstcase is a number its True


##########################################
#             faucet_valve()
##########################################
def faucet_valve():
	#print("=====faucet VALVE=======")
	#print("=====faucet VALVE=======")
	#print("=====faucet VALVE=======")
	mytrace('faucet_valve()')
	icetea =finbar()  #method finbar() determines if case has a number like case 4:
	print("icetea =",icetea) #True if numbers
	#decided to just return True or False for now
	valve.append(icetea) #valve[0] = icetea
	firstcase = valve[0]  #True if number otherwise a string so False
	
	if firstcase == True: 
		#print("here means firstcase == True meaning a NUMBER:")
		convert_case_numbers_to_strings()
	else:
		pass
		#print('firstcase == False  meaning strings words')
		#meaning to the strings words as normal

	
	


#################################


#change_list("The Simpson's cartoon")
#print(switch_config.mylist)


#change_list("funny times")
#print(switch_config.mylist)

    ############################
    ### get_case_name()
    ############################
def get_case_name(y):  #y will be the line
    #print("get_case_name called")
    #y = y.split()
    y = y.replace(":","")
    y = y.replace("case","") #remove case
    y = y.replace("\t","")    # remove :
    #print(y)
    return y
    
    
    
    ############################
    ### get_location_of_case()
    ############################
    #debugging june 16th, 2021
def get_location_of_case(listname,word):
    print("called get_location_of_case(listname,word) line 5220")
    print("listname,word=",listname,word)
    #print("get location of case () called ")
    print("this is searching for ",word)  #below took out  + "'" + both sides of word
    ## june16th2021
    
    ##### the bug is here ValueError: None is not in list
    answer =eval("" + listname + ".index("  + word + ")")
    #print('====after running get_location_of_case we get this== should be a number==')
    print("location of case",word," in listname=",answer)
    return answer




def replace_in_list(x,y,z):  
	z[x]= y   #listname[5] = 'word'
	#this doesn't do print of the list afterwards




sneaky = ['british'] # I  can change the list it uses on-the-fly
#z = 'british' as global variable
###############################
##  do_replace(x,y)
###############################
def do_replace(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=british  #list name for breaks and fallthrus final
	replace_in_list(x,y,z) 
		
		
def smart_replace(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=penguin  #list name for breaks and fallthrus final
	replace_in_list(x,y,z) 
			
		
		
		
		
###################################
## do_replace_item_in_list
###################################

	# LISTNAME z   [x  NUMBER]=  y  WITH WORD using 3 inputs 
	###########################################
def do_replace_item_in_list(z,x,y): #listname[5] = 'word'
	replace_in_the_list(x,y,z)






#dec 31st
### for combo words like "alpine meadow" allow them in javascript interface
#of switch case and then concat them together with _ underscore
#for processing and then in output remove _ underscore


#from goldfish import ball #the string will that work
#dec 24, 2020 4pm pacific standard time progress putting code in module
#talking to goldfish right now which will be input file

#from triple_lindy import *
#imports the switch case

#defining varholder

strawberry_log=[]
#tbhis will be based on tron trace idea 

  ## WRITE STRING TO FILE
def write_string_to_file(xx):
	print("=====write string to file called ====")
	print("===PUT STRING INTO FILE =====")
	import os
	os.remove("sw_test.txt")  #this deletes the file
	f = open("sw_test.txt", "a")
	print("===about to add string switchcasetester to file===")
	f.write(xx)  #make sure it reads from goldfish
	f.close()

###############
##  check if default and check if beak in switch case#####
def add_break_to_default():  #and check if default too
    print("add break to default() current does nothing ")
    # look in stirng for break
    #if "break" in switchcasetester:
        #do nothing
    #actually also test here if default in switchcasetester stirng
      #and if not default then add default
    #else:
        #then add the break to default
        #brilliant;
        #first test if default case
        #if no default add default and break







   #READ STRING FROM FILE
def read_string_from_file():
	#print("====== read string from file called ======")
	#print("=== READ_FILE_PUT_INTO_STRING====")
	f = open("sw_test.txt", "r")
	boomerang = f.read()
	#print("=====output of string here=======")
	#print(boomerang)
	return boomerang


case_main_body_list=[]
def resetting_up_case_body():
	case_main_body_list=[]
	case_main_body_list.append('starter') 
	z =''
	
	
####################################################################
##  get_length_of_string()  the length of the switch case string
## this 
####################################################################
## get length of string()
mrdefault = 0
#this gets the line number of default (there must be a default)
#this also gets the length of the switchasetester string
def get_length_of_string():  #this only works if there is a default
	mytrace('get_length_of_string()')
	#print("######## get_length_of_string() called")
	#print("get length of string() called ====== ")
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
		#this is where the default is located on this line number
			mrdefault = counter;  #right here it assigns the counter number to mrdfault var
			#print("mrdefault=",counter) #this won't work without default word
		else:
			pass
		counter += 1
		
	#count backwards thru loop to get first break
		
	#print("length of the string =",counter)
	the_counter=mrdefault
	#print("we are starting to count from ",the_counter)
	solution ="false"
	for line in switchcasetester.splitlines():
		if "break" in line:
			#print('yes break after default')
			solution="true"
			break
	
		else:
			the_counter += 1
	
	
	#if solution == "true":
	#	print("break after default")
	#else:
	#	print("add the break at end")
	

	#the_last_line = counter
	#the length of the string of switchcasetester is returned here 
	return counter;  #it returns the length of the string in counter.


thebreak = False  #by default setting


############################################
##  wise_owl()  adds break to default case
############################################
def wise_owl(t):
	#mytrace('wise_owl()')
	#print("##### wise_owl() called with",t)
	#print("WISE OWL CALLED with ",t)
	#print("wise owl() called to add break to default case if it is missing ====== door number 3")
	#print("wise_owl input t =",t)
	if t == True:
		pass #print('already a break in default case')
	else:
		#print("it's obviously FALSE so add break to switchcasetesterstring")
		#print('no break detected so adding break at bottom of default')
		global switchcasetester
		#print("switchcasetester=",switchcasetester)
		################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		#######################################################################
		strawberry=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = strawberry
		#print("=====after adding break to bottom of default we have====== ")
		#print(switchcasetester)
	#print("t=",t,"already break beneath default") #this outputs the input paramter to see what wise_owl saw
		
#######


#we know from above the range of lines that the default is 
#we also know the last line number
#we start counting from the position of the default word
#################################################
##  testing_if_break_in_default_tail()
#################################################
### if there is default fine, but it requires a break (to be parsed)
## the reason is that at Yale is says that in C a break in default is optional
## but they also say at Yale that a default is REQUIRED
## so this tests that in default(is there a break and if not simply add a break

def testing_if_break_in_default_tail(): #assumes that there is a default!!!!!
	mytrace('testing_if_break_in_default_tail()')
	#print("######## testing_if_break_in_default_tail() called############")
	#print("testing if break in default tail() called=====DOOR NUMBER 2 ===")
	global mrdefault #I was missing this
	#print("mrdefault =",mrdefault)
	#get_last_break_in_string()
	#look at this carefully it starts the smartcounter with the line of default 
	smartcounter = int(mrdefault) #the starting point   #the default line number retrieved before this
	#print("for smartcounter starting we have ",smartcounter)
	thebreak = False #default setting boolean
	global switchcasetester
	for line in switchcasetester.splitlines():
		if "break" in line:
			thebreak = True
			break  #out of loop
		else:
			pass
			smartcounter += 1
	#print("thebreak=",thebreak) #this returns True in thebreak if there is a break in default
	#print("new roller coaster testing if break missing after default and ")
	#print("now add the break at bottom of default ")
	if thebreak == False:
		#print("add break to bottom of default case now right here")
		#global switchcasetester
		#print("switchcasetester=",switchcasetester)
		################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		#######################################################################
		staypuff=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = staypuff
		#print("=====after adding break to bottom of default we have====== ")
		#print(switchcasetester)
	
	#wise_owl(thebreak) #would be wise_owl(True) #adds break to default case if it is missing break
	#return thebreak  #would return True  or   False
    

#switchcasetester=''

#saw this on the web, doubt it works
def doesitwork():
    print(getattr(goldfish, seagull))



def felix(): #felix the cat for testing
	print("====felix called testing writing string to file =======")
	newyears=read_string_from_file()
	print('     ')

	print(newyears)
	print('     ')







'''
The difference is one is just in a wordname
and the other format is typed out
maybe I need to make it the triple string
previou idea was
'''









#def victory():
#	print("read the dam file")
#	#open and read the file after the appending:
#	f = open("sw_test.txt", "r")
#	print(f.read())

# I should have case names in a list
# merely check if word "not in" list then default
# I can go through the switch case input and build a list of each case name
# dec 27th thinking to detect if no matches using not in list so that
# I can return the entered value confidently
# I found them they are in the caselist taht is generated, where I can grab them
# and merely dump them into one big list using append
switch_return_value=['starter']

varholder=[]
varholder.append("zilch") #if nothing changes it's default

var2=[]
var2.append("zilch")


def is_number(inputString):
	return any(char.isdigit() for char in inputString)

valve=[]
valve.append("nada")
angel =''
input = ''

#it would already be tested if a number in the first case already 

#this is the clever() that is actually being called line 4847
# this calls faucet_valve to determine if cases are numbers or words
#apparently this needs to exist in this file
# I need to number them because I have several functions called clever()
def clever(i): #so it already exists we are changing its value
	print("clever() line 4851")
	#sw_reset()
	print("this is the clever() that is being called line 4850")

	 #this reloads the module
	varholder[0]='' #this should reset it to nothing
	reset()  #reset() is hidden inside of clever for input to the switch
	mytrace('clever()')
	print("clever() called in switch_mgrcat")
	#faucet_valve()
	#print("valve[0]",valve[0])
	print("if true then number in first case in switch so using numbers")
	print("if false then string word in first case in switch using words or char")
	print("clever called for input to switch case exp")
	varholder[0]= i
	#===this works and it fills a list with input from an argument
	#print('varholder[0]=',varholder[0])
	#print(varholder[0]) #to actually see proof
	return varholder[0]
	angel = varholder[0]
	## ===check if input is a number or a word with letters
	#====x = angel.isdigit() commented out march 17, 2021
	#print('about to call FINBAR() to look in first case line')





#apparently this needs to exist in this file
def moreclever(i): #so it already exists we are changing its value
	print("moreclever input called")
	varholder[0] ='' #clears it out
	print("clever called for input to switch case exp")
	varholder[0]= i
	#this works and it fills a list with input from an argument
	#print('varholder[0]=',varholder[0])
	#print(varholder[0]) #to actually see proof









#testing accessing switchcase from file goldfish
def mountain2(c):
	mytrace('mountain2()')
	print("===mountain 2called===playing with switch case ")
	var2[0]= c
	global weasel
	weasel = var2[0]
	print(weasel) #so by default it prints the input string
	
	################## print input switch case string ##########################
	################## if show_input_string[0] = True for show_input_switch_string ############
	#if show_input_string[0] == None: #this is new
	#    show_input_string[0]= False
	#end if
	#so bug is this is set to True when I set it to False june 4th, 2021  
	
	##### just commented this out for the time being #########################
	#if show_input_string[0] == True:
	#   #pass
	#   print(weasel) #it was printing the switchcasetester right here
	#else:
	#   pass #otherwise it wont print the input string
	    
	global switchcasetester
	switchcasetester =''
	switchcasetester = weasel







jazz=''
#thinking of putting the switch case in here
def galaxy(moon):
	print(moon)
	jazz = moon
	c = len(jazz)
	print(c)
	#I need to generate a long string

	#switchcasetester=moon
	#return switchcasetester



##########################
##  romanwall()(
##########################
def romanwall(j):
	mytrace('romanwall')
	#print("=======romanwall called=====")
	#I might have to concat it and make it into
	#virgin reutrn switchcasetester = '''
	#it might have to be generated and then eval(string) or exec(string)
	supertramp= j
	switchcasetester= j  #seeing what happens
	print(supertramp)
	#see if it can read what is in the string
	#just testing what I can do here with the string
	answer =supertramp.count("case")
	#print("the number of cases in this string =",answer)
	#print(switchcasetester)




def adjust_input(x):
	print("adjust input called with", x, "inside of yosemite")
	newstring =varholder.append(' + x + ')

	
	
	
	 #should print 4

# Remember that the output code gen is invisible and won't be seen by
# he programmer
case = ''
valve_setting=''
# =======  switch  =================================
def switch(x):
#####################  filter to determine if input is number or word/letter/alpha
	print("we are inside of switch now",x)
	global input
	
	global case
	#strings
	#print("switch method called",x)
	#if string
	if type(x) == str:
		x = str(x)
		case = x.lower()
		print("case =",case)
	
	



# =======   fallthru       =========================
# the magic is here fallthru actually calls switch
def fallthru(y):
    eval("switch('" + y + "')")


#varholder=[]
#varholder.append("walmart")  #position 0  varholder[0]
#varholder.append("0")      #position 1
# =======   testfunction    ========================
exp=''



def first_test():
	print(" ==  testing def first_test with switch case translate test====")
	#varholder=[]
	varholder[0] ="candy" #input value test

#### this is used to do a trace log of functions called #################
### this is called at the bottom show_tron_trace_path()
### and at the beginning of each function/method  mytrace(x) name inserted of the function




print("======")
print("practicing with list funnybusiness here for practice and fun")
print("======")
funnybusiness=['starter','wildone','wildtwo']
reset_list_to_just_starter(funnybusiness)
print(funnybusiness)

coyote_list=[]  #initialize it
#trontime= ['empty', 'switch', 'case', 'case', 'code;', 'code;', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'break', 'empty', 'case', 'case', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'default', 'code;', 'code;', 'break', 'code;']


# I can simply fill it manually with a loop and append
#print(trontime)

birdsong=['starter'] #assigned
music=[0]
colorful=[0]
#down here it was unassigned
#empty_this_list_now(birdsong) #clearing it before entering the function this time
#######################################
def make_list_of_first_cases():
#######################################
	#print("initially list length of birdsong is",len(birdsong))
	if len(birdsong) > 1:
		for item in birdsong:
			if len(birdsong) > 1: 
				birdsong.pop()
		#end loop
		if len(birdsong) == 2:
			birdsong.pop()

		if len(birdsong) == 1:
			print('length of this list is 1 is correct')
		else:
			print("this list is wrong should be length 1", len(birdsong))
	else:
		if len(birdsong) == 1:
			print('the length of',birdsong, 'is 1')
		else:
			print("this one slipped though and has a length greater than 1 ",birdsong)


####################
	mytrace('make_list_of_first_cases')
	#print("========== called make list of first cases() ===========")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			smart=line.split()        # separates case from casename
			birdsong.append(smart[1]) # this adds casenameto list birdson
			music.append(mycounter)   # list of number for case line
			mycounter += 1
		else:
			mycounter +=1
		#print("after the if this is the content of birdsong",birdsong)
	#print("I think that the list of line numbers of cases is called music",music)
	#print("list of first case names",birdsong)


	if len(music) % 2 !=0:
		music.append("0")  #this is a balancer if it's an odd number adds one more to it


#what I can do is have a simple true or false switch
#and leave the function calls where they are and if triggered true
#then they will be called otherwise they won't be called.


#start_trigger()

######################################
default_location=''
def get_default_location(): #line number location of the word default
	#print("=============get default location called =================")
	mytrace('get_default_location')
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
			default_location = counter
			break
		else:
			counter += 1
			continue
	#print("the default location line number =",default_location)
	return default_location
	
	
##############################################
##	add_break_to_bottom_of_default():
##################################################
lovely=''
def add_break_to_bottom_of_default():
	mytrace('add_break_to_bottom_of_default()')
	global switchcasetester
	#print("=========just called ADD_BREAK_TO_BOTTOM_OF_DEFAULT()=========")
	lovely = switchcasetester #the whole switch case string
	x = lovely.count('break')
	#print("there are ",x ,"breaks in the switch case")
	#test if break after default line
	#print('start phase 1 ....')
	
	counter =get_default_location() #the line number
	#print("counter starting value of default is",counter)
	findbreak = False #by default unknown at this point if a break after default
	#print("findbreak=",findbreak)
	#print('start phase 2 ....')
	
	for line in switchcasetester.splitlines():
		#print('counter=',counter)
		if "break" in line:
			break_location = counter
			findbreak = True
			#print('findbreak =',findbreak)
			break
		else:
			counter += 1
			continue
	#print('start phase 3 ....')		
	#print("the value of findbreak =",findbreak)
	#print("this is after the loop has gone through looking for break after default line")		
	if findbreak == True:
		pass
		#print("findbreak = True so do nothing break exists after default")
		#print("do nothing break exists after default")
		#print("it will be interesting if this is true, but I can test it")
		#print("the number of breaks found in the switchcasetester was",x)
		#print("let's look in switchasetester and see for ourselves.")
		#print(switchcasetester)
	else:
		#print("if at this point then break after default is False")
		#print("break is false and need to add it")
		#print("switchcasetester starting =")
		#print(switchcasetester)#have to add break with tabs before it
		peach=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = peach
		#print("after adding beak beneath default we have ")
		#print(switchcasetester)
		#print("end of BIG TEST for break in default addition")	
	#return break_location   (maybe we don't need this)
	
    
		








#########=============== get last break in string ==================
listofbreaks=[]
genius=''
nobreaks = "false"
def get_last_break_in_string(): #but what if no break??? march 1st bad assumption here
	#print("======BLINK182========get last break in string in the whole switch case string ============")
	mytrace('get_last_break_in_string()')
	counter=0
	global switchcasetester
	#test this right here and now
	#print("### @@@@@ simple test looking for any break in switch case string switchcasetester")
	#if "break" in switchcasetester:
	#	print("yes there is a break")
	#	
	#lse: #this means there are no breaks in the switchcase string
	#	listofbreaks.append("0")  ## this is new 
	#	print("no break in switch case")
	
	#print("starting loop looking for breaks in switch case")
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			nobreaks = "false"	
			counter +=1
		else:
			counter += 1
			continue
		###=============
	#print(switchcasetester)
	#print("testing length of listofbreaks list")
	#print("if no breaks in switch case then add a break after default now")
	if len(listofbreaks) == 0:
		#print("list of breaks is empty")
		#print("therefore there is no break in entire string ")
		#print("this means no break in default")
		#print("adding break at bottom of default case now")
		#global switchcasetester
		#this immediatley adds break after default
		courage=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = courage
		#print("we now have ((look for the new break in default")
		#print(switchcasetester)
		#################### looks for location of break in default
		newcounter =0
		#print("starting loop looking for breaks in switch case")
		for line in switchcasetester.splitlines():
			if "break" in line:
				listofbreaks.append(counter)
				nobreaks = "false"	
				newcounter +=1
			else:
				newcounter += 1
				continue
			
	else:
		#print("the list of breaks has",len(listofbreaks), " elements")
	#idea if no breaks add one
		genius = listofbreaks[-1]  #last break number
	#print("genius is the last break line number =",genius)
	
	if counter == 0: #means no breaks in string of switchcasetester
		#print("there aren't any breaks in the switch case")
		nobreaks = "true"
		#print("nobreaks = true")
	else: #counter greater than 0
		nobreaks = "false"
		#print("nobreaks = false")
		pass

	#print("lets see the list of breaks full list",listofbreaks)
	#print("the length of hits of lines with break so the length is ",len(listofbreaks))
	#print("the number of breaks = ",counter," if none then nobreaks = ",nobreaks)
	if len(listofbreaks) >= 1:
		baby = listofbreaks[-1] #the last one
		print("the last break line number is ", baby)
	else:
		print("the number of breaks in the string is None",0)
		
	return baby #which is a string
	
	
	
	
#############################


#I need to add a break if there isn't one saturday, December 5th
#it expects a break at bottom of default.
#and I just realized it requires a default but doesn't look for one
newton=''
orange=''
#this scans through input switch and changes default to case default
#switchcasetester=''
last_break=''
#this assumes that there is a default. I will just make it mandatory to have a default
################################################################################
### this does convert_default_case AND add break after default if it needs one
################################################################################
last_line_of_string=0 #initializes it 
#####################################
## this assumes that there is a default which should exist.
## I will deal with a missing default and insert one later


# so before convertind default to case default I need to count breaks from default down
# and if there isn't one in default add a break

#idea first pass makes switch with place holder innerswitch functionname with input
#but on second pass I make the second internal switch BRILLIANt

##################################
###  convert  default  case '':
mrlastbreak=''
lastbreak=''
###################################
def convert_default_case(): #I got this working November 26th, 2020
######################################
	#print("convert_default_case()  ===&&&&&-- CALLED Motel 6 test night")
	#add_break_to_bottom_of_default()  ##march 3rd, 2021
	mytrace('convert_default_case')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location()
	
	#print("the last break would be ",listofbreaks[-1])
	if len(listofbreaks) == 0:  #maybe it will be None
		pass  #print("no breaks in the whole switch case string")
	else:
		pass
	
	last_break=get_last_break_in_string() #what if it returns None???
	#this is new march 1st 2021 starbucks coding in earlying
	last_line_of_string = get_length_of_string()
	#print("the last line of string =",last_line_of_string)
	
	if int(last_break) < int(get_default):
		#print("there is definitely no break in default case")
		#print("and a break needs to be added immediately")
		######################################################
		#print("adding break at bottom of default case now")
		global switchcasetester
		tang=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = tang
		#print("we now have ((look for the new break in default")
		#print(switchcasetester)
	else:
		pass #print("there is a break inside of default")
	
	#print("====================")
	#last_line =get_closing_curly_brace() #its just the length of the string switchcasetester
	################# just commented out line above march 1st, 2021
	
	############################################################
	
	# IF default(LINE NUMBER) < last break(LINE NUMBER)  There is a break
	#########################################################################
	#oh my god this assumes that there is a break
	#so no matter what I should put a break after default
	# this says if default is after break meaning no break after it
	#this is dependent on the last break existing or any break for that matter; it assumes a break
	#however, if there is no break in the string I am hosed and need to realize that.
	#I can't assume that there will be a break above the default or after the default either.
	#print("this if test for get_default < last_break fails if no break in string")
	#print("it's based on the bad assumption that there is a break in the switch case")
	#print("so I need to modify it to check if there is a break in the whole string")
	#print("and if count('break') == 0 then the answer is None")
	#if line number of default is LOWER then last break line number
	
	#then there is a break AFTER the default
	
	if int(get_default) < int(last_break):  #### if default  < last break  
	#this means that last break in string is above the default. b
	#########################################################################
		
		#print("there is a break after default")
		#################################################################
		####  DEFAULT IS CHANGED TO CASE 'DEFAULT':            ########### 
		#################################################################
		#change default to case 'default':
		newton=switchcasetester.replace("default:","case 'default':")
		
		###==== tuesday coding project =====##
		## test right here if a break or not
		#need to test if break is after default or not
		# and add a break here if no break so the switch case gets read.
		
		switchcasetester=''
		switchcasetester = newton
		#print("")
		#print(switchcasetester)
		##I need to add the break to default here if it doesn't exist. 
		# I need to look if a break is between default and last line of switchcase
		# march 1st, 2021 I need to add a break to default if no dfeault
		#look between default word and {
		
		make_list_of_first_cases()
		#print(switchcasetester)
		return switchcasetester
		
		#the else  is triggered if int(a)> int(b) meaning break number LESS THAN default line num
	else:
		#down below here it adds break after default and makes case deafult
		#print(switchcasetester)
		
		########################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		## I can do a count for break  starting from the default line number
		## and discover if there is a break in default the only safe place I can put it .
		#this is now unecessary since it's alrady done.
		#######################################################################
		
		
		#orange=switchcasetester.replace("}","			break \
		#	\n}")
		#switchcasetester=''
		#switchcasetester = orange
		
		
		#print(switchcasetester)
		#################################################################
		####  DEFAULT IS CHANGED TO CASE 'DEFAULT':            ########### 
		#################################################################
		#change default to case 'default':
		newton=switchcasetester.replace("default:","case 'default':")
		switchcasetester=''
		switchcasetester = newton
		#print("")
		#print(switchcasetester)
		
		make_list_of_first_cases()
		#print(switchcasetester)
		return switchcasetester
	
	






def say(x):
    print(x)

def testing_number_of_lines_in_string():
	mytrace('testing_number_of_lines_in_string')
	count =0
	for line in switchcasetester.splitlines():
		count +=1
		#print(count)
	#print("there were ",count, "lines in string")
	return count



def testingatheory():
    mytrace('testingtheory()')

    #apple = "one"
    
    
    
    
###=================== nov 19th new code ============
###================ get_closing_brace (line number) ==============
closing_brace=''
def get_closing_brace():
	#print("get_closing_brace called")
	mytrace('get_closing_brace')
	counter =0
	closing_brace =testing_number_of_lines_in_string()
	return closing_brace




###=============================================
default_location=''
def get_default_location():
	mytrace('get_default_location')
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
			default_location = counter
		else:
			counter += 1
			continue
	return default_location



list1 =[]
list1.append("four")


#varholder[0] ="four"







#print("this is actual generated code I am trying to run now....")
#print("this is betterworknow in python generated previously")



list1=[]
exp =''; case =''
exp = ""

#exec(betterworknow)
#print("=== executin betterwork now test bit")




####======== starts here ===============
##################################
##          start_trigger()
##################################
#this is the function triggered to start the parser and codegen


# this is to circumvent a bug if no break in switchasetester it crashes
# this is to circumbent a bug if the user doesn't include a default case
# which is necessary since it has a break mandatory even if all above
# cases have no break which they can
# this way I'm not adding a break to a case that wasn't intended to ahve one

    #global switchcasetester
    #if "default" not in switchcasetester
    ## add dfeeault case with break
  
    #if "break" not in switchcaseter
        #add break to default which is the only one required to have break
        #since it's the last case 
    
      
###  right here I need to add
###  verifiy default and a break in switchcase strubg  to begin with
######################################
##    starter_trigger()  
######################################
	#global switchcasetester  #just added this to hopefully fix bug
def start_trigger():
	trigger = True  #default setting
	#print("trigger =", trigger)
	#if trigger == True:
	#	print("trigger =", True)
	#else:
	#	print('trigger=',False)
	mytrace('start_trigger')
	convert_default_case() #this changes default: to case 'default': but default needs to exist!
	output = testing_if_break_in_default_tail()
	wise_owl(output) #this should feed in the parameter of if break between default and last line of string
	#print("this will go first")
	### convert default case and then test if break in default and add break if necessary
	#this is done because in C and javascript it's just:   default: so it needs to be converted to a case
	#I will have it add break inside of convert_default_case()
	#convert default case called here 







## from web stackoverflow
def islist(obj):
    if ("list" in str(type(obj)) ): 
        return True
    else : 
        return False
################################
        
#line numbers with line_numbers_of_first_cases
#################################
foo =[]
def bar():  #call this when clever(input) called
    print("bar() called") # to clear out list to make sure it's empty 
    global foo
    #print('in here now')
    foo =[1]
    print(foo)

#bar()

def goldmedal():
    global foo
    #print(foo)
    foo.append("xmas time")
    #print(foo)
    
#goldmedal()

def silvermedal():
    global foo
    foo.pop(0)
    #print(foo)
    foo.append("nighttime")
    #print(foo)
    
    
#silvermedal()

def coolness():
    global foo
    foo=[]
    #print(len(foo))
    
#coolness()

def solid():
    global foo
    foo.append("water")
    foo.append("tennis")
    foo.append("gold")
    print(foo)
    print(len(foo))
    
#solid()    

def badass():
    return  #don't need this now
    print("badass callsed")
    global foo
    foo=[]
    print(foo)
    foo.append("starter")
    foo.append("charlie brown")
    foo.append("wilson")
    foo.append("frisbee")
    foo.append("target")
    foo.append("snoopy")
    foo.append("red barron")
    foo.append("coffee")
    foo.append("starbucks")
    #print(foo)
    print("==============")
    


def clearit():
    print("clearit()")
    global foo
    foo =["starter"]
    if type(foo) is list:
        print('a list')
    else:
        print("not a list")
    #print(foo)

#badass()

def showit():
    global foo
    print(foo)
####################
##    STAGE ONE
####################
def stage_one():  #this calls start_trigger()
    mytrace('stage_one')
    #print('stage one')
    #emptying the lists in question here that might be the problem
    #print("in stage_one() resetting lists palmtrees, carnberries, royalllist, british")
    #print("penguin, roadrunner, starbuckslist")
    palmtrees=[]
    cranberries=[]
    royallist=[]
    british=[]
    penguin=[]
    roadrunner=[]
    starbuckslist=[]
    digitalcandy=[]
    start_trigger()



# thursday january 21st testing early in morning
# .bug I see is line number of first case lists is wrong
#rule_the_earth()
# File "/Users/blakesouthwood/Desktop/python code /gold Switch case code/backups GOOD working gold master switch case/
#firefall_yosemite_falls.py", line 1322, in rule_the_earth
#   second_word = line.split()[1]
# also digitalcandy has the duplciate first 2,10 issue bug

#=====line numbers of first cases list====
#[2, 10, 16, 23, 29, 35, 41, 47, 52, 52, 2, 10, 16, 25, 26, 32, 38, 42]    

'''
##  so per MIT I need to use assertion checks
#  if (condition == true) 
    do this
    else
    assertion error put messsage and then
    call return
''' 

   





caselist     =[]
breaklist    =[]
defaultlist  =[]
blanklines   =[]
mixedlist    =[]
batterondeck =[] #I can have item to comapore with in here
seriestogether =[]
res =[]
getfirstword =[]
casephrase =[]
alphalist =  ["a", "b", "c","d", "e","f","g", "h", "i","j","k","l","m","n", "o","p","q","r", "s", "t", "u","v", "w","x","y",":",";","(",")","{","}"]
casesections =[]
casesectioncounter =[]
breakposition =[]
trontime =[]
tronlinenumbers =[]
fallthrulist = []
smartlist =[]
smartlistlocations=[]
fallthrulocations=[]
#theinputlist =[]
digitalcandy=[]
line_numbers_of_first_cases=[]

global woodstock #is this what it wanted to solve the bug
#global candy
#####this is where i'm testing now
line_numbers_first_cases =[]        

woodstock =[]  #testing this out   
candy =[]  #for digital candy    ###3 oh my god I had candy a global and candy a list  [] jeeze. 
#==================================     
def simple_test():  #call this when clever(input) called
    # print("================")
    # print("simple test of filling global list") # to clear out list to make sure it's empty 
    global line_numbers_first_cases
    # print('in here now')
    #print(line_numbers_first_cases)
    line_numbers_first_cases =['snoopy','linus','lucy','woodstock']
   # print(line_numbers_first_cases)
    #print("=============")

simple_test()   


def add_to_test_list():
    #print("==================")
    #print("add to test list attempt")
    global line_numbers_first_cases
   # print("in here now")
   # print(line_numbers_first_cases)
   # print("now adding three more words to it")
    line_numbers_first_cases.append("rediculous")
    line_numbers_first_cases.append("silly")
    line_numbers_first_cases.append("tired")
    #print(line_numbers_first_cases)
    #print("====================")
            
def empty_test():  #call this when clever(input) called
   # print("===============")
   # print("empty list") # to clear out list to make sure it's empty 
    global line_numbers_first_cases
   # print('in here now')
    line_numbers_first_cases =['starter']
    #print(line_numbers_first_cases)        
    #print("==================")
        
        
        
linenumber=[]        
dunkindonuts=['starter']
list_with_code=[]
jazz=['starter']
##################################################
def magictimenow():   ### this builds the list for line_numbers_of_first_cases using strings
##################################################
	mytrace('magictimenow')
	#breakpoint()
	#print("THIS IS MAGICTIMENOW TESTING WHERE THE BUG IS APPARENTLY")
	#print("down to 11% charge better hurry")
	#this should make it real
	global woodstock
	#print("========== what is in trontime? =======")
	#print("what the fuck is in trontime",trontime)
	#print("length of trontime=", len(trontime))
	
	if len(trontime) > 0:
		del trontime[:] #this empties the list trontime
	
	#print("trontime length is now",len(trontime))
	#print("now trontime should be empty by default - to cover all of the bases")
	#print("trontime=",trontime)
	
	
	#print("woodstock contains=",woodstock)
	#global candy
	#print("candy contains=",candy)
	#print("switchcasetester=",switchcasetester)
	mytrace('magictimenow()')
	#This makes a list of true if case in line and false if no case in this line
	#print("first fillup a list with true and false")
	#print("true if case in this line and false if not")
	#print("=== simple test if case in a line if so then True")
	#print("let us see what is in switchcasetester")
	#print(switchcasetester)
	#print("=== and if no case in this line then put False")
	#print("these true and false go into list called ifcaseinline")
	ifcaseinline=['starter']   #theresult
	#this loop puts true into ifcaseinline if case in this line otherwise it puts false
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		if "case" in line:
			#print(line)
			ifcaseinline.append("true") #adds "true" to list ifcaseinline
			continue
		else: #no case in this line
			ifcaseinline.append("false") #adds 'false' to list ifcaseinline
			continue

	#print("this should show list of each line and if case in this line")
	#print("ifcaseinline",ifcaseinline)

	#now just find pattern this line true and line above it false
	firsttestforfirstcase=['starter']
	coolcounter=0
	#print("about to test loop looking for first case")
	for item in ifcaseinline:
		if item == "true" and ifcaseinline[coolcounter-1] == "false":

			#print("the line number of teh first case is",coolcounter)
			firsttestforfirstcase.append(coolcounter)
			coolcounter +=1
			continue
		else:
			coolcounter +=1
			continue
	#print("finished",firsttestforfirstcase)#this is list of trues and falses
	#pertaining to if the word 'case' is in this line number of code

	counternew=0
	for item in ifcaseinline:
		#print(item,counternew)
		counternew += 1
	#print("=============================")
	#return #this kills the function and it stops


	counter = 1  #starting counting with 1
	a_string = switchcasetester
	first_word = a_string.split()[0]
	#print('big assed test here to get a first word in a string')
	#print(first_word)
	#get line numbers and see if sequential cases on neighboring lines
	word = 0
	mycounter=0  #switchcasetester
 	#this is where trontime list is filled with 'true' if line number has 'case' in it
 	#and 'false' is put if this line doesn't have the word 'case' in it

	#print("this is the beginning of the regular for loop through the string")
	num = 1  #for organizing case numbers in order of appearance
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		genius = line.split() #new  [0] was at end of it  ((this does the line split for each line))
		mycounter += 1
		#these are two different conditions see if it finds them
		######### these are new to filter it more strictly July 23, 2020
		

		if "case" in line:
			#getfirstword.append("case")
			trontime.append("case")
			#print('case found')
			continue

		if "switch" in line:  #force feed it
			getfirstword.append("switch")
			trontime.append("switch")
			#print("switch found")
			continue

		if "fallthru" in line or "fallthrough" in line:  #force feed it
			getfirstword.append("fallthru")
			trontime.append("fallthru")
			#print("linenumber of fallthru =",mycounter)
			smartlistlocations.append(mycounter)
			fallthrulocations.append(mycounter)
			continue

		if "break" in line:  #force feed it
			#getfirstword.append("break")
			trontime.append("break")
			breakposition.append(mycounter)
			continue
			##################


		if "default" in line:  #force feed it
			getfirstword.append("default")
			trontime.append("default")
			continue

		if len(line.strip()) == 0: 
			getfirstword.append("empty")
			trontime.append("empty")
			continue
        #I remember this line clearly I wrote it at cafe borrone in Menlo park
        #and I finally was able to get the detection of cases in the correct lines in the list
		if "case" and "break" and "default" and "switch" not in line and len(line.strip()) > 0 :

			getfirstword.append("code;")
			trontime.append("code;")
			continue

	#print("==========  CAFE BORRONE  ============")


	#print('this is looking in trontime')
	thecounter=0
	for item in trontime:
		#print(item,thecounter)  #commented out long list
		thecounter += 1

	#print("now this is new virgin code to detect a case that is the first case")
	#print("and this is done by also checking if the line above tested False for having a case")
	firstcaselist=[]
	#print("========here we do some more HALLOWEEN testing============")
	#print("-----this is getting the first case in each section to use in fallthrus-----")
	#this is designed to detect the first case in a case section by detecting a case
	#that does not have a case above it making it by definition the first case
	#now this means no blank spaces between lists of cases for this detection to work.


############## this is where line_numbers_of_first_cases is constructed ##################
##############  I should make this a separate function ###################################
	
	################### may 13th, 2021 coding #########################
	#this is where the line_numbers_of_first_cases list is filled with the line number of first cases
	 #nuked 'starter' from it
	
	#breakpoint()
	#print('what it sees in the input switch case line 6675')
	#print(switchcasetester) 
	#print("this is a simple pretest of cases")
	jumbocounter=0
	for line in switchcasetester.splitlines():
		#how we designate it being the first if no case above it on previous line.
		if "case" in line:
			#print("case found in this line")
			#print(line)
			
			jumbocounter += 1
			dunkindonuts.append(jumbocounter)
			#print("line number =",jumbocounter)
			continue
		else:
			jumbocounter += 1
			continue
	#end loop
	#print("dunkindonuts=",dunkindonuts)
	
#####################################################################

	#end loop
	#print("after finding default it should be below this line ..")
	#print("after sensing if default in switch case are",dunkindonuts)
	#print("so I can see what the computer sees and analyzes where the cases are and if default there")
	
	################### may 13th, 2021 coding #########################
	
		

	#print("now in JAZZ LIST list we have hopefully just the first cases")
	#print("and here is the list",jazz)
	#don't recall if I need to add default as a case think so
	
	#what this does is look in the current line for the word "case"
	#and looks in the trontime list for the line above the current line to make
	#sure that "case" is not in the previous line determined by the word 'false'
	#print("the counter in trontime might be wrong or missing or something")
	#print("trontime=",trontime)
	#print("WAIT WHERE'S MY PHONE??? What is in trontime",trontime)
	###### this printed trontime #########
	#for item in trontime:
	#	print(item)
		
	acounter=0
	#THE BUG IS EITHER HERE SOMEHOW OR IN TRONTIME
	#the trontime list only has trues and falses so true if case in line otherwise false
	for line in switchcasetester.splitlines():
		#this checks if case in this line but no case in line before it
		#the tricky part of this solution is that it is looking above the current line
		#trontime list holds true and false depending on if 'case' in that line number
		if "case" in line and "case" not in trontime[acounter-1]:  #tests if no case above this line with case
			#print('the line number is',acounter)
			line_numbers_of_first_cases.append(acounter)
			#global woodstock
			woodstock.append(acounter)
			#global tintoy
			#tintoy = genius
			genius = line.split()
			#print(genius[1])
			strng= genius[1]
			angel= strng[:-1]
			#print(angel)
			angel = angel.strip()
			firstcaselist.append(angel) #this should grab the case name
			#print('case found')
			acounter +=1
			continue
		else:
			acounter +=1
			continue

	acounter=0
	for line in switchcasetester.splitlines():
		#this checks if case in this line but no case in line before it
		if "default" in line:  #tests if no case above this line with case
			#print('the line number is',acounter)
			line_numbers_of_first_cases.append(acounter) #adds the default line number to list
			
			woodstock.append(acounter)
			genius = line.split()

			firstcaselist.append('default') #this should grab the case name
			#print('default found')
			acounter +=1
			continue
		else:
			acounter +=1
			continue
	######################################################
	#print("there I empty dunkindonuts, list_with_code, jazz")
	#empty these lists
	del dunkindonuts[:]
	del list_with_code[:]
	del jazz[:]

	#print("after empting the new lists we have ")
	#print("dunkindonuts=",dunkindonuts)
	#print("list_with_code",list_with_code)
	#print("jazz",jazz)
	######################################################
	smartnewlist=[]

	for item in firstcaselist:
		if item != "default" :
			item = item[1:-1]
			smartnewlist.append(item)

		if item == "default":
			smartnewlist.append(item)




###################################################################################


###### how do I pass a list
#this might work
def get_first_list():
	mytrace('get_first_list()')





#this finds teh first case in each case section and works
#should be: starter,apple, bananas,chocolate, fish,default
#digitalcandy=[[3,7],[7,19],[19,26],[26,33],[33,43],[43,46]]








#2, 3, 7, 8, 9, 10, 19, 20, 26, 27, 36
def go_thru_casenumbers():
	mytrace('go_thru_casenumbers')

	dacounter=0
	for item in music:

		dacounter += 1












mycounter=0
turtle_tab1=[]
turtle_tab2=[]
turtle_tab1.append('starter')
turtle_tab2.append('starter')
#print('looking for tabs in lines================')
#this is just testing in one case for now
#what I am trying to do is 2 loops one for each case section
#so for the second pass it should start at the next case occurrence
#so first I need to prescan it and get the line number of each case
#apparently the solution is using the digitalcandy list with
#the range of case line numbers which I already have calcualted
#this way I can reuse that and focus on just one case section at a time
#and loop through the digital candy list
#I should fill a two dimensional loop
#I can make each new loop and apppend it to the big loop

biglist=[]
testlist=[1,1,1,1,] #tabs for each line in a case
testlist2=[2,2,2,2,2,2]
biglist.append(testlist)
biglist.append(testlist2)

listofifs =[]

##### this calls snowtime inside of big_gears_filling_list_with_case_bodies()
def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	#mytrace('snowtime') #it calls snowtime() below
	#print("================  big gears filling list with case bodies called  ==========")
	counter=0
	for item in digitalcandy:  #=[[2,14],[14,26],[26,33],[33,3],[38,43],[43,47]]

		counter += 1

		snowtime(item[0],item[1])  #snowtime is called here with parameters two index numbers
		#from digitalcandy for the first case and next case line number
		





z =''
#this loopsthru the string of jsswitch between
#case numbers in line
mytablist=[]
sublist=[]
case_main_body_list=[]  #just added this oct 8th
#############################################################################
#this copies the case body for each case section and addds it to case_main_body_list
#### def snowtime fills up case_main_body_list with the body of code in each case section
#############################################################################
def snowtime(x,y):  #this grabs the body from one case section at a time
	mytrace('snowtime')
	global practicestring1
	practicestring1 = ""
	
	mycounter=0
	dog=''
	mytablist=[]
	for line in switchcasetester.splitlines():


		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line:

			if len(line) == 0: #this means that the line is empty

				mycounter += 1 #see if this is necessary here or not
				continue
			else: #if here then the line length must be greater than 0 so something is in it


				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
				sublist.append(dog)
				#print('the tabs are invisible and embeddd in the code string.')


		mycounter += 1
		#print(sublist)
	mytablist.append(sublist)
	#print("mytablist =",mytablist)

	case_main_body_list.append(practicestring1)  #the body case code is added here

	del practicestring1  #this nukes it
	practicestring1 ='' #clears it out

#=========================================================================




def cotton_candy():
	mytrace('cotton_candy')
	#print("===========cotton candy debugging jan 15th 2021==========")
	
	answer=''
	for item in range(1,len(case_main_body_list)):
		#print("item in cotton candy is",item)
		if isinstance(item,int): #if int is True
			pass
		else:  #if it's not int strip it
			item = item.strip() #not int  THIS STRIPS OFF SPACES
		
		if isinstance(item,int): #if int is True
			pass
		else: #if not int do this
			answer =item.count('\\t')  #COUNTS TABS BUT I DON'T THINK I DO ANYTHING WITH THEM
			answer = ''
#I think I was using this previously to calculate tabs to add 


def stage_two():
	mytrace("stage_two")
	#print('stage two')
	#cotton_candy()

#cotton_candy()


'''
	print("about to copy practicestring1 into sweetlist")
	#this goes through the practicestring1 string using a loop and appends 
	each line into sweetlist
	for line in practicestring1.splitlines():
		sweetlist.append(line)
	case_main_body_list.append(practicestring1) #add the string not a list
	del practicestring1  #this nukes it
	practicestring1 =''
	sweetlist[:] = []  #this empties the list
	print("===just cleared practicestring1 and sweetlist set to nothing====")
'''



#===================================================
#global variable initialization here
#november 10th, 2020
theresult = ''
#testing_this_out function calls function input_string() which returns
#the docstring as a variable and is assigned to the global variable theresult



#=====================================================






#counts tabs

#### =================== truckeeriver() ==================
def truckeeriver():
	mytrace('truckeeriver')
	casecounter=0
	mycounter = 1
	#print('truckee river called')
	for line in switchcasetester.splitlines():   #this was just going thru my prototype string of switch cases
		if "case" in line:				#and oh, I need to make sure I have tabs in my real js switch
			casecounter += 1
			if "case" not in line:
				if "\t" in line and not "break" in line and not "switch" in line and not "fallthru" in line and not 'case' in line:
					#print(line)
					dog=line.count('\t') #this counts the tabs in front of a line
					turtle_tab1.append(mycounter)
					turtle_tab1.append(dog) #dog this counts total number of tabs in this line


					mycounter += 1


		else:
			pass

	#print("turtle_tab1 list=",turtle_tab1) #should be just one slot


#truckeeriver()

def stage_three():
    #print('=====stage three====')
    mytrace("stage three")
    truckeeriver()







my_list=[1, 3, 4, 5, 6]
global coyote_length
new_c_list = []
####################################
def shrink_coyote_list():
	#print("======== shrink_coyote_list called ===========")
	mytrace("shrink_coyote_list")

    #get length of coyote_list
	global coyote_length;
	coyote_length = len(coyote_list)
    #print("the list length =", coyote_length)


	default_loc = coyote_list.index('default')


	for item in coyote_list:
		if item != "default":
			new_c_list.append(item)
			continue;
		else:
			break;



    #print("the length of the new shortened list =", len(new_c_list))
    #this is my solution for list out of range bull bug

	if (len(new_c_list))% 2 == 0:  #this would only be done once and modify the list
    #to manipulate.
		pass
	else:

		new_c_list.append('nada')






#============== get starting position in coyote




x = 0
destination =0
playwith =0
def get_starting_position_in_coyote(x):
    mytrace('get_starting_position_in_coyote')
    #print("getting starting position")
    answer =new_c_list[x]  #this is what I'm looking inside of the list
   






def get_current_position_in_coyote(x):
    mytrace("get_current_position_in_coyote")
    #print("getting starting position")
    answer =new_c_list[x]  #this is what I'm looking inside of the list







hopper_list =[]
def add_one_to_position_in_coyote(x):
    mytraace("add_one_to_position_in_coyote")
    #print("fall to position called")
    x= x + 1
    answer =new_c_list[x]

    destination = answer;




#print("okay the fun starts here =======>>>>>>>>")

# this figure out the number of case sections (number of case ifs really)
#it goes through the coyote list and checks if a line contains case and the next doesn't
#this works  july 30 2020
counter =0
casecounter = 0
list_of_cases =[]
while counter < len(new_c_list):
    #print(get_starting_position_in_coyote(counter)) #position 0

    if new_c_list[counter] == "case" and new_c_list[counter +1] != "case": #this represents the bottom of case set group
        counter += 1
        casecounter += 1;
        continue;
    else:
        counter += 1
        continue;


########################################
##  new_add_to_front() actually appending it to end of list
########################################
## it's adding it to the tail NOT THE FRONT

def new_add_to_front(x,listname):
	mytrace('new_add_to_front')
	#print(" ============ function new_add_to_front() called =======")
	#listname.insert(0, x) #cool it worked  this would add it to the front
	listname.append(x)

    #go through copy of that list and del items
    #I see this represents building the list











#what I already solved was how many sections of case groups there are
#now I need to get the remaining case locations
#if case not in line meaning after first case section so this would start after the last case in the first section
#July 30th, 2020 fun
# i should know how many cases in each section
####THIS GETS THE FIRST CASE IN EACH CASE SECTION THE LINE NUMBER
#starbuckslist=[]
#starbuckslist.append('starter')
genius =''
#diamonds=[[2,7],[7,19],[19,26],[26,36]] #this is input
#I have that list 2,7,19,26,36


#so quite simply I just need to cascade it down like a waterfall from above
#which shouldn't be too hard



#line_numbers_of_first_cases
#look at this force feeding it input i need to find the generation of the inputlist
#theinputlist =[2,7,17,24,34]  # case case case case default   I took off 36 default
total = len(line_numbers_of_first_cases)
palmtrees=[]  #defined here so it's global 
mochalist=[]
greenmilelist=[]
###################################
def rule_the_earth():
###################################
	#print("========rule the earth called========")
	#print("== DEBUGGING ==")
	mytrace("rule_the_earth")
	#print("line_numbers_of_first_cases")
	#print(line_numbers_of_first_cases)
	global woodstock
	#print("woodstock list=",woodstock)
	#this is to get the first case of each section
	#print('======= ***** ====rule the earth ==== creates starbucks list === *******  =====')
	#print("==here we can see what the machine sees=====---***")
	#print(switchcasetester)
	mycounter =0
	second_word=''
	theline=''
	#print("the input to figure out the first case in each list inputlist list =",line_numbers_of_first_cases)
	## go thru digital list of the case locations
	## it will be the x position that's easy enough
	bestbuy1 =''
	bestbuy2 = ''
	
	
	test1 =''
	test2 =''
	plumtree=''
	total_word_count=''
	#print("inside of function rule_the_earth()")
	#print("palmtrees at this point has in it line 6693 ",palmtrees)
	#palmtrees.append('starter')
	#####################################
	## new addition to reset palmtrees list april 27th 2021 6:30 pm
	reset_list_to_just_starter(palmtrees) #clears out list if previously used resets it
	#print("palmtrees should only have starter in it at this location")
	palmtrees.append('starter') #which would be in slot 0
	#print("palmtrees=",palmtrees)
	#breakpoint()
	##for case sets I just go thru till case not in line and fill a new list
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		if mycounter in line_numbers_of_first_cases:
			#breakpoint()#print(line)
			#felix is the line split into a string
			felix= line.split()
			#print("NUMBER OF WORDS IN THIS CASE LINE")
			#print("number of words in this line is ",len(felix))
			
			#print("inside rule_the_earth line with case")
			#print("felix=",felix)

			if "default" in line:
				#print(line)
				second_word = line.split()[0]
				#########experimentaionl april 29th 
				#print("this is new on april 29th, 2021")
				#whatcount = len(second_word)
				#if 'case' in second_word:
				#	print("true case in this line")
				#	print("the number of words -1` for case",whatcount -1)
				#	whatcount = whatcount -1
				#else:
				#	print("false no case in this line")

				#print("the number of words -1` for case",whatcount)
				#this line will be no default
			else:
				#this ELSE MEANS DEFAULT NOT IN THIS LINE !!!!!!!
			################# code to get the 
				#print("I think that case must be in this line")
				#print("look at this next line carefully")
				#print('line =',line)
				second_word = line.split()[1] #right here it grabs just one word
				#that is the flaw
				##### addition here 
				#### first check if only one word
				#print("felix=",felix)
				#print("DEBUGGING ==6730==")
				#print("the line with default=",line)
				#print("felix[0]=",felix[0])
				del felix[0] #should delete first word case
				total_word_count = len(felix) #already deleted first word
				if total_word_count > 0:
					#print("assertion :: there is at least one word in the case")
					pass
					
				#secenario if only one word case like Tahoe
				#############################################
				## SCENARIO 1  IF ONLY ONE WORD FOR THE CASE
				# THIS DETERMINES IF THE CASE IS JUST ONE WORD
				#############################################
				if total_word_count == 1:
					#print("there is only one word in this case",felix)
					the_words = felix
					plumtree=' '.join(felix)
					#plumtree = felix  #it might be in a list actually 
					#print(plumtree)
					plumtree=plumtree[:-1] #this takes off the : on the end of the string
					#print("plumtree=", plumtree)
					#print("yeah plumtree is a stirng at this stage")
					#print("===== experimenntal plum tree to add to palmtrees === ")
					coolness = plumtree.replace("'","")
					plumtree = coolness
					#print(plumtree)
					
					#palmtrees=palmtrees[1:-1]
					palmtrees.append(plumtree)
					#print('AT THIS JUNCTURE LINE 6745 palmtrees=',palmtrees)
					#starbuckslist.append(plumtree)
				else:
					pass
				##############################
				#this senario if 2 or more words for the case like "alpine meadows
				## SCENARIO 2 IF 2 OR MORE WORDS IN THE CASE
				#THIS DETERMINES IF THE CASE IS AT LEAST 2 OR MORE WORDS
				###############################
				if total_word_count > 1:
					#print(total_word_count, " words in this  case")
					#print("felix =",felix)
				#========here is the JOIN to convert the line as a list with case into a string ======
					plumtree=' '.join(felix)
					#print("== output of plum tree ==")
					#print(plumtree)
					if plumtree.endswith(":"):
						plumtree=plumtree[:-1]  #this should delete the colon of end
						alltheway = plumtree.replace("'","") #this elminates double quotes
						plumtree = alltheway
						#starbuckslist.append(plumtree)
						palmtrees.append(plumtree)
						#print("here at line 6767 palmtrees=",palmtrees)
					else:
						pass
					
				#print("plumtree=", plumtree)
				
				#print("the words for this case are",the_words)
				#print("the number of words for this case in the line are ",total_word_count)
				##===========
				#print(" ====== entering new section of coding here at Volvo ==== ")
				
				#print("=====")
				#print("=== coding at walmart saturday night ===")
				
				
				

#january 26yh, 2021 my initial design was
#this is where we will have the case words 
#my flaw was having it designed to only handle the second word, the word after case
#and that was limiting it but it will be modified correctly soon.

# case word:  but this breaks if more than one word like "alpine meadows"
# I need to add my code adjustment here 
			#======================  thursday surgery cleaning up the words 'words'
			#wild= second_word[1:-1]
			
			#wild = "'" + wild       #adding a ' to left side of word
			#darn = wild[1:-1]
			#wild = darn
			#second_word = wild
			#=======================
			#if second_word != "default": #this is new
			#	starbuckslist.append(second_word)

			if mycounter == total:
				break
			else:
				mycounter += 1
		else:
			mycounter += 1
	#starbuckslist.pop()
	#starbuckslist.append('default')
	#print("starbuckslist=",starbuckslist)
	palmtrees.append('default')
	#print("palmtrees=",palmtrees)
	starbuckslist=[] #resets it
	reset_list_to_just_starter(starbuckslist)
	#print("what's in starbuckslist here",starbuckslist)
	#filling starbuckslist
	#####################################
	
	#print("===========================")
	for item in palmtrees:
		starbuckslist.append(item)
	#print("at line 6820 strarbuckslist =",starbuckslist)	
	#print("we now have... starbuckslist")
	#print(starbuckslist)
	#print("===========================")
	
	
	




	#print("testing this::::")
	#RIGHT here is where I need to remove " and : from each item in list
	counter = 0
	#print("new test here")
	mochalist.insert(0, "'starter'")
	for item in starbuckslist:
		#print(item)
		#if item != "starter":
		if item != "starter":
			item = item[:-1] #take out the :
			#===================================== experimental surgery here to have list

			#=====================================['apple','fish',etc]
			#print(item)
			mochalist.append(item)
		else:
			mochalist.append(item)
	mochalist.append("'default'")

	#print("the mochalist after adding starter and default to it ")
	#for item in mochalist:
	#	print(item)


	acounter=0
	#greenmilelist.append('starter')
	for item in mochalist:
		if item != "starter" and item != "default":
			item[1:-1]
			greenmilelist.append(item)



	#print("=======")

	str = "'apple'"
	#print(str)
	#print(str.replace('"', ''))





#sunrise();

#what this does is take the input of teh [concatstring list] with line numbers
#which has the first case line number for each section
#I need the case number list name to feed it
















#starbuckslist=[]
#starbuckslist.append("starter");
################################################################
def this_needs_to_work_badly():   
#this fills the starbuckslist which is used in p51 for fallthru(casenmae)

#################################################################
	#print("=========this_needs_to_work_badly() =============")
	#print("=========this_needs_to_work_badly() =============")
	#print("=========this_needs_to_work_badly() =============")
	mytrace('this_needs_to_work_badly')
	#print('===============this needs to work badly called =======to get first case name ==')
	#print("============= THIS NEEDS TO WORK BADLY() called =============== ")
	#print('this gets the first case name (designed as one word initially')
	#print("but I need to modify it to take more than one word so I will need to count")
	#print("how many words are in the *first case* so it's flexible and smart")
	#new_add_to_front(x,listname)
	mycounter = 0
	#print("starting out we have in starbuckslist",starbuckslist)
	#print('case section line number list =',concatstring)
	#print("what is in concatstring?") #I think it's the first case line number in each section
	#print(concatstring)
	
	
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		#print(line)
		if mycounter in concatstring: #so it's looping thru switchase and line number in concatstring list
			#print("!!!!!!!======!!!!!!!!!!line=")
			#print("dam line?",line)
			#print("underneath line=====================")
			firstline = line.split() #we refer to the line as firstline a variable
			#print(firstline)
			### this is where it was grabbing the one word after case
			### which wasn't able to grab more than one word by design
			
			#genius = line.split() #new  [0] was at end of it  ((this does the line split for each line))
			#print("genius[1]=",genius[1])    #gets word of that case name
			#print("the design is only getting one word")
			#print("genius=",genius)
			#print("genius this is in the first case line above")
			################# this is the problem it's only grabbing the first word
			#################
			#################
			#baby = genius[1] # it's only grabbing one word after case (by design here)
			#print("baby= genius[1]",baby)
			# if "case" in line: #see if this puppy works
			#remove the colon from the end
			#use a replace
			#firstline = line.split()
			#this makes a list called firstline
			#this gets the number of words in the line
			length_list = len(firstline)
			#now subtract first word 'case' 
			del firstline[0] #deletes the first word which is case
			length_list = len(firstline) #we thn print the number of words in this case
			#print("the number of words in this case is",length_list)
			#['case', "'alpine", "meadows':"]
			#print("line 1538")
			#print(firstline)
			#print("the length of this case name in words =",length_list)
			#while True:
			#remember that we have wiped away(erased) the case word it's gone
			if length_list == 1:
				answer = firstline[0]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                 
			if length_list == 2:
				answer= firstline[0] + " " + firstline[1]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 3:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 4:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 5:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 6:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4] + " " + firstline[5]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 7:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 8:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 9:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]  + " " + firstline[8]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 10:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7] + " " + firstline[8] + " " + firstline[9]
				answer = answer[:-1]
				#print(answer)
				baby = answer
				drive_thru.append(baby)
                
			
			
			
			####==============
			new_add_to_front(baby,starbuckslist)  ## actually adds to tail of starbuckslist
			#test
			#print("new add to front (baby,stabuckslist)")
			#print("baby=",baby)
			#print("starbuckslist=",starbuckslist)
			mycounter += 1 #n
		else:
			mycounter += 1
			
	#print("resulting starbuckslist=",starbuckslist)


######=============================================================















#this_needs_to_work_badly();[2, 7, 17, 24, 34]
#theinputlist =[2,7,17,24,34]  #5 which is case_sections + 1 (default)
case_sections = 0
total = 5
#==========================
#I will have to dynamically initialize these


mainlist=[]
#diamonds=[[2,7],[7,19],[19,26],[26,36]]  what I am aiming to make
#these are lines of the first case line numbers and then the default line number


#theinputlist= [2, 7, 17, 24, 34]  #last one is default which is really a case


length_of_input_list = len(line_numbers_of_first_cases)   #question does this work because it's an even number
#output
mainlist= [] # [[2, 7], [7, 19], [19, 26], [26, 36]]



find_default=''
lastbrace=''

list_trex=[]
listcandy=[]
defaultlist=[]  #here defaultlist is declared as empty

#uses input_list[2,7,19,26,36]
# THIS IS NEW FOR SUNDAY AUGUST 23, 2020 modified november 16th
# CONVERT TO TWIN LIST
number_of_case_sections=0
###################################
def convert_to_twin_list():  #uses list called line_numbers_of_first_cases
###################################
    mytrace("convert_to_twin_list")
    #print("=====line numbers of first cases list====")
    #print(line_numbers_of_first_cases)
    #so the length of line_numbers_of_first_cases tells us how many case sections
    #print("=9009=0=09=0=0=00=000099999=9=9=9=9=99=9=9=9=")
    #print("the number of case sections =", len(line_numbers_of_first_cases))

    #####
    ## create case lists
    #print("called create case lists")
    #create_case_lists()
    #print("them out to see them now")
    #show_case_lists()
    ##3===================
    global woodstock
    #print("woodstock in twin list=",woodstock)
    # added april 27th,2021 at 6:35 pm ===================
    
    #sniffer to see what is in digitalcandy here 
    #print("digitalcandy=",digitalcandy)
    #print('testing what is in digitalcandy line 7128')
    if len(digitalcandy) == 0:
    	print('')#'digitalcandy is empty')
    else:
    	print('')#"digitalcandy length =",len(digitalcandy))


    #this clears out digitalcandy (hopefully)
    # if digitalcandy has something in it then clear it
    if len(digitalcandy) > 0:
    	reset_list_to_just_starter(digitalcandy) #this makes it read ['starter']
    else:
    	pass
    #================
    #breakpoint()
    #print("starting out this is what is inside of list digitalcandy")
    #print("this is a moment before converting it into a twin list")
    #print("before appending to digitalcandy I wasnt verifying if it was empty")
   # print('the length of digitalcandy =',len(digitalcandy))
    #print(digitalcandy)
    ###############
    #digitalcandy.pop() #takes off first item of starterj this makes it empty
    #========================
    #global candy
    #candy=''
    #candy=[]
    #breakpoint()
    #input_list -= 1 #true cases last number is default
    ##################
    #print("inside of convert_to_twin_list")
    #print("line_numbers_of_first_cases",line_numbers_of_first_cases)
    list_trex=[] #this should reset it
    #print("list_trex=",list_trex)
    alpha = 0; beta = 1; counter = 0  #down below it was: length_of_input_list
    while counter < len(line_numbers_of_first_cases) -1:
        eval("list_trex.append(line_numbers_of_first_cases[alpha])")
        eval("list_trex.append(line_numbers_of_first_cases[beta])")
        eval("digitalcandy.append(list_trex)")
        eval("candy.append(list_trex)")
        alpha += 1; beta += 1; counter += 1
        list_trex=[] #resets list to reuse next loop
    #print('digitalcandy =',digitalcandy)
	#digitalcandy.append(defaultlist)
###=============================================




## what this does is delete the existing last sublist from digitalcandy
## and then it replaces it with a new list appended that has the default line number and
## curly brace line number (can alternatively be the last line of string) both equal length





#==============
# this looks like good logic to check between default and closing brace/last line
# determined last line number also eventually
# december 7th, this is dependent on default word existing
# the point of this code section is to VERIFY that there IS a BREAK after default
# and if there isn't a break add one
#=========
#
#===============
#defaultlist=[]
'''
mycounter = 0
check_for_default_break = "false"
x = defaultlist[0] #dfault word
y = defaultlist[1] #closing brace
for line in switchcasetester.splitlines():
	if mycounter > x and mycounter < y \
		and "break"  in line :
		check_for_default_break="true"
		break
		#mycounter += 1 #see if this is necessary here or not
	else:
		mycounter += 1
		continue
'''
###====================
####======== find_last_break_in_string  ========= 
##in switchcasetester input switch
listofbreaks=[]
def find_last_break_in_string():
	mytrace('find_last_break')
	counter=0
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			counter +=1
		else:
			counter += 1
			continue
	baby = listofbreaks[-1] #the last one
	return baby #which is a string

##############################
##  change_to_string()   -- fancy replace to switchcasetester
##############################
def change_to_string(x,y):
	mytrace('change_to_string()')
	#print('change_to_string()',x,y)
	global switchcasetester
	peach='';peach=switchcasetester.replace(x, y)
	switchcasetester=''; switchcasetester = peach



##### friday, march 26th, 2021
##### convert case line to lowercase that's what matters for matching
def convert_case_line_to_lowercase():
	mytrace('convert_case_line_to_lowercase()')
	#print('convert case line to lowercase')
	counter=0
	global switchcasetester
	for line in switchcasetester.splitlines():
		if 'case' in line:
			#this should make whole line lowercase
			change_to_string(line,line.lower())
			counter +=1
		else:
			counter += 1
			continue
	#print("after lowering words in case line we have")
	#print(switchcasetester)




#=========================
##########################################
def special_addition_to_digital_candy():
##########################################
	mytrace("special_addition_to_digital_candy")
	#global candy
	candy.pop() #treated as a list
	digitalcandy.pop() #delete last item sublist
	#print("digital candy after pop =",digitalcandy)

	#this gets the line number of the word default
	find_default = get_default_location()  #gets line number of default

	#this gets the line number of the closing brace (identical to last line of docstring)
	last_brace   = get_closing_brace()  #gets the line number of closing curly brace
	thelastbreak = find_last_break_in_string()# put it here
	mystring = str(get_closing_brace()) #puts closing brace line number in mystring
	defaultlist.append(find_default)  #defaultlist[0] #default line number
	defaultlist.append(int(mystring)) #defaultlist[2]
	
	#print("defaultlist=",defaultlist)
	#print("digitalcandy at this point",digitalcandy)
	#so this means that digital candy should already exist and be populated
	#don't want to corruptthis it is only expecting two values not three
	digitalcandy.append(defaultlist) #these two are the parameters to look between
	#print("defaultlist=",defaultlist)
	#print("line 7317")
	#print("candy",candy)
	candy.append(defaultlist)
	#print("now candy shows",candy)
	#print("at this point digital candy shows",digitalcandy)
	
	#look_for_break_after_default(defaultlist)
	#this is new code to determine if missing break in default input section
	three_in_row=[]
	three_in_row.append(find_default)  #defaultlist[0] #default line number
	three_in_row.append(thelastbreak)  #defaultlist[1] #break line number (if here)
	three_in_row.append(int(mystring))
	a = find_default
	b = thelastbreak
	c = int(mystring)
	#print("testing here before doing comparison")
	#print("a,b,c",a,b,c)
	#I might need to call this first since it's a strange bug if a missing break
	#remember if there is no break then add it with replace
	####################
	if b > a:
		#print("==== testing if break AFTER default")
		#print("there is a break in default") #in the default case
	#else:
		#print("there is a MISSING break in default case") #beneath default
		#print('there is NOT a break in default need to add one')
		#again this is adding a break in default to javascript switch case
		#because of an obscure bug caused by missing break in default
		#print("this is before adding break to default")
		#print(switchcasetester)
		#global switchcasetester
		orange=''
		global switchcasetester  #just added this may 31st, 2021 
		orange=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester='' #this nukes it resets it
		switchcasetester = orange
		#print("after adding break to default")
		#print(switchcasetester)
		return switchcasetester

#working on this December 17th new functions
'''
found_break_in_default=[]
	#called after special addition to digital candy
def look_for_break_after_default(input):
	smartcounter=0
	x = input[0]
	y = input[1]
	print("testing if it received the input values from js switch ")
	print("x=",x," ","y =",y) #between default and last line of string
	acounter =0
    for line in switchcasetester.splitlines():
        if acounter > x and acounter < y:
       		if "break" in line:
               # print("we found a break",smartcounter)
                found_break_in_default.append("true")
                break #if it's in there bail out no further action needed
            else:
                found_break_in_default.append("false")
            if "true" not in found_break_in_default: #this is a growing list it's making
            	print("need to add a break")
            else:
            	print("true is in it so don't need to add break already there")
		#   print(firstline[0])
        acounter += 1;
#==============================================================
def add_break_to_bottom_of_default(): #I got this working November 26th, 2020
	#print("=====convert_default_case called===") #this needs to be called first definitely
	mytrace('convert_default_case')
	#input
	global switchcasetester
	#print("this is the original input on switchcastester")
	#print(switchcasetester)
	newton=switchcasetester.replace("default:","case 'default':")
	switchcasetester=''
	switchcasetester = newton
	make_list_of_first_cases()
	print(switchcasetester)
	return switchcasetester
'''
##### stage_four has faucet_value() in it which checks if switch is case numbers
##### and if so then converts the numbers to strings





#############################################################################
def stage_four():
	#print(switchcasetester) 
	#print("===== testingwhat it sees in stage four() ======")
	mytrace('stage_four()')
	#print('stage four')
	####<<====== added March 15th,2021 converts numbers to strings if numbers
	magictimenow()
	convert_to_twin_list()
	special_addition_to_digital_candy() #=======added nov 25th, 2020
	rule_the_earth()


'''
starbuckslist is just the first case name of each case section
in drive_thru list I put EACH case which is wrong.
'''




#================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0

drive_thru=[]
drive_thru.append("starter")
#this is a super important function I think I wrote it at the beach a few days ago

### modfiied tuesday january 26th, 2021 to put a multi word like "alpine meadows" into fallthru('alpine meadows') currently only takes in one word
###
def testing_this_to_get_word():
	mytrace('testing_this_to_get_word')
	#print("======def ======testing this to get word() ==================")
	#print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")
	#print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")
	#print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")

	smartcounter=0
	#this looks for "case" in the switch case string
	for line in switchcasetester.splitlines(): #switch case in JS
		if "case" in line: #see if this puppy works
			#remove the colon from the end
			#use a replace
			firstline = line.split()
			#this makes a list called firstline
			length_list = len(firstline)
			#now subtract first word 'case' 
			del firstline[0]
			length_list = len(firstline)
			#print("the number of words in this case is",length_list)
			#['case', "'alpine", "meadows':"]
			#print("line 1441")
			#print(firstline)
			#print("the length of this case name in words =",length_list)
			#while True:
			
			if length_list == 1:
				answer = firstline[0]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
			 
			if length_list == 2:
				answer= firstline[0] + " " + firstline[1]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 3:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 4:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 5:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 6:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4] + " " + firstline[5]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 7:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 8:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 9:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]  + " " + firstline[8]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			if length_list == 10:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7] + " " + firstline[8] + " " + firstline[9]
				answer = answer[:-1]
				#print(answer)
				drive_thru.append(answer)
                
			#print(firstline[0])
			#print("now try this",firstline[length_list])
			smartcounter += 1;
		else:
			smartcounter +=1;
    
	#print("================== drive thru list of case names ")
	#print("the list of case names no matter how many words is here in list drive_thru")
	#print("drive_thru list contents now are ",drive_thru)
	#print("")
	#print("now we will loop thru the drive_thru list")
	#LIST OF CASE NAMES
	#print("==========================")
	#print("drive_thru=",drive_thru)
	#print("===========================")
	count=0
	for item in drive_thru:
		#print(item,count)
		count += 1
        
	#here we get the location of the "default"
	smartcounter=0
	for line in switchcasetester.splitlines(): #switch case in JS
		if "default" in line:
			firstline = line.split()
			location_of_default = smartcounter
			break
			#smartcounter += 1;
		else:
			smartcounter +=1;

########   end of this never ending function ##########

#testing_this_to_get_word()  #==================this should call it now

def stage_five():
    #print('stage five')
    testing_this_to_get_word()




    ###########################################################
    #these are the line number positions of first case for each section [2, 7, 19,26]
    #this looks in one section at a time for a break and fallthru
#diamonds =[]
    #this is all just raw code not even in a function
case1findbreak=[]
case1findfallthru=[]



def does_this_run():
    mytrace("does_this_run")
    c = 1    #current case numbr section
    d = c + 1

    x = clever[0]
    y = clever[1]
             #this loops by default through the entire string
             #for line in splitline().switch:

     #=======================================================
     #this is looking between x and y which are in diamonds
     #========================================================

    counter =0
    case1 =[] #case number list to add fallthru
   
    #print("testing getting the dam range to work")
    #print("looking for BREAK in this case section")
    smartcounter=0
    #look for BREAK in range of lines
    ##================================================
    ## LOOP LOOKING FOR BREAK IN CASE SECTION CODE
    ##================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to 
            #firstline = line.split()
            #print(line)

            if "break" in line:
               # print("we found a break",smartcounter)
                case1findbreak.append("true")
            else:
                case1findbreak.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;


        #look for FALLTHRU in range of lines
    #print("starting 2nd loop now looking for FALLTHRU")
        #=========================
    smartcounter=0 #reset at zero
    ##=========================================================
    ## LOOP LOOKING FOR FALLTHRU IN CHUNK OF CODE INSIDE OF A CASE SECTION
    ##===========================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "fallthru" in line:  #what about fallthrough also to test for
                #print("we found a fallthru",smartcounter)
                case1findfallthru.append("true")
            else:
                case1findfallthru.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;



   #this is all so clever
   # looks inside of lists for breaks, fallthrus
    if "true" in case1findbreak:
        #print('break found')
        royallist.append('break');

    if "true" in case1findfallthru:
        #print('fallthru found')
        royallist.append('fallthru')

    if "true" not in case1findbreak and "true" not in case1findfallthru:
        #print("need to add a fallthru")
        royallist.append('fallthru')

    #print("royallist=",royallist)







#//=========== iron curtain============================

 ##===============================================================
  ####=================== American River Methods ==================
  ##===============================================================









buildlist=[]
def grab_body_of_code_inside_case_sections():
    mytrace("grab_body_of_code_inside_case_sections")
    #print("grab body of code called== @@@@")
    smartcounter=0  #reset at zero

    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)

        if smartcounter > x and smartcounter < y:  #so get what's inbeteen
       #this should only print the body of this one case section
            if "case" not in line and "break" not in line and "fallthru" not in line:
                #print(line)
                buildlist.append(line,smartcounter);
                smartcounter += 1;
                #do I need continue?








#august 27 thurday coding test       this will be the sets of cases for each case section
caseset=[]
def create_case_name_lists(x,y):
    #print("==$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==")
    #print("================this is line 1615===CREATE CASE NAME LISTS=====================")
    #print("def create_case_name_lists:")
    #print("working on fix to solve bug if user uses more than one word for a case")
    #print("such as alpine meadows whereas right now its geared for one word cases")
    
    mytrace('create_case_name_lists')
    #print("=================create case name lists called == @@@@")

    smartcounter=0 #reset at zero
    genius = ''
     #need list of first cases that will work for input
    #Thursday coding to save this day from a disaster of nothing working
    ##===================================================================
    ## LOOP LOOKING  CASE SECTION APPEND LINES FROM BODY AFTER CASES UNTIL NEXT FIRST CASE
    ##=======================================================================
    #print("here we get the words in each case section=====------")
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter < y:  #so get what's inbeteen
        #this should just look
            if "case"  in line:
                #print("did it take off front of line?")
                #print(line.split(' ',1)[1])
                #print(line,smartcounter)
                #print("=================================")
                genius =line.split()
                #print("genius =",genius)
                #print("======= len(genius) ==============")
               # print("WE ARE HERE==>>>>")
               # print('number of words in the line case = len(genius) ',len(genius))
                
                #print("number of words in this line =",len(genius))
                #print("it's current state is only grab the second word which is position [1] by default")
                ap=''
                #testing with more than one word the defualt was the first one
               #================  jan 3, 2021 code fix experimentiong case alpine meadows
                if len(genius) == 2:
                    #print('teh default was 1 word case and one word')
                    caseset.append(genius[1])
                    #print(caseset)
                    
                if len(genius) == 3:
                    #print('teh default was 3 words case and two words')
                    ap =genius[1] + genius[2]
                    caseset.append(ap)
                    #print(caseset)
                    
                if len(genius) == 4:
                    #print('teh default was 4 word case and 3 words')
                    ap =genius[1] + genius[2] + genius[3]
                    caseset.append(ap)
                    #print(caseset)
                    
                if len(genius) > 4:
                    #print("more than four words in this line detected")
                    #print("just do the default for now will fix later")
                    caseset.append(genius[1])
                    #print(caseset)
                
                #print("it looks like I'm just grabbing the first word of a case which I initially tested it with")
                #print('line 1632')
                #print(caseset)
                #buildlist.append(line);
                smartcounter += 1;

    #print("caseset list for one case section=",caseset);
    wilsonball=[]
    wilsonball.append('starter')
    wilsonball.append(caseset)
    #print("******** === wilsonball=",wilsonball)










#this actually looks for breaks, missing beaks, and fallthrus
####=====================
##case_tail_list_maker() finds breaks, missing break detection, fallthrus
##========================
snowman=[]
homer=[]
gti=[]
gti.append("starter")
funny=''
seal=[]
homer.append('starter')
solution=''
snowman.append('starter')
wilecoyote=[]  #I was clearing it out here good thing I noticed it
casecaptured=''

reset_list_to_just_starter(wilecoyote)
#print("wilecoyote list",wilecoyote)
#wilecoyote.pop()

mrcase=''
def case_tail_list_maker(x,y):  #two vars x and y are case locations from digitalcandy
    mytrace('case_trail_list_maker')
    #print("=######	C A S E    T A I L   M A K E R  searches for breaks and fallthrus  ")
    #print("digitalcandy=",digitalcandy)
    #print("length of digitcandy=",len(digitalcandy))
   
    smartcounter=0
    #this looks for "case" in the switch case string
    for line in switchcasetester.splitlines(): #switch case in JS
        if "case" in line: #see if this puppy works
            firstline = line.split()
           
            smartcounter += 1;
        else:
            smartcounter +=1;

    #here we get the location of the "default"
    smartcounter=0
    for line in switchcasetester.splitlines(): #switch case in JS
        if "default" in line: #see if this puppy works
            firstline = line.split()
            location_of_default = smartcounter
            break
            #smartcounter += 1;
        else:
            smartcounter +=1;



   #not sure if I am using c and d or not or if I switched to x, y instead
    c = 1    #current case numbr section
    d = c + 1
    #print("x",x,"y",y);
    counter =0
    case1 =[] #case number list to add fallthru
    case1findbreak=[]
    case1findfallthru=[]

    smartcounter=0
    ram=''
    #look for BREAK in range of lines
    ##================================================
    ## LOOP LOOKING FOR BREAK IN CASE SECTION CODE
    ##================================================
    #homer=[] #this is to keep track of whether break or fallthru as backup checker
   ##############################################
   
    ##############################################
    ##############################################
   # print("HUGE TEST to make it work Tuesday feb 22nd")
    #this goes through the whole switch case 
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        #print("======= TESTING THIS  ========")
        #print("x =",x,"and y=",y)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            ####################################
            if smartcounter == x: #case line
                #print("GET CASE NAME")
                mrcase =get_case_name(line);  #calling method here 
               # print("just here got the_section",mrcase)
               # print(mrcase)
                
                mrcase =mrcase.lstrip() 
                mrcase =mrcase.rstrip()
                #print(mrcase)
            #end if
            
            
            #firstline = line.split()
            #print("I need to make sure it searches through the lines")
            #print(line)
            global funny
            funny += line
            #### I have simpified it to if break then break, otherwise fallthru
            if "break" in line:
                #print("===== gold ======")
                #print("we found a break line number =",x,y,smartcounter)
                
                wilecoyote.append(mrcase) # first case number in digitalcandy
                #I will put the case name instead of x
                
                homer.append(smartcounter)
                seal.append(smartcounter)
                #if i detect a break on a line in a case section that's true
                
                #smartass.append("break")
                #homer.append('break')
                case1findbreak.append("true")
            else:  # I just modified this one and using homer
                case1findbreak.append("false")  #meaning add invisible fallthru
                #print("no break found in this section") #and no fallthru
                #print("no break found =",x,y,0) #using 0 for no break found
                #homer.append('fallthru')
                #break not in line it's fallthru
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;
    #########################
  
        
        
     #we ARE STARTING A SECOND LOOP HERE -------------------
        #look for FALLTHRU in range of lines
    #print("starting 2nd loop now looking for FALLTHRU")
        #=========================
        #print("this was the old design the newone will be different")
        if "break" in funny:
            gti.append("break")
        else:
            gti.append("fallthru")
        
        
    smartcounter=0 #reset at zero
    ##=====================================================================
    ## LOOP LOOKING FOR FALLTHRU IN CHUNK OF CODE INSIDE OF A CASE SECTION
    ##======================================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            #firstline = line.split()
            #print(line)

            if "fallthru" or "fallthrough" in line: #just added fallthrough here
                #print("we found a fallthru",smartcounter)
                case1findfallthru.append("true")
              
            else:
                case1findfallthru.append("false")
         #   print(firstline[0])
        smartcounter += 1;

        #are you serious is this it? this fixed the bug
        if smartcounter > y:
            break;
    #I think that this is the end of the for loop here
    #print("=================================")
    #print("gti  list has",gti)
    #print("=================================")
    #print("========WILECOYOTE LIST=========")
    #print(wilecoyote)

   #this is all so clever
   # looks inside of lists for breaks, fallthrus
    if "true" in case1findbreak:
        #print('break found in this case section ')
        royallist.append('break'); #this adds break to royallist
       # homer.append("break")


# here it's appending the fallthru('casename')
    if "true" in case1findfallthru:
        #print('** = fallthru found in case section')
        smart = len(royallist)  #new code  a number
        smart += 1
        #before I add this one         so I am putting a number here which is used
        fall = "fallthru" + str(smart)  #to call the correct word in starbuckslist
        #print("we have",starbuckslist[smart]," added to fallthru")
        #I will need to do this
        #  fall = "fallthru('" + starbuckslist[smart] + "'")
        royallist.append(fall)
        #homer.append(fall)
        
  # here it test if "break" not in case section and "fallthru" not in case section
    wolf =''
    if "true" not in case1findbreak and "true" not in case1findfallthru:
       # print("** = need to add a fallthru in this section with no break and no fallthru")
        sosmart = len(royallist)
        sosmart += 1   #number below so it makes fallthru4 in example
        fall = "fallthru" + str(sosmart) #+ ")"  #just added this  thursday night
        #print("we have",starbuckslist[sosmart], "added to fallthru")
        #print("smart is length of royal list before adding fallthru",sosmart)
        #print just eliminted "'" +  and  "'"
        wolf = "fallthru(" +   str(sosmart)  + ")"  #this makes fallthru(4) which I need
        #because I can convert the number to a word in new list
        #print("wolf=",wolf)  #so this works
        royallist.append(fall)
       # homer.append(fall)
   
    #print("let us see what the size and end of royallist is",royallist)
    #print("royallist lenght=",len(royallist))
    royallist.append('break'); #this is for the default case which must be a break
    #print("royallist final =",royallist)
    #print("lenght of royallist final =",len(royallist))
    snowman.append("break")
    #print("gti coming thru",gti)
    #print("this is our winner=================")
    #print("seal=",seal)
    #print("the list of first case number in digitalcandy with a break in it")
    #print("wilecoyote=",wilecoyote)



##########################################################################
##           dividide and conquor    thrusday, feb 25th, 2021 nearly 1pm
##########################################################################






#####################################
### crashing waves at beach ()   ####
#####################################
penguin=[]  #defining a new list here 
def crashing_waves_at_beach():
	mytrace('crashing_waves_at_beach()')
	#print("Crashing Waves At Beach function called")
	######## there is a lot going on here
	'''
	loop thru wilecoyote of cases with breaks and
	   get index location of those cases in palmtrees list
	   put the index number into roadrunner list
	   
	 
	loop thru digitalcandy to make list of same size and fill british list with all 'fallthru'
	
	loop thru roadrunner list with index number
	and replace index number in british with "break"
	
	'''
	#print("this is what is in wilecoyote",wilecoyote)
	#print("I got this working the other day at motel 6 on Tuesday night")
	################################################
	#print('in crashing waves at beach we have wilecoyote line 7975',wilecoyote)
	#print("palmtrees at line 7977 we have ",palmtrees)
	###=================#######@@@@@@@@@@@@@@@@@@@@@@@
	print("debugging on june 16th, 2021")
	print("palmtrees to see whats in this list")
	##########################
	print("palmtrees==============")
	print(palmtrees)
	print("wilecoyote==============")
	print(wilecoyote)
	## this gets the location of the case in wilecoyote inside of palmtrees list
	for item in wilecoyote: #goes through list of case sections with breaks
		print("debugging in wilecoyote")
		print(item)
		####@@@++++++++++__+++========================
		toad = get_location_of_case("palmtrees",str(item))
		
		#print("we have this in toad=",toad)

		roadrunner.append(toad) #this returns a number the index position
	#print("ROADRUNNER list contains numbers of index locations of cases in palmtrees",roadrunner)
#################################################
	# make a new list based on digitalcandy
	#print("in digitalcandy at line 7988 we have",digitalcandy)
	thecounter=0
	for item in range(0,len(digitalcandy)): #using this for length of case sections sequence
		#filling list with fallthrus
		#print("what I am doing here is adding the Next case number so it's correct")
		  #I had to move the counter before it to get it working correctly
		british.append("fallthru" + str(thecounter + 1)) # current case number + 1 for next case
		thecounter += 1
	#this adds break after the loop finishes	
	british.append("break") #adds one more to list since default is extra case
	
	#print("========== british list ======")
	#print("british filler list =",british)
	#british[0] = "starter" #this is position 0 filler
	#british[-1] = "break" #last one must be break for default case
	#print("========== british list ======")
	#print("so here the british list should have breaks and fallthrus(with number to next case")
	
	#print("british list =",british)
	##################################################
	#this is walking thru the british list and replacing fallthru with break where there was a break in a case
	#the bug is here 
	#It's initially filled with all faltlhrus, so replace with break
	#Next I need to replace with fallthru with number 

	#print("==BIG LOOP TEST TO INSERT BREAK INTO FALLTHRU LIST CALLED BRITISH==")
	#print("what this does is replace fallthru with a break based on location of a break")
	#print("and this is in the british list")
	#print("this is using digitalcandy for the proper length of the new list roadrunner")
	############ this is where BREAK  is inserted into the list with replace method 
	mycounter=0
	#print("in crashing_waves_at_beach() around line 7942")
	#print("digitalcandy",digitalcandy)
	#print("roadrunner",roadrunner)
	
	#to debug
	#print("digitalcandy at line 8024",digitalcandy)
	#print("roadrunner at line 8025,roadrunner")
	for item in range(0,len(digitalcandy)):  #adding a case to it default
		if mycounter in roadrunner: #if it finds first case line number in roadrunner
			#print("this is where it is inserting break into the list british")
			do_replace(int(item),"break")## do_replace(1, 'break')  list[index number]
			mycounter += 1
		else:
			mycounter += 1
			
	#print("============================")
	#print("british is ",british) #break and fallthru list
	#this changes the first position slot to starter

	#this assigns values to specific elements in the british list
	#british[0] = "starter"
	#this ensures that the last one is a break no matter what it's force fed in. 
	#british[-1] = "break" #makes sure last one is break which is absolutely must be. 
	#print("here is the finished british list before adding teh fallthru with case")
	#print("british now =",british)
	##############
	#print("british list at line 8024=",british)
	#############
	#do this first  assuming of course default (worry about adding defaeult laster
	#check if "break" in switchcasetester
	#if False then add it to bottom of default
	#if no break in switch case it won't parse - sooo funny 
	
	####==================================================
	#print("=== OFFICIAL BRITISH LIST ==== USING SMART BREAKS AND FALLTHRUS NUMBERED == ")
	#print(british)
	########################################################
	british[0]  = "starter"
	british[-1] = "break" #just to be sure 
	#print("####################E#######################")
	#print("February 25th, 2021 Beach Coding with seagulls flying just above the waves ")
	#print('totally NEW OCEAN BEACH CODE TO MAKE NEW FALLTHRU INTO LIST OCEANWAVES')
	#print("which will be put into cranberries replacing what's in cranberries ")
	#print("=================-------- waves at abeach -------+++++++++=================")
	#print("======================= waves at beach and seagulls flying over ice plants =====")
	print("british list line 8593=",british)
	#print("palmtrees list =",palmtrees)
	#penguin.append('starter')
	for item in british:
		penguin.append(item)
	
	#print('penguin at line 8066',penguin)

	#penguin.append('break')
	#print("penguin= ", penguin)
	#print("starting length of penguin=",len(penguin))
	
	
	### new coding here 
	#print('british list=',british)
	newcounter=0
	#print("in crashing_waves_at_beach()")
	#print("length of palmtrees at line 8081 =", len(palmtrees))
	#print("palmtrees =",palmtrees)
	#print("around line 8004")
	#exit() #see if this works

	#print("british at line 8085=",british)
	#print("line 8086 palmtrees=",palmtrees)

	for item in range(0,len(british)):  #should only look inside of items starting with f
		if british[item].startswith("fallthru"):
			#print('item =',item)
			#print("newcounter =",newcounter)
			getnumber= british[newcounter] #gets the fallthruX
			
			getnumber = getnumber[8:] #gets the number from cutting off front fallthru
			getnumber = getnumber.rstrip()
			getnumber = getnumber.lstrip()
			#print("getnumber=",getnumber)
			newnumber = int(getnumber)
			
			casename =palmtrees[newnumber] #has cases in sequence
			#print("casename=",casename)
			mrfallthru = "fallthru("  + "'" + casename + "'" +  ")"#
			#print("mrfallthru =",mrfallthru)
			#do_replace(int(getnumber),mrfallthru)
			smart_replace(newnumber-1,mrfallthru)## just added minus 1
			#print("########### building the penguin list ")
			#print(penguin)
			newcounter += 1
		else:
			newcounter += 1
	newcounter = 0		
			
	#print("00000000000000000000000000000000")
	#print("british=",british)
	penguin[-1] = "break"
	
	#### I can change the contents of british or makea  new list so as to not mess it up.
	oceanwaves =[]

###########################################################################









tail_list=[]
cranberries=[]
cranberries.append('starter')
british =[]  # list for faltlhru and breaks for each section to be managed
roadrunner=[]
######################################
##  f22_fighter_jet()
######################################
#this is called if numbers is true:
#this is not called because I found a way
# to send the numbers thru the string parser
# I don't think that this is called 

def f22_fighter_jet(): #makes critical cranberries list which is the taillist for switch cases
	return #this kills it
	

###################################################
 
  #this makes the cranberries list which is the tail list used on codegen page
#diamonds=[[2,7],[7,17],[17,24],[24,34]]
#this makes the cranberries list

##===========================
##      def p51_mustange()  ==  adds the number to  fallthru(3) like that
##===========================
def p51_mustang(): 
	mytrace('p51_mustang')
	counter = 0
	c = 1		#current case number section
	d = c + 1
	#print("** inside of p51 mustange [[ digitalcandy ]] =",digitalcandy)
	royallist =[] #resetting this Friday april 9th
	#maybe in digitalcandy
	#print("line_numbers_of_first_cases",line_numbers_of_first_cases)
	#print("digitalcandy in p51mustange=",digitalcandy)
	for item in digitalcandy:	#this is going through the diamonds list
		holder = digitalcandy[counter]
		x = holder[0]
		y = holder[1]
		##print("x",x,"y",y);
		case_tail_list_maker(x,y)   #here it is calling case_tail_list_maker
		counter += 1

	royallist.append('break');  #in default
	counter = 0
	#print("royallist at line 8223 =",royallist)


	#this goes thru the royallist with breaks and fallthrus(numbers)
	# starter 0  fallthru2 fallthru3 fallthru4  fallthru5 default
	#loops thru to royalist[item] then accesses the starbucklist[item to append
	# I can make fallthru('fish') and fallthru('default')  and have the formula working
	#I use numbering in royalist starter1(0) (position1 fallthru2)   (position2 fallthru3) etc
	#if they use big numbers I will put them inside of (number) and grab teh number startswith("(")
	#and endswith(")")
	#print("royallist =")
	#print(royallist)
	#for item in range(1,len(royallist)):
	for item in royallist:  #so royallist has starter break fallthru3 default in it 
		if "break" in item:
			cranberries.append("break")
		
		#print("this is where fallthru gears work line 2182")
		if "fallthru" in item:
			#### this grabs the number on the end of fallthru that is already there. 
			item=item.strip()
			#print("item=",item)
			item =item[-1]
			#print("after item[-1] we have item=",item)
			item = int(item)   #is this returning a number?
			## yea this is retrieving the number from the end of the word fallthru
			
			
			doggy =palmtrees[item] #just added -1   this is like fallthru('cherry')  #was starbucks
			#print("doggy",doggy)
			doggy[1:]  #deletes first item
			doggy[:-1] #deletes last item
			
			#this builds the fallthru(nextcase)

			#print("ohbaby which has fallthru from doggy starbuckslist[item]")
			ohbaby = "fallthru("  + "'" + doggy + "'" +  ")"#this is the number
			
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target
			
		
	
		
	#print(wilecoyote[0])
	#print(wilecoyote)
	#print("firstcaselist now in palmtrees")
	#print(palmtrees)
	
	oceanwaves=[] #this sets it at empty
	#print(" ====== JUMANJI ====")
	#print(" ..................J U M A N J I ......inside of P51 Mustang() function..........")
	#add method here
	crashing_waves_at_beach()
	print("tyring to fill  list oceanwaves with british list")
	#print("here I am filing the list oceanwaves with the british list")
	print("british list which goes into oceanwaves list")
	print(british)
	
	for item in british:
		oceanwaves.append(item)
	
	#print("OCEANWAVES LIST now ",oceanwaves)
	#print(oceanwaves)
#I will needto add this to royallist
	
			
			
	
	#print("THIS IS THE TAIL LIST CALLED CRANBERRIES")
	#print("cranberries=",cranberries)
	#print("penguin=",penguin)
	
	#tail_list = copy.deepcopy(cranberries)
	#print("see if this works == making the tail_list")
	#for item in cranberries:
	#	tail_list.append(item)


# I will need to change this here and just have p51mustang
def stage_six():
    p51_mustang() #so it only calls p51_mustang now
    #firstcase = valve[0]
    #if firstcase == True:  #which means numbers like case 4:
    #    f22_fighter_jet()
    #else:
    #    p51_mustang()




#The purpose of this method == flyingcloud == is to
#fill small lists with
#the respective case names
#get case names in each set and add to list





#=====================================
#========== flyingcloud ==============  Thursday morning coding
#=====================================
case1list=[]
case2list=[]
wilderness=''
wild=''
#diamonds=[[2,7],[7,17],[17,24],[24,34]]



#forcing it to see what happens november 21st
#caselist7=['default']


#we will know before hand how many caselists will be filled 4

#this makes the first case list called starbucks which is used throughout the program
##==========================
##   flying fish             this loops through the digitial candy list of first cases
##========================== which are the line numbers of each case
def flyingfish():
	#print('digitalcandy=',digitalcandy)
	ax = len(digitalcandy)
	#print("length of digitalcandy =",ax)
	mytrace('flyingfish')
	mytrace('flyingcloud')
	x =''
	y =''
	z ='' #just reset z to nothing
	thecounter=0
	thecounter=0
	# loops through diamonds list of case position to build the first case list
	# which is called starbucks
	z = thecounter #which is 0 by default above
	z += 1  #then it starts at 1
	#print('digitalcandy=',digitalcandy)
	global candy
	#print('candy=',candy)
	#print("digitalcandy at line 8418=",digitalcandy)
	for item in digitalcandy:
		x = item[0]
		y = item[1]
		#print("** look at x,y,z here **")
		#print("x",x,"y",y,"z",z)
		flyingcloud(x,y,z) #z starts at 1 and adds 1 to z with each loop
		z += 1
		thecounter += 1
	z = 0
	thecounter=0
	nightowl()   #fills smartcasemanager





##==========================
##      flying cloud            
##==========================
#  this builds a list of the case names for each section
smartcasemanager=[]
smartcasemanager.append("['starter']")
def flyingcloud(x,y,z):
	#print("smartcasemanager=",smartcasemanager)
	words=''
	
	#print("flyingcloud called; this builds a list of the case names for each section")
	mytrace('flyingcloud')

	smartcounter=0
	#print("x,y",x,y)
	for line in switchcasetester.splitlines(): #switch case in JS
		#print("inside of loop values of x,y at top of for loop ",x,y)

		if smartcounter < x:
			smartcounter += 1
			continue

		#to stop going through string of code
		if smartcounter == y:
			break

		if "case" not in line:
				break

		if (smartcounter >= x and smartcounter < y) and ("case" in line):
			firstline = line.split()
			#print("length of firstline words =",len(firstline))
			words = len(firstline)  #this is the length of the first line
			
			#print("=========== line 2000 ===firstline====")
			#print("firstline=",firstline)
			if words == 2:
				wilderness = firstline[1] #this grabs the case name
				
			if words == 3:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]   
				
			if words == 4:  #if 3 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3] 
			
			if words == 5:  #if 4 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] 
				
			if words == 6:  #if 5 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5]
				
			if words == 7:  #if 6 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5] + ' ' + firstline[6]
				
			if words == 8:  #if 7 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5] + ' ' + firstline[6] + ' ' + firstline[7]
				
			if words == 9:  #if 8 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5] + ' ' + firstline[6] + ' ' + firstline[7] + ' ' + firstline[8]
				
			if words == 10:  #if 9 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5] + ' ' + firstline[6] + ' ' + firstline[7] + ' ' + firstline[8] + ' ' + firstline[9]
				
			if words == 11:  #if 10 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5] + ' ' + firstline[6] + ' ' + firstline[7] + ' ' + firstline[8] + ' ' + firstline[9] + ' ' + firstline[10]
				
										
				
				
			#print(" wilderness has in it", wilderness)
			#print("=====firstline[1] ====== line 2009 =======")
			#print("wilderness=", wilderness)
			wild= wilderness[1:-1]
			#print("wild=",wild)
			wild = "'" + wild  #adding a ' to left side of word
			darn = wild[1:-1]
			wild = darn
			#print("==TARGET TEST==")
			#print("===== what is in wild?",wild)
			#wild = wild[1:] #cut off the word case jeeze
			############# feb 6, 2021
			#print("wild now is",wild)  this reduces it to a string 'word'
			# will need to use the case or counter number and
			# use eval to just do this with one if
			eval("caselist" + str(z) + ".append(wild)")

		else:
			if "case" not in line:
				break

#############################################
einstein=[] #resets einstein to empty
	#========================================
#this fills up smartcasemanager list




#============================
#      nightowl()
#============================
def nightowl():
	#print("===== nightowl() called ======")
	mytrace('nightowl()')


	i = 1
	#this filles the list smartcasmanager skipping 0 position
	#while i <= len(digitalcandy):  #use range here
	for item in range(1,len(digitalcandy)):
		eval("smartcasemanager.append(" + "caselist" + str(i)+ ")")
		i += 1

	i+=1
	eval("smartcasemanager.append(" + "caselist" + str(i)+ ")")

	#this copies smartcasemanager and puts it into list einstein
	for item in smartcasemanager:
		einstein.append(item)



#this prints out the smartcasemanager list to verify that it worked and has the sublists

#=================================
def goodseason():
	mytrace('goodseason')




def stage_seven():
    #print('stage seven')
    flyingfish()


wilson=''
mystring =''


#or am I using the current case number or next case number for fallthru
#so does it represent the current location and then we add 1 to it or does fallthru(#) have
#the next number position embedded in it already
#this will go through the list and convert the fallthru(#) into names making the gold tail list
#which is used to build the case sections
bronzelist =[]
#I think it will already have it in it calculated currecent case section number + 1

#============================
#      wildgame
#============================
def wildgame(y):   #this gets the number out of fallthru(5) and converts it to the casename
	mytrace("wildgame")

	mystring='fallthru(' + str(y) + ')'  #this gets the number from fallthru to use in starbuckslist to get case name
	#print('mystring=',mystring)

	wilson=int(''.join(filter(str.isdigit, mystring)))  

	#this extracts the number from fallthru(5) and gets the 5

	#print("the input number it sees in fallthru as input",wilson)
	newnumber = wilson + 1
	#print("newnumber=",newnumber)
	newnumber = int(newnumber)
	#print("the output fallthru number for next case name after adding 1 = ",newnumber)
	answer =starbuckslist[newnumber] #this gets teh string word out of the starbucks list of case names
	#answer should be a string which is the case name
	ohbaby = "fallthru('"  + answer  + "')"  #this is the number
	#print("we now have ",ohbaby)   #this should be "fallthru('casename') which is put at bottom of a case section
	ohbaby =ohbaby.strip() #this is beautiful
	#it looks like this:   fallthru('fish')
	return ohbaby   #first time I recall using return in python for anything










goldtaillist =[]
#I need to loop through this list and create the new list for final gold tail list
def autumn():  #this builds the break fallthru(nextcasename) list
	mytrace('autumn')
	counter =0

	for item in starbuckslist:
		print(item)
		#goes through list


		if item == "break":
			#print('break found')
			goldtaillist.append("break") #how come it doesn't append this
			counter += 1


		if  "fall" in item:
			result =wildgame(counter)  #it wants a number use the counter
			#print("wildgame() result=",result)
			goldtaillist.append(result)
			counter += 1
		else:
			counter += 1

		if item == "starter":
			goldtaillist.append("starter")
			counter += 1
			continue

		if item == "default":
			goldtaillist.append("default")
			counter += 1
			continue

	#print("goldtaillist =",goldtaillist)




#autumn()



crushit =[]


#thurday, september 10, 2020 truck stop insight
#=============== stars() =============================
#=========== this goes thru dummy list with just starter fallthru and break and default
#==========/=== and adds the numbers of teh fallthru locations into cru0list
#=======================================================

miraclelist=[]

####################
##    stars()
####################
def stars():
	mytrace('stars')
    #print('STARS test of loking for words in list')
	#print('look for break default starter fallthru')
	#print("listnow =",listnow)
	counter =0
	#print("starting looking in loop")

	for item in listnow:
		if "break" == item:
			#print('break')
			crushit.append("break")
			counter += 1

		if  item.startswith("f") == True:
			#print('fallthru found')
			crushit.append("fallthru('" + str(counter) + "')")
			counter += 1

		if item.startswith('d') == True:
			#print("default found")
			crushit.append("default")
			counter += 1

		if item.startswith('s') == True:
			#print("starter found")
			crushit.append("starter")
			counter += 1



	#====
	#starter is 0 but not a case
	#first case is position 1 (if fallthru(1)) it becomes fallthru(2) for conversion
	#so it is based on current position for the current case and then the NEXT case is +1
	#==========================================
	#input must be 1 or higher but less than the length-1 can't be starter (0) or default(length-1)
	wilson=''
	newnumber=''
	counter =0
	for item in cru0:
		if item.startswith("f") == True:  #fallthru or fallthrough
			#print("fallthru found")
			mystring=item
			#print('mystring=',mystring)
			wilson=int(''.join(filter(str.isdigit, mystring)))   #this extracts the number from a string
			newnumber = wilson + 1
			newnumber = int(newnumber)
			answer =starbuckslist[newnumber] #this gets teh string word out of the starbucks list of case names
			ohbaby = "fallthru('"  + answer  + "')"
			ohbaby =ohbaby.strip()
			miraclelist.append(ohbaby)
			counter += 1

		if item.startswith('d') == True:  #default is last case needs to have break
				#print("default fuound")
				miraclelist.append("break")
				counter += 1

		if item.startswith('s') == True:
				#print("starter found")
				miraclelist.append("starter")
				counter += 1

		if item.startswith('b') == True:
				#print('break')
				miraclelist.append("break")
				counter += 1








#======== adderrsmill==============================
case_main_body_list=[]
 #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code



#################### this is where the case section bodies are added to a list
#################### case_main_body_list



################################################
##  big_gears_filling_list_with_case_bodies()
################################################
def big_gears_filling_list_with_case_bodies():
	case_main_body_list.append('starter')  #moved this here 
	mytrace('big_gears_filling_list_with_case_bodies')
	#print("================big gears filling list with case bodies called==========")
	#breakpoint()

	counter=0
	#print("=====DIGITAL CANDY ======")
	#print("digitalcandy=",digitalcandy)
	for item in digitalcandy:  #=[[2,14],[14,26],[26,33],[33,3],[38,43],[43,47]]
		#print(item[0],item[1])
		
		counter += 1
		#print("counter=",counter)
		smarty(item[0],item[1])  #snowtime is called here
	#case_main_body_list.append('default')

import re  #for regular expressions
#this one
handy_list_of_tabs=[]
dual_slots=[]
crummy =[]
fiasco =[]
n_count_per_section=''
case_section_lines_of_code=[]

#new idea have line count based on first line of code in THIS section after if case
#and the first line is 1 and not 0 so it's human math thinking

def smarty(x,y):  #this grabs the body from one case section at a time
	mytrace('smarty')
	#print("in smarty what is in case_main_body_list",case_main_body_list)
	
	#print("smarty x y testing blank lines existence to delete them")
	global practicestring1
	practicestring1 = ""
	mycounter=0
	for line in switchcasetester.splitlines():
		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line  and "}" not in line \
		and "{" not in line:
		#this takes out the empty line by skipping it
			#print("line=",line)
			#added this sept 17 2020 to eliminate empty lines that do and mean nothing
			if len(line) == '\n': #this means that the line is empty
				
				mycounter += 1 #see if this is necessary here or not
				continue
			else:
				

					#by default each line will require 2 tabs in front of it
				line=line[1:] #takes off first tab off from front of line

				# ============== Glory =======================
				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
				#=============== Glory =======================

		mycounter += 1

	#this would be the string and nuke last line trailing \n which I know will be there
	practicestring1 = practicestring1.rstrip("\n")
	### and here the practice string is added (appended) to case_main_body_list
	#print("this is WHERE a line inside of a case section is added to case_main_body_list")
	case_main_body_list.append(practicestring1)  #the body case code is added here
	#print("case_main_body_list=",case_main_body_list)
	del practicestring1  #this nukes it
	practicestring1 =''  #here we nuke practicestring1 so I can reuse for each case section
	#print("=========")
	#print("list of tabs=",handy_list_of_tabs)
	#print("number of lines with code =",len(handy_list_of_tabs))
	#print("pairs tabs and line number ",fiasco)
	#print("number of lines in each section =", n_count_per_section)
	#case_section_lines_of_code.append(n_count_per_section)
	#print("=========")
	#print("==== attempting to print out cases section code from case_main_body_list")
	acounter=0
	for item in case_main_body_list:
		#print("==========")
		#print(item)
		acounter += 1
		#print("case=",acounter)
		#print(item)
	

def loop_thru_case_sections():
	#print("======== loop thru case sections =============")
	mytrace('loop_thru_case_sections')
	#print("loop thru cases sections which is a list")

###############################################################################
###############################################################################
#TUESDAY CODING February 7th outside Panara Bread

##  THIS IS TO REPLACE A WORD IN A LIST
#################################
##  replace_in_list(number,word)    replace_in_list(2, 'fallthru')
##################################
# replace word in list by index position
def replace_in_list(x,y,z):  
	z[x]= y   #listname[5] = 'word'
	#print(z)  #print(listname)

#  new_replace_index(x,y)  uses two variables and 
#  hard code list name and call replace_in_list(x,y,z)
def new_replace_index(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=fruits  #list name
	replace_in_list(x,y,z)   ##<<==== it calls the method above brilliant
	#print(fruits)
	


fruits = ['apple', 'banana', 'fallthru']

fruits.insert(1, "orange")

#print(fruits)

fruits[0] = 'starbucks'
#print("")
#print(" changing replacing value")
#print(fruits)
end = len(fruits)-1 # last index position

#this should put tophat into front of list
new_replace_index(0,"tophat")   #<<==== look here oinly using 2 vars
replace_in_list(1, 'break',fruits)
replace_in_list(2, 'fallthru',fruits)
replace_in_list(end, 'break',fruits)
#replace_in_list(0, "starter",fruits)
fruits=[]
fruits.append("starter")
ii = 0
while ii < 10:
	fruits.append("fallthru")
	ii += 1  #always add the dam counter
	
	
#need to have a list with the NUMBER in sequence of case sections with break
# like this  listofbreaks=[1,2,5,6,7,9]

#print(fruits)
replace_in_list(end, 'break',fruits)
#print(fruits)
replace_in_list(2, 'break',fruits)
replace_in_list(3, 'break',fruits)
replace_in_list(4, 'break',fruits)
replace_in_list(8, 'break',fruits)
replace_in_list(9, 'break',fruits)
end = len(fruits)-1 # last index position
replace_in_list(end, 'break',fruits)
#print(fruits)
#print("=====")
new_replace_index(end,"panera bread") 
new_replace_index(6,"break") 

#print("=== the end here of replace for now ===")


#==================
#Output

#['apple', 'orange', 'banana', 'fallthru']

#changing replacing value
#['starbucks', 'orange', 'banana', 'fallthru']
#['starbucks', 'break', 'banana', 'fallthru']
#['starbucks', 'break', 'fallthru', 'fallthru']
#['starbucks', 'break', 'fallthru', 'break']


######################################








#loop_thru_case_sections()  #=================


#######################
##  stage_eight()
#######################
def stage_eight():
	mytrace('stage_eight()')
	#print('stage eight')
	loop_thru_case_sections()


icecream=''
def herewego(): #loops and prints all main bodies
	mytrace('herewego')
	

	counter=0
	#this loops thru the case_main_body_list
	for item in case_main_body_list:
		if counter == 0: #skips the first slot "starter"
			counter += 1 #I forgot the bloody counter
			continue

		#print("=========================================")
		#print(case_main_body_list[counter])

		icecream= case_main_body_list[counter].count("\n")

			#myString = practicestring1
			#	print(myString)  #below zapping out pesky tabs at front
			#	# uses regular expression to nuke tabs
			#	output   = re.sub(r"[\t]*", "", myString)

		#print("==== ICE CREAM number of lines of code in section =====")
		#print("the number of lines of code in this  section=",icecream, "section",counter)

		#print("================================",counter)
		counter += 1




	#print("experimenting here in here we go")
	#get length (number of lines) of each
	#body_size = len(case_main_body_list[3])
	#print("the number of lines =",body_size)

#print("")

acounter=0
#for item in case_main_body_list:
#	print(len(item))
#	acounter += 1



#print("digitalcandy=",digitalcandy)
#big_gears_filling_list_with_case_bodies()
#herewego()  #==================================




##########################
##  stage_nine()
##########################
def stage_nine():
	mytrace('stage_nine()')
	#print('stage nine')
	big_gears_filling_list_with_case_bodies()
	herewego()


#print("tail_list cranberries =",cranberries)
###=============================================================================
x = 0;y =0
smart=''
#cranberries=[]
#print("at this juncture line 9166 what exactly is in list of rows of case names list")
#print(list_of_rows_of_case_names)

list_of_rows_of_case_names=[]
for item in list_of_rows_of_case_names:
	del item
#print("length of list_of_rows_of_case_names=", len(list_of_rows_of_case_names))


#making case section sublists here
#this is for making the variable lists to fill the case sections of cases
# and to refer to each of these caselists with ifs and elifs


#########################
##   make_case_sets()
#########################
def make_case_sets():
	mytrace('make_case_sets')
	#print("===== make_case_sets called ====")
	acounter = 0
	firstcasesectionlist=[]
	firstcasesectionlist.append("starter")
	 #this will be the case name
	#print("we have length of ", len(digitalcandy))
	#print(digitalcandy) #so we can see our input values of digitalcandy list
	for item in digitalcandy:
		x = None  #zap them out perhaps
		y = None
		#what = digitalcandy[acounter]
		x = item[0]; y = item[1]

		z = acounter
		partynation(x,y) #partynation called here------ PARTYNATION -----------
		acounter += 1
	#adding default to see if it works
	#firstcasesectionlist.append("default")
	#this happens after the loop has finished
	#print("what 9999 is this =",firstcasesectionlist)
	#print("----------")
	counter=0
	list_of_rows_of_case_names.append(firstcasesectionlist) #since this will be the last one
	castle_time()

smartcasemanager=[]  #creating the initializing smartcasemanager



#this just prints it out the sets of the cases for each case section
def castle_time(): #fills up smartcasemanager
	mytrace('castle_time')

	#list_of_rows_of_case_names.append("[['default']") #trying this
	#print("============CASTLE_TIME called ===========")
	count=0
	while count < len(list_of_rows_of_case_names):
		if count == 0:
			count +=1
			continue
		#print(list_of_rows_of_case_names[count][1:])
		count += 1

	#print("more testing to get this right")
	#for item in list_of_rows_of_case_names:
	#	print(item)

	##################################################
	### SMARTCASEMANAGER LIST FILLED HERE ############
	##################################################

	#this fills up list smartcasemanager from list_of_rows_of_case_names
	#this is doing a brute force copy of a list

	#print("list_of_rows_of_case_names",list_of_rows_of_case_names)
	#print("this is what is in list_of_rows_of_case_names")
	#for item in list_of_rows_of_case_names:
	#	print(item)

	del smartcasemanager[:] #this doesn't seem to work 
	while len(smartcasemanager) > 0:
		for item in smartcasemanager:
			del item
	#print("what is in smartcasemanager now???",smartcasemanager)

	#print("smartcasemanager should be empty now",smartcasemanager)

	#print(smartcasemanager)

	#print('after deleting last item in list')
	#print("this is what is in smartcasemanager",smartcasemanager)
	#print("the length of smartcasemanager is", len(smartcasemanager))

	finallist = ['default'] #see if this works
	list_of_rows_of_case_names.append(finallist)
	#print("this should be default below======+++")
	#list_of_rows_of_case_names[-1]
	#smartcasemanager.append("['default']") #using a default case so it can be fallthrud from above
	#print(smartcasemanager) #now we add default to the end or do we need to or not


############################
#        partynation 
############################
list_of_rows_of_case_names=['starter']
firstcasesectionlist=['starter']
def partynation(x,y):  #this grabs the body
	mytrace('partynation')
	#print("====partynation======")
	global practicestring1
	practicestring1 = ""
	mycounter=0
	firstcasesectionlist=[]
	firstcasesectionlist.append('starter')
	#start loop
	#this specifically is looking for the word case
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		if mycounter >= x and mycounter < y \
		and "case" in line:     #just added default
			genius = line.split()
			wild=genius[1].strip()
			wild = wild[:-1]
			wild = wild[1:-1]

			firstcasesectionlist.append(wild)  #adding this case name to firstcasesectionlist

		mycounter += 1
	#end loop
	#This is forcing default into firstcasesectionlist
	#wild = 'default'   #major test here
	#firstcasesectionlist.append(wild)
	for item in firstcasesectionlist:
		item.replace('"',' ' )


	firstcasesectionlist[1:-1]
	for item in firstcasesectionlist:
		item.replace('"',' ' )
	#here the currently newly minted case list is added to the big list
	#which is called list_of_rows_of_case_names
	list_of_rows_of_case_names.append(firstcasesectionlist)



	firstcasesectionlist= []
	#firstcasesectionlist.append('starter')




def testingthis():
	mytrace('testingthis()')
	#print(" this prints out the contents of the important lists")

	#print("==============================================")
	#print("digitalcandy list ========")
	for item in digitalcandy:
		pass #print(item)
		
	global candy
	for item in candy:
		pass #print(item)
		
	#print("starbucks list ====of first case names in each section ====")
	#print(starbuckslist)

	#print("smartcasemanager list ========", len(smartcasemanager))
	
	#for item in smartcasemanager:#
	#	print(item)
	
	#print("============")
	#print("case_main_body_list list ========", len(case_main_body_list))
	
	#for item in case_main_body_list:
	#	print(item)
		#print(item)
	#=== code gen here ====



####################
##    stage_ten()
####################
def stage_ten():
	mytrace('stage_ten()')
	#print('stage ten')
	make_case_sets()
	#testingthis()



#I just need the lists to build my code generation now to generation
#the logic right

#codegen is using the output lists from the parser

#this is the taillist

#this is bringing it altogether simulating it creating the
#switch case in three parts
#with a counter and a loop

#trace()
#lists for starbuvks_drive_thru_code.py
caselist     =[]
breaklist    =[]
fallthrulist =[]
defaultlist  =[]
blanklines   =[]
mixedlist    =[]
batterondeck =[] #I can have item to comapore with in here
seriestogether =[]
res =[]


alphalist =  ["a", "b", "c","d", "e","f","g", "h", "i","j","k","l","m","n", "o","p","q","r", "s", "t", "u","v", "w","x","y",":",";","(",")","{","}"]

#this will be the first
#print("this will run at the top of the page and call the functions in sequence\n")
#cranberries=[]
my_godzilla_list=[]
newlist=[]
smartylist=[]
tryagain=[]
coollist=[]
#test data here it will be one file and just flow down with no imports
#rodan=[2,7,17,24,34]

tabs =['starter',"\t","\t\t","\t\t\t","\t\t\t\t","\t\t\t\t\t","\t\t\t\t\t\t"]



#I just turned these off at the bottom

'''
sunrise=[]
fishfood()
fortunate()
test1()
testhere()
'''
###################
#       get() 
###################
#this is a return value in varholder[1]
def get(x):
	switch_return_value.append(x)
	#print("inside of switch_return_value[1]")
	#print(switch_return_value[1])


firstcaselist=[]

#digital_candy=[[2, 7], [7, 17], [17, 24], [24, 34]]

switch_python_gen=''










###=================================================================
###  below I get the location of default and closing curly brace for end of switch
###  this is to be used for determining the default case which is utilized for
###  the situation of a fallthru down into default
###  this also adds one more case tothe regular cases and I need these parameters

#print("============ surgery here S=================================")
#print("")



##########################
##  make_default_case()
###########################
def make_default_case():
	mytrace('make_default_case()')
	find_default = get_default_location()
	#print("NEW location of default =",find_default)

	lastbrace = get_closing_brace()
	#print("NEW location of closing brace =", lastbrace)


	#digitalcandy.append
#november 21st coding
#make_default_case()

## what I still need to put together to have the body of the default case
## and that will be used for the default case and the body of the else:


 ##so if line is > default and line is < lastbrace
 ##and "break" not in line
 ##and fill practice string and append the pracietce sting to case_main_body_list
##use snow(x,y) and a loop to grab the lines of code inside of default
##make sure "


#print(" this prints out the contents of the important lists")

#print("==============================================")
#print("digitalcandy list ========")
#for item in digitalcandy:
#	print(item)



#print("they all need to start with 'starter' in position 0")
#print("the big 3 need to have the same number of elements for the length to be the same")

#=============================================================
# smartcasemanager list   #list of lists of case names
# case_main_body_list     #body python code for each case section
# tail_list               #breaks and fallthrus
# digitalcandy

#===== inputs ========
#firstcasesectionlist
#list_of_rows_of_case_names
#case_main_body_list
#cranberries #taillist

#=============================================================
# smartcasemanager list   #list of lists of case names
# case_main_body_list     #body python code for each case section
# tail_list               #breaks and fallthrus

#===== inputs ========
#firstcasesectionlist
#list_of_rows_of_case_names
#case_main_body_list
#cranberries #taillist

#what smartcasemanager output looks like in ufos file
#this was tyhe failed attempt at managing the indentation over to the left
#for the switch case output in python and I have a simpler solution I will end up using.




		#counter += 1














##########################
##  parktime()
###########################
def parktime():
	mytrace('parktime')
	import re
	myString = "\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
	#print(myString)
	output   = re.sub(r"[\n\t]*", "", myString)

 #seeing teh contents of stanford
def what_is_in_stanford():
   # print("what is in stanford")
    print("len of stanford =",len(stanford))
    for item in stanford:
        print(item)
        print("---------------")
        
##########################
##      stage_eleven()
###########################
def stage_eleven():
	mytrace('stage_eleven()')
	#print('stage eleven')
	parktime()


#input for the switch case happens (above) the docstring JavaScript switch case interface

#made June 29th, 2021 
#this changes switch to inswitch and fallthru into infallthru
#this is required for doing nested switches 
#nested_switch[0] must be = True
#paloalto[0]




######===================================================================
###======== switch_code_gen here ============
# add error mistake if no input for exp it will do nothing
# this is good for me to think of adding
# also add break if no break in default for input from js switch
# monday dec 14th thinking
# need to add input stuff here that is in the top running betterworks

sw=''
sweet =''
switch_gen=''
#testing input here
  #this has to be above the generated code

testlist=[]
exp =''
##############################
tahoetest=[]
tahoetest.append(0)
nested_switch=[]
nested_switch.append(False) #default testing 

main_switch=[]
main_switch.append(0)
main_switch[0]=0

#added this on June 28th, 2021 7:08 pm
gti=[] #this saves the output for the main switch by default no matter what (CATCHES IT)
execute_main_switch=[]
execute_main_switch.append(0) #this just creates position 0
###############################	
funny=[]
funny.append(0)  #used for testing nested switch
	
	
	###================= june 29th editing ===================
'''
	print("this is the test_flag") 
	if execute_main_switch[0] == True:  #flag  execute_main_switch
		exec(sweet)
	else:  #if False then store teh string for later use 
		#print(sweet)
		paloalto.append(sweet)
		print("this should be the main switch printed out, and not executed")
		print("paloalto=",paloalto[0])
	####============= june 29th 2021  testing ==================	
	print("try the magic add infallthru and inswitch june 29th,2021")
	if nested_switch[0]== True: 
		print("yes nested_switch[0] == True")
		seal1 = paloalto[0]
		x1 = seal1.replace("switch(exp)", "inswitch(exp)")
		paloalto[0] = x1
	
		seal2 = paloalto[0]
		x2 = seal2.replace('fallthru(', 'infallthru(')
		paloalto[0] = x2
		#print(paloalto[0])
	else:
		pass
		
'''

# this replaces switch to inswitch and fallthru to infallthru
# after the python has been generated

#def modify_for_nested_switch_method(x):


#paloalto=[]
#def change_switch_and_fallthru_for_nested_mode(inputlist):
#	return
#	if nested_switch[0]== True: 
#		print("yes nested_switch[0] == True")
#		seal1 = paloalto[0]
#		x1 = seal1.replace("switch(exp)", "inswitch(exp)")
#		paloalto[0] = x1
#	
#		seal2 = paloalto[0]
#		x2 = seal2.replace('fallthru(', 'infallthru(')
#		paloalto[0] = x2
#		#print(paloalto[0])
#	else:
#		pass

###########################
# june 30th 2021  wednesday testing gathering the output of the code gen into stanford list
stanford=[]  #I am not emptying this so it should just fill up
################################
##      switch_code_gen()                                                                 ###
################################
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():
	mytrace('switch_code_gen()')
	#####
	
	
	#Here I am putting the contents of penguin into cranberries
	#print("this is where I empty cranberries list and fill it with penguin")
	del cranberries[:]  #emptying cranberries here 

	for item in penguin:  #this works - how wonderful
		#print(item)
		cranberries.append(item)
		
	
	
	###########  march 7, 2021  #######################################
	# I think that I just need to loop through casemainbodylist
	# and append cranberries based on teh counter and then eliminate the third tier below
	# what I am doing is adding teh cranberris(one liner break or fallthru to the case_main_body_list
	####################################################################

	
	
	case_main_body_list_with_tail=['starter']
	
	######## acounter is HERE on next line
	acounter=1
	
	for item in range(1,len(case_main_body_list)):
		felix = case_main_body_list[item]
		#print("inside of the parser ========")
		#print("====I am looking inside the case_main_body_list here===")
		#print(felix) # I would get what case I am in here 
		#print("====acounter=", acounter ,"============")
		
		# removes newlines after lines of code
		victory = felix.rstrip()
		
		victory +="\n\t\t"+ cranberries[acounter] #tacks on break/fallthru
		
		case_main_body_list_with_tail.append(victory)  #appends the melding together to 
		
		victory=None
		victory=''
		                                 #case_main_body_list_with_tail
		#print("--------------")
		
	
		acounter += 1
	
	
	#==== end loop ======
	
	anewcounter=0
	
	
	


	##############
	topvars2 = "\nexp = varholder[0]\n\n"


	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:

	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(einstein)-1 #was using smartcasemanager but polluted
	###################################################
	#   this is printing out the caselists at the top
	###################################################
	
	#print("einstein=",einstein)
	
	#--- testing dec 24th for varholder[0] input word ----
	#------------------------------------
	top_input_of_exp = "exp = varholder[0]" 
	
	# "varholder.append(exp)\n" +
	#print("varholder[0] =",varholder[0])  
	#new line to see the input expression exp from clever

	
	print(varholder) #added this to see what the input in clever is
		#-------------------------
	# this prints the case lists of the words in each case section
	


	einstein.append("default")  #adding default to the end of einstein copy list
	
	#print("einstein list",einstein)
	
	
	
	 
	for item in range(1,len(einstein)):     #first loop was smartcasemanager
		trains =  str(counter)
		merge = "caselist" + trains    #caselist1
		toosmart = eval(merge)
		caselist = merge + " = " + str(toosmart)    #this is the caselist name we eval to display it
		#print(caselist)
		testlist.append(caselist) #trying a hunch here
		######################
		#inside1 = caselist  #this is only apparently capturing the last one
		#####################

		counter += 1
		numb += 1
		
	#after loop finished we have the caselists generated captured inside of testlist
	
	##############################################
	switchy= "switch(exp)\n" +"while True:\n\n" #=====
	##############################################

	print("")

	mycounter =1 #it was 0
	#size=  #notice -1

	front="case in caselist"

	#this makes each case section
	#=======   LOOP  =================
	# I will need to use the first part, second part, third part
	# I will use three seperate lists that work in tandem to hold the variable strings
	# which will then be accessed to concat the strings in the proper order
	#=================================
	firstpart =[]
	secondpart=[]
	thirdpart =[]
	extremelysmart=[]
	
	

	#just changed this to range(0,len(case  it was range(1,len(case 
	for item in range(1,len(case_main_body_list_with_tail)):       #second loop
		if mycounter == 1:
		#============  first section case=============

			first_if= tabs[1] + "if " + front+str(mycounter)   + ": #"
			toosmart = eval("caselist" + str(mycounter))

			newlist = [first_if, toosmart]
			##############################################################
			sofrustrated =str(newlist[0]) + " " + str(newlist[1]) #=== only catching last one==
			extremelysmart.append(sofrustrated)
			###### firstpart adding if line ###########
			firstpart.append(sofrustrated) #this feeds the if line into first part list
			### these are the case sections AFTER the FIRST CASE SECTION  	
			# this is different because it starts with an elif instead of the first if
		else:    #rest of cases after first case ======
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber
			caselistline = str(newlist[0]) + " " + str(newlist[1]) #=====
			extremelysmart.append(caselistline)
			firstpart.append(caselistline) #this feeds elif line into first part list
		
		######################
		#=== second part of each case section
		weasel= case_main_body_list_with_tail[mycounter]   ### RIGHT HERE 
		secondpart.append(weasel) #this feeds the string body into secondpart

		######################
		#=== third part of each case section
		#this is the tail either break or fallthru(name)
		
		
		mycounter += 1     #loop counter
	
	#=== END LOOP  =============================================

	################
	theelse = tabs[1] + "else:"  #this is just once
	firstpart.append(theelse) #this feeds the else clause into first part
	#this is the last real case after the regular cases

	##################3
	 #last case body for default

	lastishcase =case_main_body_list_with_tail[-1]

	secondpart.append(lastishcase)  #this feeds the body into secondpar

	##########################
	
	#this works this creates the strings of the caselist at the top above switch correctly
###============================================
# caselists concatted to string cool
	cool=''

	#== LOOP === these are stored in list called testlist
	for item in testlist: #to see if the caselist names are in here  in this list
		cool += item + "\n"
		#print(item)
	#== end loop 
	
	cool += "\n\n"

	#== END LOOP

################################################################################################
##### march 7th, 2021  I think I just add thirdpart to end of second part (it's just one line)
################################################################################################
#===case sections three parts at once ==")
	rocks=''
 #=====================
 #== LOOP
	counter=0  #each section will have the same number of items
	for item in firstpart:
		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n\n"
		counter += 1
		#printing out the three part case sections")
 #=== END LOOP

	#adding strings together here
	#=========================================
	sweet = topvars2 + cool + switchy + rocks
	#=========================================
	###============== stanford. append(sweet) =============
	# putting sweet into list stanford june 30th, 2021
	stanford.append(sweet) #Right here the output string is appended to stanford
	#here I am filling the list stanford with the sweet string before it's executed
	###=====================================================
	
	#here I will put exec(sweet) but testing multiple right onw
	
	print("=======sweet in code gen ==has this in it====june 21st==")
	print("=======sweet in code gen ==has this in it====june 21st==")
	print("=======sweet in code gen ==has this in it====june 21st==")
	print("=======sweet in code gen ==has this in it====june 21st==")
	funny[0]='' #clears it out first
	funny[0] = sweet
	print("june 29th progress Santa Cruz Avenue coding ")
	#del tahoetest[:]
	#print("just emptied tahoetest")
	#print(tahoetest)
	############ this takes out endswitch from python generated code
	##=-============june 29th, 2021 coding starbucks ===============
	# print(sweet) #this is the generated code 
# 	if "endswitch" in sweet:
# 		print("yes endswitch found in output")
# 		for line in sweet.splitlines(): 
# 			if "endswitch" in line:
# 				line = line.replace("endswitch","}")
# 				break
# 			else:
# 				continue
# 	print("new version of sweet")
# 	print(sweet)
	#so whenever I need to grab the main 
	#list gti will hold the main switch in position 0 always and is current
	gti.append(sweet)  #default this is saved 
	#when multiple switch is carried out I need to grab the main switch string
	#to add to the multi layer cake
	
	
	#what if we just capture this string so we can use it and save it if we need
	# it and so that solves the problem actually.
	
	
	#june 28th 2021=================
	#########----------------------------------------------
	#if doing_main_switch_with_nested_switches == True:
	#   #add main switch string which will have nested_switch_methods
	#   if len(multiple_switches) == 0: #not filled yet
	#       #add main switch to list 
	#        multiple_switches.append(sweet)
	#        
	#    if len(multiple_switches >= 1 and nested_switch[0] == True:
	#     
	    
	print("to execute it or not, yes if only one switch stanford len == 1 =")
	print("I will need to know based on before it is even run so I need to")
	print("count how many switches are in the switch string")
	print("based on that number we will KNOW before start inside of endswitch() ")
	print("if it is a solitary switch or a switch with nested switches inside of it")
	#listname switchcount
	
	## the list name will be called switch_count
	################# june 30th, 2021  10:02 am Santa Cruz Avenue Starbucks #############
	#this determines if we execute a switch string based on if there is ONLY one switch() in it)
	# because if there are more than 1 switches in it then it MUST HAVE nested switches
	print("this is INSIDE THE CODE GENERATOR in teh Silver Module")
	print("number of switches in this switch string is ",len(switch_count))
	print("we have a switch_count = ",len(switch_count))
	#switch_count is a list
	print("this is where the fuzzy logic determines if")
	print("the switch code in python is executed or NOT executed immediately")
	print("but is added to the stanford list which is automatic and then")
	print("it is put into a triple string to work in tandem with the nested switches")
	print("methods")
	print("LEN(SWITCH_COUNT=",len(switch_count)) #this will be for each switch string
	print("we have for len(switch_count",len(switch_count))
	'''
	if len(switch_count) == 1:
		exec(sweet)
	else:
		pass  #it is automatically already indenpendently added as a string to stanford list
	'''	
		
	#############################################
	if show_code[0] == True:
		print(sweet)
	else:
		#print(sweet)  #otherewise don't print it
		pass     
	    
	    
	    
	# here I will have the flag to show or hide the output 
	# to see what the generated code is.
	#############===================
	#################################
	#################################
	print("show_code =",show_code[0])
	if show_code[0] == True:
		print(sweet)
	else:
		#print(sweet)  #otherewise don't print it
		pass # do nothing
	#############===================
	#################################
	#################################

	#print('===== executing generated  code=====')
	# right now the nested output switch is a nested single switch
	# for doing what I want to do I need to create the main switch also
	# as a string and not execute it immediately.
	# today is June 28th, 2021
	
	########################################
	print("the input exp in clever was:: ",varholder[0]) #varholder[0]
	#print("")
	#this is where the generated python code (shown above) is executed
	
	#print("$$$ ===>> nested_switch[0]=",nested_switch[0])
	#print("what is in tahoe test at this point",tahoetest)
	#print("what is in tahoetest[0]",tahoetest[0])
	######################################
	
	
	
	
	
	##### this is to check to make sure that it puts sweet string into
	##### tahoetest[0] which is the first slot for now
	##### eventaully it will be several.
	#It is set before the switch string input in file test_inputs_beta
	#by default nested_switch[0] will be set at False
	## June 17th, 2021 testing Starbucks Santa Cruz Avenue
	#if nestedswitch True add sweet string to tahoetest[0]
	
	'''
	if nested_switch[0] == True:
		print("====nested_switch[0] = True ===",nested_switch[0])
		print("====don't execute generated python===")
		print("==== put it into tahoetest[0]===")
		## this says: put sweet into tahoetest[0]
		#############################################
		tahoetest.append(sweet) #this adds it in sequence
		# this captures the generated string and puts it into tahoetest list
		
	
		#this will needto append it rather then targeting tahoetest[0]
		#print insdeof this if let's see what it's lengthis
		print("length of tahoetest[0] =",len(tahoetest))
		print("let's immediatley see it's contents")
		print("===...===...===...==this prints out the generated python")
		print("tahoetest[0]=",tahoetest)
		#halloween=''
	'''
		#halloween = ''.join(tahoetest) #string from list to loop thru it
		######################################
		#decided I concat and build a string just use it - sweet
		#for line in sweet.splitlines():
			#if "break" or "fallthru" in line:
				#how_many_tabs=line.count("\t")
				#print("number of tabs =",how_many_tabs)
	'''
		#################################################
		print("==== /// \\\\ =====bottom of the output python hopefully")
	else:  # if nested_switch[0]= False
		#this means exec(sweet) which means it's not a nested switch 
		print("$$$ ==should be False=>> nested_switch[0]=",nested_switch[0])
		print("we are executing the generated code")
		
		main_switch[0]=gti[0] #this is a flow thru transfer by default
		
		#this will need to be set in bypass205
		
		if multi_switch_with_nested_switches[0] == True:
			print("don't execute it - don't run the output python")
			print("this is the main switch which we will add to the rest of the nested switches")
			print(gti[0])
			print(main_switch[0])
			#we can access gti[0] with the main switch python where we need it
		else: #means  multi_switch_with_nested_switches[0] == False
		
			#regular single switch with no nested switches within it
			exec(sweet)  #this is the building of the string of python code strings
	'''
	#####################################
	## testing ##### experimenting June 29th, 2021 Starbucks testing =======
	# remember that I wanted it to save each main switch by default
	# and only execute it if it is only switch in list so list length of 1  is True
	
	#paloalto=[]
	
	
	## what this does is use a flag to govern whether the main switch is executed
	## right off the bat. if execute_main_switch(first switch) is set to True execute
	## it means that there are no nested switches in it (except a method)
	## this is based on how many switches there are inside of the string
	
	#### this is a flag to determine if it is generated ######

	#change_switch_and_fallthru_for_nested_mode(paloalto[0])
	#print(paloalto[0])
	print("I jsut flipped it to False to see if it now doesn't ")
	print("put the sweet string of the python output into tahoetest[0]")
	print("what is in slot 1 of the list -the entire output string")
	#print(tahoetest[0])
	#print("what we have in tahoetest",tahoetest)
	#lets's look at tabs in line with fallthru
	
	
	# this runs the python switch code as ifs with the input
	# hard coded into it
	sweet=None
	sweet=''
	
	topvars2=None
	topvars2=''
	
	cool=None
	cool=''
	
	switchy=None
	switchy=''
	
	rocks=None
	rocks=''
	
	#print("")
	#print(" =====done executing output from switch ======")
	#print("")
	#print("testing this deletion of list with tail")
	case_main_body_list_with_tail=['']
	#print("we have",case_main_body_list_with_tail)	
		
	#print("now deleting this list case_main_body_list_with_tail")
	#case_main_body_list_with_tail=[] #hardcoded it to ensure it works
	firstpart=[]
	secondpart=[]
	thirdpart=[]
	extremelysmart=[]
	
	
#this is called after switch_code_gen
#####managing_nested_switch_scenario():

## MANAGING NESTED SWITCH SCENARIO

def managing_nested_switch_scenario():
	print("=====managing_nested_switch_scenario() called=====")
	print("=====managing_nested_switch_scenario() called=====")
	if len(stanford) > 0: #meaning something is in Stanford
		#print('nested_switch[0] = True')
		print("stanford list length=",len(stanford))
		print("so do the building cake methods")
		print("lengstanfordth of stnaford is ",len(stanford))

	else:
		print('nested_switch[0] = False')
		print("nested switch is False do nothing more")

##3===================================================        













#this executes the generated python switch code
def stage_twelve():
	gti=[] #clears out gti list 
	mytrace('stage_twelve()')
	#changing to run second switch case january 15, 2021
	switchcasetester =''
	sw =''
	
	#print("hopefully this will empty smartcasemanager")
	#print("it current has this in it ", smartcasemanager)
	#print("it's current length =",len(smartcasemanager))
	
	
	#print("list_of_rows_of_case_names ", list_of_rows_of_case_names )
	del list_of_rows_of_case_names[:] #empties this list
	#print("list_of_rows_of_case_names ", list_of_rows_of_case_names )
		
	for x in caselist1[:]:
		caselist1.remove(x)
	
	for x in caselist2[:]:
		caselist2.remove(x)
		
	for x in caselist3[:]:
		caselist3.remove(x)
		
	for x in caselist4[:]:
		caselist4.remove(x)
		
	for x in caselist5[:]:
		caselist5.remove(x)
		
	for x in einstein[:]:
		einstein.remove(x)
	
	smartcasemanager=[]
	#print(smartcasemanager)
		
	for x in testlist[:]:
		testlist.remove(x)
		
	
	resetting_up_case_body() #clears out case_main_body_list then appends('starter') to it
	 
	
	smartcasemanager=[]
	

# right now the limit is 10 case sections I need to add to that


	
	#this seems to work whereas nothing above actually worked
	## only guaranteed way to empty lists completely 
	for item in range(0,len(palmtrees)):
		palmtrees.pop()

	for item in range(0,len(digitalcandy)):
		digitalcandy.pop()

	for item in range(0,len(einstein)):
		einstein.pop()

	for item in range(0,len(wilecoyote)):
		wilecoyote.pop()
		
	for item in range(0,len(candy)):
		candy.pop()
		
		
	for item in range(0,len(case_main_body_list)):
		case_main_body_list.pop()
		
	

	for item in range(0,len(birdsong)):
		birdsong.pop()
##3====================
	for item in range(0,len(caselist1)):
		caselist1.pop()

	for item in range(0,len(caselist2)):
		caselist2.pop()

	for item in range(0,len(caselist3)):
		caselist3.pop()

	for item in range(0,len(caselist4)):
		caselist4.pop()

	for item in range(0,len(caselist5)):
		caselist5.pop()

	for item in range(0,len(caselist6)):
		caselist6.pop()

	for item in range(0,len(caselist7)):
		caselist7.pop()

	for item in range(0,len(caselist8)):
		caselist8.pop()

	for item in range(0,len(caselist9)):
		caselist9.pop()

	for item in range(0,len(caselist10)):
		caselist10.pop()
##3==========
	for item in range(0,len(royallist)):
		royallist.pop()

	for item in range(0,len(cranberries)):
		cranberries.pop()
		
	for item in range(0,len(roadrunner)):
		roadrunner.pop()
		
	for item in range(0,len(penguin)):
		penguin.pop()
		
	for item in range(0,len(british)):
		british.pop()
		
		
	###############
	#print("gti",gti)
	for item in range(0,len(gti)):
		british.gti()
		
	#print("mochalist",mochalist)
	for item in range(0,len(mochalist)):
		mochalist.pop()
		
	#print("drive_thru",drive_thru)
	for item in range(0,len(drive_thru)):
		drive_thru.pop()
	#funny
	#print("case1findbreak",case1findbreak)
	for item in range(0,len(case1findbreak)):
		case1findbreak.pop()
		
	#print("case1findfallthru",case1findfallthru)
	for item in range(0,len(case1findfallthru)):
		case1findfallthru.pop()
		
	#print("defaultlist",defaultlist)
	for item in range(0,len(defaultlist)):
		defaultlist.pop()
			
	#print("seal",seal)
	for item in range(0,len(seal)):
		seal.pop()
	#print("this one is the HOLY GRAIL one")
	#print("line_numbers_of_first_cases",line_numbers_of_first_cases)
	for item in range(0,len(line_numbers_of_first_cases)):
		line_numbers_of_first_cases.pop()	

	#print('==== after clearing them we have ======')
	
	if len(palmtrees) > 0:
		palmtrees.pop()
	#print('after checking the length of the list this deletes more if greater than 0')
	#print("palmtrees=",palmtrees)
	#print("starbucklist=",starbuckslist)
	for item in digitalcandy:
		digitalcandy.pop()

	#print("digitalcandy=",digitalcandy)
	
	if len(einstein) > 0:
		einstein.pop()
		
	
	#print("=========")
	for x in smartcasemanager[:]:
		smartcasemanager.remove(x)
	#print("contents of smartcasemanager=",smartcasemanager)
	
	#print("see if this helps empty it smartcasemanager")
	for item in smartcasemanager:
		smartcasemanager.pop()
		
		
	
	del trontime[:]  #empties trontime list
	#print("now trontime =",trontime)
	



#==========================================================================================
#===== this is test what will be generated below after the python switch is generated above



####======= this is the input to the python switch
#input_list = ["fortune"]  #global var that will be fed into switch(x)








list1=[]
list1.append("five")












#========================
#bigtestofcodegen() #massive test here getting the output
#remember that the generated python switch will be invisible except for debugging purposes


#I turned this off to work on the generation of the python that this represents

#bigtestofcodegen()

#I will need the switch and fallthru functions now
#this counts the number of lines with \n in each case section

#############################################
#count number of n's in tail
#append 2 tabs to the front of each line to
# Slice string to remove 3 last characters
#mod_string = org_string[:-3]
#print(mod_string)
















def marine_one():
	mytrace('marineone()')
    #print("====== marine one called =====")
	#print(switchcasetester)
    #print("the number of tabs in this baby")
	tabnumbers =switchcasetester.count("\t")






# put this into a function
#switch_code_gen() ##=== this calls and generates the python switch case
				  ##=== this has the code generation of the python code
#print(switch_python_gen)
#exec(switch_python_gen)




def pilgrim(): #testing import in another file
		print('pilgrim')


##############################
###      flush lists()
##############################
def flush_lists_previous():
	mytrace('flush_lists()')
	#print("flush_lists() called hallijua")
	gti=[]
	royallist=[]
	palmtrees =[]
	woodstock=[]
	oceanwaves=[]
	candy=[]
	digitalcandy=[]
	einstein=[]
	smartcasemanager=[]
	varholder=[]
	british=[]
	cranberries=[]
	

#case_main_body_list=[]
#this is new but I haven't tried 
# this has a sequence that must be followed for it to work 
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
	
	#flush_lists() #this is new january 16th, saturday debugging trying second switch case
	
daisy=''
m1=[]
m1.append(0)

sample_fish='''
 switch(x)    
    while True:                 
        if   case  == "one":
            print("this is the first case in the main ")
          
            ######################
            print("out of from  below")
            print("tahoe[0]=",tahoe[0]) #result of  running
          
            fallthru('word')   
                     
        elif case == "two":
            print("this is the first case in the main ")
            prelow")
            print("tahoe[0]=",tahoe[0]) #result of  running
            fallthru('word') 
            
        elif case == "three":
            print("this is the first case in the ")
            print("out of from  below")
'''
### just had idea if a nested method switch has yet another nested switch
#in it it needs to be changed to a method so it wouldn't happen.

listforfun=[]
listforfun.append(0)
inputstringswitches=[]
inputstringswitches.append(0)
inputstringswitches.append(0)

#after doing the silver module call this
#modify nested switch 
def modify_nested_switch():
    print("called modify switch for nested method switch")
    galaxy=''
    galaxy = sample_fish  #this is modifying string above for being a nested switch
    #listforfun[0]= galaxy
    inputstringswitches[1] = galaxy.replace("switch","inswitch")
    galaxy = galaxy.replace("fallthru","infallthru")
    inputstringswitches[1] = galaxy
    print("how does this look.... june 29th.")
    print(inputstringswitches[1])
    
    #inputstringswitches[1] = galaxy.replace("endswitch","}")
print("just checked it's not changing switch to inswitch for some bizarre reason")
print("that is a bug in the method and programming language python")
print("good thing I tested this thoroughly to find the bugs")
print("so this code above that should work DOES NOT work")
print("testing output string converted sample to nested type inswitch, infallthru")
print("=====[[[[[[[[[=quick testing I did a while ago juen 29th =====]]]]]]]]]]===[[[[]]''';;;;;;;;;")
modify_nested_switch()

#this works in fourth_of_july through dulegence 
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")

#x =dumbstringcode.replace("switch","inswitch")
#dumbstringcode=x

#y = dumbstringcode.replace("fallthru","infallthru")
#supergood = y

#print(supergood)
#print("did it finally work or not===========>>>>>")
#z = supergood  #this fixes a bug where the nested switch method is wrong
#y = supergood.replace("inner_inswitch","inner_switch")
#exam = y
#print(exam)
#print("===== end of good working code ==============")




####### TESTING 
print("testing doing a simple test of switch and fallthru changing it")
#modify_nested_switch(sample1)
#print(m1[0])


import re
def hasNumbers(inputString):
		return bool(re.search(r'\d',inputString))



	############################
	
			

##############  added April 2nd, 2021  ###############################################
# this is a pre scan of the switch case input string to determine if
# the cases are numbers like case 1 thru 5: or case 10 OR words like case "apple":
coffee=[]  #holds line number of first case in switch case
valve=[]
valve.append("nada")# 0
valve.append("sway")# 1 #so we have valve['nada','sway']
#these are just fillers they mean absolutely nothing

# this gets the line number of the first case in the switch case string
#####################################################
##  grab_first_case_of_switch_string(y)
##################################################### 
def grab_first_case_of_switch_string(y): 
	mytrace("grab_first_case_of_switch_string()") 
	#global switchcasetester
	mycounter = 0
	#this takes in sw to test for finding out if numbers like case 2: or words case "apple"
	for line in y.splitlines():
		if "case" in line:
			coffee.append(mycounter) 
			break  #here after getting the first instance of a case we leave the loop
		else:
			mycounter += 1
			continue

#####################################################
##  remove_tabs_from_string(y)
##################################################### 
def remove_tabs_from_string(y):
	mytrace("remove_tabs_from_string()") 
	y=y.replace("\t","")
	return y

#####################################################
##  grab_first_case_line_in_switch_case_string(y)
##################################################### 
def grab_first_case_line_in_switch_case_string(y):
	#global sw
	mytrace("grab_first_case_line_in_switch_case_string()") 
	#print(coffee[0])  #testing what's in this
	getline= eval("y.splitlines()[" + str(coffee[0]) + "]")
	#print(getline)
	return getline


##################################
##  check_if_number_in_string(x)
################################## 
def check_if_number_in_string(x):
	mytrace("check_if_number_in_string()") 
	theresult = any(char.isdigit() for char in x)  #this line from stackoverflow
	return theresult

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
# flow_fork_input()  #this fills valve[0] with True or False
# if valve[0] is True  it means numbers = True  (thus numbers      )
# if valve[0] is False it means numbers = False (thus words strings)
## the new code will go in here Friday morning.. April 2, 2021
#this fills valve[0] with True or False for numbers in cases
#################################
##     flow_valve_input(y)
##################################
def flow_valve_input1(y):  #this determines if switch case string is numbers or words
    #print("Flow Valve input")
    mytrace("flow_valve_input()")                            #get first case in switch case string
    ######## this gets the necessary data to test if case is a number
    getline  = grab_first_case_of_switch_string(y)           #get first case line
    toocool  = grab_first_case_line_in_switch_case_string(y) #remove tabs from the case line
    toocool  = remove_tabs_from_string(toocool)              #test if number in first case line yes = True no = False
    ######## here the data is now analyzed to see if a number  and returns True if number False if not number
    valve[0] = check_if_number_in_string(toocool)            #looks in case line
    valve[1] = toocool                                       #put case name/number into valve[1]
    #print("output from FLOW VALVE=",valve[0],"and",valve[1])
    
    #print("valve[0]=",valve[0]," and valve[1]=",valve[1])
   # print("========")
################################################



def blue2():
    mytrace("blue2()")
    #print("blue2()")
    #print("do NUMBERs parser")
    
def pink1():
    mytrace("pink1()")
    #print("pink1()")
    #print("do words parser")
    
#this fills valve[0] with True or False
#based on analyzing the switch case string first case if number or not
############################
#this controls calling numbers parser if True
#this controls calling words   parser if False
#this is in great_pumpkincat2.py


#this part hasn't been tested yet.
# I have to make sure that the normal endswitch() continues to work 
switch_count=[]
switch_count.append(0) #to create position 0
number_of_switches_in_string='' #initializing it July 1st 2021

########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	print("====TESTing in beginning of endswitch() =====>>>")
	print("====TESTing in beginning of endswitch() =====>>>")
	print("====TESTing in beginning of endswitch() =====>>>")
	switchcasetester='';switchcasetester=None;
	del switchcasetester;switchcasetester='';
	mytrace("endswitch() in switch_cat called")
	show_input_switch_string() #flag for testing this shows the input string
	#hide_input_switch_string()# flag for showing input string
	###################################
	###################################
	#june 30, 2021 10:10am santa cruz avenue Menlo Park
	#count switch inside of input string for switchcase
	print("====This is inside of silver switch module ")
	print("====This is inside of endswitch function before doing anything to the string")
	print("====meaning BEFORE the switch string is parsed")
	# I might hav eto redo this one as line.startswith("switch")
	########### I might have to do it different hen count and loop thru it
	########### and get teh accurate count that way 
	# so I wouuld loop thru string
	#and check if line.startswith('switch') to know for sure.
	#I can verify by also counting line.startswith("endswitch")
	'''
	###################################################
	#print("what is in switch_count list starting", switch_count) #should be nothing
	#number_of_switches_in_string =y.count("switch")
	#print("extra counts this many switch(s) in the string",number_of_switches_in_string)
	#
	#print("try counting endswitch for nested and then add 1 for first switch")
	#this idea occurred to me if the switch search isn't accurate
	'''
	############
	############ testing experimental (right now it doesn't matter
	############ july 1st, 2021  commented this out today don't want to think about this part 
	'''
	realnumber = y.count("endswitch") #it's possible there are no nested switches
	realnumber = realnumber + 1 #this account for the first switch which isn't counted
	if realnumber == None or realnumber == 0:
		realnumber = 1 #this is in case there are no endswitches meaning no nested switches
	#end if
	print("see if this number is different")
	print("counting the endswitch + 1 we get ",realnumber)
	'''
	
	
	#this just counts the number of "switch" in the string but not their locations
	#with my loop concept idea I would get the line number of each switch
	#but the moret that I thought about it the more it occurred to me that
	#the only way to know for sure is to count "endswitch"
	##===================================
	#right now for now this doesn't matter nor concern me one bit
	######### what this section does is determine how many switches are in a string
	#########################
	#print("extra count of switches in this input switch is",number_of_switches_in_string)
	#switch_count[0]=number_of_switches_in_string
	#print("the number of switch_count in THIS input switch string =",switch_count)
	#if switch_count[0] == 1:
	#	print("it is ONE")
	#else:
	#	print("it is ",switch_count)
	#print("===========#####################=====================")
	###################################
	
	###===================
	check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
	
	if baseline[0] != "nada": #means it converted to uppercase
		y = baseline[0]
	#else:   #added this else  and pass on June 16th
	#	 pass #this puts the input string from baseline[0] into y
	#####################
	#this checks if first case is a number like case 2: returning True if numbers 
	flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
	#####################
	print("if number in first case",valve[0])
	# the key is macro expansion is only called if numbers are True
	if valve[0] == True:    #meaning numbers like case 12:
		macro_expansion(y); #checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
	#end if
	#####################################
	flush_lists() 
	parser_mode_1(y) 
	################## normal endswitch ends here  don't mess it up.
	####################################################################
#parser guts is the same sequence of code in the endswitch above
# I am just trying to reduce code  that's all.
####============================
####      parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("parser_guts called =======")
	check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
	
	if baseline[0] != "nada": #means it converted to uppercase
		y = baseline[0]
			#else:   #added this else  and pass on June 16th
			#	 pass #this puts the input string from baseline[0] into y
		#####################
		#this checks if first case is a number like case 2: returning True if numbers 
	flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
	#####################
	print("if number in first case",valve[0])
		# the key is macro expansion is only called if numbers are True
	if valve[0] == True:    #meaning numbers like case 12:
		macro_expansion(y); #checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
		#end if
		#####################################
	flush_lists() 
	parser_mode_1(y) 	
		
		
#end of parser_guts()	
	
	######## this is the bottom of the normal scenario of a switch string with only one switch case in it
	
	####### this is where I will be testing using 2 and 3 switches in one string
	#######  july 1st, 2021  testing
	#####===============================================================================
	#####      BYPASS205  HANDLES AND MANAGES DOING NESTED SWITCHES , SO SWITCHES WITH 1 OR MORE NESTED SWITCHES
	####==================================================================================================
	##### this is bypass205 and it will manage and handle doing a multiline string
	##### which does multiple calls of the parser and code gen and fills a list called stanford
	####  with the generated python string 
	####  and then adds methods to the nested switches and then 
	#### builds a multi layer cake by concattting (in file fourth of july ) and executes it).

### this is testing and not in the real code ######

#=========================
#actual generated ouput code from chain methods on december 6th around 6 pm gilroy.

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

chain_output_list=[]
chain_output_list.append(gold1)
chain_output_list.append(gold2)
chain_output_list.append(gold3)
chain_output_list.append(gold4)
chain_output_list.append(gold5)
chain_output_list.append(gold6)
chain_output_list.append(gold7)


string_test1 = '''
	switch(exp) {  
		case 1:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4: 
			print('kangaroo hop hop!')
			n = 'more' #testing
			#nested_switch_2(n)  #maybe keep it a comment until it's in python        
			print('taught me how to write code')
			fallthru
			
		 
		case 8:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
			break
}
'''
string_test2 = ''' 
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
			break
} 
'''

string_test3 = ''' 
	switch(exp){          
		case 'zoo time':
			print("san francisco zoo")
			print("feed the flamingos")
			fallthru
		case 'the beach in santa cruz':
			print("volleyball and boardwalk")
			break
		default:
			print("we are done here")
			break
} 
'''

### this is a force feed test

string1='''
	switch(exp) #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru	
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############1
			nested_switch_11:(exp) #11
			exp = 32
			nested_switch_62:(exp) #62
			##############)
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
#this is different I see based on test model above

string2='''
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
'''


string3='''
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
'''

string4='''
	switch(exp) #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")#
		####################1
			nested_switch_31:(exp) #31
			#############
			break
		default:
			print("we are done here")
}
'''






string7='''
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
'''
#was string1 thru 7
### TESTING THIS Still TOTALLY EXPERIMENTIONAL		
quail=[] #this will simulate a switch stirng nested that  is split already into 3 switches
#this fills the three inputs trings into the quial list
# so these are still in javascript form for the switches
#quail.append(string_test1) #actual switch case with one switch for simplicity
#quail.append(string_test2) #actual switch with one switch
quail.append(gold1) #actual switch with one switch 
quail.append(gold2)
quail.append(gold3)
quail.append(gold4)
quail.append(gold5)
quail.append(gold6)
quail.append(gold7)

#quail.append(string1)
#quail.append(string2)
#quail.append(string3)
#quail.append(string4)
#quail.append(string5)
#quail.append(string6)
#quail.append(string7)

#get quial length should be 0, 1, 2 so 3 length
future = len(quail)
print('THE length of quail list =',future)
print('quail[0]')
print(quail[0])
print("===========")
print('quail[1]')
print(quail[1])
print("===========")
print('quail[2]')
print(quail[2])
print("===========")
print('quail[3]')
print(quail[3])
print("===========")
print('quail[4]')
print(quail[4])
print("===========")
print('quail[5]')
print(quail[5])
print("===========")
print('quail[6]')
print(quail[6])

print("===========")
## July 1st, 2021 testing bypass205 to see if it does three strings in a series
## thru the parser and codegenerator and puts it into stanford
	#THIS CALLS TEH CODE IN endswitch(y)
	#I need to empty stanford list right off the bat 
	#this will do thing fake switch nested just to get the mechanics understood July 1st 2021
	## right here we do 3 strings in succession
	#at the top here will be the quail list with three strings
	#empty stanford here to start from nothing
	###### empty stanford list here 
	
#this is ONLY called when there are more than ONE switch
#so an input switch string with nested switches(at least one) inside of it.
#and then the SNIFFER determines if regular switch or multi-combo switch with nesting

##=============================================
### REVERSE STANFORD LIST
##
##=============================================
def reverse_stanford_list(): #this just says what it does simply
	print("reverse_the_stanford_list ===")   
	stanford.reverse()#print stanford would have to have a length of 2 actually for a nested switch in a switch
	print("now reversed stanford list")
	print("now printing out the list showing the reversed order")
	# I don't need to print this out once it works
	# so I will commentout the three lines below soon
	#this is just so I can see what's actually in the stanford list to make sure it's correct
	print("== LOOPING THRU STANFORD LIST NOW ==")
	for item in stanford:
		print(item)
		print("==========")

# print("PRETENDING THAT THE LISTS HAVE BEEN MODIFIED THOUGH NOT REALLY YET")
#   print("==================")
#  print('lets pretend that the strings are finished and I will concat them together')
# print("but not run them")
#print("remember after the stanford list has been reversed the LAST list will be the main")
   
   
# JULY 10TH, 2021

### important - need to add methods inswitch and infallthu at top
toocool=[]
toocool.append(0)

output=[]
output.append(0)
#this loop sthru stanford list and concats each switch string together bottom up
##====================================================
##   BUILD STACKED CAKE STRING COMBINING STANFORD LIST
##====================================================
def build_stacked_cake_string_combining_stanford_list(): 
    print("========build stacked cake string by concatting  stanford list=========")
    count =0
    print("length of stanford insid eof build_stacked_cake =",len(stanford))
    ##  THIS LOOPS THRU STANFORD LIST 
    #concat_triple_string_before_and_after_switches_in_stanford_list
    genius="'''" + "\n\n"
    for item in stanford:
        genius += item
    genius += "'''"
    toocool[0] = genius
    for line in toocool[0].splitlines():
        print(line)
    #final_output[0]
    output[0]=toocool[0]    
    del stanford[:] #empty stanford here  just in case
    print("now  after build stacked cake string combinging stanford")
    print("stanford list should be empty",len(stanford))
    
    
###================================================================



    
def second_attempt():
    print("is this thing ON")
    volleyball =''
    print("===calling second attempt() ===")
    volleyball += "'''" #starter
    for item in stanford:
         #just added this dec 7 to see if needed 
        volleyball += "\n"
        volleyball += "#count="
        volleyball += str(count) + "\n"
        volleyball += item
        volleyball += "\n\n" #spacer 2 lines
        volleyball += "#============ divider =========== \n"
        count += 1
        print(count)
        #after loop is over
    volleyball += "'''" #after  just added this to see if it is right
    print('now doing the loop after finishing volleyball')
    for line in volleyball.splitlines():
        print(line)

#second_attempt()

tahoedream='''
global x
x = "one" #it was "one"     #<<=== x must be a string just as matching case == "string", 
                            #<<=== if using a number it will be converted to a string
                            #<<=== so x = 22   will work and be converted to "22"
tahoe=[]
tahoe.append(0)
'''


methods ='''
# ====  switch  
def switch(x):
    if type(x) != str:  
        x = str(x)
    global case
    case = x.lower() 
    
# ============  
def fallthru(y):
    eval("switch('" + y + "')")
#==================
def inswitch(n):
    if type(x) != str: 
        n = str(n)
    global case
    case = n.lower() 
#=====================
# for infallthru    
def infallthru(n):
    eval("inswitch('" + n + "')")
'''





main_function_switch='''

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
	

'''



bottom='''main_switch('1')''' #this calls it this triggers the generated code to run 

#exec(tahoedream)


# in a switch string.
#it doesn't count endswitches as switches 
#but I might count endswitches as a backup insurance parachute.

# this calls endswitch() on each item in quail list 
# these are the input strings that were separated from a switch with nested switches within
# that have been split up above and put into the quial list in the order of appearance
# with main first and the nested afterwards in order
# modified on July 10th, 2021
#=================================================
####======   BYPASS205() ========   ##############
##=================================================
# BYPASS205() takes in the quail list
# and outputs the stanford list of python switch cases code 
########### bypass 205 ########### july 1st 2021 testing starbucks in gilroy
def bypass205(y): #this runs the input strings thru parser and code gen 
	print("==== bypass205 test =======") #and puts them into stanford list
	del stanford[:] #this empties the stanford list
	#this loops thru quail and call everything that I normally do for an end switch
	for item in quail: # 0, 1, 2 #so it should call the parser and code gen three times
		y = item #this puts the contents of each string in quail into y 
		
		#everything below here is the same in parser code
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		mytrace("endswitch() bypass205  in switch_cat called")
		show_input_switch_string() #flag for testing this shows the input string
		###############
		parser_guts(y) #y is put in as a param to paser_guts(y) while looping thru quail list grabbing item(string)
		###############
		#check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
##################################################	
		#if baseline[0] != "nada": #means it converted to uppercase
		#	y = baseline[0]
		#	#else:   #added this else  and pass on June 16th
		#	#	 pass #this puts the input string from baseline[0] into y
		#####################
		#this checks if first case is a number like case 2: returning True if numbers 
		#flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
		#####################
		#print("if number in first case",valve[0])
		# the key is macro expansion is only called if numbers are True
		#if valve[0] == True:    #meaning numbers like case 12:
		#	macro_expansion(y); #checks if macros and expands them and converts numbs to strings
		#	y=None; del y; y = cray[0];
		#end if
		#####################################
		#flush_lists() 
		#parser_mode_1(y) 
###  end bypass205()  ##################  		

		
	## end of endswitch()
#testing proof of concept of bypas205 to do three generating strings and save them
#don't run them. Just add them to stanford list
def next_steps():
    print("next_steps().......... today is")
    print("this is next_steps() called")
    print("just do something else")
    print("this is where the next stage of conversion will happen")
######3===================================
#####=====================================
### so this is testing taking in strings and then translating into python with the module
### but I need to add an if else into endswitch governed by the switch count and endswitch count
# THIS IS TESTING AND ISN'T CALLED IN THE endswitch() ABOVE AS YET July 3rd.
#this is what calls it. 
#   made this function on sunday, dec 12th, 2021
##==========================================
##  def testing_input_to_run_thru_bypass205():  
##==========================================
def testing_input_to_run_thru_bypass205():
    print("==== testing_input_to_run_thru_bypass205(): ===== ")
    y=''
    del stanford[:] #just to be sure empty stanford first
    print("the length of stanford=",len(stanford))
    print('about to call bypass205() ======')
    print("first let's loop thru the quail list to see the beginning")
    print("LOOP THRU QUAIL LIST")
    for item in quail:
        print(item)
    print("so this is the input for the bypass205 that it will read")    
    #requires the strings in the quail list remember this is key
    #within bypass205() it will loop thru the quail list and get each switch string and
    #then call the parser(quail switch string)
    bypass205(y) #run the test data to see what it does and calls the parser and codegen 3 times
    print("the length of stanford=",len(stanford))
    print("=-- looping thru quail ==")
    for item in quail: #this is the original input
        print(item)
        print("----------")
    #go thru each switch string and get switch comment number
    print("====looping thru Stanford as it is now===")
    #bypass205 would generate the python code that is put into the stanford list 
    for item in stanford:
        print(item)
    print("----------")
    
#this triggers the test running of bypass205()
testing_input_to_run_thru_bypass205()

#what_is_in_stanford() #what is in the stanford list...to see the output python #this is the real test
# I just want to see the strings and proof that it worked 
#set these after exec
#after the stanford list is generated I can run a method over it
#and modify it to add the comment after each switch which I need
#to create the def nested switch number on top
#december 6th 8:41 opm



#loop thru test item to see that it works
#testing adding the switch number to the first one
testoutputstring='''
exp = varholder[0]

caselist1 = ['1', '2', '3']
caselist2 = ['4', '5', '6', '7']
caselist3 = ['8', '9', '10']
caselist4 = ['default']


switch(exp)
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

'''

########################################################################
########################################################################
#use this list in order top down starting from 1 to add number after switch
#switch_numbers_to_transfer  list
#this will be filled elsewhere
#I would take these two lines out when I combine the files christmas tree and this one.
print("testing inside of snoopy doghouse switch numbers to transfer")
print("that I imported from Linus file switch_numbers_to_transfer.")
print("switch_numbers_to_transfer=",switch_numbers_to_transfer)
#switch_numbers_to_transfer=[]
#switch_numbers_to_transfer=['1', '11', '15', '23', '31', '62', '66']

#switch_numbers_to_transfer=['1', '11', '15', '23', '31', '62', '66']   

#remember after these numbers are added I need to add teh def nested)switch
#and then the main)switch for the one with switch 1 (this one)
#and then I need to reverse teh switch to prepare it for bake cake method


#before
#for line in testoutputstring.splitlines():
#    print(line)
#created monday december 6th, 2021 gilroy  
#after
#switch_numbers_to_transfer[0] ##=['1'], for testing
silvermine=[]
silvermine.append(0)
number_counter=0
##===========================================================
##  add_switch_number_to_python_output_from_quail_input():  #adds switch number to each python output string
##  this uses list switch_numbers_to_transfer
##===========================================================
def add_switch_number_to_python_output_from_quail_input(testoutputstring,number_counter):
    print(" ===add_switch_number_to_python_output_from_quail_input(testoutputstring): === ")
    createstring=''; # this test is ONLY doing one call of this function 
    counter=0        # so it should work as switch_numbers_to_transfer[0]
    for line in testoutputstring.splitlines():
        if "switch(exp)" in line and "nested" not in line:
            print(line)  #next line accesses switch_numbers_to_transfer[counter]
            print("counter",counter)
            ########################################################################
            print("this is what it sees",str(switch_numbers_to_transfer[number_counter]))
            ########################################################################
            createstring += line + "#" + str(switch_numbers_to_transfer[number_counter]) + "\n"
            counter += 1
        else:
            createstring += line + "\n"
            counter += 1
            continue
    print("the output after adding the switch line number after switch")
    for line in createstring.splitlines():
         print(line)
    #this puts the output of the method above into silvermine[0]    
    silvermine[0]=createstring #for output to replace it into the same slot
 ####====== end of fucntion         
 
#number_counter=0
#add_switch_number_to_python_output_from_quail_input(testoutputstring,number_counter)
#this is after
#for line in silvermine[0].splitlines():
#    print(line)
#



# get first line with switch get the number after comment
# append that number to a list
#first_switch_list.append(number)
got_the_number=[]
##====================================================
##  get_switch_number_at_top_of_string(stringname):
##====================================================
def get_switch_number_at_top_of_string(stringname):
	print("=========get switch number at top of string().========. called")
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




##==========================================================================
xmastime=[]
xmastime.append(0)
#testing december 2, 2021 4:38pm snowman coding project
#this will be called just before bake_cake combinging the switches together happens
#this would be called on each string in stanford list ##<< important note

# this creates the "def main_switch(exp):" and 
# def inner_switch_x(exp): and converts the inner switches to inswitch and fallthru to infallthru 
# verified working dec 3rd Friday 2021 Starbucks Gilroy.
####=======================================================================
##   prepare_python_switch_string_for_baking(stringname):
##   #method used: result= get_switch_number_at_top_of_string(stringname)
##========================================================================= 
def prepare_python_switch_string_for_baking(stringname):
    print('===== prepare_python_switch_string_for_baking() =====')
    buildstring='';
    the_answer_is= get_switch_number_at_top_of_string(stringname)
    mynumb = the_answer_is;
    #========================== added on Fri Dec 3rd ====================
    ## this  ADDS the function name to the top  of a switch string; not tabs in front here
    if mynumb == '1': 
        buildstring += "\n\nexp = varholder[0]\n";
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


##==============================================================
##  loop_thru_stanford_list_and_add_number_to_each_switch():
##==============================================================
def loop_thru_stanford_list_and_add_number_to_each_switch():
    counter = 0;number_counter=0;
    for item in stanford: #this loops thru the whole stanford list and adds a number to each switch
        print('number_counter=',number_counter)
        add_switch_number_to_python_output_from_quail_input(item,number_counter) #gets teh number from switch_numbers_to_transfer
        result = silvermine[0];fancy_new_car.append(result)
        number_counter += 1


fancy_new_car=[]


##==================================================
##  loop_thru_fancy_new_car()    
##==================================================
def loop_thru_fancy_new_car():
    for item in fancy_new_car:
        print(item)


##==================================================
## fill_stanford_list_from_fancy_new_car()    
##==================================================        
def fill_stanford_list_from_fancy_new_car():
    del stanford[:]
    for item in fancy_new_car:
        stanford.append(item)

##==================================================
## loop_thru_stanford_list()   
##==================================================        
def loop_thru_stanford_list():
    for item in stanford:
        print(item)


##==================================================
##  show_output_after_switch_number_added_to_python_output_strings()    
##==================================================        
def show_output_after_switch_number_added_to_python_output_strings():
    loop_thru_fancy_new_car()  #output of switch number added to a python switch string 
    fill_stanford_list_from_fancy_new_car()
    loop_thru_stanford_list()
####============== new test down here now ========================================
#### fresh morning coding     tuesday dec 7th, 2021 morgan hill
####################################################################################




#uses method add_switch_number_to_python_output_from_quail_input()
##===========================================================
## add_number_after_top_switch_in_stanford_list():  #modified and streamlined with methods on Dec 12th, 2021
##  MAJOR METHOD 
##===========================================================
def add_number_after_top_switch_into_stanford_list(): #python output strings
    print("=====add_number_after_top_switch_in_stanford_list():=====")
    loop_thru_stanford_list_and_add_number_to_each_switch()#after switches with numbers
    show_output_after_switch_number_added_to_python_output_strings() #in stanford list
    
        
#just commented this out
#add_number_after_top_switch_into_stanford_list() #this does the entire stanford list 
#which it loops thru 


print("first test of prepare_python_switch_string_for_baking(stringname) ")
print("prepare for baking the cake coming up fast ")
#big test here on december 7th a day that will live infany for when Japan attacked the USA
#testing framing just the first switch string which is main
#what this does is create a frame and method at top of each output python switch string
##@@@@@@@@
#add_number_after_top_switch_into_stanford_list()

#this was a test here of one stirng
#stringname = stanford[0] #which is the first one for this test
#prepare_python_switch_string_for_baking(stringname)
#print('the result is in xmastime');print(" ")
#for line in xmastime[0].splitlines():
#    print(line)     
#print('second phase of this baby now on Frosty cold raining morning') 


##==================================================
## loop_thru_bad_dog()    
##==================================================
def loop_thru_bad_dog():
    print("length of bad_dog line 12344=",len(bad_dog))
    for item in bad_dog:
        print(item)
      
      
        
##==================================================
##  fill_stanford_list_from_bad_dog()   
##==================================================
def fill_stanford_list_from_bad_dog():
    del stanford[:]  #fill stnaford list
    for item in bad_dog:
        stanford.append(item)
    print("stnaford list here is __",len(stanford))


##==================================================
##  reverse_bad_dog_list()   
##==================================================
def reverse_bad_dog_list():
    bad_dog.reverse() 
  


##==================================================
## say_what_it_is_doing_comment_as_print()    
##==================================================    
def say_what_it_is_doing_comment_as_print():
    print("bad dog list of final output of all nested switches and main switch")
     
     
     
##==================================================
##  take_bad_dog_list_and_fill_stanford_list()    
##==================================================
def take_bad_dog_list_and_fill_stanford_list():
    loop_thru_bad_dog()
    reverse_bad_dog_list()
    fill_stanford_list_from_bad_dog()
    del bad_dog[:] #new today dec 13th
    say_what_it_is_doing_comment_as_print()
    loop_thru_stanford_list()
####################################################################################
bad_dog=[]
#uses method prepare ptyhon switch string for baking 
#appending output to bad dog of adding def method at top of each switch string






##========================================================
## adding_def_methods_to_top_of_each_switch_string():
## ** MAJOR METHOD **
##========================================================
def adding_def_methods_to_top_of_each_switch_string():
    print(" =====adding_def_methods_to_top_of_each_switch_string(): ======")
    for item in stanford: #what does this do 
        prepare_python_switch_string_for_baking(item) #concats each switch string together (sewing together)
        bad_dog.append(xmastime[0]) 
    take_bad_dog_list_and_fill_stanford_list()
    
    
 ###================ end of function ===============
 
##@@@@@@@@
#adding_def_methods_to_top_of_each_switch_string()    



#exit()
print("about to concat the stanford list")
print("==== VOLLEY BALL TIME ============")
print("this is the outut of the layered cake I just built ==")
print("this is the output in the string volleyball")
print("VOLLEY BALL OUTPUT of the concatted python switches that need to be put")
print("into a triple string list I just remembered so that I can execute it")
print("about to call build_stacked_cake of strings of generated switches in mainswitch and nested_switches")
##=====================================================================
fill_nested_switches_list=[]
fill_nested_switches_list.append(0)
#this is going to be used to pass the generated combined switch
# string of nested and main switches bottom up from main
#which is then passed to concat and execute.
 
 
 
####################################################################################
#uses method build_stacked_cake sring combining stanford list()
#output is in toocool[0] list
##=============================================================
## stack_the_cake_combining_python_switch_methods_together()
## ** MAJOR METHOD ** 
##=============================================================
def stack_the_cake_combining_python_switch_methods_together():
    print("=====stack_the_cake_combining_python_switch_methods_together()=======")
    toocool[0]=''; 
    print("length of stanford before stacking the cake",len(stanford))
    #this loops thru stanford list
    build_stacked_cake_string_combining_stanford_list() #this adds ''' above it and ''' below it
    #prints out combined concatted together main and nested methods 
    #for line in toocool[0].splitlines():
    #    print(line)
    fill_nested_switches_list[0]= toocool[0]
    #This is used to concat other parts of strings to exec(superball)
    #in test file playtime_testing.copy
 ##@@@@@@@@
#stack_the_cake_combining_python_switch_methods_together()
   
print("done running trhu toolcool[0] wednesday monrning decmeber 8th after dentist")
##=================================================================
## the_big_test() #this goes thru each switch string in stanford list
## and adds switch number from quail strings in transfer_switch_list
## then adds def main method and def nested_switch_X
## reversing order so main is at the bottom 
## then concats the strings together within '''
##=================================/==============================
####################################################################################

## methods used:
## add_number_after_top_switch_into_stanford_list()
## adding_def_methods_to_top_of_each_switch_string() 
## stack_the_cake_combining_python_switch_methods_together()


##===============================================================
## create_def_switch_methods_concatted_together_in_one_string()
##=============================================================
def create_def_switch_methods_concatted_together_in_one_string():
    #possibly empty stanford list here 
   
        
    print('=create_def_switch_methods_concatted_together_in_one_string()=')
    add_number_after_top_switch_into_stanford_list()
    adding_def_methods_to_top_of_each_switch_string() #framing each python switch generated output
    stack_the_cake_combining_python_switch_methods_together()
    print("#end of big testaroo dec 9th thursday morning before 10am")
    #output is a string inside of list toocool[0]

#this is the trigger to put switches into defs and concat them altogether
print("when is this called snoopy_doghouse======= ")
create_def_switch_methods_concatted_together_in_one_string()  #omy god will it work 

#but the output string is in list toocool[0]
#exit()  


#output is on thursdya dec 9th at 9:43 am 

#end of big testaroo dec 9th thrusday mroning before 10am


###==========================================
fool = toocool[0]    
#see if I can look in it
rad = fool.count("nested_switch")
print("number of rad=",rad)
    
print("this is after calling: build_stacked_cake")
#next_steps()
#reverse_stanford_list()
#managing_nested_switch_scenario() #this just checks if the stnaford len > 0



print("I am exiting it here for testing dec 4th")
#exit()
    
#=== july 6th, 2021 addition to faciliate building the concatted string
# this reversing the python list is because I have to build
# the layered cake with the main switch at the bottom and this way
# I have the main switch last in stanford[-1] so when I build the cake
# each switch case in the list is added in order top down with the main
# switch being the last one. stanford[-1]
###  THIS IS WHERE I AM REVERSING THE STANFORD LIST OF SWITCHES
###  TO FACILITATE BUILDING THE LAYERED CAKE TOP DOWN  WITH MAIN SWITCH 
###  AT THE BOTTOM WHERE IT'S SUPPOSED TO BE.
#reverse_stanford_list() #this is so that they are in the correct order for the code to run

##==================================
##  building stacked cake string


	
# july 6th, 2021  
### all of the switches in the stanford list except the last one
### need to be converted to be inside of a nested_method 


#I still need to put the nested switches into the method names which are numbered

	

	



#this is the final output of the python generated strings in def main_switch and def nested_switchX
#=====stack_the_cake_combining_python_switch_methods_together()=======
#========build stacked cake string by concatting  stanford list=========

#end of big testaroo dec 9th thursday morning before 10am