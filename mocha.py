import trex  
from trex  import * 

import official_switch_case_silver
from official_switch_case_silver  import *  

### experimental moved this into mocha 
import snowflake
from snowflake import *
from snowflake import weasel


#import preprocessor_exps
#from preprocessor_exps import *

switch_location=''
the_exps= False
'''
get location of first switch by line number in the string

check if exp in line before first switch

'''





status_of_exps=[]
status_of_exps.append(0)
##=================================================
## look_in_mystring_for_exps_at_top(mystring):
##=================================================
def look_in_mystring_for_exps_at_top(mystring):
	the_exps=False
	switch_location=''
	print("look in mystring for exps at top(mystring)")
	counter =0
	#or get line number with first switch in line
	print('stage 1  look for exps at top')
	for line in mystring.splitlines():
		#print(line)
		if "switch" in line:
			switch_location= counter
			break
		else:
			counter += 1
	print("switch_location=",switch_location)
	counter =0
	#determine if exp in line before first switch_location
	print('stage 2 look for exps before first switch')
	for line in mystring.splitlines():
		#print(line)
		if counter != switch_location:
			if "exp=" in line or "exp =" in line:
				print(line)
				the_exps = True
				break
			else:
				counter += 1
	print("the result of this jazz is the_exps=",the_exps)
	status_of_exps[0] = the_exps




##==============================
##  two_choices(mystring)
##==============================
'''
this does the two modes single switch and nested switch 

'''
def two_choices(mystring):
	#determines here if mystring is a nested switch or not 
	nested =count_switches_in_inputstring(mystring)  #method  count_switches_in_inputstring(mystring)
	#assert nested == True, "nested != True"
	if nested == True:
		print('nested is true===========::::')
	else:
		print('nested is false==========::::')
	##=========================
	if nested == True:
		print("nested is obviously TRUE this is necessary at this phase")
		look_in_mystring_for_exps_at_top(mystring)   #method look_in_mystring_for_exps_at_top(mystring)
		#print("status of the_exps=",status_of_exps[0])
		if status_of_exps[0] == True:      #means at least one exp= above first switch
			#this is then called to redistribute the exps below ONLY if they were at top
			mystring=prepare_my_string(mystring)    
		else:
			pass
		
		###########################################################
		smart_endswitch(mystring) #was (mystring)  #nested switch is in trex
	else:
		cool_endswitch(mystring)   #single switch is in official_switch_case_silver
	


###========= endswitch(string)===========
def endswitch(mystring):
    two_choices(mystring) #calls two_choices just above this method
    
    
    
    
    
    
    
    
    
    
    