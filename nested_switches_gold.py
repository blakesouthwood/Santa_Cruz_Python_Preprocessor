#experimenting putting innerswitch
#### testing nested switches looking to do count of switches
#looking out how the code written by the user will look like
# indentation is key 
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
print("==========")
how_many_switches=tennis.count("switch")
how_many_end_switches=tennis.count("endswitch")
answer = how_many_switches- how_many_end_switches
print("answer of switch count=",answer)

print("the number of switches found in input string=",answer)
print("therefore it's answer ONE inner switch")
print("==========")

'''
def inner_switch():
    casetest1 = ['test5','test6']
    
    switch(x)                           #<<====== switch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
            print("yes it's one")
            break

        elif case  == "test2":
            print ("switch case behavior works in Python now!")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testing wow works on Sublime now Coooool...")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('none')
            break   
'''
###############
#################################
##     S W I T C H   C A S E   ##
#################################

###this is new testing  double level inner switch nested
#######################
### inner switch_3
#######################
### this is inner_switch()
def inner_switch_3(n): # is the test #test7 should be input
    print("=======inner_switch called==3==",n)
    casetest1 = ['test5','test6']
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
            #inner_switch_2('coffee')
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "mars":        #<<===== but later I will make it work using just fallthru()
            print ("flying toy helicopter")
            break

        elif case  == "test4":
            print ("testing wow works on Sublime now Coooool...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("CAFE BORRONE here")
            #######################
            inner_switch_3('mars')
            #######################
            break

    #default:
        else:
            print('None')
            break   
#####============================





###this is new testing  double level inner switch nested

#######################
### inner switch_2
#######################
### this is inner_switch()
def inner_switch_2(n): # is the test #test7 should be input
    print("=======inner_switch called===2=",n)
    casetest1 = ['test5','test6']
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
            #inner_switch_2('coffee')
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testing wow works on Sublime now Coooool...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("CAFE BORRONE here")
            #######################
            inner_switch_3('mars')
            ########################
            break
    #default:
        else:
            print('None')
            break   




#################################
# value you want to run thru switch case

global x
x = "one" #it was "one"              #<<=== x must be a string just as matching case == "string", 
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
tahoe=[]
tahoe.append(0)
# =======  main  ===================================
def real_main():
    testfunction(x)  #"one" is tested

victory=[]
victory.append(0)

#######################
### inner switch_1
#######################
### this is inner_switch()
def inner_switch_1(n): #test2 is the test
    print("=======inner_switch called==1==",n)
    casetest1 = ['test5','test6']
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
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testing wow works on Sublime now Coooool...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            inner_switch_2('test7')
            #######################
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





casetest1 =['google', 'fishfood', 'probability']

#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
# this is a function with a switch case
# which has a nested switch case within it inside of a function called inner_switch_1
# =======   testfunction    ========================
def testfunction(x):
    print("=== testfunction called with x====TESTING THIS JUNE 9th======= ",x)
    print('test function testing switch case behavior')
#this is the switch called 
# ========  switch case code =======================
    switch(x)                           #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("yes it's one")
            ######################
            inner_switch_1('test4') #force feeding it for testing switch case function actually 
            ######################
            print("output from innerswitch below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')

        elif case  == "word":
            print ("this is back in main switch now !")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "rudolph":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "phrase":
            print ("testing wow works on Sublime now Coooool...")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
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


# ====   end of switch case  ======================
#        end testfunction

if __name__ == "__main__":
    real_main()
  
 #should be called when it loads page so call real_main() 
  
    
 ###########
#real goto code
 #import web_pdb #; web_pdb.set_trace()
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
import sys
#import my_methods
import math

'''
from curses.ascii import CAN
from asyncore import loop
from setuptools.dist import sequence
from pip._vendor.pyparsing import WordStart, line
from test.test_getargs2 import PositionalOnlyAndKeywords_TestCase
from email._header_value_parser import Phrase
import string
from pkg_resources.extern import names
from tkinter.constants import TOP
from lib2to3.fixer_util import Number
from array import array
from cProfile import label
'''
#from curses.has_key import python
#from builtins import False
#from ctypes.wintypes import WORD
#conn.commit()
#conn.close()


'''

#switchcasesample = 
'''
# switch(grade) {  //notices is has the brace here starting the block
#      case 'A' :
#      get startswith("case") //that should work fine testing each line
#         printf("Excellent!\n" );
#        break;
#
#      case 'B' :
#      case 'C' :
#         printf("Well done\n" );
#         break;
#      case 'D' :
#        printf("You passed\n" );
#         break;
#      case 'F' :
#         printf("Better try again\n" );
#         break;
#      default :
#         printf("Invalid grade\n" );
#   }
'''


   
def gothedistance():
    print(switchcasesample)
    print("%% go the distance called")
    listnew= switchcasesample.split()

    print(listnew)
    for item in listnew:
        if item == "case":
            print("yes")

#gothedistance();







#         
#what if I append each line with \n

def testlines(x):  #how to determine number of lines in a string
    print("testlines comparing cases and breaks parser beginnings......")
    counter = 0
    secondcounter = 0
    print(x)
    #for item in stringtest:
    newlist=stringtest.split()
    print(newlist)
    #not using breaks just continue no else
    for item in newlist:  # will become:  loop thru newlist
        if item == "case": #this was teh bug the semilocon at end of word break;
            counter +=1
            continue
        #end if
    print("number of cases in string =", counter)
    print();

    for item in newlist:
        if item == "break;": #this was teh bug the semilocon at end of word break;
            print(newlist[secondcounter]) #get location of item in list
            #print("location of word break",sweet)
            secondcounter +=1
            continue
        #end if
    print("number of breaks in string =", secondcounter)
    print();

    if counter == secondcounter:
        print("cases and breaks  correspond together")
    else:
        print('cases and breaks not same number')
            #still need to check that a break precedes a case
    print()
    print("this is bullshit a tab is not the same as 4 spaces")
    print()
 # what I see is that th ehuman knowledge stays in my brain and
 # it needs to be in a knoweldgebase that I can search like my plum searcher


testlines(stringtest) #this calls it


#now test a return inside of a while true
#actaully break jumps out of a while true
# and return exits a function


##=============== testing theory here ==========
listtest =[]


#testing using return to bail from testing_switch function

def testing_switch(z): #simulating a switch
    print("TESTING SWITCH here ...")
    print("testing_switch called with 1 for z")
    while True:
        if z == "1":
            print("it is 1")
            listtest.append("goto Chilis")
            print(listtest)
            return; #this exists the testing_switch function
        elif z == "2":
            print("it is 2")
            break;
        elif z == "3":
            print("it is 3")
            break;
        else:
            print("none of the above")
            break;
         #default
    #end while true






def catcher_follows():
    #testing theory  this should create a flag for yes
    #or rather determine if the flag is true for goto
    #and snag the label destion such as chilis.
    flag = False;
    print("catcher_follows called")
    if listtest[0] != None:
        print("there is something here")
        stringtest = listtest[0];
        if stringtest.startswith("goto"):
            print("yes it starts with goto")
            print(listtest[0])
            print("where to goto",listtest[1])
            flag = True;
        else:
            print("nope it doesn't start with goto")
            print("THIS SHOULD NOT Be called")

    else: #means empty if reaches here
        print("there is nothing in it. ")
    #End of if not = None

    #this is now triggered if flag is true for goto
    if flag == True:
       print('the flag is true')
       #then I would dynamically put together goto label;
       #then I would call it - so it's called after switch
       goto(listtest[1]);
    else:
        print("the flag is false")



print("THIS IS WHERE THE TESTING ALPHA BEGINS")
testing_switch("1") #represnting switch case here
#so i drop out of the switch case and then test
#with catcher_follows to see if a goto was called and if so
#then trigger it with eval build it and then exec() to call it

catcher_follows() #this is calls flowing down after switch




def gofish(x):
    return int(math.sqrt(x))

a =gofish(100)
print(a)

# testing my parser turning a string into an ordered
# list so I can test juxtraposition

parsed_string = []

string_input = "what is this for phrase in valentines"
fun = string_input.split(" ") #separates by space
print("the new list = ",fun)

print("");
#see if I can teach it the word first
#which in this context will have to be a function
#testing returning the first word
def first(): #this is a function to grab the first word
    #print(fun[0]) # in the list that was just created; cool this lets me see what it sees
    return fun[0];

#we know it's a word so I don't need to say first_word
def last():
    #print (fun[-1])
    return fun[-1];

if first() == "what":
    print("what is the first word")
else:
    print("first word is not what")
#end if

 #list funcgions
 #first, rest, last
 #get last word in list
print("this should return the first word in the string")
print(first())
print("this should return the last word in the string")
print(last())


print("we are here now ...............")








'''

#################################
##     S W I T C H   C A S E   ##
#################################

# value you want to run thru switch case

#global x
#x = "strawberries" 
                           #<<=== x must be a string just as matching case == "string",
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
# =======  main  ===================================
def main():
    snowflakes('strawberries')

#casesList = ["one", "word", "rudolph", "snow", "google","fishfood", "probability", "22"]
#
#switch and fallthru will need to be imported methods

# =======  switch  =================================
def switch(x):
    print('\n');
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        x = str(x)
    global case
    case = x.lower()
   # print("inside entry point rabbit hole")
   #print("of switch case and case = ",x)

# =======   fallthru       =========================
def fallthru(y):
    eval("switch('" + y + "')")

 ############ these are new haven't tested them yet
 ##################################################
def jumpgoto(x):  #needs to be for label
    eval("mylistgoto.append("' + x +'")");

def getfromlist():
    print(mylistgoto[0])
    return mylistgoto[0];
#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
mylistgoto = [];









##################################################
###########################################

# =======   testfunction    ========================
def snowflakes(x):
    print('test function testing switch case behavior')

# ========  switch case code =======================
    print("testing SWITCH CASE upper normal code test:::");

    switch(x)             #<<====== switch() method is here
    while True:           #<==== infinite loop used for fall thru method

        if case == "one":  #as method case("one"): an inner function
            print("yes it's one")
            break

        elif case == "word":
            print ("switch case behavior works in Python now!")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
            #jumpgoto("rudolph")
                                        #<<===== currently it requires the next case match in quotes
        elif case == "rudolph":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")

            break

        elif case == "snow": #testing this one
            print("matching snow");
            print ("will it work");
            break
        #this is totally cool because case can be any item in the list
        elif case in ['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("coding")
            break

        elif case  == "22":
            print ("gui design")
            break

        #default

        else:
        #elif case not in casesList: #if the case word or phrase is not in list cases
            print("this is the normal code test not the lower one")
            print(" this is the NORMAL CODE sorry no matches for", case)
            break;
     #the while loop effectively ends the block of code
     #this is done by one line of white space and indentation

#end loop
#end switch
#snowflakes('snow');# testing this out

#####====================================================



#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========



'''














def thursday_fun():
    print("fun day in the rain today its raining")

thursday_fun();

#this is code not in a function
#this stirng is not in a function
#so the indentation was from the left margine


string1 = """
print("=== what we have here is a failure of communicate===")\n
print("I am inside of string1")\n
test = "one"\n
#spacer
if (test == "one"):\n
    print("easy now")\n
    print("this test is working!!")\n
else:\n
    print("not working darn")\n
"""

exec(string1); # what this does is run the string code in
               # the string above.

so_close = """
 case 'Oranges'  #first word and second word or phrase in quotes
 """

 #stick these in a list first and second so 0 and 1 position
#smart good thinking Southwood

def new_case(the_name):
    caseline = "if case == " + "'" + the_name + "'" + ':'
    print(caseline)
print("\n")
print("testing printing a line of a case condition\n")
new_case("Oranges")



  #how do I put a prefix in front of a string
  #then put " == " after case
  #   elif case  == "word":

  #I can use the input from a list with the case and word or phrase
"""
  and then use another list that I add to the front
  and then fill in the paramaters and append it
  in python
  insert() to the front of a list
  listename = []
  listename.append(whatever)
  """

 #def myreplace(string,,b):    #name of function bug spelling counts
 #  anewstring = string.replace(a,b)













def replace_casecode():    #name of function bug spelling counts
    print();
    print('test REPLACE A STRING replace default with else:')
    mystring = "funny coffee money good default"
    # Prints the string by replacing geeks by Geeks
    print("original =",mystring)
    weasel = mystring.replace(a,b)
    print("  weasel =", weasel)
    print();

##
case = "two"
x = case

#===================================
### HERE I AM EXECUTING THE SOON TO BE GENERATED DYNAMIC PYTHON CODE
## I STILL NEED TO ADD THE \t front of a line  AND /n appended to the end of line
#so I will be using fuzzy logic and flags
# thinking about this more seriously Monday  April 27th, 2020
# I hear a train in the distance whistling it's loud horn
#def substracttopdefinelines(stringer):
    #loop thru string
    #split() string at end of defines













def trynow():  #this is not being called == funny
    #this is after the macro expansion
    #this is after the indentation is added
    go_string = """
print("::::::::::::::::")\n
switch(x) \n
print("case =",case)\n
print("x =", x)\n

print("I am in this switch case test now")\n
while True:\n
\tif case  == "one":  #as method case("one"): an inner function\n
\t\tprint("yes it's one")\n
\t\tprint("jumpint out of switch case generated here for one ==")\n
\t\tbreak\n

\telif case  == "two":\n
\t\tprint ("switch case behavior works in Python now!")\n
\t\tprint("we have two chosen!!!")\n
\t\tprint("It should have chosen two from case above the string")\n
\t\tfallthru("three")\n

\telif case  == "three":\n
\t\tprint ("go three")\n
\t\tbreak\n

\telif case  == "four": \n
\t\tprint("matching snow")\n
\t\tprint ("will it work")\n
\t\tbreak\n
#testing this (I added this and forgot)
\telif case in ['five', 'six', 'seven']:\n
\t\tprint ("coding") \n
\t\tbreak\n

\telif case  == "eight":\n
\t\tprint ("the word eight was matched - good job")\n
\t\tbreak\n
\t#default\n
\telse:\n
\t\tprint("this is the generated else down below *** inside of test for two down below", case) \n
\t\tprint("this is the SHOULD BE BAD NEWS else inside of test for two down below", case) \n
\t\tprint("sorry no matches for", case) \n
\t\tprint("......the end")\n
\t\tbreak\n
"""
    #newstring = macros(go_string)
    #go_string = newstring;
    #needs to modify the go_string
    #do macros first
    # #define fudge with 'two":'
    #it can't execute it until the code is accurate

    print(go_string); #this shows the (sooon to be ) generated python source
   # second_gostring =substracttopdefinelines(go_string)
    exec(go_string); #this runs the code  executed and interpreted















smartlist=[]

def trucks():
    print("testing trucks,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    smartlist.append('buttefly')
    smartlist.append("bird")
    print("length of trucks list", len(smartlist))
    print(smartlist)
    print()

trucks();



###3==========================================================================
# testing goto here now for labels
#//============================================================================
listoflabelcallsinorder =[]

def switchy(x):
    print("SWITCHY CALLED called with",x)
    listoflabelcallsinorder.append(x)#this adds label switched to to list
    print("the length of calls = ",len(listoflabelcallsinorder))
    print('\n');
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        x = str(x)
    
    global label

    label = x.lower()
    print("label=",label)


   # print("inside entry point rabbit hole")
   #print("of switch case and case = ",x)
   #gotoflag = False; #default


# =======   jumpto       =========================
def jumpto(y):
    print('JUMPTO called',y)
    switchy(y)
   

def firstlabel():
    print("...burp....");


def secondlabel():
    print("..2a ........0second label called");
    print("testing this out some more")

memory_list = []; #global by being outside of methods

#this has to be after the body of switch case and goto triggered true
#and chosen labeland break from whiletrue

#==========================================
#   feed_goto()
#==========================================
def feed_goto(val): #if this is called switch already started need a bypass to hop directly to destination/catch dropopin
    print("feed_goto method called", val) 
    memory_list.append(val);
    memory_list.append('true');  #I need to put the flag value in list too
    print("feed_goto=memory_list",memory_list)
    return;



#==========================================
#   catch_dropping_goto()
#==========================================
def catch_dropping_goto():
    print("CATCH DROPPING GOTO method called=====")
    print("this is catch dropping goto method")
    print("memory_list=",memory_list)
    if memory_list[1]  == "true":  #I need to put the flag value in list too
     #   get value of label
        #c = get_destination_memory() #where to goto
        gohere = "'" + memory_list[0] + "'" #this holds labelname*

        dothis = eval('jumpto(gohere)')
        print(dothis)
        exec(str(dothis)) #the question is from outside switch
        #this now officially triggers the goto
        # we are now in the domain of the label switch
        #will the jumpto method work?
    else:
        print("flag = false")
        return; #meaning do nothing

#end of catch_dropping_goto()


#important design specs I dreamed up late last night
# Monday June 22, 2020
'''
#goto thinking
#switch case body for structure stripes
#start at top of flow down encounter a gotoand normally jump down to labelseveral gotos many paths
#feed goto where it says gotoafter end if switch and while tru loop 
#catch falling gotos method
#
#but if goto triggerd don't begn at startso 2nd specialswitch for goto redirects 
#that ouls solve problem
#and when elaving freed goto set to falsefor readaibliyt call it exit-goto
#
#to pass thru catch falling gotos beneath switch case block 
#will be set to false and if false pass through catch_falling_gotos
#
#the switch case behavior and appearnce 
#in C looks very different from C gotosC macrosand Lisp macros too
#I ahve the switch case figured out and good progress on the gotos working
#
#switch case fallthru() if no break
#mulitiplel cases figured out
#'''








#I think that what this is if jumping out of inner switch case
#I put the destination into memory in a list 
#and run a function after inner switch case if true then jumpto destination memory  list
#and if false do nothing, a simple filter and that way I can jump out of an inner switch
#case which is a trick, an illusion.


#putinto memory
#then catch it
############################ this is funnel after switch case
######### what this does is dynamically recreate goto
######### if goto flag = true and calls it as if it was
######### triggered within the body of the switch case itself
   #catch_dropping_goto()
    #if goto flag == True:  #I need to put the flag value in list too
     #   get value of label
     #   dothis =eval('jumpto(' + value + ')')
     #   exec(dothis)
    #else:
      #  return: #meaing do nothing

'''
#for ( ... ) { ...
#               if (disaster)
#                   goto error;
#} ...
#error:
#       /* clean up the mess */


#for (i = 0; i < n; i++) for (j = 0; j < m; j++)
#               if (a[i] == b[j])
#                   goto found;
#/* didn't find any common element */
#found:
#/* got one: a[i] == b[j] */
#'''



#turned off tahoe_goto_test to eliminate this being the bug

#tahoe_goto_test("test_inner_switch");  #here we go  - hang on
# this should call second and then first and then break out of infinite loop

def showpathitdid():
    return
    print("#####==SHOW PATH IT DID CALLED")
    length = len(listoflabelcallsinorder)
    print("number of labels jumpedto =",length)
    #print("path it took =", listoflabelcallsinorder)
    #print(listoflabelcallsinorder[0])
    thelength = len(listoflabelcallsinorder)
    for name in range(thelength):
        print(listoflabelcallsinorder[name])
    print("done printing dam list")

def make_it_so():
    print('testing if watch_cnn_now actually called or not')


#watch cnn now this is practicing with the real goto code.
#==========================================
#   watch_cnn_now()    I need to encase a switch case into a function for scope
# and so that I can use a return to jump out instantly from anywhere
# and I need to find my catchfallinggotos which is called immediately after
# switch case (oh idea called by switch case if flag says goto called

#==========================================
def watch_cnn_now(): #no argument for the goto labels to start
    return # so it does nothing junw 9th
    print("watch_CNN_now called .........***......testing this now ")
    make_it_so();
    x = "starter"
    #breakpoint() #testing this to see if it works
    print(x);
    print("inside of WATCH CNN NOW running");
    print()
    print(" --- watch_cnn_test() function ---")
    print()
    ##this is for making goto structure for labels
    ## and to use gotos
    ###############################################

   # print("switchy(x) here inside of another function watch_cnn_now")
   # print("I think that that is the bug I need a seperate switchy_name")
   #print("or what I could do is have a second variable for uniqueness")
   #rint("for a particular method that it's used in so it runs properly. ")
    print("x ====", x)
    switchy(x) #this is really switch(x)  #fake loop  where switch normally would be       #<<====== switch() method is here
    tester_counter = 0;
    while True:    #Actual outter loop              #<==== infinite loop used for fall thru method
    #infinite loop here for this to work
        tester_counter += 1;
        print("tester_counter=",tester_counter)
        #g = input("type a letter : ")
        #print(g) #this acts as my breakpoint so I can see a var value
        #i can rename this brkpnt()
 #this is "starter" which is the top of the function since this way it starts top down

        if label == "starter":  #as method case("one"): an inner function
            print("STARTER label just reached...........")
            print('starter worked... finally')
           # print("onea") in the coprocessor mode there is no starter label
           #print it is nonetheless used as a primer
            print('onea label entered')
            #firstlabel();
            print(' 1a == jumped up tpo')
            print("this jumped to label onea above it")
            print("counter thru loop =", tester_counter)
            #it's a string
            apple = "2"
            if apple == '1':
                jumpto("starfish") #this will say: goto blueberry;
                #print("this should not print anything")
            else:
                jumpto("dolphin")  #this will say: goto waterfall;
                #print("this should not be printed either")


            #jumpto("waterfall"); #notice no break; afterwards

        
        elif label == "waterfall":  # so if twoa is called it does it and jmps up to onea then breaks out
            print("WATERFALL label just reached...........")
            print('at waterfall label now in switch case for labels')
            print("============")
           # print ("goto label twoa behavior works in Python now!")
            #secondlabel();  #prints second label information
            print("$$ watefall ");
            list1 = ["snowing","wondering", "tennis"]
            print("counter thru loop =", tester_counter)

            print("list1[0] =",list1[0]);
            if list1[0] == "snowing":
                print("true")
                jumpto("threea");#this is a goto label test
            else:  #below was not called
                print("not jumping to threea failed")
                print("counter thru loopy =", tester_counter)
                jumpto("default"); #testing
                #break; #or break out with default
            #end if


            #end for loop
            #break;
            #print('do stuff here in second label')
            #jumpto("onea");
            #NORMAL SWITCH CASE CODE HERE SWITCH AND CASE AND ELSE: USED
            #don't use a break here
                  #goto "threea" label        #<<===== fallthru() method is here *don't use* break with fallthru()
            #can't use a break here
          #this is treated as a LABEL                                 #<<===== currently it requires the next case match in quotes
        
        elif label == "dolphin":
            print("dolphin label just reached.................")
            #put 'default' into destination list
            #jumpto("default")
            feed_goto("default") #puts data in list to access sets flag to true
            print("should leave switch case")
            break; #to get out of switch case
            #print("this will not print right?")
            #break;

            

        elif label == "threea":        #<<===== but later I will make it work using just fallthru()
            print("THREEA label just started.............");
            print ("$$ ==3a go threea")
            print("this jumped below it to threea")
           # print("we have successfully jumped out of SWITCH CASE")
            #jumpto("twoa")
            print("counter thru loop =", tester_counter)
            #break;  #necessary to leave the while True: infinite loop
            print("about to start nested loop test jumping")
            i = 1
            #counter = 0
            print("while loop and jumping out of it as a goto")
            print("this is inside of threea")
            print("doing loop here and jumping out ====")
            while i < 5: #this is definitely a loop
                i += 1;
                print('i =', i)
                if i == 2:
                    print("i = 2 now")
                    print("just before jumping to strawberry called with goto as jumpto")
                    jumpto("strawberry");
                    #print("now is the time to get the fly")
                    #don't put anything after the jumpto(word) because it's pointless 
                    #break;# to break out of this little while
                #if i == 3:
                #   print("i = 3 now")
                #jumpto("blueberry");



                            #goto blueberry;
                            #why did this work.

            #this will be at the bottom anyways
       
      
        
        elif label == "blueberry":
            print("BLUEBERRY label just reached.................")
            print("we are in blueberry from a loop ")
            x = 1
            while True:
                x += 1;
                if x == 3:
                    jumpto("default"); #and this is up above how interesting. 
                    #break;

            # print("just got visited by sheriff")
            break;  #to get out of the goto switch (this wasn't called so it does nothing)
        
        elif label == "strawberry":
            print("STRAWBERRY LABEL  just reached..................")
            print("strawberry here that I jumped to")
            print("so I jumped out of a while loop with goto to label below it")
            #jumpto('default');
            #break; #all impportant. I predict they will be back
            break;
            #what I learned is a break ends the whole goto assembly
            #and I can't have a break after jumpto(word) for some bizarre reason
        
        elif label == "starfish":
            print("STARFIX label just reached.................")
            x=25
            y=0
            while y < x:
                y+= 1
                print(y)
                if y == 10:

                    jumpto("default")
                    #thats the bug
            
            #print('do not print this')
            #break;


            


        elif label == "default":        #<<===== this will be invisible not visible.
            
            print()
            print("DEFAULT label just reached...................")
            #print("used goto to get here from three nested loops!!!!")
            print("@@ welcome to default land @@")
            print('successfully jumped to DEFAULT BABY')
            print("default triggered  to leave the function but no default label in reality")
            print("counter thru loop =", tester_counter)
            print();
            
            break;  #safety to end the while loop
          #there will be no unauthroized jumps

        else:
            print("else called the escape since a label was called........")
            break;  #maybe it needs this who knows
        #this is acting as just a jump table and there will be no default necessary
        #end of label switch case
    




#watch_cnn_now();
#print("burp test here")
#print(listoflabelcallsinorder)
#showpathitdid()

#scatch_dropping_goto()


#Bshowpathitdid();










'''
#output should look like this from above


'''























#============================
def replace_a_string(a,b):    #name of function bug spelling counts
    print("look at these two strings %%%%%%%%%%%%%")
    print("testing replacing a string so work on macros expansion")
    print();
    print('test REPLACE A STRING replace default with else:')
    mystring = "funny coffee money good default"
    # Prints the string by replacing geeks by Geeks
    print("original string=",mystring)
    weasel = mystring.replace(a,b) #this is creating a new string
    print("  weasel new string =", weasel)
    print();

#replace_a_string("default", "else:")





#working on appearance of C goto layout within a function
#==========================================================

#what it will look like but for loop and labels will need to be in triple string """
'''
#somethinglist = ['testing1','testing2','testing3','testing4']
#
#for item in somethinglist:
#    if item == "testing2":
#        goto error;        #C style  without braces                   
#    else:
#        print(item)
#
#error:
#    print("error label reached")
'''


#might need a second label to be directed to if not an error
#thatwould go after initial label block

#========================
 #in python it will look like this 
 #need starter label at top to start at beginning of the function 
 #and I will need to import methods switch(), jumpto(), feed_goto(), catch_dropping_goto(), switchy()
'''
if label == "starter": #so it starts at the top  by default possibly if label == starter and first = true
    for item in somethinglist:
        if item == "testing2":
             print("about to goto error label")
            jumpto("error")        #C style  without braces                   
        else:
            print(item)
'''
'''
if label == "error":
    print("error label reached")

'''



#  this will not be seen or interpreted by the
#  interpreter for python because it's not python code
#  it's javascript syntax code which it can't read
#  nor understand

#I will add breakpoint
#inner switch
# show code gen()
#to debug trace code path
#macros also fiddle around with those and do while and swap
#this will allow macros later on so the the first pass macros will be expanded

js_switch_string = """  //you can comment C style insde of it
var expr = 'oranges';  //you can use var if you want

switch (expr) {  //brace is optional /* this switch a function call that is imported */
  case 'oranges':
    print('Oranges are $0.59 a pound.'); //should return oranges
    break;          //breaks don't required the semicolon but it's okay to use
  case 'apples':
    print('Apples are $1.55 a pound.');
    break;
  case 'mangoes':
  case 'papayas':  //this works using in with Python
    print('Mangoes and papayas are $2.79 a pound.');
    # expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:   //must have a  default
    print('Sorry, we are out of ' + expr + '.');
    break;   //optional break but recommended
}   //optional pure taste  I like it with the brace actually.
"""

#print(js_switch_string) #this shows the C style switch case

#this is just playing
#a = 4
#b = 3
#
#testing genrating some switch code
#friday night 24th of april at garlic farm truck stop
def generate_pyswitch():
    var_one = '"one":'
    teststring = '''
    switch(x)

    while True:'''

    print("testing generating some simple switch code in python")
    print(teststring)
    badass ="        if case =="
    # x = badass.ljust(4)  # four spaces from left indentation
    #print(x)
    print(badass, var_one)
    print()

#generate_pyswitch(); #testing small parts of it right now

palomar = '''
words here
more words
case "onions":
print(' some words ');
print(' another day ');
break;
'''
##########@@@@@@@@@@@@@@@@@@@@@@@ THURSDAY CODING ###############
#CODING IN THE WOODS MAY 7TH IN THE SHADE OF REDWOODS
#thinkint or mqking a new string and building top down
# right now
#how do I grab what is in quotes
#at top look for switch(exp){
#at bottom of switch case look for } or endswitch








#============
def read_case_convert_to_if():
    print('read case convert to if')
    #get line( strg)
    #print(format.string.replacewhole line)
    #case 'oranges':
    #becomes "if case == "  + word + ":"
#determine number of lines between case and break for a case;

#determine if case on several lines before case not on a line
#determine if a break and what line Number
#determine if default word exists (it needs to exist)
#thursdady, may  7th take input the case 'word':
# and output if case == "theword":




def getword():
    print("called function getword()=======//===>>>")
    #txt = "case 'oranges:"
    txt = "case 'apples':"
    x = txt.split("'")
    print(x)
    print(x[1])
    fun = x[1];
    newfun = fun.rstrip(':')
    print(newfun)
    quote = '"'
    victory = "if case == "  + quote + newfun + quote + ":"
    print(victory)

#getword();

###########3==========================================

def count_lines(thestring):
    cool = len(thestring.split('\n'))
    txt = "the length is {} lines "
    print(txt.format(cool)) #this grabs text from above line
    #print("the string is",toosmart)

   # print(f'{cool} in {str}')
   # print("there are {0} lines in".format(count_lines(str),str))

firststring = "palomar"    #also I can reference it in a list
secondstring = "js_switch_string"




def felix():
    print('testing Manipulating Strings')
    thenumber = count_lines(palomar)
    print("name of the string is", firststring)
    print()
    thenumber = count_lines(js_switch_string)
    print("the name of the string is",secondstring)
    print()



    #test for default
    #test for at least one case (count them)

 #break it down into case sections












#count cases in the switch case string
def count_cases(stringname):
    print("count_cases function called")
    string_to_search = " case "
    list_of_results = []
    print("count_cases called")
    txt = stringname;
    #so I will have to use eval to dynamically insert it
    x = js_switch_string.count("case") #count case
    print("there are", x, "cases in ", stringname)

    print('the god damned linenumber that case is on ')
    matched_lines=[line for line in js_switch_string.split('\n') if "case" in line]
    print(matched_lines)
    linenumber = 0;
    for line in js_switch_string.split('\n'):
        linenumber +=1;
        if "case" in line:
            print("linenumber is", linenumber-1)
             #because the first line has nothing on it it's the quote


    #this regturns 3, , 6, 7 for line number of the actual cases that are each on only one line
    #and we know if the numbers are sequential
    #it means several cases for one condition
    #we know that the last line for a case is break
    #so we can get the line numbers
    #and we know that 5 is a break and 3 is case
    #so line 4 is the statement for first case starting on 3

    #now can I grab that line
    #so to grab line 4 it's really line 5 for it is +1
    #these are in the order of the cases top down
    #these are the lines after each case within a case body that have python code within them
    #I will need to create a variable to determine how many lines exist between cases
    #I will need to determine if cases arde sequential with no lines in between and how many cases

    avoid_list = ["case", "switch","break","default","const", "#"]
    end_matched_lines=[line for line in js_switch_string.split('\n') \
                       #if all(avoid_list) not in line ]
                       if "case"   not in line and \
                         "break"   not in line and \
                         "switch"  not in line and \
                         "default" not in line and \
                         "const"   not in line and \
                         "#"       not in line    ]


    #I want this to say "if all(avoid_list) not in line
    #  if foreach(item,avoid_list) not in line:


    print(end_matched_lines) # these returns the list of text

    #here I put the (fed) the lines for each case statements
    #into a list to access and reuse since they are in order

    output_list =[]
    for x  in range(len(end_matched_lines)):
        output_list.append(end_matched_lines[x])
        print(end_matched_lines[x])
    print("let's see the output_list[]")
    print("this is the list I can access now", output_list)
    print()
    for x in output_list:
        print(x)
    print("length of outpout list is = ", len(output_list))
    print(output_list[0])
    print(output_list[1])
         #last oen would be default
 ## Icouldf use my search for list of words in a string
 #that I wrote for mom's poetry that does words
 #and phrases to see if they exist within each poem
 #mom wantedto know if she used a phrase before
 #but I added that feature for a list of words




def candy(): #this worked it turned the string into a list
    print('candy called')
    #print(f'list of words={js_switch_string.split()}')
    cities = js_switch_string
    cool =cities.split(' ')
    print(cool)
    print()

#candy()

#felix()
#count_cases("js_switch_string")

#generate list for multiple cases to get something actually done today
'''elif case in ['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("coding")
            break
'''

   #in switch case instead of len(something) you can do something.length  just for the fuck of it
#def convert_C_multiple_cases_into_list():
 #   for each case line
    #I can make my foreach cooler too

# wednesday, April 29, 2020
# this will have to be generated during the parse to create this
# using append
cases_together=["google", "fishfood","probability"] #this is python mode
#I should do this for the parser than to
#go through grabbing cases that are together
#and buid the list that way.
# I was just going backwards


#this builds the list in python "in ["words", "words", "words"]
#got this working  april 29th, 2020
#need to check (count) number of cases grouped together

#test if cases on this line true or false
#test if cases ALSO on this line if true multiple
#test if cases ALSo on this third line mulitpe
#test if cases also on this fourth line multiple
#test if cases also on this line
#test test for when there isn't a case on a line after first line with case



















def multiple_cases_scenario(cases_together):
    print("?????multiple cases scearnio to build list")
    # this will actually be used in parsing to create python
    # version of the multiple cases that works in python
    # when I do the parse I will buid this list and then reuse
    # that's much simpler

    # get length of list
    casestogetherlength = len(cases_together)
    # loop thru list
    # append cases names

    makelist = " in ["
    count = 0;
    quote = "'"
    cool = "" #starts with nothing in it
    cool + quote;
    for item in cases_together:
        sweet = item #one word from list
        #print(sweet)

        #count += 1;
        if count != len(cases_together):
            cool += sweet + quote #+ ",";
        if count != len(cases_together): #this is new now
            cool += ",";

        count += 1;
        print('cool sees ',cool)
        if count != len(cases_together):
            cool + ",";
            print("now cools sees", cool)

        #if count == len(cases_together):
        if count !=  len(cases_together):
            cool += quote;

        if count < len(cases_together):
           cool + ",";
        else:
            break;
             #builds list line ['word','word','word']
        #for coolneess you can  use count++  which just looks better and more natural
    print("cool =",cool)
    print("the count is", count)
    #print("cool =", cool)
    print("wild cool ",cool)
    cool = cool[:-1] #this removes the last char of string which fixes a bug I had
    tail = cool + "]" #line above worked great so nonobvious
    print("tail =",tail)
    build_it = makelist + quote + tail
    

    print("BIGGIE test here ")
    print(build_it) #to see what it sees and if it actually works (so doublful but laughable)
    print()
    print()

# creates a list  "in ["casename","casename", etc ]
# do a loop to count cases
#multiple_cases_scenario(cases_together); #this calls it












  #============================
def replace_a_string(a,b):    #name of function bug spelling counts
    print("...............testing replacing a string so work on macros expansion")
    print();
    print('test REPLACE A STRING replace default with else:')
    mystring = "FOR_ALL we know this will work"
    # Prints the string by replacing geeks by Geeks
    print("original =",mystring)
    weasel = mystring.replace(a,b)
    print("  weasel =", weasel)
    print();
#so the first word needs to be in there  the string
#replace_a_string("FOR_ALL","for(i = 0; i < ARRAY_SIZE; i++)")








macro1 = '''  #because this must remain untouched,
              I could have it skip first occurrence

    #define FOR_ALL  for(i = 0; i < ARRAY_SIZE; i++) '''

now = '''
    #and use it like this:
    #/* Clear the array :this will be the first phrase to test*/

    FOR_ALL {
      data[i] = 0;
    }
    '''
    #when the code executes it will ignore the lines with #
    #the issue is that I need the executing code
#concat macro list to codelist and run it as preprocessor
#define macro expansion
#define macro expansion

#just realized the macros will only work in triple strings

testmacro = '''
   #define FOR_ALL  for(i = 0; i < ARRAY_SIZE; i++) {
   #define CHEESE   print('have some cheese');

   def fakecode():
       print('something')  
       FOR_ALL
       do this loop
         if amount < 100:
             CHEESE

   '''

   #steps
   # '''I could split off the defines at TOP so two strings and only using below it
   #run the replace on existing  bottom half string so it doesn't see the defines at top
   #for the replace it uses the top defines string - brilliant
   #
   #loop thru string replacing the lines on bottom
   #then connect the fist string to the resulting string
   #'''
             #may 4th DESIGNING MACRO SWAPPING BEHAVIOR
'''
def macro_expand():
    count how many define macros
    put line into string
    check if #define startswith()
    if true search switch case for word and return codephrase string
    else
    break;
     go thru string of code with loop
    search each line for macrophrase
    if found replace
   '''













'''



word_list =["case", "break", "switch", "default", "const", "#"]
def cottoncandy():
    print("cotton candy called to see if several words in string")
     #just loop thru a list
    counter = 0
    print(js_switch_string)
    #start loop
    for word in word_list:  #attempting a macro now maybe later
        counter += 1
        print(word) #this prints out the word in list on each loop
        #now I have to modify this to search for all words on each line
        if word in js_switch_string:
            print("yep", word)
        else:
            print("nope")
    #end loop

cottoncandy();

def rockyroad():
    print("testing rockyroad string manipulations")
    stringtime = "testing this out"
    stringtwotime = "not testing this out"
    weird = stringtime + "*" + stringtwotime;
    print("weird=",weird)

rockyroad();



if __name__ == "__main__":
    main()
'''

#paul graham the 100 year language - reffering to a programming language in the future

#April 2003




