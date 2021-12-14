#import official_switch_case_silver
#from official_switch_case_silver  import *  

zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'
def message_from_Woodstock():
    print('hello from Woodstock the bird file')
    
message_from_Woodstock()

print("from the web trying this out")

quail=[]
# I am adding the quail list to practice filling it

endswitch_location=[]
switch_location=[]

def empty_switch_and_endswitch_list_locations():
    print("=== empty_switch_and_endswitch_list_locations()")
    del endswitch_location[:]
    del switch_location[:]
    
#get linenumbers of switches and endswitches ignore the first switch though actually doesn't matter
##########################################
#### get switch and endswitch locations 
##########################################
def get_switch_and_endswitch_locations(z): #from string z input parameter
	print("### must work now ###get switch and endswitch locations########")
	print("####3##get switch and endswitch locations########")
	#this empties switch and endswitch lists
	empty_switch_and_endswitch_list_locations()
	print("=====get_switch_and_endswitch_locations(z) called ....")
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
		#right here going thru input string look for switch and endswitch
		#and append the line number to either switch_location or endswitch_location
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
			
			
			#THIS DELETES THE FIRST SWITCH WHICH WE DON'T USE
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
	
#print("testing getting switch and endswitch locations")
#get_switch_and_endswitch_locations(red_robin)	
#exit()
	
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
print('changing line 3')
str_list[3] = "my new line value"
string = "\n".join(str_list)
print(string)

print("end of test from the web")
print("=========")
#this simulates after cutting out the inner switches but leaves the first line
#which is used for replacement of the nested method()
############################################################
########## august 5th testing what to use now #################=========$$$$$$$$$$$
############################################################
# this represents and input string with inner switches cut out
#what remains is just the switch word which will be replaced
old_coolstring='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   #here        representings stripped out inner nest
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
			switch(exp){     #here    # represents already stripped out inner nest 
			fallthru

		default:
			print('the end')
}
'''

#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 
mocha_nested_switchtest ='''
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


#so after striping out nested switches at all levels or is it just one deep 
#actually no the first time I need all of them 
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
			switch(exp){  
				case 'blable':
					print("do something")
					####################
					switch(exp){ # 15  #second level deep          Level 2    
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){ #23  #third level deep   Level 3    
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
							#############
							break
						default:
							print("we are done here")
					endswitch #38
					#############
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #47
			exp = 3
			switch(exp){ #49 #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){  #53  second level deep          Level 2    
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
			endswitch #73

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



# october 11th, 2021 
#testing texas here to do what I want
texas='''
	switch(exp){ 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){    first level deep                   Level 1
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
							switch(exp){   #third level deep   Level 3    
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
			switch(exp){ #first level deep                   Level 1
				case 'burger':
					print("do something")
					####################
					switch(exp){   second level deep          Level 2    
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
print("TEXAS TEXAS TEXASbig horn test===")
print("this adds line numbers to switch and makes a list of nested switch combos")
print('quick test adding line numbers to switch and endswitch')

sweetlist=[]
holdinglist=[]; holdinglist.append(0) #to create slot 0
boomerang=[];   boomerang.append(0)
#def get_switch_parents()

print("modifying red_robin string as texas to add comment of switch linenumbers and capturing")
print("the nested switches within it at each juncture too.")
print('testing TEXAS TEXAS TEXAS ====')
# I need to do a second pass and modify this just modified 
# texas string to show it's inner switch line numbers

##============================================
##  modify_string_before_splitting_it_up():
##============================================
def modify_string_before_splitting_it_up():
   
    print("texas string first")
    for line in texas.splitlines():
        print(line)
    print("=========================") 
    counter =0    
    print("modify_string_before_splitting_it_up():")
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
    print("this is the output test revisiting this on November 2nd, Tuesday")
    print(craftline)    
    print('end of test......... monday morning blues ')  

modify_string_before_splitting_it_up()

listinput=[]

## think if I have a switch at 3 tabs 
'''
[1][1,1]
[3][1,11]
[5][11,15]
[7][15,23]
[23]
[3][1,49]
[5][49,53]
[53]



'''
print("===================")
print("line #, Tabs, parent sw")
for item in sweetlist:
    print(item)
print('------------')
dunkapple=[]
#dunkapple.append(0) #leave empty
for item in sweetlist:
    print(item)#0,1,2   this line, tabs, parent(previous switch)
    print("accessing each one with control now")
    print(item[0]) #11
    print(item[1]) # 3 tabs 
    print(item[2]) # 1 
    super=[item[2],item[0]]
    print(super)
    print("==============")
    icetea=[item[2],item[0]]#1,11
    dunkapple.append(icetea)
#I am doing the opposite.
print("I need to have what nested switch is inside of a switch")
    
#go thru sweet list make list pairs for the parent and it's children
print("looping thru correct order now===== time for pumpkins")
for item in dunkapple:
    print(item)
    print(item[0],item[1])
#output
'''
I need to have what nested switch is inside of a switch
looping thru correct order now
['1', 1]
['1', 11]
['11', 15]
['15', 23]
['1', 49]
['49', 53]
I'm making this so only one tab difference
sweetlist= [[1, 1, '1'], [11, 3, '1'], [15, 5, '11'], [23, 7, '15'], [49, 3, '1'], [53, 5, '49']]
now we have list in dunkapple parent switch and it's nests
[['1', 1], ['1', 11], ['11', 15], ['15', 23], ['1', 49], ['49', 53]]
looping thru dunkapple........
we have ['1', 1]
1 1
nope not there yet
we have ['1', 11]
1 11
nope not there yet
we have ['11', 15]
11 15
nope not there yet
we have ['15', 23]
15 23
nope not there yet
we have ['1', 49]
1 49
nope not there yet
we have ['49', 53]
49 53
'''

#
# we have 1,11 and 1,49  so two inner switches
#
# so it would be in main switch 1 and then 11,49
#

print("I'm making this so only one tab difference")     
print("sweetlist=",sweetlist)    
#here is september 18th saturday coding candy
print("now we have list in dunkapple parent switch and it's nests")
print(dunkapple)
print('looping thru dunkapple........')
counter=0
ghostlist=[]
for item in dunkapple:
    print("we have",item)
    print(item[0],item[1]) # I could fill a new list with all of item[0]and test if number in list
    ghostlist.append(item[0])
    if item[0] == '23': #this looks for 15
        print("small victory")
        test = True
    else:
        print('nope not there yet')
        test = False
        
    counter += 1
    if counter >= len(dunkapple):
        break
    else:
        continue
        
        #now see if there is more than one nested switch like in 1
        
        
# I would skip the first item in the list 1, 1,1 it's useless and unnecessary 
print('new test if numbers in this first item list of pair')
if '23' in ghostlist:
    print("yes 23 in there in ghostlist")
else:
    print("nope not in there")
    
if '53' in ghostlist:
    print("yes 53 in there in ghostlist")
else:
    print("nope not in there")

if '49' in ghostlist:
    print("yes 49 in there in ghostlist")
else:
    print("nope not in there")            
print("dunking for apples")
print('test if 23 in item[0]=',test)

#for item in dunkapple:
#    print(item,counter)
 #   #fun = split.item
 #   counter += 1
        

counter =0
'''
going thru
['1', 1]
['1', 11]
['11', 15]
['15', 23]
['1', 49]
['49', 53]
looking for 23 in first slot on left
'''


print("and then the switches with no nests") 
print("if number in second slot and not ever in first slot it's a single")

#need to figure out how to add these automatically
print([23])
print([53])   
print('===== youtube time =====')
switchnumbers=[]
tabslist=[]
switchlinenumbers=[]
peach_data=[]

'''
peach_data[1]= ['1', '1', '1']
peach_data[2]= ['2', '11', '3']
peach_data[3]= ['3', '15', '5']
peach_data[4]= ['4', '23', '7']
'''

#at this point peach_data should already be filled
#testing determine what switches are parent-child by tab and sequence
# so 
print("testing access of data after filling peach_data")
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
    print("====== input_tab_combo(===", x, y)
    pattern_input[1]=x #5
    pattern_input[2]=y #7

porsche_carerra=[]
capture_switch_lines_nested=[]

##============================
##  access_row_in_peach_data(x)  #after it's already filled 
####==========================        
def access_row_in_peach_data(x): #return what has 3 :5 pattern of tabs
     print("access_row_in_peach_data",x)
     print("................................")
     print("................................")
     
     print("access row in peach data() called")
     print("====....= why are they remaking Twister movie ===...===......=====....===000055555======")
     print("input param =",x)
     #if peach_data[2][2] == '3':
     counter =0
     print("let us look and see what is in peach_data")
     for item in peach_data:
         print(item)
     #so by design the switch number is the same for first slot
     get_length= len(peach_data)
     print("the length of peach_data =", get_length)
     print("=======")
     #now accessing already filled matrix
     #loop thru peach_data and flag peach_data[number][x] and [x + 1]
     # so compare 2 at a time initially if x == 3 and x + 1 = 5
     #this looks for a 3 5 pattern in peach_data
     print('testing a comparision for 3 5 pattern')
     print("about to do boolean logic check for 3 and 5 pattern")
     print('the machine sees')
     
     #test if sequence ===========================================
     #x = 2
     #these are numbered numerically down so this is obvious
     #print("simple sequence test in peach_data")
     #if peach_data[x][0] == '2' and peach_data[x+1][0] == '3':
     #   print(peach_data[x][0])    # x=2
     #   print(peach_data[x +1][0]) # x=3
     #else:
     #   print("what it didn't work")
     #print("=== ending simple sequence test ===")
     print("tryin gto avoid this mess")
     #print(isnt_this_pretty)
     
     print('starting with x for loop thru peach_data',x)
     # loop 
     x = 1 #hard coded as 1 for now
     #this is a loop here 
     for item in peach_data:
        print("these determines if reaching end of peach_data list and bails")
        ###======= this ends the loop if x = get_length or get_length-1 =======
        print('value of input x now is..',x)
        #this is to break out of the peach_data loop for fail safe
        ###############################################
        # this is safety to jump out of loop to avoid out of range error 
        if x == get_length or x == get_length-1: #so it's not hard coded with 4
            print("bailing reached end of peach_data list")
            break  ##<< === break here to bail from loop 
        else:
            print("===========")
            print("everything is still good to proceed")
            print("===========")
            pass
        
        print("=============")
        #to find the 3 5 pattern of tabs comparing 
        print('this is new monday, sept 20th, 2021 testing so I can change the input vars')
        
        print('practice')
        #needto return the switch line number 
        print(pattern_input[1])
        print(pattern_input[2])
        print('end of putting data into list for juggling on the fly')
        #=====hard coded test =======================================
        #if it searching starting from peach_data[2] which is the 2nd switch
        print("first comparision =", peach_data[x][2])
        print(" second comparision =",peach_data[x +1][2])
        print('for this if the x input =',x)
        print("================================") #do I need to do 3,5,3 or just 3,5
        #if peach_data[x][2] == 3 and peach_data[x =1][2] == 5:
        #del capture_switch_lines_nested[:] #this was inside loop here now for testing
        
        if peach_data[x][2] == pattern_input[1] and peach_data[x +1][2] == pattern_input[2]:
            print("THIS WORKED using pattern_input[1] and pattern_input[2]")
            print(" PORSCHE time and Tahoe castle")
            print("yes a 3:5 pattern found")
            #then return their line numbers
            #x = 2 in this example tryin to retrieve 11,15 line numbers
            print(peach_data[x][1] + " " + peach_data[x + 1][1])
            alpha1 = peach_data[x][1]; alpha2= peach_data[x +1][1]
            print("these should be the line numbers 11 and 15 how we manage and track switches")
            print("so we have ", alpha1, "and ",alpha2)
            ### print this is new 
            porsche_carerra.append([alpha1,alpha2])
            #del capture_switch_lines_nested[:]  # comemnted out to see what happens
            capture_switch_lines_nested.append([alpha1,alpha2])
            print("what do we see here...the switch line numbers for 3, 5")
            print(capture_switch_lines_nested[0]) ##======
            badass = capture_switch_lines_nested[0]
            print('the name of the list of switch lines parent and child')
            print("capture_switch_lines_nested[0]",capture_switch_lines_nested)
            
            print("testing this.")
            print("right here line 457 we have ", capture_switch_lines_nested)
            print("let it be right")
            #copy contents for later
            #coolwhip =capture_switch_lines_nested[0] 
            #smart_rat.append(coolwhip)
            #print("smart_rat has ..",smart_rat)
            #print(smart_rat)
            #then take out duplicates
            
            
            #for item in capture_switch_lines_nested:
            #    smart_rat.append(item)
            
            one = badass[0]
            two = badass[1]
            #print("one=",one)
            #print("two=",two)
            print("end of this bunny show")
            print("what is in smart_rat list")
            print(smart_rat)
            print(":.........")
            x += 1
            print("x here is",x)
            print("get_length of data of peach_data=",get_length)
        else:
            print("no joy")
            x += 1  #adding 1 to input x bottom of loop
            
     print("here we have ",capture_switch_lines_nested) 
     print("above this should be 2 lists 2 sets of numbers")
     #this fills smart_rat with the item sfrom capture switch lines nested
     for item in capture_switch_lines_nested: 
        smart_rat.append(item)
     print("gold medal time finally...")
     print(smart_rat) 
     counter =0
     for item in smart_rat:
        print(item)
        a1 = item[0]
        a2 = item[1]
        print(a1)
        print(a2)
     print(":==============")
   
     #if pattern 3:5 and sequence is a, b= a + 1
     #   get line numbers peach_data[2][1]
     #   peach_data[3][1]
##============================
##  look for 3 5 pattern()
##============================    
def look_for_3_5_pattern():  #result 11,15 and  49,53
    print("===== look for 3 5 pattern ===")
    input_tab_combo('3','5')
    print("look for 3 5 pattern of tab depth and return switch sequence numbers")

##============================
##  look for 5 7 pattern()
##============================     
def look_for_5_7_pattern():
    print("===== look for 5 7 pattern ====")
    input_tab_combo('5','7')
    print("look for 5 7 pattern of tab depth and return switch sequence numbers")
    
plums=[]
plums_data=[]
endswitchlinenumbers=[]
endtabslist=[]

print("did we make it here......")
##=============================================================
## magic_potion   saturday september 18th, 2021 time 11:14 am
##=============================================================
def magic_potion(inputstring):
    print("============== magic_potion() called ============")
    print("================....===========")
    print("  ===== switch matrix adding...")
    for line in inputstring.splitlines():
        print(line)
    #switch_count=0    
    switch_count = 0 #for first
    #switchlinenumbers.append(0) #skips 0 not counted
    counter =0
    newstring='data on analyzing a multinested string to number the switches and tabs' + "\n"
    collosal=''
    print("This  finds the switch locations ----")
    for line in inputstring.splitlines():
        if "switch" in line and "endswitch" not in line:
            print(line)
            tabsnow= line.count("\t")
            tabslist.append(tabsnow)
            switchlinenumbers.append(counter)
            switch_count += 1
            bump =''
            if tabsnow == 1:
                bump = " "
            else:
                pass
            newstring +=  "sw_order_num= " + str(switch_count) + " " + "switch_line=" + str(counter) + bump + " tabs =" + str(tabsnow) +  "\n" 
            collosal = [str(switch_count),str(counter),str(tabsnow)]
            peach_data.append(collosal)
            counter += 1
        else:
            #newstring += "\n"
            counter += 1
    #del switchlinenumbers[0]        
    print("switchlinenumbers",switchlinenumbers)
    print("tabslist=",tabslist) 
    print("now we will print out what it sees")
    print("switch counter,switch line number,tab length")
    print(peach_data)
    print("=======")
    print("insert 000 in first data ")
    peach_data.insert(0,[0,0,0]) #this is to eliminate computer math with 0
    for item in peach_data: #already filled
        print(item)
    
    print("show first row now")
    ##################
    ##################=====
    #=======================================
print("============== experiment ==== sep 28th =2021 making the pairs ===")
print("and stacking switches and endswitches by tab depth.")
print("this only does 3 tab depth")

#switch_lines=[]
'''
def make_parent_child_set(inputstring):
    #print(inputstring)
    real_counter=0
    for line in inputstring.splitlines():
        
        #this skips line if not 7 tabs and switch not in line
        tab_length = line.count("\t")
        if "switch" in line and "end" not in line and tab_length== 1:
            #switch_lines.
            counter += 1; continue
       
       if "switch" in line and "end" not in line and tab_length== 3:
            #switch_lines.
            counter += 1; continue
        
        
        if "switch" in line and "end" not in line and tab_length== 5:
            #switch_lines.
            counter += 1; continue
            
        if "switch" in line and "end" not in line and tab_length== 1:
            #switch_lines.
            counter += 1; continue
'''                
#make_parent_child_set(red_robin)

def little_test():
    print("little test here")
    number = 2
    if number in range(1,4):
        print("yes ",number, " it's in the list")
    else:
        print("no number ", number, " not  in list")

little_test()





#this builds the pairs of switch endswitches by tabs since they ahve to be lined up
#from the switch down to the endswitch in the same tab depth 


'''
#NOTE:
def little_method(fivetabs):
  for item in tabsubs:
    fivetabs.append(item) 
  del tabsubs[:] 
'''
        
## loops thru tabsubs and appends item to tabcount
#=========================
#  little_method(tabcount)            
#=========================
def little_method(tabcount): #threetabs example is the param here in tabcount
    print(" little_method() called")
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

  
  
  


###=============================== 
 
        #del tabsubs[:] #should clear it
###=================
rattabs=[]
##==== goldmedal test()  this just does threetabs 
def goldmedaltest(): #this makes stacks column switch endswith for 3 tabs
	print("=======goldmedal test=== this one is correct== its gotta work now please ---")
	inputstring = red_robin
	print("original working code for 3 tabs that worked previously")
	counter =0
	for line in inputstring.splitlines():
		print(line)
		#######################
		tab_length = line.count("\t")
		if tab_length != 3 or "switch" not in line:
			counter += 1;continue
		#######################
		if tab_length == 3:
			if "switch" in line and "end" not in line:
				print("if switch called")
				print("======switch in line===")
				rattabs.append(counter)
				print(rattabs)
				counter += 1;continue
			if "endswitch" in line:
				print("if endswitch called")
				print("======endswitch in line======")
				rattabs.append(counter)
				print(rattabs)
				counter += 1; continue

#print("result of goldmedal test =")
#goldmedaltest()



#was in experiemntal machinery below
'''
    for line in inputstring.splitlines():
        print(line)
        tab_length = line.count("\t")
        if tab_length != 3 or "switch" not in line:
            counter += 1;continue
        ##################
        if tab_length == 3:
            if "switch" in line and "end" not in line:
                print("if switch called")
                print("======switch in line===")
                dumbtabs.append(counter)
                print(threetabs)
                counter += 1;continue
            if "endswitch" in line:
                print("if endswitch called")
                print("======endswitch in line======")
                threetabs.append(counter)
                print(threetabs)
                counter += 1; continue
    print("this one blast time for 31 flavors THIS IS THREE TABS === ---")
    print("threetabs=",threetabs)
'''
    
    
    
    
    
print('testing the internal machinery method engine now')
#threetabs=[]
#endtabslist=[]
#endswitchlinenumbers=[]
#dumbtabs=[]
##==============================
##  experimental_machinery uses internal_machinery method
##===============================
def experimental_machinery(x,inputstring):
    print("======experimental_machinery called==========")  
    counter =0
    newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    print(newstring)
    internal_machinery(x,inputstring)
 
    ###============
    #switches and endswitches at 3 tabs should be even number
#print("dumbtabs =",dumbtabs)

#print("== bees ==== this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring) ====")
#print("try_all_three(inputstring)")
#print("=====halloween ghosts trying all three 3 5 7 tabs now====")
#print(" === to the moon when will starship land ===")
#print("======= TESTING NEW CODE HERE WEDNESDAY to get the larget tab depth in string")
# this determines the highest tab count for a line with a switch
# which is used to create the listinput list

#try all three()  Did this one on Wednesday late sep

#threetabs=[[22,33],[44,66]]
#fivetabs =[[55,58],[77,86]]
#seventabs=[[88,99],[102,110]]

combined_tabs=[]
christmastree=[]

##============================================
## combine the lists together  #waterfall ifs
##=============================================
def combine_the_lists_together(x): 
    print("=====COMBINE THE LISTS TOGETEHR(X)....")
    print("blast off test of combine_the_lists_together(x)",x)
    print("at top of combine_the_lists_together use assertion x =",x)
    print("combine_the_lists_together CALLED of the wild combine the lists of tabs pairs together so sweet now ")
    #print("ASSERTIONS times") #will either be 0 or a number
    get_length_of_threetabs    = len(threetabs)
    get_length_of_fivetabs     = len(fivetabs)
    get_length_of_seventabs    = len(seventabs)
    get_length_of_ninetabs     = len(ninetabs)
    get_length_of_eleventabs   = len(eleventabs)
    get_length_of_thirteentabs = len(thirteentabs)
    #test if threetabs list is empty
    print("testing if length of threetabs list GREATER THAN 0")
    if get_length_of_threetabs > 0: #then proceed there is at least one
        print("YES length of threetabs IS GREATER THAN 0",get_length_of_threetabs)
        #this is a waterfall extending numbers to add to christmastree list
        if x >=  3:christmastree.extend(threetabs);
        if x >=  5:christmastree.extend(fivetabs);  
        if x >=  7:christmastree.extend(seventabs);
        if x >=  9:christmastree.extend(ninetabs); 
        if x >= 11:christmastree.extend(eleventabs);
        if x >= 13:christmastree.extend(thirteentabs);
    
    else:
        print('all of the tab lists are empty')
        print("don't bother trying to extend empty tab lists")
       
    print('at le bottom of function combine_the_lists_together christmastree list now has')
    print(christmastree)
    print(":what is in the christmas list above here starbucks")
    print("the chrsitmastree list is what should be whole at this point HER!!!")
    


##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("=== build_tab_list_added_together(x)======>>>>")
    print("this combines separate lists together into one list all be it clumsily")
    print("larget_tab_number =",largest_tab_number)
    del christmastree[:] #clears out the combined_tabs list to erase it
    print("about to call combine_the_lists_together wed nov 17th ")
    ## calling combine the lists together here 
    combine_the_lists_together(largest_tab_number) #<<==input is the largest tab number
    
    
    
    
#this calls it  
print("FIRST ATTEMPT ====3====")     
build_tab_list_added_together(3) #produces togetherlist=threetabs + fivetabs + seventabs   
print("combined_tabs=",christmastree)
for item in christmastree:
    print(item)
print("======this should have the lists above it= ")
 #clear it out 
print("NEXT ATTEMPT =====5===")
build_tab_list_added_together(5) #produces togetherlist=threetabs + fivetabs + seventabs   
print("christmastree=",christmastree)
for item in christmastree:
    print(item)
print("NEXT ATTEMPT =====7===")
build_tab_list_added_together(7) #produces togetherlist=threetabs + fivetabs + seventabs   
print("christmastree=",christmastree)
for item in christmastree:
    print(item)

 

 
 
fox=[]  #this is just a simple test 
def wildtest(themax):
    print("themax =",themax)
    print("called wildtest to add to list")
    if themax == 3: 
      fox.append(3) #.append(3)
      
    if themax == 5: 
      fox.append(5)
      
    if themax == 7: 
      fox.append(7)
      
      
    #if themax == 9: fox = [3,5,7,9]
    #if themax == 11:fox = [3,5,7,9,11]
    #if themax == 13:fox = [3,5,7,9,11,13]
    #if themax == 15:fox = [3,5,7,9,11,13,15]

print("starting fox list =",fox)
#wildtest(3)   
#wildtest(5)   
#wildtest(7)  
print("fox list =",fox)
print("above it should say 3,5,7")
print("road to tahoe is up hill")



         



            
            
            
            
            
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    print("==== METHOD 1 ==")
    print("build tab depth ==== METHOD 1 ==  build_tab_depth(=======>>")
    print("")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    print("max tab depth=",add_tab_depth[0])
            
##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():  #this fills the max holding_themax[0]
     print("==== METHOD 2 ==")
     print("====================  #METHOD 2 ========")
     #add_tab_depth = input
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     print("themax=",themax)


#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  #line 976
    print("==== METHOD 3 ================")
    print('====================METHOD 3 ==== line 976===>>>')
    print("this is .. build_list_input_list() ...")
    print("it gopher sees right here ",holding_themax[0])
    #holding_themax[0]
    mx = holding_themax[0] #it's using this number 
    print(type(holding_themax[0]))
    print("is it REALLY say 7  above this line???")
    if holding_themax[0] >= 3: put(3);
    if holding_themax[0] >= 5: put(5);
    if holding_themax[0] >= 7: put(7); 
    if holding_themax[0] >= 9: put(9); 
    if holding_themax[0] >= 11:put(11);
    if holding_themax[0] >= 13:put(13);
    if holding_themax[0] >= 15:put(15);
       
    print("at bottom of ifs what is in listinput")
    print(listinput)
    for item in listinput:
        super_listinput.append(item)
    print("super_listinput =",super_listinput)
  
  

#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("")
    print("==== METHOD 4.5 ==")
    print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
    print("=== this is just sick bad ass ========")
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
    else:
        print("nada")
        print("these are the tab lists from three to thirteen rudolph fly")
        print("3 and 5 tabs =",threetabs ," ",fivetabs)    
        print("7 and 9 tabs =",seventabs ," ",ninetabs)   
        print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   


  
  


##==================================================
## make_switch_and_endswitch_pairs_by_tab_levels()
## methods: internal_machinery() 
##=================================================== 
def make_switch_and_endswitch_pairs_by_tab_levels(inputstring): 
    print("make_switch_and_endswitch_pairs_by_tab_levels()")
    print("==== METHOD 4 ==")
    print(":=============== METHOD 4 ======") 
    for item in super_listinput:     # listinput is dynamically made above
        x = item;
        internal_machinery(x,inputstring)
     
    #print("  make_switch_and_endswitch_pairs_by_tab_levels(): ")
    #print("listinput list =",listinput)
    #print("THIS IS CALLING INTERNAL_MACHINERY METHOD ")   
    #for item in listinput:     # listinput is dynamically made above
    #    x = item;
    #    internal_machinery(x,inputstring)   #METHOD internal_machinery()






  
##=================================
##  list_tabs_lists_by_depth():
##================================== 
def list_tabs_lists_by_depth():
    print("==== METHOD 5 ==")
    print("==list tabs lists by depth=====METHOD 5======>>")
    print("threetabs=" ,threetabs); print("fivetabs="  ,fivetabs);
    print("seventabs=" ,seventabs); print("ninetabs="  ,ninetabs);
    print("eleventabs=",eleventabs);print("thirteentabs=",thirteentabs) 
    

#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    print("== combine tabs by length into christmastree_list======")
    print("==== METHOD 6 ==")
    print("======METHOD 6 ===  combine tabs by length into christmastree_list====>>>>")
    themax = holding_themax[0] #this gets the highest tab level (deeply nested)
    print("where is my coffee now")
    print('let us look in the three tabs list threetabs, fivetabs, seventabs')
    print(threetabs,fivetabs,seventabs)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    print("christmastree=",christmastree)
    print("")
    



#================================= 
#  build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    print("")
    print("==== METHOD 7 ==")
    print("=== METHOD 7== build pairs with jazz =======>>>>")
    print("")
    counter =0
    print("inside of build pairs with jazz the christmastree list show")
    print("christmastree=",christmastree)
    for x in christmastree: #loops thru at 2 at a time
        print(christmastree[counter],christmastree[counter +1])
        jazz = [christmastree[counter],christmastree[counter+1]]
        print("appending jazz to snowtime list now")
        #list snowtime starts virgin and then we append jazz pairs to it
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        ##=========================================================
        #prevents overflow error for out of range error
        print("this is the resulting pair list that is so coveted")
        print("this used the jazz pair pair system that works")
        print("snowtime list=",snowtime)
        if counter >= len(christmastree):
            break
            
            
            
gold_list=[]                   
def loop_thru_pairs_in_snowtime():
    print("==== METHOD 8 ==")
    print(" ==== #method 8 ===  loop_thru_pairs_in_snowtime()=============")
    print("snowtime list=",snowtime)
    for item in snowtime:  #snowtime list is loaded into gold_list
        gold_list.append(item)
    print("gold_list=",gold_list)  
    #    print(item);
        #rad1=item[0];rad2=item[1];
        #print(rad1,"and ",rad2)
   





#def goldtime():
#    print("goldtime callled goldtime goldtime")
#    for item in super_listinput:     # listinput is dynamically made above
#        x = item;
#        internal_machinery(x,inputstring)
# REFACTORED on nov 8th , 2021 to reduce the complexity modified nov 9th


##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
##========================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    print("=======THIS MAKES SWITCH AND ENDSWITCH PAIRS BY TAB LEVELS========")
    #welcome to - time 10;43 am nov 9th-")
    print("this is unreal; this_makes_switch_and_endswitch_pairs_by_tab_levels()")
    build_tab_depth(inputstring)                               #METHOD 1
    get_max_tab_number_in_list() #fills holding_themax[0]      #METHOD 2
    build_list_input_list()                                    #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels(inputstring) #METHOD 4
    list_tabs_lists_by_depth()                                 #METHOD 5
    combine_tabs_by_length_into_christmastree_list()           #METHOD 6 together
    build_pairs_with_jazz()  #combines into sublist            #METHOD 7 in christmas list
    loop_thru_pairs_in_snowtime()                              #METHOD 8
    #this will go into gold_list
        
        
'''
=== METHOD 7== build pairs with jazz =======>>>>

inside of build pairs with jazz the christmastree list show
christmastree= [11, 47, 49, 73, 15, 38, 53, 64, 23, 33]

==== #method 8 ===  loop_thru_pairs_in_snowtime()=============
snowtime list= [[11, 47], [49, 73], [15, 38], [53, 64], [23, 33]]
#after running it======= The Road Runner ==================
'''
        
        
        
        
    
 
 
     #this gets one pair in showtime designated by x 
def get_pair_in_snowtime(x):
     print(" get pair in snowtime testing",x)
     #what if I add 0,0 to first position brilliant
     if len(snowtime) == 0:
        print("length of snowtime is zero")
     print(snowtime) #would be second position
     cool = snowtime[x]
     print("list at position ",x," is",cool)
    #christmastree = [11, 47, 49, 73] [15, 38, 53, 64][23, 33]
    #next reduce to pairs
    #christmastree = [[11,47],[49,73],[15,38],[53,64],[23.33]]

print("mocha test now mocha mocha mocha mocha mocha")    
#get_pair_in_snowtime(1)
#get_pair_in_snowtime(2)
print("does it return this,[11,47],[49,73]")
print("lightning storm ===")
 
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

print(x)
print("is this thing turned on")
print(fruits[1])
searchlist=[22,44,55,77,88,102] #shadows actaul pairs with jsut first number 
snowballs=[[22, 33], [44, 66], [55, 58], [77, 86], [88, 99], [102, 110]]
snowballs.insert(0, [0,0])
for item in snowballs:
	print(item)

######=================================
#maybe switch line numberYES will be used to access the pairs
#breakthru and use a dictioanry with switch id line number
# like 11 which is going to be the first number in the pair brilliant
############==================================================


param1=[]
param2=[]
param1.append(0)
param2.append(0)
##==============================
##  get_pair_in_pairslist   example  get_pair_in_pairslist(1)
##==============================
#output param1[0] and param2[0] for a pair 
def get_pair_in_pairslist(x): 
	print("get pairs in pairslist()")
	wild= snowballs[x]  #this is accessing snowballs list 
	print("pair=",wild)
	alpha = wild[0]
	beta = wild[1]
	print("data=",alpha," ",beta)
	param1[0] = alpha
	param2[0] = beta
	print("we have these returns param1[0] and param2[0]",param1[0],"and",param2[0])
	
	
print("=============should be 55,58======")
get_pair_in_pairslist(3)
print("now 1")
get_pair_in_pairslist(1)
print("now 2")
get_pair_in_pairslist(2)
print("now 4")
get_pair_in_pairslist(4)



#[[22, 33], [44, 66], [55, 58], [77, 86], [88, 99], [102, 110]]


test_pairs = {
  "22":  "[22,33]",
  "44":  "[44,66]",
  "55":  "[55,58]",
  "77":  "[77,86]",
  "88":  "[88,99]",
  "102": "[102,110]"
}
print(test_pairs)
##========================================
## get_pair_for_switch_number(x):  #this accesses the test_pairs dictionary
##========================================
def get_pair_for_this_switch_number(x):
    print("x=",x)
    y = test_pairs[x]
    #y = eval("test_pairs.get(x)")
    print("pair =",y)
    0
#still trying to remember why I will need this   
print("testing using a dictioanry to search by switch number for pair")
get_pair_for_this_switch_number('22')
get_pair_for_this_switch_number('44')
get_pair_for_this_switch_number('55')

# I will need to go thru this pair list and HARVEST the first number and include
#it's index number and then feed that into a dictionary


#print("now go thru it and see if it goes thru the the list
print("testing looping thru list and getting each pair")
# I am testing this since I need to go direclty to a pair and extract it for copying strings
counter = 1
for item in snowballs:
	get_pair_in_pairslist(counter)
	counter += 1
	if counter >= len(snowballs):
		break
    
##==============================================================    
#we know that there will be sets of 2 numbers closest to each other
#go thru list and grab two at a time seems simple enough
#based on highest tab number which we would know like 7
#threetabs= [11, 47, 49, 73]
#fivetabs= [15, 38, 53, 64]
#seventabs= [23, 33]

peartree=[]
startime=[]
#loop thru threetabs
print("TEStING PeAR TREE backyward with plum tree to see if it works")
print("add result to final_pears_list")
print("does this one work and print x,y")
#my_list = [1,2,3,4,5,6,7,8,9,10]
print("about to see if christmas will come early this year or not")

##======================================
## fill_main_pear_list(listname):  #this build the combined list correctly 
#the lists threetabs,fivetabs,seventabs,ninetabs need to already be filled
#this is just combining them together adding them together
##=====================================
def fill_main_pear_list(listname):
    print("=====fill_main_pear_list called with listname======")
    counter=0 #this must be at 0
    for x in listname:
        print(listname[counter],listname[counter +1])
        jazz = [listname[counter],listname[counter+1]]
        startime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2
        if counter >= len(listname): #prevent from going out of bounds
            break
    print("startime list=",startime)
    print("what did this work.......or not ....did it")
    if holding_themax[0]>= 3:fill_main_pear_list(threetabs);
    if holding_themax[0]>= 5:fill_main_pear_list(fivetabs);
    if holding_themax[0]>= 7:fill_main_pear_list(seventabs);   
    if holding_themax[0]>= 9:fill_main_pear_list(ninetabs);
        
    #put in list highest tab number say 7
    
    
    
    
    
       
       
       
print("final startime filled with three tabs, five tabs, seven tabs in pairs")
print("battle star galactica")
print("startime=",startime)

print('testing fill main pear list with christmastree ')
#fill_main_pear_list(christmastree)
#it = iter([11, 47, 49, 73])
#for x, y in zip(it, it):
#    print(x, y)
#    jazz=[x,y]
#    peartree.append(jazz)
#    print("peartree =",peartree)

#print("peartree[0]=",peartree[0]) 
#print("peartree[1]=",peartree[1])
#apple1 = peartree[0][0]
#apple2 = peartree[0][1]
#print("apple1",apple1," and apple2", apple2)
#print(apple1,apple2) 
#for item in threetabs: #this is a list
#    print(item)
#    counter += 1
#    
#for item in threetabs: #this is a list
#    print(item)
#    counter += 2
    
    #counter += 1
    #print(item)
    #sly2 =item
    #counter += 1
    #print(sly1,sly2)
    #item = item.split()
    #chimp1 = item[0]
    #chimp2 = item[1]
    #print(chimp1, chimp2)
    #counter += 2 #count by 2 genius
   # print("wow will this work")
    #jazz = "[" + str(item[counter]) + "," + str(item[counter +1]) + "]"
    #peartree.append(jazz)
    #print(peartree)
    
print("end of starbucks show..")   
    


#def build_list_now_from_pairs  
    
    #print("threetabs[0]=",threetabs[0]) #simpler just use this one
    
    #app = len(threetabs)
    #print("threetabs length =",app)
    #print("")
    #if app == 4:
    #    print("yep")
    #    first.append(threetabs[0]) #11
    #    first.append(threetabs[1]) #47
    #    print(first,"first[0]=",first[0],"first[1]=",first[1])
    #    #"second =[" + str(threetabs[2]) + "," + str(threetabs[3]) + "]"
    #   #print(second)
    #    print(type(first))
    #else:
    #   print("falsy")
    



def make_sets_from_three_tabs():
    print("get length of threetabs")
    print(threetabs)

make_sets_from_three_tabs()

threetabs=[]
endtabslist=[]
endswitchlinenumbers=[]
##======================
##  sound_of_music
##======================
def sound_of_music(inputstring):
    return #kill it
    print("sound of dam music called=====using intnernal_machinery() =====")  
    print("sound of dam music called==========")
    print("sound of dam music called==========") 
    counter =0
    newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    print(newstring)
    
    #inputstring = red_robin
    #x=3
    #internal_machinery(x,inputstring)
  
    ###===================================
    print("this one blast time for 31 flavors THIS IS THREE TABS === ---")
    print("threetabs=",threetabs)
    ###============
    #switches and endswitches at 3 tabs should be even number
print("threetabs =",threetabs)







##======================
##  sound_of_music
##======================
fivetabs=[]
def sound_of_music2(inputstring):
    return #kill it
    print("sound of dam music called")   
    counter =0
    #newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    #print(newstring)
    x=5
    internal_machinery(x,inputstring)
    print("time for 31 flavors THIS IS THREE TABS === ---")
    print("fivetabs=",fivetabs)
    ###============
    #switches and endswitches at 3 tabs should be even number
print("threetabs =",threetabs)
#threetabs= [11, 47, 49, 73]

#============================
'''
  #for line in inputstring.splitlines():
    #    print(line)
    #    tab_length = line.count("\t")
    #    if tab_length != 5 or "switch" not in line:
    #       counter += 1;continue
    #    ##################
    #    if tab_length == 5:
    #        if "switch" in line and "end" not in line:
    #            print("if switch called")
    #            print("======switch in line===")
    #            fivetabs.append(counter)
    #            print(fivetabs)
    #            counter += 1;continue
    #        if "endswitch" in line:
    #            print("if endswitch called")
    #            print("======endswitch in line======")
    #            fivetabs.append(counter)
    #            print(fivetabs)
    #            counter += 1; continue
    '''
    
##======================
##  sound_of_music
##======================
seventabs=[]
def sound_of_music3(inputstring):
    return #kill it
    print("sound of dam music called")   
    counter =0
    newstring='data on analyzing a multinested string to number the endswitches and tabs' + "\n"
    collosal='';tab_length=''
    print(newstring)
    #this should be a method inside of it 
    x=7
    internal_machinery(x,inputstring)

    
    
    print("seventabs=",seventabs)
    print("time for 31 flavors THIS IS seven TABS === ---")
    print("seventabs=",seventabs)
    ###============
    #switches and endswitches at 3 tabs should be even number
print("seventabs =",seventabs)
#threetabs= [11, 47, 49, 73]





#threetabs= [11, 47, 49, 73]
    #should be 1, 11, 15, 23
    #33  38 47
    ###=============================
    
    #print(peach_data[2][0]) #2 #this row will always be empty 
    #print(peach_data[2][1]) #11
    #print(peach_data[2][2]) # 3
    #print("test if peach_data[2][2] == '3': ")
    #print("testing if switch2 has 3 tabs in front of it")
    #if peach_data[2][2] == '3':
    #    print("= TRUE ==party time===")
    #else:
    #    print("==FALSE ===does not compute===")
    #print('peach_data[1]=',peach_data[1])
    #print('peach_data[2]=',peach_data[2])
    #print('peach_data[3]=',peach_data[3])
    #print('peach_data[4]=',peach_data[4])
       
    #print("=========")
    #for line in newstring.splitlines():
    #    print(line)
    #oh yea I need to make a method that does this all at once.
    #I can have it hop thru a list to change the number
#print("now three tabs")
#three tabs
#right here we add red_robin

#sound_of_music(red_robin)

#print(" below the first one sound of music")
#print("now five tabs")
#five tabs

#sound_of_music2(red_robin)

#print("now seven tabs")
#seven tabs
###============================================================================
##  create_list_of_pairs_now(inputstring):
##  methods:  this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)
##=============================================================================
def create_list_of_pairs_now(inputstring):
    print("====create list of pairs now(0  dec 13th monday ===========================")
    print("this calls: this_makes_switch_and_endswitch_pairs_by_tab_levels")
    print("make it so star trek")
    
    print("what red_robin looks like before calling try_all_three=====")
    print(inputstring)
    print("see how it looks above if there are double switches and endswitches yet")
    this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)
    
   
    print("after running it======= The Road Runner  2.0 ===================")
#exit()
###=================================================
#when running from frosty.py comemnt the two lines below out
inputstring = red_robin
create_list_of_pairs_now(inputstring);

print('now show the pairs list')
#commented out of course..
#exit()
