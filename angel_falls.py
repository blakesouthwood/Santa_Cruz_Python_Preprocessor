June 19th, 2021 9:32 pm
successful test detecting innerswitch JavaScript/ C style input string copying to list
successfully translated it into Python (didn't execute when attempted though)
Did some fiddling to get it working 
Successfully ran test python innerswitch encased in a function nested_switch_1(n):  
and I learned what needs to be included for it to work. And the the nested switch
ran with exec(fiddler[1]).
For some strange reason the generated python of the nested switch (which wasn't in a method) 
had unforeseen issues so I worked backwards to a file with working python and will figure out
how to correclty generate the correct code. Tomorrow I will correct the translation process 
from input string in list to translated to python string neighboring list.
Bear in mind that the reasoning behind this is the nested switches should ONLY run when they
are triggered to run and not to run otherwise willy nilly. That would be bad.(not good)
I have been focusing on detecting the nested switches and copying them and placing them in a separate
string and then appending to a list in order of occurence. That went smoothly.
I was able to set the nested flag to True and the codegen correclty added the output string to a list
however all of the necessary ingredients to make it actually run were lacking. I neglected to put it into
a custom method and it was lacking access to the lists of the cases and so it was learn as you go to solve it.
Listening to https://www.youtube.com/watch?v=8wLwxmjrZj8 Space Ambient Music to focus.
When I tried to exec() the generated python representing the nested switch it didn't run. So I had to backtrack
to working experiemental code and then it made more sense how to get it working.
								   
Another issue popped up to add a tab to each line in the nested switch which is glued inside of
unique nested switch name. Wrote that the other day thankfully and it works like a charm.

happydays='''
#==================
#for inswitch
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
x = "one" #it was "one"              #<<=== x must be a string just as matching case == "string", 
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
tahoe=[]
tahoe.append(0)

victory=[]
victory.append(0)

#######################
### inner switch_1(n):
#######################


def inner_switch_1(n): #test2 is the test
    print("=======inner_switch called==1==",n)
    casetest1 = ['test5','test6']
    caselist2= ['google', 'fishfood', 'probability']
    #this is switch inside of inner_switch
    
    inswitch(n)                           #<<====== inswitch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')

        elif case  == "test2":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            infallthru('test3')         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            infallthru('test4')

        elif case  == "test4":
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in caselist2: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest2")   
            print("solving the last few probs now") 
            print("oh my god it worked")               #<<==== I just put case here to show which word matched
            print("========= coolness ====")
            print('wow this is really sweet coding genius')
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   
###================

inner_switch_1('google')

'''

fiddle=[]
fiddle.append(0)
fiddle.append(happydays)
#print(fudge[1])
print("TESTING BLADE RUNNER SERIES =what does an innerswitch by itself need")
print('it is all in one big string about to execute it')
exec(fiddle[1])
print("___________")
print("after wards we have the results above this line")
print("it should return four words starting with succ")


June 17th, 2021  1020 pm
Progress on code generator for nested switch cases. This is massively complex and I have simplified it to make it work.
Flag worked to detect if nested switch
added generated python switch to list.
Practiced adding 4 separate nested switches python to list as strings.
Then I started writing methods to manipulate them transforming them for behaving as nested switches.
Converted switch to inswitch and fallthru to infallthru.
Made method to generate nested switch method names dynamically for level and depth since each has an address.
Made auto-tab method.
It's all coming together, building the puzzle pieces and practicing what needs to do what and when.
Did click thru walk thru of process of transformation and building the string with the
nested switches in methods and now working on transformation for
the main switch with the nested switch method which looks like this:
inner_switch_1('test4') #however it can also accept a variable so it can be a list[0] input or x, etc.
Probably till end of weekend till this feature is solid and I'll upload it.

June 17th, 2021  10:55 am
Fixed bug that crashed module finally determined it was triggered by the word "case" in a print statement within a case.
Built auto-tab method creationg for my generator.
Built string stacker method to build nested switches stack in correct order with main switch at bottom.
Nearly done with stars of the constellation to make the small system work. Coming together quickly now.
Working on building output stack of strings of inner nested switch methods with generated python code
and the main switch that has the innerswitches embedded in it. Working on the code gen half now.
The parser part now works for grabbing the nested switches. I just have to trigger calling the switch module
from the input string switches in a list for each nested switch and the main switch and then putting the output
strings into another list that will be used to concat them all together before calling them.
More progress testing the generated python methods for the nested switches and the main switch
which has the nested methods inside of a case to represent doing a true nested switch. Unreal - it's working.
Battled bug from hell last night for 5 hours ValueError: None not in list. It was seeing the word "case"
in a print statement which crashed the program. I will add an if to fix it later. Case works but case crashes. 
Massive momentum this morning on constructing parser and working on codegen.
I put each input nested switch and the main switch in raw C style switch form in a list that each is appended to.
Then I will call the switch module and translate with nested_switch[0] set to True so that the generated python string
is not executed but instead is added to another list which then will be used to build
the large multline string in the proper sequence and then and only then executed.
I refer this technique to trapeze from my experiences at Club Med. It's all a process and lists make
it so much simpler to follow the logic of the steps and manage it.
I use a flag to deactivate executing the python translation and instead save the output python string
to a list which it is appended to. And then I already wrote teh code to reassemble it building a string
that will then be executed. For this mulity layer cake string to work I first insert (add) the 
methods for the inswitch() and infallthru() which are used in the nested functions and each nested switch
is encased in a separate method to prevent interference with other switch and fallthru calls.
example of some code of a nested switch function.

Note. I decided on a rule for nested switches to aid the parser. At the bottom of a nested switch
the progarmmer must use "endswitch". However, so I don't get flamed I will allow "}" for C purists to end a 
nested switch and not absolutely require "endswitch". So both camps are happy. It aids readability and it's used in PHP but it differentiates
from the } and it's easier to ascertain that the switch being examined by the human(s) is definitely
a nested switch. 

def inner_switch_2(n): #test2 is the test
    print("=======inner_switch called==2==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    
    # 1 tab depth
    inswitch(n)                           #<<====== inswitch() method is here
    # 1 tab
    while True:                  #<==== infinite loop used for fall thru method
        #2 tabs depth
        if   case  == "test1":
            # 3 tabs words within the case
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')
	

input string what programmer would write that is put into a string (example)
tennis ='''
	
	switch(exp) {
		case 'cholpolty':  
			print(\"burrito!\")
			print("bowl")
			print("lemonade")
			break
	
		case 'panda express':
			print('good food')
			##===============================
			##===== inner s w i t c h  ======
			iexp = 'code express'
			switch(iexp) {
				case 'cholpolty':  
					print(\"burrito!\")
					print("bowl")
					print("lemonade")
					break
	
		
				case 'code express':
					print('good food')
					print("in hollister ")
					adder(1)
					buildstring('soon it')
					print('run')
			
				default:
					print('no results')
					print("that is all")
					break
			endswitch
			##===============================
			##===============================
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(2) #this won't do anything until it is executed
			buildstring(' will work')
			
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(2) #this won't do anything until it is executed
			buildstring(' will work')
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3)
			buildstring(' and I will celebrate')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
here is an example of what the generated stack of nested switch as functions with
the main function at the bottom would look like so visualize the stacking.

aqua ='''  
global x
x = "one" #it was "one" 

tahoe=[]
tahoe.append(0)
# =======  main  ===================================


victory=[]
victory.append(0)

  
####THIS IS WHAT IT MUST LOOK LIKE

def inner_switch_1(n): #test2 is the test
    print("=======inner_switch called==1==",n)
    casetest1 = ['test5','test6'] #look at this right here 
    #this is switch inside of inner_switch
    # 1 tab
    inswitch(n)        #<<====== inswitch() method is here
    # 1 tab
    while True:         #<==== infinite loop used for fall thru method
        #2 tabs
        if   case  == "test1":
            # 3 tabs
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')
        #2 tabs
        elif case  == "test2":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            # 3 tabs
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   
###================



### inner switch_1
#######################
### this is inner_switch()
# looking at what is different from the regular switch 
# what is differnet is the nested switch is inside of a function
# and instead of switch it's called inswitch(n)
# instead of fallthru('something') it's infallthru('test2')
# if missing break it's infallthru('nextcase')

#notice this is in a method

def inner_switch_1(n): #test2 is the test
    print("=======inner_switch called==1==",n)
    casetest1 = ['test5','test6'] #look at this right here 
    #this is switch inside of inner_switch
    # 1 tab
    inswitch(n)        #<<====== inswitch() method is here
    # 1 tab
    while True:         #<==== infinite loop used for fall thru method
        #2 tabs
        if   case  == "test1":
            # 3 tabs
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')
        #2 tabs
        elif case  == "test2":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            # 3 tabs
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   
###================






#######################
### inner switch_2
#######################
### this is inner_switch()



def inner_switch_2(n): #test2 is the test
    print("=======inner_switch called==2==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    
    # 1 tab
    inswitch(n)                           #<<====== inswitch() method is here
    # 1 tab
    while True:                  #<==== infinite loop used for fall thru method
        #2 tabs
        if   case  == "test1":
            # 3 tabs
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')

        elif case  == "snowman":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "rabbit":
            print ("te what do we have here ool...")
            tahoe[0]="mickey mouse" #puts victory into tahoe[0]
            print("tahoe[0]",tahoe[0])
           
            print("out of inner switch 2")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   





# =======  switch  =================================
def switch(x):
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        x = str(x)
    global case
    case = x.lower() 
    
# =======  fallthru       =========================
def fallthru(y):
    eval("switch('" + y + "')")
    
    
#==================
#for inswitch
def inswitch(n):
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        n = str(n)
    global case
    case = n.lower() 

#=====================
# for infallthru    
def infallthru(n):
    eval("inswitch('" + n + "')")



# by definition a switch will reside within a function, that's obvious.

casetest1 =['google', 'fishfood', 'probability']

#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
# this is a function with a switch case
# which has a nested switch case within it inside of a function called inner_switch_1
# =======   testfunction    ========================
def testfunction(x):
    print("=== testfunction called with x====TESTING THIS JUNE 17th======= ",x)
    print('test function testing switch case behavior')
#this is the switch called 
#this is the FIRST switch the main switch 
# ========  switch case code =======================
    #1 tab
    switch(x)                           #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        # 2 tabs
        if   case  == "one":
            # 3 tabs
            print("this is the first case in the main switch")
            ######################
            inner_switch_1('test4') #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')

        elif case  == "word":
            print ("this is back in main switch now !")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "rudolph":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            print("=== this is 2nd nested swith differnet case switches have ended")
            ######################
            inner_switch_2('rabbit') #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch2 below")
            print("tahoe[0]=",tahoe[0])    
            break

        elif case  == "phrase":
            print ("testing wow works on Sublime now Coooool...")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1") 
                                   #<<==== I just put case here to show which word matched
            break

        elif case  == "22":
            print ("gui design")
            break

    #default:
        else:
            print('none')
            break         
#end loop
#end switch

testfunction('one')

'''

print('it is all in one big string about to execute it')
exec(aqua)
print("after wards we have the results above this line")



June 15th, 20201 10:00 pm
Made more progress with code gen for nested switch design and tab counter and tab inserter for auto-indentation
Made progress on parser yesterday and today leaps ahead of where I thought I would be due to dogged determination.
Working on both parser and code gen and will next generate the python code with regular module by
just adding a flag if nested_switch[0] == True so the generated module won't be executed but will
instead be added as a string to a list with each position representing the number of each "nested switch" within 
all encompassing main switch that they reside in no matter how deeply nested the switches are.
First doing two one level deep nested switches. Will try triple level after success.


June 15th, 2021 7:31 pm 
Good progress at Starbucks this morning. At this pace it should be working in sections by this weekend and then
I will connect it together by Sunday.

Grabbing nested switches and copying as a new string to a list.
Swapping switch and fallthru for unique method names works
Working on calling switch_module to translate each nested switch to python tonight.
Steady progress. Bringing the realization of each phase of the translation conversion into reality.
Just like falling dominos once each independent stage works the whole system will work. 

June 14th, 2021  8:33pm
DESIGNING UNIQUE PARSER AND UNIQUE CODE GENERATOR TO IMPLIMENT... nested switches in Python.
First I'm looking for the patterns to reveal themselves so I can create the formula and templates.
Alpha attempt will be a switch with 2 nested separate switches depth 1.
First attempt will be one nested depth 1
Second attempt will be two nested depth 2
third attempt will be three nested depth 3

NESTED SWITCH IMPLIMENTATION special parser and special code generator.
Have to detect inner switches first.
Will hopefully see blossoming of nested switch analysis and generation within next few days.
The theory is strong it's just a bunch of little steps. 
Doing step through design of parser detecting inner switches
copying and storing inner switches in separate named strings
creating template for the code gen

copying modifying the module for generating a switch to generate nested switches with unique method names
Made dummy test data switch with two nested switches  and doing step analysis to convert into code gen layout
to generate the python variant which will have unique sequentially numbered innerswitches inserted into main switch
strategicially positioned in precise case sections.

I have tomorrow off so should have process figured out and step sequence clear by tomorrow night.


June 13th, 2021  7:50pm California time
Designing the multiple switches parser at first seemed tricky but I simplified
it to treating each nested switch as a domino. I then realized I can just make
a list with each nested switch as a string and then run them thru the existing parser to
create the output string(but not exec() it) and then the output string can be added to a second list
and then in order I concat each of these nested switched along with the special methods for handling
the nested switches above these and then I do the main switch again thru the existing switch module
to translate it into a string and then 	(my thinking was actually from the stripes in the American flag)
and then exec() the produced finished string. The test I just did on test output proves the concept is sound.
Chipping away at the boulder one by one and modular development is the key and absolute confidence it can be done
are all the keys to victory.

Did proof of concept running test switch with two nested switches(as methods) and it worked.
So the theory is sound. The first time I tested it in a real world situation.
Working on parser now for nesting. The theory is based on runners(each nested switch) on bases in baseball. Instead of looking
at the problem as one big chunk of code it's managing the chaos by reducing the problem set to similar problems.
So what could be mind boggling chaos can be conquered with order and simple design techniques. I never imagined
that this was all going to actually work. On StackOverflow whenever someone dreams up their design and implimenation of a switch case
for Python they always get a comment (unanswered) can it do a nested switch? I was determined to make mine work. 
I actually got the idea of putting the nested switch into a function from the solution of how to break out of a 
nested for loop with a return inside of a function since break only breaks out of one but not both loops. It works nicely here too. But the solution isn't obvious at first
but it works. It's quite profound. Seeing code work is such a thrill. 

The parser for the nesting is unique but I will use the initial parser and
codegen to create each individual nested switch translation which is then added as a string concatted top down
to create the illusion of the nested switch whereby each nested switch is actually a method inner_switch_n with a sequence
number so it can be called. Thankfully I designed this back a year ago in pydev and it involved a great deal of thought.

first_string_test_nested_switch.py  and test_generated_code.py
Designing special parser which translates the inners switches first concats to a string
and then adds the main switch at the bottom and then executes it as one block.
So the individual nested switches are translated into a python string and referenced in a list
and then all concacted together above the main switch so they all live within the same string
which is then executed together. I already thought thru the parser and the way it works
is I number the switches (I get the count first) and then I note the location (line number)
of each switch and endswitch and the case that each inner switch resides in which case (numbered
sequentially and the level of depth derived from the tab count in front of each nested switch to determine depth.
Bear in mind in reading the input switch string it will look just like C/JavaScript code so a deeply nested
switch might be many levels deep and I need to derive the exact case it's in and count tabs to determine it's location
so I need to deduce the level and depth and number each nested switches precise location which could be several levels down.
											

June 10th, 2021 7:31 am California Time
Making progress on parser and code gen and design logic for nested switches.
Working code that will be the running output.
Uploaded proof of concept working three level deep nested switch case
which demonstrates it working. It will be generated but this
show the python implimentation that will be generated.
nested_switches_gold.py

I'm designing the special parser and code gen.
The parser will be a multiple pass using a loop and lists
to generate each nested switch  and fill the incoming data
with the logic done with fuzzy logic.
It will be working within a week.


June 9th, 21021  11AM
So put this at the top of your input code.

# the trigger for each switch isn't switch itself but it is endswitch(sw)
# there is,however, a switch method which passes the input to a case variable.

#PHP has an endswitch so it was a happy compromise

import official_switch_case_silver
from official_switch_case_silver import *  

#And in the file that has your code 
# it looks like this

#you can rename clever to whatever you want
clever('STARBUCKS')

hide_input_switch_string()   #input so what the string right below here
hide_generated_code()

print("== switch 1 ==")
print("--------")

sw =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			break
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third attempt")
			print("deer and quail about")
			
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case AMERICA:
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('sorry no matches')
			print("out of mocha")
			break
}
'''
endswitch(sw)


#going up in a few days from May 13th so by the 15th.
clever('2') #this would change varholder[0] 



hide_input_switch_string()   #input so what the string right below here
show_generated_code()
#show_generated_code()
#this switch use macros thru and to
print("== switch 12 ==")
print("--------")
 
sw ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
			
			
		case 21:
			print('Blake you did it a real good job')
			print('macros working in Python')
			print(' I did it - it works')
			
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
endswitch(sw)



clever('big bird') #this would change varholder[0] 

#hide_generated_code()
#this is the code being run

print(" == switch 11 ==")
print("--------")

sw =''' 
	switch(exp) {
		case 'fishy':  
		case 'two da':
		case 'three da':
			print(\"squirt gun!\")
			print("water everywhere")
			
			
		case 'big bird':
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			fallthrough
			
		case 'Israel canal':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			fallthru
			
		case 'ufos are real':
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
endswitch(sw)

#this one demonstrates the fallthru math adder(x) and buildstring(x) which concats strings
clever('panda express') #this would change varholder[0] 


hide_input_switch_string()   #input so what the string right below here
show_generated_code()

sw ='''
	
	switch(exp) {
		case 'cholpolty':  
			print(\"burrito!\")
			print("bowl")
			print("lemonade")
			break
	
		
		case 'panda express':
			print('good food')
			print("in hollister ")
			adder(1)
			buildstring('soon it')
			print('BARK')
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(2) #this won't do anything until it is executed
			buildstring(' will work')
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3)  #this does a running total essentially after adding
			buildstring(' and I will celebrate')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)

#output of adder and buildstring
final result=
result of adder adding 6
result of buildstring concatting  soon it will work and I will celebrate

June 9th, 2021 8:27 am 
Taking out print statements and cleaning up the code.
It works. I just got the UPPERCASE CONSTANT style of C working like this:   case CALIFORNIA:  which is converted to a string.
The point is having the look and feel and behavior of ANSI C style switch cases. I added macros for numbers (to see if it would work)
and it did.  This works:  case 1 thru 10:   and this works case 1 to 10: So they get expanded to save time typing.
Right now switch needs to be indented one tab, case is 2 tabs and inside of case next line is 3 tabs.
My next version will provide freestyle so indentation will be auto-indent but not currently working doing auto-indent.

June 8th 7:15am
Another victory duplicating the different varied facets of the C style switch case implimented for python.
case WORDS_LIKE_THIS:
case TAHOE:  now works in switch case code just upadated 
file names:  official_switch_case_silver.py and test_inputs_beta.py
	
	
adder(3) and buildstring('new words')
works for fallthru adding or concatting strings in switch
example in file too and code works

June 5th 8pm  2021

8:10pm Just found my nested switch code I coded a year ago. What a rush.
	
Encouraging progress. Can correctly detect number. Looks like lowercase, uppercase, and alphanumeric will work.
It's all really about detecting if a solid number or alphanumeric and converting it into a string.
Scary test where nothign worked and I realized whoopse I didn't have it converted into a string first and the parser
choked on it. Funny. But initially scary. More progress tomorrow and updates.
Successful testing across the board tonight.



June 5th, 2021  6pm
Will just do C style UPPERCASE case for now to get it up and usable and add the other versions later.

Right now number of case sections is limited to 10. I will up it to 256 tonight. It can be as many as you wish actually.
Decided to let it work in all lowercase and alphanumeric too as an option.
So it could work as case lake_tahoe:   and as case lake_tahoe2:  and as case LAKE_TAHOE5 and case lake_tahoe_6:
in addition to standard ANSI C   as case LAKE_TAHOE:
Right now it works converting the stringified version into python code and I'm adding the sniffer tonight 
as a filter to detect whether it's a nonstring word constant and if so to stringify it.
Nearly done taking out the print statements with comments in the code base.
I added flags for viewing the input string switch and viewing the output generated python code
so these can be flipped at will for each switch case whenever a developer chooses.
Just above switch case string.

I still need to add ERROR CODE MESSAGES for bad input for nontraditional switch case style.
Such as missing default. Default not at bottom. No break after default. Improper indentation.
Bear in mind I will be adding a freestyle no indentation necessary version soon that will add
the proper format indnetation automatically. I prefer to think about my code and not dwell on tabs myself.

hide_input_switch_string()   # input string in doc string with var sw
hide_generated_code()         #this is the generated python code
or 
show_input_switch_string()   
show_generated_code() 

Also, the other night I changed Sutter to Adder(x) for the fall thrus to do math and looking at the function
a developer can easily modify it for doing more complex math. In example each element can be added to a list
and then eval(result) to use a formula and do a complex calculation. I left BuildString(x) the way it is
for concatting a string thru fallthrus.

Going through my previous code to see how I got a nested switch case working.

I will show working goto label next. The goto works already but I wanted to get the switch case working first.

I will also add when, unless, until macros via the preprocessor the same way I made to and thru work
for numbers in the switch case using replace and a prescan of the input string.



May 31st, 2021 Monday 9:19pm California time.
I never thought that this would work but it just did. Will upload it likely tomorrow or the next day.
It converts it to lowercase and it works. I wrote a few functions that I will test more tomorrow but it works.
It's a Constant uppercase switch case based on C style. Oh, I am working on auto-indent but that will take
a while so maybe in a week or two for that feature. I will add examples of tumbler adding thru fallthru
and concating a string in the next few days (they already work).
Also right now the upper limit is 10 cases (sections) I will move it up to 256 matching the C standard this week.

Results down below.
clever('LAKE_TAHOE') 

sw =''' 
	switch(exp) {
		case CASPER:
			print("swimming upstream!")
			print("water everywhere")
			break
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case LAKE_TAHOE:
			print("big dipper")
			print("constellation")
			print("milky way galaxy")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case AMERICA:
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
endswitch(sw)

# output of the switch case that is then executed
# so this would all be invisible in the background

exp = varholder[0]

caselist1 = ['casper']
caselist2 = ['coyote']
caselist3 = ['lake_tahoe']
caselist4 = ['france']
caselist5 = ['america']
caselist6 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['casper']
		print("squirt gun!")
		print("water everywhere")
		break

	elif case in caselist2: # ['coyote']
		print("Sesame Street")
		print(" groucho and animal")
		print("this is so fun")
		break

	elif case in caselist3: # ['lake_tahoe']
		print("big dipper")
		print("constellation")
		print("milky way galaxy")
		break

	elif case in caselist4: # ['france']
		print("massive ship blocking canal in Egypt")
		print("it was stuck for six days")
		fallthru('america')

	elif case in caselist5: # ['america']
		print('manure')
		print("no more horses")
		break

	elif case in caselist6: # ['default']
		print('one walking quack d')
		print("walking geese")
		break

	else:
		print('one walking quack d')
		print("walking geese")
		break


the input exp in clever was::  LAKE_TAHOE
we are inside of switch now LAKE_TAHOE
case = lake_tahoe
big dipper
constellation
milky way galaxy

May 31st Monday 5:12 pm
Taking out print statements in code.
Deleting unused code. Will upload latest version tonight.
Working on case CONSTANTALLCAPS:  style from C currently but it won't be uploaded for a few days.
Irregardless I will be updating the working switch with macros for numbers works to and thru and numbers switches
running before and after word switches. The module I made is solid.
I will add a feature for debugging to see the generated python for the switch which would be
#show_generated_code_on  this is not implimented yet

Also working on auto-indent so a swith can be done without indentations ala C and JavaScript and then it
is automatically indented with tabs. The flag to trigger this would be #auto_indent_on  at top of input string above switch(exp)
The idea for this came from copy and pasting which is disasterous in Python but this would use fuzzy logic to determine where
to indent properly in the code generator. But actually it doesn't really have to be indented. Information can be gleanded from
the input switch string without indentation as a guide.

	
May 30th 2021 Sunday 5:33 am
It works. Switch case works mimicing look and feel style and running behavior of C switch described in Yale University C style guide.
Just need to take out print statements.
Numbers works. Macros work. Preprocessor works. Words for cases works.
Works without reloading module. Cutting out unused code. Surreal feeling seeing it work.
Also tumbler works to do math in waterfall mode via fallthrus in switch case as it cascades down.
And tumber for concatting a string dynamically works using the fallthru waterfall.
Testing nested switch this week.




May 29th 7:29 pm California time.
cases with macros and numbers now works!
But I have a bug whereby cases with words stopped working so that's likely a boolean bug.
Will work on it tonight.
Exciting progress.

May 27th 8:27pm California Time
A fallthru can be explicitly stated with a word fallthru or fallthrough
or implicitly represented by the absence of a break

in the switch case a fallthru is designated at the bottom of a case with:
either explicitly as fallthru or fallthrough or implicityly with nothing -the absence of a break
a break is designated with break
so the absence of a break means fallthru implicitly
fallthru is my preference but I added fallthrough from Swift

May 27th, 2021, 7:36 pm California Time
This is the macro expansion showing the input switch string with macros and after the macros 'to' and 'thru' are expanded.
I made this a separate module to reduce the complexity. It was a bear to get working but I prevailed. 
#INPUT 



clever('21') 


sw ='''
	switch(exp) {  
		case 1 thru 5:
			print(" 1..5...")
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			

		case 6 to 10:
			print(" 6....10.")
			print('kangaroo hop hop!')
			print('taught me how to write code')
			break
			
		 
		case 11 thru 15:
			print(" 11....15.")	
			print('mocha blast')
			print('== 31 flavors===')
			

			

		case 16 to 20:
			print(" 16....20.")
			print('ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
		case 21:
			print(" 21")
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			print('')
			break
		
		case 22 to 30:
			print(" 22....30.")
			print('sitting in the shade')
			print('writing code')
			break

		case 31 to 33:
			print(" 31....33.")
			print('sitting in the shade')
			print('writing code')
			break


		default:
			print(" default")
			print('six walking duck de fa ul t')
			print('flying geese')
            break
}
'''
endswitch(sw)

#I will put the functions here - the order makes a difference -  they have to be in a particular sequence which works
#and the lists are key and where they are declared matters. I will take out the unused lists in a few minutes but
#putting it hear in case my computer crashes.
# This will be added to the main switch program tonight and uploaded to github tonight.
endswitch has been redesigned with number sniffer input_flow_valve() and cherry_pie will be called
macro_expansion(). the final version has numbers and words going thru the stirng parser

# I will take out the print statements soon and beautify the code with more documenation
# when time permits.



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






############################
varholder=[]
#def flush_lists():
#	varholder=[]
varholder.append("zilch") #if nothing changes it's default

var2=[]
var2.append("zilch")

def is_number(inputString):
	return any(char.isdigit() for char in inputString)
valve=[]
###############################
#apparently this needs to exist in this file











#####################		
newlist =[];count =''
######################
####################################################
##      swap_thru_lines_with_expanded_cases()     ##  this is for number cases
####################################################
def swap_thru_lines_with_expanded_cases():
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
			cat =is_number(smart[1])  #calling method to check if  #the case name is a number
									 
			print(cat)
			cool = smart[1][:-1]  #chops off : from end last char
			holder = "'" + cool + "'"  #this puts the number in quotes
			cool = "case " + holder + ":"  #this is essentially rewriting the line with number in quotes
			newline = cool
			print("\t\t" + newline)  #adds tabs to front of it
			print("next I will use replace to each case line")
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



###////////////////////////////////////////////===========
    
############################
list_with_thru_macros=[]
list_with_thru_macros.append(0) #position 0 nothing
backwards_thru_list =[]  #initializing the list
#############################
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
			print(switchcasetester)
		else:
			pass


###########################################		
## make_list_of_lines_using_thru_macro():		
###########################################
def make_list_of_lines_using_thru_macro():
	mytrace('make_list_of_lines_using_thru_macro()')
	print("=====WARNING WILL ROBINSON LOST IN SPACE====")
	print("* * * * WORKING ON FUNCTION make_list_of_lines_using_thru_macro()")
	print("===----------=== make list of lines using thru macros() ====--------=")
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
	#global mouse
	global opal; opal = ''; mycounter = 0
	print("value of mycounter should be zero",mycounter)
	for item in backwards_thru_list: 
	#set mycounter to a number for line in mouse.splitlines() : #this goes thru the mouse string
		print(line)
		
	
	

####=========== test here concatting little chunks for the switch case

###############
smart =''
beta =''
opal=''
import re
foolish =''
newline=''
#################


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
	global switchcasetester ## just addded thismay 27th
	for line in switchcasetester.splitlines():
		beta = mycounter-1
		if "case" in line:
			print(line)
			smart=line.split() #separates case from casename
			#checks if case name is a number returns True or False
			cat =is_number(smart[1])  #calling method to check if the case name is a number
			print(cat)
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
	print(switchcasetester) #this is to see the switch case input string after the modification
	#after the numbers have been converted into strings






list1 =[]
list1.append("four")



exp =''; case =''
exp = ""







		











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




find_default=''
lastbrace=''

list_trex=[]
listcandy=[]
defaultlist=[]  #here defaultlist is declared as empty







#================ this gets the case names from all cases
#talk about militant bull0 indentation -wasting my precious time unreal.
firstline =""
#additions on Sunday August 23rd, 2020
royallist=[]  #mythical list of tail for case section codegen
royallist.append('starter'); #which fills position0

varholder=[]
varholder.append('0')



#apparently this needs to exist in this file
def clever(i): #so it already exists we are changing its value
	#sw_reset()
	 #this reloads the module
	varholder[0]='' #this should reset it to nothing
	#reset()  #reset() is hidden inside of clever for input to the switch
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


























tail_list=[]
cranberries=[]
cranberries.append('starter')
  ##===========================
  ##==== def p51_mustang_2f() ===  adds the number to  fallthru(3) like that
  ##===========================
  #thi






#autumn()



crushit =[]









		




#======== sutterrsmill==============================
case_main_body_list=[]
case_main_body_list.append('starter')  #this is to fill up position 0

z =''


# big gears filling list with case bodies of python code





import re  #for regular expressions
#this one
handy_list_of_tabs=[]
dual_slots=[]
crummy =[]
fiasco =[]
n_count_per_section=''
case_section_lines_of_code=[]

#n

	#print("experimenting here in here we go")
	#get length (number of lines) of each
	#body_size = len(case_main_body_list[3])
	#print("the number of lines =",body_size)

print("")

acounter=0
#for item in case_main_body_list:
#	print(len(item))
#	acounter += 1












#print("tail_list cranberries =",cranberries)
###=============================================================================
x = 0;y =0
smart=''
#cranberries=[]
list_of_rows_of_case_names=[]
##################################

#making case section sublists here
#this is for making the variable lists to fill the case sections of cases
# and to refer to each of these caselists with ifs and elifs








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








#this will need to be called for each specific thru line
###==============================================================
###================  expand_thru_macro()  ===================
###==============================================================

inputnum = 1
def expand_thru_macro():
	mytrace('expand_thru_macro()')
	print('expand_thru_macro called')
	global switchcasetester
	print(switchcasetester)
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
			print("what does smart list have",smart)  #fallthr  missing a u
			print("smart alleck result for smart[3]",smart[3])
			print("does thisfix   smart list now!! have",smart)  #fallthr  missing a u
			print("this should be case", smart[0])
			print("first number ",int(smart[1]) )     #first number  don't need int
			print("this should be --thru--",smart[2]) #thru
			print("last number", smart[3])            #last number 
			print("will then write perhaps from list yes")
			print("the input for this macros test")
			print("=============================")
			print(smart[0] + " " + smart[1] + " " + smart[2] + " " + smart[3] + ":")
			print("")
			counter = smart[1]
			#this is filling up the newlist
			
			#### THIS FILLS newlist with the case info
			# ======LOOP  ==================
			for counter in range(int(smart[1]),int(smart[3]) + 1):
				newlist.append(counter)
				counter += 1
			print('newlist sees contents',newlist)
			ajax =''
			print("length of list =",len(newlist))
			print("this is GENERATED case code from macro with 2 prefix tabs") 
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
			print("this is expand thru macro in pumpkin-falls line 286")
			print("right here== ajax  is",ajax)
			snowy=switchcasetester.replace(line, ajax)
			switchcasetester='';switchcasetester = snowy
			print("=== testing $$ this is the result of the macro thru unfurled")
			print("=== testing $$ the unfurled macro should show up")
			print(switchcasetester) #was mouse here 
			#return ajax
			



######################################
##  convert_case_numbers_to_strings()
#######################################  #if no macros it just adds strings around numbers
def convert_case_numbers_to_strings():
	print("we are here in convert case numbers to strings did this reach this far")
	print("convert_case_numbers_to_strings() called ")
	mytrace('convert_case_numbers_to_strings()')
	global switchcasetester
	make_list_of_lines_using_thru_macro()
	expand_thru_macro()
	case_numbers_to_strings() #stringifies the numbers like this 3 becomes '3'




##############################
##         cherry_pie()  this calls convert_case_numbers_to_strings
############################## # may 26th testing this 
#this is reading numbers in cases NOT STRINGS and converting them into strings
cray=[]
cray.append('starter')
def cherry_pie(y): #expands macros to and thru (if they exist)
	mytrace('cherry_pie()')
	print("cherry_pie called")
	if valve[0] == True:    #meaning numbers in cases detected
		mytrace('starter_sequence_mode_2()')
		global switchcasetester; switchcasetester=y;
		print("what is in switchcasetester before expanding macros if they exist")
		print(switchcasetester)
		##CONVERT CASE NUMBERS TO STRINGS()
		#################################
		convert_case_numbers_to_strings()  ## <<=== expands macros here 
		#################################
		print("after expanding macros we have...")
		print(switchcasetester)
		cray[0] =switchcasetester  #this assigns the output string to cray[0]
	
		




daisy=''



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
			print("the counter for spotting word case is ")
			print(mycounter)
			print("coffee has in it at this point ",coffee)
			coffee.append(mycounter)
			print(coffee[0]) #just added this 
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

##################
## testing April 3rd 2021 seeing if this works or not. 


# flow_fork_input()  #this fills valve[0] with True or False
# if valve[0] is True  it means numbers = True  (thus numbers      )
# if valve[0] is False it means numbers = False (thus words strings)
## the new code will go in here Friday morning.. April 2, 2021
#this fills valve[0] with True or False for numbers in cases
#################################
##  flow_valve_input(y)
##################################
def flow_valve_input(y):  #this determines if switch case string is numbers or words
    mytrace('flow_valve"input')
    print("Flow Valve input")
    print("Flow valve[0] = True  if numbers")
    print("Flow valve[0] = False if word(s)")
    mytrace("flow_valve_input()")  
    getline  = grab_first_case_of_switch_string(y)
    toocool  = grab_first_case_line_in_switch_case_string(y) 
    toocool  = remove_tabs_from_string(toocool)
    valve[0] = check_if_number_in_string(toocool) #looks in case line
    valve[1] = toocool
    print("valve[0]=",valve[0]," and valve[1]=",valve[1])
    print("========")
################################################


#this fills valve[0] with True or False
#based on analyzing the switch case string first case if number or not
############################
#this controls calling numbers parser if True
#this controls calling words   parser if False
#this is in great_pumpkincat2.py
#cherry_pie outputs the expanded macros into cray[0]
	# this will convert macros if they exist and stringify
	#valve[0] contrains the result of test for number in first case line
	# so the result of the test in flow_valve_input is in valve[0]
	## this expands the macros if they exist then does stringify  may 26th testing
	##### this calls the preprocessor here ##########################
	#IF NUMBERS ARE DETECTED THEN PREPROCESSOR MACROS EXPANSION  IS CALLED
	# puts True or False into valve[0] added April 2nd, 2021
	                                   # ====== this is new may 26th, 2021 testing it
########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	mytrace('endswitch')# detects if numbers in cases then valve[0] = True (it checks first case)
	###################
	flow_valve_input(y)  #output to valve[0]  True or False             
	###################
	print("valve[0]=",valve[0])
	if valve[0] == True: #this means cases are numbers
		# does macro expansion of input switch case string stored into cray[0] 
		cherry_pie(y); y=None; del y; y = cray[0];   
		# also stringifies numbers ie: case 1:  becomes case "1":                             
		# calls parser
		show_tron_trace_path()
		return #stop it dead in it's tracks here ----
		#parser_mode_2(y)    
	else: # if numbers == False does words as strings
		# for production it would just call the parser and not call cherry_pie
		print("valve[0] == False thus do strings its words", valve[0])
		#print("valve[1]=",valve[1])
		#parser_mode_1(y)               #this calls parser() strings  above and passes in 
	




May 27th, 2021  7:20 pm California time
I separted macros in the prototype and realized I needed to finish the fallthru tumbler. I already had
it adding numbers while falling thru fallthus in each case. I fixed the math. So that works.
I then thought of how I have used fallthrus in switch cases in JavaScript and it's to build strings concatting.
So I now have concatting strings thru falling thru fallthrus between cases. That was relatively easy.

I will upload the macro expansion preprocessor file and then add it to the main file and upload that.
I will add the string concat tumbler and the math adder tumbler later depending on how things go.
I felt like I was done and realized fallthrus are used a lot to concat strings so I had put that off a while
and just modified the adder of numbers to adding strings.
The program just kept growing and blossoming. I never expected to make it this far because it was a nightmare to engineer.
I got really lucky through sheer persaverance and dedication.

targetlist=[]
targetlist.append(0)

#math demonstration adding numbers between cases using fallthru
############ sutter() ############## added may 27th
def sutter(x): #this should be 3
	print("targetlist[0]=",targetlist[0])
	print("SUTTER called with ",x)
	if targetlist[0] == 0: #first time thru
		#x =x + 1
		print('targetlist[0]',targetlist[0])
		
		x = str(x)
		targetlist[0] = x
		print(targetlist[0])
	else:   #already something in here
		#targetlist[0] = targetlist[0] + x
		#x =x + 1
		x = str(x)
		targetlist[0] = int(targetlist[0]) + int(x)
	print(targetlist[0])
	#return(x)
	
buildstringlist=[]
buildstringlist.append(0)
################################################
##### concatting a string in fallthrus in switch case
############ buildstring() ############## added may 27th
def buildstring(x): #this should be 3
	print("buildstring called with ",x)
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
		
targetlist[0] = 0
buildstringlist[0] = 0
	
sw ='''
	
	switch(exp) {
		case 'cholpolty':  
			print(\"burrito!\")
			print("bowl")
			print("lemonade")
			break
	
		
		case 'panda express':
			print('good food')
			print("in hollister ")
			sutter(2)
			buildstring('merry')
			print('BARK')
			fallthru
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			sutter(3) #this won't do anything until it is executed
			buildstring(' christmas')
			fallthru
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			sutter(7)
			buildstring(' and happy new year')
			
			
			
			
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)	


output
we are inside of switch now panda express
case = panda express
good food
in hollister 
targetlist[0]= 0
SUTTER called with  2
targetlist[0] 0
DING DONG  in first if of Sutter
2
2
buildstring called with  merry
merry
BARK
we are inside of switch now starbucks
case = starbucks
where is my mocha
and my sausage sandwich...
targetlist[0]= 2
SUTTER called with  3
5
buildstring called with   christmas
merry christmas
we are inside of switch now big testing
case = big testing
where is my mocha
and my sausage sandwich...
targetlist[0]= 5
SUTTER called with  7
12
buildstring called with   and happy new year
merry christmas and happy new year

final result=
result of sutter adding 12
result of buildstring concatting  merry christmas and happy new year

May 27th, 2021 4:51pm
Separated macros functions for preprocessor and reworked endswitch(). I will upload it tonight. 
So now by tonight numbers using macros to and thru will work.  case 1 thru 10:  and case 11 to 20:
It also means I can now do (soon)  when, unless, until in conditions just like in Lisp and CoffeeScript and Ocaml.

May 21st, 2021  9:47am
Yesterday the macros to and thru worked properly. will likely upload it this weekend.
So I am in the process of adding the macro expansion code to the main file likely this weekend.
This means that a switch case with numbers can look like this:  case 1 thru 20:   and also like this case 23 to 56:
And the stringifying works so it turns all numbers into strings which  then run through the string based parser.
Accidents in code are great learning experiences for finding a radical new way of doing soething. 

And just now I figured out how to do tumbler of either concatting strings or doing math using
the fallthru feature in the swith case just like the behavior in C with fallthrus and in JavaScript.
That was tricky. It took 30 minutes to solve. I put it off for months because I had no idea how to make
it work. Everything I tried failed and then I saw my fallthru and I thought, why not try a function
and it worked like a charm. Quite thrilling actually and a simple solution. Not obvious at first. Had a few Type errors that
through me off track but I got right back onto the track. I didn't think it would ever work and nearly gave up
but I knew people would complain if I couldn't perfectly duplicate the behavior of C and JavaScript Switch cases.

C constant case names have been solved. 
Oh, more news. I solved doing this type of case just like in C. 
Using CONSTANTS   so like this case TARGET:    and case LAKE_TAHOE:  which then I will just convert into strings
like what I wo with numbers. 




May 19th, 2021  10:46 pm California Time
I will put the methods and functions into a separate module tomorrow. I wanted to post a few of the methods
so that everyone knows it's real. I took the output from the macro expansion and used that generated switch string
as input in my working multiple switch file and it ran. Surreal.

Testing beta code of expansion of macros  in Blender and Tang before I make a separate module
for macros.
The most important main function that controls how the expansion works is this method.

########################################################
def convert_case_numbers_to_strings(): #onlky to be called for numbers at this point
	print("just starting convert_case_numbers_to_strings()")
	mytrace('convert_case_numbers_to_strings()')
	macro_found[0]== False  #starting default
	print("macro_found[0]=",macro_found[0]) #starting state of flag
	detect_if_thru_and_or_to_macros_exist()
	print("TESTING output of macro_found[0]",macro_found[0])
	if macro_found[0]== True:
		print("macro_found[0] = True")
	else:
		print("macro_found[0]== False")
	#endif
#################################################################
	print("============= here the flag for macros in use trigers if = to True ===")
	if macro_found[0] == True: #added May 17th 2021  this checks in the entire switch case string
		print("macro_found[0]== 'True'")
		global switchcasetester
		print("WE MADE IT TO HERE so we have positive identified a switch")
		make_list_of_lines_using_thru_macro()
		expand_thru_macro() #expands all of them 
		print("just a
