import official_switch_case_silver
from official_switch_case_silver  import *  

# I like this idea cond_case value1= 3 and value2 = 5
#rather than just regular case
# cond_case  startswith('a'):
# cond_case if 'feb' and is_leap_year();
# cond_case  ['peach' or 'pear' or 'plum']:
# cond_case  2_values['winter','night']: 
###################
##    swap(a,b)
###################
def swap(a,b,c): #c = starbucks[1]
    cooler =c.replace(a,b)
    return cooler #starbucks[1] =string with changes made
    
    
#clever("big bird")
#for this test nested needs to be False so it prints the output
nested_switch[0]= True #means it's nested so generate string don't execuite it
show_input_switch_string()   #input so what the string right below here
show_generated_code()

print("testing with corona test string which is a working switch case")
corona=''' 
	switch(exp) {
		case 'fishy':  
		case 'two da':
		case 'three da':
			print(\"squirt gun!\")
			print("water everywhere")
			break
			
		case 'big bird':
			print("now is the time for ")
			print("all great women, yeah, right")
			print("to come to the aid of their country..nver")
			break
			
		case 'Israel canal':
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
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

#endswitch(corona)
print('the output from this translation is here')
print(sweet)
eagle=[]
eagle.append(sweet)
print(eagle[0])
#I am going to get the translation
#wait what if I don't execute it and just get what's in sweet.
#this creates this generated code 
#again this is corona output of the generated python code as regular switch
output='''
exp = varholder[0]

caselist1 = ['fishy', 'two da', 'three da']
caselist2 = ['big bird']
caselist3 = ['israel canal']
caselist4 = ['ufos are real']
caselist5 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['fishy', 'two da', 'three da']
		print("squirt gun!")
		print("water everywhere")
		break

	elif case in caselist2: # ['big bird']
		print("now is the time for ")
		print("all great women, yeah, right")
		print("to come to the aid of their country..nver")
		break

	elif case in caselist3: # ['israel canal']
		print("massive ship blocking canal in Egypt")
		print("it was stuck for six days")
		fallthru('ufos are real')

	elif case in caselist4: # ['ufos are real']
		print('manure')
		print("no more horses")
		break

	elif case in caselist5: # ['default']
		print('one walking quack d')
		print("walking geese")
		break

	else:
		print('one walking quack d')
		print("walking geese")
		break



'''

print("this is what we are testing today Friday to see if it works right adding a tab")
print("===========")
print("  == friday july 2nd testing this already coded previously ===")
print("this is the generated output of python for the test switch case")
print(output)
print("now I will add one tab to the front of each line")
#June 22, 2021 adding tabs to put this into a method 
#let's see if this moves the whole string over by one tab
#print("number of tabs =",sowhat)
    #print(ufo) #just to test this 
print("big test here =====------0000000000000========00000000=====00000000000")
print("STAGE ONE add tab to front of each line")
#this indents the whole string by one tab on each line 
print(" Adding 1 tab to front of each line in switch case output ")
print("simpe and effective does this swap work or not")
print('replacing switch with inswitch')
print('replacing fallthru with infallthru')
#pure genius
address = "_5" #this is for test purposes since this will be dynamic
solution=[]
solution.append(address)


x = output.replace("exp = varholder[0]", "def nested_switch" + solution[0] +  "(x):\nexp = varholder[0]")
output = x

x = output.replace("switch(exp)", "inswitch(exp)")
output = x
x=''
x = output.replace("fallthru", "infallthru")
output = x
print(output)
################# this iwhere I add one tab to front of each line ############
# this adds one tab to the front of each line in the string 
# so it's adding \t (one tab)
print("CRITICAL OUTPUT HERE........")
noway=''
counter=0
for line in output.splitlines(): 
    counter += 1
    if line.startswith("def"): #this looks if first line doesn't add tab
        #print("YES starting with def",counter)
        noway = line #it does nothing to the line
    else:
        noway = "\t" + line
    print(noway)
print("next stage here ======---------=======")
print(noway)
print("will this every dam work") 

#exit()
#def add in to front of switch and fallthru()

#x = txt.lstrip()
  
 ###pehraps left strip of line for first line only 
           
#chomp off first char of line 1
 #this is good now just change the first line the rest is perfect

print("==== big test to del tab at front of just hte first line")
#Wait what if I replace

 
 
    #if line.startswith("switch"):
    #now print the whole thing
print("44444444444444444444444=========")

#newlist=[noway]
########################################
print("end of adding one tab to front")
########################################
print("====0===9===8==7==6==5==4==3===3==2==1===")
print("now to add method to top")




#x = output.replace("switch(exp)", "inswitch(exp)")
#noway = x;

print(noway)
##########################################
print("done swapping inswitch for switch")
##########################################
    #if line.startswith("switch"):
    #now print the whole thing




print("========and now for something really cool= replace======")
txt = '''I like fallthru bananas and green egss and ham 
more starbucks coffee and switch is the answer'''

x = txt.replace("switch", "inswitch")
txt = x
z = txt.replace("fallthru", "infallthru")
print(z)



###########
print("attempting swapping switch and fallthru to prepare for nested switches")
print("=========")
#print("STAGE TWO SWAPPING  switch and fallthru but change nothing else")
#for line in output.splitlines(): 
#    if line.startswith('switch(exp)'):
#        print("line starting with switch detected")
#        x = line.replace("switch(exp)","inswitch(exp)")
#        print(line)
#        line = x
#    if line.startswith('fallthru'):
#        print("line starting with fallthru detected")
#        y = line.replace("fallthru","infallthru")
#        line = y
#    #if line.startswith("switch"):
#    #now print the whole thing
#print(noway)


#x =noway.replace("switch(exp)", "inswitch(exp)")
#print(x)
#noway =''
#noway = None
#del noway
#noway = x
#print(noway)
print("did it work or not")
print("=================zzzzzzzz======")

txt = noway
x = txt.replace("switch(exp)", "inswitch(exp)")
noway = x
print("noway=",noway)


#print("testing ======replace ")
#txt = "I like bananas"
#x = txt.replace("bananas", "apples")
#print(x)

#add inswitch and infallthru now ==========================
#noway1=swap('switch(exp)', 'inswitch(exp)',tacobell[1])
#print(noway1)
#print("what is above this line did it change the words or not")






'''
noway1=swap('switch(n)', 'inswitch(n)\t',tacobell[1])
print(noway1)
tacobell[1] = noway1
print("this should have one change")
print(tacobell[1])
noway2=swap('fallthru(', 'infallthru(',tacobell[1])
tacobell[1] = noway2
print("this should have two changes")
print(noway2)
'''

print(" ====== end of adding one tab to the front of each line ======")
#Here I will change swith to inswitch and fallthru to infallthru
#I will need to add the method name at the top
#and the inswitch method and infallthru method
#and add one tab or more to each line and put everything into one string


print("== MAX HEADROOM IT SHOULD ALL BE OVER NOW===")

rawcode='''

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
# looking at what is different from the regular switch 
# what is differnet is the nested switch is inside of a function
# and instead of switch it's called inswitch(n)
# instead of fallthru('something') it's infallthru('test2')
# if missing break it's infallthru('nextcase')

def inner_switch_1(n): #test2 is the test
	print("=======inner_switch called==1==",n)
	caselist1 =['testa']
    caselist2= ['testb']
    caselist3= ['testc']
    caselist4= ['testd']
    caselist5= ['google', 'fishfood', 'probability']
    caselist6= ['testf']
	#this is switch inside of inner_switch

	inswitch(n)                           #<<====== inswitch() method is here

	while True:                  #<==== infinite loop used for fall thru method
		if case in caselist1: #['testa']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			infallthru('test2')

		elif case in caselist2: #['testb']
			print("this is inside of inners witch test2")
			
			print ("switch case behavior works in Python now!")
			break         #<<===== fallthru() method is here *don't use* break with fallthru()
			#<<===== currently it requires the next case match in quotes 
		elif case in caselist3: #['testc']       #<<===== but later I will make it work using just fallthru()
			print ("go reindeer")
			break

       elif case in caselist4: #['testd']:
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in casetest5: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case in casetest6: #['testf']
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
    
    
    inswitch(n)                           #<<====== inswitch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
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





casetest1 =['google', 'fishfood', 'probability']

#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
# this is a function with a switch case
# which has a nested switch case within it inside of a function called inner_switch_1
# =======   testfunction    ========================
def testfunction(x):
    print("=== testfunction called with x====TESTING THIS JUNE 9th======= ",x)
    print('test function testing switch case behavior')

# ========  switch case code =======================
'''

#june 15th designing and thinking this out 
#get line number of each nested switch starting line where I will insert the method inswitch
#pretend this is an input s witch 



#need to get information from this

ufo ='''
	switch(x) {                        
		case "one":
			print("this is the first case in the main ")
			###### nested inner  1 ##############
			switch(n) #nested sw 1   
				case "testa":
					print("dam did it work?")
					print("yes it's test == one")
					tahoe[0]='victory' 
					fallthru

				case "testb":
					print("this is inside of inners  test2")
					print(" n now!")
					fallthru        

				case "testc":        
					print ("go reindeer")
					break

				case "testd":
					print ("testi  first nested  ol...")
					tahoe[0]="sublime" #puts victory into tahoe[0]
				default:
					print("out of inner switch 1")
					break
			} #endswitch
			####### line below end sw #################################
			print("out of inner switch 1")
			fallthru


		case 'google', 'fishfood', 'probability':
			print ("successful test in casetest1")       
			print("tahoe[0]=",tahoe[0]) #result of  running
			#what output is there from?? use a list to capture it
			fallthru

		case "word":
			print ("this is back in main now !")
			fallthru        
			                            
		case "rudolph":       
			print ("go reindeer")
			print("=== this is 2nd ne

		case "test7":
			print ("gui design")
		###### nested inner 2 ##############
			switch(n) {# nested sw 2             
				case "testa":
					print("second did it work?")
					print("yes it's test == one")
					tahoe[0]="victory" #puts victory into tahoe[0]
					fallthru

				case "snowmanb":	
					print("this is witch test2")
					print (" casethon now!")
					fallthru        

				case "testc":       
					print ("go reindeer")
					break
			
				case "rabbitd":
					print ("te what do we have here ool...")
					tahoe[0]="mickey mouse" 
					print("tahoe[0]",tahoe[0])
					fallthru

				default2:
					print('None')
					break   
				
			} #endswitch  #this should be the bottom  insanely cool
			print("out of  2")
			break
		########################===================
		 
		 case "trouble":
			print("ufo report damning")
			print("coverup")
			break
		default:
			print("sorry no matches")
			break
			  
	}endswitch
'''


switchlinenumber=[]
switch_lines=[]
switch_lines.append('0')
actualendswitch=[]
endswitchlinenumber=[]
#addit=[]
#totalswitches=0
dragon=[]
snowfall=[]
##########################
##    testing_this()
##########################


### what I did June 15th was swap out switch with inswitch and fallthru with infallthru
### which I did prematurely it will actually happen later in the process

def testing_this():
    print('testing this to count tabs now too')
    global ufo
    addit=[]
    #print(ufo)
    global totalswitches
    counter=0
    ##################
    smart =ufo.count("switch(") #so smart
    print("total number of switches=",smart)
    nice =ufo.count("endswitch")
    print("total number of endswitches=",nice)
    ###$##############
    print("=======")#this goes thru the string and detects a nested switch
    for line in ufo.splitlines():    #and copies it and puts it into 
        counter += 1    #acgtaully it gets the start and stop location line numbers
        #print(line," ",counter)
        
        if "switch(" in line and "end" not in line: #differentiate from endswitch
            #totalswitches += 1
            print("=== switch found ===")
            #starting number of nested switch is put into dragon[0]
            dragon.append(counter)
            print("dragon=",dragon)
        ######## this is new june 21st 2021 counting tabs in lines     
        if "\t" in line:
            print(line)
            print("_________________")
            print("tab found")
            print("line number =",counter)
            trouble =line.count("\t")
            print("tab numbers",trouble)
            
        if "endswitch" in line or "}"  in line: #why {
            print("==end switch found==",counter)
            #last number of end switch is put into snowfall[0]
            snowfall.append(counter)
            print("snowfall=",snowfall)

       # if "}" in line:
       #     print("this is the end of the main switch")
       #     actualendswitch.append(counter)
       #     print("snowfall=",actualendswitch)
       
    print('number of switch =',smart)
    print("number of endswitch=",nice)
    print("lines with switch =",dragon)  
    del dragon[0] #deletes first counter in list
    print("these have to be nested switches",dragon)
    #delete first switch line number which is the main switch  
    print("lines with endswitch =",snowfall)  
    del snowfall[-1]  #delete last counter in list
    print("lines with endswitch =",snowfall)  
    print("=== actual nested switches ====")
    print("nested switch starting switch()",dragon)
    print("nested switchs  endswitch locations =",snowfall) 
    #################==============
    print("first nested switch=",dragon[0],",",snowfall[0])  #first  nested switch
    print("second nested switch=",dragon[1],",",snowfall[1]) #second nested switch
    ######====================================
    # Next steps for Tuesday coding
    #copy starting line of switch to end of endswitch
    #use a loop and then store it in switch_string_list
    #then change fallthrus and the switch name to nested variants
    #then add function name to top of this new string
    
#testing_this() 







##COPY NESTED SWITCH 
#used to concat the nested switch string initialization
############################## june 15th 
##  copy_nested_switch
############################## #this is copying string of nested switch inside of main switch

def copy_nested_switch(x,y): #input of start and stop params
    print("x and y",x," ",y)
    mycounter=0
    newstring='' 
    outputstring=''
    #print(ufo) #just to test this 
    for line in ufo.splitlines(): 
        #what this does is loop thru the input string based on
        # the coordinatesa of where one set of x and y switch and endswitch are provied
        # by x and y
        if (mycounter >= x-1) and (mycounter <= y-1):
            newstring += line + "\n" #see if this works
            mycounter += 1   
            continue
        else:
            mycounter += 1   
            
    print("mycounter =",mycounter)       
    
    outputstring = newstring
    #print(newstring)
    print("this is what has been copied for the inner switch string")
    print(outputstring)
    print("end of copying a small nested switch from inside of a main switch")
    #the result of the input numbers and loping thru ufo string is putting
    #the resulting true nested switch into outputstring which is returned
    # like this   something=copy_nested_switch(x,y)
    return outputstring  #so I can put it into a list


# I get the range starting of nested switch and endswitch line numbers
# which I used to grab and copy the nested switch string into starbucks[1] for first and starbucks[2] for second
                  
starbucks=[] 
starbucks.append("starter")                    
a = dragon[0]
b = snowfall[0] 
print("the first nested switch contents")
funny =copy_nested_switch(a,b)  #based on coodinates gleaned above 
#print(funny) 
starbucks.append(funny)  
     
print("here we go ====")
#So this is starbucks[1] has the raw input string of Javascript switch case string





a = dragon[1]
b = snowfall[1] 
print("the SECOND nested switch contents")
funny =copy_nested_switch(a,b) 
#print(funny)   
starbucks.append(funny)             
   # first switch is the main by design
   # all following switches in the switch string MUST be nested switches
   # next is the depth of the switches #determined by tabs          
            
print("=========== these are the INPUT STRINGS of the nested switches ===")
print("they have NOT been translated into python yet....")
print("this is what is inside of starbucks list the two nested switch cases")
print('starbucks[1] which is the first nested switch')            
print(starbucks[1])
#print("divider insid eof starbucks list")
#print('starbucks[2]which is the second nested switc')   
print(starbucks[2])

print("RIGHT HERE THE RIGHT STUFF TRANSLATE THE SWITCH BUT DON'T RUN IT")
print("========== translate input to python string don't execute it ===")

######################
#saturay june 19th, 2021 testing to get this finally working
# alpha testing 
#I will now convert this to python and look at the output

def replace_endswitch():
    print("======trying to do replace_endswitch()======")
    goforgold= starbucks[1]
    #I need to comment out endswitch with #
    goforgold.replace("endswitch", "} #end") #this should work 
    sw = goforgold
    print("content of input string switch to verify it")
    print(sw)

#this should do this swap of endswitch and } for starbucks[1]
replace_endswitch() #code is just above this line
starbucks[1] = sw
print(starbucks[1])


#set the nested switch 
#this should set it
#this should set the codegen to create sweet put into tahoetest[0]
# but not to execute it 


##########################
nested_switch[0]= True #means it's nested so generate string don't execuite it
endswitch(sw)
print(sweet)

sw = starbucks[1]
print(sw) #to see what it sees


 #this parses and generated the python string
#print("the output string =",tahoetest[0])







#this creats the string in theory
print('so the output python should be just above this line')



#print(tahoetest[1]) #but don't execute it
#coolhandluke = tahoetest[1]
#clever("test1")
#exec(coolhandluke)
print("end of this test======0=0=0=0=0=0=0=00=")
#this is the generated switch in python now.
#But is need to change it to put it into a function
#and change switch to inswitch and fallthru to infallthru
#and put it into a method and call it too.

print("====testing the output python code to see if it runs")
#clever('test3')
#exec(tahoetest[0])




#===========================
# it would look like this
# swap('endswitch', 'goteamnow',starbucks[1])
#not turned on yet

# I am here right now ====
# I need to  convert the switch input string into python
# and then add a tab or two tabs to the front of each line3
# and then add the method name at the top






#############################################    
print("this phase will be done AFTER the switch string is translated into python")   
print("now for some gymanastics...using swap method to swap out") #THESE BOTH WORK
print("switch with inswitch and fallthru to infallthru and endswitch for fun")
# I was able to change switch and fallthru method names 
print("testingwith starbucks[1] changing switch to inswitch(n)")
#fool = starbucks[1]
#print("fool=\n",fool)

# I previously used a swap to swap numbers this one is described
# as swap but it's strings and not numbers that are being swapped in a string
#sweet =fool.replace('switch(n)', 'inswitch(n)')
##=========================
#### using swap method here 
##===========================
#I won't  do this till after I get the generated output string of python
'''
print("testing swap() method here to save time and simplify----- ")

starbucks[1]=swap('switch(n)', 'inswitch(n)\t',starbucks[1])
starbucks[1]=swap('fallthru(', 'infallthru(',starbucks[1])
starbucks[1]=swap('endswitch', '#end_nested_switch ',starbucks[1])
print("THIS IS TESTING THE SWAP FUNCTION HIDDEN IN THE BACKGROUND COOL")
print("=== will it actually work???====")
print("final test of what changes were now completed with starbucks[1]")
print(starbucks[1])

print("now with starbucks[2]")
starbucks[2]=swap('switch(n)', 'inswitch(n)\t"',starbucks[2])
starbucks[2]=swap('fallthru(', 'infallthru(',starbucks[2])
starbucks[2]=swap('endswitch', '#end_nested_switch',starbucks[2])
print("final test of what changes were now completed with starbucks[2]")
print(starbucks[2])
'''




string_methods='''
#==================
#for inswitch
def inswitch(n):
    if type(x) != str:  
        n = str(n)
    global case
    case = n.lower() 

#=====================
# for infallthru    
def infallthru(n):
    eval("inswitch('" + n + "')")

tahoe=[]
tahoe.append(0)

victory=[]
victory.append(0)
'''

dummy_switchcase='''
this would be the switch case python
that is here"

#at this stage I can replace the switch to inswitch
adn fallthru to infallthru

'''


building_string_nested_function=[]
building_string_nested_function.append(0)
## june 15th
##adding function name and then concat nested switch to it
 #THIS BUILDS THE INNER SWITCH FUNCTION WITH A NUMBER
 
 
#############################################################
## new_nested_function(g,h) this creates numerical custom def inner_switch_x(n)
#############################################################
def new_nested_function(g,h): #which nested switch do I add
    print("creating a nested function")
    first_string= "def inner_switch_" + str(g) + "(n):\n " + "\t" + str(h)
    #next add the nested switch (which is numbered by sequence)
    print(first_string)
    building_string_nested_function.append(first_string) #position 1 
    building_string_nested_function.append(string_methods) #position 2 
    building_string_nested_function.append(dummy_switchcase) #position 3 


    
################## june 15th discovery ###
#it has indented too far to the right so I need to align it all to the
# left and then add tabs to correct the indentation
# for testing   
print('==first nested switch==red alert test here ==============')
print('==first nested switch==red alert test here ==============')
print('==first nested switch==red alert test here ==============')
print('==first nested switch==red alert test here ==============')
print('==first nested switch==red alert test here ==============')

new_nested_function(1,starbucks[1])
casper = building_string_nested_function[1]
print("DAZZZLE DAZZZLE DAZZZLE DAZZZLE DAZZZLE DAZZZLE DAZZZLE DAZZZLE ")
s=''
for line in casper.splitlines(): 
    #what this does is loop thru the input string based on
    # the coordinatesa of where one set of x and y switch and endswitch are provied
    # by x and y
    if "inswitch" in line:
        dazzle =line.count("\t")
        #next how to remove some of the tabs
        print("==========......=============")
        print("tab count in inswitch line",dazzle)
        print("==========......=============")
        #s = line
        line = line[2:] #maybe this is needed THIS WORKED
       
        maybe =line.count("\t")
        print("the count of tabs is now after chopping off a tab",maybe)
        print("it should have JUST happened chopping off a tab")
        break
 #now this attempt
building_string_nested_function[1]=casper
print("now ATTEMPTING to see if I successfully subtracted ONE TAB before inswitch")
santacruz=building_string_nested_function[1]
santacruz =santacruz.replace("\t","") #removing the tabs for the whole string
building_string_nested_function[1]=santacruz

print("AFTER after after testing this to see if it works....")
print(building_string_nested_function[1])           
#count tabs before inswitch
print(".....,,.,.,.,.,.,,/,.,/,.,/,.,.,.,.,.")
print("=====maybe I need to remove ALL TABS and then insert them manually=====")

print("########what does the output look like here???======")
print(building_string_nested_function[1])
print("END of  building_string_nested_function[1] =========")

print("this is where the string methods of the switch actually start...")
print(building_string_nested_function[2])
print(" end of the contesnts of the string methods switch and fallthru")
print("start of teh actual python code here starts here")
print(building_string_nested_function[3])

print("===== end of critical red alert test =========")
print("===== end of critical red alert test =========")
print("===== end of critical red alert test =========")
print("===== end of critical red alert test =========")
print("===== end of critical red alert test =========")



print('== second nested switch==')
new_nested_function(2,starbucks[2])    
# need a swap which is replace which I will make a method called swap
# wow, it's not just the word switch its the entire nested switch string
# which will end seveal lines down with 
# endswitch
answer = starbucks[2]
sowhat =answer.count("\t")
print("number of tabs =",sowhat)
    #print(ufo) #just to test this 
for line in answer.splitlines(): 
     #what this does is loop thru the input string based on
     # the coordinatesa of where one set of x and y switch and endswitch are provied
    # by x and y
    if "\t" in line:
        lovely=line.count('\t')
        print("number of tabs in line",lovely)
        #line.replace("\t","")
        continue
    else:
        continue
print(answer)
coolness = answer.count("\t")
print(coolness)       








### experimental adding tabs to the front right now not working right 
# june 15th coding experimental 
#inputstring.replace("switch(input)", "inner_switch_1('test4')")
fox=''
####### formal to left 

def formal_to_left(n):
    global fox
    print("formal_to_left test getting rid of tabs at front")
    print(">>>>>>>>>")
    print("=========")
    #go thru string move everything to left
    for line in starbucks[1].splitlines():
        print(line)
        mylist = line.split()
       # print(mylist)
        new_string = " ".join(mylist)
        print(new_string)
        fox += new_string + "\n"
    print("what does it look like now..... Tuesday")
    print(fox)
    
    for line in fox.splitlines():
        if line.startswith("inswitch"):
            line = "/t" + line       
            print(line)
            
            
############# if figured out how to remove tabs from the front of lines#####
#####################################################
print("what this does is CHOP off 1 tab from each line")
print("==========try this ==========================")
# oh yea have tabs[1] means 1 tab and tabs[2] means 2 tabs
#and then add those to the front of lines and create a new string that way
# I might just remove all of them and add the tabs[2] etc to each line
#which is obvious based on what the first word starts with 
#have 
s = "\thello\n"
print(s)
if s[0] == '\t':
    print('why yes it is a TAB at the front')
    s=s[1:]
    print(s)
            
formal_to_left(starbucks[1])


print('testing this now on a piano bench....')
notyet=starbucks[1]
print(notyet)
#inputstring.replace("fallthru('test2'),   "infallthru('test2')"
#actually just add "in" to front of "fallthru")

##===============
## june 17th coding test 
##################
##     tabs(x)
##################
def tabs(x):
	print("x =",x)
	if x == 0:
		return ''
	elif x == 1:
		return "\t"
	elif x == 2:
		return "\t\t"
	elif x == 3:
		return "\t\t\t"
	elif x == 4:
		return "\t\t\t\t"
	elif x == 5:
		return "\t\t\t\t\t"
##=============================




def test_tabs():
	print("======== practicing inserting tabs at will====")        
	print("we see " + tabs(2) + "more words")
	print(tabs(0) + "howdy duty")
	print(tabs(1) + "howdy duty")
	print(tabs(2) + "howdy duty")
	print(tabs(3) + "howdy duty")
	print(tabs(4) + "howdy duty")
	print(tabs(5) + "howdy duty")
       

necessary_methods='''
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
    
'''
    
   
##====================================== june 17th thursday cafe borrone 2021 coding 
#### still need to put an  input string C style switch inside of a list slot
#### then run it generating the code gen string and getting sweet and
#### adding sweet to another list for the output
#### and then do that for several within a function
## this needs to call teh module and therefore endswitch() and then do one put
##  sweet string into a list and then do another one and each represents one switch case code 
##========


#============= thursday major coding Big Dipper project here now 

'''
##############
I need to prepare the nested switch put the method_inner_switch on top numbered
and swap inswitch with switch and infallthru with fallthru

##############
put output of code gen into list
add each sweet from each nested switch to list
then using output list full of sweet strings in order
build stacked code string

nested_switch[0] = True will make flag work
need to loop thru list
with input switch string
if nested_switch[0] == True:
     store_py_output.appendI(sweet) # so don't immediately execute it
else:
     exec(sweet) #if nested_switch[0] = False

then convert the switch to inswitch and fallthru to infallthru 
but only for the nested functions NOT for the main switch
and make sure that i name the inner nested swiches correctly too


then stack code of string
then run combined string of all nsted switch
metohds and main switch calling the main switch
to make it all work

'''




## first step nest flag set to True
#  and call a switch to get parsed and code gen'd with endswitch(sw)
#  and then add the generated string in sweet to a list that can be added to
# so it needs to be outside of the codegen function and not cleared until I want it cleared
#  get the switch parsed and the result sweet appended to a list
# for lack of creativitiy we will call it bigdipper


#do one switch conversion
#and then a second one to have the two strings sweet added to 
#the list. by appending

#when done I need to turn the nested switch flag to False

# then after I have this list of output strings I need to concat them together
#and then the rest should be easy

#========================================================================



#####============= make this work right now to get it over with
# divide and conquor to solve any hard problem
# break it down into ltitle pieces

#need a template for a method by calling a function
#that makes the switch string normally and then we
# have a framework of a nested_switch_method with a name with a number
# and then I will have to adjust the tabs with my tab code for indentation.

###### I need the nest flag set to True
#which disables the exec(sweet)
#and enables adding the sweet string to a growing list

    
##=====================================
## june 17th coding test 
#######################################
##     stacking_strings_top_down()(x)
#######################################
def stacking_strings_top_down():
	print("demonstrating stacking strings which will be one string")
	print('and then finally executed')
	#string0 is default always added
	#the count of others is dependent on number of nested switch methods added
	string0= "string0- methods inswitch() infallthru() switch() fallthru()"
	string1 = "string1-nestedsiwth method 1just some words \n and more words here\n a few more"
	string2 = "string2-nested switch method 2 and yet more goody tooty words\nand some more at starbucks\n last few"
	string3 = "string3-main switch cafe borrone\n is next after \n Starbucks breakfast"
	print("testing appending strings to a list")
	print("this will simulate adding generated python code that I will")
	print("then need to stack to build my super layered cake list")
	list1=[]  # to simulate the switchmethod functions and then main switch at bottom
	list1.append(string1)
	list1.append(string2)
	list1.append(string3)
	print("")
	print(".....................")
	print("list1 to see what it has in it")
	#print(list1)
	for item in list1:
		print(item)
	print("............")
	print("")
	
	print("===now test STACKING MULTI LAYER CAKE the strings===")
	top = "some words at the top layer"
	top += "         \n\n" #filler space
	top += string0
	top += "         \n\n" #filler space
	top += string1
	top += " .....   \n\n" #filler space
	top += string2
	top += " .....    \n\n" #filler space
	top += string3
	top += " .....    \n\n" #filler space
	print(top)


test_tabs()
stacking_strings_top_down()


#representing list of strings samples dummy data of output list


# working on this june 17th at cafe borrone 2021
dummy0 = "inswitch and infallthru methods\n\n"
dummy1 = "nested method 1 \n\n"
dummy2 = "nested method 2 \n\n"
dummy3 = " main switch \n\n"
##==============================
##  construct_layered_cake()
##==============================
def construct_layered_cake():
    output_list_layer_cake=''
    output_list_layer_cake  = output_list_layer_cake + dummy0
    output_list_layer_cake  = output_list_layer_cake + dummy1  
    output_list_layer_cake  = output_list_layer_cake + dummy2 
    output_list_layer_cake  = output_list_layer_cake + dummy3   

    print(output_list_layer_cake)

#construct_layered_cake()







# this calls the switch module to convert the input string into python string switch
##===========================================
##   call_module(x) not tested yet 
##===========================================
def call_module(x):  #endswitch is inside of the module
    endswitch(x)  #will this work without calling clever(x)
    #it's just translating it and NOT running through the code so possibly 
    
#input list 
output_list_python=[]
output_list_python.append('starter')

outputlist1=[]
outputlist1.append('starter')







#testing add to a list
def list_gymnastics():
    del outputlist1[0]
    for item in inputlist1:
        outputlist1.append(item)
    #print("list gymanastics fired off")
    #for item in range(1,len(inputlist1)):
    #    outputlist1.append(item)
    
    print(outputlist1)
    
    
##===========================================
##  translate_input_strings_to_python()
##===========================================
#the flag to turn running executing sweet is in the code generator
# and when the nested_switch[0] == True it puts the result
#into a list by appending it and NOT RUNNING it.
#this is what is different we are calling switch module repeatedly
#for each nested function and the main switch method by going thru a list
nested_switch=[]
nested_switch.append(True) #this should be used 
#this means nested_switch[0]

# idea 
#just had flash of insight. the code based to be appended to the 
# nested switch method just have it's tabs set up before concatting it
# to the top method name.
#there is the setting when it's generated (which is constant)
# but with a flag for nested True in the generation I can have it modify
# how many tabs and the differnce shouldn't be more than 2 tabs.
#so there is free form and then there is in a method mode. So two modes.


##===========================================
##  translate_input_strings_to_python()  not tested yet
##===========================================
#not turned on yet this shouldn't be called 
def translate_input_strings_to_python():
    print("calling trnslate-input_strings-to-python()")
    # loop thru list of input strings
    #this sets to special nested switch in code gen to true to not execute it
    # and to instead save the string output in tahoetest[0]
    
    nested_switch[0] = True; #this sets assigns flag to put sweet into string
    #get length of input_list                           # and then append to list and NOT RUN IT
    #print("length of input list =",len(input_list))
    print("")
    #I had a loop here and I took it out to test with just one
    #this calls the switch_module_silver to run parser and codegen
    # and turns of execute and returns the resulting one nested switch  code
    # but it still needs to have layers added to it to make it work correctly
    # to match the design in the file fourth_of_july.py
    print("about to convert input to output python string - not running it yet")
    show_generated_code()
    if nested_switch[0] == True:
        print("nested_switch[0] == True:")
        print('this is using input string in starbucks[1]')
        #for item in input_list: #input list would have input nested switch string in each slot
        #this is calling the method endswitch(x)
        call_module(starbucks[1]) # calls endswitch(x) like sw #call module to translate endswitchstring
        resultpython=tahoetest[0] #will contain the output string sweet concatted python
        #result goes into brewing.append(result)
        #put result into resultpython
        print("the generated python (half way there) is going into output_list_python[1]")
        print(resultpython)
        output_list_python.append(resultpython) #this would be first
        print(output_list_python[1])
        
#about to take the input from
translate_input_strings_to_python()

print('this is as far as I want to go at this point to make gradual progress')
print("=====-=-=-=-=-=-=-=-=-=--======")

# note: replace endswitch with } at the bottom of a nested switch input string
# june 21st, 2021 7:19 pm



#translate_input_strings_to_python()    
#then change switch to inswitch
#then change fallthru to infallthru
#need to add nested_switch number header
#meed to add inswitch and infallthru methods
#then add python version of nested_switch with caselists at top 
 
    
####### figure out the logic ##########
# sw is the input string
# feed it to the module
# get back 
print("=== cafe borrone found testing ===== june 17th, 2021 ==== ")
print("doing test of taking input string in a list and modifying it")
print("and putting result into another list in a series")
inputlist1=[]
inputlist1.append('starter')
inputlist1.append('apple')
inputlist1.append('orange')
inputlist1.append('plum')

print("this phase represents differnet string") 
inputlist1[1] = inputlist1[1] + "drink coffee" + "\n more stuff"
inputlist1[2] = inputlist1[2] + "drink mocha" + "\n cafe borrone"
inputlist1[3] = inputlist1[3] + "drink tea" + "\n tennis tonight"
print("inputlist1 =")
print(inputlist1)


print("now output the result of ")
list_gymnastics()
for item in outputlist1: #output list of the so called python generated code 
     print(item + "\n")

#####==============================================================
# now add a function name to the top
print(" now testing writing methods of nested switch ")
cola = "nested_switch_method_" 

def make_nest_switch_method(y):
    return 
    
    
    
    
print("when not commented out this is where aqua is executed")
print("representing a stacking of nested switches and the main switch")

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

#representing already generated switch code in python. 

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
            print ("this is inside of RABBIT so it worked.")
            tahoe[0]="mickey mouse" #puts victory into tahoe[0]
            print("tahoe[0]",tahoe[0])
            print("leaving rabbit case inside of nested switch")
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

#print('it is all in one big string about to execute it')
#exec(aqua)
#print("after wards we have the results above this line")

print("this will be the next phase changing switch to inswitch and fallthru to infallthru")
print("since we know already that these are nested switches that will be in functions")
print("therefore they will all be required to use inswitch and infallthru")
print("So I take the output and make it happen ")
