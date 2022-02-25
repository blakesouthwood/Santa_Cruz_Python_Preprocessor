


z='''
	exp= '7';
	exp='red';
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
			
			switch(exp){
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
			
			switch(exp){
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


def loop_thru_the_string(stringname):
	for line in stringname.splitlines():
		print(line)
		
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
	#this will start concatting the line with the first switch in it
	#only copy the string once it sees number in solution[0]
	
	counter = 0
	for line in instringname.splitlines():
		if counter >= grabit:   #only concatting from first switch line number forwards
			fuel_level += line + "\n"
			counter += 1
		else:
			counter += 1

	serious[0] = fuel_level
    


##==========================================
##  detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(stringname): #above top of nested switch string
	mystacktrace("detect_input_exps_above_first_switch():")
	testing_switch_input_vars='';counter =0;switch_input_vars='';active = False
	#I can concat them to the growing string daaaa
	for line in stringname.splitlines():  #looks in sample 3 line string above for testing
		if line.startswith("\texp="):
			#print(line)
			startline = counter;active = True;
			switch_input_vars += line
			collection.append(counter) #adds line number
			counter += 1
		else:
			if "\texp=" not in line  or line.startswith("switch(exp)"):
				active = False
				stopline = counter -1 #the previous line obviously
 
	clean = switch_input_vars.replace(";",",")
	switch_input_vars = clean
	switch_input_vars = switch_input_vars[:-1]
	relay[0] = switch_input_vars 

	######################################################
	#THIS WOULD THEN NEXT FILL THE STRING switch_input_vars=
	#remember I will need " at front and " at the tail
	#remove the tabs now
	cute =testing_switch_input_vars.replace("\t"," ")
	cute =cute.replace(";",",")
	cute = cute[:-1]
	testing_switch_input_vars=cute
	testing_switch_input_vars= '"' + testing_switch_input_vars + '"'
	really=testing_switch_input_vars.count('"')





##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing(stringname):
	mystacktrace(" manage_exps_prepare_for_processing()")
	concrete='';fool='';counter =0;
	for line in stringname.splitlines():
	#what this does is skip this switch(exp) line at the top 
	#so when it reacheds the first switch it stops immediately
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
			answer = " " + answer             #adding one space to front of var for uniformity
			mytest_list[counter] = answer     #force feed the change
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
	manage_exps_prepare_for_processing(stringname)
	cool = relay[0]
	take_input_vars_for_switches_convert_to_list(cool) 
	codeking=''
	# go thru each line and based on the number add a line above switch
	mycounter =1
	loop_thru_the_string(stringname)

	for line in stringname.splitlines():
		tabcount = line.count("\t")
		if "switch(exp)" in line and tabcount > 2:  #if a line with switch(exp)at 3 or greater in it
			tabcount = line.count("\t")
			###========================================================
			#here the sameplelist contains just the number or word after the exp=
			word = samplelist[mycounter]          
			tabs = tabcount * '\t'                
			##========================
			if word[-1] == "'": #this says: if last char in word = '
				word= word[:-1] #cuts off last char of word
			else:
				pass
			##===========================
			adding_exp = "exp='" + str(word) + "'"   #this is the word after exp=
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
	morebuilding=''
	counter = -1  #note this is now -1 it was 0 previously but first case was getting cut out
	for line in serious[0].splitlines():
		if counter == 1:
			pass
			counter += 1
		else:
			print(line)
			morebuilding += line + "\n"
			counter += 1
	
	serious[0]= morebuilding


#sniffer to detect exp= above first switch
#and if so then call the transform method otherwise don't call tranform method
#===========  designed on Friday, February 25th, 2022 ==== 10:17 am ===
if_exps_at_top=[]
if_exps_at_top.append(0)
##======================================================
## determine_if_exps_above_first_switch(stringname):
##======================================================	
def determine_if_exps_above_first_switch(stringname): #sniffer
	print("=@@@@===determine_if_exps_above_first_switch(stringname): ===@@@@==")
	if_exps_at_top[0] = 'False' ;#sets default setting of if_exps_at_top[0] to 'False'
	counter =0; endpoint =''; #line number of first switch// also clears it out as reset here
	#get location of first switch( at tab depth 1 )	
	for line in stringname.splitlines():
		tabsdepth = line.count("\t")#how do I say if exp= above first switch
		if "\tswitch(" in line and tabsdepth == 1:
			endpoint = counter #sets endpoint to counter
			#print("endpoint =",endpoint)
			break
		else:
			counter += 1
	#this looks to determine if exp= ABOVE first switch at 1 tab depth
	counter =0  #the endpoint constant is the line number of the first switch at tab depth 1
	print("enpoint line number with first switch at 1 tab depth =",endpoint)
	for line in stringname.splitlines():
		if "\texp=" in line and counter < endpoint: #this is gleaned above
			if_exps_at_top[0] = 'True'; #sets if_exps_at_top[0] to 'True'
			#print('right here if_exps_at_top[0] should = True')
			break  #the moment this is True end this loop obviously
		else:
			counter += 1


##==========================================================================
## take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
##==========================================================================
def take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
	loop_thru_the_string(stringname)
	detect_input_exps_above_first_switch(stringname)
	add_exp_var_above_each_switch(stringname)
	show_list_resultstring_to_verify_output()
	gauge[0]=resultstring[0];trouble = gauge[0]
	remove_exps_at_top_now(trouble)
	take_out_first_line()  
	
	
##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser(stringname):
	determine_if_exps_above_first_switch(stringname) #sets if_exps_at_top[0] to True or False
	if if_exps_at_top[0] == 'True':
		take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname)
	else:
		pass
		
	

transform_nested_switch_string_for_parser(z) #this should work now I hope

       
exit()





