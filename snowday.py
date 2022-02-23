'''
stack trace for this method chain is
===now we will see the call stack as party list===

detect_input_exps_above_first_switch():
add_exp_var_above_each_switch(stringname):
 manage_exps_prepare_for_processing()
take_input_vars_for_switches_convert_to_list(switch_input_vars):
show_list_resultstring_to_verify_output():
remove_exps_at_top_now(instringname)
take_out_first_line():
'''


import mocha  
from mocha  import * 



elcapitan='''
	exp= '9';
	exp='orange';
	exp='purple';
	
	switch(exp){   
		case 1 thru 6: 
			print("mocha morning!")
			print('a walk in the park')
			print('listening to neo music ')
			break
		
		case 7 thru 10: 
			print("two !")
			print('cold tennis')
			print('who will win? ')
			fallthru
			
			switch(exp)   
				case 'red':
					print("this is red we are inside of the nested sw i tch now I did it ")
					print("3 billion of them .go baby go make it happen..")
					fallthru
				case 'blue':
					print("this is blue we are blue blood cells ")
					print("1 zillion of them this should have printeded...")
					break
				case 'orange':
					print("this is orange saturday morning coding== ")
					print("figuring out where to apply next...")
					break
				default:
					print('this is default this was missing')
					print(' darn it')
			endswitch
			
			switch(exp)   
				case 'green':
					print("this is  green  now I did it ")
					print("the matrix make it happen..")
					fallthru
				case 'purple':
					print("this is purple panama canal 3 levels ====")
					print("needs 4 lanes have printeded...")
					break
				default:
					print('this is lower def ault this was missing')
					print(' darn it')
			endswitch
			break
		default:
			print('no matches so sorry about that ')
			print(' ')
			
}
'''	

partylist=[]

def mystacktrace(stringhere):
    partylist.append(stringhere)

def list_party_list_sequence():
    for item in partylist:
        print(item)

    
def build_top_exps_string():
    mystacktrace("build_top_exps_string()")
    ###====feb 22nd jazz ==========================
    if_you_build_it=''
    
    for line in elcapitan.splitlines():
        tabcount = line.count('\t')
        if "exp=" in line and tabcount == 1:
            if_you_build_it += line + "\n"
        else:
            pass
    print('the copied top part == this ')
    for line in if_you_build_it.splitlines():
        print(line)
    
#exit()   
    
#loop thru string and add input value we know it will be exp='blue'
# if switch indented at 3 or more then
#print line number 
 #the first number or word is passed into the first top swithch thru feedinput(num) 
#right now
#exp = 'blue'
#num = 8   #notice that this is not in a string 
#feedinput(num)
#=========================================
#exp1= 8, exp2='blue', exp3='green'
#this is above the switch case triple string

###============= new feb 21st 
relay=[]
relay.append(0)

#I need to break it in half to gain control of the process. Feb 21st 

#this is sample input to show what it will start with  or actually the intended output
############################
#switch_input_vars="exp= '8', exp='blue', exp='purple'" #notice no space before first one
##############################################
#so the code that I just wrote fills this var and now adds the " to front and tail "

# use a method and then return the string that way THIS SHOULD WORK 
#I need to take this string below and make it look like the string above
#they must be togetehr and start with one tab
#and be above top switch by one line
#so this column view is transformed into the across format seen above in switch input vars 

##=========================================
#now I will need to detect exp at top and last line
# with no line breaks
#so I am turnig teststring into switch_input_vars which 
stopline=''
startline=''
#detects if exp='word' above first switch and copies them
#after i copy them I have to comment them out brilliant
#with # at front (( just realized this fact ))

teststring='''
	exp= '8';
	exp='pink poka dots';
	exp='mocha in drive thru';
'''

gauge=[]
gauge.append(0)

#go thru the input string and concat building a small string

#what if I generate the whole thing with all content and then
#skip the exps at top on final pass


#print("this is tiny teststring to see it")
#for line in teststring.splitlines():
#    print(line)
    
collection=[]   #this gets the inputs exps for the NESTED SWITCHES INPUT


serious=[]
serious.append(0)
def remove_exps_at_top_now(instringname):
    mystacktrace("remove_exps_at_top_now(instringname)")
    print("=====remove_exps_at_top_now()=== this is called HERE 5:00 pm ====")
    fuel_level=''  #here it is initialized
    counter =0
    for line in instringname.splitlines():
        tabs = line.count("\t")
        #print("tabs =",tabs)
        if "switch(exp)" in line and tabs == 1: 
            grabit =counter 
            break
        else:
            counter += 1
    #second loop here
    #this will start concattinga the lien with teh first switch in it
    #only copy the string once it sees number in solution[0]
   
    print("value of grabit =", grabit)
    print(type(grabit))
    counter = 0
    for line in instringname.splitlines():
        if counter >= grabit:   #only concatting from first switch line number forwards
            fuel_level += line + "\n"
            counter += 1
        else:
            counter += 1
    
    
    
    print("this should be from just the first switch down,we shall see")
    print("==RIGHT== HERE THIS RESULTING STRING SHOULD HAVE NO exp= above first switch")
    for line in fuel_level.splitlines():
        print(line)
    serious[0] = fuel_level
    
#remove_exps_at_top_now(teststring)
#print("end of tiny mocha test")






######teudday feb 22nd ######
########### this is where I need to look to get this working right===
##==========================================
## detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(): #above top of nested switch string
    mystacktrace("detect_input_exps_above_first_switch():")
    #print(" detect_input_exps_above_first_switch() ========line 67 =============")
    #print(" ===DETECT INPUT EXPS ABOVE FIRST SWITCH FOR REAL =====================================================================")
    testing_switch_input_vars=''
    #print(" ====::::====detect_input_exps_above_first_switch() ")
    #this finds the range of exp= lines and starts and stop line numbers
    #loop thru string
    counter =0
    switch_input_vars=''
    active = False  #I can concat them to the growing string daaaa
    #designed to use teststring:
    #now using elcapitan
    for line in elcapitan.splitlines():  #looks in sample 3 line string above for testing
        if line.startswith("\texp="):
            #print(line)
            startline = counter
            active = True
            switch_input_vars += line
            collection.append(counter) #adds line number
            counter += 1
        else:
            if "\texp=" not in line  or line.startswitch("switch(exp)"):
                active = False
                stopline = counter -1 #the previous line obviously
                #break
                #print("done")
    #count how many lines starts with exp in a sequence
    print("what it looks like RIGHT HERE MOUSE HOUSE HERE")
    print("line 233 ===========switch_input_vars")
    print(switch_input_vars)
    clean = switch_input_vars.replace(";",",")
    switch_input_vars= clean
    print(switch_input_vars)
    switch_input_vars = switch_input_vars[:-1]
    relay[0] = switch_input_vars #just added feb 23rd wednesday
    ##====
    ##====
    
    #print("should be 9 orange green")
    #put a space before word
    ######################################################
    #THIS WOULD THEN NEXT FILL THE STRING switch_input_vars=
    #remember I will need " at front and " at the tail
    #remove the tabs now
    print(testing_switch_input_vars)
    cute =testing_switch_input_vars.replace("\t"," ")
    cute =cute.replace(";",",")
    cute = cute[:-1]
    #print("the result is building the input string of the exps")
    #print(cute)
    testing_switch_input_vars=cute
    print("testing_switch_input_vars=",testing_switch_input_vars)
    testing_switch_input_vars= '"' + testing_switch_input_vars + '"'
    #print(testing_switch_input_vars)
    print("testing_switch_input_vars=",testing_switch_input_vars)
    #print("==verifying that it starts and ends with doublue quotes===")
    really=testing_switch_input_vars.count('"')
    #print("WE NEED A TWO here")
    #print("this should say 2 and it says",really)
    #print("we need it to start with quote and ends with it too")
    #if testing_switch_input_vars.startswith('"') and \
    #   testing_switch_input_vars.endswith('"'):
    #    #print("YES Victory")
    #else:
    #    pass #print("dam defeat")
    #print("==line 109 the precious input string var======right here at this juncture ==========")    
    #needs to look like this switch_input_vars="exp= '8', exp='red', exp='green'"
    #################

#will need to have error message if user neglects/forgets
# to put the exp at the top otherwise the nested switch won't run
#NEXT I need to put # in front of each of th exp at top of input string
# saturday feb 19th 2022 wow time flies
##=================================================================
new_switch_input_vars='' #it will need to already exists for simplicity










##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing():
	mystacktrace(" manage_exps_prepare_for_processing()")
	print(" == manage_exps_prepare_for_processing==== line 250====")
	#print(" =======what is this showing for the content???===========================================================")
	concrete=''
	fool=''
	counter =0
	for line in elcapitan.splitlines():
	#what this does is skip this switch(exp) line at the top 
	#and so when it reacheds the first switch it stops immediately
	
		if "switch(exp)" in line: #this should stop it
			break
		else:
			if "exp" in line:
				line = line[5:]  #cut off first 5 chars
				line = line[:-1] #cut off end char
				fool += line  + "\n"  
		        #here it is building a string 
			#mag = line.strip()
	print("fool=",fool)
	print("what does this HAVE in it========")
	#samplelist.clear() ## new see what we have here 
	for line in fool.splitlines():
		print(line)
		#radical = line.strip()
		#samplelist.append(radical)
		#THEsE ARE rIGHT HERE but need to be put into a list
		#if counter == 0:
		#	concrete += mag 
				#print(concrete)
		#	counter +=1
		#else:
		#	concrete += mag + ", "
		#	#print(concrete)
		#	counter +=1
	concrete = concrete[:-2] #gets rid of space and , at front
	concrete = '"' + concrete + '"'  # new on feb 21st monday
	print("HERE HERE HERE CINdERLLA should be the input vars")
	print("concrete=",concrete)

	new_switch_input_vars=concrete
	#I need to make it look like switch_input_vars
	#should be red, purple
	#relay[0] = switch_input_vars
	print('line 337 ===')
	print("relay[0]=",relay[0])
	
	

#print("about to test DETECT INPUT EXPS ABOVE FIRST SWITCH")
#this would happen in the first phase scan of the string to grab the exps above first switch
detect_input_exps_above_first_switch() #and fill var string automatically
##============================================================================
#print("== line 221===here we go see if this puppy works or not")


#confusing mytest_list and samplelist


#concat copy string and then add inbetween genius
# keep going 
#this has now modified the original string in the first pass
##==================================
##  add_line_to_string(stringname): 
##==================================
# what this does is look specifically for each line with switch with tabs more than 2
# and adds a new line above the switch moving the switch line down 1
# now actually since every line is moved down one from that point
# the next switch that a line is added above means it moved down 2 and not 1
# and so on and so forth




resultstring=[]
resultstring.append(0)
samplelist=[]
##=========================================================================
##  take_input_vars_for_switches_convert_to_list(switch_input_vars):
##=========================================================================
def take_input_vars_for_switches_convert_to_list(switch_input_vars):
	mystacktrace("take_input_vars_for_switches_convert_to_list(switch_input_vars):")
	print("==take input vars for switches conver to list  ==line 283 =====")
	print('INVESTIGATE IF ((THIS)) SECTION IS ACTUALLY WORKING OR NOT')
	#print("===============================================================")
	#global testing_switch_input_vars
	#at this point they would already be in the var has a string of vars  <<============
	#switch_input_vars = testing_switch_input_vars
	#this cuts up and separates the initial string with exp= series
	#print("switch_input_vars",switch_input_vars)
	mytest_list = switch_input_vars.split(",") #split at commas put into a list 
	#loop thru my_list add space before first char if no space
	print("mytest_list=",mytest_list)
	print("===0=0=0=0=0=0=0=0=0=0=0=0=0=0=0==0=0=")
	counter =0
	for item in mytest_list: #loops thru list made from switch_input_vars string split up
		#this says look at the first char in this item
		if item[0].startswith(' ') == False: #meaning if var doesn't start with space
			answer = mytest_list[counter]
			answer = " " + answer  #adding one space to front of var for uniformity
			mytest_list[counter] = answer #force feed the change
			counter += 1
		else:
			counter += 1
			
	#######==================================================================	
	counter=0 
	#chop off from before and including =
	for item in mytest_list: #now this takes out the front part with exp=f from '='
		txt = item
		x = txt.split('=')
		y = x[1]
		print(y)
		mytest_list[counter] = y
		counter += 1
	
	##=======================================
	#take out spaces on both sides of string 
	#cut off first char and last char
	#feed each word into list myhtest_list
	counter =0
	for item in mytest_list:            #print("now mytest_list=",mytest_list)
		string = item
		string = string.strip()         #takes out spaces before and after string
		string = string[1:-1]           #cuts off first and last char whatever it may be 
		mytest_list[counter] = string   #puts string into mytest_list[counter]
		counter += 1
	
	#feed mytest_list into samplelist
	for item in mytest_list:
		samplelist.append(item)  #fills samplelist which is used to feed into adding
	print("testing to see what we have in here now")
	print("samplelist=",samplelist) #  '9', 'red', 'purple'
	
	







#THIS IS CALLLED as teh little micro main in the beginning =====
##==================================================
##  add_exp_var_above_each_switch(stringname):
##==================================================
def add_exp_var_above_each_switch(stringname): #from samplelist
	mystacktrace("add_exp_var_above_each_switch(stringname):")
	print("== add_exp_var_above_each_switch(stringname) ====line 338 =")
	print("============================>>>>>>>>>")
	#calling method now to set up switch_input_vars
	manage_exps_prepare_for_processing()
	print("this is relay[0]",relay[0])
	cool = relay[0]
	take_input_vars_for_switches_convert_to_list(cool) #was switch_input_vars
	print("february 22nd 2022 the list of what is being added is in  samplelist",samplelist)
	
	#samplelist.clear()
	#samplelist.append(9)
	#print("first is",samplelist[0])
	#samplelist.append("mocha") #poistion 1
	#samplelist.append("coffee")#position 2
	
	
	#So I need to feed the list sampleist
	#feb 23rd 
	#def fill_simplelist(stringinput):
	#	#dissect list above 
	#	print("not implimented yet")
	
	
	##======================================================
	#so I need to clear out samplelist and refill it with correct data
	##===== feb 22nd 5:32 pm===================================================
	
	
	#this is the before modification of the string view 
	for line in stringname.splitlines():
		print(line) 
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =1
	for line in stringname.splitlines():
		tabcount = line.count("\t")
		if "switch(exp)" in line and tabcount > 2:  #if a line with switch(exp)at 3 or greater in it
			tabcount = line.count("\t")
			###========================================================
			#here the sameplelist contains just the number or word after the exp=
			word = samplelist[mycounter]           #print("word=",word)
			tabs = tabcount * '\t'                 #print('tabs=',tabs)
			print('see what it sees')
			#temporary bug fix if ' on end of last word
			##========================
			if word[-1] == "'":
				print("error warning word ends with (') ")
				word= word[:-1]
				print("just removed ending apostrophe which was extranious")
				print(word)
			else:
				print("not ending with ' which is good")

			print(word)
			##===========================
			adding_exp = "exp='" + str(word) + "'"                #this is the word after exp=
			#this is adding the exp='word' to line and putting switch on next line
			codeking += tabs + adding_exp + '\n' + line + '\n'
			mycounter += 1
		else:
			codeking += line  + '\n'
	resultstring[0]=  codeking
	
	
	
	
	
#########################
#this is adding exp='word' above each NESTED SWITCH 
add_exp_var_above_each_switch(elcapitan)  #verified works becomes codeking string
#########################

def show_list_resultstring_to_verify_output():
	mystacktrace("show_list_resultstring_to_verify_output():")
	print("show_list_resultstring_to_verify_output() ==== line 370 ====")
	print("============================================================")
	#elcapitan = resultstring[0] #= resultstring
	#this is outputting the new string concatted that is in redusltstring[0]
	print('this is elcapitan that is now modified')
	for line in resultstring[0].splitlines():
		print(line)
	
	#field_of_dreams = resultstring[0]




show_list_resultstring_to_verify_output()



###===============================================
#coding sunday morning feb 20th ================= 
###==============================================
print("this is looking in resultstring[0]")


	
#this_comments_out_the_exps_above_switch_case_input()   
#I don't need to call this one
gauge[0]=resultstring[0]
trouble = gauge[0]
print("testing what the string looks like on line 503")
for line in trouble.splitlines():
	print(line)
	
remove_exps_at_top_now(trouble)

num = 9   
#feedinput(num);
def take_out_first_line():
	mystacktrace("take_out_first_line():")
	print("======the finished string is now this.=========.")
	morebuilding=''
	counter=0
	for line in serious[0].splitlines():
		if counter == 1:
			pass
			counter += 1
		else:
			print(line)
			morebuilding += line + "\n"
			counter += 1
	#two_choices(fortune_favors_the_brave)
	serious[0]= morebuilding
	for line in serious[0].splitlines():
		print(line)
	print("=========stopping at line 416 ========")

take_out_first_line()



print("===now we will see the call stack as party list===\n")
list_party_list_sequence()    
exit()


'''
===now we will see the call stack as party list===

detect_input_exps_above_first_switch():
add_exp_var_above_each_switch(stringname):
manage_exps_prepare_for_processing()
take_input_vars_for_switches_convert_to_list(switch_input_vars):
show_list_resultstring_to_verify_output():
#this_comments_out_the_exps_above_switch_case_input():
remove_exps_at_top_now(instringname)
take_out_first_line(): #which is above first switch
'''














#### nothing should run below this line ===============





#loop thru tabhistory len
#        addline_with_exp_insertion(word)
        
        
#addline_with_exp_insertion("aqua")
#locate_inner_switches_and_add_var_from_list()


print("")
show_tabs_for_nested_switches()
#exit()
genstring =resultstring[0]
insert_new_lines_with_var_expressions_dynamically(genstring)
print("==== testing elcapitan new switch string all kinds of probs why==")


'''
 int a = 100;
   int b = 200;
 
   switch(a) {
   
      case 100: 
         printf("This is part of outer switch\n", a );
      
         switch(b) {
            case 200:
               printf("This is part of inner switch\n", a );
         }
   }
   
'''



#this will just take in as input the string now not num,red_robin


print("====== testing el capitan here =======")


#loop thru string and add input value we know it will be exp='blue'
# if switch indented at 3 or more then
#print line number 
num = 8   
feedinput(num)
#main_control_sequencer(num,elcapitan)#
for line in elcapitan.splitlines():
    print(line)


two_choices(elcapitan)

list_party_list_sequence()

exit()


###==========================
#####========================












    
    
    
    
    
myswitchlist=[]
#######################################################
#the inputs would be added to the list 
listmarker =[]
listmarker.append(8)        #1       though really 0  #these were hard coded inputs 
listmarker.append("blue")   #2       though really 1
listmarker.append("green")  #3       though really 2
tabhistory=[]

#list  17(2), 29(3)
 #first inner switch + 2 becomes 19
 #second inner switch + 3 becomes 32
#0 1 2
#ignore
# 1 + 1
# 2 + 2
# 3 + 3
 


#so in theory the switch line number becomes where I now put the exp='word'
##===================================================
##  locate_inner_switches_and_add_var_from_list()
##===================================================
def locate_inner_switches_and_add_var_from_list():
	print("=== line 280  locater inner switches and add var from list =")
	print("dino[0]=",dino[0])
	counter =0
	activecount = 1
	print("here we go baby")
	for line in elcapitan.splitlines():
		tabcount = line.count("\t")
		#this is THIS LINE we are talking about =====
		if "switch" in line and tabcount > 2: #meaning after first one
			#print("tabcount in this line = ",tabcount)
			print("======SWITCH RIGHT HERE====",counter)
			##
			myswitchlist.append(counter)
			print("listmarker[activecount]=",str(listmarker[activecount]))
			print("activecount=",activecount)
			tabhistory.append(tabcount) #because we know switch in this line
			#and we need to have the same tab depth 
			#this is the overflow stop feature ======
			if activecount == len(listmarker):
				break 
			else:
				counter += 1
				#this is new to end the loop since we hit end of listmarker list
				activecount += 1
		else:
			if activecount == len(listmarker):
				break 
			else:
				counter += 1
###########===================================================



#listmarker list contents = 8, blue, green 
#I will need the tab depth of the switch by line number
##================================
##  addline_with_exp_insertion():
##================================
def addline_with_exp_insertion(word):
    print("=== line 318 addline with exp insertion() called")#add a line first with "\n" at line number BEFORE switch
    #so it will be switch line number MINUS ONE
    #word = "yellow"
    expand="exp = '" + word + "'"
    print(expand)
    return expand
    

#so it's predicable where the switch numbers will move to
# if we have 18+1  and 30 +1
#  and 31 + 1  I think 


    
def show_tabs_for_nested_switches():
	print("tabhistory list=",tabhistory)


#so I will put the exp='word' in the NEWly created line where the switches were
# which was there line number
##=========================================================
## insert_new_lines_with_var_expressions_dyanmically()
##==========================================================
#these should be inserted where the original switch number was 
secondstring =''
def insert_new_lines_with_var_expressions_dynamically(insertstring):
	global secondstring
	print("==line 463 === insert_new_lines_with_var_expressions_dynamically()===== ")
	word =''
	print("let us see what is sees at this point JUNCTURE:::")
	for line in insertstring.splitlines():
		print(line)
		
	print("myswitchlist=",myswitchlist)

	linenumber =1
	magiccounter=1 
	for line in insertstring.splitlines():
		
		 #so the switchlist will need to be modified on the fly
		
		#based on the number of number in it Need to write the formula
		if linenumber in myswitchlist:               #brilliant this should be the line to insert 
			print("CORRECT MATCH linenumber",linenumber,"in",myswitchlist)
			word = listmarker[magiccounter]          #get word in listmarker by index
			print("word line 209 =",word)
			result =addline_with_exp_insertion(word) #EXAMPLE exp='green'
			print("result line 211 =",result)
			tabdepth= tabhistory[magiccounter]
			print("tabdepth=",tabdepth)
			tabs = tabdepth * '\t'
			print("tabs =",tabs)
			combined = tabdepth + result + "\n" 
			print("combined concated exp=",combined)
			secondstring += combined 
			magicounter += 1                          # \t\t\t exp='green' \n
			linenumber += 1
		else:
			secondstring += line + "\n"
			magiccounter += 1
			linenumber += 1

	print('the result is this.......')
	for line in secondstring.splitlines():
		print(line)




