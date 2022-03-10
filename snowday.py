
   
raw ='''
	exp = '7';
	exp = 'blable';
	exp = 'tahoe';
	exp = 'winter';
	exp = 'burger';
	exp = 'fishy';
	
	switch(exp){ 
		case 1 thru 6: 
			print("====   purple    =====")
			print("====   purple   =====")
			print("===    poka dots    ======")
			print(" working on january 27th, 2022 8:56 am")
			print('== hamburger sounds good right about now')
			break
			#it should stop here
		case 7 to 10:
			print('pass drive in the snow to tahoe !')
			
			
			switch(exp){
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]=" did it"
					break
					####################
					
					switch(exp){ 
						case 'tahoe':
							print("do  of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("morgan hill starbucks nesting works")
									break
								default:
									print("we are done here")
							endswitch 
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			
			switch(exp){
				case 'burger':
					print("do something")
					####################
					
					switch(exp){   
						case 'fishy':
							print("do something")
							print("yep")
							fallthru
						case 'snow fire':
							print("nice")
							#############
							break
						default:
							print("we are done here")
					endswitch 
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch
			##############
			print('this should be the last line here for output')
			break #was f a l l t h r u
		case 11 to 15:
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''




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



dr='''
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
soclever=[]
soclever.append(0)

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
russia=[]
russia.append(0)

##============================================
## get_first_switch_location(instringname):
##============================================
def get_first_switch_location(instringname):
	#this gets the location of first switch ---------------
	fuel_level=''  #here it is initialized
	counter =0
	for line in instringname.splitlines():
		tabs = line.count("\t")
		#print("tabs =",tabs)
		if "switch(exp)" in line and tabs == 1:  
			grabit =counter 
			russia[0]=grabit #pouts grabit into russia[0]
			break
		else:
			counter += 1

##===========================================================
## copy_switch_string_from_first_switch_down(instringname):
##==========================================================			
def copy_switch_string_from_first_switch_down(instringname):
	# this copies the switch string from the first switch word down to the bottom of string
	counter = 0
	fuel_level =''
	grabit = russia[0] #here it puts var into grabit
	print("russia[0]=",russia[0])
	for line in instringname.splitlines():
		if counter >= grabit:   #only concatting from first switch line number forwards
			fuel_level += line + "\n"
			counter += 1
		else:
			counter += 1

	serious[0] = fuel_level

##==========================================
## remove_exps_at_top_now(instringname):
##==========================================
def remove_exps_at_top_now(instringname):
	mystacktrace("remove_exps_at_top_now(instringname)")
	get_first_switch_location(instringname)                  #method
	copy_switch_string_from_first_switch_down(instringname)  #method
	


##==========================================
##  detect_input_exps_above_first_switch():  These would be above the first switch
##===========================================
def detect_input_exps_above_first_switch(stringname): #above top of nested switch string
	mystacktrace("detect_input_exps_above_first_switch():")
	testing_switch_input_vars='';counter =0;switch_input_vars='';active = False
	#I can concat them to the growing string data
	for line in stringname.splitlines():  #looks in sample 3 line string above for testing
		if line.startswith("\texp="):
			#print(line)
			startline = counter;active = True;
			switch_input_vars += line
			#==== this adds the line number with exp= to list collection =======
			collection.append(counter) #adds line number
			counter += 1
		else:
			#this says if line doesn't start with "exp="" nor start with "switch(exp)"
			if "\texp=" not in line  or line.startswith("switch(exp)"):
				active = False
				stopline = counter -1 #the previous line obviously
 
	clean = switch_input_vars.replace(";",",") #replaces ; with ,
	switch_input_vars = clean
	switch_input_vars = switch_input_vars[:-1] #this cuts off the last char at end
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


#work on this
#do replace of "exp =" change to 'exp='


##============================================
##  manage_exps_prepare_for_processing():
##============================================
def manage_exps_prepare_for_processing(stringname):
	mystacktrace(" manage_exps_prepare_for_processing()")
	concrete='';fool='';counter =0;
	#what this does is skip this switch(exp) line at the top 
	#so when it reacheds the first switch it stops immediately
	for line in stringname.splitlines():
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

##====================================================
##  scan_thru_string_at_top_for_exps(stringname):
##====================================================
def scan_thru_string_at_top_for_exps(stringname):
	print(" ====scan_thru_string_at_top_for_exps(stringname): ==:::::===")
	mystring=''
	if "exp =" in stringname: #tests if exp = in string presumably at the top
		for line in stringname.splitlines():
			if "exp =" in line:
				#so concat and build new stirng
				#this changes (exp =) to (exp=) so that they are consistent
				fixedline = line.replace("exp =","exp=") #looks for exp = changes to exp=
				mystring += fixedline + "\n"
			else:
				mystring += line + "\n"
		soclever[0] = mystring
	else:
		soclever[0]= stringname



resultstring=[]
resultstring.append(0)
samplelist=[]

def do_first_stage(mytest_list):
	print("do first stage")
	counter =0
	print("look in mytest_list now", mytest_list)
	print("=========what the hell is in this list=================")
	for item in mytest_list: #loops thru list made from switch_input_vars string split up
		#this says look at the first char in this item
		if item[0].startswith(' ') == False: #meaning if var doesn't start with space
			answer = mytest_list[counter]
			answer = " " + answer             #adding one space to front of var for uniformity
			mytest_list[counter] = answer     #force feed the change
			counter += 1
		else:
			counter += 1


def do_second_stage(mytest_list):
	print("calling do second stage()======")
	counter=0 
	#chop off from before and including =
	for item in mytest_list: #now this takes out the front part with exp=f from '='
		txt = item
		x = txt.split('=')
		y = x[1]
		#print(y)
		mytest_list[counter] = y
		counter += 1
		

def do_third_stage(mytest_list):
	print("calling do second stage()======")
	counter =0
	for item in mytest_list:            #print("now mytest_list=",mytest_list)
		string = item
		string = string.strip()         #takes out spaces before and after string
		string = string[1:-1]           #cuts off first and last char whatever it may be 
		mytest_list[counter] = string   #puts string into mytest_list[counter]
		counter += 1
	
	print("show samplelist starting here=",samplelist)
	for item in mytest_list:
		samplelist.append(item)  #fills samplelist which is used to feed into adding
	print("at this point the contesnts of samplelist ??")


						
##=========================================================================
##  take_input_vars_for_switches_convert_to_list(switch_input_vars):
##=========================================================================
def take_input_vars_for_switches_convert_to_list(switch_input_vars):
	mystacktrace("take_input_vars_for_switches_convert_to_list(switch_input_vars):")
	mytest_list = switch_input_vars.split(",") #split at commas put into a list 
	do_first_stage(mytest_list)  #method
	do_second_stage(mytest_list) #method
	do_third_stage(mytest_list)  #method
	
	

##==================================================
##  add_exp_var_above_each_switch(stringname):
##==================================================
def add_exp_var_above_each_switch(stringname): #from samplelist
	mystacktrace("add_exp_var_above_each_switch(stringname):")
	manage_exps_prepare_for_processing(stringname)       #method
	cool = relay[0]
	samplelist.clear() #new here 
	take_input_vars_for_switches_convert_to_list(cool)   #method
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
	#this is right::: it must be -1 for setting the counter
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
	morebuilding=''


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
	print("endpoint line number with first switch at 1 tab depth =",endpoint)
	for line in stringname.splitlines():
	#I can change it if exp = change to exp= #work on it
		if "\texp=" in line and counter < endpoint: #this is gleaned above
			if_exps_at_top[0] = 'True'; #sets if_exps_at_top[0] to 'True'
			#print('right here if_exps_at_top[0] should = True')
			break  #the moment this is True end this loop obviously
		else:
			counter += 1

##==============================
##  loop_thru_answer()
##==============================
def loop_thru_answer(answer):
	for line in answer.splitlines():
		print(line)

##==========================================================================
## take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
##==========================================================================
def take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):
	print("==== take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname):==")
	samplelist=[];samplelist.clear() ;mytest_list=[]; mytest_list.clear();relay[0]=''
	loop_thru_the_string(stringname)                 #method
	detect_input_exps_above_first_switch(stringname) #method
	add_exp_var_above_each_switch(stringname)        #method
	show_list_resultstring_to_verify_output()        #method
	gauge[0]=resultstring[0];trouble = gauge[0]
	remove_exps_at_top_now(trouble)                  #method
	take_out_first_line(); answer =serious[0]        #method
	loop_thru_answer(answer)                         #method
	return answer #resulting concatted string
	guage[0]='';resultstring[0]='';trouble='';serious[0]='';answer='';samplelist=[]
	


finaloutput=[]
finaloutput.append(0)	

##=======================
## bottom_method()
##=======================
def bottom_method(stringname):
	if if_exps_at_top[0] == 'True':
		print("==exps at top True=>>>>>>>>>=")
		outputis=take_out_exps_at_top_and_adds_exps_above_nested_switches(stringname)
		finaloutput[0] = outputis
	
	else:
		print("this switch string doesn't have exps at the top")
		loop_thru_the_string(stringname)
		pass
		
		
##===============================================
##  transform_nested_switch_string_for_parser():
##===============================================
def transform_nested_switch_string_for_parser(stringname):
	print("===transform netsedswithdstring  ==")
	scan_thru_string_at_top_for_exps(stringname) #method
	stringname = soclever[0] #now this should fix it
	determine_if_exps_above_first_switch(stringname) #method sets if_exps_at_top[0] to True or False
	#if exp at top then use them otherwise skip
	bottom_method(stringname)

#question is the output from this put back into stringname 
#if not then that is what I need to do next
# saturday morning coding fixing bugs and testing marathon		


##===============================
## prepare_string(stringname)
##===============================
def prepare_string(stringname):
	transform_nested_switch_string_for_parser(stringname)


	
print("first attempt")	
prepare_string(raw)

print('second attempt')
prepare_string(dr) #this should work now I hope

print('third attempt')
prepare_string(z) #this should work now I hope
      
exit()

