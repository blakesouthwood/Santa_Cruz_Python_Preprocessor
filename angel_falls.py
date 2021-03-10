Tuesday, March 9th, 2021 4 PM Californai time
testing valve for words or numbers for switch.
putting two separate modules and then will merge into one once it's working correctly
I will put the number operations into a few specific functions.
But the code works and runs in Visual Studio Code which has a good step debugger and nice dark theme.
Will try to add new features gradually instead of addding everyting and hoping. This way it's 
more like the IBM 360 with frequent releases and slowly adding to the pyramid so it's always stable and always working
and much easier to debug. 

Got Sublime and got weird bug but code compiles in bbedit but not in Sublime with module reload.

Monday, March 8th, 2021  8 am California time
Victorious coding session. 
Fixed bug so if no break it's added at bottom of default case.
Tested fallthru  fallthrough  and missing break and breaks worked flawlessly.
Did testing last night and this morning and switch case is stable.
Nirvana.

Next I will test the switch module and test multiple switch cases in several different
functions.




Sunday, March 7th, 2021  10:57 pm California time
generated output just now... wow.


exp = varholder[0]

caselist1 = ['snoopy was flying', 'linus', 'lucy']
caselist2 = ['colin likes ice cream', 'blake']
caselist3 = ['thank god', 'table']
caselist4 = ['william pilot']
caselist5 = ['xmas', 'newyears']
caselist6 = ['panera', 'peanuts']
caselist7 = ['motel 6 in gilroy', 'travelcenter']
caselist8 = ['alpine meadows', 'squaw']
caselist9 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['snoopy was flying', 'linus', 'lucy']
		print("where's the dog house!")
		print("first prize")
		print("you block head Charlie Brown")
		break

	elif case in caselist2: # ['colin likes ice cream', 'blake']
		print("coding right now")
		print("================")
		fallthru('thank god')

	elif case in caselist3: # ['thank god', 'table']
		print("lucky to have bbedit")
		print("=for my backups=")
		print("----------------------")
		fallthru('william pilot')

	elif case in caselist4: # ['william pilot']
		print("jet figher pilot extroideniare")
		print("-------------")
		get('phantom jet')
		fallthru('xmas')

	elif case in caselist5: # ['xmas', 'newyears']
		print('christmas')
		print('new years eve')
		break

	elif case in caselist6: # ['panera', 'peanuts']
		print('four try again')
		fallthru('motel 6 in gilroy')

	elif case in caselist7: # ['motel 6 in gilroy', 'travelcenter']
		print('nice place to stay')
		fallthru('alpine meadows')

	elif case in caselist8: # ['alpine meadows', 'squaw']
		print('ski fast in the powder')
		fallthru('default')

	elif case in caselist9: # ['default']
		print('six walking duck de fa ul t')
		print("flying geese")
		break

	else:
		print('six walking duck de fa ul t')
		print("flying geese")
		break


===== executing generated  code=====
the input exp in clever was::  linus

where's the dog house!
first prize
you block head Charlie Brown

 =====done executing output from switch ======


Sunday, March 7th, 2021  10:30 pm California time
Solved cleaning up the breaks and fallthrus beneath the output Python code

In the code generator I melded the third tier break/fallthru to the next line
beneath the case_main_body_list which is done with a loop before actual generation
of the output and it thus eliminates the third tier addition at the end of the
code generation

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
		acounter += 1


output of case main body for each case section

		print("where's the dog house!")
		print("first prize")
		print("you block head Charlie Brown")
		break
--------------
		print("coding right now")
		print("================")
		fallthru('thank god')
--------------
		print("lucky to have bbedit")
		print("=for my backups=")
		print("----------------------")
		fallthru('william pilot')
--------------
		print("jet figher pilot extroideniare")
		print("-------------")
		get('phantom jet')
		fallthru('xmas')
--------------
		print('christmas')
		print('new years eve')
		break
--------------
		print('four try again')
		fallthru('motel 6 in gilroy')
--------------
		print('nice place to stay')
		fallthru('alpine meadows')
--------------
		print('ski fast in the powder')
		fallthru('default')
--------------
		print('six walking duck de fa ul t')
		print("flying geese")
		break
--------------


Sunday, March 7th, 2021  9:00 pm  California time.
Smart break and fallthru detector works.
If missing break in default it's added (finally)
Now cleaning up the output so the breaks and fallthrus are attached to the bottom of the individual case sections.
Currently the beaks and fallthrus are a few spaces below each case section. It was a vexing problem months ago
but I just came up with a simple solution that will definitely work and clean it up.
The solution for determining if there was a break after default:
The problem was if there was no break after default the parser would not run.

######################################

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



################
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
	
	
#########=============== get last break in string ==================
listofbreaks=[]
genius=''
nobreaks = "false"
def get_last_break_in_string(): #but what if no break??? march 1st bad assumption here
	print("======BLINK182========get last break in string in the whole switch case string ============")
	mytrace('get_last_break_in_string()')
	counter=0
	global switchcasetester
	for line in switchcasetester.splitlines():
		if "break" in line:
			listofbreaks.append(counter)
			nobreaks = "false"	
			counter +=1
		else:
			counter += 1
			continue
		###=============
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
	
'''
example output during testing
get_default= 53
last break = 34
last line  = 59

the result therefore is:
there is definitely no break in default case
and a break needs to be added immediately
adding break at bottom of default case now
we now have look for the new break in default
''	      
	      
###################################
def convert_default_case(): #I got this working November 26th, 2020
######################################
	print("convert_default_case()  ===&&&&&-- ")
	#add_break_to_bottom_of_default()  ##march 3rd, 2021
	mytrace('convert_default_case')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location()
	print("get_default line number=",get_default) #line number of default
	print("lets see the LIST OF BREAKS  full list",listofbreaks)
	
        last_break=get_last_break_in_string() #what if it returns None???
	#this is new march 1st 2021 starbucks coding in earlying
	last_line_of_string = get_length_of_string()
	print("the last line of string =",last_line_of_string)
	'''
	This is a simple math problem.
	Using the line numbers in the string
	get default line number
	get last break line number (from list)
	get last line of string determined by closing brace (yes)
	The next scenario I will add will be if break count == 0 add break at bottom of default case
	if int(last_break) < int(get_default):
		add break using replace
		this is done by using replace in the string and renaming it
	
	'''
	print("get_default=",get_default) #line number of default
	print("last break =",last_break)  #next figure out if NO BREAK WHATSOEVER
	print("last line  =",last_line_of_string)
	print("the result therefore is:")   #decided default will be required by the user
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

INPUT switch case inside of python program looks like this for testing

#this is  input variable exp for switch(exp)
print("===== FIRST 1st switch =====")

clever('linus') #this would change varholder[0] 
#maybe test put endswitch(sw) inside of clever function hidden
sw = '''
	switch(exp) {
		case 'snoopy was flying':  
		case 'linus':
		case 'lucy':
			print(\"where's the dog house!\")
			print("first prize")
			print("you block head Charlie Brown")
			break

		case 'colin likes ice cream':  
		case 'blake':
			print("coding right now")
			print("================")
			
			
		case 'thank god':  
		case 'table':
			print("lucky to have bbedit")
			print("=for my backups=")
			print("----------------------")
			

		case 'william pilot':
			print("jet figher pilot extroideniare\")
			print("-------------")
			get('phantom jet')
			
			
			
		case 'xmas':
		case 'newyears':
			print('christmas')
			print('new years eve')
			break
			
		case 'panera':
		case 'peanuts':
			print('four try again')
			
			
		
		case 'motel 6 in gilroy':
		case 'travelcenter':
			print('nice place to stay')
			
			

		case 'alpine meadows':
		case 'squaw':
			print('ski fast in the powder')
			
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			
			
}
'''
endswitch(sw)

### TESTING OUTPUT OF GENERATED PYTHON CODE FOR THE PYTHON VERSION OF THE SWITCH CASE CODE ###
Note it uses methods switch() and fallthru()

exp = varholder[0]

caselist1 = ['snoopy was flying', 'linus', 'lucy']
caselist2 = ['colin likes ice cream', 'blake']
caselist3 = ['thank god', 'table']
caselist4 = ['william pilot']
caselist5 = ['xmas', 'newyears']
caselist6 = ['panera', 'peanuts']
caselist7 = ['motel 6 in gilroy', 'travelcenter']
caselist8 = ['alpine meadows', 'squaw']
caselist9 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['snoopy was flying', 'linus', 'lucy']
		print("where's the dog house!")
		print("first prize")
		print("you block head Charlie Brown")
		break

	elif case in caselist2: # ['colin likes ice cream', 'blake']
		print("coding right now")
		print("================")
		
		
		fallthru('thank god')

	elif case in caselist3: # ['thank god', 'table']
		print("lucky to have bbedit")
		print("=for my backups=")
		print("----------------------")
		
		fallthru('william pilot')

	elif case in caselist4: # ['william pilot']
		print("jet figher pilot extroideniare")
		print("-------------")
		get('phantom jet')
		
		
		
		fallthru('xmas')

	elif case in caselist5: # ['xmas', 'newyears']
		print('christmas')
		print('new years eve')
		
		break

	elif case in caselist6: # ['panera', 'peanuts']
		print('four try again')
		
		
	
		fallthru('motel 6 in gilroy')

	elif case in caselist7: # ['motel 6 in gilroy', 'travelcenter']
		print('nice place to stay')
		
		
		fallthru('alpine meadows')

	elif case in caselist8: # ['alpine meadows', 'squaw']
		print('ski fast in the powder')
		
		
		fallthru('default')

	elif case in caselist9: # ['default']
		print('six walking duck de fa ul t')
		print("flying geese")
		
		
		break

	else:
		print('six walking duck de fa ul t')
		print("flying geese")
		
		
		break


===== executing generated  code=====
the input exp in clever was::  linus

where's the dog house!
first prize
you block head Charlie Brown

 =====done executing output from switch ======
 

Sunday, March 7th, 2021  10:34 am  California time
Taking approach of updating the program in phases and putting stable vanilla switch case code up tonight.
I will then add separate modules that are addon modules to manage the complexity that will
be imported from the switch case module to organize and manage the growing complexity of this beast of a program.
Look for updates tonight.

Solved some bad assumptions I made for the logic and possible scenarios  for breaks and fallthroughs and default.
I assumed there would be a default and there actually might not be a default.
I assumed that there would be at least one break inside of a switch case and there could be none. I was being presumptious. 
I had to reengineer my code to deal with these presumptions I made of what to expect from the user about what was out of the realm
of possibility to handle all what-if situations to guard against the failure of the switch case working as intended and expected.
I was happy that I realized that I needed to consider all possible scenarios. Of course this all happened by accident.
All of these changes were triggered by breaks being missed which was pure happy chance. 

More importantly the codebase has grown and to manage the complexity this morning I decided
to divide and conquor and create separate modules for the features to more easily control the codebase.
	
	
	Thursday, March 4th 2021  8:36 PM
buggy function currently working on debugging

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
	return default_location
##############################################
##	add_break_to_bottom_of_default():
##################################################
lovely=''
def add_break_to_bottom_of_default():   #this currently doesn't run yet 
	print("just called ADD_BREAK_TO_BOTTOM_OF_DEFAULT()")
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
	
	print("this is after the loop has gone through looking for break after default line")		
	if findbreak == True:
		print("do nothing break exists after default")
		print("it will be interesting if this is true, but I can test it")
		print("the number of breaks found in the switchcasetester was",x)
		print("let's look in switchasetester and see for ourselves.")
		print(switchcasetester)
	else:
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
	return break_location
	
	
	//===============================

Thursday, March 4th,2021
Out of the blue companies started contacting me to interview.
6 AM California Time

Worked on code to add break into default since a legal switch case works with no breaks in C which is the design
but the parser requires a break in default. So working on that impimentation currently.

Making filter for using case "words": and case 4: // right now they are separate

Working on bugs.



Tuesday, March 2nd, 2021   9:56 AM   California Time
	
Indentation errors(bugs) due to missing or misaligned INVISIBLE tabs in Python are balony.
95% of my bugs are missing tabs messing up the invisible scope.

I am adding braces { this week} . I shouldn't have to waste time thinking in terms of spaces and tabs when
I want to concentrate ON THE CODE AND THE BOOLEAN LOGIC and not tab, tab, tab, tab, whoopse missed a tab, my life stops,
my train of thought is interuppted. So tabs will be done with smart tab logic using braces for scopoe like
in C, JavaScript, C++, Java, etc, etc, etc.

But wait Python doesn't understand braces except for dictionaries and fstrings. Of course it doesn't. It's just for the gui interface
parser and then lovely sprinking tabs will be inserted using lovely fuzzy-logic to the generated pristine Python code.

Working on bug squashing today. Notably if missing break in default case the parser crashes (funny). Testing solution now.
Adding filter for detecting if a switch case is using cases with numbers like case 44:  or string words case "apple pie":
After rereading Tony Hoare's Turing Lecture decided to work and update the project in phases with frequent releases
so I can have verified bonified progress and showing my code.

end of line.







Monday, March 1st, 2021  7am California Time Listening to Daft Punk today and Eye in the Sky.

Adding do while from Mozilla JavaScript today. Will have braces and also throwing in macro for doing ++ and -- from JavaScript/C
It will have it's own parser and generator and work just like the switch case as a long variable docstring.
Braces mandatory and semicolons are optional. Forced rediculous indentation for output will be automatic so you don't waste time indenting.
#from Mozilla example in JavaScript for do while. The switch case was a dream and then when I learned
of glaring omissions of language aspects that Python dearly needs I decided to add them so that progrmamers that
are coming from JavaScript and C and C++ will can think and write code the way that they want to and how they think.
Every time I hear or read an article where some developer says "oh Python can't do this this or that I feel sick to my stomach."
The issue is the designer of the langauge was not American and I am enjoying Americanizing Python or rather making python more Californian.
My biggest gripe other than the indentation straightjacket is the glaring missing switch case which is now a working reality.

Once the codebase is stable for the switch case I will upload it when I'm happier with it. Still need to document parts and I decided to refactor parts
of it to make it more efficient and more readable so it's comprehensible. I am currently fixing the last bugs and finished reengineering
what was clearly flawed. The thought that millions and perhaps billions of coders will use these improvements for python is quite a rush.
But for me coding and melding C, JavaScript, and Lisp into Python just seems more natural and the way that it should be. 

I have absolutely no problem with braces after dealing with lame indentation. The IDEs I use are to see the indentation. It's stupid.
I think that the forced indentaiton is a massive weakness in Python and freeing programmers from having to think in invisible white spaces
and instead use tried and true braces is now an option that they can enjoy and revel in. Braces are tangible and visible and 
they make complete sense and they have been time tested. Further if someone copies and pastes so code that they already wrote
in C or JavaScript into what I refer to as the envelope plastic window parser and codegen to reuse (already working code) then
more the better. This adds incredibly more flexibility to Python too and this way programmers don't waste time translating
from one langue to the other when it can be done automatically.  I feel that what I am doing is liberating Python from its chains
and liberating programmers so they can write more code and writer it faster and enjoy coding more - I know I am feeling better with
these new revolutionary liberties. 

let result = '';
let i = 0;

do {
  i = i + 1;
  result = result + i;
} while (i < 5);
print(result);
#// expected result: "12345"

	


Decided to finally impliment hash table dictionary version of python switch case
so I will modify the codegen for if elif else structure for a verison that does dictionaries.
#the switch will be in the code at the top with a comment
#use ifs
or
#use dictionaries

Will finish implimenting more efficient and elegant design for break fallthru construction adding methods
to aid performance, reuse, and readability. Already designed it and nearly done impimenting it. Reduced
the code for it by more than 95%. It's more intelligently designed now and much cleaner. Pure zen. 
Solved fallthru bug to work with more than one word for case; now works for n words.
Solved wrong break location bug. Solved proper fallthru construction bug.

This will happen over the course of the day.
Will be doing testing today.
Getting paid version of Sublime Text (which I miss badly) on Thursday to increase my progress since BBEdit
isn't the end all that I hoped it would be but is great for doing diff but I miss the indentation lines
and look and feel of Sublime which locked me out because I haven't paid for it yet, but will on Thursday (payday).





Tuesday, Feb 23, 2021
Implimented the smart break fuzzy logic detector so it's faster and actually works.
Found new bug (simple to solve) it won't work unless there is a break after default when scanning in parser.
I enjoy the discovery process of the funcitons transformed from thought to running code.
Always interesting what it takes to make it work. 

For the switch case to meet with the criteria in the initial design of 
a switch case in C for this python implimentation it requires a default:
I finally got some momentum after getting stuck with the redesign of 
detecting breaks.

I had so much momentum and then when doing further testing I noticed that it was missing breaks. 
Finally working again. Glad I had backups.

I also got slowed down by fallthru not working with more than one word in a case, fixed it using a join

new code:
'''
this rips everything off the string except for the actual case name.
the first case name is the representative for each case section no matter how many cases it may have.
'''

def get_case_name(y):  #y will be the line
    print("get_case_name called")
    #y = y.split()
    y = y.replace(":","")
    y = y.replace("case","") #remove case
    y = y.replace("\t","")    # remove :
    print(y)
    return y


'''
this gets the case number in a sequence starting from 1 for each case section
this uses listname.index('casestring') which is compared from the firstcaselist
'''
def get_location_of_case(listname,word):
    print("listname,word=",listname,word)
    print("get location of case () called ")
    print("this is searching for ",word)  #below took out  + "'" + both sides of word
    answer =eval("" + listname + ".index("  + word + ")")
    print('====after running get_location_of_case we get this== should be a number==')
    print("location of case",word," in listname=",answer)
    return answer

'''
there is no list method for replacing an index location so I made one
it's just hardcoding listname[indexnumber] = string
I am using two methods to make it work by just calling do_replace(number,word)
'''
def replace_in_list(x,y,z):  
	z[x]= y   #listname[5] = 'word'
	#this doesn't do print of the list afterwards

def do_replace(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=british  #list name for breaks and fallthrus final
	replace_in_list(x,y,z) 
	
	
'''
this is deep inside of the parser
get a case name and strip it down to just the word(s)

'''
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
		
		'''
		when "break" is found in a line it's referenced by the counter line number in the switchcase string
		and then the genius is I grab the casename from above that was found in the first line which is equal to x
		with x, y in each sublist inside of the list digitalcandy for each case section parameters 
		'''
		
		if "break" in line:
                print("===== gold ======")
                print("we found a break line number =",x,y,smartcounter)
                
                wilecoyote.append(mrcase) # first case number in digitalcandy
                #I will put the case name instead of x
		
# some more code that fills list called british(for now) with fallthrus
# the way this works is I only look for break otherwise it's already fallthru
# and after I detect breaks I put them into a list
# and then based on their position surmised from their index location in palmtrees(firstcaselist)
# I replace the location of the breaks in the list of fallthrus
'''
this is where the index location of the current case is located in the firstcaselist(palmtrees)
then after getting the index number I insert it into roadrunner list which just holds index numbers
from the firstcaselist of where a break resides(lives)
'''
	################################################
	for item in wilecoyote: #goes through list of case sections with breaks
		toad = get_location_of_case("palmtrees",str(item))
		roadrunner.append(toad) #this returns a number the index position
	print("ROADRUNNER list contains numbers of index locations of cases in palmtrees",roadrunner)
#################################################

'''
instead of juggling with both breaks and fallthrus 
I chanced on the idea of prefilling the whole list with fallthrus 
and only add breaks if there are any. Bear in mind that no break (an absence of a beak) means fallthru
and explicit fallthru or fallthrough means a fallthru. But I just wanted to detect breaks.
This fills up a list called british  with just fallthrus 

'''
	# make a new list based on digitalcandy
	for item in range(0,len(digitalcandy)): #using this for length of case sections sequence
		#filling list with fallthrus
		british.append("fallthru")
	british.append("break") #adds one more to list since default is extra case
	
	print("========== british list ======")
	print("british filler list =",british)
	#british[0] = "starter" #this is position 0 filler
	#british[-1] = "break" #last one must be break for default case
	print("========== british list ======")
	print("british list =",british)
	##################################################
	#this is walking thru the british list and replacing fallthru with break where there was a break in a case
	    #the bug is here 
	'''
	I loop through digitalcandy which has the dimensions of the switch case with x,y for each sublist of
	where (line number) a case starts and the next case SECTION starts to designate case section structure.
	if the counter (mycounter) is IN roadrunner (which contains the index numbers that we pretranslated from the case names)
	then the method do_replace is called then the current counternumber is input for the method and break is 
	put into the location of the british list which is used to build the break/fallthru list.
	It's a terribly economic, elegant, simple and beautiful solution  that replaced and overly complicated previous solution
	and it works which is an added bonus.
	
	'''
	mycounter=0
	for item in range(0,len(digitalcandy)):  #adding a case to it default
		if mycounter in roadrunner:
			do_replace(int(item),"break")## do_replace(1, 'break')
			mycounter += 1
		else:
			mycounter += 1
			
	print("============================")
	print("british is ",british) #break and fallthru list
	'''
	position 0 is changed to starter
	position n (last position) MUST be break because it's the default case in the python version 
	
	'''
	british[0] = "starter"
	british[-1] = "break" #makes sure last one is a break absolutely. 
	print("british now =",british)
	
	print("now for british list of fallthus and breaks we have ",british)
	########################################################
	british[0] = "starter"
	british[-1] = "break" #just to be sure 
	print("british=",british)
	
	
	

thursday, Feb 18th, 2021  8:22 am California Time
	
cleaned up some code and made some convenient methods
do_replace_item_in_list()
get_location_of_case()
get_case_name()
get_length_of_firstcase_list()

# the refactoring was to simplify, stremaline, and speed up the code 
# and reduce the code footprint with a new design for detecting breaks 
# and assembling the fallthru function.
# during testing I discovered that breaks were being missed
# likley updating code here tonight since it's my day off I have time to work on this project

//======================================================

Thursday Feb 11th, 2021  2:38 pm California time

With code that looks for a break in each case section in a loop
I need to get the case name. 
The case name for this case section is grabbed in this code inside of case_tail_list_maker(x,y)

for line in switchcasetester.splitlines(): #switch case in JS
       
        #below this line the break is detected
        
        if smartcounter == x:   #x is an input parameter from the list of sets of the first case and next case line number
	    #I know that "case" will be in this line because it comes from digital candy that already determined line numbers with case.
            print("x =",x,"and y=",y)   #which are stored in the list called digitalcandy
            print("this line =",line)
            ####################################
	    # this is use of replace in a string
	    ####################################
            line = line.replace("case","") # remove case
            line = line.replace(":","")    # remove : chop off the end here
            the_section=line #should chop off the end
          
            print("we see for the_section ",the_section)
            print("")
	    #this gives me the case name in the_section
            
#this method gets the index number of the case name in the list
#the list that it is searching through is the list made up of just the first case name in each section which is used for fallthrus
def get_location_of_case(listname,word):
    print("get location of case () called ")
    print("this is searching for ",word)
    answer =eval("" + listname + ".index(" + "'" + word + "'" + ")")
    return answer
	    
            #this takes the case name as input to get the sequence index number within 
	    #the list of first cases
	    output =get_location_of_case("fruits",'orange')  #currently it's listname , first case name
            print("result =",output)                         #to follow human thinking I may change it to casename, listname
	
	
	# then once I have the index location I will put that in as a parameter
	# for replacing the contents of that index number in the trail list
	# which is by default filled with "fallthru"
	# so it would chnage that position with "break"
	
	# replace word in list by index position
	 #############################################
	 # this is use of replace a word in a list .. by index position
	 #############################################
def replace_in_list(x,y,z):  
	z[x]= y   #listname[5] = 'word'
	print(z)  #print(listname) #for testing will remove this line
        
#  new_replace_index(x,y)  uses two variables and 
#  hard code list name and call replace_in_list(x,y,z)
#########################
##  do_replace(x,y)
#########################
def do_replace(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=tail_list  #list name
	replace_in_list(x,y,z)
	

What I did over the past few days is figure out the process and where I would add the new methods
to build the tail_list which is used in the code generator as the last puzzle piece.

The way that it works is the tail_list position 0 is "starter" and is just filler
the length of the list is equal to the number of case sections plus adding one more case called default which makes 
falling thru into default possible. The bug I was having was there was fallthru('starter') for default which is wrong
and the breaks weren't working consistently and weren't in the right places in case sections. I rewrote the logic
for detecting breaks. I reduced five pages of complex code down to five lines.
To reduce calculations I prefill the tail list with "fallthru"
If there is a break change "fallthru" to break
if no break in case section  then do nothing leave it as fallthru
if fallthru in case section then do nothing leave it as fallthru

if "break" in case_section:
	#replace  tail_list index position for this case section to 'break'# the case names are in sequential order from 1
	# and they are referenced by number not name
	# I get the current case name for this case section above from x which is the input parameter: which is 'snoopy'
	# and then this returns the index number of the cases locaiton in the case section series
	output =get_location_of_case("listoffirstcasenames",'snoopy') #example this returns 2
	#this is fed below as input parama which then changes the 'tail_list' index position 2 with 'break'
	do_replace(output, 'break')
else:
	pass
	
	
==============================================================	
February 9th, 2021  3:19 pm California time
There isn't a replace word in index method for lists in Python so I made one. There is already a replace method for strings.
I needed to be able to replace a word in lists on the fly dynamically and ended up with this.
I will likely rename it but it's in development.


This is an important pair of methods to add words on-the-fly to a list.
I'm working on the fallthru,break list which is part of the third tier of the parser preparing
for the tail of the code generator.
This will be implimented with some fuzzy logic that detects if a break is in a case
and fills a list with "true" and if no break then "false"
then with this 'true' and 'false' list
I build the list with "break" and "fallthru" which moves to the next stage in the process.
This was the stage that was buggy due to logic so I simplified the logic.

# this is replacing a word in a list at index location x;  
# this shows the word "break" replacing  position 6 in the list [name] which is hardcoded into the method this method calls
##############################  I still might add the third variable to have the listname here but did it this way for brevity
new_replace_index(6,"break") 
###############################


##  THIS IS TO REPLACE A WORD IN A LIST AND I AM NOT EVEN USING AN EVAL()
#################################
##  replace_in_list(number,word)    replace_in_list(2, 'fallthru')
##################################
# replace word in list by index position
def replace_in_list(x,y,z):  # Note: this requires 3 parameters
	z[x]= y   #listname[5] = 'word'  #this hardcodes a word change in a list directly
	print(z)  #print(listname) #THIS IS OPTIONAL HAVING print(listname) here

#  new_replace_index(x,y)  uses two variables and 
#  hard code list name and call replace_in_list(x,y,z)
#  this makes it possible to replace a word in the list using only two parameters and the third is done automatically
def new_replace_index(x,y):  ###<<=========== I hardcode the list name NOT a string
	z=starbuckslist  #notice no quotes used as in regular ' strings' list name which is hard coded here and referenced with call below to function above
	replace_in_list(x,y,z)   ##<<==== it calls the method above brilliant
	#print(fruits)




Feb 9th, 2021  2 PM California Time
Now I am confident it's all going to work.

I reengineered how break is detected in the cases and fallthrus and missing breaks. I am quite pleased with it now.
I reingineered how the fallthru function is dynamically filled.
On the second pass for both of these sections of the code the second version is cleaner and more elegant and efficient.
I'm throwing in a "do while loop" later tonight for fun. (if there is time after uplaoding the updates for the switch)

While I was testing the code I was shocked to learn that breaks were being missed and fallthrus weren't set up correctly
and weren't being dynamically generated 100% with accuracy. This has all been fixed now and rectified. 
I am connecting the sections together for the breaks and fallthrus and creation of the switch case without bugs.
I am against rushing good code and usually the second design is more refined and beautiful then the first design attempt.
The reworking of the design, aka refeactoring has made a world of difference and the code should run at least five times faster too.
I will add the time difference later.

I had been working with a few sets of pairs of files and I localized it down to two files for simpicity and to reduce complexity.

There is a lot that I want to add but I still need to verify that the multiple switches work
and I will impliment the nested switches after the multiple switches are stable.
===============================================================================================

I will next merge the filter for whether words or numbers are going through the switch.
The macro for case 1 to 10  and case 1 thru 10 now works.


Feb 7th 2021  8:22 PM California Time
Simplified the logic to detect breaks and fallthrus in case sections so it's 100% accurate now.
The intial code was overly complex and 5 pages long. I reduced it to 5 lines of code.
Fixed the fallthru generated construction bugs. This was a three week nightmare bug from hell. I rewrote it from scratch.
None of these fixes and improvements have been uploaded as yet, but will be added soon.


Feb 5th 2021  1 AM California Time
================================================
Current bugs working on switch case bug database 1.0

Solved how to use macro "to" with number cases by doing a prescan of the switchcasecode input first
and then replace "to" with "thru" since the code for using thru already works fine.


january 24th, 2021  8:18pm


when using fallthru and next case is like 'alpine meadows"
right now fallthru only works for one word 
it only sees or looks for the first word and chops off the end like alpin
the bug was I was only looking for the second word (the word just after the first word case) which was position[1] #so this was a design bug I fixed

so I need to fix that. currently it can only use fallthru to a single case word like 'music'
UPDATE: making progress can now use any number of words in a case
still some persistent bugs of fallthru('words in here') failing with bad data
so I'm adding some fuzzy logic to assert that the data is correctly dynamically added

============================
february 4th, 2021 thursday 
Feature
numbers switch works and thru works  using pumpkinfalls and yellowfish
this is where I will test Yale constant  case FINDITNOW: 
need to have filter to call that
code to handle numbers turned into strings
and look for thru macro


in second switch it's chopping off the first letter
of words and messing up the fallthru which
is messed up if more than one word and
even if just one word so bug in there.


in newgoldfish  and firefall_yosemite  fallthru not right


bug in generated python code just before it is executed

elif case in caselist9: # ['default']
		print('six walking duck de fa ul t')
		print("flying geese")
		
		fallthru('starter')   #bug should be break since this is the default case
                                      #will add conditional check to force feed it a "break" into list cranberries (the third main list tail)
			              #this is supposed to be the last list item in cranberries so look at cranberries list with checks
				      #where this last list item is being changed and use trace to pinpoint it 
	else:
		print('six walking duck de fa ul t')
		print("flying geese")
		
		break
		
		        



===============================
===============================
thursday night feb 4th, 2021
This bug fix project is called Aristocats  this is fixing the fallthru('alpine meadows') bug and using more than one word
And at the same time "sometimes" if there is just one word it has double quotes such as fallthru(''word'').
An assertion and some simple fuzzy logic can detect this possibly use count(') and if more than 2 then the bug has been isolated.

new_goldfish.py
firefall_yosemite_falls.py

fallthru('only works with one word')
if it has more than one word it messes up
and chops off from first word and fails and crashes switch


it also does a fallthru("in default case")
it actually says fallthru('starter') which is funny
it should say 
break

it should be break and this is just above
the  else:

the second switch case fails with error message: NOTE: var names will be changed soon to be more descriptive
 doggy =starbuckslist[item] #just added -1   this is like fallthru('cherry')  #was starbucks
IndexError: list index out of range



==================================
in aristocrats experimental I'm working on a  bug fix
for handling one word and many words

I was having a bug with reading a string what was still a list
that I just fixed using a join. It is such a prevalent need I'm making a method to convert a list to a string to save time


Update Feb 5th, 2021  12:34 AM
I'm currently working on the filter for whether a switch is taking in numbers or words in strings.
The main engineering for the switch case works and is stable. I'm just dealing with a small number of bugs right now
but the code works.

Update Feb 4th, 2021 11:25 PM
This now works, it's more flexible as a macro based on how people want to think.
#so as you can see you can use "to"  or "thru" for a span of numbers
Both to and thru are macros that trigger a parser method to loop through a list populated starting with the first number
and the list ends with the last number. Because the cases will be expanded downward the number switch case is actually expanded
from the bottom up (backwards) so that the case lines don't change that are referenced. Again Python really has no clue whatsoever
about the code in the switch case and I use fuzzy logic and a fancy parser to analyze the contents of the switch and fill lists which are then
utilized for the code generator. I didn't want to taint my design so I purposely didn't read any books  or anything online on parsers or code generators.
I wanted it to be purely my design. I previously wrote thousands of lines of dynamic JavaScript so I wasn't phased by the attempt and effort
but I actually chose python over other languages just because it has eval() and exec(). I was pleased with writing the code generator in an hour and then it took three days to get it to actually work. The parser was extremely
difficult and required great tenacity. The amount of fuzzy logic in the parser is mind boggling. 

#====================================================================

switch(exp) {  
		case 1 to 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 4 thru 10:
			print('keep going!')
			print('taught me how to write code')
			fallthru
	
I have been figuring out and fixing the fallthru('') bug that was unable to use more than one word for a case name.
I fixed it. 

Working on stabilility  overall and will next try ten switches in a sequence.
	
I have a nested switch working in pydev and I'll get  at least a triple nested switch working.
The way that the nested switch case actually works is in the "envelope plastic window view" where the C/JavaScript style
switch is in the docstring with a var name of sw the switch code is nested and appears just a second embedded
switch case but the parser will put the nested switch case into a seperate function so in actual python code
it is a call to this function with a return value and that way the code is cleaner. And the way that the goto
will work to jump out of deeply nested loops is it puts the last value before the goto is called into a list
and the loops are inside of a function and return is called and I have a method called falling_goto_catcher(x)
that catches the value that is in the list that was put there before return was called so that it can then
trigger the behavior of the goto (which is really a fallthru) and it works.
	
I am finishing up the switch project to move on to other python additions that I have planned.
The bugs that I am encountering as I reach the finish line are sometimes baffling so I am
making my functions smaller to manage it better.
	
goto label;  it coming up next.
based on C design and behavior. This example is from Yale.https://www.cs.yale.edu/homes/aspnes/pinewiki/C(2f)Statements.html
The switch case is invisible but for debugging purposes it will be possible to see the conversion  in the parser debug stage
to see the switch case output that is representing the inner workings of the clever goto for Python. This is why I have been
hell bent to get the switch case working. I love switch cases but I've also wanted to play with gotos.
	
The way that the goto will work is goto is actually a fallthru that can go up or down within a function
and the label giveUp is actually " if case == giveUp:"  but it's all in the background just a switch case. This was my second motivation
for making switch. So it works as a prescan level above a switch case and the function will exist within a special switch case. 
It's really a switch  case veil in disguise. Granted the label along the left margine is C-ish in appearance and goto is not a 
python reserved word. In PyDev it won't let me use a function called goto() which I found comical it will not run; so I named it 
something else.
	
   1     for(i = 0; i < n; i++) {
   2         for(j = 0; j < n; j++) {
   3             doSomethingTimeConsumingWith(i, j);
   4             if(checkWatch() == OUT_OF_TIME) {
   5                 goto giveUp;   <-------------- this is what it will look like in python
   6             }
   7         }
   8     }
   9 giveUp:  <------------------------------------ this label with the colon after it will look like this in python
  10     puts("done");
	

======================================
Update 10:25AM PST Febraury 1st, 2021
I haven't had a day off in a while and didn't have access to electricity which slowed me down.
Still in total nirvana that I can reset the switch module for each switch.
I am still doing a lot of testing and note taking of bug behavior.
I will also be diagramming the design structure of the structure so I can see it visually in terms of the architecture.
	
Added ability for a fallthru to go to case with multiple words in the name such as  case "alpine meadows": and now n number of words
Working on bug triggered after first switch case.
I only just recently added the ability for cases to have more than one word such as .. case "Starship launch next week":
Still need to add converting each string to lowercase()
Multiple switch cases now works but I have a few bugs that I'm figuring out to circumvent the bugs.

Happy that multiple switch cases works.

Currently merging different parts of working aspects of differnet files (while keeping backups) 
and then using diff in BBEdit to make sure I'm changing the right parts.

Everything works just debugging now. I will also work on adding a C style constant word like
case BIG_WORDS_LIKE_THIS:  which will reuse my number code which converts it to strings.
### this one is on hold for now because it looks strange.	
case CONSTANTWORD: 
	
I will put up the gold master code (and take down this experimental code) after I finish paring it down and adding more documentation for the
behavior of each function and a description of the super structure. 


Update 7:21pm PST  January 24th, 2021
It works. I have two switches working. I have a few fixable bugs but it works. I don't believe it.
Reload came thru and works. Saving me a ton of coding. So I can reload the module before each switch case.
Thrilling. Had threes switches working in a sequence ... and then noticed a few bugs.

Update 7:07 Jan 24th starting to work
used this reload code that worked
that I will put into a function:
	
import importlib
import my_great_module
importlib.reload(my_great_module)

Just one small fallthru bug I will fix, so I have two switches working in a sequence that are completley different working in the
same function!  Starting to believe it's going to finally work as envisioned.


###############################
## update January  24th, 2021  5:58pm PST
I have been debugging the design change (refactoring) so that more than one switch case can be used in a function
and infinite switch cases can be used in a file. Making progress. I initially was going to reload the switch module (with no luck) but
I am making good progress resetting the lists. I made good bug pinpoints the past two days and can see the light
at the end of the tunnel. It turned out a bit more tricky then I imagined it would be. Testing with two switches
currently that are stacked and the first works and the second switch is outputting python code now though much of the 
parser data and output is wrong but getting more correct gradually.

############################################################################################################
#      January 12th 2021 1:03pm PST Update     Project TRON  JavaScript/C Hybrid Switch Case for Python    #
############################################################################################################
update 3:30 pm January 12th writing style guide for switch case now with examples
this will be in an html file called switch_case_style_guide.html

Progress on documentation and rules for this switch case implimentation for Python.
<html>
  <body bgcolor=white>
  <code>
from switch_mod import *    <---- required to access the switch case module parser and generator and executing the code

input('9') <----- required  #this will put the value into exp for the switch() method
                  this will be just above each switch case
                  
# 1 tab  --> switch
# 2 tabs --> case
# 3 tabs --> body

sw ='''
#debugon   <--- required comment to trigger flag to print the output python code dynamically generated to debug

	switch(exp) {  <--- required brace  and exp for var inside of switch  #amended: Feb 4, 2021 { not necessary (purely optional)
		case 'snoopy':  <---- required single quotes
		case 'linus':
			print(\"where's the dog house!\")
			print("first prize")
			break

		case 'Linus':  
		case 'Woodstock':
			print(\"tennis wannabees!\")
			print("what is the score again")
			break
			
		case 'tomato':  
		case 'table':
			print("make some ketchup")
			print("== you gotta work===")
			break  <-- break is standard 

		case 'tahoe':
		case 'donner':
			print("will I live there some day\")
			        <--- no break means implicit fallthru just like in JavaScript and C
			
		case 'fish':
		case 'marsbar':
			print('third  section')
			print('working on this')
			fallthru  <-- shorthand way of writing explicit fallthrough
			
		case 'panera':
		case 'peanuts':
			print('four try again')
		        fallthrough  <-- explicitly can be spelled this way like in Swift
		    
		case 'bestwestern':
		case 'travelcenter':
			print('nice place to stay')
			break
			

		case 'alpine meadows': <-- words in a quote for a case can be up to 10 so far
		case 'squaw':
			print('ski fast in the powder')
			break 
			#fallthru will work going into default from case just above default
			#also no break here does the same expected behavior
			 
		default:  <----- required and *must* be at the bottom
			print('six walking duck de fa ul t')
			print("no matches")
			break <----- this break is optional and is added if missing automatically
			
}     <--- required  #amended  Feb 4, 2021 not necessary (completely optional) It's for looks, it's actually ignored
'''   <---  required end of long multiline string called sw
	endswitch(sw)  <-- required #this calls the parser and codegenerator
	
	
	
	
This implimentation converts a JavaScript switch case into Python if elif else implimentation. 
Regular string switch case works with JavaScript/C appearance and running behavior  i.e. case "alpine meadows":
Regular number switch case works  i.e.   case 2:
macro "thru":   case 1 thru 10:  works with number switch  this generates case 1, case 2, ... case 10:
Based on this code I can make any macro work now.
Currently adding documentation and deep description and design info of project for switch case.
0. Major difference from what you might expect for the implimentation is that this is implimented
0. continued: by putting the JavaScript/Python hybrid blend into a docstring with a var name sw
0. continued: and "after" the docstring is endswitch(sw) which calls def endswitch() 
0. continued: and parses the string, dynamically generates the python if elif code, and executes it.
0. continued: Note: this impimentation uses eval() and exec()
0. continued: input for exp for switch(exp) occurs thru a function above the switch case docstring
0. continued: output of the "result" returned value from the switch is in a list called varholder[1] and there can be n returned outputs if desired
0. continued: To be clear the input var for the switch case body is above and outside the switch case itself which is in a docstring
0. continued: The output value(result) from the switch case is after and below the switch case doc string in a list of n size; default is one result item in varholder[1]
0. continued: I will include examples here over the next few days
0. continued: I still need to add the sniffer/filter to detect if switch(exp) and cases are numbers.
0. continued: The code in the docstring is a hybrid blend of JavaScript and Python and C behavior and syntatic style
0. continued: which uses a brace { after switch and ends with } brace at the bottom (though they are ignored).
0. continued: sticking with Python (a little) tabs are required. 1 tab before switch, 2 tabs before case, 3 tabs for case body
0. continued: tabs must be equal to 4 spaces. The tabs used for the input are used for the output Python code.
0. continued: the code within the body of a case still(for now) needs to be Python 3 code.
	
1. The idea is to have a switch case (with JavaScript behavior) that looks just like JavaScript and C switch except for all of the braces.
1.a. Though I am working on allowing using braces with Python and macro that replaces Javascript style braces with tabs so writing python won't require insane indentation.
2. Rule 1 the tab (4 spaces) that are commonly used in Python are "required" for this switch case to work flawlessly.
3. Rule 2  in a case to fallthru either you leave it blank (empty) at bottom of a case before next case or default
3. continued:  or you can use: fallthru, fallthrough  for the same effect. (lowercase)
4. For version 1 the cases in strings are converted to lowercase. I will change this in the next version to be more flexible.
5. What is this? It is a preprocessor and parser and codegenerator which parses the input JavaScript/Python code blend
5. continued:  dynamically generates the python code equivalent of creating the "expected" JavaScript/C switch behavior
6. about to impliement(will work on right now) by adding #debugon just above switch word you can read the output of generated python code to assist in debugging
7. I purposely did not look at anyone else's implimentation of a switch case in python to prevent clouding my design.
8. I did glance at the rejected Python proposals for Python 3 and laughed at the new confusing match() proposal.



This parses and generates python code and runs!! Demo of thru macro
clever('16')  #input to switch case feeding exp for switch()

sw = '''  
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 4 thru 10:
			print('keep going!')
			print('taught me how to write code')
			break
			
		case 11:  
		case 12:
			print('make some ketchup')
			print('== you gotta work===')
			break

			

		case 13:
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
		case 14 thru 20:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			fallthru
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			
}
'''
endswitch(sw)

#the macro for thru is called first and generates this version of the string before getting analyzed
#for the parser

switch(exp) {  
		case 1:
		case 2:
		case 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 4:
		case 5:
		case 6:
		case 7:
		case 8:
		case 9:
		case 10:
			print('keep going!')
			print('taught me how to write code')
			break
			
		case 11:  
		case 12:
			print('make some ketchup')
			print('== you gotta work===')
			break

			

		case 13:
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
		case 14:
		case 15:
		case 16:
		case 17:
		case 18:
		case 19:
		case 20:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			fallthru
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			
}

###this is the dynamically generated python code

exp = varholder[0]

caselist1 = ['1', '2', '3']
caselist2 = ['4', '5', '6', '7', '8', '9', '10']
caselist3 = ['11', '12']
caselist4 = ['13']
caselist5 = ['14', '15', '16', '17', '18', '19', '20']
caselist6 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['1', '2', '3']
		print("where's the dog house!")
		print('first prize')
		print('you block head Charlie Brown')
		break

	elif case in caselist2: # ['4', '5', '6', '7', '8', '9', '10']
		print('keep going!')
		print('taught me how to write code')
		
		break

	elif case in caselist3: # ['11', '12']
		print('make some ketchup')
		print('== you gotta work===')

		
		break

	elif case in caselist4: # ['13']
		print('ski fast in the powder')
		print('sweet powder snow, lovely snow')
		
		break

	elif case in caselist5: # ['14', '15', '16', '17', '18', '19', '20']
		print('Heavenly valley')
		print('big snow flakes there and moggles')
		
		fallthru('default')

	elif case in caselist6: # ['default']
		print('six walking duck de fa ul t')
		print('flying geese')
		
		break

	else:
		print('six walking duck de fa ul t')
		print('flying geese')
		
		break


#from goldfish import switchcasetester

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



   #READ STRING FROM FILE
def read_string_from_file():
	print("====== read string from file called ======")
	print("=== READ_FILE_PUT_INTO_STRING====")
	f = open("sw_test.txt", "r")
	boomerang = f.read()
	print("=====output of string here=======")
	print(boomerang)
	return boomerang






#######
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

varholder=[]
varholder.append("zilch") #if nothing changes it's default

var2=[]
var2.append("zilch")



#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
	print("====clever called for input to switch case exp")
	#then I know it's not using words but numbers
	#and to convert the numbers to strings in a special pass
	#of the input switch case since strings work
	
	x= i.isnumeric()
	if x == True:
	    print("true it's a number")
	else: #False
	    print("false not a number")
	    
	varholder[0]= i
	#this works and it fills a list with input from an argument
	print(varholder[0]) #to actually see proof

# this is a prefix parser to treat the switch as strings with numbers
#this is only called if numbers after cases not words
def do_pass_to_add_strings_to_numbers(): #in cases
    print("do pass to add strings around each case number")
# go thru each line split.switchcasetester
#each line with a case in it and add ' before and ' after number
#  so grab theline[1] since [0] is case
#and put it theline[1] into a var
#new_code = "'" +this_case_number + "'" + ":" #obviously


#if "thru" in a line
#case is [0] first number [1] thru is [2]  second number [3]
# case 1 thru 3:

def check_if_cases_are_numbers():
	pass
    #go through line get smart[1]
    #if smart[1] == int:

##########################################################
def is_number(inputString):
	return any(char.isdigit() for char in inputString)

mouse = '''switch(exp) {  
		case 3 thru 7:
			print("where's the dog house!")
			print("first prize")
			print("you block head Charlie Brown")
			break
			'''
########################################
#this builds the cases one per line replacing  case m thru n
newlist =[]
count =''
def look_for_thru_macro():
	print("=======look_for_thru_macro() called =======")
	print("=======look_for_thru_macro() called =======")
	print("=======look_for_thru_macro() called =======")
	mycounter = 0
	for line in mouse.splitlines():
		beta = mycounter-1
		if  "thru" in line:  #only used with numbers
			print("yes  thru in this line")
			line = line[:-1]  #this should chop off the colon(:) on the end
			smart=line.split() #separates case from casename
			print("this should be case", smart[0])
			print("first number ",int(smart[1]))  #first number
			print("this should be --thru--",smart[2])
			print("last number", smart[3])  #last number 
			print("will then write perhaps from list yes")
			#newlist.append(int(smart[1]))
			counter = smart[1]
			#this is filling up the newlist
			for counter in range(int(smart[1]),int(smart[3]) + 1):
				
				newlist.append(counter)
				counter += 1
			print('newlist sees contents',newlist)
			
			#newlist.append(counter)
			#counter += 1
			#newlist.append(counter)

			ajax =''
			print("length of list =",len(newlist))
			print("this is GENERATED case code from macro") 
			#this is reading out the contents of the cases one on each line
			for item in newlist:
				ajax += "\t\tcase " + "'" + str(item) + "'" + ":" + "\n"
			print(ajax)
		
print("=====see if this puppy works for my thru macro =========/////////")




		
		
		
		
		
			#checks if case name is a number returns True or False
			#smart[0] is case
			#smart[1] is first number 
			#smart[2] should be "thru"
			#smart[3] is second number and :
			#need to change whole line and swap it out
			#make a list starting  or range(n,m)
			
    
    
    
    
    
    
smart =''
beta =''
opal=''
import re
foolish =''
newline=''
####### case_numbers_to_strings changes number cases to strings with the number inside
#######  I still need to sniff and detect if the cases are numbers before calling this 
############################################################################
#################### case_numbers_to_strings ###############################
############################################################################
def case_numbers_to_strings():
	global switchcasetester
	print("=========testing case_numbers_to_strings===january 5th 2020====")
	#go thru the entire string
	#and change each case number  into a string for preparing for python handling
	mycounter = 0
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
			print(" ")
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			print(cat)
			
			cool = smart[1][:-1]  #chops off : from end
			doghouse = "'" + cool + "'"
			cool = ''
			cool = doghouse 
			cool = "case " + cool + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			print("\t\t" + newline)
			print("next I will use replace to each case line")
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal
			#will use a replace here to the switchcasetester string
			mycounter += 1
		else:
			mycounter += 1
			continue
	print(switchcasetester)

    
#use loop
#becomes
#case '1':
#case '2':
#case '3':





#testing accessing switchcase from file goldfish
def mountain2(c):
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
			smart=line.split() #separates case from casename
			#print(smart[1])
			birdsong.append(smart[1]) #this adds casenameto list birdson
			print("testing to see if this is where I'm making a mistake with the case names")
			print(birdsong) # I might be only adding the first word that might be the bug january 3rd 2021
			music.append(mycounter) #list of number for case line
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
	return default_location
	

#########=============== get last break in string ==================
listofbreaks=[]
def get_last_break_in_string():
	print("==============find last break in string============")
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
def convert_default_case(): #I got this working November 26th, 2020
	mytrace('convert_default_case')
	#print("===========convert default case called ===========")
	############################################################
	get_default= get_default_location()
	last_break=get_last_break_in_string()
	
	
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

def big_gears_filling_list_with_case_bodies():
	mytrace('big_gears_filling_list_with_case_bodies')
	mytrace('snowtime') #it calls snowtime() below
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
		
		item = item.strip()

		
		answer =item.count('\\t')
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
				
			if words == 4:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3] 
			
			if words == 5:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] 
				
			if words == 6:  #if 2 words for case 
				wilderness = firstline[1] + ' ' + firstline[2]  + ' ' + firstline[3]  + ' ' + firstline[4] + ' ' + firstline[5]
				
			print(" wilderness has in it", wilderness)
			print("=====firstline[1] ====== line 2009 =======")
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
	#this is the final input code of switchcasetester
	print("================== finalized input of switch case code =======")
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
	#print("oh my god starter_sequence called will it work???")
	look_for_thru_macro()  #testing stage with string called mouse up above
	case_numbers_to_strings() #testing on january 5th
	
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

daisy=''
def parser(a):
	#felix()  #testing with switchcasetester string
	#mtv()
	mountain2(a)
	starter_sequence()


def endswitch(y):
	parser(y)


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
