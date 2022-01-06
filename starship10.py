## this works dec 31st, 2021
## Blake Southwood Software Engineer 

#import official_switch_case_silver
#from official_switch_case_silver  import *  
#from booster2 import *
print('top of starship.py file ')
print('')
#I have to import a list now to do it

zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'


#print("from the web trying this out")

quail=[]
# I am adding the quail list to practice filling it

endswitch_location=[]
switch_location=[]

#new on january 2nd, 2022======================
def clear_out_all_lists_for_reset():
    del endswitch_location[:]
    del switch_location[:]
    del sweetlist[:]
    del holdinglist[:]; 
    del boomerang[:]


def empty_switch_and_endswitch_list_locations():
    #print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations 
##########################################
def get_switch_and_endswitch_locations(z): #from string z input parameter
	#print("### must work now ###get switch and endswitch locations########")
	#print("####3##get switch and endswitch locations########")
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	#print("=====get_switch_and_endswitch_locations(z) called ....")
	#print("====== THIS IS THE ONE THAT I NEED ======")	#this catalogues the switch and endswitch locations for an entire input string
	#print(" GET SWITCH AND ENDSWITCH LOCATIONS ADDED TO LIST")
	#print(" ========  MICKEY MOUSE HOUSE  =========")
	counter=0 #it was 0 starting counting from 1
	for line in z.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		#print(line) #this should be revealing
		#if line.isspace():
		#right here going thru input string look for switch and endswitch
		#and append the line number to either switch_location or endswitch_location
		if "switch" in line and "end" not in line:
			#print("switch found",counter)
			switch_location.append(counter)
			counter += 1			
		elif "endswitch" in line:
			#print("endswitch found",counter)
			endswitch_location.append(counter)
			counter += 1
		else:
			counter += 1
			
			
			#THIS DELETES THE FIRST SWITCH WHICH WE DON'T USE
	del switch_location[0]	#empties it what am I doing here??? july 7th deleting first switch
	#print(z)                #now I remember that is the first switch which doesn't matter
	#print("I deleted the first switch since I'm not bothering with it")
	#print("switchlocations=",switch_location)
	#print("the length of switch list =",len(switch_location))
	answer = len(switch_location)
	answer = answer -1
	#print("this is how many nested switches are here")
	#print("now we should have this many nested switches to contend with",answer)
	#print("and the answer is above this line .....")
	#this prevents a bug if I don't have endswitch in the string
	if len(endswitch_location) > 0: #this only proceeds if there is at least one endswitch
		pass #print("endswitch locations =",endswitch_location)
		#print("out of curiosity print the number of endswitches", len(endswitch_location))
	else:
		pass
		
	

	
	# I need to feed these into the pear dictionary now down below
	#I will feed the pears list with a loop thru the switch_location list
	########## WORKING ON THIS TODAY MONDAY TO MAKE SOME SERIOUS PROGRESS 
	##########  MONDAY JULY 19TH APPROACHING 12 NOON 
	
	#make pairs here
	#might have to delete teh first switch which throws everything off
	
	
	
 ####<<========
#switch 1, 10,29
#endswitch  20, 38

#switch_location
smart_rat=[]
string = """
line1
line2
line3
line4
line5"""
str_list = string.split('\n')
#print('changing line 3')
str_list[3] = "my new line value"
string = "\n".join(str_list)
#print(string)

#print("end of test from the web")
#print("=========")
#this simulates after cutting out the inner switches but leaves the first line
#which is used for replacement of the nested method()
############################################################
########## august 5th testing what to use now #################=========$$$$$$$$$$$
############################################################
# this represents and input string with inner switches cut out
#what remains is just the switch word which will be replaced

#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 

#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 

# october 11th, 2021 
#testing texas here to do what I want

sweetlist=[]
holdinglist=[]; holdinglist.append(0) #to create slot 0
boomerang=[];   boomerang.append(0)
#def get_switch_parents()

# I need to do a second pass and modify this just modified 
# texas string to show it's inner switch line numbers

##============================================
##  modify_string_before_splitting_it_up():
##============================================
def modify_string_before_splitting_it_up():
    #print("texas string first")
    #for line in texas.splitlines():
     #   print(line)
    #print("=========================") 
    counter =0    
    #print("modify_string_before_splitting_it_up():")
    craftline =''
    for line in texas.splitlines():
        if holdinglist[0] == 0: #this compendates for the first one
            holdinglist[0] = '1' #ASSIGN JUST ONE EQUAL
        else:
            boomerang[0]= holdinglist[0]
    
        if "switch" in line and "end" not in line: #this eliminates endswitch confusion
            tabcount=line.count("\t")#                                   line number          tab count 
            if tabcount == 3: #this compensates for 2nd nested switch at 3 tabs
                boomerang[0]='1' #representing parent switch 
            else:
                pass
            if tabcount == 3:
                boomerang[0]= '1'; #assignment only use one = 
            craftline += line.replace("switch(exp){","switch(exp){ # "+str(counter)+":" + str(tabcount) + " "+"parent switch=" + str(boomerang[0]) + "\n")
            holdinglist[0]=  str(counter)
            #I need to add this to the special dictionary now
            #put it into a list first
            sweetlist.append([counter,tabcount,boomerang[0]])
            counter += 1
        else:
            craftline += line + "\n"
            counter += 1
    #print("this is the output test revisiting this on November 2nd, Tuesday")
    #print(craftline)    
    #print('end of test......... monday morning blues ')  

#modify_string_before_splitting_it_up()

listinput=[]
#exit()




#
# we have 1,11 and 1,49  so two inner switches
#
# so it would be in main switch 1 and then 11,49
#

#print("I'm making this so only one tab difference")     
#print("sweetlist=",sweetlist)    




#print("and then the switches with no nests") 
#print("if number in second slot and not ever in first slot it's a single")

#need to figure out how to add these automatically
  

switchnumbers=[]
tabslist=[]
switchlinenumbers=[]
peach_data=[]



#at this point peach_data should already be filled
#testing determine what switches are parent-child by tab and sequence
# so 
#print("testing access of data after filling peach_data")
#peach_data[1]= ['1', '1', '1']
#peach_data[2]= ['2', '11', '3']
#peach_data[3]= ['3', '15', '5']
#peach_data[4]= ['4', '23', '7']

isnt_this_pretty='nada'
pattern_input=[]
pattern_input.append('0')
pattern_input.append('0') #[1] patterninput[1]
pattern_input.append('0') #[2] patterninput[2]

##============================
##  input_tab_combo(x,y):
##=============================
def input_tab_combo(x,y):
    #print("====== input_tab_combo(===", x, y)
    pattern_input[1]=x #5
    pattern_input[2]=y #7

porsche_carerra=[]
capture_switch_lines_nested=[]


plums=[]
plums_data=[]
endswitchlinenumbers=[]
endtabslist=[]


             



#this builds the pairs of switch endswitches by tabs since they ahve to be lined up
#from the switch down to the endswitch in the same tab depth 


 ##=====================this might be teh top of the methods ==========================================================
 ##===============================================================================
 
 
        
## loops thru tabsubs and appends item to tabcount
#=========================
#  little_method(tabcount)            
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

#used by the super duper function with 6 methods in it
#===============================

first=[]
add_tab_depth=[]
holding_themax=[]
holding_themax.append(0) #to create slot
christmastree=[]
second=[]   #this takes an inputstring which is the combined switchcase big string
slydog=[]
snowtime=[]
mylistinput=[]
#===========================
super_listinput=[]

def put(x):
    listinput.append(x)

#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  
    #print('=======METHOD 3 ====>>>')
    mx = holding_themax[0] #it's using this number 
    input= holding_themax[0]
    #cascading down is how it works
    if holding_themax[0] >= 3: put(3);
    if holding_themax[0] >= 5: put(5);
    if holding_themax[0] >= 7: put(7); 
    if holding_themax[0] >= 9: put(9); 
    if holding_themax[0] >= 11:put(11);
    if holding_themax[0] >= 13:put(13);
    if holding_themax[0] >= 15:put(15);
       
    for item in listinput:
        super_listinput.append(item)
    
  
  
##=================================
##  list_tabs_lists_by_depth():
##================================== 
def list_tabs_lists_by_depth():
    pass
    #print("==list tabs lists by depth=====METHOD 5======>>")
    #print("threetabs=" ,threetabs); print("fivetabs="  ,fivetabs);
    #print("seventabs=" ,seventabs); print("ninetabs="  ,ninetabs);
    #print("eleventabs=",eleventabs);print("thirteentabs=",thirteentabs) 
    


#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    #print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
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
    #print("tabsubs = ",tabsubs) #this can be increased to manage n number of tabs depth
    if   x == 3: little_method(threetabs)
    elif x == 5: little_method(fivetabs)
    elif x == 7: little_method(seventabs)
    elif x == 9: little_method(ninetabs)
    elif x == 11:little_method(eleventabs)
    elif x == 13:little_method(thirteentabs)
    else:
        pass
          







##==================================================
## make_switch_and_endswitch_pairs_by_tab_levels() 
##=================================================== 
def make_switch_and_endswitch_pairs_by_tab_levels(inputstring): 
    #print(":=============== METHOD 4 ======") 
    for item in super_listinput: # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)
     

###=============================== 
 
        #del tabsubs[:] #should clear it
###=================
rattabs=[]



##==============================
##  experimental_machinery
##===============================
def experimental_machinery(x,inputstring): 
    counter =0
    #newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    internal_machinery(x,inputstring)
 
    ###============

combined_tabs=[]
christmastree=[]




##============================================
## combine the lists together  #waterfall ifs
##=============================================
def combine_the_lists_together(x): 
    get_length_of_threetabs    = len(threetabs)
    get_length_of_fivetabs     = len(fivetabs)
    get_length_of_seventabs    = len(seventabs)
    get_length_of_ninetabs     = len(ninetabs)
    get_length_of_eleventabs   = len(eleventabs)
    get_length_of_thirteentabs = len(thirteentabs)
    #test if threetabs list is empty
    if get_length_of_threetabs > 0: #then proceed there is at least one
        #this is a waterfall extending numbers to add to christmastree list
        if x >=  3:christmastree.extend(threetabs);
        if x >=  5:christmastree.extend(fivetabs);  
        if x >=  7:christmastree.extend(seventabs);
        if x >=  9:christmastree.extend(ninetabs); 
        if x >= 11:christmastree.extend(eleventabs);
        if x >= 13:christmastree.extend(thirteentabs);
    
    else:
        pass
        #print('all of the tab lists are empty')
        #print("don't bother trying to extend empty tab lists")
       

##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    del christmastree[:] #clears out the combined_tabs list to erase it
    combine_the_lists_together(largest_tab_number) #<<==input is the largest tab number
    
    
 
#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    #print("======METHOD 6 ===  combine tabs by length into christmastree_list====>>>>")
    themax = holding_themax[0] #this gets the highest tab level (deeply nested)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    
   
#================================= 
#  build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    #print("=== METHOD 7== build pairs with jazz =======>>>>")
    #nuking snowtime here to bypass the problem
    #look in snowtime first to see what the hell is in it
    print("this is inside of build_pairs_with_jazz() inside of starship line 460")
    print("starship line 461 snowtime=",snowtime)
    del snowtime[:] #added this hopeful bug fix on january 2nd, 2022 10:38am
    #===================================================
    counter =0
    for x in christmastree: #loops thru at 2 at a time
        jazz = [christmastree[counter],christmastree[counter+1]]
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        #prevents overflow error for out of range error
        if counter >= len(christmastree):
            break
            
            
         
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    #print("build tab depth ==== METHOD 1 ==  build_tab_depth(=======>>")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")         #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth)    #this is for filling the list of each tab depth
        else:
            continue
    #print("add_tab_depth=",add_tab_depth)
    #print("max tab depth=",add_tab_depth[0])
            
      
      
            
            
def loop_thru_pairs_in_snowtime():
    #print(" ==== #method 8 ===  loop_thru_pairs_in_snowtime()=============")
    pass
    #for item in snowtime:  
        #print(item);
     #   rad1=item[0];rad2=item[1];
        #print(rad1,"and ",rad2)
    #print("snowtime list=",snowtime)




##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():  #this fills the max holding_themax[0]
     #print("======  #METHOD 2 ========")
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     #print("themax=",themax)


##===========================================================================================
##===========================================================================================
##===============================================================
##   ==this_makes_switch_and_endswitch_pairs_by_tab_levels() ====
##===============================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    #print("===THIS MAKES SWITCH AND ENDSWITCH PAIRS BY TAB LEVELS========")
    build_tab_depth(inputstring)                               #METHOD 1
    get_max_tab_number_in_list() #fills holding_themax[0]      #METHOD 2
    build_list_input_list()                                    #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels(inputstring) #METHOD 4
    list_tabs_lists_by_depth()                                 #METHOD 5
    combine_tabs_by_length_into_christmastree_list()           #METHOD 6 
    build_pairs_with_jazz()  #combines into sublist            #METHOD 7 
    loop_thru_pairs_in_snowtime()                              #METHOD 8
    #print("==bottom of this makes switch and endswitch pairs by tab levels()")
    print("this is at end of this_makes_switch_and_endswitch_pairs_by_tab_leves()")
    #print("snowtime=",snowtime)
    #this will go into gold_list
        
   
 
     #this gets one pair in showtime designated by x 
def get_pair_in_snowtime(x):
     #print(" get pair in snowtime testing",x)
     #what if I add 0,0 to first position brilliant
     if len(snowtime) == 0:
        pass #print("length of snowtime is zero")
     #print(snowtime) #would be second position
     cool = snowtime[x]
     #print("list at position ",x," is",cool)
 

 


######=================================
#maybe switch line numberYES will be used to access the pairs
#breakthru and use a dictioanry with switch id line number
# like 11 which is going to be the first number in the pair brilliant
############==================================================


param1=[]
param2=[]
param1.append(0)
param2.append(0)


##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]

peartree=[]
startime=[]

##======================================
## fill_main_pear_list(listname):  #this build the combined list correctly 
#the lists threetabs,fivetabs,seventabs,ninetabs need to already be filled
#this is just combining them together adding them together
##=====================================

threetabs=[]
endtabslist=[]
endswitchlinenumbers=[]


##======================
##  sound_of_music
##======================
fivetabs=[]



#=============bottom half which is seperates_input_strings============
#import official_switch_case_silver
#from official_switch_case_silver  import *  

def stop():
    print('stop called which calls exit')
    exit()
    
endswitch_location=[]
switch_location=[]
zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'
cat_scales=[]
cat_scales.append(0)
#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 
#make sure no space and it's switch(exp){
#first red robin here testing 


# output is to inputstring[0]
#############################################################
passinputstring=[]
smart_switch_numbers=[]
loopstring=[]
loopstring.append(0)
#twinlist=[]
passinputstring.append(0)  #get line number of switch and add number with comment to after all switches
snowman=[]
snowman.append(0)

##===================================================
##  add comment and lin number to all switches ()   ## put switch line number in
##===================================================
def add_comment_and_line_number_to_all_switches(inputstring): #this modifies the original string
	awesome='';counter =0;newstring='';
	for line in inputstring.splitlines():
		if "switch" in line and "end" not in line:
			# NEED TO HANDLE BOTH SCENARIOS switch with brace and switch without a brace 
			#############################################
			#switch is in this line definitely
			if "{" in line and "switch" in line and "end" not in line:
			### new surgery ===dec 20th monday bug fix out of the blue =======
				#if counter == 1: #modified for bu on dec 20th monday each number was off by 1 except first
				newstring += line.replace("switch(exp){","switch(exp){ #" + str(counter) + "\n")
				
			#this is necessary since the replace is quite specific and so no brace here
			# NOTE: I am adding gthe brace if it's missing to switch 
			if "{" not in line and "switch" in line and "end" not in line:
				newstring += line.replace("switch(exp)","switch(exp){ #" + str(counter) + "\n")  
			#end if  
			smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		####################################################
		elif "endswitch" in line: #just added comment number after endswitch 
			newstring += line.replace("endswitch","endswitch #" + str(counter) + "\n")
			#smart_switch_numbers.append(counter) #this is new september 30th, 2021
			counter += 1
		###################
		else:
			newstring += line + "\n"
			counter += 1
	awesome = newstring #it was concatted to newstring which we now reassign to awesome then red_robin
	return newstring #this way I can capture the changed string
##===================================================================================







import re
def first_letter(s):
    m = re.search(r'[a-z]', s, re.I)
    if m is not None:
        return m.start()
    return -1

s = "##catgiraffeapluscompscI"
i = first_letter(s)
print(i)


testthis='''
	switch(exp){
	    	case 1 thru 3:
		  	print("where\'s the dog house!")
			print('first prize')
	  		print('you block head Charlie Brown')
			fallthru
	  	case 4 to 7:
'''

coolinthegang='''
	switch(exp){
	    	case 1 thru 3:
		  	print("where\'s the dog house!")
			    print('first prize')
	  		   print('you block head Charlie Brown')
			fallthru
	  	case 4 to 7:
	    		    print('first prize')
	     		print('you block head Charlie Brown')
		         case 9 thru 11:
'''


    
        
#print('after ======= attempting lstrip() which I have no confidence in')



newlist=[]
newtime=''
thelist=[]
finaloutput=[]
finaloutput.append(0) #creates slot
'''
this cleans up input javascript code that is supposed to be 
governed by tabs in front ala Python and if a space is discovered
it is neutralized and deleted. 
This first counts the tabs in each line in the string.
second it cuts out all spaces and tabs from left of each line
then it concats a new string with the correct tab count in
front of each line so it's CLEANED UP essentially. 

'''
#bad input
examplestring='''
	      switch(exp){
	    	case 1 thru 3:
		  	print("where\'s the dog house!")
	  		    print('first prize')
	  		    print('you block head Charlie Brown')
			fallthru
	  	case 4 to 7:
	     		      print('first prize')
	     		print('you block head Charlie Brown')
		         case 9 thru 11:
'''
#cleaned up output becomes
'''
	switch(exp){
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
		case 4 to 7:
			print('first prize')
			print('you block head Charlie Brown')
		case 9 thru 11:
'''


finalstage=[]
finalstage.append(0)
##========================================
##  cut_out_left_side(inputstring):
##========================================
def cut_out_left_side(inputstring):
    print("cut out left side")
    fancy=''
    for line in inputstring.splitlines():
        #print(line)
        newline = line.lstrip() #I am using lstrip() look at that!!
        fancy += newline + "\n"
    finalstage[0] = fancy
    ## concatting tabs in front + line to redone


##========================================
##  concat_tabs_in_front(fancy):
##========================================
def concat_tabs_in_front(fancy):
    #print("conctat_tabs_in_front()")
    redone='';counter=0
    for line in fancy.splitlines():
        redone += newlist[counter] + line + "\n"
        counter += 1
        if counter >= len(newlist):#prevents out of range error
           break
    finaloutput[0]= redone
    #print("right here the OUTPUT =",finaloutput[0])


#==================================
#   append_result()  pure genius
#   #appends tabs to newlist
#=================================  
def append_result(x):
    tab = "\t"
    result = tab * x;
    newlist.append(result)  
    #this replaces: #if item == 1:result = tab * 1;newlist.append(result)


#puts tab count in each line into thelist
##===============================================================
## count_tabs_in_each_line_and_put_into_thelist(inputstring):
##===============================================================
def count_tabs_in_each_line_and_put_into_thelist(inputstring): 
    del thelist[:];del finaloutput[:];finaloutput.append(0) #creats one slot space
    for line in inputstring.splitlines():
        answer =line.count("\t") 
        thelist.append(answer)
 
#TEST STRINGS taking out junk spaces




smartlist=[]
thelist=[]
#thelist.append(do1)
#thelist.append(do2)
#thelist.append(do3)
#thelist.append(do4)
#thelist.append(do5)
#thelist.append(do6)

fixedstring=[]
fixedstring.append(0)

#================dec 25th, 2021==============
#   remove_spaces_before_words(inputstring):
#============================================
def remove_spaces_before_words(inputstring):
    buildstring=''
    for line in inputstring.splitlines():
        aline= line.lstrip(' ')#strips off left side spaces
        buildstring += aline + "\n"
    fixedstring[0] = buildstring
#=========================================================================
# take_out_extraneous_white_spaces_on_the_left_of_each_line():
#=========================================================================
def take_out_extraneous_white_spaces_on_the_left_of_each_line():
    #print(" == take_out_extraneous_white_spaces_on_the_left_of_each_line(): ==")
    #print("length of thelist=",len(thelist))
    for item in quail: #what am I calling the list 
        remove_spaces_before_words(item)             #method
        smartlist.append(fixedstring[0]) #adds output to new list
        #this fills up the list smartlist
    del quail[:]
    for item in smartlist: #now fill quail list 
        quail.append(item)
    #print("this is what is in quail list now")
    #for item in quail:
     #   print(item)
        #print("======")
#=========================================================================
# loop_thru_smartlist_after_adding_fixed_strings():
#=========================================================================
def loop_thru_smartlist_after_adding_fixed_strings():
    return 
    #for item in smartlist:
    #print(item)
        
def loop_thru_list_before_changes():
    print('what thelist looks like in starting mode')
    #for item in thelist:
    #   print(item)
    #print("=======end of strarting input strings ====")    
##===================================================================
#print("here we go with our christmas morning code to make this work") 
#just commented these out since it was here for purely testing purposes
#loop_thru_list_before_changes()      
#take_out_extraneous_white_spaces_on_the_left_of_each_line()
#loop_thru_smartlist_after_adding_fixed_strings()
#print("end of test to get rid of spaces on left side of precious code")  
##==========================================================================
##===========================================================================    

#exit()


             
#made into a function on saturday, dec 4th morgan hill starbucks 
# refactored on dec 19th for efficiency and management
##=======================================================
##  take_out_junk_spaces_from_left_side(inputstring):
##=======================================================
def take_out_junk_spaces_from_left_side(inputstring):
    #print("take out junk spaces from left side")
    #print(inputstring)
    count_tabs_in_each_line_and_put_into_thelist(inputstring) # METHOD
    for item in thelist:  #fill a list with tabs corresponding to numberof tabs numbers
        x = item;
        append_result(x)                                      # METHOD
        
    cut_out_left_side(inputstring)#puts fancy in finalstage[0]# METHOD
    fancy =finalstage[0]
    concat_tabs_in_front(fancy)                               # METHOD 
    #result in finaloutput[0] for one converted string cleaned up
#####################################################################
#print("here we go big time test..........fireworks...")

    

###========================================================================   

    
#check for position of first character or number in line 
    #check in this line for location of first letter  
    #letter =line.index('s')# or myString.index('c') or myString.index('p') or myString.index('f')
    #print("letter is",letter)
    #no spacesin switch at top so it skips it!!!~!
    #I need the word before
    
    #what if I go thru the line and 
    #first detect a space and proceed till I hit a character
    #so I am only dealing with spaces before the characters
    #and I create a new line modified 





##===================================== border line ======================================








def empty_switch_and_endswitch_list_locations():
    #print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations    #this fills the together_pair list
##########################################
switch_location=[]
endswitch_location=[]
together_pair=[]






#print("done with test to get the nested switch locations within the big switch")

### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
switch_list=[]

#print(genius[0])    	


 ####### august 10th 2021 testing commences.
 
find_nested_switch_game ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
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

gameday ='''
			switch(exp){   #1 === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					switch() #7
						case 'funny':
							print('fun')
						case "da":
							print('yeah')
						default:
							print('bye')
					endswitch #14
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #this is key here =============line 20 end of nested switch ====
'''	

#print("what we are starting with the switch with a nested switch")
#print(find_nested_switch_game)
#print("=====================")
#oh wait this needs to be the input C style switch that I search in
#maybe I need to go through the case list palmtrees
# so get line number of switches
#get linenumber of each case to determine which case section the inner switch is in
pacman=[]
pacman.append(0)


coollist=[]
#print("this gets the line number of the line that the case starts")
#print("that has the nested switch inside THIS Case")

endnestedswitchline=[]
endnestedswitchline.append(0)
#########################################
##  get_case_line_numbers(string_name):
#########################################
def get_case_line_numbers(string_name):
    linecounter =0
    casecounter = 0
   # print('get line number of each case section')
    #just get first case line numbers print it
    for line in find_nested_switch_game.splitlines(): #be sure to put stringname.splitliens()
        #this looks for cases
        if "case" in line:  #grabs first line
            #print(line)
            pacman.append(linecounter)
            casecounter += 1
            linecounter += 1
            #print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
        #if "switch" in line:
   # print("case line numbers",pacman)    
    #print(pacman[2])  
    #print("number less than 10 that ")
    #I reverse the list order to find the first case less than 10 the line with switch in it
    pacman.reverse()

#calls method above
#####==========
#get_case_line_numbers(find_nested_switch_game)
#####========


#####################################
## get_larger_number_less_than_case()
#####################################
def get_larger_number_less_than_case():
    #this gets teh larger number less tahn the case
    for item in pacman:
        if item < 10: #I will need to put  (this cuts the possibilities to those less than 10)
            coollist.append(item)
            #print(item)
            #print("this must be the answer of the case that is on line 8")
            break #so after just the first one
    #get largest number in list
    #print("this is new trying to get largest number only from list")
    superman = max(coollist) #worked June 28th MOnday 2021
    #print("largest number =",superman)

#calls method above
#######========
#get_larger_number_less_than_case()
#######========




###$############===================-----0-0--=-=-=-=-=-=0-0-0-9=0--
### GET END OF SWITCH LINE  number
#######################################
## now looking for end of nested switch case
#june 28th, 2021
#####################################
## get_end_of_switch_line_number():  #  this gets endswitch line number
#####################################
def get_end_of_switch_line_number():
    linecounter=0 #this looks for the line number of endswitch for the nested switch
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "endswitch" in line:  #grabs first line
           #print("we have a match")
            #print(line)
            #linecounter += 1 if it's endswitch don't add one
            #print(linecounter)
            endnestedswitchline[0]=str(linecounter)
            break
        else: #this looks for the  switch word
            linecounter += 1   
            continue
    #print("the end of this nested switchis",endnestedswitchline[0])
    #print("====should be 18 ====")

#calling method above this 
#####=========
#get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
#####=========

#and we know that the case number is 8
#and we know that the nested switch starts on line 10
#therefore we subtract 10-8 = 2
#so within the case the nestedswitchmethod will be on line 10 or the 2nd line within the case
###############=======================########################
#print("copy inner switch")
#first trying to copy the inner switch and put it into a list

linecounter=0 #this looks for the line number of endswitch for the nested switch
#print("testing getting a copy of nested switch")
### what I need to do is grab the numbers that I generated that I am using below
### I determine the line number that the first and only nested switch is on
### I then look for the first "endswitch" after the nested switch starts
### and it must be within the bounds of the case that it is residing within.
#here I am feeding it but I need to make it a method
#x = 11;
#y = 60;
#start  = 11  #hard coded beginning of nested switch
#finish = 60 
start_and_finish=[]


##============================================
##  inputs_pair_to_copy_a_string()
##============================================
def inputs_pair_to_copy_a_string(start,finish):
    #print("inputs pair to copy a string")
    del start_and_finish[:] #this clears it out initializing it
    start_and_finish.append(0) 
    start_and_finish.append(start) #position [1]
    start_and_finish.append(finish) #position [2]
    #start_and_finish[1] = x
    #start_and_finish[2] = y
    #print("x=",start_and_finish[1])
    #print("y=",start_and_finish[2])
    
########################################################################
 #hard coded end of single nested switch 
## COPY A NESTED SWITCH
############################

#so we have

#############################
r=find_nested_switch_game #thats the name of a string fin_nested_switch_came
#linecounter=0
makeitwork=[]
makeitwork.append(0)
## function copy a nested switch()   ==== I just put this into a function



columbia_river=[]
gold_list=[]
###############################
## copy_a_nested_switch(r):   # what this does is copy one nested switch 
###############################
def copy_a_nested_switch(r):  #copy just one nested string 
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    answer=start_and_finish[1]
    start_and_finish[1] = start_and_finish[1] - 1 #added this on dec 20th to show switch word
    #print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
    for line in r.splitlines(): #if linecounter is between start and finish
    #this should copy a full (every line) of a nested switch from switch to and including endswitch
        # if lincounter >= 10 and linecounter <= 20; #this is what it means
        if linecounter >= int(start_and_finish[1]) and linecounter <= int(start_and_finish[2]):
            innerswitch += line + "\n"  #it's concatted to innerswitch string right here
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    #print(":the result COPY OF NESTED SWITCH  ")        
    #print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner #result of copied string goes in makeitwork[0]

################################################################################

#I need to fill this list (populate it from get switch engineswitch pairs
#print("testing looping thru gold_list")
#gold_list=[[1,100],[11,60],[15,51],[23,46],[31,41],[62,86],[66,77]]
################################################################################
#print("=======begin Sunday Morning Brew Testing==========================")

def show_switch_string_with_numbers_added_after_each_switch_with_a_comment(water):
    pass  #not printing it out at this time on purpose
    #for line in water.splitlines():
    #    print(line)

def show_the_snowtime_list_of_pairs():
    print("starship line 1436 snowtime=",snowtime)   
    
def empty_columbia_river_list():
    del columbia_river[:] 
    
def add_main_switch_to_columbia_river(water):
    columbia_river.append(water)  

    
holding_string=[]
holding_string.append(0) 

##============================================================================
##  loop_thru_snowtime_list_copy_switch_bodies_and_add_to_columbia_river():
##============================================================================   
def loop_thru_snowtime_list_and_copy_switch_bodies_and_add_to_columbia_river():
    for item in snowtime:#was gold_list #loop that gets switch,endswitch pair from goldlist
        num1 = item[0];
        num2 = item[1];
        inputs_pair_to_copy_a_string(num1,num2) # get input string from goldlist
        copy_a_nested_switch(holding_string[0]) # copy string based on switch,endswitch pair 
                                                # puts resulting string into makeitwork[0] and output
        output = makeitwork[0]                  # put nested string into columbia_river list
        columbia_river.append(output)
    #print("length of columbia river =",len(columbia_river))
    #counter =1  #adding here the initial string which will be used to make the main switch


    
##=================================  
## loop_thru_columbia_river() 
##================================= 
def loop_thru_columbia_river():
    #print("now loop thru ====== COLUMBIA RIVER === to see the switch bodies seperated")
    counter =1
    return
    #for item in columbia_river:   #it is added just before looping thru i
    #    print("counter=",counter)
    #    print(item);
    #   #print("===========");
    #    counter += 1    
    
          

#gold_list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]    

##==============================================

   #This takes in what has already split the mega nested switch into 
   #switch bodies
quail=[]
sfo_pairs=[]
gold_list=[] #dec 26th sunday 7:56 am
##======================================================##=========================================
##  ==split_up_big_string_into_nested_switches(myinputstring)==
##======================================================##=========================================
def split_up_big_string_into_nested_switches(myinputstring):#this would only be called once
    #print(" ==  split_up_big_string_into_nested_switches(inputstring)  ==")
    water =add_comment_and_line_number_to_all_switches(myinputstring)               #METHOD 1
    show_switch_string_with_numbers_added_after_each_switch_with_a_comment(water)   #METHOD 2
    empty_columbia_river_list()                                                     #METHOD 3
    show_the_snowtime_list_of_pairs()                                               #METHOD 4
    add_main_switch_to_columbia_river(water)                                        #METHOD 5
    holding_string[0] = water
    loop_thru_snowtime_list_and_copy_switch_bodies_and_add_to_columbia_river()      #METHOD 6
    loop_thru_columbia_river() #prints out seperated switch bodies top down         #METHOD 7               
    #print("snowtime pairs=",snowtime)
   # print("fill the list sfo_pairs with snowtime list in case I need it")
   #gold_list is filled from snowtime RIGHT HERE
   ##3===================
    for item in snowtime:
        sfo_pairs.append(item)
        gold_list.append(item) #fills gold_list too
        
    #print("looping thru columbia river to fill quail list")
    for item in columbia_river:
        quail.append(item)
        #fills up quail list 
    
    ##==============
   # print("the switch strings cut up are now printed out top down")
    take_out_extraneous_white_spaces_on_the_left_of_each_line()
    #print("looping thru quail list to see what it has")
    #for item in quail:
    #    print(item)
    #   print('=====')
    #print(snowtime)
##================================================================        
##================================================================

##=================================================================
## manage_creating_pairs_and_separating_input_switch_strings()
## this calls 2 methods  ---------------
## * this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)
## * split_up_big_string_into_nested_switches(inputstring)
##=================================================================
def manage_creating_pairs_and_separating_input_switch_strings(inputstring):
    #print(" manage_creating_pairs_and_separating_input_switch_strings(inputstring) ")
    #empty both critical lists here 
    del columbia_river[:]
    del snowtime[:]
    #print("called manage_creating_pairs_and_separating_input_switch_strings()")
    this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)
    split_up_big_string_into_nested_switches(inputstring)
    #that's it

#print("this is where it all starts... make pairs and separate the switch strings")
#inputstring = red_robin
#manage_creating_pairs_and_separating_input_switch_strings(inputstring)


#print('testing booster2 here')
#waterfall_chain_methods_gold_master()



#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########
#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########

holdthis=[]
holdthis.append(0)

#this swaps endswitch with }
######################################
## take_out_endswitch(stringname)  #from bottom of nested switch 
######################################
def take_out_myendswitch(stringname):
	#print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			#print("detected } in line")
			#location = line.index("#")    #gets location from left where position of #
			#line = line[:location] 
			#print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			#print("after left shift it is ",line)
			#line[0] = first #this is new to slice off right of brace
			line = line[0]#first char
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	#print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():
	#    print(line)
	    
	##===========today sunday coding
	
	#then look for this } and reposition it
	
	#this is what I need to modify.
	#so the whole modified string after ripping out endswitch is now in holdthis[0]
	
	#print(holdthis[0])
	galaxy = holdthis[0] #now galaxy gets what is in holdthis[0]
	return galaxy #and this is returned
##========================================================================
##  def next_metamorphosis_take_out_inner_switch(stringname,switch_number):
##=========================================================================
baton=[]
baton.append(0) #this creates the first slot 0
start=''
finish=''
string_name=''
switch_tab_depth=''
#stringname=bigstringtest1
#this gets the endswitch line number that we need
#then I will call skip rope to finish the cutting out of the inner switch case


input_to_get_inner_switch=[]
string_after_cutting_out_inner_switch_body=[]
string_after_cutting_out_inner_switch_body.append(0)

hp=[]
hp.append(0)
lightning=[]
lightning.append(0)




innerswitchstatus=[]
innerswitchstatus.append(0)

castle1=[]
castle1.append(0)
##===================================================
## change_switch_to_method_solved(inputstring):
##====================================================
#print("make the coffee magic coding happen working on this today charlie brown") 
#solved and working on October 30th 2021 ====================================
def change_switch_to_method_solved(inputstring):
    innerswitchstatus[0]= False #by default
    #print("====== change_switch_to_method_solved(inputstring)=== get the money now====")
    #print('this now takes out the { brace after switch if it is there')
    innerswitch=''
   # print("this is what it sees when it starts change_switch_to_method_solved()")
    #for line in inputstring.splitlines():
    #    print(line)
    #print("========testing if this input string has a nested switch ==")
    innerswitch= False #default setting
    counter=0;newstring='';y='';x='';tabdepth=''; switches_total=''
    #verify that there is at LEAST ONE nested switch in here
    for line in inputstring.splitlines(): # we only need to detect one inner switch
       tabdepth = line.count("\t") #gets tab count for this line
       if "switch" in line and "end" not in line and tabdepth == 3:  #it just needs to be true once
       #this means yes there is a nested switch in this string
            innerswitchstatus[0]= True #this is new 
            innerswitch = True
            break
       else:
            innerswitch = False
            continue
    if innerswitch == False:
        pass
        #print("this switch string DOESN'T HAVE an inner switch")
    ##########################################
    #print("innerswitch =",innerswitch)
    ##### modified on halloween  2021 to bypass if no inner switch ##########################################               
    templine=''
    templine2=''
    
    #### IF INNERSWITCH == TRUE:
    if innerswitch == True: #if a switch at 3 tabs depth  is True
    #check if { in this string if so take it out
        #print('checking if left brace in string')
        if "{" in inputstring: #have to cut "{" out of string
            #print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine  +=   line.replace("{","") 
                    templine  +="\n"
                else:
                    templine += line +"\n"
            inputstring = templine
        #end if
       # print("=======testing if { taken out of string=======")
        #for line in inputstring.splitlines():
        #    print(line)
        #print("=======testing if { taken out of string=======")
       #check if } in this string an if so take it out
      
        counter=0 #new counter for this loop different from upper for loop above
        for line in inputstring.splitlines():#      getting tab depth
            tabdepth = line.count("\t") #gets tab count for this line
            #skips first switch by counter MUST BE AFTER 2nd line
            #this is where we swap switch(exp) with nested_switch_(number)(exp)
            if "switch" in line and tabdepth == 3 and "end" not in line and counter > 2: 
               # print("confirmed switchh in line and tabdepth3")
                #this is new getting the switch id number after # on-the-fly
                #get string to right of #, get right side,remove spaces
                x = line.split("#"); y = x[1];y = y.strip();
                # replace switch with nested_switch + id number harvested from comment above
                thisline = line.replace("switch(exp)", "nested_switch_" + str(y) + "(exp)")
                #this removes the extra spaces after #
                location = thisline.index("#")    #gets location from left where position of #
                thisline = thisline[:location]    #this slices off the right side from # position
                thisline = thisline + "#" + str(y) #this concats on the # and comment id number
                counter += 1; newstring += thisline + "\n"; continue
            else:
                newstring += line + "\n"; counter += 1; continue
        return newstring  
        ##################################################################
    else: #this MEANS NO INNER SWITCH IN THE INPUT STRING
        #print("no inner switches in this string")
        if "{" in inputstring: #have to cut "{" out of string
            #print("CONFIRMED there is a left brace in string")
            for line in inputstring.splitlines():
                if "{" in line:
                    templine += line.replace("{","") #taking out left brace here
                    templine  +="\n"
                else:
                    templine += line +"\n"           #otherwise it doesn't replace anything 
            inputstring = templine
        else:
            pass# print("=====no { in string  ======")
            #end if
        #print("=======testing if { taken out of string=======")
        #for line in inputstring.splitlines():
        #    print(line)
        #print("=======testing if { taken out of string=======")
        #check if } in this string an if so take it out #I have deactivated this since it's not needed
        
        #this is what we return the inputstring
        return inputstring; #no changes made 
        castle1[0] =inputstring 
        innerswitchstatus[0] = False
    ### end of function =======================================================
    
#print("where is my mocha brainfreeze test october 30th...")





#global concatthis;
	#this just might work 
	#this is a flag to pass the existing concatted string to be used fresh for next switch
	#this list is preset at False 
	#so this starts out false and passes thru it and then the list which used to have
	#FAlse in it has a string in it thereafter and the modified string from first pass
	#and subsequent passes is the new string to modify on the fly
	
#this requires the string name and start and finish to work
#this takes one nested switch with start and finish locations
#this method must be given start and finish in the params
#this prints out the new string after cutting out the nested switch except for the switch word
##===========================================================
## skip_rope_skipping_some_lines()  this cuts out ONE inner switch body
##===========================================================
def skip_rope_skipping_some_lines(string_name,start,finish):#start line nest switch and finish  endswitch
	#print("start= ",start,"finish= ",finish)
	if string_after_cutting_out_inner_switch_body[0] == False: #starting
		pass #print("it is False it is  empty ")
	else: 
		string_name = string_after_cutting_out_inner_switch_body[0]
		#print('it is NOT False and therefore we fill the string from the list[0]')
	concatthis=''
	#print("===skip_rope_skipping_some_lines(string_name,start,finish)====")
	#string_after_cutting_out_inner_switch_body[0]
	#print(string_name)
	counter=0; #concatthis =''; #finish = finish + 1 
	#switch is the start line though we are skipping after it and keeping it
	#the start line is the switch which will be preserved but skipping when cutting out
	#print("string_name=",string_name,"start=",start,"finish=",finish)
	for line in string_name.splitlines(): 
		if counter > start  and counter <= finish: 
			#print(line) #it won't print the switch word since it's skipping it
			counter += 1; continue
		else: 
			concatthis += line + "\n"; counter += 1; continue
	#print('it created this SILLY STRING === multi colored silly string=')
	#print(concatthis)
	#print("I would put this into a list to store for later")
	string_after_cutting_out_inner_switch_body[0] = concatthis
	weasel=string_after_cutting_out_inner_switch_body[0]
	#for line in weasel.splitlines():
	#	print(line)
	#return weasel  #I need to return from each for the piping to work correctly
	lightning[0] = concatthis
	#for line in lightning[0].splitlines():
	#    print(line)



def modern_take_out_endswitch(inputstring):
	#print("take_out_endswitch called=============")
	galaxy = stringname
	#print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	##================================
	#what this does is take off the comment after }
	#and then it shifts } to the far left against the margin with no spaces
	
	buildnewstring=''
	for line in holdthis[0].splitlines():
		if "}" in line:
			#print("detected } in line")
			location = line.index("#")    #gets location from left where position of #
			line = line[:location] 
			#print("resulting line looks like this",line)
			line = line.lstrip() #this should move it to the far left to align with margin
			#print("after left shift it is ",line)
			buildnewstring += line + "\n";
		else:
			buildnewstring += line + "\n";
	#end loop
	holdthis[0] = buildnewstring
	#print("this is the final outpout of take out endswitch")
	#for line in holdthis[0].splitlines():




testlist_of_strings=[]

fillherup=[]
holdon=[]
holdon.append(0)
holdthis=[]
holdthis.append(0)
galaxy=''




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
	print("let us look in this string and see what we can see")
	for line in the_nest_string.splitlines():
		print(line)
	#===========================================	
	tabdepth='';n=''
	for line in the_nest_string.splitlines(): #nest_string
		if "switch" in line and "end" not in line: #means a switch line
			tabdepth = line.count("\t")
			print('====================================================')
			print("tabdepth detect in starter_engine =",tabdepth)
			print('====================================================')
			n= tabdepth;n = n-1  #need to have one tab in front
			#note tabdepth n needs to be at least 1
			# I may make it default at 1 to run otherwise it fails
			#================================
			if tabdepth < 1:
				passthis[0] = 1; #as a potential bug fix
			else:
				break
			#end if =====================================
			break #no matter what it will break out of this loop 
	passthis[0]= n;
	#print("n =",n)
goldtime=[]
goldtime.append(0)
##===================================================================
##  modern_tab_shifter_to_left(the_nest_string):  nov 30th tested working
###==================================================================
def modern_tab_shifter_to_left(the_nest_string):
    #print("====modern tab shifter to left=======")
    starter_engine(the_nest_string)  #method call to get tabdepth on first switch line
    buildstring='';
    print("what is in passthis[0] =",passthis[0])
    print('this is inside of modern_tab_shifter_to_left(the_nest_string)')
    n = passthis[0] #filled from starter_engine method number of tabs in front of switch
    print("inside of modern tab shifter to left we have this for n")
    print("n=",n)
    print(type(n))
    print("what is it??")
    print("what is in the line above")
    ### n is number of tabs in front of switch BEFORE CHANGING IT
    if n == 0: #means one(1) tab in front of switch do nothing
        buildstring =the_nest_string #no changes to indentation
    if n > 1: #more than one tab in front of switch so cut some tabs out
        for line in the_nest_string.splitlines():
            buildstring += line[n:] +'\n' #this cuts out n tabs from the front of this line
    goldtime[0] = buildstring
    #print("output of concatted string in goldtime[0]")
    #for line in buildstring.splitlines():
    #    print(line)
### deposit now code here for take out switch body to function properly   
 

###========================================================================
## convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
###=========================================================================
def convert_switch_with_more_than_one_inner_switch_at_3_tabs(stringname):
    string_after_cutting_out_inner_switch_body[0]= False        #necessary default flag 
    counter=0 #where am I filling inputlist?
    for item in inputlist: #this grabs the params from item     #list of switches pairs start stop at 3 tabs depth
        start = item[0];
        finish = item[1];
        #print('start=',start,'','finish=',finish)                       #62; finish=86 
        skip_rope_skipping_some_lines(stringname,start,finish)  #this copies the string skipping the range designated
        counter +=1
       # print("counter=>>",counter)
       # print("=====================")
    #print("at bottom of converts  with more than one inner switch at 3 tabs")
    #print("testing if weasel is returnable at the end of the function")
     #this is after it's done
    #for line in weasel.splitlines():
    #    print(line)
    #return weasel 

	
#print("I am fillilng the inputlist right here manually force feeding it.")
#this calls it but right now I want to know where I fill th einputlist
inputlist =[]
inputlist.append([11,60])
inputlist.append([62,86])
#print(inputlist)
inputlist.reverse() #reversing the list since the cutting out must be done bottom up to work properly

#print("after reversing the list we now have===")
#print(inputlist)
#print("convert switch with more than one inner switch at 3 tabs(stringname)==== string1")
#get_switch_and_endswitch_locations_in_string(test_string1) #presumes one inner switch 


#get_switch_and_endswitch_locations_in_string(test_string1) #for this switch string
#print('we have switch_list=',switch_list)
#print("endswitch_list=",endswitch_list)
#it needs to make these [[11, 60], [62, 86]]
###testing nov 27th at 10:46am starbucks




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
	#print("====||||  get switch and endswitch locations in string  ||||======")
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
	#print("total switch at 3 tabs in this string",len(total_switches_at_3tabs_depth))
	#print("they start on these lines",total_switches_at_3tabs_depth)
	#count_switches_at_threetabs= string_name.count("
	counter=0; concatthis =''; #finish = finish + 1 
	#print("string_name=",string_name)
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
	#print("phase 2 here ====")
	counter=0; concatthis =''; #finish = finish + 1 
	#print("string_name=",string_name)
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
	#print("switch_list=",switch_list)
	#print("endswitch_list=",endswitch_list)
	#print("end of line...")
	########################======
	
	########################==========
#print("calling get switch and endswitch locations (only one set) in string ")
#this needs to be done first ===== before calling the function

#print("should be 1 for this test")
#del switch_list[:]
#del endswitch_list[:]
#print('real test now i really need this puppy to work')




#print('important testing on Saturday morning')
trialinputlist=[]
inputlist =[]

#made nov 27th, satgurday 4:15pm morgan hill starbucks 
##===========================
## build_trail_inputlist()
##===========================

def build_trial_inputlist(): #this combines switch and endswitch into pair into trialinputlist
	print("===inside of build_triall_inputlist==inside of starship ==")
	del inputlist[:] #this empties the input list discarding previous data in it
	del trialinputlist[:]
	#print("build_trail_inputlist()..")
	#print(" coding blues ")
	##==================================================================
	pair=''
	print("len of switch_list", len(switch_list))
	print("len of endswitch_list", len(endswitch_list))
	counter=0; 
	print('starting out what is length otrailinputlist')
	print("it's length = ", trialinputlist)
	print(trialinputlist) #should be empty 
	for item in switch_list:
		print("switch list counter=",switch_list[counter])
		print("endswitch list counter=",endswitch_list[counter])
		print('================')
		pair=[switch_list[counter],endswitch_list[counter]]
		print("pair=",pair)
		trialinputlist.append(pair)
		counter += 1
	pair='' #clear out pair which is just a mere variable not a list
	print("var pair=",pair)
	##=========================================================================	
	#print("look for the ball on the green")
	print("reaching the 18th hole on the green")
	print("trialinputlist=",trialinputlist)
	for item in trialinputlist:
		inputlist.append(item) #this is putting what is in trailinputlist into inputlist
	print(":============ look right here for what is different =====")	
	print("inputlist=",inputlist)
	for item in inputlist:
		print(item)
	inputlist.reverse() #is this needed here or not 

	 
  
  

#inputstring=test_string1
outputstring=[]
outputstring.append(0)
snowboarding=[]
##=================================
## take_out_switch_body(astring):  #def foxnews(astring):
##================================
def take_out_switch_body(astring): #this was foxnews
	nestedswitch= False
	#print("take_out_switch_body      today is november 28th sunday  4:29 pm ")
	#right here look if a switch at 3 tabs if not skip below
	####=== new as of monday december 6th, 2021 =========================
	#determine if 
	for line in astring.splitlines():
		tabcount =line.count("\t")
		if "switch" in line and tabcount == 3:
			#print("yes switch at 3 tabs in line")
			#print("frosty says switch at 3 tabs confirmed")
			nestedswitch= True
			break
	#print("frosty the snow man light test for nested switch")
	#print("nestedswitch=",nestedswitch)
	#print("==================================")
	if nestedswitch == False: #what this does is put the input string into output
		#add input into output  this means no changes were done to the switch string
		#print("this switch string DOES NOT have an inner switch")
		lightning[0]=astring 
	else:
	##======= this is down here now ========december 6th 2022 =========
		get_switch_and_endswitch_locations_in_string(astring) #for this switch string
		build_trial_inputlist()	 #this is new 
		convert_switch_with_more_than_one_inner_switch_at_3_tabs(astring)
	#end if
	##########================================================================
	 
	snowboarding.append(lightning[0])  #this is new dec 6th monday
	#for line in lightning[0].splitlines():
	#	print(line)







#making this sucker work no matter what 

#print("the big test begins")
#planB()
#print("now simply loop thru the finished changes in the list")

#### stage 1 test ###############
#each fruit method will do the list of 7 input strings stop
#these are the REAL CHAIN METHODS AS OF DEC 11 SATURDAY 2021 8:10 AM ====
result_of_first_method=[]
result_of_second_method=[]
result_of_third_method=[]
result_of_fourth_method=[]

#print("this is after the input stings have already been seperated")
##=================================
##  move_string_to_left_side()        first method modern tab shifter to left 
##=================================


##================================================================
## what is different is that the data strings are in quail above and are fed into testlist_of_strings
##================================================================
#
# this is using testlist_of_strings as input
#output: result_of_first_method all switch strings modified
def move_string_to_left_side():
    #empty testlist of strings and refill with fillherup
    del testlist_of_strings[:]
    ##=======================================
    ## using quail to hold the strings so I would use this here 
    for item in quail: #gets input strings from fillherup list
        testlist_of_strings.append(item)
    #print("==== passing the baton here =============/////=============")
    #print("verifying that testlist_of_strings has the switch strings from above at this juncture")    
    #for item in testlist_of_strings:
    #    print(item)
    #   print("===========")
        
  
# modern_tab_shifter_to_left  method used
    #print("=====APPLE== modern_tab_shifter_to_left()=====")
    counter = 1
    for item in testlist_of_strings:
        #print("=======")
        modern_tab_shifter_to_left(item)
        fizz=goldtime[0] #output from first_method()
        #print("apple stage1 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_first_method.append(fizz)
        #print("===== counter =",counter)
        counter += 1
    ################################################    
    counter =1
    #print("result of shifting input strings to left")
    #print("=====APPLE==APPLE   APPLE   APPLE   APPLE   APPLE=====")
    #for item in result_of_first_method:
        #print(item)
        #print("=========")
        #print("counter=",counter)
    #    counter += 1
    




##======================================================
## take_out_the_inner_switch_bodies_leaving_switch()
# output result_of_second_method
# method used: take_out_switch_body(string)  PLUM
##======================================================
def take_out_the_inner_switch_bodies_leaving_switch():
    #print("=====PLUM == take_out_switch_body(item)====")
    #take_out_switch_body method used
    counter = 1
    for item in result_of_first_method:
        take_out_switch_body(item)
        #print("===== counter =",counter)
        counter += 1
        fizz =lightning[0]
        #print("plum stage2 fizz =",fizz)
        #append outpoutto result_of_first_method
        result_of_second_method.append(fizz)
    ###################################################
    counter =1
    #print("result of taking out inner switch bodies")
    #for item in result_of_second_method:
        #print(item)
        #print("=========")
        #print("counter=",counter)
     #   counter += 1
    

#good_plum()





##===================================================================
## good_peach()  change_switch_to_method_solved : switch to nested_switchX(exp) # 
## output: result_of_third_method  PEACH
##=================================================================
def change_switch_to_nested_switch_method(): #swaps switch with nested_switch method
    #print("=====PEACH===change_switch_to_method_solved===")
    # change_switch_to_method_solved method used 
    counter = 1
    for item in result_of_second_method:
        fizz=change_switch_to_method_solved(item)
        #print("peach fizz=",fizz)
        #append outputto result_of_first_method
        result_of_third_method.append(fizz)
        #print("===== counter =",counter)
        counter += 1
    #########################################
    counter =1
    #print('result of 3rd method on string')
    #for item in result_of_third_method:
        #print(item)
        #print("=========")
        #print("counter=",counter)
     #   counter += 1
    
    
    
##===================================================================
## replace_endswitch_with_close_brace     take_out_endswitch() 
## output: result_of_fourth_method  ORANGE
##=================================================================
def replace_endswitch_with_close_brace(): #orange
    # take_out_myendswitch method used 
    #print("=======ORANGE=take_out_myendswitch===")
    counter = 1
    for item in result_of_third_method:
        take_out_myendswitch(item)  #other one is take_out_endswitch
        #print("=======")
        fizz =  holdthis[0]
        
        result_of_fourth_method.append(fizz) #this fills up result_of_fourth
        #print("===== counter =",counter)
        counter += 1
   #########################################
    #print('result of 4th method on string')
    counter=1
    #for item in result_of_fourth_method:
        #print(item)
        #print("=========")
        #print("counter=",counter)
    #  counter += 1


#######################################################

    
#this gets the numbers and fills up the list switch_numbers_to_transfer  
switch_numbers_to_transfer=[]
cell=[]
cell.append(0)
##==================================== created dec 6th monday 2021
##  get_switch_number_now(lestring): from quail list before bypass205 is called
##====================================
def get_switch_number_now(lestring): #fills list switch_numbers_to_transfer
    #print("====get_switch_number_now()=====") #gets it from quail list
    counter =0
    for line in lestring.splitlines():
        if  counter == 1 and "switch" in line and "#" in line and "end" not in line:
             x =line.index("#");
             x=x+1;
             answer=line[x:];
             cell[0]=answer;
             switch_numbers_to_transfer.append(answer) #fills up this list
             break;
        else:
             counter +=1
    
    
            
#this fills up the switch_numbers_to_tranfer list used in bypass205 to
#use in the numbering of the switches with a # after each
##====================================================
##  fill_switch_numbers_list_to_transfer():
##  method: get_switch_number_now()
##==================================================  
def fill_switch_numbers_list_to_transfer():
    for item in result_of_fourth_method:
         get_switch_number_now(item) #fills list switch_numbers_to_transfer
    counter=1
    for item in result_of_fourth_method:
        counter += 1
 


#print("=========== get switch numbmer in quail list") 
##=============================================
## get the switch_numbers_to_transfer():
#this is trapeze to get the switch number for first switch in each string
#which will be used for make the def nested_switch and main_switch in python mode
##=============================================
def get_the_switch_numbers_to_transfer():
    counter=1
    for item in chain_output_list:
        get_switch_number_now(item) 
        #print("number =",counter)
        #print(cell[0]) 
        counter += 1          
    print("switch_numbers_to_transfer",switch_numbers_to_transfer)
  



  
chain_output_list=[]
##===================================================
## fill_chain_output_list():
##==-================================================
def fill_chain_output_list():
    del chain_output_list[:] #empty it to be sure
    #print("====fill chain output list()====")
    print("this fills the chain_output_list from result_of_four_method list")
    for item in result_of_fourth_method:
        #print(item)  #just don't print it out
        chain_output_list.append(item)

##======================================================
## loop_thru_chain_output_list_and_fill_quail_list()
##======================================================          
def loop_thru_chain_output_list_and_fill_quail_list():
    #print("loop thru chain output list nad fill quail list()")
    del quail[:] #empties quail list
    for item in chain_output_list:
        quail.append(item)


##======================================================
## loop_thru_quail_list():
##===================================    
def loop_thru_quail_list():
    #return
    for item in quail:
        print(item) 
        
def loop_thru_chain_output_list():
    return
    print("== chain_output_list looping thru it to feed to parser in bypass==")
    for item in chain_output_list:
        print(item)
        print("=====================")
        
def fill_output_into_quail_list():
    for item in chain_output_list:
        quail.append(item)
    #print("final output from chain methods for input switch strings")
    #print("note: this is the quail list with these modified switch strings")
    #for item in quail:
    #    print(item)
    #    print("=============")
##=============================================
## show_list_switch_numbers_to_transfer()
##=============================================
def show_list_switch_numbers_to_transfer():
    return #print("===switch numbers to transfer== stage2 Linus==")
    #print(switch_numbers_to_transfer)  
#fillherup=[]
##====================================
##  do_the_blender_chain_methods()
##====================================
radical_list=[]
def do_the_blender_chain_methods():
    print("do blender chain methods()")
    #print('this should print out strings in testlist_of_strings')
    for item in testlist_of_strings:
       print(item) #here   it said (line) why?
    
    move_string_to_left_side()                         # method 1 indents to left
    take_out_the_inner_switch_bodies_leaving_switch()  # method 2 cut out switch bodies leaving switch
    change_switch_to_nested_switch_method()            # method 3 switch becomes nested_switchX
    replace_endswitch_with_close_brace()               # method 4 endswitch becomes }
    fill_switch_numbers_list_to_transfer()             # method 5 list generated used for codegen
    fill_chain_output_list()  
    #loop_thru_quail_list()
    #loop_thru_chain_output_list() #final output to send to rudolph parser now      
    #now I need to put what is in chain_output_list into quail list
    del quail[:]
    fill_output_into_quail_list() #final stage here 
    for item in quail:
        radical_list.append(item)
    print("==radical_list==")
    for item in radical_list:
        print(item)
        
##  waterfall_chain_methods_gold_master()  formally called do_it()  #this is the one actually being used.
## uses testlist_of_strings for input
##==================================================
#the way this works is each method does all of the switch strings as a set
#each of these methods does all of the switch strings in the list at once 
#and the results are passed downward cascading for the next method to modify.
#========WATERFALL CHAIN METHODS GOLD MASTER THE REAL DEAL=======
##===================================================================================    
## ====  WATERFALL CHAIN METHODS GOLD MASTER OFFICIAL OFFICIAL OFFICAL OFFICIAL  =====       
##  fills quail list with converted and prepped input switch strings all clean up
## this is called after the strings have been separated from the main nested switch

##=====================================================================================
def waterfall_chain_methods_gold_master():  #THIS WILL TAKE IN THE QUAIL LIST FOR INPUT
    #print("===WATERFALL CHAIN METHODS Gold Master 1.3()===  REAL WORLD = ")
    do_the_blender_chain_methods()
    loop_thru_chain_output_list_and_fill_quail_list() #yeah makes sense filling quail list
    show_list_switch_numbers_to_transfer()
 
   ##====================== jan 2nd new =====================
   # to see what are in the lists after ONE RUN of starship booster 1 and booster 2
   #=========================================================
#new january 2nd, 2022 
def show_contents_of_all_lists():
    return
    print("====show contents of all lists() inside of starship module ===")
    #if the lists are full in here I need to reset and clear them all
    print("quail=",quail)
    print("radical_list=",radical_list)
    print("testlist_of_strings=",testlist_of_strings)
    print("switch_numbers_to_transfer=",switch_numbers_to_transfer)
    print("chain_output_list=",chain_output_list)
    print("result_of_fourth_method=",result_of_fourth_method)
    print("cell=",cell)
    print("result_of_third_method=",result_of_third_method)
    print("result_of_second_method=",result_of_second_method)
    print("result_of_first_method=",result_of_first_method)
    #print("tabcount=",tabcount) #will have to clear it too likely 
    print("snowboarding",snowboarding)
    print("outputstring",outputstring)
    print('endswitch_list=',endswitch_list)
    print("string_name=",string_name)
    print("fillherup=",fillherup)
    print("holdon=",holdon)
    print("holdthis=",holdthis)
    print("galaxy=",galaxy)

def empty_the_contents_of_all_lists_inside_of_starship():
    #print("===resetting the lists in starship===")
    #print("empty_the_contents_of_all_lists_inside_of_starhip CALLED")
    #print("which means to essentially RESET() the lists in it")
    #print("after deleting them emptying them I will show their contents for proof")
    #print("first empty the said lists ")
    del quail[:]
    del radical_list[:]
    del testlist_of_strings[:]
    del switch_numbers_to_transfer[:]
    del snowtime[:]
    del chain_output_list[:]
    del result_of_fourth_method[:]
    del cell[:]
    del result_of_third_method[:]
    del result_of_second_method[:]
    del result_of_first_method[:]
    del snowboarding[:]
    del outputstring[:]
    del endswitch_list[:]
    del switch_list[:] #just added this one in case  jan 2nd to fix bug 
    #del string_name[:]
    del fillherup[:]
    del holdon[:]
    del holdthis[:]
    #=============== this one was getting overloaded
    del snowtime[:] #this is new just added it
    del sfo_pairs[:]
    del gold_list[:]
    del columbia_river[:]

    #del build_trial_inputlist[:]
   
    #del stanford[:]
    #del galaxy[:]
    ##==========================================
    '''
    print("now show me the empty lists")
    print("quail=",quail)
    #print("stanford=",stanford)
    print("radical_list=", radical_list)
    print("testlist_of_strings=", testlist_of_strings)
    print("switch_numbers_to_transfer=", switch_numbers_to_transfer)
    print("chain_output_list=", chain_output_list)
    print("result_of_fourth_method=", result_of_fourth_method)
    print(" cell=", cell)
    print(" result_of_third_method=", result_of_third_method)
    print("result_of_second_method=", result_of_second_method)
    print("result_of_first_method=", result_of_first_method)
    print("snowboarding=", snowboarding)
    print(" outputstring=", outputstring)
    print(" switch_list=", switch_list)
    print(" endswitch_list=", endswitch_list)
    print("string_name=", string_name)
    print("fillherup=", fillherup)
    print(" holdon=", holdon)
    print("holdthis=", holdthis)
    print("galaxy=", galaxy)
    '''
##===========================================================================
##  convert_nested_switch_string_to_strings_in_quail_list(inputstring):
##============================================================================
def convert_nested_switch_string_to_strings_in_quail_list(inputstring):
    manage_creating_pairs_and_separating_input_switch_strings(inputstring)
    waterfall_chain_methods_gold_master() 
    print("####### ** ==starship lists contents == ##################")
    print("out of pure curiosity showing the contents inside of Starship module")
    show_contents_of_all_lists() #new january 2nd, 2022========>>>>>>>
    print("end of showing contents of starship lists and variables")
    print("####### ** ==starship lists contents == ##################")
    
    
    
    
#inputstring = red_robin
#convert_nested_switch_string_to_strings_in_quail_list(inputstring)

#print("=======end of test inside of startship=====")
#exit()

def so_smart():
    print("------------------------------------")
    print("======== so_smart() called==========")
    print("------------------------------------")
    print("switch_numbers_to_transfer=",switch_numbers_to_transfer)
    print("snowtime=",snowtime)
    #print("thenumbers=",thenumbers)
    print("switch_list =",switch_list)
    print("endswitch_list=",endswitch_list) 
    print("testlist_of_strings=",testlist_of_strings)
    del switch_numbers_to_transfer[:]
    del snowtime[:]
    #del thenumbers[:]
    del switch_list[:]
    del endswitch_list[:]
    del testlist_of_strings[:]
    print('and the result is now after deleting them')
    print("switch_numbers_to_transfer=",switch_numbers_to_transfer)
    print("snowtime=",snowtime)
    #print("thenumbers=",thenumbers)
    print("switch_list=",switch_list)
    print("endswitch_list=",endswitch_list)
    print("testlist_of_strings=",testlist_of_strings)











