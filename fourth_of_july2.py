#import official_switch_case_silver
#from official_switch_case_silver  import *  

zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'


print("from the web trying this out")


endswitch_location=[]
switch_location=[]

def empty_switch_and_endswitch_list_locations():
    print("called empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations 
##########################################
def get_switch_and_endswitch_locations(z): #from string z input parameter
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	print("get_switch_and_endswitch_locations(z) called ....")
	print("====== THIS IS THE ONE THAT I NEED ======")	#this catalogues the switch and endswitch locations for an entire input string
	print(" GET SWITCH AND ENDSWITCH LOCATIONS ADDED TO LIST")
	print(" ========  MICKEY MOUSE HOUSE  =========")
	counter=0 #it was 0 starting counting from 1
	for line in z.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		#print(line) #this should be revealing
		#if line.isspace():
		
		if "switch" in line and "end" not in line:
			print("switch found",counter)
			
			switch_location.append(counter)
			counter += 1
			
			
		elif "endswitch" in line:
			print("endswitch found",counter)
			
			endswitch_location.append(counter)
			counter += 1
			
			
		else:
			counter += 1
			
			
			
	del switch_location[0]	#empties it what am I doing here??? july 7th deleting first switch
	print(z)                #now I remember that is the first switch which doesn't matter
	print("I deleted the first switch since I'm not bothering with it")
	print("switchlocations=",switch_location)
	print("the length of switch list =",len(switch_location))
	answer = len(switch_location)
	answer = answer -1
	print("this is how many nested switches are here")
	print("now we should have this many nested switches to contend with",answer)
	print("and the answer is above this line .....")
	#this prevents a bug if I don't have endswitch in the string
	if len(endswitch_location) > 0: #this only proceeds if there is at least one endswitch
		print("endswitch locations =",endswitch_location)
		print("out of curiosity print the number of endswitches", len(endswitch_location))
	else:
		pass
		
	print("this might be simpler to test and use actually======/////???????//////===")
	print("======================================")
	print(" ===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === ")
	print("I need to delete teh first swithc location")
	
	#del switch_location[0] #ALREADY DELETING FIRST SWITCH ABOVE BECAUSE IT'S NOT NEEDED NOT NESTED
	print('switch_location=',switch_location)
	print('endswitch_location=',endswitch_location)
	# I need to feed these into the pear dictionary now down below
	#I will feed the pears list with a loop thru the switch_location list
	########## WORKING ON THIS TODAY MONDAY TO MAKE SOME SERIOUS PROGRESS 
	##########  MONDAY JULY 19TH APPROACHING 12 NOON 
	
	#make pairs here
	#might have to delete teh first switch which throws everything off
	
	
	
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

coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here       
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
			switch(exp){     #here     
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
##########################################
##  put_switch_locations_into_switch_list()  #this is making the nested_switch_ number  
##########################################
def put_switch_locations_into_switch_list():
    get_switch_and_endswitch_locations(coolstring)
    for item in switch_location:
        switch_list.append(int(item))  #was -1 on here #off by one in the string for some reason
    print(" ");print("switch_list=")
    print(switch_list)

#######################################
##  swap_switch_to_nested_method()  #this is making the nested_switch_ number  
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	print(" THIS IS BEING CALLED TO DO THE MAGICswap switch to nested method called....")
	str_list = stringname.split('\n')
	print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)

######################################	

#this is the control center main that runs this operation
#this numbers the nested switch methods top down
genius[0]=coolstring  #assignment here 
def loop_thru_switch_locations():  #looping thru  switch_list[10,18]
    put_switch_locations_into_switch_list()
    print(genius[0])
    print("switch_list=",switch_list)
    le_number=1
    for item in switch_list:
        print("item in switch_list",item)
        #string,switch,line number
        swap_switch_to_nested_method(genius[0],item,le_number)
        coolstring =genius[0]
        le_number += 1
#######################################



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
loop_thru_switch_locations() #where to find the inner switches to replace with a nest method

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
# when the newest “MacOS Mojave 10.14. 6 Supplemental Update”

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


find_nested_switch_game ='''
	switch(exp) {  
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
print("what we are starting with the switch with a nested switch")
print(find_nested_switch_game)
print("=====================")
#oh wait this needs to be the input C style switch that I search in
#maybe I need to go through the case list palmtrees
# so get line number of switches
#get linenumber of each case to determine which case section the inner switch is in
pacman=[]
pacman.append(0)
linecounter =0
casecounter = 0
coollist=[]
print("this gets the line number of the line that the case starts")
print("that has the nested switch inside THIS Case")

endnestedswitchline=[]
endnestedswitchline.append(0)

print('get line number of each case section')
#just get first case line numbers print it
for line in find_nested_switch_game.splitlines():
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

###$############===================-----0-0--=-=-=-=-=-=0-0-0-9=0--
### GET END OF SWITCH LINE  number
#######################################
## now looking for end of nested switch case
#june 28th, 2021
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
########################################################################
start  = 10
finish = 20
## COPY A NESTED SWITCH
r=find_nested_switch_game
#linecounter=0
makeitwork=[]
makeitwork.append(0)
## function copy a nested switch()   ==== I just put this into a function


def copy_a_nested_switch(r):
    print("=====copy_a_nested_switch()======")
    innerswitch=''
    #global linecounter #this is new july 15th, 2021
    linecounter=0
    for line in r.splitlines():
        if linecounter >= int(start) and linecounter <= int(finish):
            innerswitch += line + "\n"
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result COPY OF NESTED SWITCH  ")        
    print(innerswitch)
    roadrunner = innerswitch
    makeitwork[0] = roadrunner
    print("end of testing getting nested switch string")        
        #linecounter += 1 if it's en
##############==============================#########################
##############==============================#########################
    print("copy top hat") #but include swithc#take out inner nested switch after switch word
    print("copy coat tails")
#then connect together


copy_a_nested_switch(find_nested_switch_game) #this gets put into r as a parameter


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
def copy_top_hat_of_main_switch():
    print("======copy top hat of main switch()====")
    global abovenestedswitch
    linecounter=0
    for line in find_nested_switch_game.splitlines():
        if linecounter >= int(start) and linecounter <= int(finish):
            abovenestedswitch += line + "\n"
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result copy above nested switch case ")        
    print(abovenestedswitch)

terriblysmart = abovenestedswitch

print("end of copying top half above nested switch ")  
print("it should end with switch which we will edit")


####################
#replace switch

#linecounter= 0
newlist=[]
newlist.append(0)
#newlist[0]
# I just put this into a function to have control over it 
#COPY COATTAILS BOTTOM OF BIG SWITCH AFTER NESTED SWITCH END
def copy_coattails_bottom_of_big_switch_after_nested_switch_end():
    linecounter=0
    start = 21 #INPUT PARAMS TO GRB
    finish = 32
    outerswitch=''
    for line in find_nested_switch_game.splitlines():
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
copy_coattails_bottom_of_big_switch_after_nested_switch_end()

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
print("Now I replace endswitch with }")
inputstringswitches[1] = galaxy.replace("endswitch","}")
print("now looking into inputstringswitches[1] endswitch should be gone")
print(inputstringswitches[1])
print("==== end of first major step ==in process of transformation ==")

#################



print("can we get serious here I mean really")       
bronze=0     
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

def get_number_of_nested_switches():
    print("get_number_of_nested_switches()")
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

#### get line number of cases()


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





################################################
#  get_below_after_method_insertion
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




samplecode ='''
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
			print ("switch case behavior works in Python now!")
			print("")
			fallthru('test3')         

		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			fallthru('test4')

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
'''



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
			print('== autumn nest===')
			switch(exp){   #this is new 28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #38
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


def jumanji(y):
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
	for line in swo.splitlines(): #determine if switch is in line
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
	for line in swo.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line: 
			endswitchcounter += 1  #END SWITCH COUNTER
			#print("endswitchcounter=",endswitchcounter)
			print("yea this starts with endswitch")
			continue
		else:
			continue
	print("total endswitches =",endswitchcounter)
	print("end of this checker ===========")
	print("swe we have total switches",switchcounter, "and total endswitches",endswitchcounter)
	print("now normal way of checking=======")		
	print("now normal way of checking=======")
	print("now normal way of checking=======")
	
	#this sets the flag in nested_switch[0] if at least one nested switch
	#===============================================
	#if one or more switch and one or more endswitches
	if switchcounter > 1 and endswitchcounter >=1:
		nested_switch[0] = True
	else:
		nested_switch[0] = False
	
	print("the result of this test for if this has nested switch(es)")    
	print("nested_switch[0] = ",nested_switch[0])
	print("=================")
	print("=================")


	print("this  below this is dog breath that doesn't work")
	
	#this following code below this line doesn't work as expected		
	#answer = y.count("switch")
	#backup = y.count("endswitch")
	#print("=== testing number of switches and endswitch=====")
	#print("the number of switches in the string is ",answer)
	#print("the number of endswitches in the string is ",backup)
	#if answer == 1:
	#	print("there is only one switch in this string")
	#end if
	
	#if answer > 1 and backup >= 1:
	#	print("answer > 1 and backup >= 1 meaning more than one switch and at least one endswitch")
	#	print("looks like at least one nested switch")
	#	print("switch count =",answer)
	#	print("endswitch count =", backup)
	#	print("we would call bypass205 at this point")
	#end if
	print("====== end of this initial switch counter filter that will eventually")
	print("=== trigger bypass205 to do multiple switches ====")
	
jumanji(swo)


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
			endswitch  #notice this for it is key 
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #38
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

print("the one below this line should produce 2 switches and one with 10,20")
#this find the location one one pair of a nested switch and end switch

#this gets the start and end from samplestring
#empty_switch_and_endswitch_list_locations()
get_switch_and_endswitch_locations(samplestring) #======= just commented out july 18th 
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
#loop
pairlist=[]
#this would just add the switch location
alpha=''
beta =''
counter =0
#loop ==============================
for item in switch_location: #loops thru list switch_location
    alpha = switch_location[counter]
    beta  = endswitch_location[counter] #they should be the same length 
    pairlist.append([alpha,beta])
    counter += 1
print(pairlist)
print("oh wow look at this pairlist I made=== starbucks mocha===...")
print("the length of pairlist =", len(pairlist))
print('after first attempt')
sosmart =pairlist[0] #first position
print("wow will this work >> that would be so cool")
print(sosmart[0])
print(sosmart[1])
theforce=[]

print("====== JEDI TEST ========")
jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#this is building a pair [4, 8]   #an example 

#print("celebration time it almost works completely fireworks")
print('jedi=',jedi)
theforce.append(jedi)
print("=======NEXt JEDI TEST ======")
sosmart =pairlist[1] #second position meaning second nested switch 
print("wow will this work >> that would be so cool")
print(sosmart[0])
print(sosmart[1])
#x = 10
#y = 20
jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#print("celebration time it almost works completely fireworks")
print('jedi=',jedi)
theforce.append(jedi)
print("the =========== force here ========force shows",theforce)
print("theforce[0]=",theforce[0])
print("theforce[1]=",theforce[1])
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
print("what type is it switch_location[0]",type(switch_location[0]))
#test =switch_location[0] 
#test=test-1
#switch_location[0] = test
print("switch_location now",switch_location)

#test =endswitch_location[0] 
#test=test-1
#endswitch_location[0] = test
print("endswitch_location now",endswitch_location)

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

nest_string='''
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

##################################################
##  get_one_nested_switch_start_and_finish()
##################################################
'''
 this transfers the line location of switch and endswitch
 to list of switch range 1 and 2 from 
 switch_location and endswitch_location


'''
#28,38 for second string
# I am skipping using this now NOT using this method 
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


##########################################
## take_out_x_tabs_from_front_of_line(n):
##########################################
the_nest_string= fridge[0] 
#this is what has the string_with_nested_switches in it
# THIS TAKES TABS OUT OF THE ENTIRE NESTED SWITCH 
def take_out_x_tabs_from_front_of_line(n,the_nest_string):
	print("take out ",n," tabs from front of line - of string")
	print("take_out_x_tabs_from_front_of_line(n)") #make this is into a method 
	wildness=''
	for line in the_nest_string.splitlines(): #nest_string
		if n == 3:
			wildness += line.replace("\t\t\t\t","\t") #strips one right
		if n == 2: #this leaves 1 tab in front of each line
			wildness += line.replace("\t\t\t","\t") #strips one right
		if n == 1:
			wildness += line.replace("\t\t","\t") #strips one right
		wildness += "\n"
	print("after minor surgery see if this works")
	print(wildness)
	fridge[0] = wildness
	return wildness # this worked




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

'''
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
  



'''


### successful test for between macro ################### july 19th, 2021 ########## 

print("testing between macro and how it will work")
mylist=[]

mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

testlist =[]
testlist=[1,2,3,4,5,6,7,8,9,10]
def between_test(): #between macro 
    print("BETWEEN TEST HERE ----")
    print("bla bla bla")
    print("between test")
    #x = 7
    print("the final outcome..")
    # if x >= switchline and x <= end switchline  #meaning  from start number thru endnumber
    #if x is between switchnumber and endswitch number
    #the list would contain the start number thru the stop mumber 
    # if x is between startnumber and endnumber:
    counter=0
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


def between(x,y,z):
    print("between called for if x in list between y and z")
    if x in alist: #1 thru 6
        print("True yes ",x, "between ", y, " and ",z)
    else:
        print("False,nope",x)

between(4,1,6)
between(10,1,6)

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

########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists
####################################################################||
### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  
def do_this_baby():
    print("===do this baby() adding data to peartree dictionary called ......====")
    print("practicing ADDING data to see if it works (this will be done dynamically later")
    peartree['1'] = [10,20]
    peartree['2'] = [28,38]



def get_size_of_dictionary(zoo):  #this is so I know what next record should be
    print("get size of dictionary zoo")
#but I just thought I can have a running total in a list too

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

    

#given name peartree of dictionary
def get_value_of_key(x):
    car=eval("peartree.get('" + str(x) +"')")
    print(car)
    return car



    
get_size_of_dictionary(peartree)
    
def dynamically_add_one_record_to_dictionary():
    #first pass go thru dictionary to determine it's current length put that into a list
    super=''
    super=get_size_of_dictionary(peartree)
    #so to add 1 to super for next record
    testtheory='[42,60]' #this is hardcoded here but testing at this stage so it's ok
    super += 1
    #combine = firsthalf + secondhalf 
    #print(combine)
    #eval(combine)
    #print(combine) 
    
    
    
    peartree['3'] = [42,60]
    print(peartree)
    get_size_of_dictionary(peartree)
    print("now yellow big bird test =========")
    ### look here this is correct below that owrks 
    fish =  "peartree['4'] = [66,80]"
    #what I built up above needs to look like this string 
    
    exec(fish)
    get_size_of_dictionary(peartree)
    
    
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
    sweet =get_value_of_key(1)
    print("sweet key 1 =",sweet)
    
    get_value_of_key(2)
    get_value_of_key(3)
    get_value_of_key(4)   
    get_value_of_key(5)
   



#making peartree['1'] is not tough

#what about this
#dynamically build it [10,20]
x = 10
y = 20
jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail

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
peartree = {}  
buton=[]
buton.append(0)
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

def add_data_to_pears(x,apple):
 print("add_data_to_pears()",x,apple)
 peartree[x]=apple  #this is where the list is added
 print(peartree)


#adding data to dictionary pears here 
 #july 21st 
apple = [10,20] #<<====== right here I need to produce this from the switch output
x = '1'    
add_data_to_pears(x,apple)  #feeding a new switch pair into peartree

##======
apple = [28,38]
x = '2'
add_data_to_pears(x,apple)
##======

# july 21st, 2021
#this looks into peartree for a key to return a value
# the values it put into buton[0]and buton[1]
 
# this is accessing the peartree
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
b=''  #### this is to ACCESSing DATA TO A DICTIONARY #####
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
    for item in peartree:
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

#def loop thru pears dictionary and call  nested switch


#this calls the method above:        
accessing_data_in_peartree_dictionary()

### this would be after filling this with switch_location and endswitch_location method

print("practicing with this hardcoded input data for switch and endswitch to prove it works")
print("down at pears tree here hard coded ")
# this represents a dictionary called pears already loadded with data
#=================================================
pears =	{  #for pear tree in backyard (2 of them)
  "1": [10,20], # I can make these now 
  "2": [28,38],
  "3": [1,44]
}

#see if this works
#=================================================

#####
# I need to make a method to add main switch to string list
def add_main_switch_params_to_dictionary():
    print("how it will work")
    #methods count end switches
    #Take answer add 1
    #loop thru input switch string get total number of lines
    #"3" : [1,44],  #is the result
    #call method to add it to dictionary


#pears['3'] = [4,7] #example
# 

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
    




 #add item to dictionary
#pears['3'] = [4,7] #example
print(pears)
 #access dictionary
#x = pears("1")
 
 #remove item from dictionary
#thisdict.pop("model")
 
 
#now when I loop thru switch and endswithc lines
#have it fill the dictionary with the data






#always do one nest. Just change the switch start and stop sooo simple


## MAIN TRIGGER FOR TESTING THIS CODE OF EXTRACTING NESTED SWITCH STRINGS 
###################################################
## #this means I need to feed in the one switch location and one endswitch location
## that need to have been already figured out
nest_string=[]


##  copy_one_nested_switch_string(m82)   <<=======     this is the main trigger for the test july 18th 
##  I will need to add another paramter to determine which nestd switch is grabbed 
###################################################
def copy_one_nested_switch_string(m82,zebra,cow): #so I would add a param to determine which nest to grab july 18th 
	print("let's look at the input")
	print(m82)
	print(zebra) #switch    location
	print(cow)   #endswitch location
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
	print("========COPY ONE NESTED SWITCH STRING=======")
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
	
	print("switch_location[0]",switch_location[0]) #10
	print("endswitch_location[0]",endswitch_location[0]) #20
	print("what it sees in switchlocation0 and endloaction0")
	print("===========================================")
	# LOOP thru string
	#print("list_of_switch_range[1]",list_of_switch_range[1]) #10
	#print("list_of_switch_range[2]",list_of_switch_range[2]) #20
	for line in m82.splitlines(): #determine if "endswitch" is in line
		#this by default starts copying the string once line greater than 2
		#this says if counter between 10 and 20 including start number and finish number		
		#############################################
		if "switch" in line and "endswitch" not in line: #this shows just switch
			print("switch in this line",counter)
		if "endswitch" in line:
			print("endswitch in this line",counter)
		##############################################	
		#right here if counter is between min line number and max line number
		alpha = int(switch_location[0])
		beta  = int(endswitch_location[0])   
		if counter >= alpha and counter <= beta: #if counter between(within) alpha and beta:
			buildstring += line + "\n" #I need to start at the 10th line
			counter += 1	
			continue
		else:
			counter += 1 #wasn't adding to counter
			continue #really
	print("the new creation concatted should be buildstring=")
	fridge[0]=buildstring
	print("what is in the fridge[0] the nested switch copied")
	print(fridge[0])
	#############################################
	newstring=''
	cool_string = fridge[0]
	print("#method take_out_x_tabs_from_front_of_line()")
	newstring=take_out_x_tabs_from_front_of_line(2,cool_string) #this is running #takes off 2 leading tabs
	fridge[0] = newstring
	print("final outcome Tron")
	print(fridge[0])
	################################################
	# July 21st, 2021 4:16 pm Gilroy Starbucks
	#this copies the string just copied and put it into nest_string
	nest_string.append(fridge[0])
	#need to delete teh first three tabs
	fridge[0] ='' #this empties fridge[0]
	#################################################
	
	
	
	
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
################# creation of loopstring list to hold string that will hold the nested switch string

loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=samplestring #see if this works 
print('big test here ')
print("loopstring[0]=",loopstring)
    
    

doves=[]

#########################################
## loop thru pears dictionary
## and calls copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])
#########################################
def make_the_impossible_into_reality():
    print("make the impossible into reality VIKING SHIP")
    print("show what is in pears")
    print(pears)
    counter = 1
    #it might just have to go thru once to fill pears
    # going thru a dictionary I need to designate which pair 
   
    ##########################################
    ## this loops thru the dictionary pears
    ##########################################
    print("about to lop thru pear values")
    #looping through dictionary pears 
    ## LOOP ########
    for x in pears.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        print("and so it begins...... in the beginning we had nothing")
        print(x)
        cool = x
        print("cool=",cool)
        print(cool[0],cool[1])
        #say_something(cool) #this way the switch and endswitch locations are passed into the function
        ##########################################################
        ## this calls COPY ONE NESTED SWITCH STRING()
        ##########################################################
        print("about to start copy_one_nested_switch_string()")
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        
        #endswitch_location[0]=''
        print("========================")
        #still need to add it to a list

###=== this goes thru pears dictionary  and copies the nested switch strings
make_the_impossible_into_reality() 
print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)
#this is the resulting output of copying the string embedded in the main switch

###===================================================
###===================================================
## july 21st 2021 349pm gilroy starbucks
###=== this shows the nest_string list of nested switches
def show_list_of_nested_strings_separated():
    print("==show list of nested strings separated==")
    print(" StayPuff Marshmellow Man")
    for item in nest_string:
        print(item)
        print("==========")

print("============================")
print("middle ground filler here to separate teh change just made.")
print("============================")

show_list_of_nested_strings_separated()
#now replace teh third string(the main string)
# this is to simulate cutting out the inner switches
## july 22nd, 2021 

####===========================================================###
####===========================================================###
####===========================================================###
print("july 22nd 2021 additions...")
###============== this is working correctly now ==========
def more_testing():
    print("=== more_testing() == charisma ===method testing ")
    nest_string[2] = samplestring_main #putting in a different string premade
    #this is what is different right here in the line above
    
    #testing what the stages need to look like
    #to test what it should look like but doesn't yet
    print(" now we will try it again and see how it looks ")
    print(" after changing main string")
    #loop thru nest_string
    for item in nest_string:
        print(item)
        print("==========")

more_testing()

####===========================================================###
####===========================================================###
####===========================================================###


### this works this takes the copied nested switch
### and sets the proper indentation for it
#so it takes out 2 really but we have to say 3
## july 17th 10:12am 2021 starbucks





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




#string,start,finish
#first it will just detect one nested switch , soon it will detect many



#this loops thru a string and makes a copy of the string
# but skips over a range example lines 10 thru 20

###  SKIPPING SOME LINES (INPUT STRING, START LINE NUMBER, FINISH LINE NUMBER)
#####  S K I P P I N G      S O M E      L I N E S  ############
##========================================================================
def skipping_some_lines(x,start,finish):#start line of switch and finish is endswitch
	smart = x; counter=0; concatthis =''; finish = finish + 1 
	for line in smart.splitlines():
		if counter > start and counter < finish: #if between start and finish skip these lines
			#skip
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			continue	

	ibm[0] = concatthis	  #this has the switch string with the nested switch cut out

	
	
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

skip_range=[]
#july 5th, 2021
#so I still need to get the start and finish lines  switch and endswitch for input 
del ibm[:] #empties it
#print(ibm[0])
ibm.append(samplestring) #so in  ibm[0]
print(ibm[0])
#===================print testing on july 24th saturday  2021 at 9:36am =================
print("at this point we have this in ibm[0] after taking out the first nested switch")
#del skip_range[:]
print("LOOP TEST THRU RANGE LIST Goofy dog")
range_list=[]
#this would be done separately and is filling the range_list with the switch to endswitch params
#this will be a separate method for range input for the switch endswitches
#here the sublists of the param of each nested switch are added to range_list
range_list.append([10,20]) #these are added in order and then reversed
range_list.append([28,38]) # so that the nested switches are erased bottom up
print('range_list=',range_list)
range_list.reverse()#reverse it 

'''
this goes thru the main switch string and makes a copy
of the main string in stages copying the whole thing
except for the range for each nested switch.

'''
# REDUCE MAIN NESTED SWITCHES TO JUST SWITCH WORD
def reduce_main_nested_switches_to_just_switch_word():
    print('range_list=',range_list)
    #loop thru range_list
    print("we loop thru the range_list here")
    for item in range_list: #so these have already been reversed.
        print(item, item[0],item[1])
        skip_range.append(0);   skip_range.append(0) 
        skip_range[0]= item[0]; skip_range[1]= item[1]
        #this builds a new string by skipping the nested switch sections
        skipping_some_lines(ibm[0],skip_range[0],skip_range[1]) 
        del skip_range[:] #this clear it out afterwords to wipe the slate clean
    print(ibm[0])
    print("=====================")


#here we go  
print("the goofy dog test")  
print('we start with this string')
print(ibm[0])
reduce_main_nested_switches_to_just_switch_word()

     
#print(ibm[0])
print(" starting anew here doing it the old way")
ibm.append(samplestring) #in ibm[0]
#print(ibm[0])


skip_range.append(28)
skip_range.append(38)
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 28,38 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print("now we have this after taking out both the first and second nested switch")
#print(ibm[0])
del skip_range[:]
skip_range.append(10)
skip_range.append(20)

#I guess I can put the ranges into a list and then reverse it and 
#loop thru it.

print("starting out we have this before stripping out the nested switches")

skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 10,20 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print(ibm[0])
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








danumber=''
##===============================
# swap_switch_for_nest_method_new(danumber)
#======================================
def swap_switch_for_nest_method_new(danumber): # I will add more values later perhaps 3 or 4 for coordinates
	print(" =======OPTIMUS Prime======")
	print(" =======OPTIMUS Prime======")
	print("swap switch for nest method new called....")
	print("input number isfor swap_swith for nest method now")
	print("these are the input params")
	print("q= ", "danumber= ",danumber)
	global abovenestedswitch
	abovenestedswitch=ibm[0] #loading from ibm[0] good
	print("called swap_switch_for_nest_method(n)")
	#use_number[0] #this number is assigned before I call this function
	print(":==== this is the number it will use to number the nested switch")
	print("it is using this number in use_number[0]",use_number[0])
	#print("q as a passing param is ",
	#use_number[0]=q #force feed it 0 
	#print("use_number[0] sees this just before insertion",use_number[0])
	##3=================
	acounter=0
	for line in abovenestedswitch.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		
		
		if acounter == danumber and "switch" in line: #line with switch in it  
			print(line)
			print("............. ")
			#HARD CODED NOW WITH NUST nested_switch_x(n) the series number is added later for simplicity
			abovenestedswitch = abovenestedswitch.replace("switch(exp){","nested_switch_x"  + "(n)")
			print("YES switch is in this dam line")
			print("AFTER CHANGING THE NUMBER IN NESTED SWITCH")
			print(abovenestedswitch)
			ibm[0] = abovenestedswitch
			print("===================")
			print(ibm[0])
			break #because we are only doing it once to replace only ONE switch
			acounter += 1
		else:
			acounter += 1
			continue


print("now this should be the switch in the middle")
print(" line on line 10 replaced with method call instead")
# this takes in what is in ibm[0] and the outputs it to ibm[0] also, quite clever.     
#swap_switch_for_nest_method_new(1)   
print("now we use ibm[0] and insert a method where the internal switch was located")
#northgruman
#blakesouthwood

#I can go through it and change the number

#LakeTahoe12#$
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
list_of_nested_switches.append(12)
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

##===========================================	
## number_nested_switches_in_sequence()
##===========================================
#put the input I just created into ibm[0]

forcedinputstring='''
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){          
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''
trouble=[]
trouble.append(forcedinputstring)
#this is using preset nested switch starting locations 11 and 29 for this test
# this is for making the nested switch numbered method 
def number_nested_switches_in_sequence(): # list_of_nested_switches[11,29]
	print("number_nested_switches_in_sequence()")
	newcount=1  #number of nested switches starts from 1
	## wait do I loopthru it get the position of the inner switches now why not
	## modification on july 24th 
	print("to see what it sees first")
	print(trouble[0])  #it was ibm[0] which I will change it back to later
	mystring=''
	mystring = trouble[0]
	newcounter=0
	foundone=[]
	
	# this gets the inner switch locations after the inner switch bodies have been stripped out (deleted)
	##===============================
	for line in mystring.splitlines():
		if "switch(exp)" in line:
			print("true we found switch")
			foundone.append(newcounter)
			newcounter += 1
			continue
		else:
			newcounter += 1
			continue
	print("we are done looking for the inner switch locations")
	print("====================")
	print("thefoundone llist has",foundone)
	print("the length is", len(foundone))
	print("========........======")
	print(" ")
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
		if  thecounter in foundone:  
		#this line of code is absolutely beautiful and elegant 
			print("thecounter=",thecounter)
			print("switchcount=",switchcount)
			########We know the line numbers do it on one pass perhaps
			# it should only go to the lines in the list of nested switches
			line = line.replace("switch(exp){","nested_switch_"  + str(newcount) +"(n)")
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
	trouble[0] = magic_string
	print("did I rip out the nested switches or are they still intact???")
	print("trouble[0]=",trouble[0])	
	#ibm[0] = shiney
			
####================================			
number_nested_switches_in_sequence()
print("it should have ran already testing bugs bunny here ")
			
			
			
			
			
			
			
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
#NUMBERING OF NESTED SWITCH HAS TO BE DONE BOTTOM UP SINCE WE ARE RIPPING OUT THE NESTED SWITCH AFTER THE SWITCH WORD
#oh I will have to do this bottom up so the line numbers are correct. 
print("I am taking out the lower switch first (later I will copy it first)")
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
get_switch_and_endswitch_locations(samplestring)


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










#made this july 10th in silver file just pasted it here.
##====================================================
##   BUILD STACKED CAKE STRING COMBINING STANFORD LIST
##====================================================
### important - need to add methods inswitch and infallthu at to
# the order should have already been reversed so that the main switch string is last.
def build_stacked_cake_string_combining_stanford_list(): 
    print("PRETENDING THAT THE LISTS HAVE BEEN MODIFIED THOUGH NOT REALLY YET")
    print("==================")
    print('lets pretend that the strings are finished and I will concat them together')
    print("but not run them")
    print("remember after the stanford list has been reversed the LAST list will be the main")
    volleyball ='' #initialized
    print("about to concat a string called volleyball")
    count =0
    #this goes thru the stanford list so the main switch is last.
    # and puts the contents into the string volleyball.
    function_defintions='' #initialized
    
    
    for item in stanford:
        volleyball += "\n"
        volleyball += "count="
        volleyball += str(count) + "\n"
        volleyball += item
        volleyball += "\n\n" #spacer 2 lines
        volleyball += "============ divider =========== \n"
        count += 1
        print(count)
    
    # here I can manipulate the output python code 
    # uppercase_test[0] == True:
    # baseline[0]="nada"
    print("volleyball =",volleyball)	
