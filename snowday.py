

import mocha  
from mocha  import * 



elcapitan='''
	exp= '7';
	exp='orange';
	exp='green';
	
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
    return
    #for item in partylist:
    #    print(item)

    
def build_top_exps_string():
    return  #not called 
    mystacktrace("build_top_exps_string()")
    ###====feb 22nd jazz ==========================
    if_you_build_it=''
    
    for line in elcapitan.splitlines():
        tabcount = line.count('\t')
        if "exp=" in line and tabcount == 1:
            if_you_build_it += line + "\n"
        else:
            pass
    #print('the copied top part == this ')
    #for line in if_you_build_it.splitlines():
    #    print(line)
    



relay=[]
relay.append(0)
stopline=''
startline=''
gauge=[]
gauge.append(0)
collection=[]   #this gets the inputs exps for the NESTED SWITCHES INPUT


serious=[]
serious.append(0)
##==========================================
## remove_exps_at_top_now(instringname):
##==========================================
def remove_exps_at_top_now(instringname):
    mystacktrace("remove_exps_at_top_now(instringname)")
    #print("=====remove_exps_at_top_now()=== this is called HERE 5:00 pm ====")
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
    #this will start concattinga the lien with teh first switch in it
    #only copy the string once it sees number in solution[0]
   
    
    counter = 0
    for line in instringname.splitlines():
        if counter >= grabit:   #only concatting from first switch line number forwards
            fuel_level += line + "\n"
            counter += 1
        else:
            counter += 1
   
    #print("this should be from just the first switch down,we shall see")
    #print("==RIGHT== HERE THIS RESULTING STRING SHOULD HAVE NO exp= above first switch")
    #for line in fuel_level.splitlines():
    #    print(line)
    serious[0] = fuel_level
    


##==========================================
##  detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(): #above top of nested switch string
    mystacktrace("detect_input_exps_above_first_switch():")
    testing_switch_input_vars=''
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
              
 
    clean = switch_input_vars.replace(";",",")
    switch_input_vars= clean
    #print(switch_input_vars)
    switch_input_vars = switch_input_vars[:-1]
    relay[0] = switch_input_vars #just added feb 23rd wednesday
   
    ######################################################
    #THIS WOULD THEN NEXT FILL THE STRING switch_input_vars=
    #remember I will need " at front and " at the tail
    #remove the tabs now
    #print(testing_switch_input_vars)
    cute =testing_switch_input_vars.replace("\t"," ")
    cute =cute.replace(";",",")
    cute = cute[:-1]
    testing_switch_input_vars=cute
    #print("testing_switch_input_vars=",testing_switch_input_vars)
    testing_switch_input_vars= '"' + testing_switch_input_vars + '"'
    #print("testing_switch_input_vars=",testing_switch_input_vars)
    really=testing_switch_input_vars.count('"')
    










##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing():
	mystacktrace(" manage_exps_prepare_for_processing()")
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
		


		
	concrete = concrete[:-2] #gets rid of space and , at front
	concrete = '"' + concrete + '"'  # new on feb 21st monday
	new_switch_input_vars=concrete
	
	
	
#this would happen in the first phase scan of the string to grab the exps above first switch
#detect_input_exps_above_first_switch() #and fill var string automatically
##============================================================================

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

	mytest_list = switch_input_vars.split(",") #split at commas put into a list 
	
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
		#print(y)
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
	
	
	





##==================================================
##  add_exp_var_above_each_switch(stringname):
##==================================================
def add_exp_var_above_each_switch(stringname): #from samplelist
	mystacktrace("add_exp_var_above_each_switch(stringname):")
	manage_exps_prepare_for_processing()
	cool = relay[0]
	take_input_vars_for_switches_convert_to_list(cool) 
	
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =1
	for line in stringname.splitlines():
		tabcount = line.count("\t")
		if "switch(exp)" in line and tabcount > 2:  #if a line with switch(exp)at 3 or greater in it
			tabcount = line.count("\t")
			###========================================================
			#here the sameplelist contains just the number or word after the exp=
			word = samplelist[mycounter]          
			tabs = tabcount * '\t'                
			##========================
			if word[-1] == "'":
				word= word[:-1]
			else:
				
				pass
			
			##===========================
			adding_exp = "exp='" + str(word) + "'"                #this is the word after exp=
			#this is adding the exp='word' to line and putting switch on next line
			codeking += tabs + adding_exp + '\n' + line + '\n'
			mycounter += 1
		else:
			codeking += line  + '\n'
	resultstring[0]=  codeking
	
		

##==============================================
## show_list_resultstring_to_verify_output():
##==============================================
def show_list_resultstring_to_verify_output():
	mystacktrace("show_list_resultstring_to_verify_output():")
	
	






##======================================
##   take_out_first_line():
##======================================
def take_out_first_line():
	mystacktrace("take_out_first_line():")
	#print("======the finished string is now this.=========.")
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



##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser():
    detect_input_exps_above_first_switch()
    add_exp_var_above_each_switch(elcapitan)
    show_list_resultstring_to_verify_output()
    gauge[0]=resultstring[0];trouble = gauge[0]
    remove_exps_at_top_now(trouble)
    take_out_first_line()
    list_party_list_sequence() 
    

transform_nested_switch_string_for_parser()




       
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


#print("====== testing el capitan here =======")


#loop thru string and add input value we know it will be exp='blue'
# if switch indented at 3 or more then
#print line number 
#list_party_list_sequence()

#num = 8   
#f#eed

exit()


###==========================
#####========================











#none below are called apparently 
    
    
    
    
    
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
			magicounter += 1                 
			linenumber += 1
		else:
			secondstring += line + "\n"
			magiccounter += 1
			linenumber += 1

	print('the result is this.......')
	for line in secondstring.splitlines():
		print(line)

'''
stringname = elcapitan
def setting_up_switch_string_for_parsing(stringname):
	detect_input_exps_above_first_switch():
	add_exp_var_above_each_switch(stringname):
 	manage_exps_prepare_for_processing()
	take_input_vars_for_switches_convert_to_list(switch_input_vars):
	show_list_resultstring_to_verify_output():
	remove_exps_at_top_now(instringname)
	take_out_first_line():
'''
