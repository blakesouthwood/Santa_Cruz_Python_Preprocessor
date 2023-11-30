#from goldfish import switchcasetester
import switch_config  #what do these two imports mean and do?????
import switch_subfile

import sw_module_extra
#also do this for reset below

digitalcandy=[]
######################### reset()  the module ##########
####### this makes it possible to call multiple switch cases that start out empty
######################################
def reset():
    import importlib
    import march_4_21_firefall_yosemite_falls   #add to add new front of filename
    importlib.reload(march_4_21_firefall_yosemite_falls)  #and add it here too

def change_list(zoo):
    #print("change_list() calleed")
    switch_config.init()
    switch_subfile.stuff(zoo)
    print(switch_config.mylist[0])
    
  
change_list("The Simpson's cartoon")
print(switch_config.mylist)


change_list("funny times")
print(switch_config.mylist)

    ############################
    ### get_case_name()
    ############################
def get_case_name(y):  #y will be the line
    print("get_case_name called")
    #y = y.split()
    y = y.replace(":","")
    y = y.replace("case","") #remove case
    y = y.replace("\t","")    # remove :
    print(y)
    return y
    
    
    
    ############################
    ### get_location_of_case()
    ############################
def get_location_of_case(listname,word):
    print("listname,word=",listname,word)
    print("get location of case () called ")
    print("this is searching for ",word)  #below took out  + "'" + both sides of word
    answer =eval("" + listname + ".index("  + word + ")")
    print('====after running get_location_of_case we get this== should be a number==')
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
	print("====== read string from file called ======")
	print("=== READ_FILE_PUT_INTO_STRING====")
	f = open("sw_test.txt", "r")
	boomerang = f.read()
	print("=====output of string here=======")
	print(boomerang)
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
	print("######## get_length_of_string() called")
	print("get length of string() called ====== ")
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
		
	print("length of the string =",counter)
	the_counter=mrdefault
	print("we are starting to count from ",the_counter)
	solution ="false"
	for line in switchcasetester.splitlines():
		if "break" in line:
			print('yes break after default')
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
	mytrace('wise_owl()')
	print("##### wise_owl() called with",t)
	print("WISE OWL CALLED with ",t)
	print("wise owl() called to add break to default case if it is missing ====== door number 3")
	print("wise_owl input t =",t)
	if t == True:
		print('already a break in default case')
	else:
		print("it's obviously FALSE so add break to switchcasetesterstring")
		print('no break detected so adding break at bottom of default')
		global switchcasetester
		print("switchcasetester=",switchcasetester)
		################################################################
		#### THIS IS WHERE WE ADD A  BREAK AFTER DEFAULT IF ITS MISSING  ####### 
		#######################################################################
		strawberry=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = strawberry
		print("=====after adding break to bottom of default we have====== ")
		print(switchcasetester)
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
	print("######## testing_if_break_in_default_tail() called############")
	print("testing if break in default tail() called=====DOOR NUMBER 2 ===")
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

angel =''

#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
	reset()  #reset() is hidden inside of clever for input to the switch
	print("clever called for input to switch case exp")
	varholder[0]= i
	#this works and it fills a list with input from an argument
	print('varholder[0]=',varholder[0])
	print(varholder[0]) #to actually see proof
	#return varholder[0]
	angel = varholder[0]


#apparently this needs to exist in this file
def sneaky(i): #so it already exists we are changing its value
    
	print("clever called for input to switch case exp")
	varholder1[0]= i
	#this works and it fills a list with input from an argument
	print('varholder[0]=',varholder[0])
	print(varholder[0]) #to actually see proof







global sw

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





def adjust_input(x):
	print("adjust input called with", x, "inside of yosemite")
	newstring =varholder.append(' + x + ')



# Remember that the output code gen is invisible and won't be seen by
# he programmer
case = ''
# =======  switch  =================================
def switch(x):
	global case
	#strings
	#print("switch method called",x)
	#if string
	if type(x) == str:
		x = str(x)
		case = x.lower()
	
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
##################################

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




coyote_list=[]  #initialize it
#trontime= ['empty', 'switch', 'case', 'case', 'code;', 'code;', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'break', 'empty', 'case', 'case', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'default', 'code;', 'code;', 'break', 'code;']


# I can simply fill it manually with a loop and append
#print(trontime)

birdsong=[0]
music=[0]
colorful=[0]
#######################################
def make_list_of_first_cases():
#######################################
	mytrace('make_list_of_first_cases')
	print("========== called make list of first cases() ===========")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			smart=line.split() #separates case from casename
			#print(smart[1])
			birdsong.append(smart[1]) #this adds casenameto list birdson
			print("testing to see if this is where I'm making a mistake with the case names")
			print(birdsong) # I might be only adding the first word that might be the bug january 3rd 2021
			music.append(mycounter) #list of number for case line
			mycounter += 1
		else:
			mycounter +=1

	print("I think that the list of line numbers of cases is called music",music)
	print("list of first case names",birdsong)


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
	print("### @@@@@ simple test looking for any break in switch case string switchcasetester")
	#if "break" in switchcasetester:
	#	print("yes there is a break")
	#	
	#lse: #this means there are no breaks in the switchcase string
	#	listofbreaks.append("0")  ## this is new 
	#	print("no break in switch case")
	
	print("starting loop looking for breaks in switch case")
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			nobreaks = "false"	
			counter +=1
		else:
			counter += 1
			continue
		###=============
	print(switchcasetester)
	print("testing length of listofbreaks list")
	print("if no breaks in switch case then add a break after default now")
	if len(listofbreaks) == 0:
		print("list of breaks is empty")
		print("therefore there is no break in entire string ")
		print("this means no break in default")
		print("adding break at bottom of default case now")
		#global switchcasetester
		#this immediatley adds break after default
		courage=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = courage
		print("we now have ((look for the new break in default")
		print(switchcasetester)
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
		print("the list of breaks has",len(listofbreaks), " elements")
	#idea if no breaks add one
	genius = listofbreaks[-1]  #last break number
	print("genius is the last break line number =",genius)
	
	if counter == 0: #means no breaks in string of switchcasetester
		print("there aren't any breaks in the switch case")
		nobreaks = "true"
		print("nobreaks = true")
	else: #counter greater than 0
		nobreaks = "false"
		print("nobreaks = false")
		pass

	print("lets see the list of breaks full list",listofbreaks)
	print("the length of hits of lines with break so the length is ",len(listofbreaks))
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
	print("=== GhostBusters===")
	print("get_default line number=",get_default) #line number of default
	print("lets see the LIST OF BREAKS  full list",listofbreaks)
	
	
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
	print("the last line of string =",last_line_of_string)
	print("NOW I HAVE ALL THAT I NEED TO GET THIS TO WORK CORRECTLY TONIGHT!!!!")
	print("=====GhostBusters ===")
	
	print("WHAT DOES THIS NUMBER SAY===========........>>>>>>?")
	print("======GhostBusters ==============")
	print("get_default=",get_default) #line number of default
	print("last break =",last_break)  #next figure out if NO BREAK WHATSOEVER
	print("last line  =",last_line_of_string)
	print("the result therefore is:")
	if int(last_break) < int(get_default):
		print("there is definitely no break in default case")
		print("and a break needs to be added immediately")
		######################################################
		print("adding break at bottom of default case now")
		global switchcasetester
		tang=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester=''
		switchcasetester = tang
		print("we now have ((look for the new break in default")
		print(switchcasetester)
	else:
		print("there is a break inside of default")
	
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
	print("this if test for get_default < last_break fails if no break in string")
	print("it's based on the bad assumption that there is a break in the switch case")
	print("so I need to modify it to check if there is a break in the whole string")
	print("and if count('break') == 0 then the answer is None")
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







print("this is actual generated code I am trying to run now....")
print("this is betterworknow in python generated previously")



list1=[]
exp =''; case =''
exp = ""

#exec(betterworknow)
print("=== executin betterwork now test bit")




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
    
      
### right here I need to add
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
	#print("this will go first")
	### convert default case and then test if break in default and add break if necessary
	#this is done because in C and javascript it's just:   default: so it needs to be converted to a case
	#I will have it add break inside of convert_default_case()
	#convert default case called here 
	convert_default_case() #this changes default: to case 'default': but default needs to exist!
	# I can't assume that default has a break because in C it's not necessary but here it's needed 
	output = testing_if_break_in_default_tail()
	#right here
	wise_owl(output) #this should feed in the parameter of if break between default and last line of string
	








#this resets all of the lists
##### flush_lists() ##############
def flush_lists():
	switchcasetester = ''
	sw=''
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
	#deepsea_line_numbers=[] #experimental

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
    print('in here now')
    foo =[1]
    print(foo)

#bar()

def goldmedal():
    global foo
    print(foo)
    foo.append("xmas time")
    print(foo)
    
#goldmedal()

def silvermedal():
    global foo
    foo.pop(0)
    print(foo)
    foo.append("nighttime")
    print(foo)
    
    
#silvermedal()

def coolness():
    global foo
    foo=[]
    print(len(foo))
    
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
    
#badass()

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
    print('stage one')
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
global candy
#####this is where i'm testing now
line_numbers_first_cases =[]        

woodstock =[]  #testing this out   
candy =[]  #for digital candy
#==================================     
def simple_test():  #call this when clever(input) called
    print("================")
    print("simple test of filling global list") # to clear out list to make sure it's empty 
    global line_numbers_first_cases
    print('in here now')
    print(line_numbers_first_cases)
    line_numbers_first_cases =['snoopy','linus','lucy','woodstock']
    print(line_numbers_first_cases)
    print("=============")

simple_test()   


def add_to_test_list():
    print("==================")
    print("add to test list attempt")
    global line_numbers_first_cases
    print("in here now")
    print(line_numbers_first_cases)
    print("now adding three more words to it")
    line_numbers_first_cases.append("rediculous")
    line_numbers_first_cases.append("silly")
    line_numbers_first_cases.append("tired")
    print(line_numbers_first_cases)
    print("====================")
            
def empty_test():  #call this when clever(input) called
    print("===============")
    print("empty list") # to clear out list to make sure it's empty 
    global line_numbers_first_cases
    print('in here now')
    line_numbers_first_cases =['starter']
    print(line_numbers_first_cases)        
    print("==================")
        
        
        
        
        
##################################################
def magictimenow():   ### this builds the list for line_numbers_of_first_cases
##################################################
	
	#this should make it real
	global woodstock
	print("woodstock contains=",woodstock)
	global candy
	print("candy contains=",candy)
	print("switchcasetester=",switchcasetester)
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



this is chat gpt refactoring below nov 30 2023 for a comparison
def magictimenow():
    """Analyzes the switch case code and identifies various elements, including
    first case lines, trontime locations, fallthru locations, break positions,
    and first case list."""

    global switchcasetester
    global woodstock
    global candy

    # Initialize variables
    counter = 1
    word = 0
    mycounter = 0

    # Create lists to store various information
    firstcaselist = []
    smartnewlist = []
    smartlistlocations = []
    fallthrulocations = []
    breakposition = []
    getfirstword = []
    trontime = []
    line_numbers_of_first_cases = []

    # Iterate through the lines of the switch case
    for line in switchcasetester.splitlines():
        genius = line.split()
        mycounter += 1

        # Check for specific keywords and add them to the corresponding lists
        if "case" in line:
            trontime.append("case")
        elif "switch" in line:
            getfirstword.append("switch")
            trontime.append("switch")
        elif "fallthru" in line or "fallthrough" in line:
            getfirstword.append("fallthru")
            trontime.append("fallthru")
            smartlistlocations.append(mycounter)
            fallthrulocations.append(mycounter)
        elif "break" in line:
            trontime.append("break")
            breakposition.append(mycounter)
        elif "default" in line:
            getfirstword.append("default")
            trontime.append("default")
        elif len(line.strip()) == 0:
            getfirstword.append("empty")
            trontime.append("empty")
        else:
            getfirstword.append("code;")
            trontime.append("code;")

    # Identify the line numbers of the first cases
    acounter = 0
    for line in switchcasetester.splitlines():
        if "case" in line and "case" not in trontime[acounter - 1]:
            line_numbers_of_first_cases.append(acounter)
            woodstock.append(acounter)
            genius = line.split()
            strng = genius[1]
            angel = strng[:-1]
            firstcaselist.append(angel)
            acounter += 1
            continue
        else:
            acounter += 1
            continue

    # Construct the `smartnewlist` by removing quotation marks from case names
    for item in firstcaselist:
        if item != "default":
            item = item[1:-1]
            smartnewlist.append(item)
        if item == "default":
            smartnewlist.append(item)

    # Update global variables
    woodstock = line_numbers_of_first_cases
    candy = smartnewlist

#==========================
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
	mytrace('snowtime') #it calls snowtime() below
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
## refactored on bard nov 30 2023
def snowtime(start_line, end_line):
    """Extracts the body of code for a specific case section."""

    global practicestring1

    practicestring1 = ""  # Initialize an empty string
    sublist = []  # Initialize an empty list

    for index, line in enumerate(switchcasetester.splitlines()):
        if start_line < index < end_line \
                and "case" not in line and "break" not in line \
                and "fallthrough" not in line and "fallthru" not in line:

            if len(line.strip()) == 0:  # Check if the line is empty
                continue  # Skip empty lines

            practicestring1 += line + "\n"  # Concatenate lines into the string
            sublist.append(line.strip())  # Append the stripped line to the list

    case_main_body_list.append(practicestring1)  # Add the case body code to the global list

    del practicestring1  # Delete the temporary string object
    practicestring1 = ""  # Clear the string variable

//======
def cotton_candy():
	mytrace('cotton_candy')
	print("===========cotton candy debugging jan 15th 2021==========")
	print("=======case main body list =====")
	print("starting state of this list case_main_body_list =",case_main_body_list)
	print(case_main_body_list)
	print("this is force feeding it to just be starter for some reason")
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
###################################
def rule_the_earth():
###################################
	print("========rule the earth called========")
	mytrace("rule_the_earth")
	print("line_numbers_of_first_cases")
	print(line_numbers_of_first_cases)
	global woodstock
	print("woodstock list=",woodstock)
	#this is to get the first case of each section
	#print('======= ***** ====rule the earth ==== creates starbucks list === *******  =====')
	print("==here we can see what the machine sees=====---***")
	print(switchcasetester)
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
	plumtree=''
	total_word_count=''
	
	palmtrees.append('starter')
	##for case sets I just go thru till case not in line and fill a new list
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		if mycounter in line_numbers_of_first_cases:
			#print(line)
			felix= line.split()
			print("inside rule_the_earth line with case")
			print("felix=",felix)

			if "default" in line:
				print(line)
				second_word = line.split()[0]
				#this line will be no default
			else:
			################# code to get the 
				#second_word = line.split()[1] #right here it grabs just one word
				#that is the flaw
				##### addition here 
				#### first check if only one word
				print("felix=",felix)
				
				del felix[0] #should delete first word case
				total_word_count = len(felix) #already deleted first word
				if total_word_count > 0:
					print("assertion :: there is at least one word in the case")
					
					
				#secenario if only one word case like Tahoe
				#############################################
				## SCENARIO 1  IF ONLY ONE WORD FOR THE CASE
				# THIS DETERMINES IF THE CASE IS JUST ONE WORD
				#############################################
				if total_word_count == 1:
					print("there is only one word in this case",felix)
					the_words = felix
					plumtree=' '.join(felix)
					#plumtree = felix  #it might be in a list actually 
					print(plumtree)
					plumtree=plumtree[:-1] #this takes off the : on the end of the string
					print("plumtree=", plumtree)
					print("yeah plumtree is a stirng at this stage")
					print("===== experimenntal plum tree to add to palmtrees === ")
					coolness = plumtree.replace("'","")
					plumtree = coolness
					print(plumtree)
					
					#palmtrees=palmtrees[1:-1]
					palmtrees.append(plumtree)
					#starbuckslist.append(plumtree)
				else:
					pass
				##############################
				#this senario if 2 or more words for the case like "alpine meadows
				## SCENARIO 2 IF 2 OR MORE WORDS IN THE CASE
				#THIS DETERMINES IF THE CASE IS AT LEAST 2 OR MORE WORDS
				###############################
				if total_word_count > 1:
					print(total_word_count, " words in this  case")
					print("felix =",felix)
				#========here is the JOIN to convert the line as a list with case into a string ======
					plumtree=' '.join(felix)
					print("== output of plum tree ==")
					print(plumtree)
					if plumtree.endswith(":"):
						plumtree=plumtree[:-1]  #this should delete the colon of end
						alltheway = plumtree.replace("'","") #this elminates double quotes
						plumtree = alltheway
						#starbuckslist.append(plumtree)
						palmtrees.append(plumtree)
					else:
						pass
					
				print("plumtree=", plumtree)
				
				#print("the words for this case are",the_words)
				print("the number of words for this case in the line are ",total_word_count)
				##===========
				print(" ====== entering new section of coding here at Volvo ==== ")
				
				print("=====")
				print("=== coding at walmart saturday night ===")
				
				
				

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
	#filling starbuckslist
	#####################################
	
	print("===========================")
	for item in palmtrees:
		starbuckslist.append(item)
		
	print("we now have... starbuckslist")
	print(starbuckslist)
	print("===========================")
	
	
	




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
	print("=========this_needs_to_work_badly() =============")
	print("=========this_needs_to_work_badly() =============")
	print("=========this_needs_to_work_badly() =============")
	mytrace('this_needs_to_work_badly')
	print('===============this needs to work badly called =======to get first case name ==')
	print("============= THIS NEEDS TO WORK BADLY() called =============== ")
	print('this gets the first case name (designed as one word initially')
	print("but I need to modify it to take more than one word so I will need to count")
	print("how many words are in the *first case* so it's flexible and smart")
	#new_add_to_front(x,listname)
	mycounter = 0
	print("starting out we have in starbuckslist",starbuckslist)
	print('case section line number list =',builder)
	print("what is in builder?") #I think it's the first case line number in each section
	print(builder)
	
	
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		#print(line)
		if mycounter in builder: #so it's looping thru switchase and line number in builder list
			print("!!!!!!!======!!!!!!!!!!line=")
			print("dam line?",line)
			print("underneath line=====================")
			firstline = line.split() #we refer to the line as firstline a variable
			print(firstline)
			### this is where it was grabbing the one word after case
			### which wasn't able to grab more than one word by design
			
			#genius = line.split() #new  [0] was at end of it  ((this does the line split for each line))
			#print("genius[1]=",genius[1])    #gets word of that case name
			print("the design is only getting one word")
			#print("genius=",genius)
			print("genius this is in the first case line above")
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
			print("the number of words in this case is",length_list)
			#['case', "'alpine", "meadows':"]
			print("line 1538")
			print(firstline)
			print("the length of this case name in words =",length_list)
			#while True:
			#remember that we have wiped away(erased) the case word it's gone
			if length_list == 1:
				answer = firstline[0]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                 
			if length_list == 2:
				answer= firstline[0] + " " + firstline[1]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 3:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]
				answer = answer[:-1]
				print(answer)
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
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 6:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4] + " " + firstline[5]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 7:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 8:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 9:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]  + " " + firstline[8]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			if length_list == 10:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7] + " " + firstline[8] + " " + firstline[9]
				answer = answer[:-1]
				print(answer)
				baby = answer
				drive_thru.append(baby)
                
			
			
			
			####==============
			new_add_to_front(baby,starbuckslist)  ## actually adds to tail of starbuckslist
			#test
			print("new add to front (baby,stabuckslist)")
			print("baby=",baby)
			print("starbuckslist=",starbuckslist)
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
###################################
def convert_to_twin_list():  #uses list called line_numbers_of_first_cases
###################################
    mytrace("convert_to_twin_list")
    print("=====line numbers of first cases list====")
    print(line_numbers_of_first_cases)
    global woodstock
    print("woodstock in twin list=",woodstock)
    global candy
    #input_list -= 1 #true cases last number is default
    alpha = 0; beta = 1; counter = 0  #down below it was: length_of_input_list
    while counter < len(line_numbers_of_first_cases) -1:
        eval("list_trex.append(line_numbers_of_first_cases[alpha])")
        eval("list_trex.append(line_numbers_of_first_cases[beta])")
        eval("digitalcandy.append(list_trex)")
        eval("candy.append(list_trex)")
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










#=========================
##########################################
def special_addition_to_digital_candy():
##########################################
	mytrace("special_addition_to_digital_candy")
	global candy
	candy.pop()
	digitalcandy.pop() #delete last item sublist
	#print("digital candy after pop =",digitalcandy)

	#this gets the line number of the word default
	find_default = get_default_location()  #gets line number of default

	#this gets the line number of the closing brace (identical to last line of docstring)
	last_brace   = get_closing_brace()  #gets the line number of closing curly brace
	thelastbreak = find_last_break_in_string()# put it here
	mystring = str(get_closing_brace()) #puts closing brace line number in mystring

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
	
	candy.append(defaultlist)
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
		print("this is before adding break to default")
		print(switchcasetester)
		#global switchcasetester
		orange=''

		orange=switchcasetester.replace("}","			break \
			\n}")
		switchcasetester='' #this nukes it resets it
		switchcasetester = orange
		print("after adding break to default")
		print(switchcasetester)
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

def stage_four():
	print(switchcasetester) 
	print("===== testingwhat it sees in stage four() ======")
	mytrace('stage_four()')
	#print('stage four')
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
	print("======def ======testing this to get word() ==================")
	print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")
	print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")
	print("*** MASSIVE TESTING AT STARBUCKS ON TUESDAY MORNING ***")

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
			print("the number of words in this case is",length_list)
			#['case', "'alpine", "meadows':"]
			print("line 1441")
			print(firstline)
			print("the length of this case name in words =",length_list)
			#while True:
			
			if length_list == 1:
				answer = firstline[0]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
			 
			if length_list == 2:
				answer= firstline[0] + " " + firstline[1]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 3:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 4:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 5:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 6:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2] + " " + firstline[3] + " " + firstline[4] + " " + firstline[5]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 7:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 8:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 9:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7]  + " " + firstline[8]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			if length_list == 10:
				answer= firstline[0] + " " + firstline[1] + " " + firstline[2]+ " " + firstline[3] + " " + firstline[4] + " " + firstline[5] + " " + firstline[6] + " " + firstline[7] + " " + firstline[8] + " " + firstline[9]
				answer = answer[:-1]
				print(answer)
				drive_thru.append(answer)
                
			#print(firstline[0])
			#print("now try this",firstline[length_list])
			smartcounter += 1;
		else:
			smartcounter +=1;
    
	print("================== drive thru list of case names ")
	print("the list of case names no matter how many words is here in list drive_thru")
	print("drive_thru list contents now are ",drive_thru)
	print("")
	print("now we will loop thru the drive_thru list")
	print("==========================")
	print("drive_thru=",drive_thru)
	print("===========================")
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
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0







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
    print("==$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==")
    print("================this is line 1615===CREATE CASE NAME LISTS=====================")
    print("def create_case_name_lists:")
    print("working on fix to solve bug if user uses more than one word for a case")
    print("such as alpine meadows whereas right now its geared for one word cases")
    
    mytrace('create_case_name_lists')
    #print("=================create case name lists called == @@@@")

    smartcounter=0 #reset at zero
    genius = ''
     #need list of first cases that will work for input
    #Thursday coding to save this day from a disaster of nothing working
    ##===================================================================
    ## LOOP LOOKING  CASE SECTION APPEND LINES FROM BODY AFTER CASES UNTIL NEXT FIRST CASE
    ##=======================================================================
    print("here we get the words in each case section=====------")
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter < y:  #so get what's inbeteen
        #this should just look
            if "case"  in line:
                print("did it take off front of line?")
                print(line.split(' ',1)[1])
                print(line,smartcounter)
                print("=================================")
                genius =line.split()
                print("genius =",genius)
                print("======= len(genius) ==============")
                print("WE ARE HERE==>>>>")
                print('number of words in the line case = len(genius) ',len(genius))
                
                print("number of words in this line =",len(genius))
                print("it's current state is only grab the second word which is position [1] by default")
                ap=''
                #testing with more than one word the defualt was the first one
               #================  jan 3, 2021 code fix experimentiong case alpine meadows
                if len(genius) == 2:
                    print('teh default was 1 word case and one word')
                    caseset.append(genius[1])
                    print(caseset)
                    
                if len(genius) == 3:
                    print('teh default was 3 words case and two words')
                    ap =genius[1] + genius[2]
                    caseset.append(ap)
                    print(caseset)
                    
                if len(genius) == 4:
                    print('teh default was 4 word case and 3 words')
                    ap =genius[1] + genius[2] + genius[3]
                    caseset.append(ap)
                    print(caseset)
                    
                if len(genius) > 4:
                    print("more than four words in this line detected")
                    print("just do the default for now will fix later")
                    caseset.append(genius[1])
                    print(caseset)
                
                print("it looks like I'm just grabbing the first word of a case which I initially tested it with")
                print('line 1632')
                print(caseset)
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
mrcase=''
def case_tail_list_maker(x,y):  #two vars x and y are case locations from digitalcandy
    mytrace('case_trail_list_maker')
    print("=######	C A S E    T A I L   M A K E R  searches for breaks and fallthrus  ")
    print("digitalcandy=",digitalcandy)
    print("length of digitcandy=",len(digitalcandy))
   
    smartcounter=0
    #this looks for "case" in the switch case string
    for line in switchcasetester.splitlines(): #switch case in JS
        if "case" in line: #see if this puppy works
            firstline = line.split()
            print("====spaceX starship SN10 to launch this week===")
            #casecaputured=get_case_name(firstline)
            #print("it sees as the case ",casecaputured)
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
    ram=''
    #look for BREAK in range of lines
    ##================================================
    ## LOOP LOOKING FOR BREAK IN CASE SECTION CODE
    ##================================================
    #homer=[] #this is to keep track of whether break or fallthru as backup checker
   ##############################################
   
    ##############################################
    ##############################################
    print("HUGE TEST to make it work Tuesday feb 22nd")
    #this goes through the whole switch case 
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        #print("======= TESTING THIS  ========")
        #print("x =",x,"and y=",y)
        if smartcounter >= x and smartcounter <= y:
       #this is the range I want to print
            ####################################
            if smartcounter == x: #case line
                print("GET CASE NAME")
                mrcase =get_case_name(line);  #calling method here 
                print("just here got the_section",mrcase)
                print(mrcase)
                
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
                print("===== gold ======")
                print("we found a break line number =",x,y,smartcounter)
                
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
                print("no break found in this section") #and no fallthru
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
        print("this was the old design the newone will be different")
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
    print("=================================")
    print("gti  list has",gti)
    print("=================================")
    print("========WILECOYOTE LIST=========")
    print(wilecoyote)


#### thursday coding fix 
#right here add the new surgical strike addition to make it work 
 #   smart = len(royallist)  #new code  a number
   #      smart += 1
  #       #before I add this one         so I am putting a number here which is used
   #      fall = "fallthru" + str(smart)  #to call the correct word in starbuckslist
    #     #print("we have",starbuckslist[smart]," added to fallthru")
    #     #I will need to do this
    #     #  fall = "fallthru('" + starbuckslist[smart] + "'")
    #     royallist.append(fall)
     #    
#####################################



   #this is all so clever
   # looks inside of lists for breaks, fallthrus
    if "true" in case1findbreak:
        print('break found in this case section ')
        royallist.append('break'); #this adds break to royallist
       # homer.append("break")


# here it's appending the fallthru('casename')
    if "true" in case1findfallthru:
        print('** = fallthru found in case section')
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
        print("** = need to add a fallthru in this section with no break and no fallthru")
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
    print("===::::::::::::::=====722 Palomar Drive====")
    print("royallist has ",royallist)
   
    print("homer simpson",homer) #only line numbers with break
    #I can then deduce what case sections they reside in
    #print("starbuckslist=",starbuckslist)
    print("a shot in the dark here")
    print("palmtrees=", palmtrees)
    print("I can try adding the break onto the end here.")
    print("let us see what the size and end of royallist is",royallist)
    print("royallist lenght=",len(royallist))
    royallist.append('break'); #this is for the default case which must be a break
    print("royallist final =",royallist)
    print("lenght of royallist final =",len(royallist))
    snowman.append("break")
    print("gti coming thru",gti)
    print("this is our winner=================")
    print("seal=",seal)
    print("the list of first case number in digitalcandy with a break in it")
    print("wilecoyote=",wilecoyote)

## bug in royallist it should end with break for default not a fallthru


# beach break through 
#great fucking idea,
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
	print("Crashing Waves At Beach function called")
	######## there is a lot going on here
	'''
	loop thru wilecoyote of cases with breaks and
	   get index location of those cases in palmtrees list
	   put the index number into roadrunner list
	   
	 
	loop thru digitalcandy to make list of same size and fill british list with all 'fallthru'
	
	loop thru roadrunner list with index number
	and replace index number in british with "break"
	
	'''
	print("this is what is in wilecoyote",wilecoyote)
	print("I got this working the other day at motel 6 on Tuesday night")
	################################################
	## this gets the location of the case in wilecoyote inside of palmtrees list
	for item in wilecoyote: #goes through list of case sections with breaks
		toad = get_location_of_case("palmtrees",str(item))
		roadrunner.append(toad) #this returns a number the index position
	print("ROADRUNNER list contains numbers of index locations of cases in palmtrees",roadrunner)
#################################################
	# make a new list based on digitalcandy
	thecounter=0
	for item in range(0,len(digitalcandy)): #using this for length of case sections sequence
		#filling list with fallthrus
		print("what I am doing here is adding the Next case number so it's correct")
		  #I had to move the counter before it to get it working correctly
		british.append("fallthru" + str(thecounter + 1)) # current case number + 1 for next case
		thecounter += 1
	#this adds break after the loop finishes	
	british.append("break") #adds one more to list since default is extra case
	
	print("========== british list ======")
	print("british filler list =",british)
	#british[0] = "starter" #this is position 0 filler
	#british[-1] = "break" #last one must be break for default case
	print("========== british list ======")
	print("so here the british list should have breaks and fallthrus(with number to next case")
	
	print("british list =",british)
	##################################################
	#this is walking thru the british list and replacing fallthru with break where there was a break in a case
	#the bug is here 
	#It's initially filled with all faltlhrus, so replace with break
	#Next I need to replace with fallthru with number 

	print("==BIG LOOP TEST TO INSERT BREAK INTO FALLTHRU LIST CALLED BRITISH==")
	print("what this does is replace fallthru with a break based on location of a break")
	print("and this is in the british list")
	print("this is using digitalcandy for the proper length of the new list roadrunner")
	############ this is where BREAK  is inserted into the list with replace method 
	mycounter=0
	for item in range(0,len(digitalcandy)):  #adding a case to it default
		if mycounter in roadrunner: #if it finds first case line number in roadrunner
			print("this is where it is inserting break into the list british")
			do_replace(int(item),"break")## do_replace(1, 'break')  list[index number]
			mycounter += 1
		else:
			mycounter += 1
			
	print("============================")
	print("british is ",british) #break and fallthru list
	#this changes the first position slot to starter
	british[0] = "starter"
	#this ensures that the last one is a break no matter what it's force fed in. 
	british[-1] = "break" #makes sure last one is break which is absolutely must be. 
	print("here is the finished british list before adding teh fallthru with case")
	print("british now =",british)
	
	#do this first  assuming of course default (worry about adding defaeult laster
	#check if "break" in switchcasetester
	#if False then add it to bottom of default
	#if no break in switch case it won't parse - sooo funny 
	
	####==================================================
	print("=== OFFICIAL BRITISH LIST ==== USING SMART BREAKS AND FALLTHRUS NUMBERED == ")
	print(british)
	########################################################
	british[0] = "starter"
	british[-1] = "break" #just to be sure 
	print("####################E#######################")
	print("February 25th, 2021 Beach Coding with seagulls flying just above the waves ")
	print('totally NEW OCEAN BEACH CODE TO MAKE NEW FALLTHRU INTO LIST OCEANWAVES')
	print("which will be put into cranberries replacing what's in cranberries ")
	print("=================-------- waves at abeach -------+++++++++=================")
	print("======================= waves at beach and seagulls flying over ice plants =====")
	print("british list=",british)
	print("palmtrees list =",palmtrees)
	#penguin.append('starter')
	for item in british:
		penguin.append(item)
	
	#penguin.append('break')
	print("penguin= ", penguin)
	print("starting length of penguin=",len(penguin))
	
	#faltlrhus with numbers get case number from end of fallthru
	print("MASSIVE TEST OF replacing fallthruX with fallthru('casename') in british list")
	print("======")
	print("======")
	print("======")
	### new coding here 
	print('british list=',british)
	newcounter=0
	for item in range(0,len(british)):  #should only look inside of items starting with f
		if british[item].startswith("fallthru"):
			print('item =',item)
			print("newcounter =",newcounter)
			getnumber= british[newcounter] #gets the fallthruX
			print("it sees this in british[newcounter]")
			#get the number on end of word fallthru
			print("getnumber=",getnumber)
			getnumber = getnumber[8:] #gets the number from cutting off front fallthru
			getnumber = getnumber.rstrip()
			getnumber = getnumber.lstrip()
			print("getnumber=",getnumber)
			newnumber = int(getnumber)
			print(newnumber)
			casename =palmtrees[newnumber] #has cases in sequence
			print("casename=",casename)
			mrfallthru = "fallthru("  + "'" + casename + "'" +  ")"#
			print("mrfallthru =",mrfallthru)
			#do_replace(int(getnumber),mrfallthru)
			smart_replace(newnumber-1,mrfallthru)## just added minus 1
			print("########### building the penguin list ")
			print(penguin)
			newcounter += 1
		else:
			newcounter += 1
			
			
	print("00000000000000000000000000000000")
	print("british=",british)
	penguin[-1] = "break"
	print("penguin=",penguin)
	print("11111111111111111111111111111111")
	print("11111111111111111111111111111111")
	print("11111111111111111111111111111111")
	print("11111111111111111111111111111111")
	#### I can change the contents of british or makea  new list so as to not mess it up.
	oceanwaves =[]

###########################################################################









tail_list=[]
cranberries=[]
cranberries.append('starter')
british =[]  # list for faltlhru and breaks for each section to be managed
roadrunner=[]



  ##===========================
  ##      def p51_mustange()  ==  adds the number to  fallthru(3) like that
  ##===========================
  #this makes the cranberries list which is the tail list used on codegen page
#diamonds=[[2,7],[7,17],[17,24],[24,34]]
#this makes the cranberries list
def p51_mustang(): #makes critical cranberries list which is the taillist for switch cases
	print("=== p51 MUSTANG finishing up last part of numbering fallthrus and getting next case name")
	print("=== ==== == === == the P51 Mustange is starting to fly and get off the ground entering clouds")
	print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	print(" $===$ this is where I am DEBUGGING the correct construction of fallthru $===$ ")
	print("@@ p51 MUSTANG code called which fills the cranberries third part tail with fallthru and break")
	print("P51 MUSTANG will it fly today======================::::::::::::::::::")
	#print("starbuckslist")
	#global starbuckslist  #just trying this now  trying to figure out why it's empty
	#print(starbuckslist)
	#thelength = len(starbuckslist)
	#print("the length of starbuckslist =",len(starbuckslist))
	#print("first the wilecoyote cases with breaks here")
	#print(wilecoyote)
	
	print("========")
	mytrace('p51_mustang')
	counter = 0
	c = 1		#current case numbr section
	d = c + 1
	print("** inside of p51 mustange [[ digitalcandy ]] =",digitalcandy)
	
	for item in digitalcandy:	#this is going through the diamonds list

		clever = digitalcandy[counter]
		x = clever[0]
		y = clever[1]
		##print("x",x,"y",y);
		case_tail_list_maker(x,y)   #here it is calling case_tail_list_maker
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
	for item in royallist:  #so royallist has starter break fallthru3 default in it 
		if "break" in item:
			cranberries.append("break")
		
		print("this is where fallthru gears work line 2182")
		if "fallthru" in item:
			#### this grabs the number on the end of fallthru that is already there. 
			item=item.strip()
			print("item=",item)
			item =item[-1]
			print("after item[-1] we have item=",item)
			item = int(item)   #is this returning a number?
			## yea this is retrieving the number from the end of the word fallthru
			#print(item)
			print("==========//////// ===============")
			print("LOOK RIGHT IN HERE ==> palmtrees=",palmtrees)
			print("in drive_thru list we have",drive_thru)
			#trying to use drive_thru list which should be accurate
			#it's not intermixed with breaks I don't think but starbuckslist is
			#it was drive_thru[item]
			# it was starbuckslist
			print("this is getting the case name from palmtrees[item]")
			####this isn't working because it doesnt capture more than one word soit's strong and cuts off first word.
			doggy =palmtrees[item] #just added -1   this is like fallthru('cherry')  #was starbucks
			print("doggy",doggy)
			doggy[1:]
			doggy[:-1]
			print("slice off first and last character",doggy)
			print("doggy is showing ===",doggy)
			#cool1 = doggy.lstrip("'")
			#cool2 = cool1.rstrip("'")
			#doggy = cool2

			print("palmtrees[item]=",palmtrees[item])  #was starbucks
			
			print("ohbaby which has fallthru from doggy starbuckslist[item]")
			ohbaby = "fallthru("  + "'" + doggy + "'" +  ")"#this is the number
			#just took out the "'" on both sides of doggy 
			print("ohbaby =",ohbaby)
			#########################################
			print("the constructed fallthru is in ohbaby=",ohbaby)
			#print("ohbaby=",ohbaby)
			cranberries.append(ohbaby) # just added this Thrusday, sept 10th Target
			
			print("this IS WHAT is in CRANBERRIES",cranberries)
			print("=====")
			print("the LENGTH of cranberries list=",len(cranberries))
			
	# make sure that default case needs to end with break and not fallthru
	# february 4th, 2021
	print("================= C R A N B E R R I E S   L I S T ====case-tail-maker=========")
	print("ROYALLIST =",royallist)
	print("palmtrees =",palmtrees)  #was starbuckslist
	print('CRANBERRIES list =',cranberries)
	print("drive_thru list =",drive_thru)
	#this fills up trail_list from cranberries and creates a new list
	print("wilecoyote list of case names with a break verified")
	print("00000000000000000000000")
	print("00000000000000000000000")
	print("00000000000000000000000")
	print("00000000000000000000000")
	print("00000000000000000000000")
	print(wilecoyote)
	print(len(wilecoyote))
	
		
	print(wilecoyote[0])
	print(wilecoyote)
	print("firstcaselist now in palmtrees")
	print(palmtrees)
	
	oceanwaves=[] #this sets it at empty
	print(" ====== JUMANJI ====")
	print(" ..................J U M A N J I ......inside of P51 Mustang() function..........")
	#add method here
	crashing_waves_at_beach()
	print("tyring to fill a fucking list oceanwaves with british list")
	print("here I am filing the list oceanwaves with the british list")
	for item in british:
		oceanwaves.append(item)
	
	print("OCEANWAVES LIST now ")
	print(oceanwaves)
#I will needto add this to royallist
	
			
			
	
	print("THIS IS THE TAIL LIST CALLED CRANBERRIES")
	print("cranberries=",cranberries)
	print("penguin=",penguin)
	

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



def stage_six():
    #print('stage six')
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

caselist1 =[]
caselist2 =[]
caselist3 =[]
caselist4 =[]
caselist5 =[]
caselist6 =[]
caselist7 =[]
caselist8 =[]
caselist9 =[]
caselist10 =[]
caselist11 =[]
#forcing it to see what happens november 21st
#caselist7=['default']


#we will know before hand how many caselists will be filled 4

#this makes the first case list called starbucks which is used throughout the program
##==========================
##   flying fish             this loops through the dimaonds list of first cases
##==========================
def flyingfish():
	print('digitalcandy=',digitalcandy)
	ax = len(digitalcandy)
	print("length of digitalcandy =",ax)
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
	print('digitalcandy=',digitalcandy)
	global candy
	print('candy=',candy)
	for item in digitalcandy:
		x = item[0]
		y = item[1]
		print("** look at x,y,z here **")
		print("x",x,"y",y,"z",z)
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
	print("smartcasemanager=",smartcasemanager)
	words=''
	print("===========FLYING CLOUD =============")
	print("===========FLYING CLOUD =============")
	print("===========FLYING CLOUD =============")
	print("===========FLYING CLOUD =============")
	print("===========FLYING CLOUD =============")
	print("===========FLYING CLOUD =============")
	print("flyingcloud called; this builds a list of the case names for each section")
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
			print("length of firstline words =",len(firstline))
			words = len(firstline)  #this is the length of the first line
			
			print("=========== line 2000 ===firstline====")
			print("firstline=",firstline)
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
				
										
				
				
			print(" wilderness has in it", wilderness)
			print("=====firstline[1] ====== line 2009 =======")
			#print("wilderness=", wilderness)
			wild= wilderness[1:-1]
			#print("wild=",wild)
			wild = "'" + wild  #adding a ' to left side of word
			darn = wild[1:-1]
			wild = darn
			print("==TARGET TEST==")
			print("===== what is in wild?",wild)
			#wild = wild[1:] #cut off the word case jeeze
			############# feb 6, 2021
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
def nightowl():
	print("===== nightowl() called ======")
	mytrace('nightowl')


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
	wilson=int(''.join(filter(str.isdigit, mystring)))   #this extracts the number from a string
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
	print("=====/////======= smarty() called ====line 3142=====//////=====")
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
	print("==== attempting to print out cases section code from case_main_body_list")
	acounter=0
	for item in case_main_body_list:
		print("==========")
		acounter += 1
		print("case=",acounter)
		print(item)
	

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
#First ‘starter’
#Loop
#Listname.append(‘fallthru’)

#After loop done
#Add listname.append(‘break’)
#Called once fills list
print("========== testing to replace words in lists easily ==========")
print("========== testing to replace words in lists easily ==========")
print("========== testing to replace words in lists easily ==========")

print("testing making changes to a list which I will use for constructing")
print(" breaks and fallthrus  for utlimately constructing the list to")
print(" be used to put into cranberries list")

fruits = ['apple', 'banana', 'fallthru']

fruits.insert(1, "orange")

print(fruits)

fruits[0] = 'starbucks'
print("")
print(" changing replacing value")
print(fruits)
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

print("")

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
	print("====partynation======")
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
	print(" this prints out the contents of the important lists")

	print("==============================================")
	print("digitalcandy list ========")
	for item in digitalcandy:
		print(item)
		
	global candy
	for item in candy:
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
	print("inside of switch_return_value[1]")
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
#########################################################
#########################################################
#########################################################
#======================================
#  ====== project mr coffee ========
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():
	mytrace('switch_code_gen')
	#####
	##### march 7, 2021
	#new change putting penguin into cranberries
	print("=== march 7th, 2021 testing===================///================================")
	print("penguin=",penguin)
	#print("cranberries=",cranberries)
	print("======")
	#Here I am putting the contents of penguin into cranberries
	print("this is where I empty cranberries list and fill it with penguin")
	cranberries = []  #emptying cranberries here 
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
	counter =0  #each section will have the same number of items
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
	print("")
	print(" =====done executing output from switch ======")
	print("")
	#switchcasetester='' #or del switchcasetester deletes it after done with it
	#january 16, 2021
	
	#empty case_main_body_list, put "starter" into it
	#case_main_body_list=[]
	#case_main_body_list.append("starter")
	#if default == True
	#print('what they entered')










#this executes the generated python switch code
def stage_twelve():
	mytrace('stage_twelve()')
	#changing to run second switch case january 15, 2021
	switchcasetester =''
	sw =''
	#global switchcasetester #new
	#switchcasetester =''  #new
	#print(switchcasetester)
	#case_main_body_list=[] #nukes it
	resetting_up_case_body() #clears out case_main_body_list then appends('starter') to it
	print("caselist",caselist)
	print("smartcasemanager",smartcasemanager)
	pass
	
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
	print(switchcasetester)
    #print("the number of tabs in this baby")
	tabnumbers =switchcasetester.count("\t")






# put this into a function
#switch_code_gen() ##=== this calls and generates the python switch case
				  ##=== this has the code generation of the python code
#print(switch_python_gen)
#exec(switch_python_gen)




def pilgrim(): #testing import in another file
		print('pilgrim')



#case_main_body_list=[]
#this is new but I haven't tried it yet december 5th
def starter_sequence():
	#case_main_body_list=[] #this shoudl work january 16th, saturady night 2021
	#case_main_body_list.append('starter') 
	#print("oh my god starter_sequence called will it work???")
	badass()
	stage_one()
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
	switch_code_gen() #  <<<==============it's called right here the code generator
	stage_twelve()  # <== this resets the lists for next use of switch
	show_tron_trace_path()
	clearit()
	global woodstock
	print("what we have in woodstock=",woodstock)
	print("now we clear out woodstock list")
	woodstock =[]
	print("woodstock=",woodstock)
	global candy
	print('what we have in candy=',candy)
	print("now we delete its contents")
	candy=[]
	print("candy=",candy)
	
	showit()
	empty_test() #test of global list
	
	#flush_lists() #this is new january 16th, saturday debugging trying second switch case
	
daisy=''
def parser(a):
	#felix()  #testing with switchcasetester string
	#mtv()
	mountain2(a)
	starter_sequence()


def endswitch(y):
	print("endswitch called with ",y)
	parser(y) #this calls parser() abobve and passes in 
	
	
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
  
