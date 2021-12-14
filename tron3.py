#tron3
 
# 9:27am Starbucks Gilroy software engineering
delorean=[]
delorean.append(0)

testinput='''
def nested_switch_66(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 66==",exp)
	caselist1 = ['fishy']
	caselist2 = ['snow fire']
	caselist3 = ['default']
	
	
	inswitch(exp)#66
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
			print("yep")
			infallthru('snow fire')
	
		elif case in caselist2: # ['snow fire']
			print("nice")
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_62(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 62==",exp)
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
			exp = 'fishy'
			nested_switch_66(exp) #66
			#############
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
	
def nested_switch_31(exp):	
	#exp = varholder[0]
	print("==NESTED SWITCH 31==",exp)
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("INSIDE CASE 1 OF NESTED SWITCH 31")
			print("yep")
			infallthru('where now')
	
		elif case in caselist2: # ['where now']
			print("nice")
			break
	
		elif case in caselist3: # ['default']
			print("we very done")
			break
	
		else:
			print("we very done")
			break
	
	
def nested_switch_23(exp):	
	#exp = varholder[0]
	print(" ==NESTED SWITCH 23rd== ",exp)
	caselist1 = ['tahoe']
	caselist2 = ['cold water']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['cold water']
			print("nice")
		####################
			exp='fishy'
			nested_switch_31(exp) #31
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_15(exp):	
	#exp = varholder[0]
	print("==NEST SWITCH 15==",exp)
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("rafted down Truckee River Once.")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice mocha in the morning")
			print(" kayaking at Fallen Leaf Lake")
			exp = 'cold water'
			####################
			nested_switch_23(exp) #23
			#############
			break
	
		elif case in caselist3: # ['default']
			print("we are done here")
			break
	
		else:
			print("we are done here")
			break
	
def nested_switch_11(exp):	
	#exp = varholder[0]
	print("=== NEST SWITCH 11==",exp)
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("do something yes Tahoe ski trip")
			####################
			exp = 'tahoe'
			nested_switch_15(exp) #15
			#############
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
	

exp = varholder[0]
print("it sees for exp",exp)
def main_switch(exp):	
	print("===MAIN SWITCH==",exp)
	#exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("where's the dog house!")
			print('first prize')
			print('you are so smart  Charlie Brown a genius')
			result[0] ="Charlie Brown football kicker"
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#break
			#############
			exp = "blable"
			nested_switch_11(exp) #11
			print("just added this inbetween two nested switches")
			print('it will come thru here anyways and flow down')
			exp = 'burger'
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			result[0] ="31 flavors mint chocolate chip"
			break
			#infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	
'''

delorean[0]=testinput    
    
    
##=====================    
add_to_list=[]
fill_nested_switches_list=[]
fill_nested_switches_list.append(0)

topvalue=[]
topvalue.append(0)
 #testing putting it here for INPUT to the dynamically generated switch case

#put this string into a list with just the string by itself in position 0
method_defs='''
# =======  switch  =================================
def switch(x):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	x = str(x)
	global case
	case = x.lower() 
# =======  fallthru       =========================
def fallthru(y):
	eval("switch('" + y + "')")
#==================
#for inswitch
def inswitch(n):
	#if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
	#	n = str(n)
	global case
	case = n.lower() 
#=====================
# for infallthru    
def infallthru(n):
	eval("inswitch('" + n + "')")
'''





#add_to_list[0]
 #this remains unchanged and is a default string
#default necessary at top of all of these 
# this one will always be the same

result=[]
result.append(0)

#############################################
#this would come from a list and I need to 
# add the def nested_switch_1(n) at the top and indent the formatting
# to it before it makes it to the play_testing mode
#so then I would merely add the strings of each neseted switch
#to add_to_list

#######======================================
#this nest needs to be changed in the input list stanford after reversed
# and def nested siwtch added at the top and the whole thing indented

varholder=[]
varholder.append(0)

nestswitches= delorean[0] #this is holding the input string generated switch methods
#it's one big string

#test it with varholder[0] = '1' for first test 


#simulating moving the generated string around inside of a list 
fill_nested_switches_list[0]= nestswitches

#the difference is x input for main_switch(x)
trigger='''\n
main_switch(varholder[0]) 
'''

#add_to_list[4]


# the number of nested lists is unknown can be figured out

#this is always first in the list
#add_to_list.append(method_defs)
#add_to_list.append(nestswitches) #variable number of these


#add_to_list[3]

## this concats together the nested switches and the main switch
## with the main switch at the end (last)
## this is a simulation for the end result which will be more simplified
# july 12th, 2021 testing at starbucks in gilroy
#superball=''
alltheway=[]
# this concats the strings in the list and then executes the string code
fireone=[]
fireone.append(0)
fireone[0] = False
##########################################################################
def enter_value(x):
    varholder[0]=str(x)  #look at this it takes in the input 

x = topvalue[0];


    
    
#concat_items_in_list(x)
def concat_items_in_list(x): #add_to_list added at top before this as input
	print('---------------------------------------------')
	print("concat_items_in_list() called with input x",x)
	print('---------------------------------------------')
	enter_value(x) #this is fed in from above 
	print("=====concat items in list()====")
	fireone[0]= True
	global superball
	#the only actual input is fill_nested_switches_list[0]
	##============================================================
	#using list since that way I can pass it from elsewhere where it's generated
	#the only thing that changes is fill_nesetd_switches_list[0]
	superball =  method_defs + fill_nested_switches_list[0] + trigger +"\n"
	print(superball) 
	#varholder[0]= '1' #input into the main 
	#exec(superball)
	
###=============================
### clever_cat() triggers the concatting and executing of the python
###=============================
def clever_cat():
    print("====clever_cat called===")
    ### ==== executed here
    concat_items_in_list(topvalue[0])#this builds the concatted string superball
    print('input is ',varholder[0])
    exec(superball, globals()) #runs the switchcase
##################################


##=====================================
#topvalue[0]='1'
#clever_cat()
##======================================================================
#Error message I got from python compiler
#TypeError: exec() globals must be a dict, not str (safety tip)

#print("input varholder[0]=",varholder[0])
print('result[0] =',result[0])


