December 1st, 2021 10:39am Morgan Hill, California  Starbucks
Today is a happy day!

Input string successfully translated into strings to send thru bypass205() parser.
Note: this is after line numbers have previously already added after each switch which becomes their id.
	
string_name= 
	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
				case 'blable':
					print("do something")
					####################
					switch(exp){ #15
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
									####################
									switch(exp){ #31
										case 'fishy':
											print("do something")
											print("yep")
											fallthru
										case 'where now':
											print("nice")
											break
										default:
											print("we very done")
									endswitch 
							#############
									break
								default:
									print("we are done here")
							endswitch #46  
							#############
							break
						default:
							print("we are done here")
					endswitch #51   
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #60   
			exp = 3
			switch(exp){ #62

			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
	endswitch #100
The chain methods transforms the switch string into this output in a list.
Not all nested strings will have nested strings with them which I dealt with today.
				
Not shown here but the indentation level on the left before the switch is just 1 tab. so this makes it look off.
Notice the inner switches are now numbered nested_switch methods
				
	switch(exp) #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_62(exp) #62

			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
	} #100  

........ 1

	switch(exp) #11
		case 'blable':
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #60   4..........endwitch 4  line 60 3 tabs 

........ 2

	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			nested_switch_23(exp) #23
			#############
			break
		default:
			print("we are done here")
	} #51   3 ...

........ 3

	switch(exp) #23
		case 'tahoe':
			print("do something")
			print("yep")
		case 'fallen leaf lake':
			print("nice")
		####################
			nested_switch_31(exp) #31
			#############
			break
		default:
			print("we are done here")
	} #46  2.......

........ 4

	switch(exp){ #31
		case 'fishy':
			print("do something")
			print("yep")
			fallthru
		case 'where now':
			print("nice")
			break
		default:
			print("we very done")
	} 

........ 5

	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #86

........ 6

	switch(exp){ #66
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
	} #77 5 .....

........ 7

###==============
##   plan B 
##================  testing converting nest string testlist_of_strings
def planB():  #november 30th, tuesday 9:45 am morgan hill starbucks 
    print("never give up")
    print('===== welcome to planB ==== november 30th tuesday===')
    print("doing planB testing each nest_list doing chain_methods")
    print("length of testlist_of_strings =",len(testlist_of_strings))
    for item in testlist_of_strings:
        print(item)
    print("====now we do the chain methods on the switch strings====")
    counter=1
    print('======== calling simulated chain methods =========')
    for item in testlist_of_strings: #test string names numbered
        print("========================")
        simulated_chain_methods(item) #testing chain methods
        print("====== counter= ",counter)
        counter += 1
        

print("the big test begins")
planB()
print("now simply loop thru the finished changes in the list")
#the new finished strings should be in hollister list all cleaned up and reduced
print("was Snoopy right and Woodstock too?")
counter =1
for item in hollister_list:
    print(item)
    print("........",counter)
    counter += 1
    
		
##=========================================
##  simulated_chain_methods():
##===================================
def simulated_chain_methods(mystring): #starting point  
    count_endswitches=mystring.count("endswitch")
    print("number of endswitches in THIS  string",count_endswitches)
    
    if count_endswitches > 1:
        print("TRUE countswitches =",count_endswitches)
        
        print("simulated_chain_methods() Rudolph the red nosed reindeer")
        print("simulated_chain_methods() Rudolph the red nosed reindeer")
        fizz  = dafirst_method(mystring) #modern_tab_shifter_to_left()
        fizzy = dasecond_method(fizz)    #take_out_switch_body()
        fuzzy = dathird_method(fizzy)    #change_switch_to_method_solved()
        frac  = dafourth_method(fuzzy)   #take_out_endswitch()
        hollister_list.append(frac)      #added to list here
    else: 
        print("count_endswitches=",count_endswitches)
        #no nested switch in this switch string
        modern_tab_shifter_to_left(mystring)#modern_tab_shifter_to_left() shift indentation
        astring = goldtime[0] #its output
        finalresult=take_out_endswitch(astring)#take_out_endswitch()
        mystring=finalresult
        hollister_list.append(mystring) #added to list here		

#chain methods below 
#manipulate_string left shift indentation
def dafirst_method(astring): #this does the left shift 
    print("first message called..modern_tab_shifter_to_left")
    #shifts string left to indent it properly
    modern_tab_shifter_to_left(astring) #I think that this does left shift indentation
    astring = goldtime[0]
    return astring
    
#take_out_switch_body
def dasecond_method(astring): #cuts out switch body leaving switch word in all occurances
    print("seconed method called...take_out_switch_body")
    take_out_switch_body(astring) #this takes out the switch body 
    #the output goes into lightning[0]
    astring=lightning[0] #this is new to see if it works=========
    return astring


#change_switch_to_method_solved
def dathird_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method called...change_switch_to_method_solved")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=change_switch_to_method_solved(astring)
    #astring += " bright"
    return finalresult


#take_out_endswitch(stringname)
def dafourth_method(astring):  #this changes the inner switch to nested_switch numbered 
    print("third method called..take_out_endswitch().")
    #change_switch_to_method_solved() takes out switch puts in nested_switch
    finalresult=take_out_endswitch(astring)
    return finalresult
    
hollister_list=[]				


		
		
###=================================================================
passthis=[]
passthis.append(0)
##
#this gets the tabdepth in front of top switch word
##==================================================
##  starter_engine(the_nest_string):   nov 30th tested working accurately
##==================================================
def starter_engine(the_nest_string):
	print("======starter engine called======")
	tabdepth='';n=''
	for line in the_nest_string.splitlines(): #nest_string
		if "switch" in line and "end" not in line: #had "not"
			tabdepth = line.count("\t")
			n= tabdepth;n = n-1  #need to have one tab in front
			break
	passthis[0]= n
	print("n =",n)

goldtime=[]
goldtime.append(0)
##===================================================================
##  modern_tab_shifter_to_left(the_nest_string):  nov 30th tested working
###==================================================================
def modern_tab_shifter_to_left(the_nest_string):
    print("====modern tab shifter to left=======")
    starter_engine(the_nest_string)  #method call to get tabdepth on first switch line
    buildstring='';n = passthis[0] #filled from starter_engine method number of tabs in front of switch
    ### n is number of tabs in front of switch BEFORE CHANGING IT
    if n == 0: #means one(1) tab in front of switch do nothing
        buildstring =the_nest_string #no changes to indentation
    if n > 1: #more than one tab in front of switch so cut some tabs out
    # concatting the buildstring here 
        for line in the_nest_string.splitlines():
            buildstring += line[n:] +'\n' #this cuts out n tabs from the front of this line
    goldtime[0] = buildstring #output is in goldtime[0]
    #this prints out the result of the concatted uildstring
    for line in buildstring.splitlines():
        print(line)
    print('testing it now after changing the string')


##=================================
## take_out_switch_body(astring):  #def foxnews(astring):
##================================
def take_out_switch_body(astring): #this was foxnews
    print("take_out_switch_body      today is november 28th sunday  4:29 pm ")
    get_switch_and_endswitch_locations_in_string(astring) #for this switch string
    build_trial_inputlist()	 #this is new 
    convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)		

		#made nov 27th, satgurday 4:15pm morgan hill starbucks 
##===========================
## build_trail_inputlist()
##===========================
def build_trial_inputlist(): #this combines switch and endswitch into pair into trialinputlist
	del inputlist[:] #this empties the input list discarding previous data in it
	del trialinputlist[:]
	print("build_trail_inputlist()..")
	counter=0;
	for item in switch_list:
		pair=[switch_list[counter],endswitch_list[counter]]
		trialinputlist.append(pair)
		counter += 1
		
	print("look for the ball on the green")
	print("trialinputlist=",trialinputlist)
	for item in trialinputlist:
		inputlist.append(item)
	print("inputlist=",inputlist)
	for item in inputlist:
		print(item)
	inputlist.reverse() #is this needed here or not 

		
###========================================================================
## convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
###=========================================================================
def convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
    string_after_cutting_out_inner_switch_body[0]= False        #necessary default flag 
    counter=0 #where am I filling inputlist?
    for item in inputlist: #this grabs the params from item     #list of switches pairs start stop at 3 tabs depth
        start = item[0];
        finish = item[1];
        print('start=',start,'','finish=',finish)                       #62; finish=86 
        skip_rope_skipping_some_lines(stringname,start,finish)  #this copies the string skipping the range designated
        counter +=1
        print("counter=>>",counter)
        print("=====================")
    print("at bottom of converts  with more than one inner switch at 3 tabs")
    print("testing if weasel is returnable at the end of the function")	
		
		
switch_list=[]
endswitch_list=[]
total_switches_at_3tabs_depth=[]

#delete helper lists first
def delete_helper_lists_first():
	del total_switches_at_3tabs_depth[:]
	del switch_list[:]
	del endswitch_list[:]
	
#this gets the important switch and endswitch at 3 tabs length which is critical.
def get_switch_and_endswitch_locations_in_string(string_name):
	print("====||||  get switch and endswitch locations in string  ||||======")
	delete_helper_lists_first()
	#count how many switches at tab depth 3
	####=================
	switchcount=0
	counter = 0
	for line in string_name.splitlines():
	    tabdepth = line.count("\t")
	    if "switch" in line and "end" not in line and tabdepth == 3:
	        switchcount += 1 #doesn't have ++
	        total_switches_at_3tabs_depth.append(counter)
	        counter += 1
	        continue
	    else:
	        counter += 1
	        continue
	####===================
	print("total switch at 3 tabs in this string",len(total_switches_at_3tabs_depth))
	print("they start on these lines",total_switches_at_3tabs_depth)
	#count_switches_at_threetabs= string_name.count("
	counter=0; concatthis =''; #finish = finish + 1 
	print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'switch' in line and "end" not in line and tabdepth == 3: 
			switch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("phase 2 here ====")
	counter=0; concatthis =''; #finish = finish + 1 
	print("string_name=",string_name)
	#this looks for switch at 3 tabs depth and adds line number of switch
	for line in string_name.splitlines():
		tabdepth = line.count("\t")
		if 'endswitch' in line and tabdepth == 3: 
			endswitch_list.append(counter)
			counter += 1
			continue
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	print("end of line...")
	########################======
		
##===========================================================
## skip_rope_skipping_some_lines()  this cuts out ONE inner switch body
##===========================================================
def skip_rope_skipping_some_lines(string_name,start,finish):#start line nest switch and finish  endswitch
	print("start= ",start,"finish= ",finish)
	if string_after_cutting_out_inner_switch_body[0] == False: #starting
		print("it is False it is  empty ")
	else: 
		string_name = string_after_cutting_out_inner_switch_body[0]
		print('it is NOT False and therefore we fill the string from the list[0]')
	concatthis=''
	print("===skip_rope_skipping_some_lines(string_name,start,finish)====")
	#string_after_cutting_out_inner_switch_body[0]
	print(string_name)
	counter=0; #concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	print("string_name=",string_name,"start=",start,"finish=",finish)
	for line in string_name.splitlines(): 
		if counter > start  and counter <= finish: 
			print(line) #it won't print the switch word since it's skipping it
			counter += 1; continue
		else: 
			concatthis += line + "\n"; counter += 1; continue
	print('it created this SILLY STRING === multi colored silly string=')
	print(concatthis)
	print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
	weasel=string_after_cutting_out_inner_switch_body[0]
	for line in weasel.splitlines():
		print(line)
	#return weasel  #I need to return from each for the piping to work correctly
	lightning[0] = concatthis
	for line in lightning[0].splitlines():
	    print(line)

		
##=========
Tuesday, November 30th, 2021  2:10 PM PST Hollister,California Starbucks.
Previous version of indenting to left works without errors after extensive testing.

Fixed bug in cutting out body of inner switches. 
I can now run chain_methods on each string to prepare each of the input switch strings for bypass205().
This section started back in August. It's the last day of November and with persaverance I got it working.
Relieved. 


Tron Rises. Sat Nov 27th, 2021 5:19pm
Finally got taking out inner switch bodies at 3 tabs working. 
Now I will test changing to nested_switch method numbered . What an ordeal to get it stable. Works now.


9:22am Nov 23rd, 2021 PST
Tron Music
https://www.youtube.com/watch?v=I22AqV9zV50
	
Testing the chains methods thoroughly and chaining them together today.
They are each verified to be correct for all scenarios.
Total rush seeing it all come together.
This section deals with setting up the input switch strings for the parser bypass205() to handle a switch
with unknown numbers of nested switches initially at unknown depths until they are analyzed.


#testing
#INPUT STRING
spilled_coffee ='''
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 ==========
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #14
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 ===============
				case 'funny':
					print('fun')
				case "da":
					print('yeah')
				default:
					print('bye')
			endswitch #26 ==============
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====
'''	
#OUTPUT String
	switch(exp){   #1 === line 10 beginning of single nested switch ======      
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			switch(exp) #7 ==========
			print("nicely")
			break
		case "trouble":
			print("in trouble now")
			switch(exp) #19 ===============
		default:
			print("we are done here")
	endswitch #this is key here =============line 20 end of nested switch ====

stringname=spilled_coffee;  #this sucker was moving...pilots in ireland describing ufo zooming by.    
#start =1; finish=1; #this means start and finish unknown
modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start=1,finish=1)
print("did this sucker work tuesday november 23?")

#this was redesigned and modified on sunday november 21st at 8:30am to 
# work with skipping some lines with no known locations of inner switches at 3 tabs
# and it calls method build_pair_list to find them and reverse them for input for skipping_some_lines
# and I have to subtract 1 from start and finsh
#this one is used to get the main switch and take out switches at 3 tab depth
##===========================================================================
##  modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
def modified2_cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    ###======= this is ingenius=========
    #METHOD BUILD_PAIR_LIST(STRINGNAME) 
    # and loops thru list feeding start and finish  params and calling skipping_some_lines()
    #the input for start and finish will be 1 by default but they will be overwritten
    #by the build pair list on-the-fly.
    build_pair_list(stringname)           # goes thru thenewpairs list and
    for item in thenewpairs:              # fills start and finish into skipping_some_lines params
        start = item[0];finish = item[1]; # print("start,finish=",start," ",finish)
        skipping_some_lines(stringname,start-1,finish-1)#so close now 
    #this means that the output string should be placed into never_defeated[0]
    print("let us see what we have jazz blues.")
    for line in never_defeated[0].splitlines(): #prints it after takening out. 
        print(line)
	

flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
switch_list=[]
endswitch_list=[]
thenewpairs=[]

##============================
##  buildpairlist()  created nov 21st, sunday to manage doing the main switch 
##============================  and cutting out switches at three tabs for main switch 
def build_pair_list(stringname):
	print("====== build_pair_list called ======")
	counter =0
	#this fills up the switch_list line
	#===================================
	# LOOP FILLS UP SWITCH_LIST 
	#===================================
	#loop thru stringname and fill up switch list
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "switch" in line and "end" not in line:
			switch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	counter =0
	#loop thru stringname and fill up endswitch list
	#this fills up the switch_list line
	# =======================================
	# LOOP FILLS ENDSWITCH LIST 
	#========================================
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if "endswitch" in line :
			endswitch_list.append(counter)
			counter += 1
		else:
			counter += 1
			continue
	print("switch_list=",switch_list)
	print("endswitch_list=",endswitch_list)
	del switch_list[0]     #delete first switch number which is on line 1
	del endswitch_list[-1] #delete last number endswitch which is end of entire string
	print("after deleting first and last switch we have..")
	print("switch_list=",switch_list);print("endswitch_list=",endswitch_list)
	counter=0 #build the pairs and put them into sweet; then append sweet to thenewpairs list
	#===================================================================================
	# LOOP FILLS THENEWPAIRS LIST WITH SWEET WHICH HAS SWITCH,ENDSWITCH LINE NUMBERS
	#===================================================================================
	for item in switch_list:
		sweet=[switch_list[counter],endswitch_list[counter]]
		thenewpairs.append(sweet)
		counter += 1
	print("this is what we want to see at starbucks")
	print("thenewpairs=",thenewpairs)
	#==================================
	# LOOP PRINTS OUT THE NEWPAIRS LIST
	#==================================
	for item in thenewpairs:
		print(item)
		print('stop here for now')
		#exit()
	############################
	#REVERSE THE NEWPAIRS LIST BECAUSE IT HAS TO BE DONE BOTTOM UP TO THE STRING 
	############################
	thenewpairs.reverse() #they have to be skipped bottom up to work properly
	print("thenewpairs=",thenewpairs)	



##===========================================
##  skipping_some_lines() #this works
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("======= skipping_some_lines() ================called",start,finish)
	# if I have a flag that it's been triggered then afterewards 
	# print("this is the input string used stating skipping_some_lines")
	# for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
	#print('what is in baton[0]',baton[0])
	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
	# because the numbering system of the string starts from 1 too.
	### look that we have the counter here set to 1 by default 
	counter=1; concatthis =''; #finish = finish + 1 
	print("start=",start,"finish=",finish) #I took out x = 
	#smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	#print(smart)
	print("=== ah now I get it these are the lines that it MUST SKIP and we want what is before and after this range to create the modified string =")
	print("it sees in start",start)   #this is a number
	print("it sees in finish",finish) #this is a number too
	##=================
	#so I would build pair list of inner switches at 3 tabs and then loop thru them to skip them
	#this is new on sunday november 21st 2021
	#what I want to skip on the fly without range data
	
	#------------------------------------------------
	#from switch at 3 tabs until endswitch at 3 tabs
	#skip the lines inbetween leaving switch word
	##----------------------------------------------
	
	
	##=============== this is a new addition to automate the grabbing of inner switches ====
	# this creates pairs of the switch, endswitch pairs 
	#if start == 1 and finish == 1: #meaning figure out pairs on the fly
	
		
	#exit()
	counter=0
	#for item in thenewpairs:
	#	start  = item[0]; print("start=",start)
	#	finish = item[1]; print("finish=",finish)
		
	for line in x.splitlines(): #smart = x
			#this preserves the switch word and skips the rest of nested switch body including endswitch
			# if counter is between start and finish #just after start and less than = to finish
			#just added start +1 and finish + 1
			#tabdepth= line.count("\t")
			#if tabdepth == 3 and "switch" in line and "end" not in line:
			#		start = counter
			# use while loop of course
			#so it's upside down and backwards to create the same meaning.
			# probably need to do a prescan but maybe i can do it without doing prescan
			#get location of switch and endswitch at 3 tabs
			#while "endswitch" not in line:
			#####################==================
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
		##=======================================
	print("===output from skipping some lines====")
	#print('it created this string')
	#print(concatthis)
	print("how does it look===>>> by lettuce field")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	#this has red_robin hardwired into the code 
	#just commented out line below november 10th, 2021 to see wehat happens 
	#toosmart[0]= red_robin #it did say toosmart[0] = red_robin
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	print("now the result is here....!!!!@@@@@$$$$$")
	print(never_defeated[0])
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
	#exit()	
	#print(ibm[0])

	
	
	
	
	


9:26 am PST testing piping between chain methods now.
	
Piping works. Nov 20th, 2021  11:00am PST So chaining methods works. This means feeding the output from a method
as input for the next method in a chain (a line of methods).

Saturday, Nov 20th, 2021  9:06 am
Last major chain method confirmed working!

Flow Zone Trance concentration music:
https://www.youtube.com/watch?v=veHqJSC-9Lo
		

I will now pipe the methods together and apply them to each input string in list.
The rest is gravy and simple to impliment. Likely tomorrow morning the pre-parser code will be golden.
The half after the parser dealing with the python code is simple to put together with the methods already working.
INPUT sample strings looked like this:
		switch(exp) #11
		case 'blable':
			print("do something")
			####################
			switch(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47
=======testing if { taken out of string=======
confirmed switchh in line and tabdepth3
===== oh yeah =====

	switch(exp){ #49
		case 'burger':
			print("do something")
			####################
			switch(exp){ #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73

				
OUTPUT:
	===== oh yeah =====
we made it to the top of the Donnor Summit 
counter= 1

	switch(exp) #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_49(exp) #49

			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
counter= 2

	switch(exp) #11
		case 'blable':
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47
counter= 3

	switch(exp) #49
		case 'burger':
			print("do something")
			####################
			nested_switch_53(exp) #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73
counter= 4

	switch(exp) #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			nested_switch_23(exp) #23
			#############
			break
		default:
			print("we are done here")
	endswitch #38
counter= 5

	switch(exp) #53
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
	endswitch #64
counter= 6

	switch(exp) #23
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #33
end of the show time movie trailer

### code below

##===================================================
## change_switch_to_method_solved(inputstring):
##====================================================

#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    print("====== change_switch_to_method_solved(inputstring)=== get the money now====")
    innerswitch=''
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default se tting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    if innerswitch == True: #if a switch at 3 tabs depth  is True
    #check if { in this string if so take it out
        print('checking if left brace in string')
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine  +=   line.replace("{","") 
                    templine  +="\n"
                else:
                    templine += line +"\n"
            inputstring = templine
        #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
       #check if } in this string an if so take it out
      
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():
            tabdepth = line.count("\t") #gets tab count for this line
            #skips first switch by counter MUST BE AFTER 2nd line
            #this is where we swap switch(exp) with nested_switch_(number)(exp)
            if "switch" in line and tabdepth == 3 and "end" not in line and counter > 2: 
                print("confirmed switchh in line and tabdepth3")
                #this is new getting the switch id number after # on-the-fly
                #get string to right of #, get right side,remove spaces
                x = line.split("#"); y = x[1];y = y.strip();
                # replace switch with nested_switch + id number harvested from comment above
                thisline = line.replace("switch(exp)", "nested_switch_" + str(y) + "(exp)")
                #this removes the extra spaces after #
                location = thisline.index("#")    #gets location from left where position of #
                thisline = thisline[:location]    #this slices off the right side from # position
                thisline= thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else:
        print("no inner switches in this string")
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine += line.replace("{","") #taking out left brace here
                    templine  +="\n"
                else:
                    templine += line +"\n"           #otherwise it doesn't replace anything 
            inputstring = templine
        else:
            print("=====no { in string  ======")
            #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
        #check if } in this string an if so take it out #I have deactivated this since it's not needed
        
        #this is what we return the inputstring
        return inputstring; #no changes made 
    ### end of function =======================================================
    

    



###================== cold brew linus and snoopy ================== saturday morning software  november 20th, 2021 ====
#this is testing adding the nested switch 
linus_and_snoopy=[]
##==================================
##   add_nested_switch_methods():
##==================================
def add_nested_switch_methods():
    print("add nested_switch_methods() in catching_first_change list")
    for item in catching_first_change:
        print(item)
        #here calling method chaning_switch_to_method_solved swaps switch for nested_method_numbered
        fizz =change_switch_to_method_solved(item)
        print("===== oh yeah =====")
        linus_and_snoopy.append(fizz)
       



##================================================
##print_out_result_of_adding_nested_switch():
##================================================
def print_out_result_of_adding_nested_switch():
    counter =1
    print('we made it to the top of the Donnor Summit ')
    for item in linus_and_snoopy:
        print("counter=",counter)
        for line in item.splitlines():
            print(line)
        counter +=1

print("here we go... let her rip")       
add_nested_switch_methods()
print_out_result_of_adding_nested_switch()




Fri Nov 19th, 2021
Utter disbelief. Just fixed some code and got more working.
Adding working functionality on the fly to chain methods
shift to left works
cut out inner switch bodies works
both on the fly applied to a list.

https://www.youtube.com/watch?v=I22AqV9zV50   Tron music - pretty dam good.
getting cutting out the inner switch bodies had some simple but slightly perplexing logic bugs but
I ironed them out.

The rush is phenomenal seeing the nested switch starting to come to life. It's alive!

the first two methods were challenging. The second one was a real mother of a bitch. I just kept breaking
the code down to smaller methods to manage the complexity.

three more methods to go for chain methods. They work. Just making them work on their own now with no help.

#output looping thru list

now big test of second chain method #taking out switch bodies
this should print out 6 stritngs
counter= 1

	switch(exp){ #1
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){ #11
			exp = 3
			switch(exp){ #49

			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}

=========
counter= 2

	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #47

=========
counter= 3

	switch(exp){ #49
		case 'burger':
			print("do something")
			####################
			switch(exp){ #53
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #73

=========
counter= 4

	switch(exp){ #15
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			####################
			switch(exp){ #23
			#############
			break
		default:
			print("we are done here")
	endswitch #38

=========
counter= 5

	switch(exp){ #53
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
	endswitch #64

=========
counter= 6

	switch(exp){ #23
		case 'tahoe':
			print("do something")
			print("yep")
			fallthru
		case 'fallen leaf lake':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #33

=========
code working for taking out inners witch bodies before sending it to parser.
Will test convert inner switch to nested method next.
		
Raw code that works before cleaning it up. Fully worked just now.
		
		

flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
##===========================================
##            skipping_some_lines() #this works
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("skipping_some_lines() called",start,finish)
	#if I have a flag that it's been triggered then afterewards 
	#print("this is the input string used stating skipping_some_lines")
	#for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
	#print('what is in baton[0]',baton[0])
	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
	# because the numbering system of the string starts from 1 too.
	### look that we have the counter here set to 1 by default 
	counter=1; concatthis =''; #finish = finish + 1 
	print("start=",start,"finish=",finish) #I took out x = 
	#smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	#print(smart)
	print("=== ah now I get it these are the lines that it MUST SKIP and we want what is before and after this range to create the modified string =")
	print("it sees in start",start)   #this is a number
	print("it sees in finish",finish) #this is a number too
	for line in x.splitlines(): #smart = x
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		# if counter is between start and finish #just after start and less than = to finish
		#just added start +1 and finish + 1
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
	print("===output from skipping some lines====")
	#print('it created this string')
	#print(concatthis)
	print("how does it look===>>> by lettuce field")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	#this has red_robin hardwired into the code 
	#just commented out line below november 10th, 2021 to see wehat happens 
	#toosmart[0]= red_robin #it did say toosmart[0] = red_robin
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
		
	#print(ibm[0])
		#just moved this over one tab	
#end skipping_some_lines  ========================================================
print("Levels TEST on wonderful Monday winter wonderland ")
print("this will take out the inner switch between") 
never_defeated=[]
never_defeated.append(0)

for line in skitahoe.splitlines():
    print(line)

##===========================================================================
##  cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
##===========================================================================
def cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):
    print('this one is sooo critical')
    print("cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish):")
    skipping_some_lines(stringname,start,finish)
    #this means that the output string should be placed into never_defeated[0]
    for line in never_defeated[0].splitlines():
        print(line)
        
stringname=skitahoe; start=7; finish = 14; #this sucker was moving....    
cut_out_inner_switch_body_leaving_switch_word(stringname,start,finish)

print(" RED RED RED cut out switch body leave only switch word baby red alert testing cut out switch body leaving switch word tesitng 4 ..")    
#exit()

#this is testing with dummy data above in test_code_now
#taking out the inner switch body
print("halloween is coming snoopy and woodstock test")

#print(test_code_now)
#the inner switch is at 9 (which we keep) so we start from +1 meaning 10
#and the endswitch is at 19 but we need to nuke that too so it's endswitch + 1
print("take out 10 thru 20") #but actually keep 10 and takeout including20
#x = test_code_now
#the number system starts from 1 for the switch numbering
#because it starts counting from 0 and not 1 we need to subtract 1 from it
#so it was originally 10, 19

#if switch is #9 and endswitch is 19
#Add 1 to each number start and finish
print("rose test")








#modified so it doesn't matter where the inner switch is 
# they will all be at 3 tabs
#the first switch must be at 1 tab and inner switches need to be at 3 tabs one depth in
#THIS IS NEW CODE WEDNESDAY CODING...november 10th ........
##########################################################################################
#####################################################################################
 #creates first slot in list for string
	#print("actually this builds lists of switch and endswitch locations and makes pairs")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print("===========smart_cut_out_inner_switch_bodies_at_three_tabs=========")
	#print(" checking to see if more than ONE inner switch at three tabs and ")
	#print("if so then put them into a list")
	#print("the first loop determines how many inner switches at 3 tabs")
	#print("the second loop will go thru a list of the pairs - ah yes but ")
	#print("not implimented yet ")
	
	#print("it sees in finish",finish) #this is a number too
	

# "actually this builds lists of switch and endswitch locations and makes pairs")
# what it does: creates pairs set of start, finish after getting list of switch and endswitch lines
# then it will loop thru pairs set in reverse order and cut out switch bodies bottom up 


## new november 10th 2021 !!:37am
#JUST TRY IT


#this requires this function below to be called first though
#  smart_cut_out_inner_switch_bodies_at_three_tabs(samplestring)
pairset=[]
genius=[]
genius.append(0)

never_defeated=[]
never_defeated.append(0)
list_of_inner_switches_at_three_tabs=[]
list_of_inner_endswitches_at_three_tabs=[]




##========================================================
## loop_thru_pair_set_and_call_skiplines(samplestring)
##=========================================================
def loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring):
	print("len(never_defeated) =",len(never_defeated))
	#never_defeated[0] = thestring #this takes the initial string put into never_defeated[0]
	never_defeated.append(thestring) #maybe this is what I need to do to fix this bug
	print(never_defeated[0]) 
	counter =0
	#loop thru pairset of sets of switch,endswitch (already reversed to go bottom up)
	for item in pairset: #the pairset list was filled in smart_cut_out_inner_switch_bodies_at_three_tabs
		alpha = item[0];beta  = item[1];print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		#METHOD skipping_some_lines()============= uses never_defeated[0] stirng in list
		skipping_some_lines(thestring,start,finish)
		#doing this to see if it cut out the inner switch body 
		print("this is showing the changes reducing switches in never_defeated[0]")
		mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
		print("this is what the switch string looks like after taking out a switch body")
		counter += 1
	








##====================================================================
##  make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring)
##====================================================================
def make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):
	print("METHOD make_Pair_set_of #### called  ... make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):")
	counter =0
	print('let us look at this string to see what it sees')
	print("========//////////==========///////==============")
	for line in inputstring.splitlines():
		print(line)
	print("========//////////==========///////==============")
	for line in inputstring.splitlines(): #smart = x
		#this preserves the switch word and skips the rest of nested switch body including endswitch
		#for this line get tab_depth
		#print("this is where I add the switch line number to list of inner switches at three tabs")
		tab_depth= line.count("\t") #but this presumes just one inner switch there could be more
		#if 3 tabs True AND switch in line and end not in line and counter > 1 
		if tab_depth == 3 and "switch" in line and "end" not in line and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_switches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)		
	#second new loop but looks for endswitch locations at 3 tabs 
	counter =0
	for line in inputstring.splitlines(): #smart = x
		print(line)		
		tab_depth= line.count("\t")
		#print("this is where I add the endswitch line number to list of inner switches at three tabs")
		if tab_depth == 3 and "endswitch" in line  and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_endswitches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("==================")
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)	
	print("list_of_inner_endswitches_at_three_tabs=",list_of_inner_endswitches_at_three_tabs)		
	print("===================")
	print("===== end of phase 1 =====")
	##======================================================================================
	print('doing Friday debugging oh what fun it is to ride in a one horse open sleigh')
	if len(list_of_inner_switches_at_three_tabs) == 1:
		print("this means only ONE dam pair")
	else:
		print("the length is =",len(list_of_inner_switches_at_three_tabs))
		cat = len(list_of_inner_switches_at_three_tabs)
		print("the length of inner switches at three tabs is ",cat)
	###=================================================================	
	print("now I need to make pairs")
	get_number = len(list_of_inner_endswitches_at_three_tabs)
	
	if get_number == 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	##3=======================================================================		
	if get_number > 1: #it's only doing it if the gen_number > 1 daaaaaa
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	else:
		pass #print("there is only one switch endswitch so do regular mode just one inner switch at 3 tabs ")
	if get_number > 1:
		pairset.reverse()  # REVERSE PAIRSET SO THAT I CAN CHANGE THE INNER SWITCHES BOTTOM UP
	
	print(pairset)
	print("loop thru pairset") #to go thru input string and reduce inner switches to just switch word bottom up
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
	##======================================
	print("method to go thru pairset and call skipping_some_lines(start,finish)")
	#do_fancy_walk_thru_pairset_list_cutting_out_switch_bodes_bottom_up(inputstring):
	#########====================================
		#skipping_some_lines(genius[0],start,finish)
	#it goes thru the string and makes list of switch,endswitches
	
	#skipper needs to cut out from bottom up 
	#skipping_some_lines(x,start,finish):
	#it will call a method

#this must be called after one switch string has had it's inner switches reduced to switch word
#def reset_to_initial_conditions(): #brainchild on NOv 11th, Thursday morning#
#	print(" ====reset_to_initial_conditions()======"#)
#	never_defeated[0] =""
#	list_of_inner_switches_at_three_tabs=[]
#	list_of_inner_endswitches_at_three_tabs=[]
#	pairset=[]
#	baton[0]= "" #should clear it out
    

#def show_output_string_after_changes():
#    mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
#		print("this is what the switch string looks like after taking out a switch body")
#		print('resulting string change is for counter',counter)
#		for line in mouse.splitlines():
#			print(line)    
#this makes pairset list of switch and endswitch 
#this is only run ONCE
fullhouse=[]
##============================================================================
##  take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word
##----------------------------------------------------------------------------
##  Methods: make_pair_set_of_inner_switches_at_three_tabs_depth(thestring) oh wow genius here
##  Methods: loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
##  Methods: skipping_some_lines(x,start,finish)
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	print("THIS NEEDS TO WORK NOW==")
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("did this baby finally get called  1")
	print("called ....take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)") 
	make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
	print("this is scenario where if one inner switch it's not filling the pairset")
	print("pairset=",pairset)
	
	loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
	print("list_of_inner_switches_at_three_tabs=", list_of_inner_switches_at_three_tabs)
	print("list_of_inner_endswitches_at_three_tabs=", list_of_inner_endswitches_at_three_tabs)
	print("pairset=",pairset)
	print("this should be the result of the switch with inner switches cut to just switch word, bodies gone")
	for line in never_defeated[0].splitlines():
	    print(line)
	## adding resultof output of methods of taking out inner switches into never_defeated[0]
	## which is put into list fullhouse using append
	fullhouse.append(never_defeated[0])
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""
	



#print("====STARTING ATTEMPT 1====== charlie brown music is the best jazz ====")


#take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)


#exit() 
print("this is after the first string and taking out inner switch bodies...")
#print("====STARTING ATTEMPT 2====== charlie brown music is the best jazz ====")
#reset_to_initial_conditions()
	##==========================

##=======================
#take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestringzoo1)


#reset_to_initial_conditions() #this must be done after each transformation
print("the final OUTPUT is here ...")
print("length of fullhouse should be 2 is now",len(fullhouse))


#for item in fullhouse:
#    print(item)

####################################################
#print("size of FULLHOUSE is..",len(fullhouse))
#for item in fullhouse:
#    print(item)

print("time to go sledding")
#exit()


print("now I will try to do a few stings with it.") 
print("end of this initial test of ")
result_of_check_if_inner_switch=[]
result_of_check_if_inner_switch.append(0)

#coded on november 19th friday at 10:48 am morgan hill starbucks
##====================================================================
## determine_if_inner_switch_inside_of_this_switch_string(weasel):
##====================================================================
def determine_if_inner_switch_inside_of_this_switch_string(weasel):
    print("determine_if_inner_switch_inside_of_this_switch_string(weasel):")
    ## START INNER LOOP ======= devised on nov 19th friday 10L30 am ===========
    innerswitch= False #this must be set to False before each call below 
    result_of_check_if_inner_switch[0] = False
    for line in weasel.splitlines(): #this looks for an inner switch at 3 tabs depth
        tabdepth = line.count("\t")
        if tabdepth == 3 and "switch" in line:
            print("where's the party THIS string has an inner switch ")
            innerswitch = True
            result_of_check_if_inner_switch[0] = True
            break
        else:
            continue
        print("....")
    print('this has to be called after the loop is done')
    print("result_of_check_if_inner_switch[0]=",result_of_check_if_inner_switch[0])
    #end loop ===================


funtestlist=[]

print("big bird for prez")
print("testing in my mind wed november 10th test ..going thru list and calling take out switch bodies.")
funtestlist=[samplestring,samplestringzoo1] #samplestringzoo1
#use the list I made earlier catching_first_change

#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
def try_the_mocha():
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    print("let us see the strings in this list")
    for item in catching_first_change:
        print(item)
    print("===== okay is this it ===")
    
    print("length of catching first change should be 6",len(catching_first_change))
    counter=0  #this is running the method for second stage of chain_methods
    for item in catching_first_change: #funtestlist: #strings in funtest list
        weasel = item
        ## determines if there is an inner switch in THIS string ==========
        determine_if_inner_switch_inside_of_this_switch_string(weasel)
        #print("determine if inner switch at 3 tabs depth in this switch string ")
        innerswitch= result_of_check_if_inner_switch[0]
        print('innerswitch if true or false it is .. =',innerswitch)
        if innerswitch == True:  #if there is an inner switch then apply the method below  
            take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
        else:
            #this is new as of fri nov 19th 
            #if no inner switch then just add the switch string to fullhouse list
            #print("just added this in situation where no inner switches in string in list")
            print("========= nov 19th friday debugging ==")
            print("this is new ")
            print("if inner switch == False then add weasel to fullhouse")
            fullhouse.append(weasel)
            #this means no innerswitch in this switch string 
            pass  #it's False no inner switch
        counter += 1
        
        ###=========================================================
    print(" end of double loop ")
    print("after going thru catching first change list it should be 6 for counter")
    print("counter =",counter)
    print("len(fullhouse)=",len(fullhouse))
    print("let us look in here if switch stirngs with no inner switches okay and exist at least")
    for item in fullhouse:
        print(item)
    del catching_first_change[:]
    #this fills the output list into catching_first_change list 
    for item in fullhouse:
        catching_first_change.append(item)
        
    print("now big test of second chain method #taking out switch bodies")
    print("this should print out 6 stritngs")
    counter=1
    for item in catching_first_change:
        print("counter=",counter)
        print(item)
        print('=========')
        counter += 1
        
    

print("this is for all of the marbles out of style")
try_the_mocha()    
print('did it work razzle dazzle pumpkins')




	
	


Monday, Nov 15th, 2021
What this does is prep the string before it is fed into bypass205() which calls the parser individually
for each input switch string.
I already tested and verified that my pair list of switch endswitches works and that 
a list made up of the pairs is correct.

Testing chain methods individually then will test as a chain using piping now called do_pipe()
All of the methods in chain methods now verified to work.
do_pipe() works. Note. Python has a pipe() method for the os therefore I changed my pipe name to do_pipe().
Will next test chain_methods() together with all cylinders running. time 9:40 am. Nov 15th
	
	
Afterwards I will then work on post parser on python switch stings output combining.



Sunday morning nov 14th, 2021 working on method chaining still.

input=[]
input.append(0)

output=[]
output.append(0)


##=====================
##   get_final_finished_string()
##=====================
def get_final_finished_string():
    print("output[0]=",output[0])
    print("=== result is in output[0] ===")
    for line in output[0].splitlines():
	print(line)
    
##=====================
##   do_pipe()
##=====================
def do_pipe():
    input[0] =''
    input[0] = output[0]


##=====================
##   initialize_lists()
##=====================
def initialize_lists():
    input[0] =''
    output[0]=''
   
    
##=================================
## change_this_slot_string(counter)
##=================================
def change_this_slot_string(counter):
    counter = int( counter)
    nest_list[counter] = output[0]
   
    
##============================
## transform_string()    uses nest_list with strings in it of switch case bodies
##============================
def transform_string():
    counter =0
    for item in nest_list:
        chain_methods(item)           #this does the sequence of methods to one string 
        change_this_slot_string(counter) #this replaces the string in the slot with the modified string
        counter +=1

##==================================================
## loop_thru_finished_list_of_prepped_strings():
##==================================================
def loop_thru_finished_list_of_prepped_strings():
    counter =0
    for item in nest_list:
        print(item)
        print("counter=",counter)
        print("===========")
        #this will then append and build the quail list for input to bypass205()

# code name waterfall
##=======================
##  chain_methods()
##========================
#using descriptive names not true method names yet
def chain_methods(item):
    print("==== chain_methods called ====")
    initialize_lists() #clears out input[0] and output[0]
    input[0] = item #this captures the string 
    add_comment_with_number_to_top_switch(input[0]);do_pipe()
    shift_string_to_left_by_reducing_tabs(input[0]);do_pipe()
    cut_out_switch_bodies_at_3_tabs_depth(input[0]);do_pipe()
    swap_switch_with_nested_switch_number(input[0]);do_pipe()
    replace_the_last_endswitch_with_brace(input[0]) 
    get_final_finished_string() #in output[0] prints it out to see it










##=================================================================================

saturday morning, nov 13th, 2021
== Method Chaining ==
# I knew that Ruby had method chaining and thought it would be cool if Python could do chaining.
# of course it uses a some fancy code but it will work. It's a matter of how its implimented.
indent_to_left.add_comment_to_switch.cut_out_switch_bodies.swap_switch_with_nest_method.add_brace()
# it will be implimented like this:
method_chaining("method1.method2.method3.method4.method5()") #only way I can get away with using dots(.)
# put into a list in the same order as in the argument param
# it is fed the starting var data in list input[0]
# and the resulting result string is in  output[0]

I was thinking about applying each method individually to the list and looping thru 
it and thought that was inefficient and wondered if there was a way to simulate chaining to 
get the same effect and gain the efficiency and elegance of doing a chain of methods and 
just how it would work and be possible to impliment. 

Late last night an idea popped into my head and I quickly figured out how to make it work.
Chaining methods. For the pre-parser I need to call up to ten methods that are applied individually
to each string and that would have meant looping through all of the strings in a  list each time.
With this solution I just do one loop and apply the method chain to each string just once.
Wrote code at midnight last night and will test it today.

#Raw design code last night at midnight.
##======================================
## change_slot_string(counter)
##======================================
def change_slot_string(counter):
  counter = int( counter)
  nest_list[counter] = output[0] #nest_list is name of list that can become an input param

	
#A method that calls a series of methods really utilizing output from previous method
##======================================
## transform_string()
##======================================
def transform_string():
    counter =0
    for item in nest_list:
      chain_method(item)
      change_slot_string(counter)
      counter +=1

##======================================
## feed_data()
##======================================
def feed_data():
  input[0] =“”
  input[0] = output[0]


	
# waterfall #this will be generated
##======================================
## chain_method(item) 
##======================================
def chain_method(item):
  input[0] = item
  output[0] = method1(input[0]);feed_data()
  output[0] = method2(input[0]);feed_data()
  output[0] = method3(input[0]);feed_data()
  output[0] = method4(input[0]);feed_data()
  output[0] = method5(input[0]) 

	
#Result in output[0]
Indent to left margine
Add comment to switch
Cut out switch body at 3 tabs deoth
Swap switch with nested switch
Replace bottom endswitch with brace

Each method stage all five in sequence to a string

Chain the methods output to list[0]
Then that list is input to next method
Input[0] string method name
Put change into output[0]
Transfer then input[0] = output[0]





fri, nov 12th, 2021 11:30am
	
coding music today: https://www.youtube.com/watch?v=ckmh6FvHidQ
		
I need to loop thru the quail string list of nested switches and take out the inner switch bodies
and then replace the switch word that is an inner switch with a nested_method numbered.

Almost forgot. Found my code to indent initial switch strings that are deeply indented and reduces the
tab count so it is aligned correctly to the left margine with the proper indentation.

	
There are two phases involved here. The preparation of a switch string before it goes into bypass205
and secondly taking the output python generated code (for each switch string) from the parser and
combining them together for a switch with nested switches which is then finally executed.
First half is modifying the input JavaScript style switch string and preparing it for the parser.
Second half is adding elements to the output python switches strings and combining them.
I had to break the problem in half to manage the complexity. The first half I thought would take a week.
It has taken three months but I solved it so I am nonetheless still ecstatically happy.
The second half is super easy and works. I have done extensive testing of how and what the code will do
so I am 100 percent confident it will all work. The speed bumps have been the limitations of Python so I 
have been making methods to simplify the obfuscated nature and bizzare way that python does things.

#this is a sample of output python code generated by the parser 
#what remains is adding the def methodname at the top - added to the top of the string
samplecode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']

	inswitch(n) #3 
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			infallthru('test2')

		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			infallthru('test3')         

		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			infallthru('test4')

		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			inner_switch_2('test7') #commented out
			#######################
			print("out of inner switch 1")
			print("")
			break

		elif case in caselist5: #['google', 'fishfood', 'probability'] 
			print("successful test in casetest2")   
			print("solving the last few probs now") 
			print("oh my god it worked")     
			print("========= coolness ====")
			print('wow this is really sweet coding genius')
			break

		elif case in caselist6: #['test6']
			print ("gui design massive coolness test Starbucks")
			break

		#default:
		else:
			print('None')
			break
'''

def put_output_python_nested_switch_code_into_def_inner_switch_numbered(stringname):
	print('===== TESTING RED ALERT ======')
	print("put outpout python nested switch code into def inner switch numbered")
	#this calls a method to get this switch number to use to number this nested switch
	thenumber= get_switch_number_in_comment_in_output_python_code_string(stringname) #use other code similar to this
	#print("the number it returned is",thenumber) #thenumber=22 #for testing
	string_to_add= "def inner_switch_" +thenumber.strip() +"_(n):\n"
	concatstring = string_to_add + stringname;
	#print("lets see if it actually worked or not and concatted it correctly")
	##################################
	for line in concatstring.splitlines():
		print(line)
	flynow.append(concatstring) #so the resulting string modified exists.
	
#modified on november 12th 2021 friday to get this sucker working 
##====================================
##  get_switch_number_in_comment()  it gets the switch number from FIRST LINE OF STRING then bails
##====================================
#this looks ofr the first switch at 3 tabs need to modify it to 1 tab depth. aha 
def get_switch_number_in_comment_in_output_python_code_string(stringname): #this might be for when
	print("get_switch_number_in_comment_in_output_python_code_string(stringname)")
	print("indian braves dancing for rain")
	# I create copies of the switch body strings
	print("get_switch_number_in_comment_in_output_python_code_string() called it's getting the first inner swithc at 3 tabs length ")
	awesome=''
	y = ''
	counter =0  #say it's 3
	print("this is what the string we are manipulating looks like")
	for line in stringname.splitlines():
		print(line)
	print("================-------===")
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	#do I need to give it the line number as an input
	counter =0 #this looks for inswitch at 1 tab depth length 
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		tablength= line.count("\t")
		if "inswitch" in line and "end" not in line and tablength == 1:#and "#" in line and counter > 1: #just need to grab the first switch 
			#switchcounter += 1        #O just added" "#" in line and counter > 1
			x = line.split("#")  
			y = x[1];
			#str(y) #turns it into a string
			print("switch number ",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;	
	
Full steam ahead dash to the finish line in 5th gear.
Working on the transformation of the output python switch code which is a while True loop with ifs.
Reviewed my code and found and then rewrote code to add  "def nested_switch + number + (exp)" on top of
output python switch code. I then modified get number after inswitch() after # . That works smoothly now.

I still have a few more items to modify the switchcode to prepare it before it goes into the parser.
in quail list of separated string things to do (steps)
have to replace inner switches (cut out inner switch bodies leaving just switch word)
get number from  comment after switch of line number (that works)
Need to replace inner switch word with nested_switch method + number
take out excess tabs in front of switch cases so it's uniform
Have to make the main switch string with nested switches at 3 tabs replaced by methods

In review the parser is designed to do only one switch string and convert it into python representation.
Therefore I use a special extension called bypass205 that does any number of inputs switch strings
in a list and fills the stanford list but does not execute the code. They are each managed separately.

##======================================================================================================

Nested switches (that look just like C switch cases ... will be working by 
this weekend and the whole modules for switch and nested switch
will be on github. It's been a wild ride. What a roller coaster. So much logic. 

Massive momentum today after solving bugs late last night till midnight to outthink Python's peculiarities.
Super progress this morning got me over the hump and now I am going full speed ahead.
https://www.youtube.com/watch?v=sRvEwXDxz_I
	
https://www.youtube.com/watch?v=ZwY4YPxTufs
	
https://www.youtube.com/watch?v=FbbCHWQZ70o

I will start sending the seperated strings to the parser in bypass205 likely tomorrow. What a rush. I am so thrilled
by my recent progress. 

Thursday, Nov 11th, 2021  10:36am PST
What a rush. By the way it also takes out braces if they exist. Next I will loop thru the list of seperated strings and apply this to each switch string
that has more than one switch within it meaning at least 1 switch. So it will test for if string.count("switch") >= 2 and string.count("endswitch") > 1
swap inner switches to methods works automatically for all switches at 3 tabs length in a string.
I wrote it on halloween and just retested it.
INPUT example 

jazz6='''
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #77  
			#############
			break
		case 'what':
			print("nice")
			####################
			switch(exp){ #88  
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86   look this is endswitch chnaged to brace later
'''
OUTPUT
	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			nested_switch_77(exp) #77
			#############
			break
		case 'what':
			print("nice")
			####################
			nested_switch_88(exp) #88
			#############
			break
			
		default:
			print("we are done here")
	endswitch #86
Yes, I know wait what about the input for (exp) for each switch. I will add that line above later. it's trivial.

Code to do the magic.
print("about to do thorough testing of chnage_switch_to_method_solved()")
#solved october 29th, 2021  NEXT get the number after comment just in time
'''
this builds a string called newstring replacing switches
at 3 tabs depth with nested_switch
with the comment id after # tacked onto
 the end of the nested_switch_22(exp) like so.
'''
#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    print("====== change_switch_to_method_solved(inputstring)=== ====")
    innerswitch=''
    for line in inputstring.splitlines():
        print(line)
    print("========testing if this input string has a nested switch ==")
    innerswitch= False #default se tting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    ##########################################
    print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    if innerswitch == True:
    #check if { in this string if so take it out
        print('checking if left brace in string')
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine  +=   line.replace("{","") 
                    templine  +="\n"
                else:
                    templine += line +"\n"
            inputstring = templine
        #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
       #check if } in this string an if so take it out
         ##################################################            
       # if "}" in inputstring:  #have to cut "}" out of string      
       #     print("CONFIRMED there is a right brace in string")
       #     for line in templine.splitlines():
       #         if "}" in line:
       #             
       #              templine2 += line.replace("}","")
       #              templine2  +="\n" 
       #        else:
       #             templine2 += line +"\n"
       #    inputstring = templine2
       #     print("======testing if } taken out of string======")
       #    for line in inputstring.splitlines():
       #        print(line)
       #     print("======testing if } taken out of string======")
         #end if   
       # do nothing
       ######================================
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():
            tabdepth = line.count("\t") #gets tab count for this line
            #skips first switch by counter MUST BE AFTER 2nd line
            #this is where we swap switch(exp) with nested_switch_(number)(exp)
            if "switch" in line and tabdepth == 3 and "end" not in line and counter > 2: 
                print("confirmed switchh in line and tabdepth3")
                #this is new getting the switch id number after # on-the-fly
                #get string to right of #, get right side,remove spaces
                x = line.split("#"); y = x[1];y = y.strip();
                # replace switch with nested_switch + id number harvested from comment above
                thisline = line.replace("switch(exp)", "nested_switch_" + str(y) + "(exp)")
                #this removes the extra spaces after #
                location = thisline.index("#")    #gets location from left where position of #
                thisline = thisline[:location]    #this slices off the right side from # position
                thisline= thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else:
        print("no inner switches in this string")
        if "{" in inputstring: #have to cut "{" out of string
            print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine += line.replace("{","") #taking out left brace here
                    templine  +="\n"
                else:
                    templine += line +"\n"           #otherwise it doesn't replace anything 
            inputstring = templine
        else:
            print("=====no { in string  ======")
            #end if
        print("=======testing if { taken out of string=======")
        for line in inputstring.splitlines():
            print(line)
        print("=======testing if { taken out of string=======")
        #check if } in this string an if so take it out #I have deactivated this since it's not needed
        ''' ##################################################            
        if "}" in inputstring:  #have to cut "}" out of string      
            print("CONFIRMED there is a right brace in string")
            for line in templine.splitlines():
                if "}" in line:
                     templine2 += line.replace("}","") #this is where I was taking } out
                     templine2  +="\n"
                else:
                     templine2 += line +"\n"
            inputstring = templine2
            print("======testing if } taken out of string======")
            for line in inputstring.splitlines():
               print(line)
            print("======testing if } taken out of string======")
         #end if 
        '''
        ########################################
        #this is what we return the inputstring
        return inputstring; #no changes made 
    ### end of function ===============================
    
print("where is my mocha brainfreeze test october 30th...")

print("==========testing string da===================")
print("=============================")


And testing code here:
	
inputstring=''
inputstring = da         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
    
print("=============================")
print("======= testing string data1======================")
    
    
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data1         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
    print(line)
    
print("=============================")
print("========testing string data2=====================")


inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data2     
#what I am doing here is returning the concatted string to the string fizz variable.    
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)

##==================
print("about to test data3 and I can't have anything after the #22 after switch")
inputstring=''
print("====== second test but no inner switch here ===")
inputstring = data3         
fizz=change_switch_to_method_solved(inputstring)
print("===== oh yeah =====")
for line in fizz.splitlines():
   print(line)





thursday, nov 11th, 2021 9:09 am Pacific Time
Cutting out inner switch bodies at 3 tabs works on-the-fly automatically. sweet. 
This is yet another victory in the tranformation of the input switch code to prepare it for the parser.
Next I will swap out the inner remaining inner switch words with a nested_switch numbered.
This morning had some weird bugs and they were only rectified by using listname.clear() 
The method loops thru a list of the strings which are in a list of the separated switch strings.
#I will beautify the code later. Just getting it all working right now.

funtestlist=[samplestring,samplestringzoo1] #samplestringzoo1
#ratmaze_list=[]
#=====================
#  try_the_mocha()
#=====================
def try_the_mocha():
    print("try the mocha() testing.......... running the rat maze and learning it...")
    fullhouse.clear()
    counter=0
    for item in funtestlist:
        take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(item)
        counter += 1
    print("len(fullhouse)=",len(fullhouse))
    for item in fullhouse:
        print(item)
	
try_the_mocha() ##<<===== method called
##============================================================================
##  take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word
##----------------------------------------------------------------------------
##  Methods: make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
##  Methods: loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
##  Methods: skipping_some_lines(x,start,finish)
##============================================================================
def take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring):
	print(" take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(thestring)")
	baton[0]=thestring
	print("did this baby finally get called  1")
	print("called ....take_out_nested_switch_bodies_at_three_tabs_depth_leaving_switch_word(samplestring)") 
	make_pair_set_of_inner_switches_at_three_tabs_depth(thestring)
	loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring)
	print("list_of_inner_switches_at_three_tabs=", list_of_inner_switches_at_three_tabs)
	print("list_of_inner_endswitches_at_three_tabs=", list_of_inner_endswitches_at_three_tabs)
	print("pairset=",pairset)
	fullhouse.append(never_defeated[0])
	#if it is here then it's called ONLY after the first one has completed and thereafter
	#==================================================
	## this resets super important lists utilized 
	never_defeated[0]=''
	list_of_inner_switches_at_three_tabs.clear()
	list_of_inner_endswitches_at_three_tabs.clear()
	pairset.clear()
	baton[0]= ""

##====================================================================
##  make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring)
##====================================================================
def make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):
	print("did this baby finally get called  2")
	print("METHOD make_Pair_set_of #### called  ... make_pair_set_of_inner_switches_at_three_tabs_depth(inputstring):")
	counter =0
	for line in inputstring.splitlines(): #smart = x
		#print(line) the line still exists even if I don't print it out
		#this preserves the switch word and skips the rest of nested switch body including endswitch
		#for this line get tab_depth
		#print("this is where I add the switch line number to list of inner switches at three tabs")
		tab_depth= line.count("\t") #but this presumes just one inner switch there could be more
		#if 3 tabs True AND switch in line and end not in line and counter > 1 
		if tab_depth == 3 and "switch" in line and "end" not in line and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_switches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)		
	#second new loop but looks for endswitch locations at 3 tabs 
	counter =0
	for line in inputstring.splitlines(): #smart = x
		print(line)		
		tab_depth= line.count("\t")
		#print("this is where I add the endswitch line number to list of inner switches at three tabs")
		if tab_depth == 3 and "endswitch" in line  and counter > 1: #proceed
			#this puts the current line number into the list below
			list_of_inner_endswitches_at_three_tabs.append(counter)
			counter += 1
		else:
			counter += 1
	print("==================")
	print("list_of_inner_switches_at_three_tabs=",list_of_inner_switches_at_three_tabs)	
	print("list_of_inner_endswitches_at_three_tabs=",list_of_inner_endswitches_at_three_tabs)		
	print("===================")
	print("===== end of phase 1 =====")
	print("now I need to make pairs")
	get_number = len(list_of_inner_endswitches_at_three_tabs)
	if get_number > 1:
		#create pairs   THIS IS CONSTRUCTING THE PAIRSET LIST OF SWITCH ENDSWITCH LINE NUMBERS
		counter=0
		for item in list_of_inner_switches_at_three_tabs:
			pairs = [ (list_of_inner_switches_at_three_tabs[counter]) , list_of_inner_endswitches_at_three_tabs[counter] ]
			print(pairs)
			pairset.append(pairs)
			counter += 1
	else:
		pass #print("there is only one switch endswitch so do regular mode just one inner switch at 3 tabs ")
	pairset.reverse()
	print(pairset)
	print("loop thru pairset") #to go thru input string and reduce inner switches to just switch word bottom up
	for item in pairset:
		alpha = item[0];
		beta  = item[1];
		print("alpha=",alpha, "beta=",beta)
		
		
##========================================================
## loop_thru_pair_set_and_call_skiplines(samplestring)
##=========================================================
def loop_thru_pair_set_to_cut_out_inner_switch_bodies(thestring):
	print("did this baby finally get called  3")
	print(" =============== the waving American Flag ===========")
	print('right here never_defeated length = 0 meaning it is empty')
	print("len(never_defeated) =",len(never_defeated))
	#never_defeated[0] = thestring #this takes the initial string put into never_defeated[0]
	never_defeated.append(thestring) #maybe this is what I need to do to fix this bug
	print(never_defeated[0]) 
	counter =0
	#loop thru pairset of sets of switch,endswitch (already reversed to go bottom up)
	for item in pairset: #the pairset list was filled in smart_cut_out_inner_switch_bodies_at_three_tabs
		alpha = item[0];beta  = item[1];print("alpha=",alpha, "beta=",beta)
		start = alpha; finish = beta
		#METHOD skipping_some_lines()============= uses never_defeated[0] stirng in list
		skipping_some_lines(thestring,start,finish)
		#doing this to see if it cut out the inner switch body 
		print("this is showing the changes reducing switches in never_defeated[0]")
		mouse = never_defeated[0] #the result of skipping some lines goes into never_defeated[0]
		print("this is what the switch string looks like after taking out a switch body")
		counter += 1
	

	
pairset=[]
genius=[]
genius.append(0)

never_defeated=[]
never_defeated.append(0)
list_of_inner_switches_at_three_tabs=[]
list_of_inner_endswitches_at_three_tabs=[]


flag_test=[]  
toosmart=[]
toosmart.append(0)
baton=[]
baton.append(0)
 
flag_test.append(False) #set flag_test by default to False
#flag_test[0]
# x is the name of the string to be modified
##===========================================
##            skipping_some_lines()
##===========================================
def skipping_some_lines(x,start,finish):#input string, switch number then endswitch line number  ....start line nest switch and finish  endswitch
	print("METHOD  skipping_some_lines() called==========")
	print("skipping_some_lines() called",start,finish)
	#if I have a flag that it's been triggered then afterewards 
	#print("this is the input string used stating skipping_some_lines")
	#for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
		smart=x;
		#change it to True now
		flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
		#what this does is use the new concatted changed string changed on the fly with each pass
		#for second and all subsequent passes it uses baton[0]
		x = baton[0]
	#print('what is in baton[0]',baton[0])
	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	# changed it to start counter from 1 instead of 0 on Oct 5th, 2021
	# because the numbering system of the string starts from 1 too.
	### look that we have the counter here set to 1 by default 
	counter=1; concatthis =''; #finish = finish + 1 
	print("start=",start,"finish=",finish) #I took out x = 
	#smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	#print(smart)
	print("=== ah now I get it these are the lines that it MUST SKIP and we want what is before and after this range to create the modified string =")
	print("it sees in start",start)   #this is a number
	print("it sees in finish",finish) #this is a number too
	for line in x.splitlines(): #smart = x
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		# if counter is between start and finish #just after start and less than = to finish
		#just added start +1 and finish + 1
		if counter > start+1 and counter <= finish +1: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish  we are cutting out these lines of code
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
	print("===output from skipping some lines====")
	#print('it created this string')
	#print(concatthis)
	print("how does it look===>>> by lettuce field")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	#this has red_robin hardwired into the code 
	#just commented out line below november 10th, 2021 to see wehat happens 
	#toosmart[0]= red_robin #it did say toosmart[0] = red_robin
	baton[0] = concatthis  #here the concatthis has been put into baton[0]
	##==========================================================
	### mocha test ### this is new November 10th, 2021  ########
	never_defeated[0]= concatthis  #just added this line 
	###########################################################
	##==========================================================
	concatthis='' #this resets concatthis to empty-
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
		
	#print(ibm[0])
		#just moved this over one tab	
#end skipping_some_lines  ========================================================


#INPUT

samplestring ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch  #======== ============38
			fallthru
		
		default:
			print('the end')
}
'''	


samplestringzoo1 ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch  #========== 20  ==========notice this for it is key 
			print('taught me how to write code')
			fallthru
			print('hello world')
			switch(exp){  # ===== 24===== 3 tabs, 2nd case , line 2 in this case, 1 in series
				case 'rats':
					print("do autumns")
					print("yep")
					fallthru
				case 'more':
					print("badness")
					break
				default:
					print("we tesla done here")
			endswitch  #========== 34  ==========notice this for it is key 
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======39       
				case 'autumn':
					print("falling leaves")
					print("a night on the town ")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much cranberries")
			endswitch  #======== ============49
			fallthru
		
		default:
			print('the end')
}
'''	

#OUTPUT


	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
			print('taught me how to write code')
			fallthru
			
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======28       
			fallthru
		
		default:
			print('the end')
}


	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){  # ===== 10 ===== 3 tabs, 2nd case , line 2 in this case, 1 in series
			print('taught me how to write code')
			fallthru
			print('hello world')
			switch(exp){  # ===== 24===== 3 tabs, 2nd case , line 2 in this case, 1 in series
	
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new ======39       
			fallthru
		
		default:
			print('the end')
}

#did it work razzle dazzle pumpkins

Wednesday, November 10th, 2021
PUtting code up on github in case my laptop dies. As an emergency backup.
Lots of files. Code nearly done, days away, but I don't want to risk losing it if my laptop crashes.

Gaining Steam and accelerating. I now have momentum and it feels great seeing it reach completion.
I have the following working and connected.
Go thru input multi switch string
make pairs list of switch and endswitches by tab depth
add sublists together for one list of switch, endswitch pairs
separate switch strings using pairlist and put nested string into a list

if a switch string has a nested switches at three tab depth then reduce switch bodies to just switch word.
Next I will add the methods to replace inner switch with nested_switch_numbered making it into a method.
This now works using fuzzy logic and can deal will multiple inner switches. I used my macro trick
and change the string from bottom up so that the pair numbers are still valid that I used to access the string.

#hardest parts over, the rest I have working methods and functions so I'm just methodically putting it together.
#greatly relieved it's going well and coming together and crystalizing nicely. 
Past few days have been tremendously productive in THE ZONE. Likely it will be all working by this weekend at this point
and uploaded to the web on github. Grateful I have not given up. The key for me was reading from the Practical Programmer
and testing with "made it here, etc" that helped localize bugs faster. And I read that Elon Musk used to write big functions
and his new programmers' task was managing the code better putting parts into methods. So I started breaking down massive 5 
page functions down to half a page and creating methods. I really like methods they are easier to grasp their mechanics.
This has helped me tremendously to manage the complexity and reuse more code more easily.
I am 100% confident that the nested switch feature will work now. Again all of the working code exists. I'm just
connecting the modules and testing it to death and adding error detection.



Friday, November 5th, 2021 11:34 am Morgan Hill, California Starbucks
	
Methodically going thru code pieces to verify everything is working.
The first objective is taking the big string of switches and cutting it up and putting
each switch case body into a list as a string.
I also have to get the switch, endswitch pairs for the whole string and put those line numbers into a list.
Initially it was in a dictionary.

Copying a switch body works given params starting line and ending line within a string
(this is key since I need to cut out each switch body and put it into a list for further transformation)
Cutting out switch body using skipping and keeping switch word works.
Create pair set of switch ,endswitch works.
I have a working dictionary but decided to use a list of sublists instead for absolute simplicty.
Adding comment and line number after each switch works.
Creating threetabs, fivetabs,seventabs,ninetabs switches works.
Combing all of the tab lists works using extend()

I decided I will construct it in sections in a separate file to reduce the code complexity.
I will do this rather than trying to have the whole thing work together which would not go well.
I am doing the gradual construction this way to isolate bugs that are localized by design.

I am working on the construction of the working code in stages to reduce the complexity and reduce the juggling.



12:20 PM  Nov 4th 2021
	
I will add all of the code in one file in a few days to github for the nested module.
This was a bit more complex than I ever imagined to get it to perfectly mimic C switch cases.
I will add the feature of the floating default anywhere within a switch case later.

https://www.youtube.com/watch?v=ZRSNy8DcIDk
	
	
	
SUMMARY OF PLAN OF ATTACK #all of the functions and methods work for this to happen. 

Each puzzle piece component currently works right now

determine if switch string has more than 1 switch in it

loop thru switch string and add comment with line number after each switch

create range list of pairs of switch endswitch line numbers from initial string of nested switches

using range list(pairs)  COPY each switch at it's tab depth to endswitch and put into quail list

loop thru quail list and CUT out inner nested switches bodies leaving just switch word (referred to as SKIPPING) thru concatting

loop thru quail list and replace inner switch with nested_method + line number in the comment that it grabs on the fly

##=====================================

#what I worked on this morning was creating a method to grab the commented line number from the first switch in a string
in quail list which will then be accessed in the same order in the stanford list where the python output string will be
I will then add indentation and use the number in the list to put into the def nested_switch_ (number) that completes
the construction of each nested string. I have the cake layer code that concats all of the methods together bottom up and
then it's executed and *should* fully work as it (has been) in testing preparing for this moment.

These are the steps that will be welded together likely tonight.

going thru the entire mega switch string a comment is added after each switch like so:  switch(exp){ # 33  
and the number added using replace is the respective line number within the mega initial strating switch string
	
the triggering of the nested switch functionality (gear box) is triggered by bypass205() omage to bypass of Portland in Oregon
if switch count in string is > 1 and endswitch count > 1; if True then proceed with bypass205()
and all bypass205 does really is call the same methods to convert a string into python but appends it to a list
instead of executing it.

	
first part = create list of pairs of switch, endswitch numbers called rangelist and referred to as pairs also
this involves taking the big combo switch string with nested strings and locating the location of each switch and endswitch pairs
based on their respective tab depth before the word switch and endswitch
the pairs list looks like pairslist=[[1,100], [22,33],[44,56]]
the key is that the pairslist is organized in a specific prescribed fashion of one tab, three tabs, five tabs etc
the reason for this is in case there are several (branches) starting at 3 tabs within the body of the main switch at tab 1.

using the rangelist several different methods will manipulate the switch strings in a sequence in stages.

#COPY switch strings and append to quail list
looping thru the rangelist copy each switch to endswitch at the same tab depth
and append each switch string to a list
	
#SKIP switch string body of inner switch strings (cut them out essentially) this is done by concatting the string to manipulate it

Next looping thru the list 
each switch string is reduced to only one level deep nesting by cutting out the inner switch body but leaving the inner switch word
#example
switch(exp){ #22
   case "will work":
	print("nice")
	exp = 2
	switch(exp){ # 33  <<=== notice only the switch word remains the body has been cut out
	print("every nice")  #also notice that the depth within a string is only at 1 tab and 3 tabs
	
Then the inner switch word is converted into a nestedswitch method with it's id number and braces are removed
switch(exp) #22
   case "will work":
	print("nice")
	exp = 2
	nested_switch_33(exp) # 33  <<=== notice only the switch word remains the body has been cut out
	print("every nice")

What is going on is that each set LEVEL is managed by representing a template copy in a sense of
one level switch with a 2nd level nested switch as a method
and this is repeated for each set and in python each switch is it's own separate nested method numbered to prevent name clashes.
however the method methods for the first switch at the top in a string have a nested method added after going thru the parser
		
	
	

Thursday, Nov 4th, 2021  10:40am Morgan Hill, California
	
https://www.youtube.com/watch?v=sRvEwXDxz_I
	
https://www.youtube.com/watch?v=jofkDRNetdw	
	
good coding music

I wrote some brilliant code yesterday that is beautiful and works. 7 hours straight.


peartree=[]
startime=[]
#loop thru threetabs
print("TEStING PeAR TREE backyward with plum tree to see if it works")
print("add result to final_pears_list")
print("does this one work and print x,y")
#my_list = [1,2,3,4,5,6,7,8,9,10]
print("about to see if christmas will come early this year or not")

##======================================
## fill_main_pear_list(listname):
##=====================================
def fill_main_pear_list(listname):
    print("=====fill_main_pear_list called with listname======")
    counter=0 #this must be at 0
    for x in listname:
        print(listname[counter],listname[counter +1])
        jazz = [listname[counter],listname[counter+1]]
        startime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 #notice counting by 2
        if counter >= len(listname): #prevent from going out of bounds
            break
    print("startime list=",startime)
    print("what did this work.......or not ....did it")
    #put in list highest tab number say 7
    if holding_themax[0]== 7:
        fill_main_pear_list(threetabs)
        fill_main_pear_list(fivetabs)
        fill_main_pear_list(seventabs)
    
    if holding_themax[0]== 5:
        fill_main_pear_list(threetabs)
        fill_main_pear_list(fivetabs)
    
    if holding_themax[0]== 3:
        fill_main_pear_list(threetabs)
       
       
       
print("final startime filled with three tabs, five tabs, seven tabs in pairs")
print("battle star galactica")
print("startime=",startime)

 
listinput=[]
first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot

second=[]   #this takes an inputstring which is the combined switchcase big string
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
#  this uses internal_machinery() method in loop below
##========================================================
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    themax = max(add_tab_depth) #gets the biggest number in the list  calculated
    holding_themax[0] = themax #stored to use elsewhere
    print("themax=",themax, "which is the highest tab number before a switch in string")
    #this dynamically creates listinput of tabs
    print("======")
    if themax == 3: listinput = [3]
    if themax == 5: listinput = [3,5]
    if themax == 7: listinput = [3,5,7]
    if themax == 9: listinput = [3,5,7,9]
    if themax == 11:listinput = [3,5,7,9,11]
    if themax == 13:listinput = [3,5,7,9,11,13]
    if themax == 15:listinput = [3,5,7,9,11,13,15]
    print("listinput=",listinput) # dynamically filled based on the max tab count #3,5,7
    for item in listinput: # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)  #calls internal_machinery()(
    print("==done==")
    print("threetabs="   ,threetabs); print("fivetabs="    ,fivetabs);
    print("seventabs="   ,seventabs); print("ninetabs="    ,ninetabs);
    print("eleventabs="  ,eleventabs);print("thirteentabs=",thirteentabs)
##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]

inputstring = red_robin
print("what red_robin looks like before calling try_all_three=====")
print(red_robin)
print("see how it looks above if there are double switches and endswitches yet")
this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)


print("testing looping thru list")
#this represents a list of sublists of the switch,endswitch pairs
testlist=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]

returnlist=[]
returnlist.append(0)
#I can make my own custom methods to get from list
#the list is actually referenced starting from 1 where I start the counter
##==============================================
##  get_pair_from_testlist(x):
##==============================================
def get_pair_from_testlist(x):
    print("=========get_pair_from_testlist=========")
    print("testing get_pair_from_testlist",x)
    counter = 1
    print("inside the loop we see for x this ",x)
    for item in testlist: #it doesn't really loop, it's a one pass loop
        #if number entered bigger then length of list warn then break    
        if x > len(testlist): #error detection bypass worked 
            print("ERROR went beyond number length in list")
            print("please enter a number less than ",len(testlist))
            break
        #if number entered less than 1 warn then break
        if x < 1: 
            print("ERROR number must be 1 or higher")
            break
        if counter == x: #it matched with a doable number
            print(item)
            alpha = item[0]
            beta  = item[1]
            print(alpha,beta)
            returnlist[0] = [alpha,beta]
            print("returnlist[0] =",returnlist[0])
            break
        else:
            break
##==============================================================

            
get_pair_from_testlist(1)
get_pair_from_testlist(1)
print("the pair is ",returnlist[0][0],"really cool",returnlist[0][1])
get_pair_from_testlist(-1)
get_pair_from_testlist(0)
get_pair_from_testlist(2)
get_pair_from_testlist(3)
get_pair_from_testlist(4)
get_pair_from_testlist(5)
get_pair_from_testlist(6)
get_pair_from_testlist(7)
get_pair_from_testlist(22)

#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    for item in tabsubs:
        tabcount.append(item)
    del tabsubs[:]
        
        
        
tabsubs=[]
threetabs=[]
fivetabs=[]
seventabs=[]
ninetabs=[]
eleventabs=[]
thirteentabs=[]
fifteentabs=[]
#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("==========internal_machinery() called======")
    print("inputstring",inputstring);print("tabsubs ",tabsubs, " ",x)
    counter=0
    for line in inputstring.splitlines():
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
        if tab_length == x: 
            if "switch" in line and "end" not in line:
                tabsubs.append(counter);counter += 1;continue
            if "endswitch" in line:
                tabsubs.append(counter);counter += 1;continue 
    print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:print("nada")
    print("3 and 5 tabs    =",threetabs ," ",fivetabs)    
    print("7 and 9 tabs    =",seventabs ," ",ninetabs)   
    print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   
 
       

listinput=[]
first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot

second=[]   #this takes an inputstring which is the combined switchcase big string
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
#  this uses internal_machinery() method in loop below
##========================================================
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    themax = max(add_tab_depth) #gets the biggest number in the list  calculated
    holding_themax[0] = themax #stored to use elsewhere
    print("themax=",themax, "which is the highest tab number before a switch in string")
    #this dynamically creates listinput of tabs
    print("======")
    if themax == 3: listinput = [3]
    if themax == 5: listinput = [3,5]
    if themax == 7: listinput = [3,5,7]
    if themax == 9: listinput = [3,5,7,9]
    if themax == 11:listinput = [3,5,7,9,11]
    if themax == 13:listinput = [3,5,7,9,11,13]
    if themax == 15:listinput = [3,5,7,9,11,13,15]
    print("listinput=",listinput) # dynamically filled based on the max tab count #3,5,7
    for item in listinput: # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)  #calls internal_machinery()(
    print("==done==")
    print("threetabs="   ,threetabs); print("fivetabs="    ,fivetabs);
    print("seventabs="   ,seventabs); print("ninetabs="    ,ninetabs);
    print("eleventabs="  ,eleventabs);print("thirteentabs=",thirteentabs)
##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]




#twin list 
wrote code to get first switch id in the comment before it's sent thru the bypass205() and turned into python
the list of switch id numbers in order will be utilized for creating the nested_switch numbers

Oh. Yesterday I nixed the idea of using a dictionary which has weird rules and bugs so changed
back to using a list with sublists for managing the pairs of switch endswitch pairs.
I then made a get() method for grabbing pairs from the list.

worked on dynamically building the combininglist of tabs which is used throughout the code to manipulate switch strings.
example
it will take in the max tab length for a switch in a given string as input
and based on that number determines how many of the tablists to add
if just 3 then just threetabs
if it is 5 then it adds together threetabs and fivetabs
first time I've ever used the extend method and happy it worked, was vexing before discovering extend

combinedlist = threetabs + fivetabs + seventabs #this looks dirt simple but doesn't work like this in a function (oh darn)
this can handle up to fifteentabs but it can be as much as desired, artificial stop at fifteen tabs for switches initially.
		
The purpose of the combinedlist is is is utilized throughout the preparser to grab with the pairs
the switch strings which are seperated using the combinedlist itself.

example of the function in test mode
#dummy code for testing ....
threetabs=[[22,33],[44,66]]
fivetabs =[[55,58],[77,86]]
seventabs=[[88,99],[102,110]]

combined_tabs=[]

#testing purposes
# this adds the tabs lists like threetabs + fivetabs + seventabs into combined_tabs list
print("== snowmen having snowball fight==testing build_tab_list_added_together(x):======")
##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("called build tab list added together")
    print("larget_tab_number =",largest_tab_number)
    del combined_tabs[:] #clears out the combined_tabs list to erase it
    if largest_tab_number == 3:
       combined_tabs.extend(threetabs)
           
    if largest_tab_number == 5:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)
            
    if largest_tab_number == 7:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)        
    
    if largest_tab_number == 9:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs) 
        combined_tabs.extend(ninetabs)        
    
    if largest_tab_number == 11:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)
        combined_tabs.extend(ninetabs) 
        combined_tabs.extend(eleventabs) 
    
    if largest_tab_number == 13:
        combined_tabs.extend(threetabs)
        combined_tabs.extend(fivetabs)  
        combined_tabs.extend(seventabs)
        combined_tabs.extend(ninetabs) 
        combined_tabs.extend(eleventabs)
        combined_tabs.extend(thirteentabs)         
    
#this calls it  
     
build_tab_list_added_together(3) #produces togetherlist=threetabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)
print("======= ")
 #clear it out 
build_tab_list_added_together(5) #produces togetherlist=threetabs + fivetabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)

build_tab_list_added_together(7) #produces togetherlist=threetabs + fivetabs + seventabs   
print("combined_tabs=",combined_tabs)
for item in combined_tabs:
    print(item)






Wednesday, November 3rd, 2021 11:42 am
Home Strech. I nixed using a dictionary and am using a list with sublists for the switch endswitch pairs.
Making custom methods so it does the same thing as the dictionary methods. I find it simpler and cleaner than using the dictionary.

Testing each stage of the process of getting the switch and endswitch pairs. 
After the indendent stages work by themselves connecting them
will take just a few minutes.

Essentially doing massive testing and simplying and
slight refactoring right now. 

In summary working on testing and streamlining taking in the input code
and preparing it for the parser string before it's sent into bypass205() 
and the rest is gravy. I am thrilled it's going to work. 


Monday, November 1st, 2021 8:42 am
All Systems Green. 
When the code works it feels like this: 
https://www.youtube.com/watch?v=sX1Y2JMK6g8
	
All that is remaining is connecting the last few puzzle pieces(already working) that put the output python
switch strings into their respective methods and adds indentation and concats in cake layers and executed.


Worked on and refined replacing inner switch word with dynamically built nested_switch which uses the comment id line number
which is added on the fly. I also replace the endswitch with the } brace conforming to C and JavaScript.
Conversion of inner switches works for n number whether none, 1, or many - any amount flawlessly.

this:
	switch(exp){ #62
		case 'burger':
			print("do something")
			####################
			switch(exp){ #66  
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	endswitch #86   
				
#######################################################	
is transformed into this: this is then as a string added to a list that is then
fed thru the parser which triggers bypass205(x) which translates each string seperately into python code
				
	switch(exp) #62
		case 'burger':
			print("do something")
			####################
			nested_switch_66(exp) #66
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
	} #86   
			



Thursday, October 28th, 2021 11:56am
Working on testing and ensuring that I can fill the dictionary(struct) record with data
and then access it on-the-fly accurately. The dictionary is loaded from a list of the switch pairs.
Recently worked on proof of concept walking thru steps and connecting parts to make sure that the chain of events
is accurate and in the right order. Testing with actual data to ensure that bypass205() is correct.
Working on the final stages now. at the point of the lunar module about to land on the moon. will continue testing
each separate stage to ensure it works independently (to avoid conflict) and then connect the constellation together.
Super close. I also need to work on next the cleaning up of the python string generated of switch code that
needs to be put into methods named by the switch id number. Just need to test it.
Unreal feeling making it this far. Unimaginable complexity so I had to continue breaking down sections into smaller parts
to manage the intense complexity.



Wednesday, October 27th, 2021   11:47am Morgan Hill, California Starbucks
In C for a switch case ... the default statement doesn't have to come at the end. It may appear anywhere in the body of the switch statement. 
I figured out how to make this behavior work so default can be anywhere in the switch case. Simple solution.
In summary, for the switch case implimentation in Python staying true to form of C the default can be anywhere within
a switch case and doesn't have to be at the bottom of the cases. It can be anywhere. I have previously thought it wasn't possible
and then today the simple solution popped into my head. Just move the default to the bottom of the switch case before putting it
thru the parser. It doesn't matter (really) where the default resides if there are no case matches it's irrelevant where the default is
but being able to represent the switch case wholly how it's represented in C is still a great honor. 

I have been walking through the transformation of the nested switches and feeding the split up combo swith string in seperate
file into the bypass205() parser and now working on putting those python output switch strings into the final stage.

Victory is within my grasp now.


#important code that is involved endswitch(), bypass205(), parserguts()
#Monday, Oct 25th, 2021 2:25pm
What I have been working on diligently  is making the code that will automatically split up a combo string
of multiple switches into separate switches and for this to work I had to figure out how to organize and manage
the location of each switch endswitch pair and add that to a dictionary which is used elsewhere.
To prepare the individual switches and the each switch so that it only has one level deep of nesting so
if a switch starts at 3 tabs it can only have five tab indentation switches so one level of depth within it
and then the nested switches within it at 5 tabs (for this example) need to have their switch bodies removed
(after copying them) and then just leave the switch word. All of the switches are numbered by their intitial line
number automatically with a comment which is used to track and manage them. So once the inner switch bodies is
taken out by copying the string and skipping after the position of the switch word down to and including its endswitch
then the remaining switch words needs to be replaced with a nested_method utilizing the unique initial line number comment
that was previously inserted. I am at this point where I replace the inner switch with a nested method that is numbered.
Though I have been a bit anxious to test that the bypass was still working flawlessly that I got working back in June of this
year since I had recently gained some momentum with progress.  And in the past few days I finished several monumentally
complex functions of code to make the transformation seamless preparing the nested switches to be cleaned up and formatted
before running through bypass205 which converts them into python code that next need to have the swich strings put into
the unique method names. 

#code to test bypass205 taking in 3 strings in quail list as input in JavaScript mode
#testing here running 3 strings in quail thru bypass205
print("============== red white and blue time ===========")
del quail[:]
print("length of quail list=",len(quail))
quail.append(str1)
quail.append(str2)
quail.append(str3)
print(" JAZZ MUSIC TIME code test of bypass205() it's been a long wait indeed")
print("printing what is in quail list right here for this test")
for item in quail:
    print(item)
    print("===++====++===")
y='' #normally this takes in the input string for testing I make it empty since the strings are fed into quail list
bypass205(y)    
print("then we look in the stanford list")
print("======output from Stanford List======")
for item in stanford:
    print(item)

print("======= end of stnaford going down Palm drive now=====") 
print("======== Code Blue Exit =====") 
print("  === end of red white and blue ========================")
exit()


nested_switches_count=[]
nested_switches_count.append(0) #so by default it's [0] in position 0
nested=[]
nested.append(False) #loaded with False in nested[0] by default starting

# so it would be True if nested is true
	#for this test we pretend that we have already seperated the big switch string
	# into sepeate strings and they ahve been placed into the quail list
	# #but I can do it here later, with y as input
	# for right now in this phase the quail list has already been filled
	# and we have determined that nestwich is True
########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	print("==== endswitch () called...======")
	print("let us see what is in y passed into endswitch")
	print("============")
	print(y)
	print("============")
	switchcasetester='';switchcasetester=None;
	del switchcasetester;switchcasetester='';
	mytrace("endswitch() in switch_cat called")
	show_input_switch_string() #flag for testing this shows the input string
	#check  if nested switches
	print("count how many endswitches in string")
	answer = y.count("endswitch") #it counts endswitches here 
	do_nested_switch_count()
	print("if answer = 0 continue moss beach one string test ")
	print("the number of endswitches in the input y string is",answer)
	nested_switches_count[0] = answer #maybe int(answer) counts endswitches in string y input to endswitch(y) 
	############### new nearly 9pm ###########################
	# Thursday, August 26th, 2021 12:27pm 
	# inside of original_stage1.py inside of left folder
	# still need to add the methods to make this section work
	# which fills up the quail list that will be fed into bypass205
	# #this is the section that I'm working on right now ===
	# WORKS not added yet : make pair_list here of pairs of switch endswitch 
	# WORKS not added yet : then  loop through pair_list to fill quail list
	# quail list of strings  using copy_string if at least one endswitch in input string
	# Need to fill quail list with these switch bodies strings
	#################
	#========================================================
	print('=====')
	###========= testing this august 4th 2021 ==================================
	print("here we go, leaping into the == Grand Canyon == will it fly?")
	## test to do bypass205 if nested switches > 1
	#bypass205 is only called if there  is at least one endswitch inside of the input string
	# for endswitch(x) above
	# requires nested[0] to be True or False (True to call bypass205(y)
	###########################################
	if nested_switches_count[0] > 1: #based on number of endswitch count
		nested[0] = True; 
		print("what is in nested[0]",nested[0])
		print("bypass 205 CALLED IN ENDSWITCH biggest test yet to make sure that his works----")
		#this goes thru the quail list that is filled beforehand above
		#this method is only called if there are nested switches
		print("quail list must have at least a length of 2")
		###############
		bypass205(y)  #<<== this manages nested switches  
		###############

	else:
		nested[0] = False; 
		print("===bypass205 NOT CaLLEd  only one string, no endswitches===")
		pass
	###===========================================
	#this section is only run if a string switch string NOT NESTED ONES
	print("so this would be skipped if nested switch string combo bypass")
	if nested[0] == False or answer == 0:#all of this below is skipped if nested = True
		print("the string will be parsed and codegened - it doesn't have any nested switches")
		check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
		if baseline[0] != "nada": #means it converted to uppercase
			y = baseline[0]
		#end if
		flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
		print("if number in first case",valve[0])
		if valve[0] == True:    #meaning numbers like case 12:
			macro_expansion(y); #checks if macros used and expands them and converts numbs to strings
			y=None; del y; y = cray[0]; 
		#end if
		flush_lists() 
		parser_mode_1(y) ### <<===== parser_mode_1() called here 
	else:
		pass
	################## normal endswitch 

####====== BYPASS205() ======== ###
# stanford list is filled in the code generator at the bottom
#######################################################################
########### bypass 205 ########### july 1st 2021 testing starbucks in gilroy
#premise is that quail list has more than one switch string in it
#for bypass205 to work so a minimum of 2 switch strings

    #######     #######    #######
          #     #     #    #
        #       #     #    #
       #        #     #    #######
     #          #     #          #
    ########    #######    #######     
#=========================================
##  bypass205(y)   #this requires that the quail list is already filled with switch strings
######################=========
def bypass205(y): 							# runs input strings thru parser and  
	print("=========bypass205() called===========")
	print("quail input list of switch strings has a length of ",len(quail))
	print("if len(quail)>= 2: you are good")
	if len(quail) >= 2:
		print("GREEN LIGHT SUFFICIENT quail requirement met")
	else:
		print("RED LIGHT insufficient quail list is only 1 in length")
	print("====")
	###==== error message if insufficient list length for quail ===
	if len(quail) < 2:# quail list requires 2 or more in length of switch strings
		print("error message in bypass205")
		print("quail list needs minimum of 2 strings to work in quail list")
		return  # don't go forward if the quail list is too small
	else:
		pass   
	mytrace("bypass205()") 					# code gen puts in stanford list
	del stanford[:] 						# empties  stanford list 
	# this swaps the endswitch out and puts in } at end of switch
	# this is dependent on quail list already being filled with strings
	# loop thru quail list and apply parser guts for each string
	todo_after_putting_strings_into_quail_before_starting_bypass205()#replaces endswitch with }
	print("right here we are going thru the quail list and manipulating the strings as y individually")
	
	for item in quail: 						# loop thru quail list 
		y = item 							# this puts the contents of each string in quail into y 
		###==========================sept 2nd test 2021
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		show_input_switch_string() 			# flag for testing this shows the input string
		parser_guts(y)  					# does parser and codegen of each switch string        
		#stanford list is filled here 
###  end bypass205()  ################## 


#parser guts is the same sequence of code in the endswitch above
# I am just trying to reduce code  that's all.
####============================
####      parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("====== parser_guts called =======")
	check_if_uppercase_constant_cases(y)	#if UPPCASE this senses it and converts to string
	if baseline[0] != "nada":				#means it converted to uppercase
		y = baseline[0]
	flow_valve_input1(y)					#puts True or False into valve[0] added April 2nd, 2021
	print("if number in first case",valve[0])
											# macro expansion is only called if numbers are True
	if valve[0] == True:					#meaning numbers like case 12:
		macro_expansion(y); 				#checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
	flush_lists() 
	parser_mode_1(y) 	

###==================================	
	

#################################
##     flow_valve_input(y)
##################################
def flow_valve_input1(y):  #this determines if switch case string is numbers or words
    print("======Flow Valve input1(y) ======")
    mytrace("flow_valve_input()")                            # get first case in switch case string
    getline  = grab_first_case_of_switch_string(y)           # get first case line
    toocool  = grab_first_case_line_in_switch_case_string(y) # remove tabs from the case line
    toocool  = remove_tabs_from_string(toocool)              # test if number in first case line yes = True no = False
    valve[0] = check_if_number_in_string(toocool)            # looks in case line
    valve[1] = toocool                                       # put case name/number into valve[1]
    print("output from FLOW VALVE=",valve[0],"and",valve[1])
################################################


###########################
##     parser_mode_1()
###########################
def parser_mode_1(a):  ## testing April 3rd 2021 seeing if this works or not. 
	print("====== parser_mode1(a) =====",a)
	mytrace('parser_mode_1 in switch_cat()') #was greatpumpkin
	#print('=======INSIDE OF PARSER in switch_cat for strings  =========')
	mountain2(a)    # this changes sw to switchcasetester #I can't beleive that this reverse number was being called 
	starter_sequence_mode_1()
# flow_fork_input()  #this fills valve[0] with True or False
# if valve[0] is True  it means numbers = True  (thus numbers      )
# if valve[0] is False it means numbers = False (thus words strings)
## the new code will go in here Friday morning.. April 2, 2021
#this fills valve[0] with True or False for numbers in cases




Monday, oct 25th, 2021 1:49pm.
Just did a successful test of bypass205() which resides inside of the endswitch() method that
is called if there is more than one switch case. I fed it three strings that were in the quail list
and it dutifully ran them thru the parser and put them into the stanford list.
So successful test.
Input strings followed by translation into python version of the switch case in the new implimentation.
So moving forward now. Next I need to connect the individual components that I have been working on for
months that gets the switch and endswitch and tab depths for the entire input string and puts the combinations
into a list as pairs of line numbers based on one tab, three tabs, five tabs, seven tabs, etc and then 
puts the pairs in order into a dictionary (got that code working recently).

I was working on creating methods that now work to copy the inners switches and put them into a list.
Then taking out the inner switch bodies leaving just the switch word and then replacing that with a method name
after retrieving the comment id number after the switch. Sounded like cake walk but wasn't quite that simple.

# input strings in the quail list that is the result of these switches having been separated from
# their original combo string.

str1 = '''
	switch(exp) {  #1
		case 1:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4: 
			print('kangaroo hop hop!')
			n = 'more' #testing
			nested_switch_2(n)  #maybe keep it a comment until it's in python        
			print('taught me how to write code')
			fallthru
			
		 
		case 8:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
			break
}
'''
#notice I am using the } with no tab but no endswitch here either

str2 = ''' 
	switch(exp){   #2       
		case 'blable':
			print("do something")
			print("yep")
			fallthru
		case 'more':
			print("nice")
			break
		default:
			print("we are done here")
			break
} 
'''

str3 = ''' 
	switch(exp){  #3        
		case 'zoo time':
			print("san francisco zoo")
			print("feed the flamingos")
			fallthru
		case 'the beach in santa cruz':
			print("volleyball and boardwalk")
			break
		default:
			print("we are done here")
			break
} 
'''


python output after going thru first phase of parser
#======output from Stanford List======
#this is output of looping thru the stanford list with 3 strings in it
exp = varholder[0]

caselist1 = ['1']
caselist2 = ['4']
caselist3 = ['8']
caselist4 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['1']
		print("where's the dog house!")
		print('first prize')
		print('you block head Charlie Brown')
		fallthru('4')

	elif case in caselist2: # ['4']
		print('kangaroo hop hop!')
		n = 'more' #testing
		nested_switch_2(n)  #maybe keep it a comment until it's in python        
		print('taught me how thru write code')
		fallthru('8')

	elif case in caselist3: # ['8']
		print('mocha blast')
		print('== 31 flavors===')
		fallthru('default')

	elif case in caselist4: # ['default']
		print('the end')
		break

	else:
		print('the end')
		break



exp = varholder[0]

caselist1 = ['blable']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['blable']
		print("do something")
		print("yep")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



exp = varholder[0]

caselist1 = ['zoo time']
caselist2 = ['the beach in santa cruz']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['zoo time']
		print("san francisco zoo")
		print("feed the flamingos")
		fallthru('the beach in santa cruz')

	elif case in caselist2: # ['the beach in santa cruz']
		print("volleyball and boardwalk")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break






Monday, Oct 25th, 2021 12:24pm
I was going through my files and reviewing it and I chanced on my test code I wrote back in June.
It shows what is ultimately being generated in terms of the inner switches and main switch.
Also I wanted to state that in essence what this program does is create the illusion that Python
has switch cases that can be nested and look exactly like C and JavaScript switch cases in all repects
with the same running behavior.  So in essence this program is translating JavaScript/C/Lisp syntax
into Python indirectly.

Each nested switch lives in a method with a unique id name which will be its initial line number in the input string
before it's parsed. The main switch is in a method for main_switch(exp) which will be at the bottom and the nested
switches will be above it and the way that it works in reality is all of the switches are put into a docstring multiline
and executed so they are all essentially within a bubble separate from the rest of the code that it resides within.


This is a test file that runs that is what is actually produced after translating the input JavaScript
switch cases into python and put into methods. This is an example of a triple nested switch case and 
how it's impimented as python in Python which doesn't have a switch or case in it.

#this is the output running the code below. input is x="one" in testfunction(x) triggered by real_main() at bottom

=== testfunction called with x====TESTING THIS JUNE 9th=======  one
test function testing switch case behavior
this is the first case in the main switch
=......======inner_switch called==1= .....= test7
go for tahoe
out of from innerswitch1 below
tahoe[0]= tobagan
this is back in main switch now !
go reindeer
=== this is 2nd nested swith differnet case switches have ended
=======inner_switch called==2== snowman
this is inside of inners witch test2
switch case behavior works in Python now!
None
out of from innerswitch2 below
tahoe[0]= tobagan

######### end of output of running the Python code below ############

#################################
# value you want to run thru switch case

global x
x = "one" #it was "one"              #<<=== x must be a string just as matching case == "string", 
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
tahoe=[]
tahoe.append(0)
# =======  real_main()  ===================================
def real_main():  #calls testfunction(x)this callst testfunction(x)
    testfunction(x)  #"one" is tested

victory=[]
victory.append(0)

#######################
### inner switch_1
#######################
### this is inner_switch()
def inner_switch_1(n): #test2 is the test
    print("=......======inner_switch called==1= .....=",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    inswitch(n)                  #<<====== inswitch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')

        elif case  == "test2":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break                    #<<===== fallthru() method is here *don't use* break with fallthru()
                                     #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":       #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("go for tahoe")
            tahoe[0]="tobagan" #puts victory into tahoe[0]
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
            infallthru('snowman')

        elif case  == "snowman":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            infallthru('test3 ')        #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "rabbit":
            print ("te what do we have here ool...")
            tahoe[0]="mickey mouse" #puts victory into tahoe[0]
            print("tahoe[0]",tahoe[0])
            #######################
            #inner_switch_2('test7')
            #######################
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


#to simulate passing in data to a nested switch 
input_nest=[]
input_nest.append(0)

casetest1 =['google', 'fishfood', 'probability']

#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
# this is a function with a switch case
# which has a nested switch case within it inside of a function called inner_switch_1





# =======   testfunction    ========================
def testfunction(x):
    print("=== testfunction called with x====TESTING THIS JUNE 9th======= ",x)
    print('test function testing switch case behavior')
#this is the switch called 
# ==   main    ======  switch case code =======================
    switch(x)                           #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("this is the first case in the main switch")
            input_nest[0] = 'test7'
            ######################
            inner_switch_1(input_nest[0]) #force feeding it for testing switch case function actually 
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
            inner_switch_2('snowman') #force feeding it for testing switch case function actually 
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


# ====   end of switch case  ======================
#        end testfunction

if __name__ == "__main__":
    real_main() #this calls real_main()
  




Monday, Oct 25th 2021  11:02 am
	
Working on creating separate component puzzle pieces (small programs) that I will test independently
before wiring them together in a small subsystem. I will soon test running the output nested strings that
have been filtered into the bypass205() method to convert into python. I will write down the steps
for the flow of control and then see how close it is. The next phase after that is adding a method name
to each of the nested strings based on the nested switch which has the id comment number at the top
and then concatting each of these methods into a big string in the building cake upside down so the main switch
is at the bottom. Nearly finished. What an ordeal. Mind warping complexity and problem solving to "discover" a workable
solution. The conversion functions to add the method name and ensure the indentation is correct and the cake layer
builder code all already work. 

Learning the fine art of reducing complexity by breaking up complicated functions into smaller functions
and making tricky parts into separate methods. Momentumn regained - relieved.
I prefer starting method names with a verb which is much more descriptive.

I refer to a dictionary as a struct which is essentially a record in C.

add_data_to_struct("2","fast")
print(dictionaryname)

get_this_x_in_struct('year')
	
	
	
	
	
	
Fri Oct 22nd, 2021  7:54 am.
	
In cruise control now. Moving forward effortlessly.
Added functionality to convert inner switches at 3 tab depth into nested methods based on their embedded comment number
Reduced the function to not even require a method so it's done on the fly freeing from a method call.
Improved simpler design to do the change on-the-fly.

# what this represents is one of the final phases before running the INPUT JAVASCRIPT switch case string 
# thru the bypass205() in the parser that converts a list of nested switch stings into Python 3

# this replaces the inners switch at 3 tabs with a nested method name with the id comment number -added previously
# it will access a list using a loop and they will be put in in sequential order top down
# this can handle any number of nested switches at 3 tabs
##======================================================================
##  convert_inner_switches_into_nested_methods_numbered(stringname): 
##=======================================================================
def convert_inner_switches_into_nested_methods_numbered(stringname): #this is feeding in the number looking for
	x='';concatthis='';counter =0
	for line in stringname.splitlines(): #this shows the starting condition of the string to be changed
		print(line)
	#modified this and got it working correctly on friday, oct 22nd morgan hill 2021
	for line in stringname.splitlines():
		tabdepth = line.count("\t")
		if  tabdepth == 3  and "switch" in line:
		# I just moved what was in a method into the loop where the action happens
			x = line.split("#")  
			y = x[1];       #it was str(ournumber)
			y = y.replace(" ",'')
			filler ="nested_switch_" + str(y) +"(exp)" #has to be a string
			line = line.replace("switch(exp){",filler) #notice replace method using var filler
			concatthis += line + "\n"
			counter += 1
			continue
		else:
			concatthis += line  + "\n"
			counter += 1
			continue
	################	
	for line in concatthis.splitlines():
		print(line)	
		
#Note: yes there will be an exp = number before each switch; I was just focusing on functionality of the conversion

convert_inner_switches_into_nested_methods_numbered(string_egg) 
#### input string ############
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			switch(exp){ #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			switch(exp){ #33 
			#############
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
##### output string #############
	switch(exp){ #11
		case 'blable':
			print("do something")
			####################
			nested_switch_15(exp) #15
			#############
			print("yep")
			fallthru
		case 'more':
			print("nice")
			####################
			nested_switch_33(exp) #33 
			#############
			break
		default:
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs
pumpkin express
####### input string ############
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			switch(exp){ #25
			#############
			print("yep")
			fallthru
		case 'more':
			switch(exp){ #34
			print("nice")
			switch(exp){ #45
			break
		default:
			switch(exp){ #66
			print("we are done here")
	endswitch #60   4..........endwitch 4  line 60 3 tabs

				
				###### output string after conversion #######
	switch(exp){ #22
		case 'blable':
			print("do something")
			####################
			nested_switch_25(exp) #25
			#############
			print("yep")
			fallthru
		case 'more':
			nested_switch_34(exp) #34
			print("nice")
			nested_switch_45(exp) #45
			break
		default:
			nested_switch_66(exp) #66
			print("we are done here")
	endswitch #60   4..........endwitch 4
		


Tue Oct 19th, 2021  5:25 pm Gilroy, California
I can now cut out the nested switch bodies of the switch strings in the list of separated switches.
What I am doing is I put the the main switch and cut it up by tab depth of inner switches.
Then I go thru each of the switch bodies that have inner switches at level three tabs and take that switch body out
leaving just the switch word.
I then replace that inner switch word with a nested_switch method which is numbered by the original switch line number.

I can now replace the inner switch with a method automatically.
Getting closer to finishing ...
So much testing. 
The disbelief is awe inspiring. I didn't expect it to actaully work as designed and it's totally beautiful.
It's a dream seeing it all come together and actually work as designed. 



This is what the JavaScript switch case code looks like before it's converted into python.
If you notice I transform the inner switches into methods that keep the inner switches separated.
Again this is what the string of the switch looks like before it goes thru the parser that translates
it into python strings. However, the initial switch code allows many levels of nested switches just
like in JavaScript. If you notice there are "thru" and "to" macros that work with numbers. And the fallthru
feature works too. A user can use break or fallthru. Further for the management of the complexity each switch
is actually unique and has an id number based on it's initial line number which is how it's referenced.

switch(exp) {  
	case 1 thru 3:
		print("where's the dog house!")
		print('first prize')
		print('you block head Charlie Brown')
		fallthru
			
	case 4 to 7:
		print('kangaroo hop hop!')
		nested_switch_1(n)  #sample of nested switch 
		print('taught me how to write code')
		fallthru
			
		 
	case 8 to 10:
		print('mocha blast')
		print('== autumn nest===')
		nested_switch_2(n)         
		fallthru
		
	default:
		print('the end')
	}


October 17th, 2021 8:44 am   Morgan Hill, California
On verge of finishing. Reviewing the method bypass205() which takes in the switch input strings and converts them
from JavaScript style switches into Python code one by one in a list. 
Yesterday when I got the code working to convert each input string to left justify with just one tab in front of the
switch at the top for all configurations it occurred to me I had succeeded - since it was the last hurdle.
Pure nirvana. 
This code is the second working design to shift a nested string to the left margin
##=================================
##  manipulate_string(addstring)
##=================================

def manipulate_string(addstring):
    #the objective is to reduce tabs so only 1 tab in front of first switch in string
    cutout=''
    #why can't I just go thru the string and replace the first three tabs with ""
    print("======manipulate_string=======")
    print("getting tab count in front of first switch here")
    for line in addstring.splitlines():
        if "switch" in line and "end" not in line:
            tabsinthisline = line.count("\t")
            print("the tabs in front of first switch are",tabsinthisline)
            #the objective is to have only 1 tab in front of first switch
            # which then propogates down the length of the entire string
            if int(tabsinthisline) > 1:    #example
                
                cutout = tabsinthisline -1
                print("tabsinthisline =",tabsinthisline)
                print("cutout =",cutout)
                break
                
            if tabsinthisline == 1: #which means do nothing we want just 1 tab first
                cutout = -1;
                break
            
            if tabsinthisline == 0:
                break
                
             # do nothing   193241613
     #take out just 2 tabs
    print("now doing SECOND phase of manipulate_string")
    super=''
    for line in addstring.splitlines():
        #if "switch" in line and "end" not in line:
        tabsinthisline = line.count("\t")
       # print(line,tabsinthisline)#first is 3 so subtract 2
        #it does all lines of the string taking out the first 2 tabs which are chars
        
        
        if cutout != 0  or cutout > 0:#this handles if cutout = 0 meaning None
            sliced = line[cutout:] #this can be a variable
        else: #this means its == to 0
            #this is for the scenario of zero tabs in front of first switch starting
            if tabsinthisline == 0:#this handles if there are zero tabs in front of switch line
                #here we need to add a tab if there are zero tabs.
                sliced = "\t" + line;#meaning don't cut any tabs out
            else:
                sliced =  line; 
        super += sliced + "\n" # this does all lines in the string
        
        #this is for the scenario of it's already perfect at 1 tab length in front of switch
        if cutout == -1:
            super += line 
        #end if
    print("================ taking out 2 tabs quickly and dirtily")    
    for line in super.splitlines():
        print(line)

print('testing cutting out first two tabs from front of string')
print("moving everythign to left side for formatting this sucker see if gold nears")


testlist_of_strings=[]
testlist_of_strings.append(teststring1)
testlist_of_strings.append(teststring2)
testlist_of_strings.append(teststring3)
testlist_of_strings.append(teststring4)
testlist_of_strings.append(teststring5)
testlist_of_strings.append(teststring6)
testlist_of_strings.append(teststring7)

print("===== testing this using a loop =====")
counter=0
for item in testlist_of_strings:
    print("counter =",counter)
    manipulate_string(item)
    counter += 1



Friday, Oct 15th, 11:33am
Good progress last night till 11ish too.
Progress straightening out (formatting) switch strings in nest_list.
I can control the indentation on the fly which I need to turn each into a method. 3 lines of code.
That's what I like about Python. Zen is waiting to be discovered when coding in Python.
Feeling energized now. Daily chipping away at the boulder. 
My approach is breaking everything down into small modules that I focus on to reduce the complexity
and to maintain momentum. 




Thursday, Oct 14th, 2021 8:14pm
After burners are on. I am flying faster now. 
I have the generated list of separated strings of switches.
I can now go thru them and cut out the inner switch (if one) and leave the switch word accurately; will be replaced with a method.
And, I just got handling multiple inner switches at the three tab depth detected and captured line numbers.
I have the code to accurately get the inner switch id number (its original line number)
I have the code working to cut out the proper range of the inner switch body.
The rest is easy because the code after it gets converted to python already works - I did that first months ago.
I have had tremendous progress over the past few days after hitting a wall. 


Wednesday, oct 13th, 2021 11:53 am
Made progress.
I can split up the nested strings -all levels.
I can cut out the bodies of nested switches preparing to add method names swapping out inner switch word.
The light at the end of the tunnel has brightened.
Slow and gradual progress and refactoring and majorly simplifying the code with little prototypes to get it working
using tight efficient methods that are thoroughly tested.
The remaining additions all work just need to be added and tested.


Thursday, Oct 7, 2021  10:28am
Broke through the wall to the other side. Lot of progress.
My code to make the switch pairs (switch endswitch ) based on tab depth is solid.
I am dynamically making and filling a dictionary of the pairs of the sets of switch endswitch
so that I can split up the mega combo switch string into the separate switches.
I can copy the inner switches and place them into a list. I can cut out the inner switch bodies accurately 
which is necessary to make the whole thing work. I have the working code to make the nested methods.
The end of this show is nearing completion. So many obstacles and unforeseen snags.

Relieved the worst is over. Staging the phases of the last steps now.


Saturday, Oct 2nd 2021
The complexity is deep so I had to use some clever ticks to figure out what is what.
So... I am using comments to store data on the fly and grab by other functions so that I can tranfer
data and communicate at lightning speed. What I do is I transfer the line number of switches from their
original location which I use as an ID for each switch - it's original line number.
So with that in mind I made a method to add a comment after each switch with it's line number.
And after I do the copy and paste jazz juggling nested switches elsewhere I need to know what switch is where.

Here is that code to do GET SWITCH NUMBER (AND IT'S BODY) AND PUT SWITCH NUMBER AS COMMENT AFTER SWITCH
##===================================================
# example:  before  switch(exp){ 
# example:  after   switch(exp){ #22
# so the immutable string is changed 					   
# this puts original line number in comment after ALL SWITCHES in the first string with nested switches
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	print(" .......add_comment_and_line_number_to_all_switch()....this was just called .. ")
	awesome=''
	counter =0
	newstring=''
	print('baseline is red_robin starting appearance')
	print(inputstring)
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
			smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		else:
			newstring += line + "\n"
			counter += 1
	awesome = newstring
	red_robin=''
	red_robin = awesome
	print(red_robin)   
	print("smart_switch_numbers=",smart_switch_numbers)  #this is new here too 

print('about to test new code.... oh goody')
add_comment_and_line_number_to_all_switches(red_robin) 
					   
##===========================
##====================================
##  get_switch_number()
##====================================
def get_switch_number(stringname): #this might be for when
# I create copies of the switch body strings
	print(" ..get_switch_number.. ")
	awesome=''
	counter =0  #say it's 3
	#we would be looking in the main string for this
	#not changing line just getting line number from it since it's the ID for the switch
	for line in stringname.splitlines(): #this requires the lines numbers already added 
		if "switch" in line and "end" not in line: #just need to grab the first switch 
			#switchcounter += 1
			x = line.split("#")
			y = x[1];
			#str(y) #turns it into a string
			print("switch number is",y) 
			#how do i get what is after # split th eline I think
			counter += 1
			print(stringname)
			break
		else:
			counter += 1
	return y;

#skip 16 thu 38

weasel=get_switch_number(testcode) #so this figures out what switch is in a list slot
print("number of this string is... drum roll..",weasel)
					   
###========================
					   
Putting it together and streamlining the steps.
This is bad ass cool. Wow. Mind blowing nesting any depth works. Possibly uploading to github by Tuesday.
Sticking to the tenets of Dijkstra elegance and extreme simplicity. Methods are the key. God I love dynamic programming
and fuzzy logic.

Some code to show the management of complexity. 
What this code does is make the first switch with nested switches and represents
cutting out the first level deep nested switches down to the switch word which will then (later) replaced with method
names calling the next level switch.
This will also be utilized for subsequent (next) levels of switches with nested switches as a template.

##========================
## add_to_range_list()
##========================
def add_to_range_list(): #uses addthis list 
    print("add_to_range_list() this is necessary to work")
    for item in addthis:
        range_list.append(item) #adding to range list
        
    print("length of range list =",len(range_list))
    
##========================
## feed_range_list()
##========================
def feed_range_list():
    range_list.append([11,24]) 
    range_list.append([26,38])
    print('range_list=',range_list)
    range_list.reverse()#reverses it NOTICE WE REVERSE THE LIST TO CHANGE IT BOTTOM UP
    print("length of range list =",len(range_list))


##========================================================================
#####     S K I P P I N G   S O M E      L I N E S  ############
##========================================================================
def skipping_some_lines(x,start,finish):#start line nest switch and finish  endswitch
	print("======== skipping_some_lines()==========")
	print("skipping_some_lines() called",start,finish)
	#if I have a flag that it's been triggered then afterewards 
	#for the first pass flag_test[0]= False and then it's flipped to True
	print("flag_test[0]=",flag_test[0])
	if flag_test[0] == False: #meaning first pass  and what it's set to by DEFAULT
	    smart=x;
	    #change it to True now
	    flag_test[0] = True #this should now be tru e
	else: #meaning TRUE this is run after first run of skipping_some_lines()
	      #what this does is use the new concatted changed string changed on the fly with each pass
	      #for second and all subsequent passes it uses baton[0]
	    x = baton[0]

	##==========================================================
	# the issue is that on the second pass it is using the original string
	# and it needs to be using the modified string
	counter=0; concatthis =''; #finish = finish + 1 
	print("x=",x,"start=",start,"finish=",finish)
	smart=x;
	print("inside of skipping lines before going thru the loop this is the value of")
	print("the input string it will mess around with")
	print("==============================")
	for line in smart.splitlines():
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		if counter > start and counter <= finish: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish 
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			#ibm[0] = concatthis
			continue	
	print("===output from skipping some lines====")
	del ibm[:] #this should empty it
	print("this is the output result of skipping some lines")
	#print(concatthis)
	#what I am doing here is putting what has been concatted in the string into toosmart[0]
	toosmart[0]= concatthis
	baton[0]   = concatthis  #here the concatthis has been put into baton[0]
	concatthis=''
	print('in baton here we have')
	#print(baton[0])
	print('==============')
	#ibm[0] = concatthis	  #this has the switch string with the nested switch cut out
	#putting concatthis into ibm[0] here 
	ibm.append(toosmart[0])
	print("at the bottom of the skipping some lines to take out inner switch")
	print(" it sees this in ibm[0]")
	
		

#The change that I need to make here is to cut out switches greater than 3 tabs  tabdepth > 3
##======================================================
##   reduce_main_nested_switches_to_just_switch_word():  #I think that this does all switches no matter their depth
##=======================================================
def reduce_main_nested_switches_to_just_switch_word(astring): #11 - 23 and 25-37
    print(astring)
    #add_to_range_list() #this is new to put switch and endswitch lines into range_list
    feed_range_list() #added on wednesday, September 15th, 2021
    flag_test[0]== False #this flag is new this is the default setting for this flag
    print("flag_test[0]=",flag_test[0])
    print("length of range_list of pairs=",len(range_list))
    print("range_list=",range_list)
    counter=0
    # loop thru range_list
    print("before starting let's look into the range_list",range_list)
    print("range_list=",range_list) #
    for item in range_list: 
        print("**",item, item[0],item[1])
        print("inside of loop thru range_list :: COUNTER HERE=",counter)
        skip_range[0]= item[0]; 
        skip_range[1]= item[1]
        print("skip_range=",skip_range)
        toosmart[0]=astring #this might work
        skipping_some_lines(astring,skip_range[0],skip_range[1]) #this makes a new string skipping guts of inner switch
        counter += 1
        
       
##=========================


Tuesday, Sep 28th, 2021
Automatically making pairs of switch - endswitch works governed by the tab count.
so now I can proceed with separating the strings of nested switches and putting it all together.
Update on Oct 2nd . I succeeded in splitting up the switch main string with the nested strings into
individual nested switch strings and put them into a list.
I wrote some code that finds all of the switches and endswitches and makes pairs lists. I then can use this
to copy the switch bodies and I know the line of inner switches also.
threetabs= [11, 47, 49, 73]
fivetabs= [15, 38, 53, 64]
seventabs= [23, 33]

The code that finds the switch end switch pairs such as above 11,47

tabsubs=[]
threetabs=[]
fivetabs=[]
seventabs=[]
ninetabs=[]
eleventabs=[]
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
def internal_machinery(x,inputstring):
    print("=======internal_machinery called ====.......========")
    print("tabsubs should start empty",tabsubs)
    print("internal_machinery called======>>>>>>",x)
    counter=0
    print(inputstring)
    for line in inputstring.splitlines():
        print(line)
        #this skips line if not 7 tabs and switch not in line
        tab_length = line.count("\t")
        if tab_length != x or "switch" not in line:
            counter += 1; continue
       
        if tab_length == x: 
            print("tabsubs should start empty",tabsubs)
            if "switch" in line and "end" not in line:
                print(line)
                tabsubs.append(counter) 
                counter += 1; continue
            if "endswitch" in line:
                print(line)
                tabsubs.append(counter)
                counter += 1; continue 
      
                
    print('right here now')
    print(tabsubs)
    print("where is the cursor?")
    if x == 3:
        for item in tabsubs:
            threetabs.append(item)
            print("threetabs=",threetabs)
        del tabsubs[:]
    elif x == 5:
        for item in tabsubs:
            fivetabs.append(item)
            print("fivetabs=",fivetabs) 
        del tabsubs[:] 
    elif x == 7:
        for item in tabsubs:
            seventabs.append(item)
            print("seventabs=",seventabs)
        del tabsubs[:]
    elif x == 9:
        for item in tabsubs:
            ninetabs.append(item)
            print("ninetabs=",ninetabs)
        del tabsubs[:]
    elif x == 11:
        for item in tabsubs:
            eleventabs.append(item)
            print("eleventabs=",eleventabs)
        del tabsubs[:]
        
    else:
        print("nada")

       

##==============================
##  experimental_machinery
##===============================
def experimental_machinery(x,inputstring):
    print("experimental_machinery called==========")  
    counter =0
    newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    print(newstring)
    internal_machinery(x,inputstring)
 
#this one will be renamed and I will add depth of tabs to 20 something for now
##============================
##  try all three()  Did this one on Wednesday
##============================
def try_all_three(inputstring):
    print("=====trying all three 3 5 7 tabs now====")
    print(" === to the moon when will starship land ===")
    x=3;internal_machinery(x,inputstring)
    x=5;internal_machinery(x,inputstring)
    x=7;internal_machinery(x,inputstring)
    print("==done==")


	
	
	
#============================
Wednesday sep 22, 2021
Hit a wall and broke through it.
For pattern matching of nested switches I needed to be able to determine
if the tab depth like 3:5 and a few 5s were in order like this 3,5,5,5,5
and I needed to get the number of the repeating tab depth which I will use
to know which switch numbers are used since they are numbered top down and I 
actually manage them in parallel by their line number in the original combo switch string.

I am happy to report that I can verify with certainty that I can count the number
of the repeating number accurately and verify that the pattern of a repeating
number is in a sequence. 
I already previously wrote the code to determine the 3:5 pattern  and 5:7 pattern
and 7:9 pattern and 9:11 pattern (tab depth) but I had difficulty determining if
the repeating tab continued and for how many times. Knowing how many of the same
tab number repeats was crucial and now it's solved. I just need to put them into 
methods.

I spent all of the past few days getting the tab diff detector working to detect
tab patterns but only for two numbers like 3:5 and I then had to figure out a quick
and dirty and simple solution after my complex solutions grew in if conditions beyond
belief. I found a method to verify an uninterupted sequence of numbers in a list in this
case I'm using the counter thru a list.

Rounding third and coming home on finally getting the nesting behavior jiving with
the design. The design uses a template based on the main nest method module(reuse is good)
since I'm using slices for each tab indentation level. I did hit some unforeseen minefields 
along the way and they slowed me down a bit and threw me off the tracks derailing my 
momentum but I'm chugging along again.

Just last night I got the methods working to accurately detect where a switch has a nested
switch by tab depth change. Again this is a prescan before the fun begins and it has to
be done automatically which makes it more adventurous and hazardous. 

Tuez Sep 21 2021
Nested switch location nesting analyzer works.
I can see the light at the end of the Summit Tunnel now in the Sierras.
Days till this is fully operational for nesting feature.


Sunday, Sept 19th, 2021  12:19pm
Engineered solution to determine pattern of indentation pairing.
so if I have a switch with a nested switch with a pattern of 3 tabs and 5 tabs
I can detect the location by line number which I use for the ID of each switch.
I have a separate function that numbers the switches sequentially so I know their promixity.
Just successfully was able to analzye a string of nested switches to determine the 3:5 pattern 
which I will also add detecting 5:7  and 7:9 and 9:11 for now and more later.

The point is since I need to have the nested switches separated and isolated but I need to know where they reside.
So this was a vexing engineering problem that had little to do with coding but had more to do with figuring out
how to analyze and find the pattern of the association of the switches and determine where they live.
Fun * 100 now that it works. Previously it was frustration * 1 million. I wrote the key algorithms yesterday in two hours.
Today I put the methods in loops and am using methods.

So what all of this means is that I can finish the last part of the construction of the nested switches
now that I can accurately detect them after devising a management system and ids line numbers of switches in input string
and since they are numbered top down starting from one I know if they follow each other in a sequence. 

red_robin ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			exp = 3
			switch(exp){  #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
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
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	

output of testing
sw_order_num= 1 switch_line=1  tabs =1
sw_order_num= 2 switch_line=11 tabs =3
sw_order_num= 3 switch_line=15 tabs =5
sw_order_num= 4 switch_line=23 tabs =7
sw_order_num= 5 switch_line=49 tabs =3
sw_order_num= 6 switch_line=53 tabs =5


[0, 0, 0]
['1', '1', '1']
['2', '11', '3']
['3', '15', '5']
['4', '23', '7']
['5', '49', '3']
['6', '53', '5']

yes a 3:5 pattern found
11 15

yes a 3:5 pattern found
49 53



Thursday, Sep 16, 2021
For the nested switching to work the user must use tabs for spacing.
#example though in github it butchers the spacing but each tab is 4 spaces. I just copied and pasted it in here.
#the first switch(below) is just one tab indentation. Bear in mind later I will add my macro to uses braces instead of tabs.

snowman='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'blable':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'tahoe':
									print("do something")
									print("yep")
									#################### this one is new 
									switch(exp){  #fourth level deep   Level 4    
										case 'obama':
											print("do something")
											print("good")
											fallthru
										case 'ufos are real':
											print("better")
											break
										default:
											print("nice job")
									endswitch 
							#############
									fallthru
								case 'fallen leaf lake':
									print("nice")
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
			##############
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  #first level deep                   Level 1
				case 'music':
					print("do something")
					####################
					switch(exp){  #second level deep          Level 2    
						case 'sierra':
							print("do something")
							print("yep")
							fallthru
						case 'snow lake':
							print("nice")
							####################
							switch(exp){  #third level deep   Level 3    
								case 'coolish':
									print("do something")
									print("yep")
									fallthru
								case 'auburn':
									print("nice")
									####################
									switch(exp){  #fourth level deep   Level 4    
										case 'coolish':
											print("do something")
											print("yep")
											fallthru
										case 'auburn':
											print("nice")
											#######################
											switch(exp){  #fifth level deep   Level 5    
												case 'coolish':
													print("do something")
													print("yep")
													fallthru
												case 'auburn':
													print("nice")
													break
												default:
													print("we are done here")
											endswitch 
											break
										default:
											print("we are done here")
									endswitch 
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
			fallthru
		
		default:
			print('the end')
}
'''	



Monday, September 13, 2021
Reengineering. Refactoring. Testing. Wiring the modules together.
Nested switches solved and module nearly pristine. Decided to 
make a module with several modoes so just one module takes care of generating each nested string
in parser and a separate module for after python generated.
Got the idea from the module that manages the first main swith with nesting and using that framework
for each next tab level of nesting so it's more eleganta and simpler so only dealing with one level
of switches with numbered nests which have their location address hard coded into the nested_method name.
Just retested to make sure that I can (put) a number as a comment to a switch string after switch
and then (get) it later to be used in the frame nested method in python. So I'm dealing with the 
nested switches like individual frames in a movie so it's managed maticuously with complete control.




Sept 6, 2021
Yesterday engineered managing and orchestrating nested switches.



sept 4 2021
final testing of switch case nested 5 levels deep.
implimenting goto label also. prototype works uses braces for scope based on C.
breaking deeply out of loops possible.


August 28th Saturday 11:11 am Gilroy Starbucks
All systems are green. The code runs ... bug free.

I designed the module to do nested switches at any level and will impliment it this week.
Using fuzzy logic it should be just one page of code. The tricky part was the managing and
numbering the nested switches and keeping track of them.

August 28th,2021 nearly ready for launch of switch case with infinite nesting
First launching switch with single level nesting in a few days. Meaning one level deep nesting initially.
Stage 2 will be launching in two weeks with up to 5 levels deep nesting for now.

Refining the code that combines the switches and puts them into methods after
taking the output in the stanford list and triggering the main switch.
Just retested the auto tabbing and putting each nested switch in python into methods.
All works perfectly.
Just polishing up the code after some welding.
Putting the methods together so it's all automatic.

Thrilling seeing it working.

Next step is connecting the first half which takes the input switch case with nested switches
and separates the strings and puts it into the quail list and then 
it will go thru the endswitch() function where the multiple switches are detected
and will thereby trigger the bypass205() method and convert each string into python
and then what I refined today will be called welding_together_all_python_nested_switches().
So a little bit more testing but the modules work separately currently, just need to
connect them. 

#====================================================

August 27th, Friday, 11:06am Morgan Hill Starbucks
Working code filling the quail list with input strings after separating them.
Found working code main switch string conversion code
which takes out the nested switches and puts in 
a nested method numbered
which I will make a second version to handle
dealing with nested switches with nested switches.
Came up with ingenius naming scheme that gets the
correct address line number and switch it's embedded in
and will impliment tomorrow.


August 26th 12:43 pm
Just got this working
# Thursday, August 26th, 2021 12:27pm 
	# inside of original_stage1.py inside of left folder
	# still need to add the methods to make this section work
	# which fills up the quail list that will be fed into bypass205
	# #this is the section that I'm working on right now ===
	# WORKS not added yet : make pair_list here of pairs of switch endswitch 
	# WORKS not added yet : then  loop through pair_list to fill quail list
	# quail list of strings  using copy_string if at least one endswitch in input string
	# Need to fill quail list with these switch bodies strings
this happens above and before bypass205() is called in endswitch if multiple switches detected 

August 24th, 2021 MenloPark, Ca
More testing and refining bypass205() inside of endswitch().
bypass205() is a method triggered if there are nested switches  embedded in the main switch.
Now I can handle nested switches with aplomb. I just need to integrate 
the sting slitter called cookie_cutter which needs to be called before endswitch().
Cookie_cutter is the string splitter that puts the individual nested switches and main switch into 
the quail list. After being parsed and codegened the strings are added to the stanford list.
Then I will work on integrating the end game of already working code that puts the outoput
python strings into methods. 
I spent the past few days perfecting the pair list called range_list for a newst holding lists
of the switch , endswitch line locations. Initially I was going to use a dictionary and I 
gradually gravtated towards a list of lists.


August 23rd 2021
Designing modificationto handle multiple nesting beyond one level deep up to five levels deep.
This is a coprocessor seperate module engine to modify nested switches with inner switches.


August 22, 2021  11:07am Hollister, California
Will next work on design and management structure and plumbing tool.

Currently finishing each stage and testing independently before connecting them together.
Due to the overwhelming growing complexity after this is finished
I'm making a simple program in javascript to represent simple pictures of the chunks
and location and name of each function and method and what they do with search
to see the design implimentaiton at the function level. And I will be able to click on
a function to see more details. And I will have simple pipe diagrams overlay to see the 
flow through the system. This is a necessity (to be done later) so I can see the structure
archiecture and flow of control and keep the functions behavior purpose clear and 
TRANSPARENT SINCE IT'S ALL INVSIBLE AND I NEED TO SEE IT. This idea occured to me this morning
because I was lost at sea what was doing what and when and I was so many fathoms deep in the code
I couldn't visualize the structure levels I designed. And what was crucial was seeing the structure and keeping
track of what functions and methods were contributing to behaviors.

I originally designed just the main switch to have nested switches and the second design
will allow nested switches to have nested switches to handle  nesting 3 deep. Right now it
limitd to 2 deep and I'm modifying it by tab depth for now for 3 tabs depth main switch
5 depth 2nd level, 7th tab depth 3rd level and 9th tab tabs 4th level depth, more to be added later.

This all happens before the parser and codegen. Organizing the code now.
The second half after the code gen puts the generated swith code strings into methods
and combines in one string wheich is then executed works already.




August 18th,2021 9pm
Engineered working architecture to automatically detect all nested switches
and copy them to the input list. This was more daunting then I first thought.
Happy the worst vexing piece works.  Last piece which happens with generated python
just needs to be streamlined and already works. Tomorrow should be productive.
Greatly relieved this part finally works as designed.


Wednesday,August 11th, 2021  1:13pm Menlo Park, California
working on sepearting stings methods connecting methods together adding arguments params.




Saturday, August 7th, 2021 11:57am Morgan Hill Starbucks
Recently had a problem with my window not going up on my car and that ate up precious time
and then I had problems with my iphone not charging and I fixed that problem. Combined that
ate up 3 days and set me back a few days from completing this project.
I can see the light at the end of the train tunnel (like the Summit Tahoe on Donnor Pass)
and the hardest methods work beautifully and are debugged.


Perfecting input so the input string is checked for switch count and endswitch count
to determine if nested_switches = True and if so bypass205 is called.
Testing bypass205() thoroughly now.

Reviewing functions and methods to do Cookie Cutter which separates the input
string into the main switch and the nested switches (if they exist) and then change
the inner switches in the main switch into numbered nested methods. That all works.
These are all put into the qail input list and endswitches changed to } also.
Then as a list they are fed into bypass205 inside of the method endswitch().
Afterwards the output of the parser and code gen for each switch is put into the stanford list.

Then the next stage is train yard whereby each generated python switch string is encased into a template numbered method
and indented properly. The numbering is crucial so an id as a comment is put into each nested string
to double check accuracy of identification. This code works. And then the cake layer combo concatter works which connects
the stings are combined and then finally executed.

So the front end activities have been streamlined and automated chopping up the input string if there
is more than one switch. bypass205 has been added to endswitch and testing continues. I sent thru
a few individaul strings to make sure that bypass isn't executed when it shouldn't be.
So I'm focused on the backend now taking the python output of each switch case and then adding
them to the combo cake layers in order - also known as train switch yard since they must be backwards
order with main at the bottom or in other words last.

At this point I have used dummy test data between stages and now I am setting up everything to work
the way that it is designed. So previously I already had 3 strings in the quail list to test bypass205()
which for simplicity just checks the length of quail to determine if there are any nested switches.
Now the next test is starting with a multi switch string, split it up, and fill quail and send it thru
endswitch and bypass205. Then after that I will work on adding the nested number methods.
So I am proceeding methodically to ensure each stage works and carefully weld them together. 
												 
working in files. fourt_of_july2.py and official_switch_case_silver.py
testing in concert with utilizing the parser and codegen for real world testing

Wednesday, August 4th, 2021 1:13pm Starbucks
What happend today is I activated by bypass feature within the endswitch() method so that I can now
handle singlular switches in a multiple switches so a switch with nested switches. This was a nontrivial problem.
I think I am up to 12,000 to 13,000 lines on the project now. Grateful it works. My biggest program yet. All python.

Up until today this was not implimented into the design. 
A lot of features had to work in tandem and in concert with a multitude of methods 
to make this super complex feature work. Today is a happy day.
I included some of the key code that makes it work.

testing the management of converting a switch with nested switches into separate strings
and then running them through endswitch() method which detects if more than one switch in the string.
If there is more than one switch it triggers bypass205() which separates the switches (not shown in this code below)
and then flips a fuzzy logic flag in the codegen so that each generated switch is saved in a list.
and then combined to make the output for running the multiple switch case.

Just tested bypass205() inside of endswitch() and it worked!!
That was cool. I was slightly nervous and had some speed bumps but overcame my fear and
conquered it with persaverance. #that was the most critical stage converting the javascript/C switch into python
on-the-fly sensing more than one switch. Now for the test I had 3 already separated strings but it did indeed work.
Thrilled. The rest is gravy from here. 

Just test one string which works correctly.
So now the two scenarios work. one switch in an input string and more than one switch in an input string.
Over the moon right now. What a great fight that was.


####====== BYPASS205() ======== ###
# stanford list is filled in the code generator at the bottom
#######################################################################
########### bypass 205 ########### july 1st 2021 testing starbucks in gilroy
#premise is that quail list has more than one switch string in it
#for bypass205 to work so a minimum of 2 switch strings
def bypass205(y): 							# runs input strings thru parser and  
	print("=========bypass205() called===========")
	print("quail input list of switch strings has a length of ")
	print(len(quail))
	print("if len(quail)>= 2: you are good")
	if len(quail) >= 2:
	   print("GREEN LIGHT SUFFICIENT quail requirement met")
	else:
	    print("RED LIGHT insufficient quial list is only 1 in length")
	print("====")
	###==== error message if insufficient list length for quail ===
	if len(quail) < 2:# quail list requires 2 or more in length of switch strings
		print("error message in bypass205")
		print("quail list needs minimum of 2 strings to work in quail list")
		return # don't go forward if the quail list is too small
	else:
		pass
	###=============================================================    
	mytrace("bypass205()") 					# code gen puts in stanford list
	del stanford[:] 						# empties  stanford list 
	todo_after_putting_strings_into_quail_before_starting_bypass205()
	#this swaps the endswitch out and puts in } at end of switch
	#loop thru quail list and apply parser guts for each string
	for item in quail: 						# loop thru quail list 
		y = item 							# this puts the contents of each string in quail into y 
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		show_input_switch_string() 			# flag for testing this shows the input string
		parser_guts(y)  					# does parser and codegen of each switch string        
											# and is placed into stanford list
###  end bypass205()  ##################  		


##=========================================
def swap_endswitch_with_curlybrace():
    print("=== swap_endswitch_with_curlybrace() ====")
    counter=0
    for item in quail:#looping thru quail list
        if "endswitch" in item:
            print("yes endswitch is in this string")
            holdon[0] =take_out_endswitch(item)
            quail[counter] = holdon[0]
            holdon[0]=''
            counter += 1
            continue
        else:
            print("nope no endswitches")
            counter += 1
            continue
#end function


def todo_after_putting_strings_into_quail_before_starting_bypass205():
    swap_endswitch_with_curlybrace() 



# I need to call endswitch() to call bypass for this test
#august 4th test at starbucks on santa cruz avenue 

# so it would be True if nested is true
	#for this test we pretend that we have already seperated the big switch string
	# into sepeate strings and they ahve been placed into the quail list
	# #but I can do it here later, with y as input
	# for right now in this phase the quail list has already been filled
	# and we have determined that nestwich is True
########################
##     endswitch(y)      this calls flow_valve_input which checks if cases are numbers or words
########################  and if numbers = True then call parser_mode_2(y); If numbers = False parser_mode_1(y)
def endswitch(y): #pulls in sw 
	print("ENDSWITCH CALLED DOES IT EVEN WORK () called...")
	switchcasetester='';switchcasetester=None;
	del switchcasetester;switchcasetester='';
	mytrace("endswitch() in switch_cat called")
	show_input_switch_string() #flag for testing this shows the input string
	#check  if nested switches
	print("count how many endswitches in string")
	answer = y.count("endswitch")
	print("if answer = 0 continue moss beach one string test ")
	print(answer)
	print('=====')
	###========= testing this august 4th 2021 ==================================
	print("here we go, leaping into the == Grand Canyon == will it fly?")
	if nested_switches_count[0] > 1: #based on number of endswitch count
		nested[0] = True; 
		print("bypass 205 CALLED IN ENDSWITCH biggest test yet to make sure that his works----")
		bypass205(y)  #<<== this manages nested switches
		#or I can do ((so y is meaningless for this test)
		#return       # it is called once and then endswitch ends
	else:
		nested[0] = False; 
		pass
	###===========================================
	#this section is only run if a string switch string NOT NESTED ONES
	print("so this would be skipped if nested switch string combo bypass")
	if nested[0] == False or answer == 0:#all of this below is skipped if nested = True
		check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
		if baseline[0] != "nada": #means it converted to uppercase
			y = baseline[0]
		#end if
		flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
		print("if number in first case",valve[0])
		if valve[0] == True:    #meaning numbers like case 12:
			macro_expansion(y); #checks if macros used and expands them and converts numbs to strings
			y=None; del y; y = cray[0]; 
		#end if
		flush_lists() 
		parser_mode_1(y) 
	else:
		pass
	################## normal endswitch 


#three scenario tests
bypass205() by itself
endswitch with byhpass205() implimented (added)
endswitch doing regular singular switch not doing bypass205()


#this test below is outside of any function above and any method
def raw_testing_of_bypass205():
    print("==########################===")
    print("RAW TESTING OF BYPASS205()....")
    print("TO THE MOON...")
    ##################### this is a test of bypass205 with three strings already separated
    y=''
    del stanford[:] #just to be sure empty stanford list first
    print("the length of stanford=",len(stanford))
    print('about to call bypass205() ======')
    #WARNING: this requires strings in quail list for bypass205 to run
    # this is testing using bypass205 to create multiple python strings for each switch input string
    print("what is in y",y)
    print("maybe just the quail list is necessary")
    print("length of quail list =",len(quail))
    
    bypass205(y) #run the test data to see what it does and calls the parser and codegen 3 times
    print("the length of stanford=",len(stanford))
    what_is_in_stanford()# list   
    # I just want to see the strings and proof that it worked 

    next_steps()
    managing_nested_switch_scenario() #this just checks if the stnaford len > 0
    # here we see the output python in the stanford list BEFORE it's combined in cake to
    # form a big string that will eventually be executed
    build_stacked_cake_string_combining_stanford_list()
    res=get_number_of_nested_switches()
    print("====== LOOK FOR IT ========")
    print("this is the number of nested switches =",res)

#raw_testing_of_bypass205()  #turned off for testing officially above




#simulating an input string here we go

def santa_cruz_test():
    print("SANTA CRUZ TEST to infinity and beyond")
    print("here we go")
    print("length of quail list prefilled")
    print("length of quail")
    print("length =",len(quail))
    y=''
    del stanford[:]
    endswitch(y) ##<<======== august 4th test 12:45pm 
    what_is_in_stanford() #output of runnin ghte code. 
    next_steps()
    managing_nested_switch_scenario() #this just checks if the stnaford len > 0
    # here we see the output python in the stanford list BEFORE it's combined in cake to
    # form a big string that will eventually be executed
    build_stacked_cake_string_combining_stanford_list()
    res=get_number_of_nested_switches()
    print("====== LOOK FOR IT ========")
    print("this is the number of nested switches =",res)

#santa_cruz_test()    


#to test a single string whereby bypass is not triggered 
def moss_beach_test(v): # 1 string test
    print("====MOSS BEACH TEST to infinity and beyond===")
    print("here we go")
    print("length of quail list prefilled")
    print("length of quail")
    del quail[:]
    print("length =",len(quail))
    #y=''
    del stanford[:]
    print("y=")
    print(y)
    endswitch(y) ##<<======== august 4th test 12:45pm 
    what_is_in_stanford() #output of runnin ghte code. 
    next_steps()
    managing_nested_switch_scenario() #this just checks if the stnaford len > 0
    # here we see the output python in the stanford list BEFORE it's combined in cake to
    # form a big string that will eventually be executed
    build_stacked_cake_string_combining_stanford_list()
    res=get_number_of_nested_switches()
    print("====== LOOK FOR IT ========")
    print("this is the number of nested switches =",res)

y =oldstring_test2
moss_beach_test(y)


####============================
####      parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("parser_guts called =======")
	check_if_uppercase_constant_cases(y)	#if UPPCASE this senses it and converts to string
	if baseline[0] != "nada":				#means it converted to uppercase
		y = baseline[0]
	flow_valve_input1(y)					#puts True or False into valve[0] added April 2nd, 2021
	print("if number in first case",valve[0])
											# macro expansion is only called if numbers are True
	if valve[0] == True:					#meaning numbers like case 12:
		macro_expansion(y); 				#checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
	flush_lists() 
	parser_mode_1(y) 	

###==================================
	
	



Wednesday,August 4th,2021  10:06 am Menlo Park Starbucks
Working on ensuring each separate small program module works before connecting them in sequence together.

Macro with Hypertalk structure works.swap with is from Algol 60. Verb first with sentence structure. Structured Pseudocode.
"swap 'switch(exp)' with 'inswitch(exp)' in list[0]"

Tuesday, August 3rd time 6:12pm on home stretching approaching home plate.
Worked on building methods to gather together collections of methods together
cleaning up the code.  Working on getting the switch and endswitch lines into pairs which 
are then put into a list. Unreal progress this morning and this evening. 
So working on the first half management of transforming the input switch string into separate files
before it is sent thru the parser and codegen for each individual switch string. All of the code
is completed already. I am just packaging it and organizing it and making it easier to deal with.
Startling how much code is necessary to do this all. Hopefully making the goto label will be less
than two pages of code which will work ontop of the switch case framework.
Might have it stiched together tomorrow and put it up on github.
The nested switch code is completely separate from the rest of the switch to manage
the complexity.

#I will change var and list names and function names. I make them memorable to keep it fun.
###############################################################
################ testing call of these methods at once
###========== august 3rd test Tuesday nice air conditioning ====
def nested_switch_trapeze_tricks():
    print("==== nested_switch_trapeze_tricks() called=====")
    loop_thru_switch_locations()
    get_case_line_numbers(find_nested_switch_game)
    get_larger_number_less_than_case()
    get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
    copy_a_nested_switch(find_nested_switch_game)
    copy_coattails_bottom_of_big_switch_after_nested_switch_end() 
    fishfood()
    get_inner_switch_line() #not sure if I need this one
    switcharoo=[];switcharoo.append(0);linecounter=0
    print("the nubmer of nested switches=")
    get_number_of_nested_switches()  # here it is 

#this calls it right here 
nested_switch_trapeze_tricks()


##===================
#loop
pairlist=[]
theforce=[]
#this would just add the switch location
alpha=''
beta =''
counter =0
jedi=''
#this reads in data from switch_location
#               and from endswitch_location
def fill_pairlist_with_switch_and_endswitch_pairs(yy):
    print("====fill pairlist with switch and endswitch pairs()=====")
    get_switch_and_endswitch_locations(yy) #===== using sample stringh 
    print("this is grabbing the switch locations which are dynamically added to a dictionary for pairlist")
    print("the length of switch location =",len(switch_location))
    print("the length of end switch locatoin =",len(endswitch_location))
    print("==============...............============")
    # loop ==============================
    counter =0;allpha='';beta='';   #so this is one small set switch and endswitch line numbers
    for item in switch_location: #loops thru list switch_location
        alpha = switch_location[counter]
        beta  = endswitch_location[counter] #they should be the same length 
        pairlist.append([alpha,beta]) #always in sets of 2 #adds alpha and beta as list into pairlist  list
        print("pairlist=",pairlist)
        counter += 1
    print("======================")
    print("what is in the pairlist")
    newcounter=0
    print("the length of the pairs =",len(pairlist))
    # loop =======================
    for item in pairlist:
        print(item)
        sosmart = pairlist[newcounter]
        print(sosmart[0]) 
        print(sosmart[1]) 
        print("====== JEDI TEST ========")
        #this is constructing filling the data in the dictionary pair values
        jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
        print('jedi=',jedi)
        theforce.append(jedi) #the pair is added as list to theforce
        turbo  =theforce[newcounter]
        newcounter += 1
    print("theforce=",theforce)
    print("the length of theforce list =",len(theforce))
    print("did we make it this far... in a galaxy")
###=====

def testing_pair_list():
    print("======testing pair list() ======")
    print("theforce[0]=",theforce[0]) 
    print("theforce[1]=",theforce[1])
    
    
fill_pairlist_with_switch_and_endswitch_pairs(samplestring)
testing_pair_list()



Tuesday, August 3rd, 2021 11: 47 am Morgan Hill Starbucks
	https://www.youtube.com/watch?v=HEe3xfWfkG8

Just got method working to dynamically add records to dictionary using lists for input.
This way I can change it on the fly and add to it quickly and easily.
working on the nested features and double checking to make sure everything is working before
uploading it.
Creating more methods too for readability aid.

####################################################################||
### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  
#####################
## do this baby 

#what I need to do is add to a dictionary dynamically 
#####################
def do_this_baby():
    print("do this baby caled")
    print("===do this baby() adding data to peartree dictionary called ......====")
    print("practicing ADDING data to see if it works (this will be done dynamically later")
    peartree['1'] = [10,20]
    peartree['2'] = [28,38]  #uses small anonymous list for data
    print(peartree)
    x = peartree.get("1")
    print("x=",x)
    
    
    
#testing adding data record to dctionary dynamically.
#Declare a dictionary (empty) 
print("testing dynanmically adding data to a dictionary Drive Thru")
data = {'a': 1, 'b': 2, 'c': 3}
print(data)
data.update({'d':3,'e':4})  # Updates 'c' and adds 'd'
print(data)

fun={}
print("first the fun dictionary is empty")
print(fun)
#input values to dynamically add data for teh switch endswitch to dictionary

cherish=[10,20]
skyblue =[28,38]


print("This is doing an update here --->")
fun.update({'1':cherish,'2':skyblue})
print("hard coded here printing out the dictionary fun")
print(fun)
print("========")
num1='3'
num2='4'
silver =[42,46]
gold =[50,52]

#put these into a list also
crystal=[]
crystal.append(0)
crystal.append(num1)
crystal.append(num2)

dust=[]
dust.append(0)
dust.append(silver)
dust.append(gold)

def dynamically_add_data_to_dictionary(a,x,y):
    print("testing... dynmically add data to dictionary a, x, y")
    print("Tesitng using lists now which are changeable on the fly")
    a.update({crystal[1]:dust[1],crystal[2]:dust[2]}) #totally dynamic attempt here
    print(a)

print("here dynamic attempt ------->>")
dynamically_add_data_to_dictionary(fun,gold,silver)


print('after updating fun dictionary dynamically  strawberry fields===')
print(fun)
print(fun.get("1"))
rat=fun.get("1")
print("below should be 10 and 20 for the result")
print(rat[0])
print(rat[1])
print("now to empty dictionary called fun")
fun.clear() #empties dictionary
print(fun)
    
##===============================
## get_size_of_dictionary  (name of dictionary)
##===============================
def get_size_of_dictionary(zoo):  #this is so I know what next record should be
    answer = len(zoo)
    print("get size of dictionary zoo",answer)
    #how do I loop thru a dictionary
    for x in peartree:
        print(x)
    print("====")
    print("")
    for x in thisdict.values():
        print(x)
    print("")   
    print("=====")
    for x, y in thisdict.items():
        print(x, y)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



#==========OUTPUT===========
here dynamic attempt ------->>
testing... dynmically add data to dictionary a, x, y
Tesitng using lists now which are changeable on the fly
{'1': [10, 20], '2': [28, 38], '3': [42, 46], '4': [50, 52]}
after updating fun dictionary dynamically  strawberry fields===
{'1': [10, 20], '2': [28, 38], '3': [42, 46], '4': [50, 52]}
[10, 20]
below should be 10 and 20 for the result
10
20
now to empty dictionary called fun
{}
playing with dictionary access...
testing getting car model
Mustang
Muppets Animal
do this baby caled
===do this baby() adding data to peartree dictionary called ......====
practicing ADDING data to see if it works (this will be done dynamically later
{'1': [10, 20], '2': [28, 38]}
x= [10, 20]
{'1': [10, 20], '2': [28, 38]}
get size of dictionary ... a test
length of peartree = 2
2
doing simple test here to get value of key number in peartree dictionary
====Domino's Pizza==
[10, 20]
the value of key 1 in peartree = [10, 20]
does this work or not???
10
20
=========
[28, 38]
the value of key 1 in peartree = [28, 38]
28
38
get size of dictionary zoo 2
1
2
					   

Sunday, August 1st, 2021 11am California time
Approaching the finish line for nested switches. Likely adding Tuesday at this point.

Testing and still wiring together the pieces.
Flow of Control procress of construction of Nested Switches feature.
I just have to wire them together.
Currently retesting each separate puzzle piece 

1 we start with a string that has a switch in it.
But we are dealing with nested switches and not regular switches

#######=====================
[done] (1)FIRST count how many switches and endswicthes are in a string to 
determine the number of nested switches
jumanji() in fourth_of_july checks for the number of switches in the input string

so if one nested switch then we need to detect the inner switch
if more than one nested switch then we need to detect them and
get their exact location which case and how much indentation etc.
and we need to make a copy of the inner switch string
take out nested switch from main switch and put nested_method in that line
#this is in fourth_of_july.py

#====================
[done] (2)
Separate the nested switches from th main switch
this is done in fourth_of_july.py
building string skipping inner nested switches 
put comment in front of #inner_nestswith so it's not called for now
I also am working on taking out the nested switches after they ahve been 
copied and leave teh switch for the nested switch and then replace
the switch for each nested switch with a method that is numbered
(this is what I have been working on recently)

I think I will have  list to hold the nested switch methods.
They will each be unique depth case (name/number probably number)
I might need to map the number of each to the case name.

create a list in quail list of each switch starting 
with main switch in position quail[0]

#=====================
#not added to endswitch as yet, still beta testing
#this phase is tested successfully at the bottom of official_switch_case_silever.py
[done] (3) inside of function endswitch(sw) #testing in official_switch_case_silver.py
if switchcount > 1:  #then nested switch #this triggers bypass205()
   bypass205()  #this method loops thru the qail list with the switch strings
   and calls the paser and code gen for each input switch string
 else:
    pass 

#=====================      
(4) inside of codegen() the concatted output string sweet
is appended to the list stanford (if nested_switch[0]== True)
# this is working filling the stanford list 
this results in the stanford list having the switch strings
we then reverse the list so that main is last in the list
so that when we conccat them together top down it will work correctly
since the nested switches will be embedded within methods above it

#=================
[done] (5)  working on a management method that is called after the last quail string
is sent thru the parser and codegen
so what I can do is when the count on the last stanford list is reached
then I know it's done creating the python strings output


[done] (5) I need to put the nested_method_number() name where each inner switch was
within the main switch in the correct case and line number

[done] (x) change switch to inswitch and fallthru to infallthru in nested switch strings

[done] (x) put nested switch strings into a method for the nested_switch_number

[done] (x) concat together in a triple string ''' switch main and nested switches in python
    and execute(string)
    
[done] (x) execute string

###3=================================================================

Saturday, July 31st, 2021  12:15 pm
Decided to reduce the complexity of the nested feature and will manage it as separate stages
that are completely independent but are called in order so that I can manage it more cleanly.
I will connect the pieces to make sure they each talk to each other.

Added put, get to macros today. I was working on a swap to work with lists which didn't go well and then it occurred to me
that since lists are mutable I can just change on-the-fly one list slot with another list's slot simply. Spared me much grief.
Excited that I am wiring together the different sections of the nested feature that I built independently.

Based on time available the whole nested feature will be on the github by Tuesday at the latest. I have Tuz Wed off 
for my buffer if things get mired in the swamp. It is thrilling to have made it this far.

I will also have to do more testing once it's all wired together and then for testing I will add it as a separate
module since it's so complex and so there is no interference with the main module.


Thursday, July 29th, 2021  8:53am
	
	Putting together the submodules for the nested switch codebase. I was going to put it into one program
	but the complexity is deep so I decided to keep it as a dozen submodules that are controlled by a 
	manager submodule so that it's easier to comprehend and fathom it all. There is a lot going on.
	It makes it easier to debug and understand too. So I view it as a dozen eggs small modules - makes it easier
	to manage. Until I came to that realization I was overwhelmed with it all in one place.
	#will take a day or two maybe Saturday it will be complete and I'll upload it.
	This is the current focus to complete the nested feature and activate the bypass205 feature to 
	handle multiple switch inputs. By keeping it modular it makes understanding the plumbing much easier.
	And the system is easier to comprehend and visualize.
	Also I made a debugged gold working version of the regular one switch module I'll upload this weekend.
	It's really interesting that the way that the whole program came together it utterly facilitated
	the ability for the whole thing to actually work. I remember the struggle getting the module to initially
	work without reloading. That was fraught with massive frustration. It's been a rocky road with small victories
	along the way.
	
	Next:
	Working on testing a triple nested switch with three levels deep of switches within a main switch.
	
10:45 am Tuesday, July 27th, 2021
It works. Wow.
Nested switches works. Unreal.
I will connect the program pieces together and upload soon.
Need to add some documentation.



Found some code I wrote on July 12th for this moment. Pure Nirvana.
code I wrote to combine the strings and run it. 

Tuesday, July 27th, 2021  8;33 am Morgan Hill Starbucks
Finishing up build cake concattting the nested strings and main switch string and methods and call to main switch.
Everything added (the strings) to a list. Just need to add the triple string component. Running past third headed
into home plate. What a journey.


Monday, July 26th, 2021 11:36 am Morgan Hill Starbucks
I have putting main switch string into a main switch method and properly indented.
The main switch string is from the starting point of the generated python.
The output nested switch strings from the python code gen are put into a list and then read individually.
I have a method to loop thru list of the nested strings and build nested_methods numbered in a sequence working.
Nearly finished.


###====================================================================
##  create main switch for cake base for the multi-combo nested switch
###====================================================================
# fixed on july 26th 

## testing making the main switch and putting it into a function
themainswitchstring = ''' 
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
			n=2
			nested_switch_1(n)  
			print("all great women, yeah, right")
			print("to come to the aid of their country..nver")
			break
	
		elif case in caselist3: # ['israel canal']
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			fallthru('ufos are real')
	
		elif case in caselist4: # ['ufos are real']
			print('manure')
			n = 3
			nested_switch_2(n)  
			print("no more horses")
			break
	
		elif case in caselist5: # ['default']
			print('one walking quack d')
			print("walking geese")
			n=5
			nested_switch_3(n) 
			break
	
		else:
			print('one walking quack d')
			print("walking geese")
			break
	
	
	
'''



solution=[]
solution.append(0) 
#this adds the def main_switch(x): to the top and indents the body of the switch case
def create_main_switch_for_cake_base():
    print('create main switch for cake base\n\n\n')
    global themainswitchstring 
    x = themainswitchstring.replace("exp = varholder[0]", "def main_switch(x):\n\texp = varholder[0]")
    themainswitchstring = x
    mycounter=0
    for line in themainswitchstring.splitlines():
        if "\t" in line and mycounter ==0: #takes out tab from first line only 
            themainswitchstring = themainswitchstring.strip('\t')
            themainswitchstring = themainswitchstring.lstrip() #should take out spaces
            break
            
    mycounter=0
    for line in themainswitchstring.splitlines():
        if "\t" in line and "def" in line: #takes out tab from first line only 
            line = line.lstrip('\t')
            line = line.lstrip()
            break
    print(themainswitchstring) 


print("start test for mainswitch\n\n\n")    
create_main_switch_for_cake_base()

#OUTPUT

create main switch for cake base



def main_switch(x):
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
			n=2
			nested_switch_1(n)  
			print("all great women, yeah, right")
			print("to come to the aid of their country..nver")
			break
	
		elif case in caselist3: # ['israel canal']
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			fallthru('ufos are real')
	
		elif case in caselist4: # ['ufos are real']
			print('manure')
			n = 3
			nested_switch_2(n)  
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
	
	
	

#about to put this into a method



output1='''#output1
exp = varholder[0]

caselist1 = ['one', 'two da', 'three da']
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


output2='''#output2
exp = varholder[0]

caselist1 = ['two', 'two da', 'three da']
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


output3=''' #output3
exp = varholder[0]

caselist1 = ['three', 'two da', 'three da']
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


## coded this on July 25th, 2021 in gilroy.================
###=========================================================
##  put_switch_case_into_nested_method_and_add_tabs(number)
###=========================================================
nestring=nest1
def put_switch_case_into_nested_method_and_add_tabs(yeah,number):
    global output,output1,output2,output3 #each individual string will be put into the output string for uniformity
    #and then at the bottom of this function reset output to '' to empty it
    output =yeah #so clever
    print(output) #the truth is in the pudding
    solution[0] = "_" + str(number) 
    x = output.replace("exp = varholder[0]", "def nested_switch" + solution[0] + \
     "(x):\nexp = varholder[0]")
    output = x
    x = output.replace("switch(exp)", "inswitch(exp)");output = x; x=''
    x = output.replace("fallthru", "infallthru");output = x
    #where I add one tab to front of each line ############")
    noway=''; counter=0; toosmart='' # I copy each line to a new strings since strings are immutable
    for line in output.splitlines(): 
        counter += 1
        if line.startswith("def"): #this looks if first line then doesn't add tab
            noway = line #it does nothing to the line
            toosmart += noway + '\n'
        else:
            noway = "\t" + line  #adds a tab to front of each line
            toosmart += noway + '\n'
        #print(noway)
    #to see what's in it after it's modified and tabbed
    for line in toosmart.splitlines():
        print(line) 
        
print("first test")
stringname[0] = output2   
put_switch_case_into_nested_method_and_add_tabs(stringname[0],2)
print("end of first test")

# the number is fed into the top of the nested method
# note the main switch is NOT numbered

####################################################################
# loop thru nested_python_string
# I might need to reverse the nested list first so they are called in the right order.
# and I might fill a new list that holds the results of the golden nested switches
#I could have a different list with the number list for the nested switches perhaps
sample_list=[]
sample_list.append(0)
sample_list.append(0)
sample_list.append(0)
sample_list[0] =output1
sample_list[1] =output2
sample_list[2] =output3
#testing loop thru method for different input nested strings and numbering numerically
cool_counter=1
x = 0
for item in sample_list:
    put_switch_case_into_nested_method_and_add_tabs(sample_list[x],cool_counter)
    cool_counter += 1
    x += 1
    

	
##===============================================================


11:06 pm Sunday, July 25th 2021
#in a method now
#input called output which was generated with the parser and codegen
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
#then running thru the new method below it puts its contents into a method so I can call it

#remind the reader that output is the same of the input string
solution=[]
solution.append(0) 
saved_result=[]
saved_result.append(0)
##=========================================================
## put_switch_case_into_nested_method_and_add_tabs(number)
##=========================================================
def put_switch_case_into_nested_method_and_add_tabs(number):
    global output #input string to modify
    solution[0] = "_" + str(number) 
    x = output.replace("exp = varholder[0]", "def nested_switch" + solution[0] + \
     "(x):\nexp = varholder[0]")
    output = x
    x = output.replace("switch(exp)", "inswitch(exp)");output = x; x=''
    x = output.replace("fallthru", "infallthru");output = x
    #where I add one tab to front of each line ############")
    noway=''; counter=0; toosmart='' # I copy each line to a new strings since strings are immutable
    for line in output.splitlines(): 
        counter += 1
        if line.startswith("def"): #this looks if first line then doesn't add tab
            noway = line #it does nothing to the line
            toosmart += noway + '\n'
        else:
            noway = "\t" + line  #adds a tab to front of each line
            toosmart += noway + '\n'
        #print(noway)
    #to see what's in it after it's modified and tabbed
    saved_result[0] = toosmart  #here I put it in a list to use more easily
    for line in toosmart.splitlines():
        print(line) 
    
put_switch_case_into_nested_method_and_add_tabs(3)  #this calls it and takes a number to the nest number
#this calls the method above

OUTPUT of this method which will be added to the cake concat layered list
def nested_switch_3(x):
	exp = varholder[0]
	
	caselist1 = ['fishy', 'two da', 'three da']
	caselist2 = ['big bird']
	caselist3 = ['israel canal']
	caselist4 = ['ufos are real']
	caselist5 = ['default']
	
	
	inswitch(exp)
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
			infallthru('ufos are real')
	
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
	
	
	
##=============================================================================	
	9:43 pm Sunday, July 25th.
It's difficult to describe the euphoria of this project coming together. 
I just think of the millions of programmers that will use this.

This is putting the switch case in python into a method as a numbered nest.

  == friday july 2nd testing this already coded previously ===
this is the generated output of python for the test switch case

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




now I will add one tab to the front of each line
big test here =====------0000000000000========00000000=====00000000000
STAGE ONE add tab to front of each line
 Adding 1 tab to front of each line in switch case output 
simple and effective does this swap work or not
replacing switch with inswitch
replacing fallthru with infallthru

def nested_switch_1(x):
exp = varholder[0]

caselist1 = ['fishy', 'two da', 'three da']
caselist2 = ['big bird']
caselist3 = ['israel canal']
caselist4 = ['ufos are real']
caselist5 = ['default']


inswitch(exp)
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
		infallthru('ufos are real')

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




CRITICAL OUTPUT HERE...stage two.....
	
def nested_switch_1(x):
	exp = varholder[0]
	
	caselist1 = ['fishy', 'two da', 'three da']
	caselist2 = ['big bird']
	caselist3 = ['israel canal']
	caselist4 = ['ufos are real']
	caselist5 = ['default']
	
	
	inswitch(exp)
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
			infallthru('ufos are real')
	
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
	
###===============================================================
This is the code in raw form before I put it into a method tonight.

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

address = "_1" #this is for test purposes since this will be dynamic
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
print("CRITICAL OUTPUT HERE...stage two.....")
noway=''
counter=0
for line in output.splitlines(): 
    counter += 1
    if line.startswith("def"): #this looks if first line doesn't add tab
        #print("YES starting with def",counter)
        noway = line #it does nothing to the line
    else:
        noway = "\t" + line  #adds a tab 
    print(noway)
print("next stage here ======--R2D2--=======")
print(noway)
 

	
	
	
	
	
	
	9:24 pm Sunday July 25th.
Progress of phase 3 showing output of cake layer builder showing what the output looks like
before converting each switch by putting them into a template method. methods at top are fillers.
Not the real methods just fillers for now.  Phase 3 will entail putting each switch into a method

run_combo='''

def inswitch():
	print(test this)

def infallthru():
	print('do something')




exp = varholder[0]

caselist1 = ['blable']
caselist2 = ['more']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['blable']
		print("do something")
		print("yep")
		fallthru('more')

	elif case in caselist2: # ['more']
		print("nice")
		break

	elif case in caselist3: # ['default']
		print("we are done here")
		break

	else:
		print("we are done here")
		break



#============ divider =========== 



exp = varholder[0]

caselist1 = ['autumn']
caselist2 = ['winter']
caselist3 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['autumn']
		print("falling leaves")
		print("sunlight from the sky")
		fallthru('winter')

	elif case in caselist2: # ['winter']
		print("snow time")
		break

	elif case in caselist3: # ['default']
		print("so much creativity")
		break

	else:
		print("so much creativity")
		break



#============ divider =========== 



exp = varholder[0]

caselist1 = ['1', '2', '3']
caselist2 = ['4', '5', '6', '7']
caselist3 = ['8', '9', '10']
caselist4 = ['default']


switch(exp)
while True:

	if case in caselist1: # ['1', '2', '3']
		print("where's the dog house!")
		print('first prize')
		print('you block head Charlie Brown')
		fallthru('4')

	elif case in caselist2: # ['4', '5', '6', '7']
		print('kangaroo hop hop!')
		nested_switch_1(n)
		print('taught me how thru write code')
		fallthru('8')

	elif case in caselist3: # ['8', '9', '10']
		print('mocha blast')
		print('== autumn nest===')
		nested_switch_2(n)   #this is new 28
		fallthru('default')

	elif case in caselist4: # ['default']
		print('the end')
		break

	else:
		print('the end')
		break



#============ divider =========== 
call_main_switch()
'''
Build Cake code before refactored.

##====================================================
##   BUILD STACKED CAKE STRING COMBINING STANFORD LIST
##====================================================
def build_stacked_cake_string_combining_stanford_list(): 
    print("building stacked cake concat stanford list")
    print("======Lake Lagunita=====")
    print("remember after the stanford list has been reversed the LAST list will be the main")
    volleyball ='' #initialized
    print("about to concat a string called volleyball")
    count =0
    #this goes thru the stanford list so the main switch is last.
    # and puts the contents into the string volleyball.
    function_defintions='' #initialized
    #I will put these in volleyball to initialize
    #dummy code place holder for testing
    function_definitions ="\n\ndef inswitch():\n\tprint(test this)\n\ndef infallthru():\n\tprint('do something')\n\n"
    volleyball += function_definitions #must be first
    #stanford list should alread by reversed so that main switch is last and at bottom
    for item in stanford:
        volleyball += "\n\n"
        volleyball += item
        volleyball += "\n\n" #spacer 2 lines
        volleyball += "#============ divider =========== \n"
        count += 1
        #print(count)
    

    #adding triple string
    print(" the multiline string output")
    print("is called run_combo which will")
    print("be executed like this exec(run_combo)")
    print("")
    
    
    front="run_combo='''"
    #no tabs in front of the main method call
    middle= "call_main_switch()\n" #triggers main switch
    tail ="'''"
    
    volleyball = front + volleyball + middle + tail
    print(volleyball)
    #exec(run_combo)
    


Sunday July 25th, 2021 8:30 pm
Phase 3 begins the last phase of the Nested Switch Case
I have the output python strings after going thru the parser and code gen (translation the python code)
I just have to test adding the method framing of the python output strings (which already works)
and use the cake layer building (cool method) to concat the list and execute it.

I have to make sure that the test beta nested switches have an input var in the main switch (that works)
and so I have been doing back and forth from my prototoype working version based on output and working
backwards from what it needs to look like to work.

I have tomorrow off so I should make good progress on phase 3 and whatever I get working and ironed out tonight.
The code is in three differnet files so that I have been able to manage the complexity.
I still need to convert some more code into methods to reduce the code base for the nested switches.
The fact that I made it this far proves to me that it's all going to work. 


Phase 1 was scanning the input nested switch string.
Counting switch cases, getting the switch and end switch line numbers
and adding them to a dictionary.
looping thru the main string and copying the nested switches and putting each into a list
then deleting the nested strings (really skipping them) when creating copy of main swith minus the nested switches
but left the nested switch word instact and then swapped it for a number nested_switch method to call it later.


Phase 2 was a pain; very time consuming fraught with tiny details
Ended up making a copy one nested switch method that I now reuse in a loop.
Preparing the input strings that had been separated from the main switch
and taking out the endswitch and swapping it with a }.
And applying the correct indentation (tabs) for each of the switch case strings.
I also built an address manager using a dictionary to keep track of the precise location
of the nested switches in case there are lots of them. Haven't turned that feature on yet.
Number from top down starting at top of main original switch string, level (number of tabs),
case number in sequence, line number within case that nested switch is on, number in series 
of nested switches at same level in that same level. For now it's just using a one digit number.
I also need to test three levels deep to see what happens. Thus far I have done two levels deep 
of nesting and it worked.



Sunday, July 25th, 2021 6:16pm 
Doing testing right now. Finishing up the first half to get the input strings ready for the translation thru
bypass205 and working on that. It runs just found one undersight and it was annoying thinking of how much
trivial and time consuming is necessary when I want to do something super simple so adding a swap macro.
Macros really do come in handy and make code ten times easier to comprehend.
Swap is in a the Burroughs dialect of Algol 60  and now its in Python. What did Tony Hoare say in his hints paper.
"Here is a language so far ahead of its time, that it was not only an improvement on its 
predecessors, but also on nearly all its successors." swap a with b



	


The rush is profound. It works!!!! Nested switches in python works. And everyone said it couldn't be done.
The best part is that it looks like a C switch case in all respects (especially the expected behavior) but it's Python underneath. 
Gigi D´Agostino i´ll fly whit you Defectnoise trance mix 2016
https://www.youtube.com/watch?v=oNup6h7Y--k

Saturday, July 24th, 2021  12 noon Morgan Hill, California Starbucks WiFi

Putting chunks of code into methods to clean up the code and reduce the amount of code involved.
Four hours of refining the code to make it beautiful. Beautiful counts. Will add the code here tomorrow.

Made methods for taking out the nested switches from the main switch (after copying them)
Made methods to swap out the remaining switch word residue of each nested switch and replace it with
a number nested_switch method. Gotta get to work so will add more details later.

So the transformation of grabbing the switch string and converting it into separate strings
before sending it thru the parser and code gen are now working.
And, this is good, I already finished the methods for the transformation of the python code
strings to put them each into methods and indent them properly and concat them together 
and then like a class the methods are all within a docstring with a var and called.
This way there is no interference with other switches. They are each completely isolated
and only work together within the string that they all temporarily reside in and then they vanish.


This is the bypass205() in endswitch() that manages the building of the nested switches. It's sweet.
# what you don't see yet is the crucial if (which governs if bypass205() is called
# which is dependent upon if more than one switch inside of input switch string

if switchcount in inputstring> 1:
	bypass205()
#endif

#also what yuou don't see is that at the bottom of the CODEGEN
SO THE CODE IS SAVED AND NOT RUN IMMEDIATELY WHEN A NESTED SWITCH IS TRUE
there is a mighty if if nested_switch[0] == True:
#then it doesn't exec(string)
but instead add the stringto the stanford list
which is later combined and then executed AFTER each string is turned into a method
and reversed so the main switch is at the bottom
	
	
This will be added last. I decided to build the bypass205 sepaately from the code base to get it working first	



####============================
####      parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("parser_guts called =======")
	check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
	
	if baseline[0] != "nada": #means it converted to uppercase
		y = baseline[0]
			#else:   #added this else  and pass on June 16th
			#	 pass #this puts the input string from baseline[0] into y
		#####################
		#this checks if first case is a number like case 2: returning True if numbers 
	flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
	#####################
	print("if number in first case",valve[0])
		# the key is macro expansion is only called if numbers are True
	if valve[0] == True:    #meaning numbers like case 12:
		macro_expansion(y); #checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
		#end if
		#####################################
	flush_lists() 
	parser_mode_1(y) 	
	
	
##==============================	
##   bypass205(y)   #this is homage to the 205 bypass I took all the time to bypass the traffic in Portland Oregon
##=================================
def bypass205(y): #this runs the input strings thru parser and code gen 
	print("==== bypass205 test =======") #and puts them into stanford list
	del stanford[:] #this empties the stanford list
	#loop thru quail and call everything that I normally do for an end switch
	#######################################
	# THIS IS LOOPING THRU THE QUAIL LIST which was filled above and before bypass205()
	#######################################
	for item in quail: # 0, 1, 2 #so it should call the parser and code gen three times
		y = item #this puts the contents of each string in quail into y 
		
		#everything below here is the same in parser code
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		mytrace("endswitch() bypass205  in switch_cat called")
		show_input_switch_string() #flag for testing this shows the input string
		###############
		parser_guts(y)
		


Friday, July 23rd, 2021 Gilroy Starbucks Wifi
I decided to make it possible for a user to create custom macros and will
have a file for just macros all in one spot.

Today working on the main switch string formatting before it is fed to the parser and codegen.


Thursday, July 22nd, 2021 Gilroy
Looks like nested switches will be working seamlessly this weekend.
Good progress.
9:49 am
	
Some code. What this does is replace the first line of each nested switch which has switch(exp){
and replaces it with a numbered nested method in a sequence. At this point the inner switch
has already been copied and stored in a list and the body of each inner switch in this current 
string has been deleted. This is the last stage before running the code thru the parser using
bypass205() which can do multiple parser and codegens of several strings and concat them to build 
the combined nested switch on the fly and run it with exec().
	
	So the starting point looks like this:
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here       
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){     #here     
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			switch(exp){     #here     
			fallthru

		default:
			print('the end')
}

The output result looks like this:
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			nested_switch_1(n)                 #<<=== this is now a method
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			nested_switch_2(n)                  #<<=== this is now a method call
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			print('== window won't go back up===')
			break
			
		
		case 13 to 15:
			print('at starbucks')
			print('== where is my mocah?===')
			nested_switch_3(n)               #<<=== this is now a method call
			fallthru

		default:
			print('the end')
}
The code looks like this that creates the behavior.
### this started working on july 9th, 2021 Friday. I forgot that it was friday.
			      
endswitch_location=[]
switch_location=[]

def empty_switch_and_endswitch_list_locations():
    print("called empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
			      
##########################################
#### get switch and endswitch locations 
##########################################
def get_switch_and_endswitch_locations(z): #from string z input parameter
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	print("get_switch_and_endswitch_locations(z) called ....")
	print("====== THIS IS THE ONE THAT I NEED ======")	#this catalogues the switch and endswitch locations for an entire input string
	print(" GET SWITCH AND ENDSWITCH LOCATIONS ADDED TO LIST")
	print(" ========  MICKEY MOUSE HOUSE  =========")
	counter=0 #it was 0 starting counting from 1
	for line in z.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		#print(line) #this should be revealing
		#if line.isspace():
		
		if "switch" in line and "end" not in line:
			print("switch found",counter)
			
			switch_location.append(counter)
			counter += 1
			
			
		elif "endswitch" in line:
			print("endswitch found",counter)
			
			endswitch_location.append(counter)
			counter += 1
			
			
		else:
			counter += 1
			
			
			
	del switch_location[0]	#empties it what am I doing here??? july 7th deleting first switch
	print(z)                #now I remember that is the first switch which doesn't matter
	print("I deleted the first switch since I'm not bothering with it")
	print("switchlocations=",switch_location)
	print("the length of switch list =",len(switch_location))
	answer = len(switch_location)
	answer = answer -1
	print("this is how many nested switches are here")
	print("now we should have this many nested switches to contend with",answer)
	print("and the answer is above this line .....")
	#this prevents a bug if I don't have endswitch in the string
	if len(endswitch_location) > 0: #this only proceeds if there is at least one endswitch
		print("endswitch locations =",endswitch_location)
		print("out of curiosity print the number of endswitches", len(endswitch_location))
	else:
		pass
		
	print("this might be simpler to test and use actually======/////???????//////===")
	print("======================================")
	print(" ===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === ")
	print("I need to delete teh first swithc location")
	
	#del switch_location[0] #ALREADY DELETING FIRST SWITCH ABOVE BECAUSE IT'S NOT NEEDED NOT NESTED
	print('switch_location=',switch_location)
	print('endswitch_location=',endswitch_location)
	# I need to feed these into the pear dictionary now down below
	#I will feed the pears list with a loop thru the switch_location list
	########## WORKING ON THIS TODAY MONDAY TO MAKE SOME SERIOUS PROGRESS 
	##########  MONDAY JULY 19TH APPROACHING 12 NOON 
	
	#make pairs here
	#might have to delete teh first switch which throws everything off
	
	
			      
			      
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
switch_list=[]
##########################################
##  put_switch_locations_into_switch_list()  #put the line nubmers of all switch locations into switch_list  
##########################################
def put_switch_locations_into_switch_list():
    get_switch_and_endswitch_locations(coolstring)
    for item in switch_location:
        switch_list.append(int(item))  #was -1 on here #off by one in the string for some reason
    print(" ");print("switch_list=")
    print(switch_list)

#######################################
##  swap_switch_to_nested_method()  #this is making the nested_switch_ number  
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	print(" THIS IS BEING CALLED TO DO THE MAGICswap switch to nested method called....")
	str_list = stringname.split('\n')
	print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)

######################################	

#this is the control center main that runs this operation
#this numbers the nested switch methods top down starting from 1
genius[0]=coolstring  #assignment here 
def loop_thru_switch_locations():  #looping thru switch_list[10,18]
    put_switch_locations_into_switch_list()
    print(genius[0])
    print("switch_list=",switch_list)
    le_number=1
    for item in switch_list:                                    #<<== this has the line numbers in the string of the word "switch(exp){"
        print("item in switch_list",item)                       #<<== this grabs the current item (number)
        #string,switch,line number
        swap_switch_to_nested_method(genius[0],item,le_number)  #<<== item is fed into this as a parameter
        coolstring =genius[0]
        le_number += 1
#######################################

			      
#this calls the change of swapping the inner switch word into a numbered nested method
#where to find the inner switches to replace with a nest method
## calling LOOP THRU SWITCH LOCATIONS (INNER)
## this calls the main function above to swap the inner switch to a method that is numbered			      
loop_thru_switch_locations() #inside of the main switch string and replace with a nested method
#this calls the function to add the inner nested methods where the inner switches currently reside
			      
			      
			      


Wednesday, July 21st, 2021 Gilroy Starbucks 5pm
Massive progress.
The nested cases are copied and put into a list and the main switch string too just now.
I have to fix the indentation for the main string right now. And I have a few more lose ends
but good significant progress.
Next I will turn on the main switch cleaner that replaces the nested switches with a method name.
That code works and I just need to integrate it.

Creating the pair list like this:  [10,20] and adding it to the dictionary was a pain but now works. 
The big leap forward was looping thru the keys in the dictionary and calling the copy_one_nested_switch_string()
Progress accelerated after that finally worked. 

Made many methods to automate everything. Adding records to dictionary. Building records on the fly. 
I am now looping thru the dictionary with the switch case start and stop as params and then calling
the copy nested string method and creating the string for a nested switch which then put into a list of the switch strings.
Just figured out how to automatically add the main switch params to the dictionary.

Monday,July 19th, 2021 10:29am Morgan Hill Starbucks California
between macro works!!!  9 lines of code.

2pm  In short my dictionary works, and I can loop thru the dictionary and call the function to copy a nested string with x and y
params which are now passed along and put into switch_location[0] and endswitch_location[0].
My test used a hard coded dictionary already populated. What was different is I decided to pass the switch and endswitch location
that are in the dictionary value to the copy nested string method. That made it work.

Made my dictionary and can loop thru it to grab each nested string based on the params of start switch and end switch
as value into the dictionary and then when I loop thru the dictionary called pears it copies that switch endswitch set
with the function copy one nested switch. Now I will automate the buiding of the pears list dynamically and 
for the output of running the loop I will have it fill a list before it's passed onto the convert to python stage which already works.

I have a function that loops thru the input switch string and stores the locations of the switches and endswitches already.
Working on storing and accessing switch and endswitch pairs (line numbers) stored in a dictionary
to run thru my function that copies one nested switch. Dictionary uses lists to store pairs
of switch and endswitch line numbers. I will loop thru the dictionary and call the copy_nested_switch function.



Sunday July 18th, 2021 time 11:20 am
I initially made a function that copied one nested switch and it uses many methods to do procedures but works perfectly.
I was then considering making a function to grab two nested switches within a main switch and realized
that I could just use the copy_one_nested_switch function that grabs just one nested switch and use it repeatedly for any more
of nested functions so it behaves like a method. Saves a lot of time. I would then just have to change
the input parameters which are the line numbers within the main switch for the
nested switch start line number and endswitch line number. Like simply moving the needle on the record.


Sunday, July 18th, 2021 time 9:16 am Gilroy, California Starbucks Wifi
Coding helper methods today to reduce code and aid readability.
Looks like nested switch feature will be working within a few days. Most difficult aspects 
have already been conquered. 

Later this week I am adding the macro between. This will be used as:
This came up because it would make for more elegant Z E N code.
	
	if x is between y and z; representing a range. But these would all be numbers.
	
From Wolfram language between[x[min,max]] 

alpha = int(list_of_switch_range[1]) #min switch line number
beta  = int(list_of_switch_range[2]) #max endswitch line number
if counter >= alpha and counter <= beta:    
#would become
if counter between int(list_of_switch_range[1] and int(list_of_switch_range[2]:

Note regarding macros when, unless, until:
I just tested them to prove that it will work. 
They are based on the Lisp, Ruby, and CoffeeScript implimentations of these expressive and powerful words.

They will become methods in the background like this in the preprocessor: 
# so they aren't free floating apparitions - this is behind the curtain in the preprocessor.

	when(condition   == True)
	until(condition  == True) #loop
	unless(condition == False)
	
so that's how they work in reality in the background.

Further I am adding C style comments for the preprocessor too.
/*
comments here
like this
*/

#which gets translated into
# 
#
#
#

#========================================================

Adding #include filename to the preprocessor. It expands to import filename.
It must be within a multiline string with var name and be called within a function.
The point is that this way the code is more natural as a blend with the heritage of C to all programming
while at the same time not violating any of Python's rules - it just bends them a bit.
Also it will invariably be encased in an existing triplestring var that is being executed and thus would only take one line.
The point is to make the code more palatable and "natural" to true programmers in terms of how they think.
It also plays homage to the heritage and legacy of C. And I decided to add it because I can. I don't like the word "can't".

example:
avar='''
#include filename; 
'''
exec(avar)

#it would produce: import filename

Made progress with splitting up a switch string with several switches.
I can detect the number of switches and get their starting line and stop line.
I can copy the nested switch thus extract it and remove the extraneous indentation so it's flush
with the left margin with just one tab for a gutter. 

Friday, July 16th, 2021 Gilroy, California 9:10 am Starbucks
Working on nested switch process integration. It has ten modular pieces and I'm reducing the code currently.
Putting the code in separate files for testing before integration is completed.
First half separates the switch strings and put the result into a list.
Second half puts the generated python into a list that is then modified. Each string is put into a framework
with a def method. Lot going on so it must be maticulous. Had a rocky road connecting the puzzle pieces
so decided to get unstuck by creating completely separate modules to avoid conflicts. And to go slow and easy to
get to the finish line. Working on first half the next few days to get it solid and automated using lots of
helper methods which aids readability.

12:13 pm July 14th
	
Have working code to count the number of switches and endswitches in a switch string
which is used to determine if there are in fact at least one or more nested switches
This is used to set the nested_switch[0] to True also

working on the transformation stage of the input nested switch string sequence
getting the location and end point of each nested switch
copying each nested switch and storing the string into a list
working on one nested string at a time
copy the whole nested string and then only copy and concat the first line of th nested string
copy the string after the nested switch 
glue together the two halfs
Then repeat the process for other nested switches if there are any.
Then loop thru the modified switch string and replace each nested switch word with a nested switch method that is numbered 
top down in order of occurence.

Next stage
This is done to each nested switch string
take a nested switch string which left adjusted by default
and add the nested method def at the top and then indent the entire
switch string by one tab added to the left side

Last Stage
Last stage is concatting the layers of the string sections by concatting
the elements of the list which is full switch case strings which have already been reversed
so that the main switch is last since they will be put into a triple string with a variable
and then executed.


Wednesday, July 14th, 2021 11am California Time Santa Cruz Avenue, Menlo Park, California down the street from Cafe Borrone

Working on the last stages of connecting the dots for
transforming the nested switches into python and putting them into methods
and into a single docstring and executing it. Doing each stage in a separate file today to get them debugged. They all work already. Six I believe.

Macros are cool. These will be put into methods later.
Had to have a little fun this morning.
Made working macros: when, unless, until  right out of the Lisp playbook. Since CoffeeScript and Ruby also have when,unless,until
I decided to add them for the fun of it. Still in the primordial  stage. 

##===========================================================
## == macro when ============================================
##===========================================================


#if condition = true
#condition = "('apple == 1 and banana == 10')"

starbucks='''
apple = "1"
banana = "2"

when condition == True:
    print("they are TRUEEEE")
else:
    print('they are False')

'''
#runthis(starbucks)
print(starbucks)
starbucks =starbucks.replace('when','if ')
starbucks=starbucks.replace('condition', "(apple == '1' and banana == '1')")

print(starbucks)
print("the moment of truth nears...")
print("")
exec(starbucks)
print('=====')
print("===== end of testing when===============")


##==================================================
### macro  until ===================================
##==================================================
funny='''
print("now trying until")   
 
total = 0
# u n t i l condition == True
until total < 10:
    print("not yet ",total)
    total += 1
print("now total has reached 10")
'''
print(funny)
funny =funny.replace('until','while ')
print(funny)
exec(funny)


#===================================================
### macro unless ===================================
#===================================================

#The code in the unless block will be executed
# if the given condition is false.
#trying u n l e s s
# if  when condition not true(meaning = False)
condition = "(score >= 40)"
stars='''
score = 22

unless condition == False:
   print("score =",score)
   print("this worked if this shows up")
   print(" special code would run here")
   print("proving the condition was FALSE ==")
else:
   print("it is indeed true")
   print("score =",score)
   print("if it was True this would show up")

'''
print(stars)
stars =stars.replace('unless','if ')
print(stars)
print("====")
stars =stars.replace('condition',"(score >= 40)")
print(stars)
print("=====")
exec(stars)




July 13th, 2021  9:45am Gilroy, California
	
Today I am working on the trapeze the last part connecting the generated python with building the doc string with
the variable to be executed. Adding def nested_switch_number to strings and indenting properly. The puzzle pieces
are completed and I am connecting them together today. Then I will be doing more testing. Then I will upload the code to github.

Example of generated python for doing two nested switches
and the results of it running. What you see below is all chunks from a list
that is looped thru and concatted into a triple multiline string
and then executed. I just added the ability to get an output result from a nested switch
that is put into a list and accessible after the inner switch has completed.
BELOW IS THE GENERATED CODE

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


#exp = varholder[0]
nest_output=[]
nest_output.append(0)

def nested_switch_1(n):
	print("====starting nested_switch1===",n)
	
	caselist1 = ['zoo time', 'more']
	caselist2 = ['the beach in santa cruz']
	caselist3 = ['default']


	inswitch(n)
	while True:
		print("case=",case)
		if case in caselist1: # ['zoo time','more']
			print("swe are now in nested switdh 1")
			print("an francisco zoo")
			print("feed the flamingos")
			infallthru('the beach in santa cruz')

		elif case in caselist2: # ['the beach in santa cruz']
			print("volleyball and boardwalk")
			nest_output[0]='santa cruz beach boardwalk output'
			break

		elif case in caselist3: # ['default']
			print("we are done here")
			break

		else:
			print("we are done here")
			break



def nested_switch_2(n):
	print("======starting nested_switch2=====",n)
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']


	inswitch(n)
	while True:
		print("case=",case)
		if case in caselist1: # ['blable']
			print("do this is in nestedswitch 2")
			print("yep")
			infallthru('more')

		elif case in caselist2: # ['more']
			print("nice")
			break

		elif case in caselist3: # ['default']
			print("we are done here")
			break

		else:
			print("we are done here")
			break




varholder=[]
varholder.append(0)

varholder[0] = 1
exp = varholder[0]

x = varholder[0]
def call_main_switch(x):
	print("call main switch called with",x)
	caselist1 = ['1']
	caselist2 = ['4']
	caselist3 = ['8']
	caselist4 = ['default']
	# main switch test

	switch(x)
	while True:

		if case in caselist1: # ['1']
			print("inside of main switch first case")
			print("where's the dog house!")
			print('first prize')
			n = 'more' #input to nst swtch
			nested_switch_1(n)  # nest 1 test ============
			#example getting output from the nested switch
			print(nest_output[0]) #output from nested switch
			print('after doing nested switch 1')
			fallthru('4')

		elif case in caselist2: # ['4']
			print("inside of main switch second case ")
			print('kangaroo hop hop!')
			 #maybe keep it a comment until it's in python        
			print('taught me how thru write code')
			n = 'blable' #input to nes swtch
			nested_switch_2(n)  # nest 2 test==========
			print("after doing nested sw tch 2 ===")
			fallthru('8')

		elif case in caselist3: # ['8']
			print('mocha blast')
			print('== 31 flavors===')
			fallthru('default')

		elif case in caselist4: # ['default']
			print('the end')
			break

		else:
			print('the end')
			break




 
#notice no indentation for this line
call_main_switch(x) # see if this works
#this calls the main switch when this is executed


call main switch called with 1
inside of main switch first case
where's the dog house!
first prize
====starting nested_switch1=== more
case= more
swe are now in nested switdh 1
an francisco zoo
feed the flamingos
case= the beach in santa cruz
volleyball and boardwalk
santa cruz beach boardwalk output
after doing nested switch 1
inside of main switch second case 
kangaroo hop hop!
taught me how thru write code
======starting nested_switch2===== blable
case= blable
do this is in nestedswitch 2
yep
case= more
nice
after doing nested sw tch 2 ===
mocha blast
== 31 flavors===
the end

 


July 12th, 2021 10:20am
This now runs in Python.
I will try deeper nesting next.
THIS IS WHAT THE INPUT SWITCH CASE CODE LOOKS LIKE
THOUGH IT MUST BE IN A TRIPLE STRING AS NOTED WITH NECESSARY LINES
ALSO THIS IS CRUCIAL. THIS VERSION STILL REQUIRES PYTHON STANDARD INDENTATION.
MY NEXT VERSION WILL DO SMART-AUTO-INDENT.

sw=''' <-----NECESSARY at beginning
	exp = '4'
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthrough #this spelling works too from Swift
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp = 'blable'
			switch(exp){          
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is from php
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			exp = 'fish'
			switch(exp){          
				case 'fish':
					print("do something")
					print("yep")
					fallthru
				case 'trout':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			fallthru

		default:
			print('the end')
        }     <----NECESSARY at end
'''           <----NECESSARY at end 
endswitch(sw) <--- NECESSARY at end (this is a method that calls the parser and codegen)		
				
July 11th, 2021  11:07 am
Exciting times
did a run thru of how the output code needs to look and ran it worked.
so I now know for sure how to have the output python strings of the different switch cases to
cooperate and work together. Last file called playtime_testing.py
Monumental last hurdle cleared. What a relief. So cool. 
	
	
	
	
	
	
July 10th, 2021  11:12 am Starbucks in Gilroy.
Loop works to change switch to nested switch numbered in order from switch line number list!

loop_thru_switch_locations() #this calls swap_switch_to_nested_method(stringname,linenumber,series_num):

==INPUT==

#-------------------  july 10th, 2021   11:03 pm  -------starbucks coding-------

coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){          
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){          
			fallthru

		default:
			print('the end')
}
'''



### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
#I made the method to change the switch for the nested switch into the method numbered
#######################################
##  swap_switch_to_nested_method()
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	#print(coolstring)
	str_list = stringname.split('\n')
	print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)
	
	
First successful test of looping method that goes thru switch line number list and changes switch to nested method
on-the-fly and modfies the string before it goes into the parser and code gen
I figured out that it's simpler to modify the input strings in JavScript switch case mode instead of in python mode later

##=================== section I just added just now july 10th this morning 2021 ===================	
switch_list=[]
switch_list.append(10)
switch_list.append(18)
# test list of switch_list[10,18] representing the line numbers gleaned earlier in the input string of nested switches

#Testing this out now

genius[0]=coolstring  #assignment here 
###=====================================
###  loop_thru_switch_locations():
###=====================================
def loop_thru_switch_locations():  #looping thru  switch_list[10,18]
    print("loop_thru_switch_locations called")
    print("switch_list=",switch_list)
    le_number=1 #number sequence for the nested switches starting from 1 by default
    for item in switch_list:
        print("item in switch_list",item)
        swap_switch_to_nested_method(genius[0],item,le_number) #I had to modify this to use the list genius[0] which holds the mutable string
        coolstring =genius[0] #this copies whats' in genius[0]
        le_number += 1
    #it can't be this simple can it?
    
loop_thru_switch_locations()
print("did it work=============MMMMMMMMMM----======MMMMMMMMM==========")
print(genius[0])   

OUTPUT of the changed modified string

loop_thru_switch_locations called
switch_list= [10, 18]
item in switch_list 10
changing line 10
item in switch_list 18
changing line 18
did it work=============MMMMMMMMMM----======MMMMMMMMM==========

switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			nested_switch_1(n)
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			nested_switch_2(n)
			fallthru

		default:
			print('the end')
}




JULY 10TH, 2021  9:51 Am Gilroy Starbucks near Panera Bread
Final push to tie together all of the loose strings.
Working  on aspects of after the bypass205 has been called and filled the stanford list 
aftger the input strings have been parsed and code generated with the generated python of the main switch string 
and n number of nested switches.
I modified bypass205 cutting the code by 80% by making a method of parser chunk of code which was in endswitch()
I make the build layered cake for concatting the final python nested switch strings and main string and inswitch and infallthru methods.

reverse_stanford_list() #so the order is the nested switches first and the main switch is last on the far right
#this is so that when the concatted string is executed it's in the correct order

build_stacked_cake_string_combining_stanford_list() #this loops thru the stanford list and concats it into a string
# which will be executed

bypass205() now looks like this:
	########### bypass 205 ########### july 1st 2021 testing starbucks in gilroy
def bypass205(y): #this runs the input strings thru parser and code gen 
	print("==== bypass205 test =======") #and puts them into stanford list
	del stanford[:] #this empties the stanford list
	#loop thru quail and call everything that I normally do for an end switch
	for item in quail: # 0, 1, 2 #so it should call the parser and code gen three times
		y = item #this puts the contents of each string in quail into y 
		
		#everything below here is the same in parser code
		switchcasetester='';switchcasetester=None;
		del switchcasetester;switchcasetester='';
		mytrace("endswitch() bypass205  in switch_cat called")
		show_input_switch_string() #flag for testing this shows the input string
		###############
		parser_guts(y)

		
#this is parser_guts()
####    parser_guts()           #dreamed up on July 10th, 2021 to see if it would work
####============================
def parser_guts(y):
	print("parser_guts called =======")
	check_if_uppercase_constant_cases(y)  #if UPPCASE this senses it and converts to string
	
	if baseline[0] != "nada": #means it converted to uppercase
		y = baseline[0]
			#else:   #added this else  and pass on June 16th
			#	 pass #this puts the input string from baseline[0] into y
		#####################
		#this checks if first case is a number like case 2: returning True if numbers 
	flow_valve_input1(y)   #puts True or False into valve[0] added April 2nd, 2021
	#####################
	print("if number in first case",valve[0])
		# the key is macro expansion is only called if numbers are True
	if valve[0] == True:    #meaning numbers like case 12:
		macro_expansion(y); #checks if macros and expands them and converts numbs to strings
		y=None; del y; y = cray[0];
		#end if
		#####################################
	flush_lists() 
	parser_mode_1(y) 	


#note: I will rename the vars after it all works. Approaching the finish line and I want to see it work before I beautify it.
# building stacked cake is where I will combine top down the generated python strings.
# I am doing this trial run to see what is missing. Victory approaches.

# JULY 10TH, 2021
##====================================================
## BUILD STACKED CAKE STRING COMBINING STANFORD LIST
##====================================================
def build_stacked_cake_string_combining_stanford_list(): 
    print("PRETENDING THAT THE LISTS HAVE BEEN MODIFIED THOUGH NOT REALLY YET")
    print("==================")
    print('lets pretend that the strings are finished and I will concat them together')
    print("but not run them")
    print("remember after the stanford list has been reversed the LAST list will be the main")
    volleyball ='' #initialized
    print("about to concat a string called volleyball")
    count =0
    for item in stanford:
        volleyball += "\n"
        volleyball += "count="
        volleyball += str(count) + "\n"
        volleyball += item
        volleyball += "\n\n" #spacer 2 lines
        count += 1
        print(count)
    
    # here I can manipulate the output python code 
    # uppercase_test[0] == True:
    # baseline[0]="nada"
    print("volleyball =",volleyball)	#this is the output that will generate the final combined concatted string	

##=============================	
Last night and this morning I refined the method to add the nested switch method into the input string where the 
switch(n){ is currently and replace it with a serial sequential numbered method. Each inner switch is numbered top down
in order. The last part I will add is starting with 1 at the top. Right now it's hard coded. But the method works that replaces
the switch to the nested switch method name. I still need to next put this into a loop to do it automatically instead of manually.
### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
#I made the method to change the switch for the nested switch into the method numbered
# Note: I have a method (I made a few days ago) that makes a list of the line numbers of all switches in a string 
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	#print(coolstring)
	str_list = stringname.split('\n')
	print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)
	
	
# example of input and the output result	
#string_change =coolstring
#stringname=coolstring
print("now change the inner switches to the nested method numbered")
# the params are STRINGNAME to modify, LINE NUMBER OF SWITCH(TO CHANGE) in this string, number that will be the SEQUENCE SERIAL NUMBER for this nested method
swap_switch_to_nested_method(coolstring,10,1)
############# still to do next ############## haven't added this feature yet
#NEXT part will be putting this into a loop with just the line numbers OF NESTED SWITCHES in a list to do this 
# with method calls to swap_switch_to_nested_method()
##############################################
print("after first change ====>>>>>>>")
coolstring =genius[0] #this copies what is in genius[0] into the immutable string name
#series_num = number_series[0] 
swap_switch_to_nested_method(coolstring,18,2)	#this does the next nested switch change
print("after the 2nd change ...")
#coolstring =genius[0]
print(genius[0])
print("done with this test of the new method")	  

INPUT string looks like this at this stage:
# this represents AFTER the nested switch cases have been cut out except for the line with switch
# I cut out the nested switches after copying them and then 
# I made a copy of the whole string line by line but skipped the lines in the range of the inners switches except the top line with switch
# which I left as a marker
	  
coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){          
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){          
			fallthru

		default:
			print('the end')
}
'''
	  
OUTPUT result of replacing original switch (the body of the switch was already removed beforehand and copied)
# this part is funny but true. I will add one more step to prevent a bug.
# when concatting the strings in cake I have to comment out the nested_swithes with # in front of them so they don't get called
# and then the last step is taking out the # in front of the nested_switches and then executing the combined string
# at this current stage it's okay to have them uncommented
	  
	  switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			nested_switch_1(n)
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			nested_switch_2(n)
			fallthru

		default:
			print('the end')
}
	  
	  
	  
	  
	
July 8th, 2021 1:08 pm Starbucks Santa Cruz Avenue, Menlo Park, California near Stacks.
Made progress with parser to read and copy nested switch cases and then delete them (after they have been copied and added to a list) and glue in a method numbered
within the bounds of the main switch on the same line and in the case where the nested switch was. Again, nested switches
are placed into their own methods for simplicity. Yesterday I was able to replace two nested switches with methods correctly.
There is a great deal of juggling that goes and and so I have broken everything down into stages and I work on the behavior
for each stage and soon the constellation of the componenents will be ready to connect together.

July 6th, 2021 Tuesday 12:41 pm Starbucks Hollister, California near Target
Working on mapping out procedural steps to create the process of taking the output python switches in the stanford list
and converting it for concatting the cake with layers (each layer a nested switch)
Each nested switch has a unique numerical number in it's name and has to be above the main switch to be called.
The location of each nested switch has essentially an address for the switch it directly lives within in which case 
(number sequence from top of that switch) and what line number within that particular case.
So I have been working backwards from the end goal of the switch case in python. And I compare with what is currently working
and what the final output python needs to look like. 

	
July 5th, 2021 Monday. 9:47 am Starbucks Santa Cruz Avenue, Menlo Park, California.
	
Decided to divide the nested switch code  component in half to manage the complexity. Reducing the complexity is key.
There was just too much to think about all at once. 
So the beginning is called the Before parsed and codegen and the After is juggling the building of the python components.
I have already make prototype working code for each puzzle piece but now I have to turn them into methods.

The Before part involves determining the switch count, but first checking if the input string has more than
one switch and at least one endswitch. All nested switches in the input string must use an endswitch which differentiates
the nested switches from the main switch. Also indentation is key as always in Python.

This was a happenchance discovery. When I make the main switch with the nested method names placed within it they get called.
so I comment them out until just before the main switch is called.
First half deals with the input preparing it for running thru the parser and code gen.
Second half modifies the nested output builds the nested methods in the layered cake to concat it together and then it's exec(combined_string)

Inside of endswitch() I prescan the input switch string to count how many switches are in the string.
I then have an if condition. 

if switch_count > 1 :  
    bypass205() #this loops thru a list of the input strings of multiple swith strings
else:
   #does regular parser and codegen()

<code>
if switchcounter > 1 and endswitchcounter >=1:
    nested_switch[0] = True
    # the nested switches have already been sensed and put into a list called quail
    bypass205(y) #this runs each switch string in the list thru the parser and code gen and 
else:            # in the code gen they are put into stanford list (appended)  and not executed at this juncture
    nested_switch[0] = False
</code>		

What exactly bypass205() does is quite remarkable.
A normal endswitch(y) handles just one switch case string. But with this bypass we can still just use one endswitch()
but we can deal with a multi-combo-nested-switch of any size. So the bypass205() is triggered by a switch counter > 1 essentially
and then after the nested switch string is divided up into individual switch cases and added to a list I simply loop
thru the list and call the parser and codegen. The other aspect that's different is that at the bottom of codegen()
normally the concatted string of python that is assembled on-the-fly using lists it's executed. 
But in the situation of the scenario of a nested_switch which will have a flag
the output for each generated python switch is stored in the stanford list and NOT executed.

But upon finishing the entire list being finished and filled after translating into python
then another function is called after codegen which takes the stanford list and
adds infallthru and inswitch replaces and puts the nested switches into custome method names
that identify the location in the sequence and level of cases and line number
and then it's executed.
##========================================
#In the sequence of the function calls for the parser
switch_code_gen() #the parser and codegen are called multiple times and add the output to stanford list uninterupted
managing_nested_switch_scenario() #<<========this is called after the stanfordlist has the python switch strings
# this normally by default does just one exec(string)
# but it doesn't execute the string if it's a nested switch
# but it does nothing if it's not a nested switch which is determined by 
# whether the stanford list is not empty
# if the stanford list len is greater than 0
# then it modifies each switch string with methods and concats them with makecake and executes it
#
#so for a normal one switch case string managing_nested_switch_scenario does nothing
#but if a nested_switch is True then it takes the python output strings from the stanford list and
# converts it into a gigantic multiline string encapsulating the methods of the nested switches above the main switch and
#calls the main switch.
#=========================================

A normal endswitch(y) call takes in one switch input string and checks if macros and expands them
But what is different is we are still using endswitch(y) for handling a nested switch by using bypass205()
which is called within the beginning of the endswitch() after the switch counter sensor determines if the input switch string
has more than one switch (meaning it has nested switches) each that must end in endswitch which aids readability, but is also 
a determining factor if a nested switch is indeed nested.
So after sensing that due to multiple switches is true then bypass205 is triggered and just after the switch counter senses more than
one switch is encased in the input switch string then these are separated and put into the list quail. Like a mother quail and her little
babies walking in single file behind her. This separation of the nested switches is done before bypass205 is called.
Then within bypass205 I simply loop thru the list and call the parser and codegen multiple times till n and 
these each run thru the parser and codegen like a regular switch and each is appended to the stanford list to hold the python output
for each switch. From this point the second half of the transformation of managing and executing the nested switch in python continues.


#Looks like this inside of bypass205 when it's called :
	def bypass205(y): #this runs the input strings thru parser and code gen 
	    print("==== bypass205 test =======") #and puts them into stanford list at the end of the codegen
	    del stanford[:] #this empties the stanford list: this initializes the stanford list to empty
	    #loop thru quail and call everything that I normally do for an endswitch()
	    for item in quail: # 0, 1, 2 #so it should call the parser and code gen three times
		y = item #this puts the contents of each string in quail into y 
		#rest of calls within endswitch()
		
Thankfully, the bridge of bypass205() (works) which is triggered in the endswitch after a nested switch string is detected
in input can take in a string of n nested switches and separates them.
I also refined and perfectec my switch detector to detect the accurate number of switches (one main and n nested)
which is critical in terms of accuracy. These are put into a list.
For the second half the nested switches are put into unique method names and then will put into a list.
The list is then concatted and called exec(combined_cake)


July 3rd, 2021 Saturday coding working on automatic nested switch management
I have the design figured out and tested the bypass205() which does the multi switch string - meaning a switch with nested switches.
Everything works. I just need to turn the current raw code into methods so I can automate it.
My example uses one switch with a nested switch and I need to write some fuzzy logic to automate separating the nested switch(es)
from the main switch that they reside in and determine their address position within the switch. I decided for convenience that
all nested switches must use endswitch to end nested switch.
I'm working on the automating of the method naming for the nested switches.
I am working on each new component outside of the main code base and playing with it and then slowly adding each one to the
main code base. This might take another week to refine it.
Last night I had a revelation for creating the main switch and separating the nested switches from the main switch.
Rather than deleting the lines within the nested switches (my original strategy) I decided instead to 
create a new string that I concat and just don't add those strings within the nested switch that I have already copied for
each nested switch. This was out of left field and then I realized that it was a brilliant and simple solution  that is easily workable.

So in review I am working on the section of the code where the switch with nested switches is read and analyzed to determine
what is in it and managing the separtion of the nested switches, noting their locations, naming the switches by location
and then modifying the main switch string so that it looks like the design with the nested switches turned into methods that are called.

Next after that I will work on modifying the python generated for each switch and preparing it to be put into the unique method names
and indented by one tab more to the right and they will each be placed in a list.
I will be using lists heavily for the manageing and analysis.



July 1st, 2021 Thursday 8:17 pm California time Starbucks Gilroy, California
Critical test worked on first try. I didn't expect it to actually work the first time.
Of course I spent days designing it. The rest of nested switch management
is a cakewalk. Stunned silence. Wow. Holy Toledo.

July 1st, 2021 Thursday 7:48pm California time Starbucks Gilroy, California
Working on proof of concept of taking a switch with nested switches and separating it into individual switches. (that works)
Working right now on testing taking the input strings of the (3 test strings) representing separate switches
and running it through a loop with the same contents of function endswitch() but will use bypass205 on 5 (bypasses traffic in Portland, Oregon) 
so that it's controlled and can do more than one string sent to th code generator and grab the string of the python code
and put each generated python switch into a list.
it will do all three separately and then generating the python with codegen
which is NOT exec() but stored into a list which I will do other modifications to before exec().  
That is what I'm attempting right now. It is critical for nested switches
to work. It involves fuzzy logic and flags. Once it works I will add more methods and reduce the code to simplify
and streamline it.


June 30th, 2021 Wednesday 8:45 am California Time @ starbucks Santa Cruz Avenue, Menlo Park, California
	
Just solved the missing puzzle piece which turned out to be simple actually. Nested switches will work - as many levels deep as you want.
Now I just have to connect the puzzle pieces. And innumerable number of nesting is possible. You want to do 1,000 nested switches within
one switch. - go for it. Go wild.
I can detect switches (and count them) within a switch case input string.
I can extract the nested switch(s) from the main switch and put it/them into a separate string.
I can then put all of these switches into separate strings into a list.

For each run the Stanford list is emptied at the top before anything happens. This can be controlled at will though.

So the strings of the output strings of generated python are collected in the stanford list in order that the switches are encountered
within the main switch.

If there is just one switch then it's just stanford[0].
All nested switches within the main switch are loaded in the list stanford based on order of apperance(location)
and the count of the stanford list is used to manage everything.

I can run the list thru a loop calling endswitch(x) to generate the python code version.
I can "now" feed each output python string into a list. This is list stanford.
The gathering of this data (harvesting) is completely independent of whether an output switch runs or not (based on flags)
This is important because it's less to think about, dwell on, and less complexity; it's utter simplicity.

And what I have been spending my time on already works. I can take a nested switch string in python output and convert it into
an inner nest method. I can name the method name correctly in sequence with depth(tab count), 
case number in sequence(where it resides within), and line number that the original switch was so it's in the exact line within the case.
Further I still need to add the input list which will feed the input var n or exp, right now settled on n that will fall into the method input
via the list in the background since lists are mutable and so Lispish.
I can also replace the main(mother) switch with the nested_switch method and completely remove the nested switch.
One works, I will work on more nested switches. I am also doing the automatic indentation (smart tabs) for the nested switch methods which are within
methods.

Any depth nesting switches is possible based on this design.

Next I'm working on the layered cake.This includes the method names which are unique to nested switches.
Each nested switch method has a unique name. Further that will be a list variable for input to each nested switch and 
an output list for maintaining the output being live within the running switch.
The bottom layer is the main switch and the nested switches are methods above it.
These are concatted together and then executed.

Fixed bug in converting a nested switch from a regular switch into a nested switch which uses different methods: inswitch() and infallthru()
and is encased inside of a unique numbered(named) method. For some reason replace() wasn't working and it was missing changing the
switch and fallthru into inswitch and infallthru so I did a work around since there is an aparent bug in the replace() method.
	
	
	
June 28th Monday, 2021 10:15 pm
Significant progress. modified initial design slightly aiding the construction of the nested switch more easily.
Happy with progress past few days. Going well. Good momentum. 

June 28th Monday, 2021 3:53 pm
Next Three days just doing the design engineering and prototyping of building a nested switch and running it thru
the module to build the concatted strings and then executing it. Each nested switch is represented by a method
and each is generated seperately. It  alpha phase it might work tonight. beta by Wednesday evening. Working on using
lots of methods to simplify and reuse as much as possible. Thankfully the hardest part already works. Just juggling now really.
	
Engineered how nested switches parser and code gen will work. Code name Juggler.
Should be working in a few days. Building it in small components and then
will connect them together and it should work. Using 2 flags. I love fuzzy logic.

June 24th, Thursday, 2021
11pm. After I got it working I redid it in lists and it's much more streamlined and automating it will be simpler.
It's much cleaner now.

8:32 pm California time
Working on functions to insert the nested_switch_method into the parser just before code generation(first one for testing).
After detecting the correct case number where the nested switch is and the line number in sequence within the case
I worked on tonight copying the case body lines and then insert the nested_switch on the proper line
and rewrite the case body lines to insert it. Refinining the algorithm now that it works. Decided to just use strings and not lists for this one.



June 22nd, 2021  9:17pm California time
Did some more testing. I was just copying and pasting C switch cases off the web to see if they would run.
So far a missing break in default doesn't crash anymore.
But using the word "case" anywhere other than for case name; like in a print statement causes a crash.
And since it's python if the indentation isn't correct per the design it will crash.
one tab in front of switch
two tabs in front of case
three tabs in front of line below case word
etc, etc
So, this means if a programmer copies and pastes C or JavaScript code it won't parse and run unless
the indentation is correct. So I will next workon auto-indent detection and fixing for switch cases.

Right now I am heading full steam ahead on finishing up the construction of the output python generated
from the input switch case string for nested cases which is extremely tricky but luckily through sheer determination
I am making daily progress. I expect it to be solid and bug free and working by the 4th of July at this point.
The project has exceeding my expectations and had I known how deep it was going to be like one hundred fathoms
deep I might not have attempted it but it's a fun project nonetheless.

June 22nd, 2021 Tuesday time 12 noon Santa Cruz Avenue Starbucks near Stacks and Cafe Borrone in Menlo Park.
I just saw and an example of the new match case (the new switch case for python) that I'm competing with.
It had an example with function calls from inside of cases. I realized I hadn't tested that scenario other than
my buildstring() method and adder() for math water fall style so I just got that feature working. Bad ass.
To work the new functions(methods) are put into a file called method_calls and that file is imported
at the top of official_switch_case_silver this way the user (developer) doesn't have to
actually fiddle inside directly in the switch module but this way it will work and it's 
easy to use and clean.

In other news I successfully have started the conversion process of taking the output of a nested switch and 
changing it into nested mode this way I can run it through the parser and codegen with zero changes and then make
changes afterwards which is more zen like. And I will merely use the nested_switch flag to determine which
switch case going through needs to have changes to the nested mode after the code gen is done.


Example below
sw ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			do_something()
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			do_something_else()
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



June 21, Monday 2021 time 11:08 pm 
	
With my new approach the code generator has fewer hiccups.

Had difficulty with nested stages so for safety using working switch case and s l o w l y connecting the
stages together to prepare the python generated switch which is extremely different then a regular switch.
Slow and easy wins the race, and rushing is never good. Working continually backwards and now only sticking
to the set up and not trying any curve balls to make it work. Making more methods for the delicate engineering
so it will ultimately mean less code and easier to manage and comprehend.

What I got working today was inputing the input for the generated nested switch method. It was tricky but I solved it.
Since I made the end output which runs the real tricky part was getting the input nested switch to translate
and then after extreme difficulty I ended up keeping it in regular switch mode to run thru the parser and code gen
to generate the switch code output and then I am making the changes to make it work within a method which then calls
itself. When the bugs started stopping all forward progress I was forced to break it into smaller chunks and greatly
simplify the stages of the transformation. Fortunately the prototype works and using a representation of a nested switch
within a method is the saving grace for this actaully working. 

I also had to detect tabs and had no fun in figuring out how to subtract tabs from the front of lines and add tabs
to create the correct indentation since the switch is within a method. But I overcame that obstacle with steadfast 
determination and absolute commitment. The end of this project is near. I am going to make a new folder with
the key files in it so that I can focus on the end game. Right now it's coming together and by having smaller chunks
that I can manage it's easier to control the behavior of the nested switch methods.

To make it work I am reducing the nested program into ten small programs to bring order to the chaos
amd reduce the complexity. Once the puzzle pieces work doing their specific small behavior the nested switches
will fly.


June 21 Monday, 2021 time 12:35 pm starbucks Santa Cruz Avenue in Menlo Park, California (Cafe Borrone closed today)
Finishing the last aspects of connected the layers of the cake together.


Looks like July 4th project Tron will be completed.
C style switch converts to python 3 on-the-fly and runs.
Right now bug if case used inside of a block of code beneath a case. I will have it ignored to bypass it. 
Nested switches as deep as you want.
Just finishing the nested switch engine. Parser works. Working backwards on Codegen to assemble and link
together the output generated python with nested switches treated as methods which is done with encapulation within a string.
So after a nested switch is extracted from a regular switch  it is copied to a list.
Then it is run through the switch module and converted into python.
This is where the fun begins.
Swapping words switch to inswitch and fallthru to infallthru.
I then create a new unique method name and concat the generated python and add indentation.
Just solved problem of adding input var to trigger the switch by putting it into a list
which is accessed when the nested which (living in a string) is called the innerswitch method (when called) accesses the list[x]
and then it functions perfectly. If lists were not mutable this would be extremely difficult.
Everything for the engienering is been broken down into small pieces. Working on the creation of the goal
string representing the already translated python switch representation. 
Battling bugs with careful maticulous design and frequent testing.
Created a staged apporoach of rocket modules that are independent but run together in a sequence to manage the complexity.
Note: each nested switch is represented as a method that is made on the fly and triggerd by the method name call.
This aids readabiliy and clears away clutter and allows the management of the insane complexity of juggling literally possibly
thousands of nested functions within the maze of a switch case that could conceivable reach millions and depth of an unknown n
since all code morphs and changes seemingly at will as design requirements evolve.
This address feature might involve a fourth parameter for safety perhaps. Time will tel..
Victory approaches. Address location of nested switchs. Still need to make simple numbering of nested switches x for depth level y case(as sequence number) residing in, 
z if multiple (as a number in sequence of nested switch possibly in a series) within a case. ie, 3 nested switches in a series within a case
	
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
