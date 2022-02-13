import trex  
from trex  import * 

import official_switch_case_silver
from official_switch_case_silver  import *  


def two_choices(mystring):
	print("two_choices called ")
	nested =count_switches_in_inputstring(mystring)
	if nested == True:
		smart_endswitch(mystring)  #nested switch
	else:
		cool_endswitch(mystring)   #single switch
	


