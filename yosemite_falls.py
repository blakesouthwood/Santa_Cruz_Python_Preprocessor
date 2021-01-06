Jan 5th 10pm Pacific Time Jan 5th 2021
Was testing the thru macro and realized there could be more than one occurance in a switch so 
I figured out how to manage the thru macros so that there can be innumerable thru macros for cases in a switch case.
example
case 1 thru 5:
case 6 thru 15:
case 16 thru 25:
case 26 thru 50:


Jan 5th. Made a lot of bug fixes and added more features that I dreaded of implimenting months ago.
I made massive progress in the past few days and am extremely happy it's working as envisioned.
Documenting and making the code pretty. Renaming everything so it's cohereent and easy to follow.
Will also make a map diagram of the architectural structure. The program was made from about 50 modules
and then pieced together. My first parser and code generator. I will gradually upload the working code
in the new few days. I need to delete the dead code not being called. 

Jan 4th 2021
Got case words working
case “alpine meadows”:   # works; origininally I only tested using one word and then I thought, try more words.
It can be up to ten words now
Will add higher limit later

Got switch case using just numbers figured out (and working now) Jan 5th!!! 
This code now works. January 5th
It tests if cases are numbers and then runs special code to handle numbers
as opposed to words.

Not implimented yet but prototype works. (works now) 
case 1:
   Bla bla bla

case 2:
   Bla bla bla

case 3 thru 7:  #working on thru macro currently  #macro working at 7:42pm Jan 5th, 2021
     Bla bla bla

*experimenting*   #will work on this later. Got a lot figured out and working tonight. 
With goto  label based on
C design usage 


    goto labelname;

label:


#Dec 31st 7:14pm
Fixed bugs and worked on new features: Will upload changes later.
Figured out how to do multiple words like "alpine meadows" for cases rather then solitary words in a string for cases such as "Google".
Figured out how to do numbers such as case 1:  case 23:  and macro  so it's possible to do:   case 1 thru 10:
Solved bug that crashed parser if no break in default by adding break automatically if missing.
So now it's possible to write a true C switch case that doesn't require a break at end of
default section but default is required per Yale C Standards.


#dec 28th 9pm.
Switch in Beta.
Just found a few bugs the more I test it.
Just noticed Python doesn't generate teh default case but it's an easy fix.
Now using Sublime and Visual Studio Code for testing. I only got it actually fully working tonight.

#dec 28th, 2020  6:03 pm
finally works as designed
V I C T O R Y  JavaScript switch case works in Python!!
Will make it pretty now. Trial and error.
Will likely update code to web tonight.
Working on using more than one word in a case like "alpine meadows"

what prototype looks like currently using switch case


from yosemite_falls import *  #this is the switch case module
#this module will be renamed switchcasemod

def cool():
	print("cool running now")
	clever('olaf') #this fills the exp for switch
	#this is a docstring multiline string used to hold tabbed switch case
	sw = '''
	switch(exp) {
		case 'snoopy':  
		case 'linus':
			print(\"where's the dog house!\")
			print("first prize")
			break

		case 'olaf':  
		case 'tim':
			print(\"tennis wannabees!\")
			print("what is the score again")
			break
			
		case 'tomato':  
		case 'table':
			print("make some ketchup")
			print("== you gotta work===")
			break

		case 'tahoe':
		case 'donner':
			print("will I live there some day\")
			
			
		case 'fish':
		case 'marsbar':
			print('third  section')
			print('working on this')
			
		case 'panera':
		case 'peanuts':
			print('four try again')
		
		case 'bestwestern':
		case 'travelcenter':
			print('nice place to stay')
			break
			

		case 'alpine':
		case 'squaw':
			print('ski fast in the powder')
			break
			
		default:
			print('six walking duck de fa ul t')
			print("no matches")
			break
}
'''
	endswitch(sw)  #this calls the parser and codegenerator and executes the generated python
	#Output currently prints the generated python. Which is turned on for debugging purposes.

	
cool()  #function call



#dec 28thj 8:05 am 
'''
working on communicating with the switchcase module from other files to allow seamless
operating of switch cases.
Considering all options since I can't use a circular import.



'''

#dec 24, 2020 4pm pacific standard time progress putting code in module
#talking to goldfish right now which will be input file

#from triple_lindy import * 
#imports the switch case

#defining varholder


# This is a javascript switch case for Python. In Beta right now. Will add fixes to make it work completely
# later tonight to clean up the indentation for the output of the python.
# I will add the documentation and design and description of what each section does and why.

# It currently works with ifs and I will work on adding a dictionary version in a week.
# I still need to test it more and add numbers and macro thru to do things like:  case 1 thru 10:
# It's super complex but has a super simple design
# After it's working as designed I will make the function names and variables more descriptive.
# I will also remove the scaffolding.
#============================
#the switch case string will be outside of this file
#but the input will be the name for now switchcasetester


switchcasetester=''
ball=''




switchcasetester = '''
	switch(exp) {
		case 'coffee':  
		case 'tea':
			print(\"where is my mocha!\")
			print("extra hot with whip")
			break

		case 'walmart':  
		case 'target':
			print(\"it is christmas eve and I brought in the carts!\")
			print("everything is on christmas sale")
			break
			
		case 'frosty':  
		case 'rudolph':
			print(\"so many snow men!\")
			print("first sled the sleigh ready")
			print("=== I hate bugs ====")
			break

		case 'candy':
		case 'coconuts':
			print("see's candies  section\")
			
			
		case 'fish':
		case 'marsbar':
			print('third  section')
			print('working on this')
			
		case 'panera':
		case 'peanuts':
			print('four try again')
		
		case 'motel':
		case 'hotel':
			print('do you have a reservation')
			break
			

		case 'alpine':
		case 'squaw':
			print('ski fast in the powder')
			break
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''
varholder=[]
varholder.append("zilch") #if nothing changes it's default

#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
	print("clever called")
	varholder[0]= i
	print(varholder[0]) #to actually see proof


def adjust_input(x):
	print("adjust input called with", x, "inside of yosemite")
	newstring =varholder.append(' + x + ')
	#print(newstring)
	#eval(newstring)
	#print(varholder[0])
# Remember that the output code gen is invisible and won't be seen by 
# he programmer
case = ''
# =======  switch  =================================
def switch(x):
	#print("switch method called",x)
	if type(x) != str:
		x = str(x)
	global case
	case = x.lower()
	
def budweiser():
	print("bud-weis-er")

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
def make_list_of_first_cases():
	mytrace('make_list_of_first_cases')
	#print("========== called make list of first cases() ===========")
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			smart=line.split()
			#print(smart[1])
			birdsong.append(smart[1])
			music.append(mycounter)
			mycounter += 1
		else:
			mycounter +=1
	
	#print("I think that the list is called music",music)
	
	
	if len(music) % 2 !=0:
		music.append("0")
	
	
#what I can do is have a simple true or false switch
#and leave the function calls where they are and if triggered true
#then they will be called otherwise they won't be called.


#start_trigger()

#I need to add a break if there isn't one saturday, December 5th
#it expects a break at bottom of default.
#and I just realized it requires a default but doesn't look for one 
newton=''
#switchcasetester=''
def convert_default_case(): #I got this working November 26th, 2020
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
	#print(switchcasetester)
	return switchcasetester
	
	#output
#
#convert_default_case() #purely testing this. I need to add a main at the bottom
#this is where I was calling the conversion of default to a case
#which involves outputting a new string





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
    #print("testing theory method dropping var into stringwithcode")
    #print("getting resulting value inside switch case output after")
    #print("leaving docstring switch")

    #apple = "one"
###=================== nov 19th new code ============
###================ get_closing_brace (line number) ==============
closing_brace=''
def get_closing_brace():
	#print("get_closing_brace called")
	mytrace('get_closing_brace')
	counter =0
	closing_brace =testing_number_of_lines_in_string()
	###print("the line number of closing brace =",closing_brace)
	#for line in switchcasetester.splitlines():   #so if they are together  stacked
	#	if "}" in line:
	#		closing_brace = counter
	#		print('location of closing brace =',counter)
	##	else:
	#		counter += 1
	#		continue

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


#print("======look below this line=======")
#print("this is vartest testing the prototype testing four in varholder[0]")
#print("this should return nothing")
vartest ='''
print("===============vartest   works")
apple = list1[0] #where it grabs the data input
print("it sees",apple);
while True:
    if apple == "two":
        print("it's two")
        list1.append("two little pigs");
        break;
    elif apple == "three":
        print("ti'w three")
        list1.append("three little pigs");
        break;
    elif apple == "four":
        print("four horsemen")
        list1.append("four horsemen ran to get piggies is the reuslt");
        print("list=",list1)
        break;
    elif apple == "five":
        print(" fifty little piggies");
        list1.append("fifty little piggies");
        print("list=",list1)
        break;
    else:
        print("no matches found")
        break;
         '''

#exec(vartest)




print("this is actual generated code I am trying to run now....")
print("this is betterworknow in python generated previously")



list1=[]
exp =''; case =''
exp = ""

#exec(betterworknow)
print("=== executin betterwork now test bit")




############## this needs to  work right now ######## launch the rocket
#TRY IT HERE  I will call the variable christmastree
#print("tyring to exec(christmastree) see if it runs")


christmastree='''
exp = varholder[0] 
caselist1 = ['coffee', 'tea']
caselist2 = ['walmart', 'target']
caselist3 = ['frosty', 'rudolph']
caselist4 = ['candy', 'coconuts']
caselist5 = ['fish', 'marsbar']
caselist6 = ['panera', 'peanuts']
caselist7 = ['tv', 'deers']
caselist8 = ['default']
switch(exp)
while True:
	if case in caselist1: # ['coffee', 'tea']
		print("where is my mocha!")
		print("extra hot with whip")
		fallthru('walmart')
	elif case in caselist2: # ['walmart', 'target']
		print("what a sale today!")
		print("everything is on christmas sale")
		
		break
	elif case in caselist3: # ['frosty', 'rudolph']
		print("so many snow men!")
		print("first sled the sleigh ready")
		break
	elif case in caselist4: # ['candy', 'coconuts']
		print("see's candies  section")
		
		
		break
	elif case in caselist5: # ['fish', 'marsbar']
		print('third  section')
		print('working on this')
		
		fallthru('panera')
	elif case in caselist6: # ['panera', 'peanuts']
		print('four peanuts again')
		
		fallthru('tv')
	elif case in caselist7: # ['tv', 'deers']
		print('five christmas test')
		print("will it work in time for santa")
		fallthru('default')
	elif case in caselist8: # ['default']
		print('six walking duck de fa ul t')
		print("flying geese")
		break
	else:
		print('six walking duck de fa ul t')
		print("flying geese")
		break
'''
#print("testing running python code with christmastree")
#exec(christmastree)





####======== starts here ===============
#this is the function triggered to start the parser and codegen
def start_trigger():
	#global switchcasetester  #just added this to hopefully fix bug
	trigger = True
	print("trigger =", trigger)
	if trigger == True:
		print("trigger =", True)
	else:
		print('trigger=',False)

	mytrace('start_trigger')
	#print("this will go first")
	#print(switchcasetester)
	convert_default_case()
	



def stage_one():  #this calls start_trigger()
    #print('stage one')
    start_trigger()

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
def magictimenow(): 
	mytrace('magictimenow()')
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
		#I need to look at two lines at the same time
		#if "case" in line:
		#	print("previous line",ifcaseinline[mycounter-1],mycounter-1)
		#	print("this line case",ifcaseinline[mycounter],mycounter)
		#	if ifcaseinline[mycounter-1] == "false":
		#		print("this is what I am looking for",mycounter)

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

		if len(line.strip()) == 0: #will it work (doubtful)
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


	##print("========== massive test at cafe borrone ============")
	#print("===========================")
	#print(trontime)
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

    #copy the list

   # theinputlist= line_numbers_of_first_cases[:]
    #print("the list in littlest file =",line_numbers_of_first_cases)
	#print("====INPUT LIST TEESST=== =",line_numbers_of_first_cases)




#this finds teh first case in each case section and works
#should be: starter,apple, bananas,chocolate, fish,default
#digitalcandy=[[3,7],[7,19],[19,26],[26,33],[33,43],[43,46]]








#2, 3, 7, 8, 9, 10, 19, 20, 26, 27, 36
def go_thru_casenumbers():
	mytrace('go_thru_casenumbers')
	
	dacounter=0
	#print("length of music list",len(music))
	for item in music:

		#print(item,dacounter)
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

def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	mytrace('snowtime')
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

def snowtime(x,y):  #this grabs the body from one case section at a time
	mytrace('snowtime')
	global practicestring1
	practicestring1 = ""
	#switchcasetester isthe
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

def cotton_candy():
	mytrace('cotton_candy')

	answer=''
	for item in range(1,len(case_main_body_list)):
		#print(item)
		item = item.strip()

		#answer =item.count("\t")
		answer =item.count('\\t')
		#print("this many tabs in this line ",answer)
		answer = ''



def stage_two():
	mytrace("stage_two")
	print('stage two')
	cotton_candy()
    
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








#will need to use switchcasetester.splitlines():
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
    print('stage three')
    mytrace("stage three")
    truckeeriver()







my_list=[1, 3, 4, 5, 6]
global coyote_length
new_c_list = []
def shrink_coyote_list():
	#print("======== shrink_coyote_list called ===========")
	mytrace("shrink_coyote_list")

    #global coyote_list;
    #r=0
    #get length of coyote_list
	global coyote_length;
	coyote_length = len(coyote_list)
    #print("the list length =", coyote_length)

    #print("the length of the list =", len(coyote_list))
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
    #print("x =",x)
    #print('position_0=',answer)






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





def new_add_to_front(x,listname):
	mytrace('new_add_to_front')
	#print(" ============ function new_add_to_front() called =======")
	#listname.insert(0, x) #cool it worked
	listname.append(x)

    #go through copy of that list and del items
    #I see this represents building the list











#what I already solved was how many sections of case groups there are
#now I need to get the remaining case locations
#if case not in line meaning after first case section so this would start after the last case in the first section
#July 30th, 2020 fun
# i should know how many cases in each section
####THIS GETS THE FIRST CASE IN EACH CASE SECTION THE LINE NUMBER
starbuckslist=[]
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
def rule_the_earth():
	#print("rule the erath called at 940")
	mytrace("rule_the_earth")
	#this is to get the first case of each section
	#print('======= ***** ===========rule the earth ==== creates starbucks list === *******  =====')

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
	##for case sets I just go thru till case not in line and fill a new list
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		if mycounter in line_numbers_of_first_cases:
			#print(line)
			felix= line.split()
			#print("felix=",felix)

			if "default" in line:
				second_word = line.split()[0]

			else:
				second_word = line.split()[1]


			
			#======================  thursday surgery cleaning up the words 'words'
			wild= second_word[1:-1]
			#print("wild=",wild)
			wild = "'" + wild  #adding a ' to left side of word
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
	#print("starbuckslist=",starbuckslist)




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










starbuckslist=[]
starbuckslist.append("starter");
def this_needs_to_work_badly():
	mytrace('this_needs_to_work_badly')
	print('===============this needs to work badly called =======to get first case name ==')

	#new_add_to_front(x,listname)
	mycounter = 0
	print('case section line number list =',builder)
	for line in switchcasetester.splitlines():   #so if they are together  stacked
		#batterondeck represents previous loop count
		#go thru case list here as the feeder
		if mycounter in builder:
			genius = line.split() #new  [0] was at end of it  ((this does the line split for each line))
			#print(genius[1])    #gets word of that case
			baby = genius[1]
			new_add_to_front(baby,starbuckslist)
			mycounter += 1 #n
		else:
			mycounter += 1
	




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
def convert_to_twin_list():  #uses list called line_numbers_of_first_cases
    mytrace("convert_to_twin_list")
  
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

def special_addition_to_digital_candy():
	mytrace("special_addition_to_digital_candy")
	
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
		global switchcasetester
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
	mytrace('stage_four()')
	#print('stage four')
	magictimenow()
	convert_to_twin_list()
	special_addition_to_digital_candy() #===================added nov 25th, 2020
	rule_the_earth() 






#================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0


#this is a super important function I think I wrote it at the beach a few days ago
def testing_this_to_get_word():
    mytrace('testing_this_to_get_word')
    #print("======def ======testing this to get word() ==================")


    smartcounter=0
    #this looks for "case" in the switch case string
    for line in switchcasetester.splitlines(): #switch case in JS
        if "case" in line: #see if this puppy works
            firstline = line.split()
            #print(firstline)
            #print(firstline[0])
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
    mytrace('create_case_name_lists')
    #print("=================create case name lists called == @@@@")

    smartcounter=0 #reset at zero
    genius = ''
     #need list of first cases that will work for input
    #Thursday coding to save this day from a disaster of nothing working
    ##===================================================================
    ## LOOP LOOKING  CASE SECTION APPEND LINES FROM BODY AFTER CASES UNTIL NEXT FIRST CASE
    ##=======================================================================
    for line in switchcasetester.splitlines(): #switch case in JS
        #print("smartcounter =",smartcounter)
        if smartcounter >= x and smartcounter < y:  #so get what's inbeteen
        #this should just look
            if "case"  in line:
                #print(line,smartcounter)
                genius =line.split()
                caseset.append(genius[1])
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
def case_tail_list_maker(x,y):
    mytrace('case_trail_list_maker')
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
  ##==== def p51_mustange() ===  adds the number to  fallthru(3) like that
  ##===========================
  #this makes the cranberries list which is the tail list used on codegen page
#diamonds=[[2,7],[7,17],[17,24],[24,34]]
#this makes the cranberries list
def p51_mustang(): #makes critical cranberries list which is the taillist for switch cases
	mytrace('p51_mustang')
	counter = 0
	c = 1		#current case numbr section
	d = c + 1

	for item in digitalcandy:	#this is going through the diamonds list

		clever = digitalcandy[counter]
		x = clever[0]
		y = clever[1]
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

	#print("================= C R A N B E R R I E S   L I S T ====case-tail-maker=========")
	#print("ROYALLIST =",royallist)
	#print('CRANBERRIES list =',cranberries)
	#this fills up trail_list from cranberries and creates a new list
	#print("============================")
	#print("THIS IS THE TAIL LIST CALLED CRANBERRIES")




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
	mytrace('flyingfish')
	mytrace('flyingcloud')
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
		flyingcloud(x,y,z) #z starts at 1 and adds 1 to z with each loop
		z += 1
		thecounter += 1

	nightowl()   #fills smartcasemanager
	




##==========================
##   flying cloud            this builds a list of the case names for each section
##==========================
smartcasemanager=[]
smartcasemanager.append("['starter']")
def flyingcloud(x,y,z):
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
			wilderness = firstline[1] #this grabs the case name
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
def nightowl():
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

def loop_thru_case_sections():
	#print("======== loop thru case sections =============")
	mytrace('loop_thru_case_sections')
	#print("loop thru cases sections which is a list")


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
    
    
#print("tail_list cranberries =",cranberries)
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




#======================================
#  ====== project mr coffee ========
#this takes in lists calculated above and generates a string of python switch case code
def switch_code_gen():
	mytrace('switch_code_gen')
	
	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.
    
	
	 #name of  generated docstring switch_python_gen
	#print("varholder.append(exp)")
	

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

	## ===========  LOOP =============
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
	counter =0  #each section will have the same number of items
	for item in firstpart:
 		rocks += str(firstpart[counter]) + "\n" + str(secondpart[counter]) + "\n" +str(thirdpart[counter]) + "\n\n"
 		counter += 1
 	#printing out the three part case sections")
 
    #a -----main list so sublists in the main list
    # so I only use ONE LIST for all three 
    #adding strings together here 

	sweet = topvars2 + cool + switchy + rocks
	#for debugging I will have a flag here to see output and test separately for user
	#print(switchcasetester)
	print(sweet)
	
	print('testing executing generated string of code...')
	print(" =================")
	exec(sweet)  #this is the building of the string of python code strings
	
	#if default == True
	#print('what they entered')










#this executes the generated python switch code 
def stage_twelve():
	mytrace('stage_twelve()')
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




#this is new but I haven't tried it yet december 5th
def starter_sequence():
	print("oh my god starter_sequence called will it work???")
	stage_one()
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
	switch_code_gen() #it's called right here
	stage_twelve()
	

def smart():
	starter_sequence()

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

