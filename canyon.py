# This is a javascript switch case for Python. In Beta right now. Will add fixes to make it work completely
# later tonight to clean up the indentation for the output of the python.
# I will add the documentation and design and description of what each section does and why.

# It currently works with ifs and I will work on adding a dictionary version in a week.
# I still need to test it more and add numbers and macro thru to do things like:  case 1 thru 10:
# It's super complex but has a super simple design
# After it's working as designed I will make the function names and variables more descriptive.
# I will also remove the scaffolding.


switchcasetester = '''
	switch(grade) {
		case 'apple':  #first input x
		case 'money':
			print(\"first  section!\")
			print("one")
			
			
		case 'candy':
		case 'coconuts':
			print('second  section\")
			if color == 'red':
				print(color)
			else:
				print(no color)
			


		case 'fish':
		case 'marsbar':
			print('third  section')
			print('working on this')
			


		case 'panera':
		case 'peanuts':
			print('four try again')
			if failure == True:
				print('failed')
			else:
				print("keep trying")
			

		case 'tree':
		case 'snow':
			print('five christmas test')
			

		default: 
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''

disney_tron_trace_list=['starter']
######## show tron trace path
def show_tron_trace_path():
	print("#######==== showing TRON TRACE path list =====#####")
	#print(disney_tron_trace_list)
	counter=0
	last =''
	#reading thru looking for pairs
	for item in disney_tron_trace_list: #loops thru it
		print(item) #gives us the line number

#### mytrace
def mytrace(x): #just checks if first item is the same if slo don't load it
	disney_tron_trace_list.append(x)



newton=''
#switchcasetester=''
def convert_default_case(): #I got this working November 26th, 2020
	print("=====convert_default_case called===") #this needs to be called first definitely
	mytrace('convert_default_case')
	#input
	global switchcasetester
	print("this is the original input on switchcastester")
	print(switchcasetester)
	newton=switchcasetester.replace("default:","case 'default':")
	switchcasetester=''
	switchcasetester = newton
	print("this is after the change to same file name.")
	print(switchcasetester)
	#return switchcasetester
	#output

convert_default_case() #purely testing this. I need to add a main at the bottom	
#this is where I was calling the conversion of default to a case
#which involves outputting a new string





#from test_string_input import *
#from littletest import *




#this retrieves the switch doct string input and put it into the
# global variable theresult
#this function testing_this_out is called when this file loads
#def testing_this_out():
#	return
    #mytrace('testing_this_out')
    #print("testing_this_out testing; it calls input_string() from other file")
    #theresult =input_string()
    #print('this is going to print out the switch case looping lines...')
    #print(theresult)


#testing_this_out()

#so look for break and fallthru and also look for # if in line

#reember work on split comparison of javascript brace and python indentation


#traversing a list






def lucky():
    mytrace('lucky()')



def keeptrying():
	print("")
	#print("I need to traverse a list and access numbers")



foxy = "google"
treelist =['google', 'fishfood', 'probability']
def gothedistance():
    mytrace('gothedistance()')
    #print("gothedistance function called")
    if foxy in treelist:  #testing any now!!
        print("")
        #print("yes foxy word ", foxy, "is in list");
    else:
        print("")
        #print("testing any in list did NOT work")


def lookforit():
    #print(" ")
    #print("function look for it called")
    #print("testing this out")
    #print("about to test say(x) below")
    say("time for work now type faster thinking time")

def say(x):
    print(x)

def testing_number_of_lines_in_string():
	count =0
	for line in switchcasetester.splitlines():
		count +=1
		print(count)
	print("there were ",count, "lines in string")
	return count

list1 =[]
varholder =["four"]

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
	print("get_closing_brace called")
	mytrace('get_closing_brace')
	counter =0
	closing_brace =testing_number_of_lines_in_string()
	print("the line number of closing brace =",closing_brace)
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
	
		
	
	
	
print("======look below this line=======")
vartest ='''
print("===============vartest here does it  work or not")
apple = varholder[0] #where it grabs the data input
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
        print("fudgy")
        list1.append("fudgy gooey piggies is the reuslt");
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

exec(vartest)
#print("we have finished the if elif else tree")
#print("this is after it's been executed from string")
#print("list1 ==>",list1)

#lookforit()
#lucky()
#getsomeinput()
#gothedistance()
#testingatheory()






def lumbardstreet():
	print("")

	# based on line number of fallthru or position in list rather
	# what case is after it first?
def find_nearest_case_for_fallthru():
	print("")

'''
def coolness():
    print("the victory starts here ============")
	print("Wile E. Coyote genius")
	for item in getfirstword:
		print(item)

    #print(casephrase)
	print("now the case names")
	for item in casephrase:
		print(item)

'''




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
def magictimenow(): #starting counting from 1 instead of 0
	mytrace('magictimenow()')
	#print("first fillup a list with true and false")
	#print("true if case this line and false if not")
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

			print("the line number of teh first case is",coolcounter)
			firsttestforfirstcase.append(coolcounter)
			coolcounter +=1
			continue
		else:
			coolcounter +=1
			continue
	print("finished",firsttestforfirstcase)#this is list of trues and falses
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

	print("==========  CAFE BORRONE  ============")


	#print("========== massive test at cafe borrone ============")
	print("===========================")
	print('trontime=======>>>>>',trontime)
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
			print('default found')
			acounter +=1
			continue
		else:
			acounter +=1
			continue


	#print("crucial pumpkin time test to create ===== first case list ===========")
	#print("this should be the printing of the first case lists which is crucial to work")
	print("firstcaselist=",firstcaselist)
	#print("the firstcaselist is here....",firstcaselist)
	smartnewlist=[]
	
	for item in firstcaselist:
		if item != "default" :
			item = item[1:-1]
			smartnewlist.append(item)

		if item == "default":
			smartnewlist.append(item)


	print("smartnewlist=",smartnewlist)

	for item in firstcaselist:
		print(item)

	print(smartnewlist[1])



	#print("quick little test here to see what it sees")


	#print("end of show")
	#need to removequotes and : look thru my code elsewhere I have it
	print("###################")
	print("this is from the list named line_numbers_of_first_cases ")
	print("list of line numbers of first cases called line_numbers_of_first_cases=",line_numbers_of_first_cases)
	#theinputlist =line_numbers_of_first_cases[:]  #this should copy it
	print("##############")
	print("the input list should be ...",line_numbers_of_first_cases)



#line_numbers_of_first_cases=[]


###### how do I pass a list
#this might work
def get_first_list():
	mytrace('get_first_list()')
	
    #copy the list

   # theinputlist= line_numbers_of_first_cases[:]
    #print("the list in littlest file =",line_numbers_of_first_cases)
	print("====INPUT LIST TEESST=== =",line_numbers_of_first_cases)




#this finds teh first case in each case section and works
#should be: starter,apple, bananas,chocolate, fish,default
#digitalcandy=[[3,7],[7,19],[19,26],[26,33],[33,43],[43,46]]






coyote_list=[]  #initialize it
#trontime= ['empty', 'switch', 'case', 'case', 'code;', 'code;', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'break', 'empty', 'case', 'case', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'case', 'case', 'code;', 'code;', 'code;', 'code;', 'code;', 'empty', 'fallthru', 'empty', 'default', 'code;', 'code;', 'break', 'code;']
#coyote_list = trontime[:]  #THIS COPY MIGHT NOT BE WORKING
#coyote_list = trontime

# I can simply fill it manually with a loop and append
print(trontime)

birdsong=[0]
music=[0]
colorful=[0]
def make_list_of_first_cases():
	mytrace('make_list_of_first_cases')
	print("========== called make list of first cases() ===========")
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
	#print('list',birdsong)
	#print("I think that the list is called music",music)
	print('list',music)
	print("length of musiclist =", len(music))
	if len(music) % 2 !=0:
		music.append("0")
	#print("====end of make_list_of_first_cases=====================================")


#2, 3, 7, 8, 9, 10, 19, 20, 26, 27, 36
def go_thru_casenumbers():
	mytrace('go_thru_casenumbers')
	print('======= go thru casenumbers ========')
	#print('called go thru case numbers')
	#print("length of birdsong", len(birdsong))
	#print("length of music", len(music))
	dacounter=0
	#print("length of music list",len(music))
	for item in music:

		print(item,dacounter)
		dacounter += 1


		








make_list_of_first_cases()
#go_thru_casenumbers()




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
#print("lists inside of list solution that should work===")
#print("biglist =",biglist)
#digitial candy list right here premade elsewhere
#digitalcandy=[[2,7],[7,17],[17,24],[24,34],[34,43],[0,0]]
#this using digital candy???
listofifs =[]
#this is not called yet
#this walks through digitalcandy case tocase numbers
def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	mytrace('snowtime')
	print("================  big gears filling list with case bodies called  ==========")
	counter=0
	for item in digitalcandy:  #=[[2,14],[14,26],[26,33],[33,3],[38,43],[43,47]]
		print(item[0])
		print(item[1])
		counter += 1
		print("counter=",counter)
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
# and puts the case body into a string called pracestring1 which is concatted
	print("=======   s n o w  t i m e   ==============")
	#print("=====================  snowtime called", x, y," ===================")
	#print("===== this grabs body of code and writes it to practicestring1=============================================================")
	#print((" and then appends the whole body of the case to case_main_body_list"))
	#print("this creates a substring of case body for one case")
	#print("then appends it to sweetlist")
	global practicestring1
	practicestring1 = ""
	#switchcasetester isthe
	mycounter=0
	dog=''
	mytablist=[]
	  # so it's not 0
	#set_numbers_to_grab_between(x,y) #params go here
	#print("between ", x, " and ",y)
	#print(switchcasetester)
	#this is just doing one string case grab
	for line in switchcasetester.splitlines():   #so if they are together  stacked
	#this fills us practicestring 2 and a;sp a[[emd ot omtp sweetlist

		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line:  #macro between 2 and 13
		#this takes out the empty line by skipping it

			#added this sept 17 2020 to eliminate empty lines that do and mean nothing
			if len(line) == 0: #this means that the line is empty

				mycounter += 1 #see if this is necessary here or not
				continue
			else:
			
			#the solution is so simple just remove leading tabs which look like \t
				#puts some if so based on the number of tabs 
				# I know if it's nested  so 4 down to 3 and 3 down to 2 etc
				#surgery november 27th #################
				# this takes the tabs out of the line string
				nline = line.strip()
				line =nline
				########################################
				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
				cat1=practicestring1.count('\t')
				###### new
				practicestring1 = practicestring.strip()
				cat2=practicestring1.count('\t')

				practicestring1 =practicestring1 + "\n" 
				print('cat1 tabs =',cat1)
				print('cat2 tabs =',cat2)
				print("")
				#print(sublist)
	##############################
				#adding code
				dog=line.count('\t') #this counts tabs and puts the number into the variable dog
				print("TABS =",dog)
				sublist.append(dog)
				print('the tabs are invisible and embeddd in the code string.')
				#so I need to replace the three tabs with 2 tabs I think

		mycounter += 1
		print(sublist)
	mytablist.append(sublist)
	print("mytablist =",mytablist)
	#right here check if last character is \n if so slice it off
	practicestring1=practicestring1.rstrip() #take off \n at end

	#print("==== >>>> == this should be generated correctly formated ")
	#print(practicestring1)
	practicestring1 = practicestring1[:-1] #this chops off the \n on the end
	#print("==== >>>> == the string is added to case main body list")
	case_main_body_list.append(practicestring1)  #the body case code is added here
	
	del practicestring1  #this nukes it
	practicestring1 ='' #clears it out

#=========================================================================

def cotton_candy():
	mytrace('cotton_candy')
	#return #should kill it
	#casebody1 = practicestring1
	#print(casebody1)
	print("========cotton candy called ====")
	print("========cotton candy called ====")
	print("========cotton candy called ====")
	print("========cotton candy called ====")
	print("========cotton candy called ====")
	print("==...good...===I didn't realize that I was printing the case main body list here too")
	print("length of case_main_body_list =", len(case_main_body_list))
	print(case_main_body_list)
	answer=''
	for item in range(1,len(case_main_body_list)):
		print(item)
		item = item.strip()

		#answer =item.count("\t")
		answer =item.count('\\t')
		print("this many tabs in this line ",answer)
		answer = ''

	print("=====1============")

	print("=====2=========")

	print("testing to count number of tabs in some lines of case body code")
	print("is this thing TURNED ON??????")

		 

	

cotton_candy()

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





#testing_this_out() #this would be called when it's imported
#this calls the functiona bove testing_this_out()
#and then it loops through it printing out each line

#=====================================================








#will need to use switchcasetester.splitlines():
def truckeeriver():
	mytrace('truckeeriver')
	casecounter=0
	mycounter = 1
	print('truckee river called')
	for line in switchcasetester.splitlines():   #this was just going thru my prototype string of switch cases
		if "case" in line:				#and oh, I need to make sure I have tabs in my real js switch
			casecounter += 1
			if "case" not in line:
				if "\t" in line and not "break" in line and not "switch" in line and not "fallthru" in line and not 'case' in line:
					print(line)
					dog=line.count('\t') #this counts the tabs in front of a line
					turtle_tab1.append(mycounter)
					turtle_tab1.append(dog) #dog this counts total number of tabs in this line

				#casenumber += 1
					mycounter += 1

			#dog=line.count('\t')
			#if line[0]== '\t':
			#	print('tab0')
			#
			#if line[1]== '\t':
			#	print('tab1')

			#print(dog," tabs in line",line, mycounter)
			#mycounter += 1
		else:
			pass

	print("turtle_tab1 list=",turtle_tab1) #should be just one slot


#truckeeriver()


#coyote_list=["empty", "switch", "case","case", "code","break","empty","case","case","case","case","code","fallthru","empty","case","case", "code","break","empty","case","case","code","fallthru","default","code","break","code","empty"]
#this is a copy (the first word only) of the lines in the switch case.
#I need the switch caste line and splitlines



#big_gears_filling_list_with_case_bodies()
#cotton_candy() #see if it can access the contents of the case sections? unknown








my_list=[1, 3, 4, 5, 6]
global coyote_length
new_c_list = []
def shrink_coyote_list():
	print("======== shrink_coyote_list called ===========")
	mytrace("shrink_coyote_list")

    #global coyote_list;
    #r=0
    #get length of coyote_list
	global coyote_length;
	coyote_length = len(coyote_list)
    #print("the list length =", coyote_length)

    #print("the length of the list =", len(coyote_list))
	default_loc = coyote_list.index('default')
    #print("default_location is", default_loc)
    #get the postion of default and lenght of list
    #and delete tail of list after and including default
    #r = str(default_loc)
    #coyote_list = eval("coyote_list[:-" + str(default_loc) + "]")
    #print("coyote_list=",coyote_list)
    #print(coyote_list)

	for item in coyote_list:
		if item != "default":
			new_c_list.append(item)
			continue;
		else:
			break;

    #print("this is our new list")

    #print(new_c_list) #if this works I will be so pissed

    #print("the length of the new shortened list =", len(new_c_list))
#this is my solution for list out of range bullshit bug

	if (len(new_c_list))% 2 == 0:  #this would only be done once and modify the list
    #to manipulate.
		pass
	else:
		#print("not even length so odd length")
		new_c_list.append('nada')

    #print("new list after modfication =", new_c_list)


#shrink_coyote_list()




#============== get starting position in coyote

# ============= get current position in coyote

#============== add one to position in coyote


x = 0
destination =0
playwith =0
def get_starting_position_in_coyote(x):
    mytrace('get_starting_position_in_coyote')
    print("getting starting position")
    answer =new_c_list[x]  #this is what I'm looking inside of the list
    print("x =",x)
    print('position_0=',answer)
    #holdinglist.append(answer)
    #fall_to_position_in_coyote(x)





def get_current_position_in_coyote(x):
    mytrace("get_current_position_in_coyote")
    print("getting starting position")
    answer =new_c_list[x]  #this is what I'm looking inside of the list
    print("x =",x)
    print("current_position",answer)
   # holdinglist.append(answer)
    #fall_to_position_in_coyote(x)   #<<==== this is called automatically





hopper_list =[]
def add_one_to_position_in_coyote(x):
    mytraace("add_one_to_position_in_coyote")
    print("fall to position called")
    x= x + 1
    answer =new_c_list[x]
    print("x =",x)
    print('result=',answer)
    destination = answer;
    #hooper_list.append(destination)
    print('fall thru to case', destination)
    print("after_moving_one_slot_to_right",answer)



print("okay the fun starts here =======>>>>>>>>")

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

print("the number of case sections =",casecounter)




def new_add_to_front(x,listname):
	mytrace('new_add_to_front')
	print(" ============ function new_add_to_front() called =======")
	#listname.insert(0, x) #cool it worked
	listname.append(x)

    #go through copy of that list and del items
    #I see this represents building the list





fruits=[]
goldenlist = []
def build_test_list():
    mytrace('build_test_list')

    goldenlist.append("starter")  #first cases
    goldenlist.append("apple")
    goldenlist.append("bananas")
    goldenlist.append("chocolate")
    goldenlist.append("fish")

    #positions 0,1,2
    fruits = ['apple', 'banana', 'cherry']

    fruits.pop(1)      #removes element from list

    fruits = ['apple', 'banana', 'cherry']

    fruits.insert(1, "orange")
    fruits.insert(0, "Blake")

    new_add_to_front('Tahoe',fruits)
    new_add_to_front('cabin',fruits)
    new_add_to_front('santa cruz',fruits)
    new_add_to_front('pumpkins',fruits)
    #print("fruits list =",fruits)

build_test_list();


#this makes a list of the case name for the list of first cases in each section
def sunrise():
    #mytrace('sunrise')
    print("sunrise() called")



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
	mytrace("rule_the_earth")
	#this is to get the first case of each section
	print('======= ***** ===========rule the earth ==== creates starbucks list === *******  =====')

	mycounter =0
	second_word=''
	theline=''
	print("the input to figure out the first case in each list inputlist list =",line_numbers_of_first_cases)
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


			#print("baby=",second_word)

			#"'money':"
			#test  = second_word.rstrip(':"')
			#print("this is test=",test)
			#test2 = test.lstrip('"')
			#print("this is test2",test2)
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


	#print("this should print out what we have in the starbuckslist")



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

	#greenmilelist.append('default')  #=== here we are
	#print("starbuckslist=",starbuckslist)
	#print("mochalist =",mochalist)
	#print("greenmile =",greenmilelist)

	#print("=======")

	str = "'apple'"
	#print(str)
	#print(str.replace('"', ''))





sunrise();

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
	print("== **** ===this should be the list of first case names finally")
	print('starbuckslist =',starbuckslist)






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
    print(":::::::::::convert_to_twin_list called ::::::::::::")
    print("should be inputlist ",line_numbers_of_first_cases)
    print('length of input cases=',len(line_numbers_of_first_cases))
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


    #----------------------------------------
    print("------this is digital candy, diamonds, mainlist-----------------")
    print("digitalcandy=",digitalcandy)
    print("-----------------------")
    print("")
    for item in digitalcandy:
        #print(item)
        print(item[0],item[1])
    #output looks like this : diamonds=[[2,7],[7,19],[19,26],[26,36]]
    
## what this does is delete the existing last sublist from digitalcandy
## and then it replaces it with a new list appended that has the default line number and 
## curly brace line number (can alternatively be the last line of string) both equal length


def special_addition_to_digital_candy():
	mytrace("special_addition_to_digital_candy")
	print("=== special addition to digital candy ===")
	print("digital_candy starting out =",digitalcandy)
	digitalcandy.pop() #delete last item sublist
	print("digital candy after pop =",digitalcandy)

	#this gets the line number of the word default
	find_default = get_default_location()  #gets line number of default
	
	#this gets the line number of the closing brace (identical to last line of docstring)
	last_brace   = get_closing_brace()  #gets the line number of closing curly brace
	mystring = str(get_closing_brace()) #puts closing brace line number in mystring 
	print("mystring=",int(mystring))
	#defaullist is populated with default line number and closing brace line number 
	defaultlist.append(find_default)   #here the default list is 
	defaultlist.append(int(mystring))

	if find_default != None and last_brace != None:
		print("they both have something")
		print(find_default)
		print(type(find_default))
		print(last_brace)
		print(type(last_brace))

	print("defaultlist =",defaultlist)
	digitalcandy.append(defaultlist)
	print("digitalcandy=",digitalcandy)
	
	print("-----------------------")
	print("")
	for item in digitalcandy:
		#print(item)
		print(item[0],item[1])



magictimenow()
convert_to_twin_list()
special_addition_to_digital_candy() #===================added nov 25th, 2020
rule_the_earth()  ##=================






#================ this gets the case names from all cases
#talk about militant bullshit indentation -wasting my precious time unreal.
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
        if "default" in line: #see if this puppy works
            firstline = line.split()
            location_of_default = smartcounter
            break
            #smartcounter += 1;
        else:
            smartcounter +=1;



testing_this_to_get_word()  #==================this should call it now






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
    #I just added this for fun for some testing
    #I think I will use a new list and feed it info so it's seamless

    for item in royallist:
    	print(item)


#does_this_run()






#//=========== iron curtain============================

 ##===============================================================
  ####=================== American River Methods ==================
  ##===============================================================


  #================ this gets the case names from all cases
#talk about militant bullshit indentation -wasting my precious time unreal.
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
    print("=================create case name lists called == @@@@")

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
                print(line,smartcounter)
                genius =line.split()
                caseset.append(genius[1])
                #buildlist.append(line);
                smartcounter += 1;

    print("caseset list for one case section=",caseset);
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
   # print("testing getting the dam range to work")
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

     #we ARE STARTING A SECOND LOOP HERE -------------------
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

	print("================= C R A N B E R R I E S   L I S T ====case-tail-maker=========")
	print("ROYALLIST =",royallist)
	print('CRANBERRIES list =',cranberries)
	#this fills up trail_list from cranberries and creates a new list 
	print("============================")
	print("THIS IS THE TAIL LIST CALLED CRANBERRIES")
	for item in cranberries:
		print(item)
	

	
	#tail_list = copy.deepcopy(cranberries)
	print("see if this works == making the tail_list")
	#for item in cranberries:
	#	tail_list.append(item)
	





p51_mustang() #==========

'''
The purpose of this method == flyingcloud == is to fill small lists with
the respective case names
get case names in each set and add to list



'''




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


	nightowl()   #fills 
	#goodseason() #prints out smartcasemanager



#do not forget this
#still need to add case on the end called "default"
##==========================
##   flying cloud            this builds a list of the case names for each section
##==========================
smartcasemanager=[]
smartcasemanager.append("['starter']")
def flyingcloud(x,y,z):
	mytrace('flyingcloud')
	#print(' flyingcloud called to build first case list called starbucks')
	#print("FLYING CLOUD list of case names for putting in a list for each case section===")
	#print("flyingcloud called",x,y,z)
	smartcounter=0
	#print("x,y",x,y)
	for line in switchcasetester.splitlines(): #switch case in JS
		#print("inside of loop values of x,y at top of for loop ",x,y)
		#print("smartcounter=",smartcounter)
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
			#smartcounter += 1

	
	#========================================
#this fills up smartcasemanager list
def nightowl():
	mytrace('nightowl')
	

	print("length of digitalcandy =",len(digitalcandy), "which is how many case sections")
	
	i = 1
	#this filles the list smartcasmanager skipping 0 position
	while i <= len(digitalcandy):
		eval("smartcasemanager.append(" + "caselist" + str(i)+ ")")
		i += 1
	
	i+=1
	eval("smartcasemanager.append(" + "caselist" + str(i)+ ")")
	


#this prints out the smartcasemanager list to verify that it worked and has the sublists

#=================================
def goodseason():
	mytrace('goodseason')
	print("smartcasemanager list=",smartcasemanager)
	print("=== goodseason()  ======print what's in the smartcasemanager list of case list for each section")
	for item in smartcasemanager:
		print(item)



flyingfish()  #========

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
	#hoorayyy
	#print("----------------")
	#print("output from wildgame() ==>", ohbaby)

#== wildgame() this prints the first case list
print("== printing out starbucks list here")
print("this is the first case list of cases for each section ")
print("=======================")
print(starbuckslist)
print("========================")

#print("")
bronzelist.append("starter")
bronzelist.append(wildgame(1))
bronzelist.append(wildgame(2))
bronzelist.append(wildgame(3))
bronzelist.append(wildgame(4))
bronzelist.append("default")




mintlist=[]
mintlist.append('starter')
mintlist.append('break')
mintlist.append('break')
mintlist.append('fallthru(3)')
mintlist.append('fallthru(4)')
mintlist.append('default')








goldtaillist =[]
#I need to loop through this list and create the new list for final gold tail list
def autumn():  #this builds the break fallthru(nextcasename) list
	mytrace('autumn')
	#print("autumn leaves falling")
	#print("autumn called to make new list of breaks and fallthrus final")
	#print("please work I need this to work")
	counter =0
	print('starbucks =',starbuckslist)
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

	print("goldtaillist =",goldtaillist)




#autumn()

listnow=[]
listnow.append("starter")
listnow.append("fallthru")  #the number is derived from it's location in the list
listnow.append("fallthru")
listnow.append("break")
listnow.append("break")
listnow.append("default")

crushit =[]


#thurday, september 10, 2020 truck stop insight
#=============== stars() =============================
#=========== this goes thru dummy list with just starter fallthru and break and default
#==========/=== and adds the numbers of teh fallthru locations into crushitlist
#=======================================================

miraclelist=[]

def stars():
	mytrace('stars')
    #print('STARS test of loking for words in list')
	#print('look for break default starter fallthru')
	print("listnow =",listnow)
	counter =0
	print("starting looking in loop")

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

	#print("the end-------- we are here ------------")
	#print("crushit list =",crushit)
	print("starbuckslist=",starbuckslist)

	#====
	#starter is 0 but not a case
	#first case is position 1 (if fallthru(1)) it becomes fallthru(2) for conversion
	#so it is based on current position for the current case and then the NEXT case is +1
	#==========================================
	#input must be 1 or higher but less than the length-1 can't be starter (0) or default(length-1)
	wilson=''
	newnumber=''
	counter =0
	for item in crushit:
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

	#print("the end")
	print("starbuckslist=",starbuckslist)
	print("miraclelist list =",miraclelist)
	print("")
	print(miraclelist[0])
	print(miraclelist[1])
	print(miraclelist[2])







#theinputlist =[2,7,17,24]  # case case case case default   I took off 36 default
#total = len(theinputlist)
def rule_the_earth(): 
	mytrace('rule_the_earth')
	#this is to get the first case of each section
	print('======= ***** ===========rule the earth ======= *******  =====')
	mycounter =0
	second_word=''
	theline=''
	print("the input to figure out the first case in each list inputlist list =",theinputlist)
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
		if mycounter in theinputlist:
			#print(line)
			felix= line.split()
			print("felix=",felix)
			
			if "default" in line:
				second_word = line.split()[0]

			else: 
				second_word = line.split()[1]  
				

			print("baby=",second_word)
			
			
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
	print("starbuckslist=",starbuckslist)

	print("this should print out what we have in the starbuckslist")

	print("testing this::::")
	#RIGHT here is where I need to remove " and : from each item in list
	counter = 0
	print("new test here")
	mochalist.insert(0, "'starter'")
	for item in starbuckslist:
		#print(item)
		#if item != "starter":
		if item != "starter":
			item = item[:-1] #take out the :
			#===================================== experimental surgery here to have list
			
			#=====================================['apple','fish',etc]
			print(item)
			mochalist.append(item)
		else:
			mochalist.append(item)
	mochalist.append("'default'")

	print("the mochalist after adding starter and default to it ")
	for item in mochalist:
		print(item)


	acounter=0
	#greenmilelist.append('starter')
	for item in mochalist:
		if item != "starter" and item != "default":
			item[1:-1]
			greenmilelist.append(item)

	#greenmilelist.append('default')  #=== here we are 
	print("==============================")
	print("starbuckslist=",starbuckslist)
	print("==============================")
	print("mochalist =",mochalist)
	print("greenmile =",greenmilelist)

	str = "'apple'"
	print(str)
	print(str.replace('"', ''))
		
		
	print(greenmilelist)
	print("going through greenmile list")
	for item in greenmilelist:
		item[1:-1]
		print(item)
		print("fallthru(" + item + ")") #this is a test to see what it looks like

	print("testing seeing what's in each slot of green milelist here")
	print("green 0",greenmilelist[0])
	print("green 1",greenmilelist[1])
	print("green 2",greenmilelist[2])
	print("green 3",greenmilelist[3])
	print("green 4",greenmilelist[4])
	print("green 5",greenmilelist[5])




	#builder.append('default')
	# get rid of colon: at end of word default
	# fix this 'starter', "'apple':"  so apple looks like starter
	print("========end of rule the earth function=====")

#======== sutterrsmill==============================
case_main_body_list=[]
case_main_body_list.append('starter')  #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code

def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	print("================big gears filling list with case bodies called==========")
	
	
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
	print("=====/////======= smarty called =========//////=====")
	#print("line 818 snowtime(",x,y,")  S  N  O  W  T  I  M  E  ")
	#print("=====================  snowtime called", x, y," ===================")
	print("smarty x y testing blank lines existence to delete them")
	global practicestring1
	practicestring1 = ""
	mycounter=0
	for line in switchcasetester.splitlines():   
		if mycounter > x and mycounter < y \
		and "case" not in line and "break" not in line and "fallthrough" \
		not in line and "fallthru" not in line  and "}" not in line \
		and "{" not in line:  #macro between 2 and 13
		#this takes out the empty line by skipping it

			#added this sept 17 2020 to eliminate empty lines that do and mean nothing
			if len(line) == 0: #this means that the line is empty
				print(line.count("\n")) #just added this
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
				# ============== Glory =======================
				practicestring1 += line + "\n"  #this puts the lines of the string into practicestring1
				#=============== Glory =======================
				#line 2386 where the fun is

				#Right here  flag whether to add  + "\n"


			#############
				looky =line.count("\t")
				print('number of TABS in this line',looky,"line",mycounter)
				#subtracting 1 from each tab for the generated code format
				looky = looky -1
				dual_slots=[] #reset
				crummy =[]    #reset
				crummy.append(looky)
				crummy.append(mycounter)
				dual_slots.append(crummy)
				handy_list_of_tabs.append(looky)
				fiasco.append(dual_slots)
				
				#this is to analyze the tab count on each line beforehand
				myString = practicestring1
				print(myString)  #below zapping out pesky tabs at front
				# uses regular expression to nuke tabs
				output   = re.sub(r"[\t]*", "", myString)
				print(output)
				practicestring1 = output
				print("number of lines of code in each case section which I need to track")
				print('number of lines with \n =',practicestring1.count("\n"))
				n_count_per_section=practicestring1.count("\n")
			####################
		mycounter += 1
	
	### and here the practice string is added (appended) to case_main_body_list
	case_main_body_list.append(practicestring1)  #the body case code is added here
	
	del practicestring1  #this nukes it
	practicestring1 =''  #here we nuke practicestring1 so I can reuse for each case section
	print("=========")
	print("list of tabs=",handy_list_of_tabs)
	print("number of lines with code =",len(handy_list_of_tabs))
	print("pairs tabs and line number ",fiasco)
	print("number of lines in each section =", n_count_per_section)
	case_section_lines_of_code.append(n_count_per_section)
	print("=========")

def loop_thru_case_sections():
	print("======== loop thru case sections =============")
	mytrace('loop_thru_case_sections')
	print("loop thru cases sections which is a list")
	for item in case_section_lines_of_code:
		print(item)

loop_thru_case_sections()  #=================
icecream=''
def herewego(): #loops and prints all main bodies
	mytrace('herewego')
	#this loops through the case_main_body_list and prints the case python code
	print("here we go () called it prints the case body code from the list ")
	#mightymouse = "happy"
	print("======= here we go() called =======")

	counter=0
	print("length of case body list =", len(case_main_body_list))
	#print(case_main_body_list)
	#this loops thru the case_main_body_list
	for item in case_main_body_list:
		if counter == 0: #skips the first slot "starter"
			counter += 1 #I forgot the bloody counter
			continue

		print("=========================================")
		print(case_main_body_list[counter])

		icecream= case_main_body_list[counter].count("\n")

			#myString = practicestring1
			#	print(myString)  #below zapping out pesky tabs at front
			#	# uses regular expression to nuke tabs
			#	output   = re.sub(r"[\t]*", "", myString)

		print("==== ICE CREAM number of lines of code in section =====")
		print("the number of lines of code in this  section=",icecream, "section",counter)
		
		print("================================",counter)
		counter += 1
		
		
		
		
	print("experimenting here in here we go")
	#get length (number of lines) of each
	body_size = len(case_main_body_list[3])
	print("the number of lines =",body_size)

print("")

acounter=0
for item in case_main_body_list:
	print(len(item))
	acounter += 1
    
    

print("digitalcandy=",digitalcandy)
big_gears_filling_list_with_case_bodies()
herewego()  #==================================
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
		partynation(x,y) #partynation called here 
		acounter += 1
	#adding default to see if it works
	#firstcasesectionlist.append("default")
	#this happens after the loop has finished
	print("what 9999 is this =",firstcasesectionlist)
	print("----------")
	counter=0
	list_of_rows_of_case_names.append(firstcasesectionlist) #since this will be the last one
	print("== CRITICALTEST ==")
	print(list_of_rows_of_case_names)
	castle_time()

smartcasemanager=[]  #creating the initializing smartcasemanager

#just added these twolines wednesday nov 18th
#caselist0 = ['starter']
#smartcasemanager.append(caselist0)

#this just prints it out the sets of the cases for each case section
def castle_time(): #fills up smartcasemanager
	mytrace('castle_time')

	#list_of_rows_of_case_names.append("[['default']") #trying this
	print("============CASTLE_TIME called ===========")
	count=0
	while count < len(list_of_rows_of_case_names):
		if count == 0:
			count +=1
			continue
		print(list_of_rows_of_case_names[count][1:])
		count += 1

	print("more testing to get this right")
	for item in list_of_rows_of_case_names:
		print(item)

	##################################################
	### SMARTCASEMANAGER LIST FILLED HERE ############
	##################################################
	
	#this fills up list smartcasemanager from list_of_rows_of_case_names
	#this is doing a brute force copy of a list
	for item in list_of_rows_of_case_names:
		smartcasemanager.append(item)
	
	
	print(smartcasemanager)
	smartcasemanager.pop()
	print('after deleting last item in list')
	print(smartcasemanager)

	finallist = ['default'] #see if this works 
	list_of_rows_of_case_names.append(finallist)
	#print("this should be default below======+++")
	print(list_of_rows_of_case_names[-1])
	#smartcasemanager.append("['default']") #using a default case so it can be fallthrud from above
	print(smartcasemanager) #now we add default to the end or do we need to or not
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
			print('this is in wild here',wild)
			firstcasesectionlist.append(wild)  #adding this case name to firstcasesectionlist
			#print("TESTING what this is doing")
			#print(firstcasesectionlist)
		mycounter += 1
	#end loop
	#This is forcing default into firstcasesectionlist
	#wild = 'default'   #major test here 
	#firstcasesectionlist.append(wild)
	for item in firstcasesectionlist:
		item.replace('"',' ' )
	#print(firstcasesectionlist)
	
	firstcasesectionlist[1:-1]
	for item in firstcasesectionlist:
		item.replace('"',' ' )
	#here the currently newly minted case list is added to the big list 
	#which is called list_of_rows_of_case_names
	list_of_rows_of_case_names.append(firstcasesectionlist)


	print("PARTY NATION testing  to see what's in here dam")
	print(list_of_rows_of_case_names)
	#this resets it
	firstcasesectionlist= []
	#firstcasesectionlist.append('starter')
	

make_case_sets()



#=== code gen here ====


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
print("this will run at the top of the page and call the functions in sequence\n")
#cranberries=[]
my_godzilla_list=[]
newlist=[]
smartylist=[]
tryagain=[]
coollist=[]
#test data here it will be one file and just flow down with no imports
#rodan=[2,7,17,24,34]

tabs =['starter',"\t","\t\t","\t\t\t","\t\t\t\t","\t\t\t\t\t","\t\t\t\t\t\t"]

'''
def stage_one():
	mytrace('stage_one')
	starter()
    convert_default_case()
    make_list_of_first_cases()
    cotton_candy()
    build_test_list()




def stage_two():
	mytrace('stage_two')
	magictimenow()
    convert_to_twin_list()
    special_addition_to_digital_candy()
    get_default_location()
    get_closing_brace()
	



def stage_three():
	mytrace('stage_three')
	rule_the_earth()
    testing_this_to_get_word()
    p51_mustang()
    flyiing_fish()
    loop_thru_case_sections()
    big_gears_filling_list_with_case_bodies()


def stage_four():
	mytrace('stage_four')
	herewego()
    make_case_sets()
    castle_time()


def stage_five():
	mytrace('stage_five')
	doghouse()
    parktime()
    switch_code_gen()


'''



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

'''
caselist0 = ['starter']
caselist1 = ['apple','money'] #took out 'money' to verify it works with one
caselist2 = ['bananas','coconuts','strawberries','tangerines']
caselist3 = ['chocolate','marsbar']
caselist4 = ['fish','peanuts']
caselist5 = ['wine']
caselist6 = ['default']  #here it is
'''






#case_main_body_list=[]  #dummy data this will be gleaned thru parser
'''
case_main_body_list.append('starter')
case_main_body_list.append("\t\t\tif color == 'red':\n\t\t\t\tprint(color)\n\t\t\telse:\n\t\t\t\tprint(no color)")

case_main_body_list.append("\t\t\tprint('second case')\n\t\t\tprint('testing 2')")
case_main_body_list.append("\t\t\tprint('third case')\n\t\t\tprint('testing 3')")
case_main_body_list.append("\t\t\tprint('fourth case')\n\t\t\tprint('testing 4')")
case_main_body_list.append("\t\t\tprint('fifth case')\n\t\t\tprint('testing 5')")
case_main_body_list.append("\t\t\tprint('default case')\n\t\t\tprint('default d')")
'''

#remember that I am just generating this code to build a string and not interpetting
#it in pydev just yet, got a get it lined up correctly first

#Here is the tail list
#I had to add another break for the case default so the list had the same length as the other lists for input

#tail_list =['starter', "fallthru('bananas')", "fallthru('chocolate')", "fallthru('cherries')", 'break', 'break','break']


#  these are the inputs for the code generator
#
#  lists where they are generated correctly
#
#  smartcasemanager has caselist1 - 5  # in shark_code_generation.py lists of cases for each case section
#
#  case_main_body_list # suttersmill.py has the tabs done right in the switch case input
#	  		   			#this has the code inside of each case section tabbed correctly
#
#  tail_list  miraclelist in palomar.py #breaks and fallthrus
#
#for item in digitalcandy
print("length of digitalcandy list",len(digitalcandy))
print("")
print("length of firstcasesectionlist list",len(starbuckslist))
print("")
#adding default case 
#smartcasemanager.append("['default']")
print("length of smartcasemanager list",len(smartcasemanager))
print("")
print("length of case_main_body_list list",len(case_main_body_list))
print("")
print("length of taillist list",len(cranberries))
print("")
###=================================================================
###  below I get the location of default and closing curly brace for end of switch
###  this is to be used for determining the default case which is utilized for
###  the situation of a fallthru down into default
###  this also adds one more case tothe regular cases and I need these parameters

print("============ surgery here S=================================")
print("")

def make_default_case():
	find_default = get_default_location()
	print("NEW location of default =",find_default)

	lastbrace = get_closing_brace()
	print("NEW location of closing brace =", lastbrace)


	#digitalcandy.append
#november 21st coding
#make_default_case()

## what I still need to put together to have the body of the default case
## and that will be used for the default case and the body of the else:

'''
 so if line is > default and line is < lastbrace
 and "break" not in line 
 and fill practice string and append the pracietce sting to case_main_body_list
use snow(x,y) and a loop to grab the lines of code inside of default
make sure "
'''

print(" this prints out the contents of the important lists")

print("==============================================")
print("digitalcandy list ========")
for item in digitalcandy:
	print(item)
	
print("starbucks list ====of first case names in each section ====")
print(starbuckslist)

print("smartcasemanager list ========", len(smartcasemanager))
for item in smartcasemanager:
	print(item)

print("case_main_body_list list ========", len(case_main_body_list))
for item in case_main_body_list:
	print(item)

print("==========tail list ========", len(cranberries))
for item in cranberries:
	print(item)

print("they all need to start with 'starter' in position 0")
print("the big 3 need to have the same number of elements for the length to be the same")

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

def doghouse():
	print("dog house attempt")
	mytrace('doghouse')
	counter =0
	sublist=[]
	together=[]
	sowhat=''
	#print(case_main_body_list[1]) #it was counter
	#sowhat = case_main_body_list[1]
	print("========going into the deep abyss=====")
	#================================
	weasel1 =[]
	maybe = case_main_body_list[1]
	print("attempt1")
	case_lines= 2
	s1=[tabs[2],tabs[2]] #first section lines indentation
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)
			weasel1 = s1[0] + line
		if counter == 1: #line number
			print(s1[1] + line)
		counter += 1

		#========
	maybe = case_main_body_list[2]
	print("attempt2")
	case_lines= 2
	s1=[tabs[2],tabs[2], tabs[3], tabs[2], tabs[3]] #first section lines indentation
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)

		if counter == 1: #line number
			print(s1[1] + line)

		if counter == 2: #line number
			print(s1[2] + line)

		if counter == 3: #line number
			print(s1[3] + line)

		if counter == 4: #line number
			print(s1[4] + line)
			
		counter += 1


	#=========================

	#========
	maybe = case_main_body_list[3]
	print("attempt3")
	case_lines= 2
	s1=[tabs[2],tabs[2], tabs[3], tabs[2], tabs[3]] #first section lines indentation
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)

		if counter == 1: #line number
			print(s1[1] + line)

		if counter == 2: #line number
			print(s1[2] + line)

		if counter == 3: #line number
			print(s1[3] + line)

		if counter == 4: #line number
			print(s1[4] + line)
			
		counter += 1
	#=========================
	maybe = case_main_body_list[4]
	print("attempt4")
	case_lines= 2
	s1=[tabs[2],tabs[2], tabs[3], tabs[2], tabs[3]] #first section lines indentation
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)

		if counter == 1: #line number
			print(s1[1] + line)

		if counter == 2: #line number
			print(s1[2] + line)

		if counter == 3: #line number
			print(s1[3] + line)

		if counter == 4: #line number
			print(s1[4] + line)
			
		counter += 1

	#===========
	maybe = case_main_body_list[5]
	print("attempt5")
	case_lines= 2
	s1=[tabs[2]] #first section lines indentation means just one line output
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)
		counter += 1

#=========================
	maybe = case_main_body_list[6]
	print("attempt6")
	case_lines= 2
	s1=[tabs[2],tabs[2]] #first section lines indentation
	counter=0  #remember need to stip out \\n from second
	for line in maybe.splitlines():
		if counter == 0: #line number
			print(s1[0] + line)

		if counter == 1: #line number
			print(s1[1] + line)

		
			
		counter += 1




		

		


		
		
doghouse()

	

	
def parktime():
	print("P A r K T i M e =========////////t/t/t/t/t/t/t/t")
	mytrace('parktime')
	import re
	myString = "\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
	print(myString)
	output   = re.sub(r"[\n\t]*", "", myString)
	print(output)

parktime()




#input for the switch case happens (above) the docstring JavaScript switch case interface 
varholder =[]
varholder.append('money')

#====--------------------------------------------------------

# =======  switch  =================================
def switch(x):
    if type(x) != str:  
        x = str(x)
    global case
    case = x.lower() 
    print("switch sees",x)


# =======   fallthru       =========================
# the magic is here fallthru actually calls switch
def fallthru(y):
    eval("switch('" + y + "')")


##===================

def rocket_science():
	print("==///=====rocket science called=====///===")
	print(case_main_body_list[3])
	mylist =[]
	mylist = case_main_body_list[3]
	

#if line.startswith("if"):
	#result = tab added to front
rocket_science()

#  ====== project mr coffee ========
#this takes in the lists calculated above and generates a docstring of python switch case code
def switch_code_gen():
	mytrace('switch_code_gen')
	print("#===========switch code gen called================ ")
	print("")
	
	# wednesday testing eve of thanksgiving
	# the generated python switch is generated and saved in 
	# a variable called switch_python_gen

	#here will be the caselists for each case section that will be generated
	#I have to make a doctring with a name for the output python that will be run.
	
	print("switch_python_gen='''")  #name of  generated docstring switch_python_gen
	#this builds the case lists for each case section
	#which are used when it says: if case in caselist2:
	#print(foolish)
	exp = varholder[0]

	print("exp shows as input",exp)
	print("")
	numb = 1
	counter = 1
	#thedefault = "['default']"
	# for i in range(len(list_fruits)):
	numberofcaselists = len(smartcasemanager)-1
	#print('number of caselists =',numberofcaselists)
	#print('first caselists one is',smartcasemanager[0])
	while numb <= int(numberofcaselists): #5
		trains =  str(counter)
		merge = "caselist" + trains        #caselist1
		toosmart = eval(merge)                    	#caselist1
		caselist = merge + " = " + str(toosmart)    #this is the caselist name we eval to display it
		print(caselist)
		#sweet += caselist  #new
		counter += 1
		numb += 1
	#print("caselist" + str(counter +1) + "= default")
	#smartcasemanager.append("['default']")
	#print(smartcasemanager[-1])
		#this prints the default caselist which will be the the length of the list
		#even though the 0th one of smartcasemanager is starter
	#genius= tabs[1] + "caselist" + str(numberofcaselists) + "=" + smartcasemanager[-1]	
		######## this is added after the loop finishes above
		#thought nov 23 it's designed to read cases so give it a cas

		#######=========== nov 23 obvious solution to getting it right
		#change the input so default is case default: then it will read it
		#just like all of the others - pure genius
	
	#print(genius)
		#########
	print("")


	print('#list input varholder=[] must be above function with switch')
	print("varholder.append(exp)")
	print("case = varholder[0]")
	print("exp = varholder[0]")
	print("")
	print("switch(exp)\n" +"while True:\n")
	print("")
	#=== start loop ====
	mycounter =1 #it was 0
	#size=  #notice -1
	front="case in caselist"
	#while mycounter <= len(case_main_body_list):     #6
	for item in range(1,len(case_main_body_list)):
		if mycounter == 1: #first
			first_if= tabs[1] + "if " + front+str(mycounter)   + ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [first_if, toosmart]
			print(str(newlist[0]) + " " + str(newlist[1]))
			#sweet += str(newlist[0]) + " " + str(newlist[1])

		else:    #rest of cases after first case
			restofifs= tabs[1] + "elif " + front+str(mycounter)+ ": #"
			toosmart = eval("caselist" + str(mycounter))
			newlist = [restofifs, toosmart] #comments put case names to right of caselistnumber
			print(str(newlist[0]) + " " + str(newlist[1]))
			#so i need to modify a smart-tabbed version of teh case_main_body_list
			#before generating it -then it will work. Genius.
		print(case_main_body_list[mycounter] )
		print(tabs[2] + cranberries[mycounter])   #case section
		#it had tabs[2] + case_main_body_list[mycounter]
		#print(tabs[2] + cranberries[mycounter]) #the tail
		print("")
		mycounter += 1     #loop counter
	#=== end loop ========
	print(tabs[1] + "else:")
	print(case_main_body_list[-1])    #last case
	print(tabs[2] + cranberries[-1])  #last break   tail_list
	print(" ''' ")  #end of decleration of switch output docstring
	##################################################

	print("")       #remember close the docstring
	print("=================== big test here generating it output to string")
	print("testing printing this to see it after it's generated...")
	#I can concat it together perhasto a variable, brilliant

	#print(switch_python_gen)

	
varholder =[]
varholder.append("money")
switch_code_gen() ##=== this calls and generates the python switch case 
				  ##=== this has the code generation of the python code
print(switch_python_gen)
exec(switch_python_gen)
#==========================================================================================
#===== this is test what will be generated below after the python switch is generated above



####======= this is the input to the python switch
#input_list = ["fortune"]  #global var that will be fed into switch(x)


def bigtestofcodegen():
	mytrace('bigtestofcodegen')
	print('BIG TEST OF CODE GEN CALLED  this executes the python switch case')
	print("===== massive test =======")
	exec(switch_python_gen)

	#one_fine_day()

def one_fine_day():
	mytrace('one_fine_day')
	print("one fine day called")
	codeObejct = compile(switch_python_gen, 'input_list', 'exec')
	exec(codeObejct)
	




list1=[]
list1.append("five")

    #this would be generated python code with switch() and fallthru() functions
    #this docstring has different rules










vartest ='''
print("happy donuts")
print('this is going to execute python code from a doc string')
x = list1[0]
print("it sees ---- ",x)




print("===============vartest here does it  work or not")
case = x #varholder[0] #where it grabs the data input
print("it sees",x);

print('case=',case)
print("what the heck does x equal before the switch",x)
switch(x)
while True:
    print("inside of the while true x =",case)
    if case == "two":
        print("it's two")
        print("this is two time now ")
        break;
    elif case == "three":
        print("fudgy")
        print("fudgy gooey piggies is the reuslt");
        break;
    elif case == "five":
        print(" fifty little piggies");
        
        print("looks good - you can see everything")
        fallthru('six')
        
    elif case == "six":
        print(" ten little cats");
        
        print("meow meow meow")
        break;
        
    else:
        print("no matches found")
        break;
'''
#exec(vartest)

show_tron_trace_path()
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
one =''
#### the cow jumped over the moon 
def the_cow_jumped_over_the_moon():
	print("======the cow jumped over the moon========")

	one = "print('first  section!')\nprint('one')\n\n\n"
	two = "print(\'second  section')\nif color == \'red\':\nprint(color)\nelse:\nprint(no color)\n\n"  
	
	print(one)
	print(len(one))
	print("one test")
	print(one)
	print('now tab test')
	legend = tabs[2] + one
	print(legend)
	thetail =one[-4:]
	print("the tail=",thetail)
	#######


	print(two)
	print('now tab test')
	legend2 = "\t\t" + two
	print(legend2)

	thetail =two[-4:]
	print("the tail=",thetail)


	print("=======")
	jumanji=one.split('\n')
	print("hopefully this makes the jumanji list and prints each sentence out")
	counter=0
	print("the length of jumanji=", len(jumanji))
	for item in jumanji:
		#if here for counter and tab number 
		flag1 = 2
		if flag1 == 2 and counter == 1:  #experimenting with examples here 
			print("\t\t" + item)
		if flag1 == 3:
			print("\t\t\t" + item)


	print("======")
	jumanji2=two.split('\n')
	print("the length of jumanji2 =", len(jumanji2))
	counter=0
	print("hopefully this makes the jumanji list and prints each sentence out")
	for item in jumanji2:
		print("\t\t" + item)

	        
 
	#three = "print('third  section')\nprint('working on this')\n\n"                                        
  
	#four = 'print(\'four try again\')\nif failure == True:\nprint(\'failed\')\nelse:\nprint("keep trying")\n\n'
  
	#five = "print('five christmas test')\n\n"                                                                  
   
	#six = 'print(\'six walking duck de fa ul t\')\nprint("flying geese")\n'  





the_cow_jumped_over_the_moon()




'''
'starter', 

one = 'print("first  section!")\nprint("one")\n\n\n',                                                       3 \n

two = 'print(\'second  section")\nif color == \'red\':\nprint(color)\nelse:\nprint(no color)\n\n',          2 \n
 
three = "print('third  section')\nprint('working on this')\n\n",                                               2  \n
  
four = 'print(\'four try again\')\nif failure == True:\nprint(\'failed\')\nelse:\nprint("keep trying")\n\n',  2 \n
  
five = "print('five christmas test')\n\n",                                                                     2 \n
   
six = 'print(\'six walking duck de fa ul t\')\nprint("flying geese")\n']                                      1 \n
'''



smartlist_number_of_true_lines=[]
def onelasttest():
	mytrace('onelasttest()')
	print("======= one last time ======")
	counter =0
	the_memory='false' #default setting status of line above

	for item in case_main_body_list[counter]:
		sweet = case_main_body_list[counter].count("\n")
		if sweet != 0:
			sweet = sweet -1

		print("number of lines =",sweet)
		smartlist_number_of_true_lines.append(sweet)
		counter += 1
	print("===========")
	print("list of lines in each section",smartlist_number_of_true_lines)
	counter=0
	for item in case_main_body_list:
		print(len(item))

		for line in item.splitlines():
			if line.startswith("if"):
				the_memory="true"
			else:
				the_memory="false"

			if line != '\n':
				print(tabs[2] + line) 


			


	 

onelasttest()

mymainlist=[]
badass =[]
def nuclear_winter():
	counter =0
	for item in case_main_body_list[counter]:
		wilson = item
		badass.append(case_main_body_list[counter])
		
		mymainlist.append(badass)
		counter += 1
		

	sweet=''
	counter1 = 0
	for item in mymainlist:
		print(item)
		return
		
	

nuclear_winter()



'''
['starter', 'print("first  section!")\nprint("one")\n\n\n', 'print(\'second  section")\nif color == \'red\':\nprint(color)\nelse:\nprint(no color)\n\n', "print('third  section')\nprint('working on this')\n\n", 'print(\'four try again\')\nif failure == True:\nprint(\'failed\')\nelse:\nprint("keep trying")\n\n', "print('five christmas test')\n\n", 'print(\'six walking duck de fa ul t\')\nprint("flying geese")\n']

'''

#this is the case_main_body_list 

'''
['starter', 
'print("first  section!")\nprint("one")\n\n\n', 
'print(\'second  section")\nif color == \'red\':\nprint(color)\nelse:\nprint(no color)\n\n',
"print('third  section')\nprint('working on this')\n\n",
'print(\'four try again\')\nif failure == True:\nprint(\'failed\')\nelse:\nprint("keep trying")\n\n',
"print('five christmas test')\n\n", 
'print(\'six walking duck de fa ul t\')\nprint("flying geese")\n']
'''



#def working_on_final_brew():
#this is the lsit that I will add tabs too
# Driver code     


# Python program to convert a list to a string
# to string using join() function 
    
# Function to convert   
def listToString(s):
    print("listToString called")  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

#running = case_main_body_list or change it to a string 


#working_on_final_brew()

s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s))  

#given string
string1="Python is great"

#printing the string
print("Actual String: ",string1) 
  
print("String coverted to list :",string1.split()) 
#prints the list given by split()

def marine_one():
    print("====== marine one called =====")
    print(switchcasetester)
    print("the number of tabs in this baby")
    tabnumbers =switchcasetester.count("\t")
    print("tab total =",tabnumbers) 

marine_one()
