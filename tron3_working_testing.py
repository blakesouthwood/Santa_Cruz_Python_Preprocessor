#tron3
 
# 9:27am Starbucks Gilroy software engineering
delorean=[]
delorean.append(0)
##======testing importing a list from snoopy_doghouse=======================================
#from snoopy_doghouse import test_list
#print('testing in tron3 to see if the list was returned from snoopy_doghouse file')
#print("testlist=",test_list)
#print(test_list[0])

#the issue is getting the list 


##this is from what was just generated== but slightly modified ======
## dec 17th friday
#there is no ''' at the top... interesting actually it is there 
#was nested_switches=

#output string to give it a name to reference it but the name is not in
civicsi='''
def nested_switch_66(exp):	
	exp = varholder[0]
	
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
	exp = varholder[0]
	
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("do something")
			####################
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
	exp = varholder[0]
	
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("do something")
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
	exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
		####################
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
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("we made it to nested switch 15 tahoe here we come")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nice")
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
	#exp = varholder[0]  #hav eto comment this one out 
	
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("Now we are in nested switch 11")
			####################
			exp = 'Tahoe'
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
def main_switch(exp):	
	exp = varholder[0]
	
	caselist1 = ['1', '2', '3']
	caselist2 = ['4', '5', '6', '7']
	caselist3 = ['8', '9', '10']
	caselist4 = ['default']
	
	
	switch(exp)#1
	while True:
	
		if case in caselist1: # ['1', '2', '3']
			print("oh my god this was real generated code!")
			print('first prize')
			print('you block head Charlie Brown kick the football')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			#############
			exp = 'blable'
			nested_switch_11(exp) #11
			exp = 3
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	
'''


nested_switches='''
def nested_switch_66(exp):	
	#exp = varholder[0]
	
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
	exp = varholder[0]
	
	caselist1 = ['burger']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#62
	while True:
	
		if case in caselist1: # ['burger']
			print("more in nested_switch_62")
			####################
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
	
	caselist1 = ['fishy']
	caselist2 = ['where now']
	caselist3 = ['default']
	
	
	inswitch(exp)#31
	while True:
	
		if case in caselist1: # ['fishy']
			print("made it to nested switch 31")
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

exp = 'fallen leaf lake'	
def nested_switch_23(exp):	
	#exp = varholder[0]
	
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#23
	while True:
	
		if case in caselist1: # ['tahoe']
			print("do something")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("nested switch 23 we made it to fallen leaf lake")
		####################
			exp = 'fishy'
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
	exp = 'fallen leaf lake'
	caselist1 = ['tahoe']
	caselist2 = ['fallen leaf lake']
	caselist3 = ['default']
	
	
	inswitch(exp)#15
	while True:
	
		if case in caselist1: # ['tahoe']
			print("now in nested_switch15 oh nice ")
			print("yep")
			infallthru('fallen leaf lake')
	
		elif case in caselist2: # ['fallen leaf lake']
			print("in nested switch 15 now ")
			####################
			exp = 'fallen leaf lake'
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
	exp = 'blable'
	caselist1 = ['blable']
	caselist2 = ['more']
	caselist3 = ['default']
	
	
	inswitch(exp)#11
	while True:
	
		if case in caselist1: # ['blable']
			print("we are now in nested_switch11 with blable")
			exp = 'tahoe'
			####################
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
def main_switch(exp):	
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
			print('you block head Charlie Brown')
			infallthru('4')
	
		elif case in caselist2: # ['4', '5', '6', '7']
			print('kangaroo hop hop!')
			print("how much more of this is there, all in Norweigen")
			#############
			exp = 'blable'
			nested_switch_11(exp) #11
			exp = 'more'
			nested_switch_62(exp) #62
			##############
			print('taught me how thru write code')
			infallthru('8')
	
		elif case in caselist3: # ['8', '9', '10']
			print('mocha blast')
			print('== 31 flavors===')
			infallthru('default')
	
		elif case in caselist4: # ['default']
			print('the end')
			break
	
		else:
			print('the end')
			break
	
'''
#testing on friday dec 17th generated combined nested switches 
#putting into fill_nested_switches_list[0]
fill_nested_switches_list=[]
fill_nested_switches_list.append(0)
fill_nested_switches_list[0]=nested_switches #generated string from red_nosed_deer.py
#line 41269 create_def_switch_methods_concatted_together_in_one_string()
#print('looping thru nested_switches now .. this is getting a bit weird')
print('testing seeing what is in list now after(was before) putting it into variable')
for line in fill_nested_switches_list[0].splitlines():
    print(line)
    
future_nested_switches =fill_nested_switches_list[0]#harded coded above for testing

#delorean[0]=testinput    
    
    
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

#nestswitches= delorean[0] #this is holding the input string generated switch methods
#it's one big string

#test it with varholder[0] = '1' for first test 


#simulating moving the generated string around inside of a list 
#fill_nested_switches_list[0]= testinput

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
print("inside tron3 testing outpout of concatting strings dec 15th ")

print("=====are we almost there yet======")
print('print fill_nested_switches_list I just imported')

    
show_code= True    
#concat_items_in_list(x)
#using list since that way I can pass it from elsewhere where it's generated
#the only thing that changes is fill_nested_switches_list[0]
###==================================
##  concat_items_in_list(x):
##===================================
def concat_items_in_list(x): #add_to_list added at top before this as input
	print('--------concat items in list(x)---------------------------')
	#print(len(fill_nested_switches_list[0]))
	
	print("concat_items_in_list() called with input x",x)
	print('---------------------------------------------')
	enter_value(x) #this is fed in from above 
	print("=====concat items in list()====")
	fireone[0]= True #when this is True it shows the code generated with print
	#fill_nested_switches_list[0]=input_nested_strings
	
	#print("length of list in question is",len(fill_nested_switches_list[0]))
	global superball
	#the only actual input is fill_nested_switches_list[0]
	nested_switches=''
	nested_switches=fill_nested_switches_list[0]
	#print("what the hell is in here??")
	#print(nested_switches)
	#maybe str(fill_nested_switches_list[0])
	#future_nested_switches= civicsi #testing generated output that would be in a list
	print(method_defs)
	print(future_nested_switches)
	print(trigger)
	
	#nest put this code here concat items in list at bottom of red_nosed_deer
	#===========================================================================
	superball =  method_defs + future_nested_switches + trigger + "\n"
	#===========================================================================
	if show_code == True:
		print(superball) #prints the generated switch code methods
	else:
		pass  #otherwise it prints nothing 
	#so at this juncture the global var superball has the combined stacked string


###=============================
### clever_cat()  triggers the concatting and executing of the python
### calls method: concat_items_in_list() filling superball and then executes it
###=============================
def clever_cat():
    print("====clever_cat called===")
    ### ==== executed here
    concat_items_in_list(topvalue[0])#this builds the concatted string superball
    print('input is ',varholder[0])
    #===========================
    exec(superball, globals()) #runs the switchcase
    #===========================
##################################

##=====================================
topvalue[0]='1'
clever_cat()
##======================================================================

#print("input varholder[0]=",varholder[0])
print('result[0] =',result[0])


