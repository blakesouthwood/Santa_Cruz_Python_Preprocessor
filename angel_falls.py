thursday night 10ish pm May 13th, 2021

Working on the flow of control and updating the filter for if numbers in cases used
but for the time being here is the code that is testing word switch cases and 
number switches (already unfurlled) which I used for testing purposes to solve the bug
that was preventing running numbers and word switches after each other. Previously
word switches ran fine in any number but if I added a number switch it crashed
and conversely if I had all number switches and then tailed with a word switch it crashed.
So I decided to upload the working code at this point that I'm working on and modifying
the flow_valve code which detects if numbers in cases in a switch and does the
expansion of the "to" and "thru" macros which will be implimented (they work) in the next 
few days and I'm taking out the unused dead code and cleaning up the code and taking
out the ten trillion print statements. I used visual Studio code to debug the last few bugs
and College Ruled papers and lots of print statements to determine what was different.

The two files that are beta are mrcoffee_mocha.py which is the switch module
and sip_coffee.py which is the input switches file. I will take out 95% of the parser_2 and code_gen_2 this weekend which
is now not being used. 

I just have to add the preprocessor macros code (already works) and then it will be complete.
This solution eliminated 4,000 lines of code using tricky coding and smart reuse that I didn't originally envision.
Deepest code I've ever written. What a thrill. Total disbelief it duplicates C's switch case behavior and look and feel .

May 13th, 2021 The code works. I am so happy. I investigated the bug and solved it.
I can run 1 trillion switches with numbers or words intermixed. Bad ass.


May 12th, 2021  8:47 am
ONE BUG AWAY FROM ViCTory.

I can run a bunch of word switches it runs.
I can run a bunch of number switches it runs.
but when I mix them together going from word switches to a number switch it crashes.
I have the numbers switches going through the string word paraser and codegen now to cut the code size in half
and to streamline the flow.
One last bug I will conquor tonight.







MAY 10TH, 2021  7:31 pm
	
Currently working on getting number switches like case 1 thru 10:  to work.
Up till now only one numbers switched work. Just got two number switches in a sequence working,
but with a few bugs but closer than I've gotten before.
Also testing a word switch followed by a numbers switch.



May 3rd, 2021 Monday 9:21 pm 
Just tested 10 unique different switch cases in a sequence and they worked.
All switch cases were in a row and each one ran in order so all ten were done
immediately. I didn't start and stop for each one. I just ran them all at once
to test the stability and durability of the switch module and it worked.

Again this new version doesn't use reload module anymore.

May 3rd, 2021 Monday 7:56pm California time.
Note: it runs in BBEDit but just tried it in Sublime and it doesn't work on Mac.
listname.clear() doesn't work in Sublime for some lame assed reason.
I made a new method to empty a list in Python that works in Sublime. I'll update
tomorrow so the switch works in Sublime Text 3. I wonder why JavaScript is
a million times more stable than Python.

def empty_mylist(name):
    del name[:]
	
testlist =["one","two","three"]
empty_mylist(testlist)	

		
After the nirvana of seeing the beautiful generated python I noticed ... a few bugs.
I solved them today. I just ran three switches (without reloading the switch module)
and they worked perfectly and they correctly included the default case which was missing previously
and the first case was being skipped. 
The euphoria and rush I feel at this moment is indescribable. It's like a successful launch of a rocket.
The frustraton and agony of the bugs was arguous. I persevered though.
What a victory. I had to use Visual Studio Code to step through the code to see what it was doing and see what was what.
I will upload it in a few minutes. I feel like I can walk on water right now and fly through the clouds. It actually works.

I will test and integrate the numbers version of switch case. This will take a few days. I made the valve switch
to direct to the word parser or the numbers parser but haven't modified the numbers code to work with the new design yet.
looks like this: it already works but I have to integrate it into the refactored design. Words now works.
	
I still need to code some fuzzy logic to empty caselists used which hold the casenames so just for now it works
with just 6 cases but it can be modified to work with millions. I will have a default handling up to 1,000 for now. 
	
sw = '''
	switch(exp) {  
		case 1 thru 5:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 6 to 10:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			break
			
		 
		case 11 to 15:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru

			

		case 16 to 20:
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			fallthrough
			
			
		case 26:
			print('oh yeah')
			print('tahoe here I come')
			break
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
           		break
}
'''





May 2nd, 2021 Sunday 10pm PST California.
I did it! I ran two switch cases in sequence without using reload of the module.
That was my original goal. Pure nirvana. No reload necessary.
Will experiment with my flow valve to handle number cases and integrate it.
I didn't think it was possible.  In total shock right now.



April 30th, 2021 7:22am
I timed how long it takes to reload the switch module.
The time to do reload the switch module was in 0.0008 seconds.

def sw_reset():
	importlib.reload(switchmodtrial7)
	
start_clock = time.perf_counter()
sw_reset()
stop_clock = time.perf_counter()
print(f"time to do reload of module was  in {stop_clock - start_clock:0.4f} seconds")



April 29th, 2021 10:51PM
Just tested the numbers (not working) I will fix the numbers tomorrow. The way it works
is there are separate parsers for words and numbers and I didn't expect words to be working today.
I will fix it tomorrow or this weekend so people can play with it.
Found working numbers switch case.  switch_module3.py and switchcasetester_numbers.py

I will upload a file with numbers working for the impatient people.

Switch case with the identical style from C and JavaScript works in Python now!!!
A user can use implicit fallthrus with no break or explicit fallthrus  using either fallthru or fallthrough.

I just tested three unique switch cases in a row and they worked for words.
Granted it reloads the switch module for this prototype. Still working on making it work without reloading the module
but it is still nonetheless cool. Numbers works too with macros  case 1 thru 10:     and   case 12 to 15:
Taking out the print statements now.... I need to clean up the code but I will upload it.
I'll end up taking a lot of the code. 

Was working on different versions so I need to integrate them together but still hell of a rush seeing it work.
I added a more advanced break and fallthru manager which I don't think is in this version but I'll add it soon (it works).

Beta files are switchmodtrial7.py and swtest.py

Very cool. 



april 29th, 2021  at 1:34 pm PST
Finally able to truly flush the lists clean and trying multiple switches.
Will upload code once it works. What a bear doing something trivial.

#without reinitializing the particular lists this completely emptied them.
I will convert this into a method.

for item in range(0,len(palmtrees)):
    palmtrees.pop()
#followed by 
if len(palmtrees) > 0:
    palmtrees.pop()
		
Figured out how to add Ruby Chaining Functions/methods in Python which will make coding Python faster and more elegant.
And don't have to use classes or self to make it work. So it will work methods and functions.

Adding option to do switch case with braces with no indentation/or whatever you want for indentation and then
it will be reformated to the correct tab insertion to conform with the current working switch case that has tab indentation
requirements.

Looked at the new Python spec on switch being added to Python and felt relieved it's a mess and confusing. Mine conforms
to the look and feel and behavior of C and JavaScript switch cases and now Python forced indentation will be optional.

#=============================================


April 18th,2021 9:37 pm California time
Nearly there so the switch resets for each occurance of a switch to avoid using a reload(module).
Discovered if I have a function call in the switch  in a case to another function it doesn't work
but I know how to make it work since it's within a case it's called after the switch is completed
so it's trivial though nonetheless annoying but still doable. A function within a switch case section
for generating it just as text isn't called and only when the Python output is called does the 
function get called which means it's within an elif  just as the fallthru is in
the generated python code and is actually a function call so it means
that I will have the function there but it's triggered after the switch 
and so it will leave from a break in the case section and do what I refer to
as a falling star that is triggered if the particular case has a function in it
and then the "feet" of the switch calls the function triggered inside the function.
And the function inside of a case section must reside  in the same file
as the switchcase.  So it seems as if it's calling it from within the C style
switch but it's really called in the Python simulated switch case code. Of course
I will have to thoroughly test it to ensure it works flawlessly.

I honestly didn't anticipate running multiple switch cases would be an issue until I tested it
and it totally crashed. 

My flow_valve works forking for mode1 if string word cases and mode2 if a number case like case 3:
Right now I have combined the two unique parsers together though still separate. Macros work in numbers
for case 1 thru 10:   and case 30 to 40: (Tricky but it works)
Right now I have written methods to reset lists actually empty them and that works.
Now working on a few bugs to do multiple switch cases in sequences. Running one switch works.
It's when I have a second switch that it crashes and I isolated the bug so almost there.

The bug is it's looking in a list for a case name to get the number
and the previous switch case info is still there so it was appending the second switch numbers/words
to the list in question. Apparently this has occurred in several of the lists. Wittling it down.
Then I discovered that the breaks and fallthrus were suddenly wrong and the way that the code gen works
is it is split into three tiers and so it's just the third list that is wrong and so I will compare the
codegen from a recent file to see the diff and what changed. 

April 7th, 2021 5:45 pm California time
Debugging.

Found number bug for case number with fallthru in switch case using numbers.
The fallthru currenlty points to the case after the the closest one. So I need to
evidently test fallthrus with the numbers switch case version more thoroughly.

My brother suggested I test the switch case to make sure it works inside of an infinite loop
which is commonly done in C and C++. I will give it a go. Nice challenge.
To impliment the switch inside of the infinite loop they will both be in the parser strings:
	
	

Currently the code runs fine once for one switch but if I have two switches the first works
and the second one crashes. I have been clearing out the lists and vars and narrowing down
the possiblities of where the bug is as I eliminate the print statements peppered throughout the code.

I have started using Visual Studio Code's debugger to step thru the code.

My merged parser codegen works with words and with numbers but only for one switch curently.
If I run two separate switch cases in a sequence it crashes.

I can execute a switch using numbers by itself and it works.
I can execute a switch using words by itself and it works.
But if I do more than one switch in a sequence it crashes.
I am working on resetting the code's initial state to prevent
the overflow of values which is messing it up currently.


April 4th, 2021 10pm California Time PST
My code worked. I am in total shock. On my fifth attempt at merging the code to avoid name collissions
and going through everything carefully I tried a word switch case scenario and then a number case scenario
and they both worked. Wow.



April 2nd 2021 Friday
Flow valve works and added
And refactored to simplify the complexity


April 1st, 2021 7:46 pm California Time
The fork valve is called before the parser and chooses which of the two parsers to execute
based on if the switch case string contains numbers or words.
What the code below does is determine what type of switch case it is numbers or strings/words
this is to work in the same way as switch case defined in ANSI C. 

Fork Valve to determine whether to do switch case with words/chars or numbers
This utilizes the input var sw for the switch case string that will be parsed
which is triggered inside of the endswitch(sw) function.
The result of this number detector in the first case is utilized in a simple
if else to call mode_1() parser for strings or mode_2() parser for numbers.

These functions determine with a prescan of the switch case string whether it's going to use words or numbers
and it produces an output of True if numbers == True determined by looking in the first case in the switch case input string
and if the output is False as in if numbers == False then it chooses the parser for strings words.


# April 1, 2021 6:39 pm 
# the test is if numbers == True then do numbers switch case
# and then    if numbers == False then do words switch case
# this is done before the parser runs thru the switch string and determines
# which switch-case mode to parse numbers or words
# this grabs the var passed as a parameter sw so this is going to be called
# in endswitch which receives the paramater sw as an argument
# this doesn't call the switch case, it scans thru the input string in a loop
# and analyzes the first line with case in it 
# this is the input for the flow valve which is based on football[0]
# which has an if else. if number True in first case in switch then do numbers swith
# if not number False then do switch for words
#it returns the line number of first case in coffee[0]
#########################################
##  grab_first_case()
#########################################


coffee =[]
def grab_first_case_of_switch_string(): 
	print("== $$$$$ == grab_first_case_name_or_number() called")
	global sw
	mycounter = 0
	#this takes in sw to test for finding out if numbers like case 2: or words case "apple"
	for line in sw.splitlines():
		if "case" in line:
			print("the line number with first instance of case is", str(mycounter))
			#this gets the line number of first case and puts it into coffee[0]
			coffee.append(mycounter)
			break  #here after getting the first instance of a case we leave the loop
		else:
			mycounter += 1
			continue

football=[]
football.append("nada")# 0
football.append("sway")# 1

def remove_tabs_from_string(y):
	y=y.replace("\t","")
	return y

def grab_first_case_line_in_switch_case_string():
	getline= eval("sw.splitlines()[" + str(coffee[0]) + "]")
	return getline

def check_if_number_in_string(x):
	 theresult = any(char.isdigit() for char in x)  #this line from stackoverflow
	 return theresult

def flow_fork_input():
    getline   = grab_first_case_of_switch_string()
    toocool   = grab_first_case_line_in_switch_case_string() 
    toocool   = remove_tabs_from_string(toocool)
    print(toocool)
    getresult = check_if_number_in_string(toocool)#looks in case line
    football[0] = getresult
    football[1] = toocool
    print("output football[0]=",football[0])
    if football[0] == True:
    	print(" === using numbers === ")
    	print("proof  football[1]=",football[1])
    else:
    	print(" === using words === ")
    	print("proof  football[1]=",football[1])

	





flow_fork_input()



March 31st, 2021
Uploading working.switch.case.in.python tonight for sure.

undaunted. wow. flow valve works. greatness awaits.... (this means using switches with words and then with numbers works.
Will test using multiple switches in a row next. Clearing out vars and lists works too.
							
it's really going to work. This is mind blowing. This shouldn't work but it does.
I feel like I have opened the genie's bottle. The possibilities are endless.
I did discover a bug with a fix that will generate an error message if different case sections
have duplicate case names. 



March 30th 9am 2021
Oh MY God it's going to work. PURE NIRVANA !!!!
all successful tests this morning. I added a number detector to input function clever(will be renamed)
and then in endswitch() function I have my if else flow valve using valve[0] with True or False to determine
which parser to run mode_1 or mode_2.   Simple is always better. So obvious.
Everything going in one file. Just tested again with separate files to make sure each of the two files works and they work perfectly.
So pleased. Will upload tonight. What a f'n rush. 




Having import issues whereby two imported files
Cant see or talk to each other so putting two files into one
So everything is accessible without debate.
Python isnt as smart ( in its design) as C in its design.
#include in C just works.
Now by having just one imported file
I will have complete control.



Sunday March 28th 2021 9:13 pm
Redesign nearly complete
Switch with words works
Switch with numbers works
Fixing flow valve to prevent function name collisions.
Likely working in the morning




Thursday March 26th 2021 

9:12 pm
I think it will be working tomorrow.
I have switch words working in one file 
and switch numbers 
Working in another file with Macros.
Combining them into one file was a bad idea.
They will run separately.
Implimenting fix tomorrow morning.
Adding flow valve and fuzzy logic.

This has taken longer to impliment
because I wanted to duplicate the
C language style switch appearance and
behavior described in detail by
Yale University. I had no idea what I was
up against. Along the way I decided to take
the liberty to add some new features. 
Further, one of my aims was adding macros.

8:20 am 

Adding capacity initially
To handle 10,000 cases.
And more can be added.

Fixed bug for comparing switch input string to case 
Making both lowercase with comparing names in cases
such as “Russia” “India” “Canada”

Input can be lowercase or uppercase or
Various combinations with a capital letter to stsrt with
But in the process at point if seitch input
Reduced to lowercase and all case names
For comaring are briefly transfirmed to
Lowercase for strcmp.

case == string.lower()
Otherwise if a word in a case name has
A capital letter it wont match.


Modified design to be completely modular to be 
able to add new features more easily
over time. It has 2 modes currently 
And adding more modes including C constant words not in strings
And nested switches. 

Tuesday March 23rd 2021
7 pm California time

Refined architectural design
So the main switch case process mgr
is in one file with faucet_valve
and pretest to determine if cases 
are words or numbers C style.

I settled on 2 modules to reduce complexity and
simplify debugging. Nearing 10,000 lines of code.

And the main file orchestrates
the two parsers. 

The second module is customized for
dealing with case numbers and the macros to 
and thru and expanding the macros and converting 
the numbers to strings. 

The faucet_valve is a fork for
directing to the words parser and codegen
through main list mode_1  words or mode_2 numbers
def mode_1()
if numbers == False.
mode_2() is triggered by 
if numbers == True: # to do numbers.
Which is directed to the second imported 
module with a modified parser and preparser for numbers.

Reset of vars and list occurs after 
Either codegen is completed.

I will commense testing multiple switch cases 
now.

I need to test a nested switch now that will
convert  to residing in a function 
in actual python code to work.
 
 



Monday, March 22, 2021
6pm California time

The initial setting for the number of case sections is 100 but
the programmer can add as many as they would like to the code. 
Unfortunately the python language won't allow generating lists on-the-fly programmatically.
I will include a function to generate (( caselist100 =[] ) dynamically with a loop and they can be 
copied and pasted into the code rather than doing it manually.
				      
Will put up code for switch case 1.0 in a little while tonight.
				       
				  



Sunday March 21, 2021 
8:16 pm California time

Launching version 1.0 switch case 
For Python 3 Monday afternoon.
Javascipt/C style switch case
With their expected switch behavior.
 
Will handle strings and numbers.
It’s a working version.

Still testing multiple switches
Should work using automatic reset()
that clears vars and lists.
Doesn’t use reload module anymore.


Saturday, march 20th, 2021
Isolated bug.
Will fix Monday and Tuesday.

thursday, March 18th, 2021 8:52 pm California time
Solved bug
reengineered flow of control and connected the dots to make it work.
Will upload tonight or tomorrow. The solution was obvious.



thursday, March 18th, 2021  6:32 pm California time PST
Strings, words already work. I had trouble with the faucet_valve.
I made a bunch of methods for manipulating lists faster and more easily.

Absolute disbelief. Numbers working (starting to). I almost fell out of my chair.
I thought NO WAYYYYYY.
Everything I'm working on is preparser so it's not that tough.
I put the module into the regular switch module at the top and leaped ahead in progress.
It's like seeing the light at the end of the tunnel and like the Wright Brothers
first achieving first powered and sustained flight twenty feet off the ground.
What a feeling. It's like driving on a pot holed bumpy road and the getting onto the freeway
280 and driving 100 mph. What a rush.

The point of the faucet_value is so that the switch case can either do words or numbers on the fly.
The key is that it does numbers as strings but it has to convert them first.

##########################################
#             faucet_valve()  #this governs whether to convert numbers to strings, otherwise if strings(it falls thru)
##########################################
def faucet_valve():
	print("=====faucet VALVE=======")
	print("=====faucet VALVE=======")
	print("=====faucet VALVE=======")
	mytrace('faucet_valve()')
	icetea =finbar()  #method finbar() determines if case has a number like case 4:
	print("icetea =",icetea) #True if numbers
	#decided to just return True or False for now
	valve.append(icetea) #valve[0] = icetea
	firstcase = valve[0]  #True if number otherwise a string so False
	print("contents of valve[0]",valve[0])
	print(valve[0])
	print("firstcase =",firstcase)
	if firstcase == True: 
		print("here means firstcase == True meaning a NUMBER:")
		convert_case_numbers_to_strings()
	else:
		print('firstcase == False  meaning strings words')
		pass #meaning to the strings words as normal

	

Made progress on flushing the lists clean and vars so that multiple switches can be used
without reloading. Faster too. 

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
	print("clear_out_list() called")
	nicejob = i
	nicejob = nicejob.lstrip()
	nicejob = nicejob.rstrip()
	sweet = eval(i) #fox
	print(sweet) #['apps','balls','craps']
	del sweet[:] # will this work
	print(sweet) #should be []

fox = ['apps','jacks','popcorn','mtv'] #so an outside free floating list not in a list


input:
	sw = '''
	switch(exp) {  
		case 1 thru 5:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case 6 to 8:
			print('keep going!')
			print('taught me how to write code')
			fallthru
			
		case 9:  
		case 10:
			print('make some ketchup')
			print('== you gotta work===')
			break;

			

		case 11 to 15:
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			
			
		case 16 thru 20:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			
			
}
'''
endswitch(sw)



output before hitting a wall of another bug
	switch(exp) {  
		case '1':
		case '2':
		case '3':
		case '4':
		case '5':
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			break

		case '6':
		case '7':
		case '8':
			print('keep going!')
			print('taught me how thru write code')
			fallthru
			
		case '9':
		case '10':
			print('make some ketchup')
			print('== you gotta work===')
			break;

			

		case '11':
		case '12':
		case '13':
		case '14':
		case '15':
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			
			
		case '16':
		case '17':
		case '18':
		case '19':
		case '20':
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		case 'default':
			print('six walking duck de fa ul t')
			print('flying geese')
			
			
			break 			
						
}
	
	

Wed March 17th, 2021  
11:44pm 
Much cleaner implimentation. Simplicity trumping complexity.
The fawcett valve now faucet_valve was confusing, hard to follow and overly complicated.
The faucet valve governes the flow of control first detecting if case number or case word.
I ripped out the number code and placed it into a seperate module.
Easier to follow what's going on now. Pure zen. Elegant.


10:36 pm 

By putting the numbers methods into a separate module that changes the switch case string from number version to strings 
it's easier to keep track of what is going on and understand the code and reduce the complexity.
It dawned on me to just keep the numbers transformation code in its own module. So simple in hindsight.

Very close now. Managing complexity is only possible with divide and conquor.
Luckily I developed the numbers version of the switch case separately.
Testing it. Some interesting bugs but it's nearly there. A labor of love. Lot of code.
I was thinking today that not only will I be using this switch case daily in my code
but the whole world will be able to use it too. It's a rush thinking of someone contemplating
how they want their code to look and they learn that there is a beautiful smart and cool
switch case in python with identical switch case behavior (and look and feel) to JavaScript and C.

I never imagined how deep this program would be. Never wrote a parser before. First code generator too.
I've generated dynamic JavaScript before which gave me the courage to attempt this.
My saving grace was a year back I made a Python if elif else: and added a switch() and fallthru()
and that's what gets generated. If I hadn't already lucked out making that work in PyDev I never
would have attempted this.

In review the switch using words, multiple words for cases works and the switch using numbers and macros to and thru works
and I made a faucet valve method to test what the first case is number or word and then control if it bypasses
the rest of the valve and does the string words by default or if a number is detected it calls the methods
that converts the case numbers into strings (ex: case "1": from case 1: )and detects and expands macros to and thru.
Macros work. I love macros. Knuth liked them and they are in Lisp and C and now in Python.

Look for the working code tomorrow. 
	
9:07 am
Figured out how to make it work.
Putting numbers methods in separate module
Which already works.
Faucet_valve correctly detects words or
Numbers now and so tonight the dream
Will become reality.
Will also add reset() method to start each switch with virgin settings.
And will test several switches in sequence.
Was also pleased by happenchance to notice sql calls done
With same technique I use for switch case in long string var.

8:03 am
adding fuzzy logic and flags to make it work


7:32 am California Time
words in cases works through faucet_valve control switch case
debugging and testing cases with numbers adding flags, step by step sequence
discovered I needed to add scenario for if case 1:  without a to or thru whoopse.
slow and steady wins the race. the turtle won the race and the rabbit lost. slow and methodical.


Tuesday, March 16th, 2021
12:42 PM California time.

Officially connecting the functions together after unit testing to
ensure that switch with words works and then switch using numbers works
and then that reset works so that multiple switch cases can be used without
interference by wiping previous switch case input data and output data.

Unit testing for release and connecting the functions together.
Example functions in the process of testing.
This is a function that determines if words or numbers are used in the switch case and directs methods to be called
if numbers are used in cases. If words are used it flows through as a bypass.
Having fun. Nice to seeing the software grow in a controlled manner. Not tested yet. Coded a lot last few days
Dijkstra and Knuth method writing raw code and thinking it thru with minor testing.


#code for resetting switch case module vars and lists in parser and codegen so they are wiped clean.
#zap var method
def zap_var(y):
	eval("y=''")  #this empties the var
	return y  

#empty_list method
def empty_list(x): #might need to have it take in with string
	# and then do this x = x[1:-1] possibly
	eval("x.clear()") #this empties the list by the name entered

	

list_of_lists=[['applepie'],['peachpie'],['lemonpie']]

applepie=["one","two","three",'four','five']
peachpie =["fun","silly","iceplant",'seagulls']
lemonpie=["lemon tree", "plum tree", "pear tree"]
################################
##  see_each_list_contents()
###############################
def see_each_list_contents():
	print("see each list contents testing this now")
	counter=0
	print(list_of_lists[0])
	print(list_of_lists[1])
	print(list_of_lists[2])
	for item in list_of_lists:
		weasel=item[counter]
		print("list name=",weasel)
		#this loops through the list item from list above
		for item in eval(weasel):
			print(item)
		print("------------")
	
	print("==== did it work ====")
	
	
see_each_list_contents()


 # flush all vars and all lists which will be done after codegen completed
 # this flushes the lists to empty and vars set to ''
 #################################
 ##      american_standard()  
 #################################
def american_standard():
	#empty lists used in parser and codegen
	#note the list_of_lists does not get emptied, these are necessary for the data structure
	for item in list_of_lists:
		weasel=item[counter]
		print("list name=",weasel)
		#this loops through the list item from list above
		for item in eval(weasel):
			print(item)
			empty_list(item) 
			print(item)
		print("------------")
		#empty_list(item) #this empties this list to []

    #empty vars used  in parser and codegen
    #the list_of_vars[] does not itself get cleared it is for the loops reference
	for item in list_of_vars:   #which have their names in a list for convenience
		vartime=item[counter]
		print("list name=",vartime)
		for item in eval(vartime):
			print(item)
			zap_var(item) 
			print(item)
		 #this empties this var to ''


		
		
	
#this is a flag to determine if macros thru and to are in the switch case
do_macro_conversion= False # by default
# I can't assume that there is a to or thru macro in use
def detect_if_thru_and_or_to_macros_exist():
	if numbers == True:
		#do a count
		number_of_thrus=switchcasetester.count(" thru ")
		number_of_tos = switchcasetester.counter(" to ")
		print("the number of thrus =", number_of_thrus)
		print("number of tos =",number_of_tos)

		global switchcasetester
		print("=========testing case_numbers_to_strings===january 5th 2020====")
		mycounter = 0; thru_count = 0; 
		for line in switchcasetester.splitlines():
			#case in line     AND   either thru or to
			if "case" in line :
				if " thru " or " to " in line: #they mean the same
					thru_count += 1
					mycounter += 1
				else:
					mycounter += 1
					pass
		print("thru_count",thru_count)
		# determining what the thru/to count is which turns on do_macro_conversion 
		if int(thru_count) >= 1:
			print("yes thru_counter >= 1 so do macro conversion")
			do_macro_conversion = True
		else:
			do_macro_conversion = False



			

# fawcett_value function 
# this function uses the following methods:

#           check_if_first_case_is_number()
#           detect_if_thru_and_or_to_macros_exist()
#           make_list_of_lines_using_thru_macro()
#			bottom_up_change_of_thru_line_test()
#			change_to_into_thru()
#			expand_thru_macro()
#			case_numbers_to_strings() 

##########################################
#             fawcett_value()
##########################################
def fawcett_valve():
	print("fawcett_value called control flow of words or numbers")
	mytrace('fawcett_value()')

	#test if first case is number and not a word or character
	check_if_first_case_is_number() #puts True or False put into valve[0]
	firstcase = valve[0]            #True if number otherwise a string so False
	
	# detects if cases are numbers not words
	# if firstcase is True it's numbers else it's False and words
	if firstcase == True: # ex case 1:    #if firstcase is a number (not a word) True it's a number
	
		print("numbers detected for cases   firstcase == True ")
		#tests if there are 'thru' and/or 'to' macros in case lines with numbers
		#in ex: case 1 thru 10:   ..and..    case 11 to 15:
		do_macro_conversion=detect_if_thru_and_or_to_macros_exist()
		# This if runs if there are macros to and/or thru in use in this switchcase
		#determine if macros thru and/or to in case being used in this switch case
		
		if do_macro_conversion == True:
			print("do_macro_conversion == True so expanding the macros")
			#so these methods are only called if the switch case uses only numbers
			make_list_of_lines_using_thru_macro()
			bottom_up_change_of_thru_line_test()
			change_to_into_thru()
			expand_thru_macro()
			case_numbers_to_strings() # this changes case 1:  into case "1": etc
		
		else:  #if case number like case 1:
			print(" do_macro_conversion == False:  meaning no macros to expand")
			#this means not numbers but words so do nothing else different 
			#do nothing becase if we reach here it's words
			print("string words  detected in cases")
			pass
		
		#end inner if
	else:  #False meaning first case is string and not a number
		pass
	#end outter if




Big release tomorrow Tuesday March 16th.
Organized and streamlined code for switch case.
Redid reset so no module reload necessary. 
Support for words and numbers.
Example case “dream on”:
Example case 1 thru 10:
Macros work. Multiple switches support will be working.




Sunday, March 14th, 2021 5:51 am California time
Listening to Neptune Currents (Sunday mornings only) on KKUP 91.5 FM
Also listen to KZSU Stanford 90.1 FM
Both available online Free on MyTuner Radio

I should be putting up the workings switch case version 1.0 possibly tonight or at least this coming week.
It will do strings, numbers, and multiple switch cases. I have done a lot of refactoring to simplify the codebase
and I have been coding a lot of methods to make the code more readable and manageable so I can reuse more code.
The nested switch case will be added a week later. (this means a switch case with a nested switch case in it)

Starbucks morning coding.

I had initially but the fawcett valve inside of the switch method and then I concluded that
it would be much more practical to detect whether a particular switch implimentation was
a number or string before generating the Python switch implimentation. I designed the valve
with a simple if else with if number in first case equals True then it's a number case.
Now I will add a detector for if int, float, or number with commas.

The original code for strings is the main body and an if else at the top determines whether to convert the
numbers in cases into strings and then proceed with the normal switch conversion behavior treating
the entire switch case as strings. If the first case is not numbers then it just skips the stage of 
converting numbers to strings.

I designed the code for using numbers and words in switch cases.
The initial design was: ex   case 4:   but now tonight it will handle case 4.5564:  and case 3,445,444:
I am just trying to show some latitude and expandability and flexibility of the design.

The body of each case that uses numbers will have a converter to treat the number as it's original state
so it can be used for math calculations. I have not added that feature yet. Likely it will be a var value
so it's live for doing math as opposed to the implimented case state where everything is a string for convenience.
This way numbers are in one state for the case as a string and exist as a playable number for math.

I will be adding ints and floats and numbers with commas too for full support.
I designed the reset mechanism to bypass having to reload the switch module for
each instance of a switch case. Will simply flush the vars and lists in the parser and codegen.
I will have time to add this code and test it later this afternoon.

I recently was perplexed when my switch code broke in Sublime with an error 
can't reload(module) so I did a work around and eliminated that route and wrote two methods
to clear out vars and lists; each will be done with a loop going through a list one by one.
Actually an elegant solution.

Beta Conversion of numbers to strings in switch case.
I still need to add some ifs to check if the macros exist or not before attempting to convert them.


#if "thru" in a line
#case is [0] first number [1] thru is [2]  second number [3]
# case 1 thru 3:
determine_if_cases_are_numbers=[]
#this just grabs the word/number in the first case to determine what it is
def check_if_cases_are_numbers():  #this does nothing currenlty
	mytrace('check_if_cases_are_numbers')
	global switchcasetester
	grabit=''
	print("========march 11th 2020====")
	mycounter = 0
	for line in switchcasetester.splitlines():
	#loop do splitlines
 		if "case" in line:  #it only needs to test the first case to verify
 			grabit = line[4:-1]
 			print(grabit)
 			grabit = grabit.lstrip()
 			grabit = rstrip()
 			print(grabit)
 			answer = grabit.isdigit()
 			print(answer)
 			determine_if_cases_are_numbers.append(answer)
 			break # I only need to grab the contents of the first case
 		else:
 			mycounter += 1
 			continue

			
#########################################
def change_to_into_thru():
	mytrace('change_to_into_thru')
	print("change macro to into thru")
	print("=========")
	#print("this is presuming we know it's a number switch case")
	#print("if the macros to and thru are used they need to be change")
	#print("to is converted into thru")
	############
	global switchcasetester
	print("=========looping thru looking for to===feb 5th 2020====")
	print(switchcasetester)
	mycounter = 0
	for line in switchcasetester.splitlines():
		simple = mycounter-1
		
		if "case" and "to" in line:  #this means the macro to
			print(line)
			
			banana=''
			banana=switchcasetester.replace(" to "," thru ")  #just addded spaces
			switchcasetester='' #this nukes it resets it
			switchcasetester = banana
			print("the result of changing macro to to thru is this:")
			#print(switchcasetester)
		else:
			pass
		
		


		
def make_list_of_lines_using_thru_macro():
	mytrace('make_list_of_lines_using_thru_macro')
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
	print("==@@@@@@@@@==THIS IS the list with thru macros line numbers====")
	print(list_with_thru_macros)		
	#then I need to reverse the list
	backwards_thru_list = list_with_thru_macros
	backwards_thru_list = backwards_thru_list.reverse()
	print("########### backwards order now #####")
	print("backwards we have",backwards_thru_list)
	bottom_up_change_of_thru_line_test()

##### testing january 10th to go to each case thru from bottom up and change line
##### to prove it's working
####################################################################
## what this does is change the thru macro line starting at the bottom
## by accessing the backwards list made above 
##  backwards_thru_list  that took in the line number of each thru line and reversed it
##########
def bottom_up_change_of_thru_line_test():
	mytrace('bottom_up_change_of_thru_line_test')
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
		#beta = mycounter-1
		
		#if counter == item(line number)
			print(line)
			


smart =''
beta =''
opal=''
import re
foolish =''
newline=''
####### case_numbers_to_strings changes number cases to strings with the number inside
#######  I still need to sniff and detect if the cases are numbers before calling this 
##############################################################################
#################### case_numbers_to_strings() ###############################
##############################################################################
###### this converts the numbers to strings such as case 1:  to case '1': ####
##############################################################################
def case_numbers_to_strings():
	mytrace('case_numbers_to_strings')
	global switchcasetester
	print("======THURSDAY TEST ===testing case_numbers_to_strings===january 5th 2020====")
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
			holder = "'" + cool + "'"
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			print("\t\t" + newline)  #adds tabs to front of it
			print("next I will use replace to each case line")
			#see if it works here inside of the switch case line by line
			############################
			# see if this works
			opal=switchcasetester.replace(line,"\t\t" +newline)
			switchcasetester=''
			switchcasetester = opal


			############################
			mycounter += 1
		else:
			mycounter += 1
			continue
	print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings
	#HERE is where the changed case numbers as strings are put into switchcasetester
	#will use a replace here to the switchcasetester string
			

=======================================================================================================

Friday, March 12, 2021 8am California time.
Solved problem with Sublime not reloading modules (it has disabled it). I am using Sublime now. Though using BBEdit for diffs.
Quote: "SublimeText does not natively support module reloading"
So solved a work around that worked last night and I will add the code tonight to the switch case code base.
So now I should be able to use infinite switch cases in real-time and reset them instantly so there are no 
variable collisions. So the switch will be faster and not require reloading the switch case module which was
my original goal.  

Will start cleaning up the code and taking out the prints and adding the documentation.
Such a thrill seeing this project blossom.

Oh, I will finally impliment tonight using cases that takes words and then takes numbers next by adding the filter
to the parser. I decided that instead of having the flow valve inside of the switch method I will instead have
it in the preparser to look at what is in the first case in the switch code before parsing commenses
and that way it determines whether it will be a word(s) or number(s) so this means that the decision for
what type of switch it is characters/words or numbers happens before the switch code in python is generated so
this should be faster.

I have been working on the diff between the normal (words) implimentation of the switch and my other switch that uses numbers and macros
and how they are different to clearly divide them and thankfully the way that I implimented numbers will work perfectly as
the top hat above the normal switch code and is triggered to run only if it is determined if the switch's first case is a number
meaning it's a number switch. 

I will also be testing using several switches tonight that waterfall from one down to the other two switches with one being numbers.
And now that it should work without having to reload the switch module it should be faster.

So much fun! Dogged determination. 





switch input valve to determine if word/char or number
this determines the path course for words or numbers for a given switch case.
This just shows what has been added to the switch(x) and testing prints

In review switch cases are phenomenally versatile with nearly endless configurations.
I started with handling words and now adding numbers and slowly integrating them.
Initially handled      case "word":
added  phrase cases    case "merry christmas":
added numbers          case 1:
added macro thru       case 1 thru 10:
added macro to         case 1 to 10: 
For numbers in switch it's different because I added macros to write code faster
and using numbers it will have to handle math so I will add a macro to conver to int, float, etc if math formula calculations are added

def switch(x):
#####################  filter to determine if input is number or word/letter/alpha
	print("we are inside of switch now",x)
	global input
	global valve_setting
	valve_setting ='' #clears it out if previously used
	#here  x is tested if it is a number using builtin method isdigit()
	theinput = x.isdigit()
	if theinput == True:
		#print("its a number ")
		valve_setting = "number"
	else:
		valve_setting = "word"
	print("this is inside of the switch statement")
	print("that takes in input and checks if number or word")
	print("the valve_setting =",valve_setting, "which is",x)


Tuesday, March 9th, 2021 4 PM Californai time
testing valve for words or numbers for switch. Valve inside of switch determines if cases are words or numbers.
The way that it actually works is numbers are put into strings and that way it just works. That was a stroke of luck.
I modified my regular switch to just handle numbers and so  I will keep them separate and then integrate them
slowly with the alpha word switch the dominant main vein and then have a detour for numbers to convert them to strings.
I will add a do_math() method if users want to do math inside of the switch with numbers.
So the first phase is seeing it work with either words in cases or numbers and then I will integrate the code
but initially the code is totally separate to prevent any conflict between the two code bases. 

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
        if acounter > x and 
