# -*- coding: utf-8 -*-
#from bugsbunny import * 

#from goldfish import switchcasetester
#import switch_config  #what do these two imports mean and do?????
#import switch_subfile

#import sw_module_extra


#bugsbunny.py
#march 18th, 2021
global sw
varholder=[]
#def flush_lists():
#	varholder=[]
varholder.append("zilch")

#case_main_body_list_with_tail =[]

#experimental

valve=[]
var2=[]
var2.append("zilch")
starbuckslist=[]

# I have cases lists up to 1000
# you can add more but they must be in order and spelled correctly.
# python won't correctly dynamically generate them unfortunately.

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
	listname=[]

  
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
def swap_thru_lines_with_expanded_cases():
	## https://www.youtube.com/watch?v=_CzJ5bdRDU4
	#import pudb; pu.db  #added at point you want to start debugger
	
	mytrace('swap_thru_lines_with_expanded_cases()')
	global switchcasetester
	print("=========testing case_numbers_to_strings===january 5th 2020====")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
			print(" ")
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			# this is where it gets number that is now a string
			cat =is_number(smart[1])  #calling method to check if 
									  #the case name is a number
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
	#after the numbers have been converted into strings



###////////////////////////////////////////////===========
    

list_with_thru_macros=[]
list_with_thru_macros.append(0) #position 0 nothing
backwards_thru_list =[]  #initializing the list

#### ### this needs to happen first 
################ case 1 to 10: becomes case 1 thru 10:######################
######################################################
#### change to into thru ()       created friday feb 5th, 2021 morning
######################################################

#########################################
def change_to_into_thru():  #this is a simple way of doing it
	mytrace('change_to_into_thru()')
	print("change macro to into thru")
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
		
		





def make_list_of_lines_using_thru_macro():
	mytrace('make_list_of_lines_using_thru_macro()')
	print("=====WARNING WILL ROBINSON LOST IN SPACE====")
	print("* * * * WORKING ON FUNCTION make_list_of_lines_using_thru_macro()")
	print("===----------=== make list of lines using thru macros() ====--------=")
	#go thru list and if thru in line add that line to list
	global mouse
	thru_counter = 0
	for line in switchcasetester.splitlines():
		#just added the word to that means the same thing as thru
		if  "case" and "thru" in line:  #on
			list_with_thru_macros.append(thru_counter)
			thru_counter += 1
		else:
			thru_counter += 1
			continue
	print(list_with_thru_macros)		
	#then I need to reverse the list
	backwards_thru_list=list_with_thru_macros
	backwards_thru_list.reverse()
	print("backwards we have",backwards_thru_list)
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
	global mouse
	global opal
	opal = ''
	mycounter = 0
	print("value of mycounter should be zero",mycounter)
	for item in backwards_thru_list: 
	#set mycounter to a number for line in mouse.splitlines() : #this goes thru the mouse string
		print(line)
		
	
	

####=========== test here concatting little chunks for the switch case


smart =''
beta =''
opal=''
import re
foolish =''
newline=''

##############################################################################
#################### case_numbers_to_strings() ###############################
##############################################################################
######  converts numbers to strings case 1: to case '1': #####################
##############################################################################
def case_numbers_to_strings():
	mytrace('case_numbers_to_strings()')
	global switchcasetester
	print("=========testing case_numbers_to_strings===january 5th 2020====")
	print("========  CASE NUMBERS TO STRINGS  ====")#go thru the entire string
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			print(cat)
			cool = smart[1][:-1]  #chops off : from end
			holder = "'" + cool + "'"
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
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





# 
# 	return switchcasetester
# 
# def romanwall(j):
# 	print("=======romanwall called=====")
# 	I might have to concat it and make it into
# 	virgin reutrn switchcasetester = '''
# 	it might have to be generated and then eval(string) or exec(string)
# 	supertramp= j
# 	switchcasetester= j  #seeing what happens
# 	print(supertramp)
# 	see if it can read what is in the string
# 	just testing what I can do here with the string
# 	answer =supertramp.count("case")
# 	print("the number of cases in this string =",answer)
# 	print(switchcasetester)
# 
# def adjust_input(x):
# 	print("adjust input called with", x, "inside of yosemite")
# 	newstring =varholder.append(' + x + ')



	


#varholder=[]
#varholder.append("walmart")  #position 0  varholder[0]
#varholder.append("0")      #position 1
# =======   testfunction    ========================
exp=''








coyote_list=[]  #initialize it
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
	

#########=============== get last break in string ==================
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
	mytrace('convert_default_case_2')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location_2()
	last_break=get_last_break_in_string_2()
	
	
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




def stage_one_2():  #this calls start_trigger()
    #print('stage one')
    start_trigger_2()

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
digitalcandy=[]
line_numbers_of_first_cases=[]
        #####this is where i'm testing now
def magictimenow_2():
	mytrace('magictimenow()')
	#This makes a list of true if case in line and false if no case in this line
	#print("first fillup a list with true and false")
	#print("true if case in this line and false if not")
	#print("=== simple test if case in a line if so then True")
	#print("=== and if no case in this line then put False")
	#print("these true and false go into list called ifcaseinline")
	ifcaseinline=['starter']   #theresult
	#this loop puts true into ifcaseinline if case in this line otherwise it puts false
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		if "case" in line:
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


	
	thecounter=0
	for item in trontime:
		#print(item,thecounter)
		thecounter += 1

	#print("now this is new virgin code to detect a case that is the first case")
	#print("and this is done by also checking if the line above tested False for having a case")
	firstcaselist=[]
	#print("========here we do some more HALLOWEEN testing============")
	#print("-----this is getting the first case in each section to use in fallthrus-----")
	#this is designed to detect the first case in a case section by detecting a case
	#that does not have a case above it making it by definition the first case
	#now this means no blank spaces between lists of cases for this detection to work.



	#this is where the line_numbers_of_first_cases list is filled with the line number of first cases
	 #nuked 'starter' from it
	acounter=0
	#what this does is look in the current line for the word "case"
	#and looks in the trontime list for the line above the current line to make
	#sure that "case" is not in the previous line determined by the word 'false'
	#the trontime list only has trues and falses so true if case in line otherwise false
	for line in switchcasetester.splitlines():
		#this checks if case in this line but no case in line before it
		#the tricky part of this solution is that it is looking above the current line
		#trontime list holds true and false depending on if 'case' in that line number
		if "case" in line and "case" not in trontime[acounter-1] :  #tests if no case above this line with case
			#print('the line number is',acounter)
			line_numbers_of_first_cases.append(acounter)

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

			genius = line.split()

			firstcaselist.append('default') #this should grab the case name
			#print('default found')
			acounter +=1
			continue
		else:
			acounter +=1
			continue



	smartnewlist=[]

	for item in firstcaselist:
		if item != "default" :
			item = item[1:-1]
			smartnewlist.append(item)

		if item == "default":
			smartnewlist.append(item)







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

def cotton_candy_2():
	mytrace('cotton_candy_2')

	answer=''
	for item in range(1,len(case_main_body_list)):
		
		item = item.strip()

		
		answer =item.count('\\t')
		answer = ''



def stage_two_2():
	mytrace("stage_two_2")
	print('stage two_2')
	#cotton_candy_2()

#cotton_candy()


'''
	print("about to copy practicestring1 into sweetlist")
	#this goes through the practicestring1 string using a loop and appends each line into sweetlist
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









#truckeeriver()

def stage_three_2():
    print('stage three_2')
    mytrace("stage_three_2")
    truckeeriver()








# 
# 
#     print("the length of the new shortened list =", len(new_c_list))
#     this is my solution for list out of range bull bug
# 
# 	if (len(new_c_list))% 2 == 0:  #this would only be done once and modify the list
#     to manipulate.
# 		pass
# 	else:
# 
# 		new_c_list.append('nada')








# 
# 
# 
# 
# print("okay the fun starts here =======>>>>>>>>")
# 
# this figure out the number of case sections (number of case ifs really)
# it goes through the coyote list and checks if a line contains case and the next doesn't
# this works  july 30 2020
# counter =0
# casecounter = 0
# list_of_cases =[]
# while counter < len(new_c_list):
#     print(get_starting_position_in_coyote(counter)) #position 0
# 
#     if new_c_list[counter] == "case" and new_c_list[counter +1] != "case": #this represents the bottom of case set group
#         counter += 1
#         casecounter += 1;
#         continue;
#     else:
#         counter += 1
#         continue;






#line_numbers_of_first_cases
#look at this force feeding it input i need to find the generation of the inputlist
#theinputlist =[2,7,17,24,34]  # case case case case default   I took off 36 default
total = len(line_numbers_of_first_cases)
def rule_the_earth_2():
	#print("rule the erath called at 940")
	mytrace("rule_the_earth_2")
	#this is to get the first case of each section
	#print('======= ***** ===========rule the earth ==== creates starbucks list === *******  =====')
	print("debugging inside of rule_the_earth_2()")
	mycounter =0
	second_word=''
	theline=''
	#print("the input to figure out the first case in each list inputlist list =",line_numbers_of_first_cases)
	## go thru digital list of the case locations
	## it will be the x position that's easy enough
	bestbuy1 =''
	bestbuy2 = ''
	mochalist=[]
	greenmilelist=[]
	test1 =''
	test2 =''
	print("line numbers of first cases",line_numbers_of_first_cases)
	
	#breakpoint()
	##for case sets I just go thru till case not in line and fill a new list
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		print("line_numbers_of_first_cases",line_number_of_first_cases)
		if mycounter in line_numbers_of_first_cases:
			#print(line)
			felix= line.split()
			print("********* BUG IN HERE_What does felix list =")
			print("felix=",felix)
			
			print("========== LOOK IN HERE ")
			if "default" in line:
				second_word = line.split()[0]

			else:
			#the bug is apparentlyhere
				print(line)
				second_word = line.split()[1]



			#======================  thursday surgery cleaning up the words 'words'
			wild= second_word[1:-1]
			#print("wild=",wild)
			wild = "'" + wild       #adding a ' to left side of word
			darn = wild[1:-1]
			wild = darn
			second_word = wild
			#=======================
			if second_word != "default": #this is new
				starbuckslist.append(second_word)

			if mycounter == total:
				break
			else:
				mycounter += 1
		else:
			mycounter += 1
	starbuckslist.pop()
	starbuckslist.append('default')
	print("starbuckslist=",starbuckslist)
	



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

#what this does is take the input of teh [builder list] with line numbers
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

#uses input_list[2,7,19,26,36]
# THIS IS NEW FOR SUNDAY AUGUST 23, 2020 modified november 16th
# CONVERT TO TWIN LIST
def convert_to_twin_list_2():  #uses list called line_numbers_of_first_cases
    mytrace("convert_to_twin_list_2")

    #input_list -= 1 #true cases last number is default
    alpha = 0; beta = 1; counter = 0  #down below it was: length_of_input_list
    while counter < len(line_numbers_of_first_cases) -1:
        eval("list_trex.append(line_numbers_of_first_cases[alpha])")
        eval("list_trex.append(line_numbers_of_first_cases[beta])")
        eval("digitalcandy.append(list_trex)")
        alpha += 1; beta += 1; counter += 1
        list_trex=[] #resets list to reuse next loop

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
def special_addition_to_digital_candy_2():
	mytrace("special_addition_to_digital_candy")

	digitalcandy.pop() #delete last item sublist
	#print("digital candy after pop =",digitalcandy)

	#this gets the line number of the word default
	find_default = get_default_location_2()   #gets line number of default

	#this gets the line number of the closing brace (identical to last line of docstring)
	last_brace   = get_closing_brace_2()        #gets the line number of closing curly brace
	thelastbreak = find_last_break_in_string_2()#put it here
	mystring = str(get_closing_brace_2())       #puts closing brace line number in mystring

	#print("mystring=",int(mystring))
	#defaullist is populated with default line number and closing brace line number
	defaultlist.append(find_default)  #defaultlist[0] #default line number
	#defaultlist.append(thelastbreak)  #defaultlist[1] #break line number (if here)
	defaultlist.append(int(mystring)) #defaultlist[2]
	#print("these are regarding the input js switch case default break and curly brace")
	#print("default list numbers are: default, last break, curly brace",defaultlist)

	#so this means that digital candy should already exist and be populated
	#don't want to corruptthis it is only expecting two values not three
	digitalcandy.append(defaultlist) #these two are the parameters to look between
	#look_for_break_after_default(defaultlist)
	#this is new code to determine if missing break in default input section
	three_in_row=[]
	three_in_row.append(find_default)  #defaultlist[0] #default line number
	three_in_row.append(thelastbreak)  #defaultlist[1] #break line number (if here)
	three_in_row.append(int(mystring))
	a = find_default
	b = thelastbreak
	c = int(mystring)
	print("testing here before doing comparison")
	print("a,b,c",a,b,c)
	#I might need to call this first since it's a strange bug if a missing break
	#remember if there is no break then add it with replace
	if b > a:
		#print("==== testing if break AFTER default")
		print("there is a break in default")
	else:
		print("there is a MISSING break in default case")
		#print('there is NOT a break in default need to add one')
		#again this is adding a break in default to javascript switch case
		#because of an obscure bug caused by missing break in default
		#print("this is before adding break to default")
		#print(switchcasetester)
		#global switchcasetester
		orange=''

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

######################
##  stage_four_2
#######################
def stage_four_2():
	mytrace('stage_four_2()')
	#print('stage four')
	magictimenow_2()
	convert_to_twin_list_2()
	special_addition_to_digital_candy_2() #======added nov 25th, 2020
	rule_the_earth_2()






#================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0


#this is a super important function I think I wrote it at the beach a few days ago
def testing_this_to_get_word_2():
    mytrace('testing_this_to_get_word_2')
    print("======def ======testing this to get word() ==================")


    smartcounter=0
    #this looks for "case" in the switch case string
    for line in switchcasetester.splitlines(): #switch case in JS
        if "case" in line: #see if this puppy works
            firstline = line.split()
            print("line 1441")
            print(firstline)
            print(firstline[0])
            smartcounter += 1;
        else:
            smartcounter +=1;

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



#testing_this_to_get_word()  #==================this should call it now
######################
##  stage_five_2
#######################
def stage_five_2():
    #print('stage five')
    testing_this_to_get_word_2()




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

    print("royallist=",royallist)







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
                    print('teh default was 3 words case and two words')
                    ap =genius[1] + genius[2]
                    caseset.append(ap)
                    #print(caseset)
                    
                if len(genius) == 4:
                    print('teh default was 4 word case and 3 words')
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
                print(caseset)
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
    mytrace('case_trail_list_maker_2')
    #print("=######	C A S E    T A I L   M A K E R called  ")
    smartcounter=0
    #this looks for "case" in the switch case string
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
	mytrace('p51_mustang_2')
	counter = 0
	c = 1		#current case numbr section
	d = c + 1

	for item in digitalcandy:	#this is going through the diamonds list

		sea = digitalcandy[counter]
		x = sea[0]
		y = sea[1]
		##print("x",x,"y",y);
		case_tail_list_maker_2(x,y)
		counter += 1

	royallist.append('break');  #in default
	counter = 0

	#this goes thru the royallist with breaks and fallthrus(numbers)
	# starter 0  fallthru2 fallthru3 fallthru4  fallthru5 default
	#loops thru to royalist[item] then accesses the starbucklist[item to append
	# I can make fallthru('fish') and fallthru('default')  and have the formula working
	#I use numbering in royalist starter1(0) (position1 fallthru2)   (position2 fallthru3) etc
	#if they use big numbers I will put them inside of (number) and grab teh number startswith("(")
	#and endswith(")")
	print('royallist =',royallist)
	
	for item in royallist: #use range here 
	#for item in range(1,len(royallist)): #added march 16,20211:19pm
		if "break" in item:
			cranberries.append("break")

		if "fallthru" in item:
			item=item.strip()
			item =item[-1]
			#print("item=",item)
			item = int(item)
			#print(item)
			doggy =starbuckslist[item] #this is like fallthru('cherry')
			ohbaby = "fallthru(" +  "'" + doggy  +  "'" + ")"  #this is the number

			#print("ohbaby=",ohbaby)
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target



###############################
## stage_six_2
###############################
def stage_six_2():
    #print('stage six')
    p51_mustang_2()







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
	mytrace('flyingfish_2')
	mytrace('flyingcloud_2')
	x =''
	y =''
	thecounter=0
	# loops through diamonds list of case position to build the first case list
	# which is called starbucks
	z = thecounter #which is 0 by default above
	z += 1  #then it starts at 1
	for item in digitalcandy:
		x = item[0]
		y = item[1]
		flyingcloud_2(x,y,z) #z starts at 1 and adds 1 to z with each loop
		z += 1
		thecounter += 1

	nightowl_2()   #fills smartcasemanager





##==========================
##   flying cloud_2            this builds a list of the case names for each section
##==========================
smartcasemanager=[]
smartcasemanager.append("['starter']")
def flyingcloud_2(x,y,z):
	words=''
	
	#print("===========FLYING CLOUD =============")
	#print("flyingcloud_2 called; this builds a list of the case names for each section")
	mytrace('flyingcloud_2')

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
				
			if words == 4:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3] 
			
			if words == 5:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] 
				
			if words == 6:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5]
				
			#print(" wilderness has in it", wilderness)
			#print("=====firstline[1] ====== line 2009 =======")
			#print("wilderness=", wilderness)
			wild= wilderness[1:-1]
			#print("wild=",wild)
			wild = "'" + wild  #adding a ' to left side of word
			darn = wild[1:-1]
			wild = darn
			#print("wild now is",wild)  this reduces it to a string 'word'
			# will need to use the case or counter number and
			# use eval to just do this with one if
			eval("caselist" + str(z) + ".append(wild)")

		else:
			if "case" not in line:
				break


einstein=[] #resets einstein to empty
	#========================================
#this fills up smartcasemanager list
###############################
## nightowl_2
###############################
def nightowl_2():
	mytrace('nightowl_2')


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



###############################
## stage_seven_2
###############################
def stage_seven_2():
    #print('stage seven')
    flyingfish_2()


wilson=''
mystring =''

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








#======== sutterrsmill==============================
case_main_body_list=[]
case_main_body_list.append('starter')  #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code


###############################
## big_gears_filling_list_with_case_bodies_2()
###############################

def big_gears_filling_list_with_case_bodies_2():
	mytrace('big_gears_filling_list_with_case_bodies_2')
	#print("================big gears filling list with case bodies called==========")


	counter=0
	for item in digitalcandy:  #=[[2,14],[14,26],[26,33],[33,3],[38,43],[43,47]]
		#print(item[0],item[1])

		counter += 1
		#print("counter=",counter)
		smarty_2(item[0],item[1])  #snowtime is called here
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
	loop_thru_case_sections_2()


icecream=''
###############################
## herewego_2()
###############################
def herewego_2(): #loops and prints all main bodies
	mytrace('herewego_2')
	#this loops through the case_main_body_list and prints the case python code
	#print("here we go () called it prints the case body code from the list ")
	#mightymouse = "happy"
	#print("======= here we go() called =======")

	counter=0
	#print("length of case body list =", len(case_main_body_list))
	#print(case_main_body_list)
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
	big_gears_filling_list_with_case_bodies_2()
	herewego_2()


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
	print(" this prints out the contents of the important lists")

	print("==============================================")
	print("digitalcandy list ========")
	for item in digitalcandy:
		print(item)

	print("starbucks list ====of first case names in each section ====")
	print(starbuckslist)

	print("smartcasemanager list ========", len(smartcasemanager))
	for item in smartcasemanager:#
		print(item)

	print("case_main_body_list list ========", len(case_main_body_list))
	for item in case_main_body_list:
		print(item)
	#=== code gen here ====

###############################
## stage_ten_2()
###############################
def stage_ten_2():
	mytrace('stage_ten_2()')
	#print('stage ten')
	make_case_sets_2()
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
	parktime_2()


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
	mytrace('switch_code_gen')

	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.


	 #name of  generated docstring switch_python_gen
	#print("varholder.append(exp)")
	#this is the final input code of switchcasetester
	#print("================== finalized input of switch case code =======")
	print(switchcasetester) #to see what it sees

	#remembering one is printing
	#the other is generating (and printing to see it)
	#before it's executed the python switch case form


	##############
	topvars2 = "\nexp = varholder[0]\n\n"


	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:

	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(smartcasemanager)-1
	###################################################
	#   this is printing out the caselists at the top
	###################################################

	#--- testing dec 24th for varholder[0] input word ----
	#------------------------------------
	top_input_of_exp = "exp = varholder[0]"
	# "varholder.append(exp)\n" +
	print("varholder[0] =",varholder[0])
	#how do I determine if it's empty

	if not varholder:
		print("List is empty")
	else:
		print("varholder has something in it")
		print(varholder)
		#-------------------------
	# this prints the case lists of the words in each case section
	#print("------- testing what is in each list dec 3oth -------")
	#print("einstein list",einstein)
	#print("====-=====")
	#print("firstcasemanager list",smartcasemanager)
	#print("-----------------------------------------")
	## ===========  LOOP =============
	#add default to end of einstein; this is because there is no actual default case
	#it's used as a lifesafter in case someone wantsto fallthru into default
	#I decided to create a default case but in the input it's not there

	einstein.append("default")  #adding default to the end of einstein copy list
	
	#print('after the appending of default we have..')
	#print("einstein list",einstein)
	#print("----------------")
	for item in range(1,len(einstein)):     #first loop was smartcasemanager
		trains =  str(counter)
		merge = "caselist" + trains    #caselist1
		toosmart = eval(merge)
		###########################
		if int(trains) < 10: #adds another space to line up output list
			caselist = merge + "  = " + str(toosmart)    #this is the caselist name we eval to display it
		else:
			caselist = merge + " = " + str(toosmart)    #this is the caselist name we eval to display it
		###########################
		testlist.append(caselist) #trying a hunch here
		######################
		#inside1 = caselist  #this is only apparently capturing the last one
		#####################

		counter += 1
		numb += 1
	#after loop finished we have the caselists generated captured inside of 
	

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
	for item in range(1,len(case_main_body_list)):       #second loop
		if mycounter == 1:
		#============  first section case=============

			first_if= tabs[1] + "if " + front+str(mycounter)   + ": #"
			toosmart = eval("caselist" + str(mycounter))

			newlist = [first_if, toosmart]


			###########################
			sofrustrated =str(newlist[0]) + " " + str(newlist[1]) #=== only catching last one==
			extremelysmart.append(sofrustrated)
			###### firstpart adding if line ###########
			firstpart.append(sofrustrated) #this feeds the if line into first part list



		else:    #rest of cases after first case ======
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber


			caselistline = str(newlist[0]) + " " + str(newlist[1]) #=====
			extremelysmart.append(caselistline)
			firstpart.append(caselistline) #this ffeeds elif line into first part list

		######################
		#=== second part of each case section
		weasel= case_main_body_list[mycounter]
		secondpart.append(weasel) #this feeds the string body into secondpart

		######################
		#=== third part of each case section
		#this is the tail either break or fallthru(name)
		crans =tabs[2] + cranberries[mycounter]  #=====
		thirdpart.append(crans) #this feeds the tail into thirdpart


		mycounter += 1     #loop counter
	###===== this is for the ELSE: at bottom of switch case
	#this is the default section else
	# end of regular cases
	#=== END LOOP  =========================

	################
	theelse = tabs[1] + "else:"  #this is just once
	firstpart.append(theelse) #this feeds the else clause into first part
	#this is the last real case after the regular caes

	##################3
	 #last case body for default

	lastishcase =case_main_body_list[-1]

	secondpart.append(lastishcase)  #this feeds the body into secondpar

	##########################
	trying = tabs[2] + cranberries[-1] #=====
	thirdpart.append(trying) #this feeds the tail into thirdpart


	#practice printint out the three tier cakes for each section
	#print("below this line is the concatted output in strings")
	#print("first is the castlists from the top")
	#this works this creates the strings of the caselist at the top above switch correctly
###============================================
# caselists concatted to string cool
	cool=''

	#== LOOP === these are stored in list called testlist
	for item in testlist: #to see if the caselist names are in here  in this list
		cool += item + "\n"
		#print(item)
	#print("this is printing the string of each case from cool")
	cool += "\n\n"

	#===case sections three parts at once ==")
	rocks=''
 #=====================
 #== LOOP
	output_list=[]  #adding this list to capture content body of each case to return an output 
	output_list.append('starter') #filler for position 0
	counter =0  #each section will have the same number of items
	for item in firstpart:
		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n" +str(thirdpart[counter]) + "\n\n"
		#eval("output_list.append(" + '"' + str(secondpart[counter]) + '"' + ")" )
		counter += 1
		#printing out the three part case sections")
		#putting content of a case in here
        
	#a -----main list so sublists in the main list
	# so I only use ONE LIST for all three
	#adding strings together here

	sweet = topvars2 + cool + switchy + rocks
	#for debugging I will have a flag here to see output and test separately for user
	#print(switchcasetester)
	
	#this is new it shows the generated code
	if show_py_switch[0] == True:
		print(sweet)
	else:
		#print('not showing generated python switch case code since flag = False')
		pass

	#print('testing executing generated string of code...')
	#print(" =================")

	exec(sweet)  #this is the building of the string of python code strings
	
	
####################################################


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
	pass

































#######################################
##  convert_case_numbers_to_strings()
#######################################
def convert_case_numbers_to_strings():
	#print("convert_case_numbers_to_strings() called ")
	mytrace('convert_case_numbers_to_strings()')
	global switchcasetester
	make_list_of_lines_using_thru_macro()
	expand_thru_macro()
	case_numbers_to_strings() 

#this is reading numbers in cases NOT STRINGS and converting them into strings

#this is new but I haven't tried it yet december 5th
def starter_sequence_mode_2():
	mytrace('starter_sequence_mode_2()')
	#this ensures that these are ONLY called if valve[0] is True
	if valve[0] == True: #meaning numbers in cases detected
		print("== in starter_sequence_mode_2 and valve[0] = True  ====")
	
		#print("this is starter_sequence 2")
		global switchcasetester
		#this is the only line I need to put into faucet_valve() in march_firefall_yosemite_falls
		convert_case_numbers_to_strings()
		#print("this is where the true parser starts..")
		#print('')
		stage_one_2()
		stage_two_2()
		stage_three_2()
		stage_four_2()
		stage_five_2()
		stage_six_2()
		stage_seven_2()
		stage_eight_2()
		stage_nine_2()
		stage_ten_2()
		stage_eleven_2()
		#print("now code gen time..")
		switch_code_gen_2() #it's called right here
		stage_twelve_2()
		
		flush_lists()
		#this clears them out sw and switchcasetester
		global sw
		sw = ''
		global switchcasetester
		switchcasetester=''
		smartcasemanager=[]
		print("smartcasemanager=",smartcasemanager)
		british=[]
		penguin=[]
		clear_out_all_case_lists()
		#print("function trace path Tron..")
		#show_tron_trace_path() #this shows the function/method trace path top down
		
	else:
		pass
daisy=''
def parser_mode_2(a):  #in snoopy1.py
	mytrace('parser_mode_2 in snoopy1()') #was greatpumpkin
	print('=======INSIDE OF PARSER in snoopy1  =========')
	#felix()  #testing with switchcasetester string
	mountain2(a)    # this changes sw to switchcasetester #I can't beleive that this reverse number was being called 
	starter_sequence_mode_2()


##############  added April 2nd, 2021  ###############################################
# this is a pre scan of the switch case input string to determine if


# this gets the line number of the first case in the switch case string



# flow_fork_input()  #this fills valve[0] with True or False
# if valve[0] is True  it means numbers = True  (thus numbers      )
# if valve[0] is False it means numbers = False (thus words strings)
## the new code will go in here Friday morning.. April 2, 2021
#this fills valve[0] with True or False for numbers in cases



#this fills valve[0] with True or False
#based on analyzing the switch case string first case if number or not
############################
#this controls calling numbers parser if True
#this controls calling words   parser if False
#this is in great_pumpkincat2.py




	
#this will need to be called for each specific thru line
###==============================================================
###================  expand_thru_macro()  ===================
###==============================================================

inputnum = 1
def expand_thru_macro():
	mytrace('expand_thru_macro()')
	print('expand_thru_macro called')
	global switchcasetester
	#print(switchcasetester)
	change_to_into_thru()   #<====== this is where "to macro" swapped with "thru" in switch case input
	newlist=[] #resets newlist
	global mouse; global ajax; global snowy; snowy=''
	mycounter = 0 ### mouse 
	for line in switchcasetester.splitlines():  #doing mouse not doing switchcasetester yet
		#beta = mycounter-1
		#reinitialize what I'm using with each loop iteration
		smart=[]; ajax=''; newlist  =[]
		#this is the bug fix so I say if "thru" in line but NOT "fallthru" in line.
		if "thru" in line and "case" in line and "fallthru" not in line:  #only used with numbers
			print(line)
			if ":" in line and line.endswith(":"): #referring to one : in line
				line = chomp(line) #moved taking off colon here  line=line[:-1] 
				print(line)
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
			#print('newlist sees contents',newlist)
			ajax =''
			#print("length of list =",len(newlist))
			#print("this is GENERATED case code from macro with 2 prefix tabs") 
			#this is reading out the contents of the cases one on each line
			
			##==============================================================
			# LOOP ====================
			#print("just took out  + "'" + str(item)  + "'" + 
			for item in newlist:  #this list has the number in it
				ajax += "\t\tcase " +   str(item)   + ":" + "\n"
				#now delete last \n on end 
			#print("==== big test of replacing it ====")
			ajax = ajax.rstrip() #see if this works takes off last "\n" whcih was extra
			ajax = ajax[:-1] #chops off last char on end which is the :
			#this is where the expandef macros is inserted in the line with "thru"
			#print("this is expand thru macro in pumpkin-falls line 286")
			#print("right here== ajax  is",ajax)
			snowy=switchcasetester.replace(line, ajax)
			switchcasetester='';switchcasetester = snowy
			#print("=== testing $$ this is the result of the macro thru unfurled")
			#print("=== testing $$ the unfurled macro should show up")
			#print(switchcasetester) #was mouse here 
			#return ajax
			
			
	
	################################
	########### CHOMP(x)  ##########
	################################
	## this bites off the last character in a string ##
def chomp(x):
	mytrace('chomp()')
	#print("====== chomp called",x)
	x = x[:-1] 
	print("x=",x)
	return x


#def make_some_case_lists():
#	mytrace('make_some_case_lists()')
#	i =1
#	while i < 1000:
#		print("caselist" + str(i) + "=[]")
#		i += 1

#make_some_case_lists()
	
#starter_sequence()

#this way starter_sequence is called below it's definition
#if this is the bug I will be happy and still aggrivated
#my theory is based on the stages which do the same thing
#of being called afterwards but managing the function calls
#that seem to be localized.


# to run this code to parse and generate the python version of
# the javascript switch case into python if tree run
#starter_sequence()



#starter_sequence() #this will be triggered from the parser

# I need to have a function start the code running


#############  end of woodstock added here  april 4th 
#############========================================================
#############


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
	for line in switchcasetester.splitlines():
		#this will be the first case it test
		#just added "'" not in line and '"' not in line:
		################################################################
		if "case" in line and "'" not in line and '"' not in line:  
			#print("so I can see what it sees I am printing the line")
			print(line)
			toowild = line
			break #get out of the dam loop 
		else:
			counter += 1
			continue
	#end loop
	#uses method hasNumbers to determine if a string has number in it.
	#print("====JUMANJI test ===this is in switch_mgrcat=")
	#print("this is what it sees in the first case",toowild)
	money= hasNumbers(toowild)  #returns True or False
	#print("is there a number in the string",money)
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
	#print(valve[0])
	#print("firstcase =",firstcase)
	#sif firstcase == True: #if case is a number like 2:
		#print("here means firstcase == True meaning a NUMBER:")
		#convert_case_numbers_to_strings()
		#mode_2() numbers in pumpkins
	#else:
		#print('firstcase == False  meaning strings words')
		#meaning to the strings words as normal
		#mode_1() strings words



############################################
##             is_number()
############################################
def is_number(inputString):
	mytrace('is_number')
	return any(char.isdigit() for char in inputString)

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


def colin():
	mytrace('colin()')
	#print("Colin suggests using college ruled paper to design code")
	#print("successful test")

def donaldduck():
	mytrace('donaldduck')
	#print("=====DONALD DUCK =============")
	#print("this is DONALD DUCK duckY TIMES AHEAD")
	#print("this is in file christmas.py")




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
	print(switchcasetester) #this is to see the switch case input string after the modification
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
	#print("change macro to into thru")
	#print("=========")
	#print("this is presuming we know it's a number switch case")
	#print("if the macros to and thru are used they need to be change")
	#print("to is converted into thru")
	############
	#print(switchcasetester)
	global switchcasetester
	#print("=========looping thru looking for to===feb 5th 2020====")
	print(switchcasetester)
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
def bottom_up_change_of_thru_line_test():
	mytrace('bottom_up_change_of_thru_line_test()')
	global mouse
	global opal
	opal = ''
	print("=========bottom_up_change_of_thru_line_test()===january 10th 2020====palo alto tennis")
	print("tennis  ====4444455555666666666677778888#go thru the entire string")
	#and change each case number  into a string for preparing for python handling
	## this uses backwards_thru_list
	mycounter = 0
	print("value of mycounter should be zero",mycounter)
	#this makes sure that the backwards list is in reverse order and exists 
	print("the backwards list",backwards_thru_list)
	print("===")
	print("=====")
	print("=======")
	print("==========")
	print("==============")
	 #this is governed by just looping thru the bckwards thru list
	for item in backwards_thru_list: 
	#set mycouter to a number for line in mouse.splitlines() : #this goes thru the mouse string
		print(line)






############################################
## make_list_of_lines_using_thru_macro()
############################################
def make_list_of_lines_using_thru_macro():
	mytrace('make_list_of_lines_using_thru_macro()')
	#print("===----------=== make list of lines using thru macros() ====--------=")
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
	#print("==@@@@@@@@@==THIS IS the list with thru macros line numbers====")
	#print(list_with_thru_macros)		
	#then I need to reverse the list
	backwards_thru_list = list_with_thru_macros
	backwards_thru_list = backwards_thru_list.reverse()
	#print("########### backwards order now #####")
	#print("backwards we have",backwards_thru_list)
	bottom_up_change_of_thru_line_test()






smart =''
beta =''
opal=''
import re
foolish =''
newline=''
####### case_numbers_to_strings changes number cases to strings with the number inside
#######  I still need to sniff and detect if the cases are numbers before calling this 
##############################################################################
###### this converts the numbers to strings such as case 1:  to case '1': ####
##############################################################################
#################### case_numbers_to_strings() ###############################
##############################################################################

def case_numbers_to_strings():
	mytrace('make_list_of_lines_using_thru_macro()')
	global switchcasetester
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	
	#print("========  CASE NUMBERS TO STRINGS  ====")#go thru the entire string
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	#print("looking at switchcasetester before doing this juncture")
	#print(switchcasetester)
	#print("end of this now")
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
			print(" ")
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			print(cat)
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
	#print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings



#above and before stage_one()

#####===================================================
# this is the one line function that does the magic conversion
# from numbers to stings and expands the macros to and thru
# convert_case_numbers_to_strings()

#### this is the main() for number conversion
##############################################################################
##   convert_case_numbers_to_strings():
##############################################################################
# this determine lines with case and thru in same line
# and puts the line number in the switch string into a list
# expand the thru and to macro making list of cases
# convert each number into a string adding quotes around numbers
def convert_case_numbers_to_strings():
	mytrace('convert_case_numbers_to_strings()')
	#print("convert_case_numbers_to_strings() called ----")
	make_list_of_lines_using_thru_macro()
	expand_thru_macro()
	case_numbers_to_strings()
	
####=================================================


	
#this will need to be called for each specific thru line
###==============================================================
###           expand_thru_macro()  
###==============================================================
inputnum = 1
def expand_thru_macro():
	mytrace('expand_thru_macro()')
	#print('expand_thru_macro called')
	global switchcasetester
	#print("just in time changing to into thru")
	#print(switchcasetester)
	####################################################
	#### this is where macro "to" is changed to "thru"
	####################################################
	change_to_into_thru()   #<====== this is where "to macro" swapped
							## with "thru" in switchcasetester input
	
	
	#print("========== expand_thru_macro() called ======")
	#print("with thru added we have")
	#print(switchcasetester)
	#print("===========")
	newlist=[] #resets newlist
	#print("testing this method expand_thru_macro(0 right now")
	global mouse
	global ajax
	global snowy
	snowy=''
	#print("=======expand_thru_macro() called =================")
	#print("we are starating with this test string mouse to get it working")
	#print(mouse)
	mycounter = 0 ### mouse 
	for line in switchcasetester.splitlines():  #doing mouse not doing switchcasetester yet
		#beta = mycounter-1
		#reinitialize what I'm using with each loop iteration
		smart    =[]
		ajax=''
		
		newlist  =[]
		#this is the bug fix so if thru in line (accidentally) confused thru in fallthru
		#so I say if "thru" in line but NOT "fallthru" in line.
		if  "thru" in line and "case" in line and "fallthru" not in line:  #only used with numbers
			#### just added if case is also in this line
			################################################################
			#print("LOOK IN HERE !!!! yes  thru in this line",line)
			#print("MASSIVE SURGERY HERE TO REMOVE THE  COLON ON THE END")
			#print("this makes it conditional on if case in line and colon at end")
			##########################################
			if ":" in line and line.endswith(":"):
				line = chomp(line) #moved taking off colon here 
				print(line)
			else:  #so now if the line doesn't end with a colon it doesn't chomp it
				pass
			### waita  minute when should chomp be used?
			
			#line = chomp(line)
			#line = line[:-1] 
			#print("this is what the line looks like after chomp takes off last char")
			#print("but what is different now is it's competely conditional")
			#print("and chomp only chops off the last char which must be : with case starting line")
			
			#print(line)
			###### print edited out line below
			#line = line[:-1]  #this should chop off the colon(:) on the end
			smart=line.split() #separates case from casename
			#line = line[:-1] #this should take the colon off of the last number
			
			#print("what does smart list have",smart)  #fallthr  missing a u
			#smart = smart[:-1]
			
			#print("smart alleck result for smart[3]",smart[3])
			
			
			#print("does this fix the god dammned alient smart list now!! have",smart)  #fallthr  missing a u
			#print("this should be case", smart[0])
			#print("first number ",int(smart[1]) )     #first number  don't need int
			#print("this should be --thru--",smart[2]) #thru
			#print("last number", smart[3])            #last number 
			#print("will then write perhaps from list yes")
			#print("the input for this macros test")
			print("=============================")
			print(smart[0] + " " + smart[1] + " " + smart[2] + " " + smart[3] + ":")
			#print("")
			counter = smart[1]
			#this is filling up the newlist
			
			#### THIS FILLS newlist with the case info
			# ======LOOP  ==================
			for counter in range(int(smart[1]),int(smart[3]) + 1):
				newlist.append(counter)
				counter += 1
			#print('newlist sees contents',newlist)
			ajax =''
			#print("length of list =",len(newlist))
			#print("this is GENERATED case code from macro with 2 prefix tabs") 
			#this is reading out the contents of the cases one on each line
			
			##==============================================================
			# LOOP ====================
			#print("just took out  + "'" + str(item)  + "'" + 
			for item in newlist:  #this list has the number in it
				ajax += "\t\tcase " +   str(item)   + ":" + "\n"
				#now delete last \n on end 
			
			#print("==== big test of replacing it ====")
			ajax = ajax.rstrip() #see if this works takes off last "\n" whcih was extra
			ajax = ajax[:-1] #chops off last char on end which is the :
			
			
			######## just added 
			#this is where the expandef macros is inserted in the line with "thru"
			#print("this is expand thru macro in pumpkin-falls line 286")
			#print("right here== ajax  is",ajax)
			#print("")
			snowy=switchcasetester.replace(line, ajax)
			switchcasetester=''
			switchcasetester = snowy
			#put the generated list and but outer loop here 
			#####################################=======================
			##### this puts the unfurled macro back into string mouse from ajax
			#inputnum = 1
			#newcounter = 0  #just added
			###LOOP =============================
			#for line in mouse.splitlines():
			#	if  "thru" in line and newcounter == inputnum:  #just added  first thru case
			#	#this replaces the single line with the unfurled line with cases 
			#		mouse = mouse.replace(line, ajax)        
			#		break
			#	else:
			#		newcounter += 1  # just added 
			#		continue
			#		
			#print("=== testing $$ this is the result of the macro thru unfurled")
			#print("=== testing $$ the unfurled macro should show up")
			#print(switchcasetester) #was mouse here 
			#return ajax
			
			
	


####################################
###       CHOMP(x)  
####################################
## this bites off the last character in a string ##
def chomp(x):
	mytrace('chomp()')
	#print("####################======== chomp called",x)
	x = x[:-1] 
	#print("x=",x)
	return x



do_macros = False #by default
#this is a flag to determine if macros thru and to are in the switch case
do_macro_conversion= False # by default



# I can't assume that there is a to or thru macro in use
#this checks if at least one to or one thru in the entire switch case since it will
#be scanned entirely.

def detect_if_thru_and_or_to_macros_exist():  #this requires TWO NUMBERS in Case line
	mytrace('detect_if_thru_and_or_to_macros_exist()')
	print("====called   detect if thru and or to macros exist ===")
	if numbers == True: #if True then there are 2 numbers detected in a case  line
		#do a count
		number_of_thrus=switchcasetester.count("thru")
		number_of_tos = switchcasetester.counter("to")
		#print("the number of thrus =", number_of_thrus)
		#print("number of tos =",number_of_tos)

		#global switchcasetester
		print("=========testing case_numbers_to_strings===january 5th 2020====")
		mycounter = 0; thru_count = 0; 
		for line in switchcasetester.splitlines():
			#case in line     AND   either thru or to
			if "case" in line :
				if "thru" or "to" in line: #they mean the same
					print("thru or to detected in line")
					do_macros = True  #means macro thru or to in this case
					break  #now bail from this loop
					#once it's true it's set in stone that thru andor to macros exist someewhere
					thru_count += 1
					mycounter += 1
				else:
					#print("here it says no thru or to in case line")
					#print("and what it's doing is flipping it false")
					#print("so what I need to do is once it's true it's true for good and bail")
					do_macros = False #means no macro to or thru in this case line
					#print("here it's false and if they are all false fine")
					#print("but once it's true it stops and it's true for the flag of domacros")
					mycounter += 1
					pass
		#print("thru_count",thru_count)
		# determining what the thru/to count is which turns on do_macro_conversion 
		#if int(thru_count) >= 1:
		#	print("yes thru_counter >= 1 so do macro conversion")
		#	do_macro_conversion = True
		#else:
		#	do_macro_conversion = False


##################################
## checks if first case is number
##################################
## march 15th, 2021 Monday
##################################
valve=[]
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
					print("there is only one number in the case line")
					print("here we have discovered there is indeed a NUMBER in case line")
					numbers = False  #meaning ONLY one number in case not two numbers 
					numberflag = True
				else:
					numberflag = False
					pass

			#this scenario is for just  case 2:
			#if  " thru " and " to " not in line:
			#print("=====PIER 39 Crab testing ===== wednesday, march 17th 2021")
			#print("=====PIER 39 Crab testing ===== wednesday, march 17th 2021")
			#print("=====PIER 39 Crab testing ===== wednesday, march 17th 2021")
			#print("=====PIER 39 Crab testing ===== wednesday, march 17th 2021")
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
######## show tron trace path
def show_tron_trace_path():
	print("#######==== showing TRON TRACE path list =====#####")
	counter=0
	last =''
	disney_tron_trace_list.pop(0) #delete's starter position 0
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number

#### mytrace
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

#empty_list method
def empty_list(x): #might need to have it take in with string
	#print("empty_list called working on it")
	# ['applepie']
	print(x)
	newlist = "['" + x + "']"
	print(newlist)
	eval(newlist.clear())
	print(newlist)
	#print("do nothing else yet")
	# and then do this x = x[1:-1] possibly
	# hard coding emptying list
	# changed this March  18, 2021
	#noway= eval("x =[]") #this empties the list by the name entered
	#return noway




    #import importlib
    #from importlib import reload
    #import march_firefall_yosemite_falls   #add to add new front of filename
    #importlib.reload(march_firefall_yosemite_falls)  #and add it here too

def change_list(zoo):
    #print("change_list() calleed")
    switch_config.init()
    switch_subfile.stuff(zoo)
    print(switch_config.mylist[0])
    


###############===================================

###++++$$$$$$$$$$$$$$$$$$$$$$$$$ working on this sunday january 10th $$$$$$$$$$$$$$$$$
###++++$$$$$$$$$$$$$$$$$$$$$$$$$ working on this sunday january 10th $$$$$$$$$$$$$$$$$
####////////////===========================================
## will use this one to replaceing the macro with the expanded macro
## which is a string I reference in a list by order number like string_1, string_2
## these will be
## I need to have my macroexpand function go thru a list of thru lines
## and dynamicallyh build each casethru expanded and the stringname
## added to a list
#and change each case number  into a string for preparing for python handling
## this isn't called yet #go thru the entire string
####################################################
##      swap_thru_lines_with_expanded_cases()     ##
####################################################
def swap_thru_lines_with_expanded_cases():
	mytrace('swap_thru_lines_with_expanded_cases')
	global switchcasetester
	#print("=========testing case_numbers_to_strings===january 5th 2020====")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
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
			switchcasetester=''; switchcasetester = opal
			#HERE is where the changed case numbers as strings are put into switchcasetester
			#will use a replace here to the switchcasetester string
			mycounter += 1
		else:
			mycounter += 1
			continue
	print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings




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



'''
print(" ====== Beach Boys Music =========")
print(" ====== Beach Boys Music =========")

target = list_of_lists[0] #get name of list in list by position
empty_a_list(target)
target = list_of_lists[1] #get name of list in list by position
empty_a_list(target)
print(applepie)
print(peachpie)
print(lemonpie)
print("=============================")
print("===============================")
print("======about to nuke a list======")
print('fox list')
print(fox)
print("I can empty the free floating list fox")
print("with  clear_out_list('fox')")
clear_out_list('fox')
print('after testing lemonpie')
print(fox)
#this takes out a list inside of another list by location
target = list_of_lists[0]
print_out_a_list(target) 



'''
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


	#print('practice deleting all items in it')
	#appliepie=[] #see if that works no quotes
	#print("testing using eval to empty a list on the fly==")
	###=================
	#print("does applepie exists",applepie)
	#sweet = eval(nicejob) #applepie
	#del sweet[:] # will this work
	#sweet *= 0

	#applepie=[] #makes new list with same name
	#print("applepie now should be empty")
	#print(applepie)
	#print("the length of the list =",len(applepie))

	#print("now refilling it up applie pie")
	applepie.append('one')
	applepie.append('two')
	applepie.append('three')
	applepie.append('four')
	applepie.append('five')
'''
##########################################
def empty_lists_in_list_of_lists():
	print("about to start loop")
	print("the length =", len(list_of_lists
		))
	for item in list_of_lists:
		weasel=item[counter]
		print("list name=",weasel)
		#this loops through the list item from list above
		for item in eval(weasel):
			empty_a_list(item)#see if this works
		print("------------")
	
	print("testing accessing varstrings from list does it work")
	print("======list_of_vars====")
	print(list_of_vars[0])
	print(list_of_vars[1])
	print(list_of_vars[2])
	print("about to start loop")
	for item in list_of_vars:
		tuna=item[counter]
		print("list name=",tuna)
		#this loops through the list item from list above
		for item in eval(tuna):
			print(item)
		print("------------")

print("testing about to empty list of lists with a method")
#empty_lists_in_list_of_lists()
print("now let's view list_of_lists")
print("the length is",len(list_of_lists))

'''

#empty_lists_in_list_of_lists()

'''

######## testing deleting a list now 
print("== practice deleting item in loop from list=== ")
print("== practice deleting item in loop from list=== ")
print("== practice deleting item in loop from list=== ")
counter = 0
print("==== tahoe ski bum make it happen alpine meadows")
for item in list_of_lists:
	#weasel=item[counter]
	#print("list name=",weasel)
	#empty_list(weasel)
	#this loops through the list item from list above
	for item in eval(weasel):
		print(item)
		del item
		print(weasel) #should be empty list
		counter += 1
print("what does it see in the lists now?")
print("the names should be in there but they should be empty")
print(list_of_lists)
print("length of list 0 =",len(applepie))
print("length of list 1 =",len(peachpie))
print("length of list 2 =",len(lemonpie))
#loop thru each list


'''


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






######################==========================
##### testing january 10th to go to each case thru from bottom up and change line
##### to prove it's working
####################################################################
## what this does is change the thru macro line starting at the bottom
## by accessing the backwards list made above 
##  backwards_thru_list  that took in the line number of each thru line and reversed it
############################################################
#def bottom_up_change_of_thru_line_test():
#	mytrace('bottom_up_change_of_thru_line_test')
#	global mouse
#	global opal
#	opal = ''
#	print("=========bottom_up_change_of_thru_line_test()===january 10th 2020====palo alto tennis")
#	print("tennis  ====4444455555666666666677778888#go thru the entire string")
#	#and change each case number  into a string for preparing for python handling
#	## this uses backwards_thru_list
#	mycounter = 0
#	print("value of mycounter should be zero",mycounter)
#	#this makes sure that the backwards list is in reverse order and exists 
#	print("the backwards list",backwards_thru_list)
#	print("===")
#	print("=====")
#	print("=======")
#	print("==========")
#	print("==============")
#	 #this is governed by just looping thru the bckwards thru list
#	for item in backwards_thru_list: 
#	#set mycouter to a number for line in mouse.splitlines() : #this goes thru the mouse string
#		print(line)
	
##################==============	
	


#####################===============
# took out make_list_of_lines_using_thru_macros

	################==================



#def remove_from_tail(x):
	#url = 'abcdc.com'
	#if url.endswith('.com'):
    	#url = url[:-4]



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
	#print("second test of checking for numbers in string")
	#cooly= sum(map(str.isdigit, toowild))
	#print("count of numbers in this string =",cooly)
	##this returns the numbers from a case one or two
	#temp = re.findall(r'\d+', toowild) 
	#res = list(map(int, temp)) 
	#,cooly,res; #should be True, 2, [4,7]
	#finbar position 0 returns True if number in case or False
	#finbar position 1 returns number of numbers in this string
	#finbar position 2 returns list of the numbers in case like [4,7]








#smart =''
#opal=''
#import re
#foolish =''
#newline=''
####### case_numbers_to_strings changes number cases to strings with the number inside
#######  I still need to sniff and detect if the cases are numbers before calling this 
#to the switchcasetester string


#this will need to be called for each specific thru line
###==============================================================
###================  expand_thru_macro()  ===================
###==============================================================















	

##################### March 15th, 2021  ############################
# this determines whether the switch case is numbers or words/chars
#need to add the number functions (shown below) to this file from pumpkins.py
# this faucet valve uses test if first case is number or string
# and then accordingly calls methods to convert the numbers to strings in cases
# and expand the to and thru macros
# first I need to have it check if "thru" or "to" is switchcasetester
# be sure to do that

# faucet_value function 
# this function uses the following methods:

#           check_if_first_case_is_number()
#           detect_if_thru_and_or_to_macros_exist()
#           make_list_of_lines_using_thru_macro()
#			bottom_up_change_of_thru_line_test()
#			change_to_into_thru()
#			expand_thru_macro()
#			case_numbers_to_strings() 

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
	#print("contents of valve[0]",valve[0])
	#print(valve[0])
	#print("firstcase =",firstcase)
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
def get_location_of_case(listname,word):
    #print("listname,word=",listname,word)
    #print("get location of case () called ")
    #print("this is searching for ",word)  #below took out  + "'" + both sides of word
    answer =eval("" + listname + ".index("  + word + ")")
    #print('====after running get_location_of_case we get this== should be a number==')
    #print("location of case",word," in listname=",answer)
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




'''
slick= fruits.index('fallthru')
print("slick=",slick)
print("==========using the method get_location_of_case(listname,word)========")
print("real testing begins here ")
print("this returns a number")
print("=== methods called down here")
print("fruits list =",fruits)
output =get_location_of_case("fruits",'banana')
print("result =",output)
output =get_location_of_case("fruits",'fallthru')
print("result =",output)
output =get_location_of_case("fruits",'pears')
print("result =",output)
output =get_location_of_case("fruits",'cherries')
print("result =",output)
output =get_location_of_case("fruits",'lake tahoe')
print("result =",output)
'''

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
			print("mrdefault=",counter) #this won't work without default word
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
	
	
	if solution == "true":
		print("break after default")
	else:
		print("add the break at end")
	

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
		print('already a break in default case')
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
	print("t=",t) #this outputs the input paramter to see what wise_owl saw
		
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
	print("mrdefault =",mrdefault)
	#get_last_break_in_string()
	#look at this carefully it starts the smartcounter with the line of default 
	smartcounter = int(mrdefault) #the starting point   #the default line number retrieved before this
	print("for smartcounter starting we have ",smartcounter)
	thebreak = False #default setting boolean
	global switchcasetester
	for line in switchcasetester.splitlines():
		if "break" in line:
			thebreak = True
			break  #out of loop
		else:
			pass
			smartcounter += 1
	print("thebreak=",thebreak) #this returns True in thebreak if there is a break in default
	print("new roller coaster testing if break missing after default and ")
	print("now add the break at bottom of default ")
	if thebreak == False:
		print("add break to bottom of default case now right here")
		#global switchcasetester
		print("switchcasetester=",switchcasetester)
		################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		#######################################################################
		staypuff=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = staypuff
		print("=====after adding break to bottom of default we have====== ")
		print(switchcasetester)
	
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


# this calls faucet_valve to determine if cases are numbers or words
#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
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
	print('varholder[0]=',varholder[0])
	print(varholder[0]) #to actually see proof
	return varholder[0]
	angel = varholder[0]
	## ===check if input is a number or a word with letters
	#====x = angel.isdigit() commented out march 17, 2021
	#print('about to call FINBAR() to look in first case line')
	#print("=1=1=1=1=1=1=1=1=1=1=1=1=1=1=1=")
	#print("this is inside of function CLEVER()")
	#global switchcaseteser
	#numberflag = False # by default until otherwise determined 
	#print("ABOUT TO LOOK IN SWITCH STRING FIRST CASE FOR WORD")
	#for line in switchcasetester.splitlines():
		#this will be the first case it test
		#just added "'" not in line and '"' not in line:
		################################################################
	#	if "case" in line :  
			#print("so I can see what it sees I am printing the line")

	#		print(line)
	#		toowild = line
	#		print("this has to be the first case line the FIRST LINE")
	#		print(line)
	#		print("###################################")
	#		break #get out of the dam loop 
	#	else:
	#		counter += 1
	#		continue
	#end loop
	#uses method hasNumbers to determine if a string has number in it.
	#money= hasNumbers(toowild)  #returns True or False
	#print("is there a number in the string",money)
	#if money == True:
	#	print("yes number in the line")
	#else:
	#	print("no number in line")
	##return money 
	#print("=2=2=2=2=2=2=2=2=222=2=2=2=2=2=")
	#print("what=",what)
	#valve[0] = what
	#print(valve[0])
	#print("number true not number false",what)

	#print("=3=3=3=3=3=3=3=3=3=1=1=1=1=1=1=")
	####################
	#x =is_number(i)
	#if x == True:#number  in input
	#	print("its a number ")
	#	input = "number"
	#	valve.append(True)
	#	print(valve[0])
	#else:
	#	valve.append(False)
	#	print(valve[0])
	#	input = "word"
	#	print("it's a letter or word")
	#	print("departing from clever function for input we have",valve[0])
	
		##################
	#print("calling faucet valve inside of clever()")
	#faucet_valve()




#apparently this needs to exist in this file
def moreclever(i): #so it already exists we are changing its value
	print("moreclever input called")
	varholder[0] ='' #clears it out
	print("clever called for input to switch case exp")
	varholder[0]= i
	#this works and it fills a list with input from an argument
	print('varholder[0]=',varholder[0])
	print(varholder[0]) #to actually see proof









#testing accessing switchcase from file goldfish
def mountain2(c):
	mytrace('mountain2()')
	print("===mountain 2called===playing with switch case ")
	var2[0]= c
	global weasel
	weasel = var2[0]
	global switchcasetester
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
	print("=======romanwall called=====")
	#I might have to concat it and make it into
	#virgin reutrn switchcasetester = '''
	#it might have to be generated and then eval(string) or exec(string)
	supertramp= j
	switchcasetester= j  #seeing what happens
	print(supertramp)
	#see if it can read what is in the string
	#just testing what I can do here with the string
	answer =supertramp.count("case")
	print("the number of cases in this string =",answer)
	print(switchcasetester)

'''
#global valve_setting
	#theinput = x.isdigit()
	#if theinput == True:
	#	#print("its a number ")
	#	valve_setting = "number"
	#else:
	#	valve_setting = "word"
	#print("this is inside of the switch statement")
	#print("that takes in input and checks if number or word")
#	
#
	#print("the valve_setting =",valve_setting, "which is",x)
	#################################################
	 	#print("it's a letter or word")
'''



def adjust_input(x):
	print("adjust input called with", x, "inside of yosemite")
	newstring =varholder.append(' + x + ')



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
	
	#numbers
	# if int
	#if type(x) == int:
	#	x = int(x)
	#	case = int(x)
	



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
	print("make_list_of_first_cases() called ")
	print('starting reset of list')
	print("initially list length of birdsong is",len(birdsong))
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
			smart=line.split() #separates case from casename
			birdsong.append(smart[1]) #this adds casenameto list birdson
			music.append(mycounter) #list of number for case line
			mycounter += 1
		else:
			mycounter +=1
		print("after the if this is the content of birdsong",birdsong)
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
	print("=============get default location called =================")
	mytrace('get_default_location')
	counter =0
	for line in switchcasetester.splitlines():
		if "default" in line:
			default_location = counter
			break
		else:
			counter += 1
			continue
	print("the default location line number =",default_location)
	return default_location
	
	
##############################################
##	add_break_to_bottom_of_default():
##################################################
lovely=''
def add_break_to_bottom_of_default():
	mytrace('add_break_to_bottom_of_default()')
	global switchcasetester
	print("=========just called ADD_BREAK_TO_BOTTOM_OF_DEFAULT()=========")
	lovely = switchcasetester #the whole switch case string
	x = lovely.count('break')
	print("there are ",x ,"breaks in the switch case")
	#test if break after default line
	print('start phase 1 ....')
	
	counter =get_default_location() #the line number
	print("counter starting value of default is",counter)
	findbreak = False #by default unknown at this point if a break after default
	print("findbreak=",findbreak)
	print('start phase 2 ....')
	
	for line in switchcasetester.splitlines():
		print('counter=',counter)
		if "break" in line:
			break_location = counter
			findbreak = True
			print('findbreak =',findbreak)
			break
		else:
			counter += 1
			continue
	print('start phase 3 ....')		
	print("the value of findbreak =",findbreak)
	print("this is after the loop has gone through looking for break after default line")		
	if findbreak == True:
		print("findbreak = True so do nothing break exists after default")
		print("do nothing break exists after default")
		print("it will be interesting if this is true, but I can test it")
		print("the number of breaks found in the switchcasetester was",x)
		print("let's look in switchasetester and see for ourselves.")
		print(switchcasetester)
	else:
		print("if at this point then break after default is False")
		print("break is false and need to add it")
		print("switchcasetester starting =")
		print(switchcasetester)#have to add break with tabs before it
		peach=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = peach
		print("after adding beak beneath default we have ")
		print(switchcasetester)
		print("end of BIG TEST for break in default addition")	
	#return break_location   (maybe we don't need this)
	
    
		








#########=============== get last break in string ==================
listofbreaks=[]
genius=''
nobreaks = "false"
def get_last_break_in_string(): #but what if no break??? march 1st bad assumption here
	print("======BLINK182========get last break in string in the whole switch case string ============")
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
		print("starting loop looking for breaks in switch case")
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
	print("genius is the last break line number =",genius)
	
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
	print("the number of breaks = ",counter," if none then nobreaks = ",nobreaks)
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



##################################
###  convert  default  case '':
mrlastbreak=''
lastbreak=''
###################################
def convert_default_case(): #I got this working November 26th, 2020
######################################
	print("convert_default_case()  ===&&&&&-- CALLED Motel 6 test night")
	#add_break_to_bottom_of_default()  ##march 3rd, 2021
	mytrace('convert_default_case')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location()
	#print("=== GhostBusters===")
	#print("get_default line number=",get_default) #line number of default
	#print("lets see the LIST OF BREAKS  full list",listofbreaks)
	
	
	#reverse the list
	#print("trying to reverse this sucker")
	#listofbreaks.reverse()
	#print(listofbreaks)

	
	 
	#print("the last break would be ",listofbreaks[-1])
	if len(listofbreaks) == 0:  #maybe it will be None
		print("no breaks in the whole switch case string")
	else:
		pass
	
	last_break=get_last_break_in_string() #what if it returns None???
	#this is new march 1st 2021 starbucks coding in earlying
	last_line_of_string = get_length_of_string()
	#print("the last line of string =",last_line_of_string)
	#print("NOW I HAVE ALL THAT I NEED TO GET THIS TO WORK CORRECTLY TONIGHT!!!!")
	#print("=====GhostBusters ===")
	
	#print("WHAT DOES THIS NUMBER SAY===========........>>>>>>?")
	#print("======GhostBusters ==============")
	#print("get_default=",get_default) #line number of default
	#print("last break =",last_break)  #next figure out if NO BREAK WHATSOEVER
	#print("last line  =",last_line_of_string)
	#print("the result therefore is:")
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
	
	print("====================")
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
	print("trigger =", trigger)
	if trigger == True:
		print("trigger =", True)
	else:
		print('trigger=',False)
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
    print(foo)
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
    print("in stage_one() resetting lists palmtrees, carnberries, royalllist, british")
    print("penguin, roadrunner, starbuckslist")
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
    print(line_numbers_first_cases)
    print("====================")
            
def empty_test():  #call this when clever(input) called
   # print("===============")
   # print("empty list") # to clear out list to make sure it's empty 
    global line_numbers_first_cases
   # print('in here now')
    line_numbers_first_cases =['starter']
    print(line_numbers_first_cases)        
    #print("==================")
        
        
        
        
        
##################################################
def magictimenow():   ### this builds the list for line_numbers_of_first_cases
##################################################
	mytrace('magictimenow')
	#this should make it real
	global woodstock
	#print("woodstock contains=",woodstock)
	#global candy
	#print("candy contains=",candy)
	#print("switchcasetester=",switchcasetester)
	mytrace('magictimenow()')
	#This makes a list of true if case in line and false if no case in this line
	#print("first fillup a list with true and false")
	#print("true if case in this line and false if not")
	#print("=== simple test if case in a line if so then True")
	#print("=== and if no case in this line then put False")
	#print("these true and false go into list called ifcaseinline")
	ifcaseinline=['starter']   #theresult
	#this loop puts true into ifcaseinline if case in this line otherwise it puts false
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		if "case" in line:
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


	
	thecounter=0
	for item in trontime:
		#print(item,thecounter)
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

	#this is where the line_numbers_of_first_cases list is filled with the line number of first cases
	 #nuked 'starter' from it
	acounter=0
	#what this does is look in the current line for the word "case"
	#and looks in the trontime list for the line above the current line to make
	#sure that "case" is not in the previous line determined by the word 'false'
	#the trontime list only has trues and falses so true if case in line otherwise false
	for line in switchcasetester.splitlines():
		#this checks if case in this line but no case in line before it
		#the tricky part of this solution is that it is looking above the current line
		#trontime list holds true and false depending on if 'case' in that line number
		if "case" in line and "case" not in trontime[acounter-1] :  #tests if no case above this line with case
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
	#print("=======case main body list =====")
	#print("starting state of this list case_main_body_list =",case_main_body_list)
	#print(case_main_body_list)
	#print("this is force feeding it to just be starter for some reason")
	#case_main_body_list=[]
	#case_main_body_list.append("starter")
	answer=''
	for item in range(1,len(case_main_body_list)):
		print("item in cotton candy is",item)
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
	print('stage two')
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
    print('=====stage three====')
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
	print("========rule the earth called========")
	print("== DEBUGGING ==")
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
	print("inside of function rule_the_earth()")
	print("palmtrees at this point has in it line 6693 ",palmtrees)
	#palmtrees.append('starter')
	#####################################
	## new addition to reset palmtrees list april 27th 2021 6:30 pm
	reset_list_to_just_starter(palmtrees) #clears out list if previously used resets it
	print("palmtrees should only have starter in it at this location")
	palmtrees.append('starter') #which would be in slot 0
	print("palmtrees=",palmtrees)
	##for case sets I just go thru till case not in line and fill a new list
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		if mycounter in line_numbers_of_first_cases:
			#breakpoint()#print(line)
			#felix is the line split into a string
			felix= line.split()
			print("NUMBER OF WORDS IN THIS CASE LINE")
			print("number of words in this line is ",len(felix))
			
			#print("inside rule_the_earth line with case")
			print("felix=",felix)

			if "default" in line:
				print(line)
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
				print("I think that case must be in this line")
				print("look at this next line carefully")
				print('line =',line)
				second_word = line.split()[1] #right here it grabs just one word
				#that is the flaw
				##### addition here 
				#### first check if only one word
				#print("felix=",felix)
				#print("DEBUGGING ==6730==")
				#print("the line with default=",line)
				print("felix[0]=",felix[0])
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
					print('AT THIS JUNCTURE LINE 6745 palmtrees=',palmtrees)
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
						print("here at line 6767 palmtrees=",palmtrees)
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
	print("palmtrees=",palmtrees)
	starbuckslist=[] #resets it
	reset_list_to_just_starter(starbuckslist)
	print("what's in starbuckslist here",starbuckslist)
	#filling starbuckslist
	#####################################
	
	print("===========================")
	for item in palmtrees:
		starbuckslist.append(item)
	print("at line 6820 strarbuckslist =",starbuckslist)	
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

#what this does is take the input of teh [builder list] with line numbers
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
	#print('case section line number list =',builder)
	#print("what is in builder?") #I think it's the first case line number in each section
	#print(builder)
	
	
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		#print(line)
		if mycounter in builder: #so it's looping thru switchase and line number in builder list
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
			
	print("resulting starbuckslist=",starbuckslist)


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
    print("digitalcandy=",digitalcandy)
    print('testing what is in digitalcandy line 7128')
    if len(digitalcandy) == 0:
    	print('digitalcandy is empty')
    else:
    	print("digitalcandy length =",len(digitalcandy))


    #this clears out digitalcandy (hopefully)
    # if digitalcandy has something in it then clear it
    if len(digitalcandy) > 0:
    	reset_list_to_just_starter(digitalcandy) #this makes it read ['starter']
    else:
    	pass
    #================
    #breakpoint()
    print("starting out this is what is inside of list digitalcandy")
    print("this is a moment before converting it into a twin list")
    print("before appending to digitalcandy I wasnt verifying if it was empty")
    print('the length of digitalcandy =',len(digitalcandy))
    print(digitalcandy)
    #digitalcandy.pop() #takes off first item of starterj this makes it empty
    #========================
    #global candy
    #candy=''
    #candy=[]
    #input_list -= 1 #true cases last number is default
    print("inside of convert_to_twin_list")
    print("line_numbers_of_first_cases",line_numbers_of_first_cases)
    list_trex=[] #this should reset it
    print("list_trex=",list_trex)
    alpha = 0; beta = 1; counter = 0  #down below it was: length_of_input_list
    while counter < len(line_numbers_of_first_cases) -1:
        eval("list_trex.append(line_numbers_of_first_cases[alpha])")
        eval("list_trex.append(line_numbers_of_first_cases[beta])")
        eval("digitalcandy.append(list_trex)")
        eval("candy.append(list_trex)")
        alpha += 1; beta += 1; counter += 1
        list_trex=[] #resets list to reuse next loop
    print('digitalcandy =',digitalcandy)
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
	
	print("defaultlist=",defaultlist)
	print("digitalcandy at this point",digitalcandy)
	#so this means that digital candy should already exist and be populated
	#don't want to corruptthis it is only expecting two values not three
	digitalcandy.append(defaultlist) #these two are the parameters to look between
	#print("defaultlist=",defaultlist)
	print("line 7317")
	print("candy",candy)
	candy.append(defaultlist)
	print("now candy shows",candy)
	print("at this point digital candy shows",digitalcandy)
	
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
	if b > a:
		#print("==== testing if break AFTER default")
		print("there is a break in default")
	else:
		print("there is a MISSING break in default case")
		#print('there is NOT a break in default need to add one')
		#again this is adding a break in default to javascript switch case
		#because of an obscure bug caused by missing break in default
		#print("this is before adding break to default")
		#print(switchcasetester)
		#global switchcasetester
		orange=''

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
	special_addition_to_digital_candy() #===================added nov 25th, 2020
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
		print(item,count)
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

    print("royallist=",royallist)







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
                print(line.split(' ',1)[1])
                print(line,smartcounter)
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
                    print(caseset)
                    
                if len(genius) == 3:
                    #print('teh default was 3 words case and two words')
                    ap =genius[1] + genius[2]
                    caseset.append(ap)
                    print(caseset)
                    
                if len(genius) == 4:
                    #print('teh default was 4 word case and 3 words')
                    ap =genius[1] + genius[2] + genius[3]
                    caseset.append(ap)
                    print(caseset)
                    
                if len(genius) > 4:
                    #print("more than four words in this line detected")
                    #print("just do the default for now will fix later")
                    caseset.append(genius[1])
                    print(caseset)
                
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
print("wilecoyote list",wilecoyote)
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
                print(mrcase)
            #end if
            
            
            #firstline = line.split()
            #print("I need to make sure it searches through the lines")
            print(line)
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
   # print("===::::::::::::::=========")
    #print("royallist has ",royallist)
   
    #print("homer simpson",homer) #only line numbers with break
    #I can then deduce what case sections they reside in
    #print("starbuckslist=",starbuckslist)
    #print("a shot in the dark here")
    #print("palmtrees=", palmtrees)
    #print("I can try adding the break onto the end here.")
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

## bug in royallist it should end with break for default not a fallthru


# beach break through 
#great idea,
#modify parameter of list in method do_replace
#so on the the fly with ONE name parameter I can change the
#list that do_replace method operates on and modifies
#have the listname reference an outside list outside of the meth#od above it
#and when I chnage what's in that outside list it will change i#t


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
	print('in crashing waves at beach we have wilecoyote line 7975',wilecoyote)
	print("palmtrees at line 7977 we have ",palmtrees)
	## this gets the location of the case in wilecoyote inside of palmtrees list
	for item in wilecoyote: #goes through list of case sections with breaks
		toad = get_location_of_case("palmtrees",str(item))
		
		print("we have this in toad=",toad)

		roadrunner.append(toad) #this returns a number the index position
	#print("ROADRUNNER list contains numbers of index locations of cases in palmtrees",roadrunner)
#################################################
	# make a new list based on digitalcandy
	print("in digitalcandy at line 7988 we have",digitalcandy)
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
	print("in crashing_waves_at_beach() around line 7942")
	print("digitalcandy",digitalcandy)
	print("roadrunner",roadrunner)
	
	#to debug
	print("digitalcandy at line 8024",digitalcandy)
	print("roadrunner at line 8025,roadrunner")
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
	british[0] = "starter"
	#this ensures that the last one is a break no matter what it's force fed in. 
	british[-1] = "break" #makes sure last one is break which is absolutely must be. 
	#print("here is the finished british list before adding teh fallthru with case")
	#print("british now =",british)
	print("british list at line 8024=",british)
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
	#print("british list=",british)
	#print("palmtrees list =",palmtrees)
	#penguin.append('starter')
	for item in british:
		penguin.append(item)
	
	print('penguin at line 8066',penguin)

	#penguin.append('break')
	#print("penguin= ", penguin)
	#print("starting length of penguin=",len(penguin))
	
	#faltlrhus with numbers get case number from end of fallthru
	#print("MASSIVE TEST OF replacing fallthruX with fallthru('casename') in british list")
	#print("======")
	#print("======")
	#print("======")
	### new coding here 
	#print('british list=',british)
	newcounter=0
	print("in crashing_waves_at_beach()")
	print("length of palmtrees at line 8081 =", len(palmtrees))
	print("palmtrees =",palmtrees)
	print("around line 8004")
	#exit() #see if this works

	print("british at line 8085=",british)
	print("line 8086 palmtrees=",palmtrees)

	for item in range(0,len(british)):  #should only look inside of items starting with f
		if british[item].startswith("fallthru"):
			#print('item =',item)
			#print("newcounter =",newcounter)
			getnumber= british[newcounter] #gets the fallthruX
			#print("it sees this in british[newcounter]")
			#get the number on end of word fallthru
			#print("getnumber=",getnumber)
			getnumber = getnumber[8:] #gets the number from cutting off front fallthru
			getnumber = getnumber.rstrip()
			getnumber = getnumber.lstrip()
			#print("getnumber=",getnumber)
			newnumber = int(getnumber)
			#print(newnumber)
			print("===right here this is where things go south fast====")
			print("palmtrees=",palmtrees)
			print("palmtrees[newnumber",palmtrees[newnumber])
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
	#print("penguin=",penguin)
	#print("11111111111111111111111111111111")
	#print("11111111111111111111111111111111")
	#print("11111111111111111111111111111111")
	#print("11111111111111111111111111111111")
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
def f22_fighter_jet(): #makes critical cranberries list which is the taillist for switch cases
	mytrace('f22_fighter_jet()')
	counter = 0
	c = 1		#current case numbr section
	d = c + 1

	for item in digitalcandy:	#this is going through the diamonds list

		neato = digitalcandy[counter]
		x = neato[0]
		y = neato[1]
		##print("x",x,"y",y);
		case_tail_list_maker(x,y)
		counter += 1

	royallist.append('break');  #in default
	counter = 0

	#this goes thru the royallist with breaks and fallthrus(numbers)
	# starter 0  fallthru2 fallthru3 fallthru4  fallthru5 default
	#loops thru to royalist[item] then accesses the starbucklist[item to append
	# I can make fallthru('fish') and fallthru('default')  and have the formula working
	#I use numbering in royalist starter1(0) (position1 fallthru2)   (position2 fallthru3) etc
	#if they use big numbers I will put them inside of (number) and grab teh number startswith("(")
	#and endswith(")")
	#print('royallist =',royallist)
	
	for item in royallist: #use range here 
	#for item in range(1,len(royallist)): #added march 16,20211:19pm
		if "break" in item:
			cranberries.append("break")

		if "fallthru" in item:
			item=item.strip()
			item =item[-1]
			#print("item=",item)
			item = int(item)
			#print(item)
			doggy =starbuckslist[item] #this is like fallthru('cherry')
			ohbaby = "fallthru(" +  "'" + doggy  +  "'" + ")"  #this is the number

			#print("ohbaby=",ohbaby)
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target

###################################################
  ##===========================
  ##      def p51_mustange()  ==  adds the number to  fallthru(3) like that
  ##===========================
  #this makes the cranberries list which is the tail list used on codegen page
#diamonds=[[2,7],[7,17],[17,24],[24,34]]
#this makes the cranberries list
def p51_mustang(): #makes critical cranberries list which is the taillist for switch cases
	#print("=== p51 MUSTANG finishing up last part of numbering fallthrus and getting next case name")
	#print("=== ==== == === == the P51 Mustange is starting to fly and get off the ground entering clouds")
	#print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")

	#print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	#print("@@ p51 MUSTANG code called which fills the cranberries third part tail with fallthru and break")
	#print("P51 MUSTANG will it fly today======================::::::::::::::::::")
	
	mytrace('p51_mustang')
	counter = 0
	c = 1		#current case numbr section
	d = c + 1
	#print("** inside of p51 mustange [[ digitalcandy ]] =",digitalcandy)
	royallist =[] #resetting this Friday april 9th
	#maybe in digitalcandy
	print("line_numbers_of_first_cases",line_numbers_of_first_cases)
	print("digitalcandy in p51mustange=",digitalcandy)
	for item in digitalcandy:	#this is going through the diamonds list

		holder = digitalcandy[counter]
		x = holder[0]
		y = holder[1]
		##print("x",x,"y",y);
		case_tail_list_maker(x,y)   #here it is calling case_tail_list_maker
		counter += 1

	royallist.append('break');  #in default
	counter = 0
	print("royallist at line 8223 =",royallist)


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
			#print(item)
			#print("==========//////// ===============")
			#print("LOOK RIGHT IN HERE ==> palmtrees=",palmtrees)
			#print("in drive_thru list we have",drive_thru)
			print("palmtrees at line 8253 =",palmtrees)

			#print("this is getting the case name from palmtrees[item]")
			####this isn't working because it doesnt capture more than one word soit's strong and cuts off first word.
			print("palmtrees=",palmtrees)
			print("palmtrees[item]=",palmtrees[item])
			doggy =palmtrees[item] #just added -1   this is like fallthru('cherry')  #was starbucks
			#print("doggy",doggy)
			doggy[1:]
			doggy[:-1]
			#print("slice off first and last character",doggy)
			#print("doggy is showing ===",doggy)
			#cool1 = doggy.lstrip("'")
			#cool2 = cool1.rstrip("'")
			#doggy = cool2

			#print("palmtrees[item]=",palmtrees[item])  #was starbucks
			
			#print("ohbaby which has fallthru from doggy starbuckslist[item]")
			ohbaby = "fallthru("  + "'" + doggy + "'" +  ")"#this is the number
			#just took out the "'" on both sides of doggy 
			#print("ohbaby =",ohbaby)
			#########################################
			#print("the constructed fallthru is in ohbaby=",ohbaby)
			#print("ohbaby=",ohbaby)
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target
			
			#print("this IS WHAT is in CRANBERRIES",cranberries)
			#print("=====")
			#print("the LENGTH of cranberries list=",len(cranberries))
	print('cranberries list at line 8281=',cranberries)

	# make sure that default case needs to end with break and not fallthru
	# february 4th, 2021
	#print("================= C R A N B E R R I E S   L I S T ====case-tail-maker=========")
	#print("ROYALLIST =",royallist)
	#print("palmtrees =",palmtrees)  #was starbuckslist
	#print('CRANBERRIES list =',cranberries)
	#print("drive_thru list =",drive_thru)
	#this fills up trail_list from cranberries and creates a new list
	#print("wilecoyote list of case names with a break verified")
	#print("00000000000000000000000")
	#print("00000000000000000000000")
	#print("00000000000000000000000")
	#print("00000000000000000000000")
	#print("00000000000000000000000")
	#print(wilecoyote)
	#print(len(wilecoyote))
	
		
	#print(wilecoyote[0])
	#print(wilecoyote)
	#print("firstcaselist now in palmtrees")
	#print(palmtrees)
	
	oceanwaves=[] #this sets it at empty
	#print(" ====== JUMANJI ====")
	#print(" ..................J U M A N J I ......inside of P51 Mustang() function..........")
	#add method here
	crashing_waves_at_beach()
	#print("tyring to fill  list oceanwaves with british list")
	#print("here I am filing the list oceanwaves with the british list")
	for item in british:
		oceanwaves.append(item)
	
	print("OCEANWAVES LIST now ",oceanwaves)
	#print(oceanwaves)
#I will needto add this to royallist
	
			
			
	
	#print("THIS IS THE TAIL LIST CALLED CRANBERRIES")
	#print("cranberries=",cranberries)
	#print("penguin=",penguin)
	

####### this was in working code
'''
for item in royallist:
		if "break" in item:
			cranberries.append("break")

		if "fallthru" in item:
			item=item.strip()
			item =item[-1]
			#print("item=",item)
			item = int(item)
			#print(item)
			doggy =starbuckslist[item] #this is like fallthru('cherry')
			ohbaby = "fallthru(" +  "'" + doggy  +  "'" + ")"  #this is the number

			#print("ohbaby=",ohbaby)
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target
'''
###########


	#tail_list = copy.deepcopy(cranberries)
	#print("see if this works == making the tail_list")
	#for item in cranberries:
	#	tail_list.append(item)


# I will need to change this here and just have p51mustang
def stage_six():
    #print('stage six')
    firstcase = valve[0]
    if firstcase == True:  #which means numbers like case 4:
        f22_fighter_jet()
    else:
        p51_mustang()


#p51_mustang() #==========




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
##   flying fish             this loops through the dimaonds list of first cases
##==========================
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
	print("digitalcandy at line 8418=",digitalcandy)
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
##   flying cloud            this builds a list of the case names for each section
##==========================
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

#============================
#      wildgame
#============================
#or am I using the current case number or next case number for fallthru
#so does it represent the current location and then we add 1 to it or does fallthru(#) have
#the next number position embedded in it already
#this will go through the list and convert the fallthru(#) into names making the gold tail list
#which is used to build the case sections
bronzelist =[]
#I think it will already have it in it calculated currecent case section number + 1
def wildgame(y):   #this gets the number out of fallthru(5) and converts it to the casename
	mytrace("wildgame")
	#print("===============WILDGAME CALLED WITH input number for FALLTHRU =",y)
	#new notes. we want the next case if 1 apple we should get fallthru 2 so banans
	#so the current case section number + 1 goes into fallthru(number)
	########=========== decided thursday, september 10, 2020 at Target
    #  starter position 0 then 1, 2, etc  so for fallthru add 1 to current position
	#print("testing wildgame() to generate the next case number for fallthru")
	#print("starbuckslist=",starbuckslist)
	#print("the length =", len(starbuckslist))
	#print("==========")
	#print(".........")   #so we get fallthru('fish')  which is literally amazing
	#whatever the number abstracted it turn to an int and add one to it

	#print("this is getting the number out of ( ) inside of fallthru(number) word")
	#==========================================
	#starter is 0 but not a case
	#first case is position 1 (if fallthru(1)) it becomes fallthru(2) for conversion
	#so it is based on current position for the current case and then the NEXT case is +1
	#==========================================
	#input must be 1 or higher but less than the length-1 can't be starter (0) or default(length-1)

	mystring='fallthru(' + str(y) + ')'  #this gets the number from fallthru to use in starbuckslist to get case name
	#print('mystring=',mystring)

	#print("wildgame function called ....",mystring)
	#this extracts the number from a string
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








#======== sutterrsmill==============================
case_main_body_list=[]
case_main_body_list.append('starter')  #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code




def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	#print("================big gears filling list with case bodies called==========")


	counter=0
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
	#print("=====/////======= smarty() called ====line 3142=====//////=====")
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
	#print("==== attempting to print out cases section code from case_main_body_list")
	acounter=0
	for item in case_main_body_list:
		#print("==========")
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
	print(z)  #print(listname)

#  new_replace_index(x,y)  uses two variables and 
#  hard code list name and call replace_in_list(x,y,z)
def new_replace_index(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=fruits  #list name
	replace_in_list(x,y,z)   ##<<==== it calls the method above brilliant
	#print(fruits)
	
	
#Use loop based on number of case sections

#Loop
#Listname.append(‘fallthru’)

#After loop done
#Add listname.append(‘break’)
#Called once fills list
#print("========== testing to replace words in lists easily ==========")
#print("========== testing to replace words in lists easily ==========")
#print("========== testing to replace words in lists easily ==========")

#print("testing making changes to a list which I will use for constructing")
#print(" breaks and fallthrus  for utlimately constructing the list to")
#print(" be used to put into cranberries list")

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

print(fruits)
replace_in_list(end, 'break',fruits)
print(fruits)
replace_in_list(2, 'break',fruits)
replace_in_list(3, 'break',fruits)
replace_in_list(4, 'break',fruits)
replace_in_list(8, 'break',fruits)
replace_in_list(9, 'break',fruits)
end = len(fruits)-1 # last index position
replace_in_list(end, 'break',fruits)
print(fruits)
print("=====")
new_replace_index(end,"panera bread") 
new_replace_index(6,"break") 

print("=== the end here of replace for now ===")


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

def stage_eight():
	mytrace('stage_eight()')
	#print('stage eight')
	loop_thru_case_sections()


icecream=''
def herewego(): #loops and prints all main bodies
	mytrace('herewego')
	#this loops through the case_main_body_list and prints the case python code
	#print("here we go () called it prints the case body code from the list ")
	#mightymouse = "happy"
	#print("======= here we go() called =======")

	counter=0
	#print("length of case body list =", len(case_main_body_list))
	#print(case_main_body_list)
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

def stage_nine():
	mytrace('stage_nine()')
	#print('stage nine')
	big_gears_filling_list_with_case_bodies()
	herewego()


print("tail_list cranberries =",cranberries)
###=============================================================================
x = 0;y =0
smart=''
#cranberries=[]
list_of_rows_of_case_names=[]


#making case section sublists here
#this is for making the variable lists to fill the case sections of cases
# and to refer to each of these caselists with ifs and elifs

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

	print("==============================================")
	print("digitalcandy list ========")
	for item in digitalcandy:
		pass #print(item)
		
	global candy
	for item in candy:
		pass #print(item)
		
	#print("starbucks list ====of first case names in each section ====")
	#print(starbuckslist)

	#print("smartcasemanager list ========", len(smartcasemanager))
	for item in smartcasemanager:#
		pass #print(item)

	#print("case_main_body_list list ========", len(case_main_body_list))
	for item in case_main_body_list:
		pass
		#print(item)
	#=== code gen here ====


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
#####=========== get() ===================
#this is a return value in varholder[1]
def get(x):
	switch_return_value.append(x)
	#print("inside of switch_return_value[1]")
	print(switch_return_value[1])


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
















def parktime():

	mytrace('parktime')
	import re
	myString = "\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
	#print(myString)
	output   = re.sub(r"[\n\t]*", "", myString)




def stage_eleven():
	mytrace('stage_eleven()')
	#print('stage eleven')
	parktime()


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

#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#####          switch_code_gen()                      ###
#########################################################
#########################################################

# I am thinking of seperating it totally  to make sure it works
# with the lists generated from the parser as inputs for switch_code_gen
# and that way I can determine where the bug is.

##########################################################

#this does switch code gen for words/chars NOT numbers
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():
	
	
	
		
	mytrace('switch_code_gen')
	#####
	
	##### march 7, 2021
	#new change putting penguin into cranberries
	print("=== march 7th, 2021 testing===================///================================")
	print("what is in penguin???")
	print("flying PENGUIN=",penguin)
	print("=========================")
	#print("cranberries=",cranberries)
	#breakpoint()
	print("======")
	#Here I am putting the contents of penguin into cranberries
	print("this is where I empty cranberries list and fill it with penguin")
	cranberries=[]  #emptying cranberries here 
	for item in penguin:  #this works - how wonderful
		print(item)
		cranberries.append(item)
		
	print("CrAnBeRRies-----  =",cranberries)
	
	###########  march 7, 20201  #######################################
	# I think that I just need to loop through casemainbodylist
	# and append cranberries based on teh counter and then eliminate the third tier below
	# what I am doing is adding teh cranberris(one liner break or fallthru to the case_main_body_list
	####################################################################
	### FALLING IN LOVE 
	print("======== Daft Punk =============")
	print("theory that there are blank lines at end of each case section")
	
	case_main_body_list_with_tail=['starter']
	#case_main_body_list_with_tail.append('starter')
	
	acounter=1
	print("inside of case_main_body_list")
	for item in range(1,len(case_main_body_list)):
		print(item)

	for item in range(1,len(case_main_body_list)):
		felix = case_main_body_list[item]
		print("what is in felix right here",felix)
		print("")
		# removes newlines after lines of code
		victory = felix.rstrip()
		print("victory looks like this", victory)
		print("what is in cranberries[acounter]",cranberries[acounter])
		print("")
		victory +="\n\t\t"+ cranberries[acounter] #tacks on break/fallthru
		print(victory)  #testing outpout
		case_main_body_list_with_tail.append(victory)  #appends the melding together to 
		
		victory=None
		victory=''
		                                 #case_main_body_list_with_tail
		print("--------------")
		
	
		acounter += 1
	
	print("we now have")
	print("this should be the case_main_body_list with the break and fallthurs ... we hope")
	for item in range(1,len(case_main_body_list_with_tail)):
		print(item)
	
	    
	    #case_main_body_list_with_tail.append(item + cranberries)  #how to add an extra line    
	    #create new list adding them together perhaps
	    
	
	############################
	print("================switch_code_gen () called ===========")
	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.


	 #name of  generated docstring switch_python_gen
	#print("varholder.append(exp)")
	#this is the final input code of switchcasetester
	print("================== finalized input of switch case code =======")
	print(switchcasetester) #to see what it sees

	#remembering one is printing
	#the other is generating (and printing to see it)
	#before it's executed the python switch case form

#this is the input for exp for switch(exp)
	##############
	topvars2 = "\nexp = varholder[0]\n\n"


	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:

	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(smartcasemanager)-1
	###################################################
	#   this is printing out the caselists at the top
	###################################################

	#--- testing dec 24th for varholder[0] input word ----
	#------------------------------------
	top_input_of_exp = "exp = varholder[0]" 
	
	# "varholder.append(exp)\n" +
	print("varholder[0] =",varholder[0])  
	#new line to see the input expression exp from clever

	#how do I determine if it's empty

	if not varholder:
		print("List is empty")
	else:
		print("varholder has something in it")
		print(varholder)
		#-------------------------
	# this prints the case lists of the words in each case section
	print("------- testing what is in each list dec 3oth -------")
	print("einstein list",einstein)
	print("====-=====")
	print("firstcasemanager list",smartcasemanager)
	print("-----------------------------------------")
	## ===========  LOOP =============
	#add default to end of einstein; this is because there is no actual default case
	#it's used as a lifesafter in case someone wantsto fallthru into default
	#I decided to create a default case but in the input it's not there

	einstein.append("default")  #adding default to the end of einstein copy list
	print('after the appending of default we have..')
	print("einstein list",einstein)
	print("----------------")
	print("now makeing each word lowercase for matching with cases")
	
	#res = list(map(lambda x: x.lower(), einstein ))
	#print(res)
	#newton=[]
	#for i in range(len(einstein)):
	#for i in einstein:
	#	answer = i.lower()
		#newton.append(answer)
	#print("newton list now is..")
	#print(newton)
	#
	#	#Iterate through einstein
	#	einstein[i] = einstein[i].lower()
	#print("einstein list now",einstein)
	print("=====")

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



		else:    #rest of cases after first case ======
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber
			caselistline = str(newlist[0]) + " " + str(newlist[1]) #=====
			extremelysmart.append(caselistline)
			firstpart.append(caselistline) #this ffeeds elif line into first part list
		
		######################
		#=== second part of each case section
		weasel= case_main_body_list_with_tail[mycounter]   ### RIGHT HERE 
		secondpart.append(weasel) #this feeds the string body into secondpart

		######################
		#=== third part of each case section
		#this is the tail either break or fallthru(name)
		
		###crans =tabs[2] + cranberries[mycounter]  #=====
		###thirdpart.append(crans) #this feeds the tail into thirdpart


		mycounter += 1     #loop counter
	###===== this is for the ELSE: at bottom of switch case
	#this is the default section else
	# end of regular cases
	#=== END LOOP  =========================

	################
	theelse = tabs[1] + "else:"  #this is just once
	firstpart.append(theelse) #this feeds the else clause into first part
	#this is the last real case after the regular cases

	##################3
	 #last case body for default

	lastishcase =case_main_body_list_with_tail[-1]

	secondpart.append(lastishcase)  #this feeds the body into secondpar

	##########################
	##trying = tabs[2] + cranberries[-1] #=====
	##thirdpart.append(trying) #this feeds the tail into thirdpart


	#practice printint out the three tier cakes for each section
	#print("below this line is the concatted output in strings")
	#print("first is the castlists from the top")
	#this works this creates the strings of the caselist at the top above switch correctly
###============================================
# caselists concatted to string cool
	cool=''

	#== LOOP === these are stored in list called testlist
	for item in testlist: #to see if the caselist names are in here  in this list
		cool += item + "\n"
		#print(item)
	#print("this is printing the string of each case from cool")
	cool += "\n\n"


################################################################################################
##### march 7th, 2021  I think I just add thirdpart to end of second part (it's just one line)
################################################################################################
#===case sections three parts at once ==")
	rocks=''
 #=====================
 #== LOOP
	counter=0  #each section will have the same number of items
	for item in firstpart:
		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n\n"# +str(thirdpart[counter]) + "\n\n"
		counter += 1
		#printing out the three part case sections")

	#a -----main list so sublists in the main list
	# so I only use ONE LIST for all three
	#adding strings together here

	sweet = topvars2 + cool + switchy + rocks
	#for debugging I will have a flag here to see output and test separately for user
	print("this is the javascript cleaned up before the translation")
	print(switchcasetester)
	print(sweet)

	print('===== executing generated  code=====')
	
	print("the input exp in clever was:: ",varholder[0]) #varholder[0]
	print("")
	exec(sweet)  #this is the building of the string of python code strings
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
	
	print("")
	print(" =====done executing output from switch ======")
	print("")
	print("testing this deletion of list with tail")
	case_main_body_list_with_tail=['']
	print("we have",case_main_body_list_with_tail)	
		
	print("now deleting this list case_main_body_list_with_tail")
	#case_main_body_list_with_tail=[] #hardcoded it to ensure it works
	firstpart=[]
	secondpart=[]
	thirdpart=[]
	extremelysmart=[]
	
	#switchcasetester='' #or del switchcasetester deletes it after done with it
	#january 16, 2021
	
	#print(case_main_body_list_with_tail)
	
	
		
	print(firstpart)
	print(secondpart)
	print(thirdpart)
	print(extremelysmart)
	#empty case_main_body_list, put "starter" into it
	#case_main_body_list=[]
	#case_main_body_list.append("starter")
	#if default == True
	#print('what they entered')








#======================================
'''
#  ====== project mr coffee ========
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():

	mytrace('switch_code_gen')
	#####
	##### march 7, 2021
	#new change putting penguin into cranberries
	#print("=== march 7th, 2021 testing===================///================================")
	#print("penguin=",penguin)
	#print("cranberries=",cranberries)
	#print("======")
	#Here I am putting the contents of penguin into cranberries
	#print("this is where I empty cranberries list and fill it with penguin")
	cranberries = []  #emptying cranberries here 
	for item in penguin:  #this works - how wonderful
		print(item)
		cranberries.append(item)
		
	#print("CrAnBeRRies-----  =",cranberries)
	
	###########  march 7, 20201  #######################################
	# I think that I just need to loop through casemainbodylist
	# and append cranberries based on teh counter and then eliminate the third tier below
	# what I am doing is adding teh cranberris(one liner break or fallthru to the case_main_body_list
	####################################################################
	### FALLING IN LOVE 
	#print("======== Daft Punk =============")
	#print("theory that there are blank lines at end of each case section")
	
	case_main_body_list_with_tail =[]
	case_main_body_list_with_tail.append('starter')
	
	acounter=1
	for item in range(1,len(case_main_body_list)):
		felix = case_main_body_list[item]
		# removes newlines after lines of code
		victory = felix.rstrip()
		victory +="\n\t\t"+ cranberries[acounter] #tacks on break/fallthru
		print(victory)  #testing outpout
		case_main_body_list_with_tail.append(victory)  #appends the melding together to 
		victory =''                                    #case_main_body_list_with_tail
		#print("--------------")
		
	
		acounter += 1
	
	#print("we now have")
	#print("this should be the case_main_body_list with the break and fallthurs ... we hope")
	for item in range(1,len(case_main_body_list_with_tail)):
		pass #print(item)
	
	    
	    #case_main_body_list_with_tail.append(item + cranberries)  #how to add an extra line    
	    #create new list adding them together perhaps
	    
	
	############################
	#print("================switch_code_gen () called ===========")
	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.


	 #name of  generated docstring switch_python_gen
	#print("varholder.append(exp)")
	#this is the final input code of switchcasetester
	#print("================== finalized input of switch case code =======")
	#print(switchcasetester) #to see what it sees

	#remembering one is printing
	#the other is generating (and printing to see it)
	#before it's executed the python switch case form

#this is the input for exp for switch(exp)
	##############
	topvars2 = "\nexp = varholder[0]\n\n"


	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:

	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(smartcasemanager)-1
	###################################################
	#   this is printing out the caselists at the top
	###################################################

	#--- testing dec 24th for varholder[0] input word ----
	#------------------------------------
	top_input_of_exp = "exp = varholder[0]" 
	
	# "varholder.append(exp)\n" +
	#print("varholder[0] =",varholder[0])  
	#new line to see the input expression exp from clever

	#how do I determine if it's empty

	if not varholder:
		print("List is empty")
	else:
		print("varholder has something in it")
		print(varholder)
		#-------------------------
	# this prints the case lists of the words in each case section
	#print("------- testing what is in each list dec 3oth -------")
	print("einstein list",einstein)
	#print("====-=====")
	#print("firstcasemanager list",smartcasemanager)
	#print("-----------------------------------------")
	## ===========  LOOP =============
	#add default to end of einstein; this is because there is no actual default case
	#it's used as a lifesafter in case someone wantsto fallthru into default
	#I decided to create a default case but in the input it's not there

	einstein.append("default")  #adding default to the end of einstein copy list
	#print('after the appending of default we have..')
	print("einstein list",einstein)
	#print("----------------")
	#print("now makeing each word lowercase for matching with cases")
	
	#res = list(map(lambda x: x.lower(), einstein ))
	#print(res)
	#newton=[]
	#for i in range(len(einstein)):
	#for i in einstein:
	#	answer = i.lower()
		#newton.append(answer)
	#print("newton list now is..")
	#print(newton)
	#
	#	#Iterate through einstein
	#	einstein[i] = einstein[i].lower()
	#print("einstein list now",einstein)
	#print("=====")

	for item in range(1,len(einstein)):     #first loop was smartcasemanager
		trains =  str(counter)
		merge = "caselist" + trains    #caselist1
		toosmart = eval(merge)
		###########################
		if int(trains) < 10: #adds another space
			caselist = merge + "  = " + str(toosmart)    #this is the caselist name we eval to display it
		else:
			caselist = merge + " = " + str(toosmart)    #this is the caselist name we eval to display it
		###########################
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



		else:    #rest of cases after first case ======
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber
			caselistline = str(newlist[0]) + " " + str(newlist[1]) #=====
			extremelysmart.append(caselistline)
			firstpart.append(caselistline) #this ffeeds elif line into first part list
		
		######################
		#=== second part of each case section
		weasel= case_main_body_list_with_tail[mycounter]   ### RIGHT HERE 
		secondpart.append(weasel) #this feeds the string body into secondpart

		######################
		#=== third part of each case section
		#this is the tail either break or fallthru(name)
		
		###crans =tabs[2] + cranberries[mycounter]  #=====
		###thirdpart.append(crans) #this feeds the tail into thirdpart


		mycounter += 1     #loop counter
	###===== this is for the ELSE: at bottom of switch case
	#this is the default section else
	# end of regular cases
	#=== END LOOP  =========================

	################
	theelse = tabs[1] + "else:"  #this is just once
	firstpart.append(theelse) #this feeds the else clause into first part
	#this is the last real case after the regular cases

	##################3
	 #last case body for default

	lastishcase =case_main_body_list_with_tail[-1]

	secondpart.append(lastishcase)  #this feeds the body into secondpar

	##########################
	##trying = tabs[2] + cranberries[-1] #=====
	##thirdpart.append(trying) #this feeds the tail into thirdpart


	#practice printint out the three tier cakes for each section
	#print("below this line is the concatted output in strings")
	#print("first is the castlists from the top")
	#this works this creates the strings of the caselist at the top above switch correctly
###============================================
# caselists concatted to string cool
	cool=''

	#== LOOP === these are stored in list called testlist
	for item in testlist: #to see if the caselist names are in here  in this list
		cool += item + "\n"
		#print(item)
	#print("this is printing the string of each case from cool")
	cool += "\n\n"


################################################################################################
##### march 7th, 2021  I think I just add thirdpart to end of second part (it's just one line)
################################################################################################
#===case sections three parts at once ==")
	rocks=''
 #=====================
 #== LOOP
	counter =0  #each section will have the same number of items
	for item in firstpart:
		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n\n"# +str(thirdpart[counter]) + "\n\n"
		counter += 1
		#printing out the three part case sections")

	#a -----main list so sublists in the main list
	# so I only use ONE LIST for all three
	#adding strings together here
	#the generated pieces of the coded are generated top down and added sideways
	sweet = topvars2 + cool + switchy + rocks
	#for debugging I will have a flag here to see output and test separately for user
	#print("this is the javascript cleaned up before the translation")
	#print(switchcasetester)
	
	
	#there are two of these one for numbers and one for strings
	#print(sweet)
	if show_py_switch[0] == True:
		print(sweet)
	else:
		#print('not showing generated python switch case code since flag = False')
		pass
		
	#print('===== executing generated  code=====')
	
	print("the input exp in clever was:: ",varholder[0]) #varholder[0]
	print("")
	exec(sweet)  #this is the building of the string of python code strings
	# this runs the python switch code as ifs with the input
	# hard coded into it
	#print("")
	#print(" =====done executing output from switch ======")
	#print("")
	#switchcasetester='' #or del switchcasetester deletes it after done with it
	#january 16, 2021
	
	#empty case_main_body_list, put "starter" into it
	#case_main_body_list=[]
	#case_main_body_list.append("starter")
	#if default == True
	#print('what they entered')
'''






'''
#  ====== project mr coffee ========
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():
	mytrace('switch_code_gen')
	case_main_body_list_with_tail=[]
	case_main_body_list_with_tail.append('starter')
	#print("starting out this is what is in  case_main_body_list_with_tail")
	#print(case_main_body_list_with_tail)
	#####
	##### march 7, 2021
	#new change putting penguin into cranberries
	#print("=== march 7th, 2021 testing===================///================================")
	#print("penguin=",penguin)
	#print("cranberries=",cranberries)
	#print("======")
	#Here I am putting the contents of penguin into cranberries
	#print("this is where I empty cranberries list and fill it with penguin")
	cranberries = []  #emptying cranberries here 
	for item in penguin:  #this works - how wonderful
		print(item)
		cranberries.append(item)
		
	#print("CrAnBeRRies-----  =",cranberries)
	
	###########  march 7, 20201  #######################################
	# I think that I just need to loop through casemainbodylist
	# and append cranberries based on teh counter and then eliminate the third tier below
	# what I am doing is adding teh cranberris(one liner break or fallthru to the case_main_body_list
	####################################################################
	### FALLING IN LOVE 
	#print("======== Daft Punk =============")
	#print("theory that there are blank lines at end of each case section")
	#breakpoint()
	
	
	print("starting out in codegen cranberries=",cranberries)
	acounter=1
	for item in range(1,len(case_main_body_list)): #it skips the first one
		print("the last f'n bug is right here")
		print("case_main_body_list =",case_main_body_list)
		felix = case_main_body_list[item]
		print("felix=",felix)
		# removes newlines after lines of code
		victory = felix.rstrip()
		print("victory here shows",victory)
		print("cranberries[acounter]=",cranberries[acounter])
		################################
		victory +="\n\t\t"+ cranberries[acounter] #tacks on break/fallthru
		print(victory)  #testing outpout
		case_main_body_list_with_tail.append(victory)         #appends the melding together to 
		victory =''  #this clears out the variable victory    #case_main_body_list_with_tail
		print("--------------")
		acounter += 1
	
	#print("we now have")
	#print("this should be the case_main_body_list with the break and fallthurs ... we hope")
	#for item in range(1,len(case_main_body_list_with_tail)):
	#	pass #print(item)
	
	    
	    #case_main_body_list_with_tail.append(item + cranberries)  #how to add an extra line    
	    #create new list adding them together perhaps
	    
	
	############################
	#print("================switch_code_gen () called ===========")
	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.


	 #name of  generated docstring switch_python_gen
	#print("varholder.append(exp)")
	#this is the final input code of switchcasetester
	#print("================== finalized input of switch case code =======")
	#print(switchcasetester) #to see what it sees

	#remembering one is printing
	#the other is generating (and printing to see it)
	#before it's executed the python switch case form

#this is the input for exp for switch(exp)
	##############
	topvars2 = "\nexp = varholder[0]\n\n"


	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:

	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(smartcasemanager)-1
	###################################################
	#   this is printing out the caselists at the top
	###################################################

	#--- testing dec 24th for varholder[0] input word ----
	#------------------------------------
	top_input_of_exp = "exp = varholder[0]" 
	
	# "varholder.append(exp)\n" +
	#print("varholder[0] =",varholder[0])  
	#new line to see the input expression exp from clever

	#how do I determine if it's empty

	if not varholder:
		print("List is empty")
	else:
		print("varholder has something in it")
		print(varholder)
		#-------------------------
	# this prints the case lists of the words in each case section
	#print("------- testing what is in each list dec 3oth -------")
	print("einstein list",einstein)
	#print("====-=====")
	#print("firstcasemanager list",smartcasemanager)
	#print("-----------------------------------------")
	## ===========  LOOP =============
	#add default to end of einstein; this is because there is no actual default case
	#it's used as a lifesafter in case someone wantsto fallthru into default
	#I decided to create a default case but in the input it's not there

	einstein.append("default")  #adding default to the end of einstein copy list
	#print('after the appending of default we have..')
	print("einstein list",einstein)
	#print("----------------")
	#print("now makeing each word lowercase for matching with cases")
	
	#res = list(map(lambda x: x.lower(), einstein ))
	#print(res)
	#newton=[]
	#for i in range(len(einstein)):
	#for i in einstein:
	#	answer = i.lower()
		#newton.append(answer)
	#print("newton list now is..")
	#print(newton)
	#
	#	#Iterate through einstein
	#	einstein[i] = einstein[i].lower()
	#print("einstein list now",einstein)
	#print("=====")

	for item in range(1,len(einstein)):     #first loop was smartcasemanager
		trains =  str(counter)
		merge = "caselist" + trains    #caselist1
		toosmart = eval(merge)
		###########################
		if int(trains) < 10: #adds another space
			caselist = merge + "  = " + str(toosmart)    #this is the caselist name we eval to display it
		else:
			caselist = merge + " = " + str(toosmart)    #this is the caselist name we eval to display it
		###########################
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



		else:    #rest of cases after first case ======
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber
			caselistline = str(newlist[0]) + " " + str(newlist[1]) #=====
			extremelysmart.append(caselistline)
			firstpart.append(caselistline) #this ffeeds elif line into first part list
		
		######################
		#=== second part of each case section
		weasel= case_main_body_list_with_tail[mycounter]   ### RIGHT HERE 
		secondpart.append(weasel) #this feeds the string body into secondpart

		######################
		#=== third part of each case section
		#this is the tail either break or fallthru(name)
		
		###crans =tabs[2] + cranberries[mycounter]  #=====
		###thirdpart.append(crans) #this feeds the tail into thirdpart


		mycounter += 1     #loop counter
	###===== this is for the ELSE: at bottom of switch case
	#this is the default section else
	# end of regular cases
	#=== END LOOP  =========================

	################
	theelse = tabs[1] + "else:"  #this is just once
	firstpart.append(theelse) #this feeds the else clause into first part
	#this is the last real case after the regular cases

	##################3
	 #last case body for default

	lastishcase =case_main_body_list_with_tail[-1]

	secondpart.append(lastishcase)  #this feeds the body into secondpar

	##########################
	##trying = tabs[2] + cranberries[-1] #=====
	##thirdpart.append(trying) #this feeds the tail into thirdpart


	#practice printint out the three tier cakes for each section
	#print("below this line is the concatted output in strings")
	#print("first is the castlists from the top")
	#this works this creates the strings of the caselist at the top above switch correctly
###============================================
# caselists concatted to string cool
	cool=''

	#== LOOP === these are stored in list called testlist
	for item in testlist: #to see if the caselist names are in here  in this list
		cool += item + "\n"
		#print(item)
	#print("this is printing the string of each case from cool")
	cool += "\n\n"


################################################################################################
##### march 7th, 2021  I think I just add thirdpart to end of second part (it's just one line)
################################################################################################
#===case sections three parts at once ==")
	rocks=''
 #=====================
 #== LOOP
	counter =0  #each section will have the same number of items
	for item in firstpart:
		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n\n"# +str(thirdpart[counter]) + "\n\n"
		counter += 1
		#printing out the three part case sections")

	#a -----main list so sublists in the main list
	# so I only use ONE LIST for all three
	#adding strings together here
	#the generated pieces of the coded are generated top down and added sideways
	sweet = topvars2 + cool + switchy + rocks
	#for debugging I will have a flag here to see output and test separately for user
	#print("this is the javascript cleaned up before the translation")
	#print(switchcasetester)
	
	
	#there are two of these one for numbers and one for strings
	#print(sweet)
	if show_py_switch[0] == True:
		print(sweet)
	else:
		#print('not showing generated python switch case code since flag = False')
		pass
		
	#print('===== executing generated  code=====')
	
	print("the input exp in clever was:: ",varholder[0]) #varholder[0]
	print("")
	exec(sweet)  #this is the building of the string of python code strings
	# this runs the python switch code as ifs with the input
	
	#emptying case main body list with tail
	#case_main_body_list_with_tail=[] #empty it
	#print("case_main_body_list_with_tail=[]",case_main_body_list_with_tail)
	
	#print("trying to empty this dam list")
	#for item in range(0,len(case_main_body_list_with_tail)):
	#	case_main_body_list_with_tail.pop()
		
	#print("the value of case_main_body_list_with_tail")
	#print(case_main_body_list_with_tail)
		
		
	#just empty it right here to solve the problem
	#case_main_body_list_with_tail=[]
	# hard coded into it
	#print("")
	#print(" =====done executing output from switch ======")
	#print("")
	#switchcasetester='' #or del switchcasetester deletes it after done with it
	#january 16, 2021
	
	#empty case_main_body_list, put "starter" into it
	#case_main_body_list=[]
	#case_main_body_list.append("starter")
	#if default == True
	#print('what they entered')


'''

#this executes the generated python switch code
def stage_twelve():
	gti=[] #clears out gti list 
	mytrace('stage_twelve()')
	#changing to run second switch case january 15, 2021
	switchcasetester =''
	sw =''
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
	
	print("defaultlist=",defaultlist)
	print("candy=",candy)
	print('digitalcandy=',digitalcandy)
	print("palmtrees=",palmtrees)
	print("how many of these have data in them after the first switch?")
	print("gti",gti)
	print("mochalist",mochalist)
	print("drive_thru",drive_thru)
	#funny
	print("case1findbreak",case1findbreak)
	print("case1findfallthru",case1findfallthru)
	print("seal",seal)
	print("line_number_of_first_cases",line_numbers_of_first_cases)
	print("case_main_body_list=",case_main_body_list)
	#print("case_main_body_list_with_tail",case_main_body_list_with_tail)
	
	
	print("candy=",candy)
	print("starbucklist=",starbuckslist)
	print("digitalcandy=",digitalcandy)
	print("einstein=",einstein)
	print("wilecoyote=",wilecoyote)
	print('birdsong=',birdsong)
	print("cranberries =",cranberries)
	print("royallist =",royallist)
	print("roadrunner =",roadrunner)
	print("penguin =",penguin)
	print("british =",british)
	#print('stage twelve')

	print("caselist1=",caselist1)
	print("caselist2=",caselist2)
	print("caselist3=",caselist3)
	print("caselist4=",caselist4)
	print("caselist5=",caselist5)
	print("caselist6=",caselist6)
	print("caselist7=",caselist7)
	print("caselist8=",caselist8)
	print("caselist9=",caselist9)
	print("caselist10=",caselist10)
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
	print("gti",gti)
	for item in range(0,len(gti)):
		british.gti()
		
	print("mochalist",mochalist)
	for item in range(0,len(mochalist)):
		mochalist.pop()
		
	print("drive_thru",drive_thru)
	for item in range(0,len(drive_thru)):
		drive_thru.pop()
	#funny
	print("case1findbreak",case1findbreak)
	for item in range(0,len(case1findbreak)):
		case1findbreak.pop()
		
	print("case1findfallthru",case1findfallthru)
	for item in range(0,len(case1findfallthru)):
		case1findfallthru.pop()
		
	print("defaultlist",defaultlist)
	for item in range(0,len(defaultlist)):
		defaultlist.pop()
			
	print("seal",seal)
	for item in range(0,len(seal)):
		seal.pop()
	print("this one is the HOLY GRAIL one")
	print("line_number_of_first_cases",line_numbers_of_first_cases)
	for item in range(0,len(line_numbers_of_first_cases)):
		line_numbers_of_first_cases.pop()	

	print('==== after clearing them we have ======')
	
	if len(palmtrees) > 0:
		palmtrees.pop()
	print('after checking the length of the list this deletes more if greater than 0')
	print("palmtrees=",palmtrees)
	print("starbucklist=",starbuckslist)
	for item in digitalcandy:
		digitalcandy.pop()

	print("digitalcandy=",digitalcandy)
	
	if len(einstein) > 0:
		einstein.pop()
		
		
	print("candy=",candy)
	print("defaultlist=",defaultlist)	
	print("einstein=",einstein)
	print("wilecoyote=",wilecoyote)
	print('birdsong=',birdsong)

	print('british=',british)
	print('penguin=',penguin)
	print('royallist=',royallist)
	print('cranberries=',cranberries)
	print('roadrunner=',roadrunner)
	print('case_main_body_list=',case_main_body_list)
	#print('case_main_body_list_with_tail=',case_main_body_list_with_tail)

	#if len(caselist1) > 0:
	#	caselist1.pop()

	print("caselist1=",caselist1)
	print("caselist2=",caselist2)
	print("caselist3=",caselist3)
	print("caselist4=",caselist4)
	print("caselist5=",caselist5)
	print("caselist6=",caselist6)
	print("caselist7=",caselist7)
	print("caselist8=",caselist8)
	print("caselist9=",caselist9)
	print("caselist10=",caselist10)
	
	print("are these empty now for a clean slate after first switch?")
	print("gti",gti)
	print("mochalist",mochalist)
	print("drive_thru",drive_thru)
	#funny
	print("case1findbreak",case1findbreak)
	print("case1findfallthru",case1findfallthru)
	print("seal",seal)
	print("this one is the Big Deal line_numbers_of_first_cases needs to be empty")
	print("It was previously not being emptied obviously ... now it is")
	print("apparently this one REALLY needs to be empty or I am screwed")
	print("line_number_of_first_cases",line_numbers_of_first_cases)
	
	#print('stage twelve')




#==========================================================================================
#===== this is test what will be generated below after the python switch is generated above



####======= this is the input to the python switch
#input_list = ["fortune"]  #global var that will be fed into switch(x)





#def bigtestofcodegen():
#	mytrace('bigtestofcodegen')
#	#print('BIG TEST OF CODE GEN CALLED  this executes the python switch case')
#	#print("===== massive test =======")







list1=[]
list1.append("five")









#researched it on the web for exec(string)
#.Another solution is to write that string to
#a temporary python file and execute it.

#My other thought is to dynically write it into a function
#and then call the function





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
	#print("gti=",gti)
	#print("palmtrees=",palmtrees)
	#print("royallist=",royallist)
	#print("woodstock=",woodstock)
	#print("candy=",candy)
	#print("smartcasemanager=",smartcasemanager)
	#print("einstein=",einstein)
	#print("varholder=",varholder)
	#print("british=",british)
	#print("cranberries=",cranberries)

#case_main_body_list=[]
#this is new but I haven't tried 
##################################
## starter sequence mode 1
##################################
#this is for parsing and codegen of cases with words only
def starter_sequence_mode_1():
	#this if means this can only run if valve[0] is False not numbers
	if valve[0] == False: #means cases are words like "apple pie"
		mytrace('starter_sequence_mode_1()')
		#print('------------starter_sequence mode 1 called here ---------->>>>>')
		#print('------------starter_sequence mode 1 called here ---------->>>>>')
		#print('------------starter_sequence mode 1 called here ---------->>>>>')
		#case_main_body_list=[] #this shoudl work january 16th, saturady night 2021
		#case_main_body_list.append('starter') 
		#print("oh my god starter_sequence called will it work???")
		convert_case_line_to_lowercase()
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
		print('stopping just before switch_code_gen()')
		#quit() #see if this works
		switch_code_gen() #  <<<==============it's called right here the code generator
		stage_twelve()  # <== this resets the lists for next use of switch
		
		clearit()
		global woodstock
		#print("what we have in woodstock=",woodstock)
		#print("now we clear out woodstock list")
		woodstock =[]
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
		print("british=",british)
		penguin=[]
		print("penguin=",penguin)
		clear_out_all_case_lists() #doing 16 for now
		show_tron_trace_path()
	else:
		pass
		
	
	showit()
	empty_test() #test of global list
	
	#flush_lists() #this is new january 16th, saturday debugging trying second switch case
	
daisy=''
###########################
####  PARSER  ############# does strings words
###########################
#def parser_mode_1(a):
#	mytrace('parser in switch_mgrcat() seeing if this is called or not')
#	print('=======INSIDE OF PARSER in switch_mgrcat  =========')
#	print("INSIDE of parser_mode_1() which isdoing strings words ")
#
#
#	#felix()  #testing with switchcasetester string
	#mtv()
#	mountain(a)
#	starter_sequence_mode_1()  ######
	#print(valve[0])
	#print("inside of the ParSer() calling starter sequence with")
	# print("the user of value of valve[0]", valve[0])
	# print("so the actual FLOW VALVE is at top of PARSER")
	# if valve[0] == False: #meaning string words not numbers
	# 	mytrace('inside of parser in switch_mgrcat()', valve[0])
	# 	print("valve[0]== False")
	# 	print("this is not numbers so doing string word parser")
	# 	print("#################################")
	# 	print("#################################")
	# 	print('about to call starter sequence')
	# 	starter_sequence_mode_1()  #words strings
	# elif valve[0] == True:
	# 	mytrace('inside of parser in switch_mgrcat in elif valuve[0] =True()',valve[0])
	# 	print("valve[0] == True it's numbers !!!@!@#@#####")
	# 	print("its numbers later")
	# 	print("in near future calling pumpkins for numbers")
	#donaldduck()
	 #numbers
		#return
	#end if flow valve


import re
def hasNumbers(inputString):
		return bool(re.search(r'\d',inputString))


#########################
##  endswitch()
#########################
#def endswitch(y):
	#print("this will do the check if number in first case line in switch case")
	#print("the it will do the flow of control flow valve determining which")
	#print("pasers to call and now both parsers will be in this file.")
	#testing if this is even called or not 
	#print("=============== about to do the Flow Valve of Control =========")
	#print("value of valve[0] == ",valve[0])
	#if valve[0] == True:  # so thus do numbers switch parser
#		print("valve[0] == True thus numbers", valve[0])
	#	if valve[0] == True:
	#		print("======DO NUMBERS SWITCH==== ")
	#	colin() #<==== you are now a function
	#	donaldduck()
	#	parser_mode_2(y) #this calls parser() abobve and passes in 
	#else:  #it must be false if not true and therefore do strings switch words
	#	if valve[0] == False:
	#		print("=====DO STRING SWITCH ===")
	#	print("inside of endswitch it sees this in valve[0]", valve[0])
	#	print("valve[0] == False thus strings", valve[0])
	#	parser_mode_1(y) #this calls parser() abobve and passes in 

	############################
	
			

##############  added April 2nd, 2021  ###############################################
# this is a pre scan of the switch case input string to determine if
# the cases are numbers like case 1 thru 5: or case 10 OR words like case "apple":
coffee=[]  #holds line number of first case in switch case
valve=[]
valve.append("nada")# 0
valve.append("sway")# 1

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
	print(coffee[0])  #testing what's in this
	getline= eval("y.splitlines()[" + str(coffee[0]) + "]")
	print(getline)
	return getline


##################################
##  check_if_number_in_string(x)
################################## 
def check_if_number_in_string(x):
	mytrace("check_if_number_in_string()") 
	theresult = any(char.isdigit() for char in x)  #this line from stackoverflow
	return theresult

###################
## parser_mode_1()
##################
## testing April 3rd 2021 seeing if this works or not. 
def parser_mode_1(a):
	print("a= ",a)
	mytrace('parser_mode_1 in switch_cat()') #was greatpumpkin
	print('=======INSIDE OF PARSER in switch_cat for strings  =========')
	mountain2(a)    # this changes sw to switchcasetester #I can't beleive that this reverse number was being called 
	starter_sequence_mode_1()
# flow_fork_input()  #this fills valve[0] with True or False
# if valve[0] is True  it means numbers = True  (thus numbers      )
# if valve[0] is False it means numbers = False (thus words strings)
## the new code will go in here Friday morning.. April 2, 2021
#this fills valve[0] with True or False for numbers in cases
#################################
##  flow_valve_input(y)
##################################
def flow_valve_input(y):  #this determines if switch case string is numbers or words
    print("Flow Valve input")
    mytrace("flow_valve_input()")                            #get first case in switch case string
    getline  = grab_first_case_of_switch_string(y)           #get first case line
    toocool  = grab_first_case_line_in_switch_case_string(y) #remove tabs from the case line
    toocool  = remove_tabs_from_string(toocool)              #test if number in first case line yes = True no = False
    valve[0] = check_if_number_in_string(toocool)            #looks in case line
    valve[1] = toocool                                       #put case name/number into valve[1]
    print("valve[0]=",valve[0]," and valve[1]=",valve[1])
    print("========")
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


#flow valve_input called in endswitch
# this looks quickly at the first case in the switch string
	# and checks if the first case is a number or a word/char
	# if it's a number it refturns True else it returns False
	##################################################
	# the output from the flow valve is 
	# if numbers = True  put True  into valve[0]
	# if numbers = False put False into valve[0]
	#this says if numbers == True
	
########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	
	#---------reloading switch_module--------
	
	#---------------------------------------
	mytrace("endswitch() in switch_cat called")
	print("we have an input argument parameter y",y)
	#this determines if switch case string uses numbers or words/chars
	#####################
	flow_valve_input(y)   #puts True or False into valve[0] added April 2nd, 2021
	#####################
	if valve[0] == True: #this says numbers = True
		#print("valve[0] == True thus numbers", valve[0])
		#print("valve[1]=",valve[1])
		#breakpoint()
		#NUMBERS PARSER AND CODEGEN
		flush_lists() #new just addd april 7th triggered before parser starts
		parser_mode_2(y) 
	else: #if numbers == False    and therefore it's strings words
		#This means do strings words parser
		#means valve[0] == False:
		#print("valve[0] == False ", valve[0])
		#print("this means numbers = False so do words")
		#print("valve[1]=",valve[1])
		#WORDS PARSER AND CODEGEN
		#breakpoint()
		flush_lists() # new just added april 7th
		parser_mode_1(y) 
	

	#uses method hasNumbers to determine if a string has number in it.
	#this looks in the first line with case in the switch case string
	# to determine if there is a number in it yes or not
	# if number in it then to switch with numbers = true
	# if no number in it then do with numbers == false
	#money= hasNumbers(toowild)  #returns True or False
	#print("the result of if number in first case line =",money)
	#print("is there a number in the string",money)
	#valve[0] = money
	#print(valve[0])
	##############

	


	

	

	
	
	#sw to a andto mountain2 as an argument it is really getting sw



#starter_sequence()

#this way starter_sequence is called below it's definition
#if this is the bug I will be happy and still aggrivated
#my theory is based on the stages which do the same thing
#of being called afterwards but managing the function calls
#that seem to be localized.


# to run this code to parse and generate the python version of
# the javascript switch case into python if tree run
#starter_sequence()



#starter_sequence() #this will be triggered from the parser

# I need to have a function start the code running
  