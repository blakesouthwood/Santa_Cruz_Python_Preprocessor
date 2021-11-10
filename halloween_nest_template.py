#import official_switch_case_silver
#from official_switch_case_silver  import *  

zoo=[]
zoo.append(0)# zoo[0]
zoo.append(1)# zoo[1]
#zoo[1] = 'test3'


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


#==============================
#  build_listinput_list  for threetabs,fivetabs, seventabs,ninetabs, eleventtabs,thirteentabs
#==============================
def build_list_input_list():  #line 976
    print('build list input list() ======METHOD 3 ==== line 976===>>>')
    print("it gopher sees right here ",holding_themax[0])
    #holding_themax[0]
    mx = holding_themax[0] #it's using this number 
   
    print("")
    print('we know it sees 7')
    print(type(holding_themax[0]))
    print("is it REALLY say 7  above this line???")
    if holding_themax[0] == 3: 
        listinput=[3]; #.append(3)
        
    if holding_themax[0] == 5:
        listinput=[3,5];
        
    if holding_themax[0] == 7: 
        listinput=[3,5,7];
    
    if holding_themax[0] == 9: 
        listinput=[3,5,7,9];
    
    if holding_themax[0] == 11:
        listinput=[3,5,7,9,11];
    
    if holding_themax[0] == 13:
        listinput=[3,5,7,9,11,13];
    
    if holding_themax[0] == 15:
        listinput=[3,5,7,9,11,13,15];
    
    print("at bottom of ifs what is in listinput")
    print(listinput)
    for item in listinput:
        super_listinput.append(item)
    print("super_listinput =",super_listinput)
  
  
  
  
  
  
  
  
  
  
  
  
  
##=================================
##  list_tabs_lists_by_depth():
##================================== 
def list_tabs_lists_by_depth():
    print("==list tabs lists by depth=====METHOD 4======>>")
    print("threetabs=" ,threetabs); print("fivetabs="  ,fivetabs);
    print("seventabs=" ,seventabs); print("ninetabs="  ,ninetabs);
    print("eleventabs=",eleventabs);print("thirteentabs=",thirteentabs) 
    










#this takes in the tab depth with x and goes thru the string
#and fills the appropiate tab list if 3 then threetabs, if 5 then fivetabs
##====================================================
## internal_machinery()   designed wed sep 29th, 2021
##====================================================
## key engine inside of function this_makes_switch_and_endswitch_pairs_by_tab_levels()
def internal_machinery(x,inputstring): #this doesn't change anything in the string whatsoever
    print("")
    print("===internal_machinery() called=== METHOD 4.5  inside of METHOD 4  ===")
    print("")
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
    print("these are the tab lists from three to thirteen rudolph fly")
    print("3 and 5 tabs    =",threetabs ," ",fivetabs)    
    print("7 and 9 tabs    =",seventabs ," ",ninetabs)   
    print("11 and 13 tabs  =",eleventabs," ",thirteentabs)   




##==================================================
## make_switch_and_endswitch_pairs_by_tab_levels() 
##=================================================== 
def make_switch_and_endswitch_pairs_by_tab_levels(): 
    print("make_switch_and_endswitch_pairs_by_tab_levels()")
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
##  experimental_machinery
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

 #testing purposes
# this adds the tabs lists like threetabs + fivetabs + seventabs into combined_tabs list
print("== snowmen having snowball fight==testing build_tab_list_added_together(x):======")
##========================================================
##  build_tab_list_added_together(largest_tab_number):   Thursday, Nov 4th, 2021 
#   this does this combined_tabs = threetabs + fivetabs + seventabs etc
##========================================================
def build_tab_list_added_together(largest_tab_number):
    print("=== build_tab_list_added_together(x)======>>>>")
    print("larget_tab_number =",largest_tab_number)
    del christmastree[:] #clears out the combined_tabs list to erase it
    if largest_tab_number == 3:
       christmastree.extend(threetabs)
           
    if largest_tab_number == 5:
        christmastree.extend(threetabs)
        christmastree.extend(fivetabs)
            
    if largest_tab_number == 7:
        christmastree.extend(threetabs)
        christmastree.extend(fivetabs)  
        christmastree.extend(seventabs)        
    
    if largest_tab_number == 9:
        christmastree.extend(threetabs)
        christmastree.extend(fivetabs)  
        christmastree.extend(seventabs) 
        christmastree.extend(ninetabs)        
    
    if largest_tab_number == 11:
        christmastree.extend(threetabs)
        christmastree.extend(fivetabs)  
        christmastree.extend(seventabs)
        christmastree.extend(ninetabs) 
        christmastree.extend(eleventabs) 
    
    if largest_tab_number == 13:
        christmastree.extend(threetabs)
        christmastree.extend(fivetabs)  
        christmastree.extend(seventabs)
        christmastree.extend(ninetabs) 
        christmastree.extend(eleventabs)
        christmastree.extend(thirteentabs)         
    
#this calls it  
     
build_tab_list_added_together(3) #produces togetherlist=threetabs + fivetabs + seventabs   
print("combined_tabs=",christmastree)
for item in christmastree:
    print(item)
print("======= ")
 #clear it out 
build_tab_list_added_together(5) #produces togetherlist=threetabs + fivetabs + seventabs   
print("christmastree=",christmastree)
for item in christmastree:
    print(item)

build_tab_list_added_together(7) #produces togetherlist=threetabs + fivetabs + seventabs   
print("christmastree=",christmastree)
for item in christmastree:
    print(item)
#exit();
 
 
 
 
fox=[]
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
wildtest(3)   
wildtest(5)   
wildtest(7)  
print("fox list =",fox)
print("above it should say 3,5,7")
print("road to tahoe is up hill")



#==========================================================
# combine_tabs_by_length_into_christmastree_list(input)
#==========================================================
def combine_tabs_by_length_into_christmastree_list():
    print("")
    print("combine tabs by length into christmastree_list===METHOD 6 ======>>>>")
    themax = holding_themax[0]
    print("where is my coffee now")
    print('let us look in the three tabs list threetabs, fivetabs, seventabs')
    print(threetabs,fivetabs,seventabs)
    build_tab_list_added_together(holding_themax[0])   #METHOD  7
    print("christmastree=",christmastree)
    print("")
    '''
    if input == 3:
        print('3 total in themax')
        christmastree = threetabs
    if input == 5:
        print('5 total in themax')
        christmastree=threetabs +fivetabs
    if input == 7:
        print('7 total in themax')
        christmastree=threetabs +fivetabs + seventabs
    if input == 9:
        print('9 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs
    if input == 11:
        print('11 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs  + eleventabs 
    if input == 13:
        print('13 total in themax')
        christmastree=threetabs +fivetabs + seventabs + ninetabs + eleventabs + thirteentabs
     '''
       
         



#================================= 
# build_pairs_with_jazz()
#=================================  
#this goes thru christmas list of pairs and and makes snowtime list of pairs jazz added to snowtime 
def build_pairs_with_jazz(): 
    print("")
    print("build pairs with jazz ======= METHOD 7=====>>>>")
    print("")
    counter =0
    for x in christmastree: #loops thru at 2 at a time
        print(christmastree[counter],christmastree[counter +1])
        jazz = [christmastree[counter],christmastree[counter+1]]
        print("appending jazz to snowtime list now")
        #list snowtime starts virgin and then we append jazz pairs to it
        snowtime.append(jazz) #using startime as practice main pairs list for now nov 3
        counter += 2 
        #prevents overflow error for out of range error
        if counter >= len(christmastree):
            break
            
            
            
            
            
            
            
#=======================================
#  build_tab_depth(inputstring)
#========================================            
def build_tab_depth(inputstring):
    print("")
    print("build tab depth ======= METHOD 1 =========>>")
    print("")
    for line in inputstring.splitlines():
        if "switch" in line and "end" not in line: #this is looking for a switch in a line
            get_tab_depth=line.count("\t")      #this is a var that gets the count of tabs
            add_tab_depth.append(get_tab_depth) #this is for filling the list of each tab depth
        else:
            continue
    print("add_tab_depth=",add_tab_depth)
    print("max tab depth=",add_tab_depth[0])
            
      
      
      
      
      
            
            
def loop_thru_pairs_in_snowtime():
    print(" ==== #method 8 ===")
    print("snowtime list=",snowtime)
    for item in snowtime:  
        print(item);
        rad1=item[0];rad2=item[1];
        print(rad1,"and ",rad2)




##=======================================
## get_max_tab_number_in_list()
##=======================================       
def get_max_tab_number_in_list():
     print("====================  #METHOD 2 ========")
     #add_tab_depth = input
     themax = max(add_tab_depth);  #a list of the tabs before switches
     holding_themax[0]=themax;
     print("themax=",themax)


#def goldtime():
#    print("goldtime callled goldtime goldtime")
#    for item in super_listinput:     # listinput is dynamically made above
#        x = item;
#        internal_machinery(x,inputstring)
# refactored on nov 8th , 2021 to reduce the complexity modified nov 9th
##========================================================
## this_makes_switch_and_endswitch_pairs_by_tab_levels
##========================================================  
def this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring):
    #welcome to - time 10;43 am nov 9th-")
    print("this_makes_switch_and_endswitch_pairs_by_tab_levels()")
    build_tab_depth(inputstring)                       #METHOD 1
    get_max_tab_number_in_list()                       #METHOD 2
    build_list_input_list()                            #METHOD 3
    make_switch_and_endswitch_pairs_by_tab_levels()    #METHOD 4
    list_tabs_lists_by_depth()                         #METHOD 5
    combine_tabs_by_length_into_christmastree_list()   #METHOD 6
    build_pairs_with_jazz()  #combines into sublist    #METHOD 7
    loop_thru_pairs_in_snowtime()                      #METHOD 8
    
        
    
 
 
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
    
    if holding_themax[0]== 9:
        fill_main_pear_list(threetabs)
        fill_main_pear_list(fivetabs)
        fill_main_pear_list(seventabs)
        fill_main_pear_list(ninetabs)
        
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

print("======================================")
print("make it so star trek")
inputstring = red_robin
print("what red_robin looks like before calling try_all_three=====")
print(red_robin)
print("see how it looks above if there are double switches and endswitches yet")
this_makes_switch_and_endswitch_pairs_by_tab_levels(inputstring)
print("testing if this sucker really filled up the list whith pairs")
for item in christmastree:
    print(item)
print("after running it======= The Road Runner ===================")
exit()
#print("right here we will see what is in the radical counter",radicalcounter)
print("aftger try_all_three() what red robin looks like ")
print("what red_robin looks like before calling try_all_three=====")
print(red_robin)
#exit()

#this_makes_switch_and_endswitch_pairs_by_tab_levels



print("I think that it should be only 3 times")
#sound_of_music3(red_robin)
print('what does this look like')
print("=== THIS IS THE OUTPUT OF SWITCH ENDSWITCH PAIRS ===")
print("======actual output we are seeking=======")
print("threetabs=",threetabs)
print("fivetabs=",fivetabs)
print("seventabs=",seventabs)
print("seventabs=",ninetabs)
print("seventabs=",eleventabs)
print("==========")
print('now the method one mechanical machinery')
print("trying goldmedaltest() now...")
#goldmedaltest()
#print("rattabs=",rattabs)
#exit()


'''
[0, 0, 0]
['1', '1', '1'] #skip first one 
['2', '11', '3']  
['3', '15', '5']
['4', '23', '7']
show first row now
======= endswitch adding information data for matrix ===
This  finds the switch locations ----
data on analyzing a multinested string to number the endswitches and tabs

							endswitch 
					endswitch 
			endswitch 
endswitchlinenumbers [33, 38, 47]
tabslist= [7, 5, 3]
now we will print out what it sees
switch counter,switch line number,tab length
switches not including first switch

switch locations will all be lower numbers
['2', '11', '3']  ['3', '15', '5'] ['4', '23', '7']
#end switches
these need to be REVERSED DAAAA
end switch location 
[  ['3', '47', '3'],['2', '38', '5'],['1', '33', '7'],]

this is what the pairs will look like in a list 
look at the tabs and line number only
creating the pairs list
[11, 47]  3 tabs
[15, 38]  5 tabs
[23, 33]  7 tabs
so rather start counting from 2 for switches as 1

oh yea do your stacking by tab column switch and endswitches
#3 tabs  switch -1 by skipping one
switch 11  actually switch1(but really switch2) ignoring first one
endswitch 47  actually endswitch(max) positively brilliant

#5 tabs
switch 15   would be switch2 if I use a counter to name these
endswitch max-2   would be endswitch2 but just the line number matters

#7 tabs
switch 23
endswitch 33

three_tabs=[]


experiment
based on tab length
if "switch" in line and "end" notin line: and tab length == 3
    addswitch.append(count)
    
if "endswitch" in line and tab length == 3
    addswitch.append(count)
    
three_tabs=[]
switch , endswitch
[11,47]

five_tabs=[]
[15,38

seven_tabs=[]

'''







#end switches



#========

#['2', '11', '3'] ['3', '15', '5']['4', '23', '7']

#[['1', '33', '7'], ['2', '38', '5'], ['3', '47', '3']]




#11,33
#13    
##================================      
## loop_thru_found_values()
##===============================
def loop_thru_found_output_values():
    print(" ==mr coffee === loop thru found output values ====")
    print("if this is called do this")
    print(" ==== DRINK MOCHA ===")
    print("sitting at starbucks is this called")
    print("this has capture_switch_lines_nested[0]")
    print("=======loop thru found output values()=======")
    if len(capture_switch_lines_nested) == 0:
        print("capture_switch_lines_nested is EMPTY!!!")
    else:
        print("capture_switch_lines_nested=", capture_switch_lines_nested)
    if len(capture_switch_lines_nested) == 1:
        print("yep it will always have a length of 1")
        print(capture_switch_lines_nested)   
    else:
        pass
    for item in capture_switch_lines_nested:
        print(item)
 


print('beginning testing running the methods together')
print('let there be light')               
magic_potion(mocha_nested_switchtest)
print("end of saturday")
access_row_in_peach_data(2)
print(" ====== tahoe fire ============")
print("==========next test=============")
del peach_data[:]
print("contents in peach_data at start")
print(peach_data)
print("what does it show above this line?")

##############################
##################################
'''
print("==== now RED ROBIN testing here thursday sept 23rd  test =====")
print(" putting 3 and 5 in for pattern search")

#look_for_3_5_pattern() ## this is new monday sep 20th, 2021
#magic_potion(red_robin)

#print("the result is in capture_switch_lines_nested[0]")
#print("this list has the 3:5 pattern switch lines ")
loop_thru_found_output_values()
 #loops thru capture_switch_lines_nested
#del capture_switch_lines_nested[:]
print("====the great divide grand canyon South Rim ====")
print("====the great divide grand canyon South Rim ====")
print("====the great divide grand canyon South Rim ====")
##===============
'''
#look_for_5_7_pattern() ## this is new monday sep 20th, 2021

#magic_potion(red_robin)
#loop_thru_found_output_values()

##=============================
print("we will stop here ") 
#exit()
print("now at bottom")
#access_row_in_peach_data(1)
print("end of show")
#exit()
'''
######=======================================================
# the starting point is with inner switches bodies cut out
# but I just thought of putting their bodies in a list just for this switch strings
# this represents three nested switches in a switch after main string
# so thru the dictionary I could have the list of these inner switch strings
# that way they are easier to find
##===========================================================
#so this will actually be a module template used to do this

nest_list_sub1=[]
nest_list_sub1.append(0) #skipped since I don't use position [0]
#need addresses of levels to put in here 
# tab depth 3 = 1
# tab depth 5 = 2
# tab depth 7 = 3
'''


neststring1='''
switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			#if this is the 
			switch(exp){  #levels[1][1]
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			switch(exp){   ##levels[1][2]        representings stripped out inner nest    
			fallthru
			
		
		case 11 to 12:
			print('this is so frustrating')
			switch(exp){  #levels[1][3]
			print('== window won't go back up===')
			break
			
		default:
			print('the end')
}
'''

#working on this July 15th, 2021 10:16am Starbucks
#get_switch_and_endswitch_locations(coolstring)
#output to these lists
#switch_location #skips the first main switch not included
#endswitch_location (if any)
get_switch_and_endswitch_locations(red_robin)
print("DONE DONE DONE with this test- it must work")
print("I need the list of switch and endswitch locations")
print("I vaguely recall that I combine them in jedi")
print("done with test to get the nested switch locations within the big switch")

### this started working on july 9th, 2021 Friday. I forgot that it was friday.
genius=[]
genius.append(0)
# the number series will always start from 1 and then increase in number
number_series=[]
number_series.append(0)
switch_list=[]

#this accesses coolstring august 5th, 2021
#this is to set the inner switch positions in the main switch input strings
#after the bodies of the nested switches have been stripped out

##########################################
##  put_switch_locations_into_switch_list()  #this is making the nested_switch_ number  
##########################################
def put_switch_locations_into_switch_list(inputstring): #just added param
    print("##2### put_switch_locations_into_switch_list ###")
    print("##2## put switch locations into switch list ###")
    print("put switch locations into switch list")
    #### get swith and endswitch locations called here 
    get_switch_and_endswitch_locations(inputstring) #it's right here 
    for item in switch_location: #this is only going thru switch_location
        switch_list.append(int(item))  #was -1 on here #off by one in the string for some reason
    # print(" ");print("switch_list=")
    #print(switch_list)



#######################################
##  swap_switch_to_nested_method()  #this is making the nested_switch_ number  
#######################################
def swap_switch_to_nested_method(stringname,linenumber,series_num):
	#print("input: stringname", stringname)
	#print("input: linenumber", linenumber)
	#print("input: series_num", series_num)
	#print("##4## swap switch to nested method - numbered ###")
	#print("##4## swap switch to nested method - numbered ###")
	#print(" THIS IS BEING CALLED TO DO THE MAGICswap switch to nested method called....")
	str_list = stringname.split('\n')
	#print('changing line',linenumber)
	#series_num = number_series[0] 
	str_list[linenumber] = "\t\t\tnested_switch_" + str(series_num) + "(n)"
	stringname = "\n".join(str_list)
	genius[0]=stringname   #strings are immutable but lists are mutable(changeable)

######################################	

#this is the control center main that runs this operation
#this numbers the nested switch methods top down
#genius[0]=coolstring  #assignment here <<<==================



coolstring='' #just put this here sep 18th, saturday
#######################################
##  loop_thru_switch_locations():
#######################################
def loop_thru_switch_locations(regularstring):  #looping thru  switch_list[10,18]
    print("##1##loop thru switch locations ######")
    print("##1##loop thru switch locations ######")
    #trick put_switch_locations_into_switch_list
    #method called
    put_switch_locations_into_switch_list(regularstring) #method
    print('this filles switch_list of switch line numbers')
    #print(genius[0])
    print("what is the order of the switch_list I think it's reversed to do bottom up")
    print(switch_list)
    print("------------")
    print("switch_list=",switch_list)
    le_number=1 #default numbering nested string 
    for item in switch_list: #loops thru switch_list WITH SWITCH LOCATIONS (LINE NUMBERS)
        print("item in switch_list",item)
        #string,switch,line number
        # swap_switch_to_nested_method here 
        #method this one is the holy grail that actually works
        ###############################
        swap_switch_to_nested_method(genius[0],item,le_number) 
        coolstring =genius[0]
        le_number += 1  #adding to the nested number here
    print("#### end of loop thru switch locations() ####")
    print('the EXIT sign is green')
#######################################



print("STAR TREK TEST FULL PHOTON LASERS add numberednested method McCoy looks good now beam me up ")
print("starting with this input main string with nested switch bodies cut out")
print("tahoe dream")
##==========================================================|
## swap_nested_switches_with_methods_in_main_switch_string
##==========================================================|
genius=[]
genius.append(0)

def swap_nested_switches_with_methods_in_main_switch_string(inputstring):
    print("=== here we go = swap_nested_switches called ===")
    print("===swap_nested_switches_with_methods_in_main_switch_string()===") 
    loop_thru_switch_locations(inputstring) 
    print("this is the output string of the transformation from input string")
    ## this is after loop thruw switch locations method is completed
    print("this is the main input switch string after adding nested methods")
    print("the output of this transformation of swapping switch for nested_method")
    #this is the input string transformed 

#this calls it
#the change I made was changing the string from coolstring to old_coolstring
# saturday september 18, 2021

#this calls above
print("=== begin tron test ==line 323 =TESTING september 1st here we go=-=== to see if this sucker works === august 27th ==== please work ==")
print("this is testing the main switch string module changing nested switches")
print("that already had their bodies cut out and swaping in a nested method")
print("debugging test here....")
print("what is in coolstring",old_coolstring)
#just changed this it was coolstring I changed it to old_coolstring
genius[0]=old_coolstring  #assignment here <<<==================
print("about to call swap_nested_switches_with_methods_in_main_switch_string(coolstring)")
swap_nested_switches_with_methods_in_main_switch_string(old_coolstring)


print("fter testing tron getting closer=== 1 ...2.....3  out the EXIT")
print("the output is in genius[0]")
print(genius[0])
print('end of test of swap nesetd switches with methods in main switch string ')
print(" oh that's what this does...da ")
print("====line 332 ==end of this tron test september 1st=====")
print("======end of this tron test september 1st=====")
#exit()  #stop it here
	#string_change =coolstring
#stringname=coolstring
#print("now change the inner switches to the nested method numbered")
#swap_switch_to_nested_method(coolstring,10,1)	  #####======

print("after first change ====>>>>>>>")
#coolstring =genius[0]                            #########==========

#series_num = number_series[0] 
#swap_switch_to_nested_method(coolstring,18,2)	  ########=========
#print("after the 2nd change ...")
#coolstring =genius[0]
##print(genius[0])                                ################============
print("done with this test of the new method")
  #building the method to make this magic happen automatically


#-------------------  july 10th, 2021   11:03 pm  -------starbucks coding-------
#I am hard coding the location of the switch words. I need to have it search on it's own
# but I recall I have code that does that elsewhere
#now I need to find the code that makes the correct nested switch list locations

#they are being harded coded in here I should be getting them from above

#switch_list.append(11) #was 10,18,31
#switch_list.append(19)
#switch_list.append(32)## added a third switch to test it more thoroughly 

##============================================================================
print("here put switch_locations into switch_list")
## this is new added Thursday july 15th 2021 prevents off by one error
## it takes input of nested switch line number locations from switch_location
## and puts them into switch_list (but again not the first main switch)   

#this one just commented out
#put_switch_locations_into_switch_list()
print("about to test it with the loop thru switch method ====")
print("today is july 22nd, 2021 thursday refining the algorithms and methods")
## calling LOOP THRU SWITCH LOCATIONS (INNER)

######======================
#loop_thru_switch_locations() #where to find the inner switches to replace with a nest method
######======================


print("did it work=============MMMMMMMMMM----======MMMMMMMMM==========")
print("we called loop_thru_switch_locations() which calls swap_switch_to_nested_method()")
print("we should have successfully swapped out the inner switches with nested_method numbered")
print("today is july 15th, 2021 at Starbucks connecting the functions")
print(genius[0])    	
print("olympic gold medal to make it this far.")
print("==IT SHOULD BE ABOVE THIS LINE WITH THE NESTED NUMBERS METHODS INNER SWITCHES==")
print("now I need to work on copying the nested strings to a list")
print("and then taking out the nested strings from the main switch string except for switch")
    
#this one works just need to test it as a method above 
#str_list = coolstring.split('\n')
#print('changing line 11')
#str_list[10] = "\t\t\tnested_switch_1(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)

#print(string_change)
#stringname = string_change
#############
#str_list = coolstring.split('\n')
#str_list[18] = "\t\t\tnested_switch_2(n)"
#coolstring = "\n".join(str_list)
#print(coolstring)


#what if I go thru a list to make teh changes
#=====================================================
#z = 'test4'

#choose to 'Update Now'
# when the newest “MacOS Mojave 10.14. 6 Supplemental Update”

#say we add it to first case 2nd line after case just bump down whatever
#is on that line. copy that line just for saftey and add it to the tail
#with \n at beginning and end of that line


### look for nested switch called    switch_nest()  
# get case number which case is it, first, second, third for this test
#then get line number of case section determine what line it's on.
#(the nested switch method)

output_string_test='''
 switch(x) #main switch    #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("this is the first case in the main switch")
            #switch_nest() #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')   
                     
        if case == "two":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word') 
            
        if case == "three":
            print("this is the first case in the main switch")
            print("out of from innerswitch1 below")
           
            
'''

######## testing 2nd and 3d level deep nested switch cases july 29th, 2021


# will mess around with this later. 

triple_nested_switchtest ='''
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

answer=triple_nested_switchtest.count("endswitch")
print('counting the nested switches to see how it goes ====Boo ')
print("the number of nested switches based on endswitch=",answer)
for line in triple_nested_switchtest.splitlines():
    print(line)
print("=== the end ====")
print("================")

#answer we seek is case section 2, line 2
################===============================
#33 june 28th, 2021 9:26 pm now 

#where I detect the nested switch  location and starting and ending point
# I copy the nested switch and delete it from the main switch
# I add a method where thes switch word is.
# My compromises to get it working faster are the nested switch
# must end with endswitch  and not a curly brace
# this makes it easier to get working and aids readability

#the switch main switch is chopped off at the begining of the inner switch
#the bottom after the nested switch ends with endswitch is copied
#to the top half but only after the nested method is added to th eline
#where the nested switch was 



# when code is running there is nothing to see.
# If we have moving behavior (which is invisible)
# that is what matters -but like what Fred Brooks says
# software is invisible. So I need to make it tangible and visable.

#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========



# starting testing here to see if I can reduce the code to make sense

 ####### august 10th 2021 testing commences.
# first switch at 1 tab, nested switches at 3 tabs 
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
					switch(exp){
						case 'blable':
							print("do something")
							print("yep")
						default:
							print("what the")
					endswitch #party time 
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch # 27 this is key here =============line 20 end of nested switch ====
			print('taught me how to write code')
			fallthru
			
		case 8 to 10:
			print('mocha blast')
			switch(exp){   #34  ===  beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch # 44  this is key here =============line 20 end of nested switch ====
			print('== 31 flavors===')
			fallthru
		case 11 to 15:
			print('sooo smart')
			switch(exp){   #49  === line 10 beginning of single nested switch ======      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch # 55this is key here =============line 20 end of nested switch ====
			print('== chilpaltah ===')
			
		default:
			print('the end')
}
'''	
print("what we are starting with the switch with a nested switch")
print(find_nested_switch_game)
print("=====================")
#oh wait this needs to be the input C style switch that I search in
#maybe I need to go through the case list palmtrees
# so get line number of switches
#get linenumber of each case to determine which case section the inner switch is in
pacman=[]
pacman.append(0)


coollist=[]
print("this gets the line number of the line that the case starts")
print("that has the nested switch inside THIS Case")

endnestedswitchline=[]
endnestedswitchline.append(0)
#########################################
##  get_case_line_numbers(string_name):
#########################################
def get_case_line_numbers(string_name):
    linecounter =0
    casecounter = 0
    print('get line number of each case section')
    #just get first case line numbers print it
    for line in find_nested_switch_game.splitlines(): #be sure to put stringname.splitliens()
        #this looks for cases
        if "case" in line:  #grabs first line
            print(line)
            pacman.append(linecounter)
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
        #if "switch" in line:
    print("case line numbers",pacman)    
    #print(pacman[2])  
    print("number less than 10 that ")
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
            print(item)
            print("this must be the answer of the case that is on line 8")
            break #so after just the first one
    #get largest number in list
    print("this is new trying to get largest number only from list")
    superman = max(coollist) #worked June 28th MOnday 2021
    print("largest number =",superman)

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
            print("we have a match")
            print(line)
            #linecounter += 1 if it's endswitch don't add one
            print(linecounter)
            endnestedswitchline[0]=str(linecounter)
            break
        else: #this looks for the  switch word
            linecounter += 1   
            continue
    print("the end of this nested switchis",endnestedswitchline[0])
    print("====should be 18 ====")

#calling method above this 
#####=========
#get_end_of_switch_line_number() #puts it into endnestedswitchline[0]
#####=========

#and we know that the case number is 8
#and we know that the nested switch starts on line 10
#therefore we subtract 10-8 = 2
#so within the case the nestedswitchmethod will be on line 10 or the 2nd line within the case
###############=======================########################
print("copy inner switch")
#first trying to copy the inner switch and put it into a list

linecounter=0 #this looks for the line number of endswitch for the nested switch
print("testing getting a copy of nested switch")
### what I need to do is grab the numbers that I generated that I am using below
### I determine the line number that the first and only nested switch is on
### I then look for the first "endswitch" after the nested switch starts
### and it must be within the bounds of the case that it is residing within.
#here I am feeding it but I need to make it a method
########################################################################
start  = 10  #hard coded beginning of nested switch
finish = 20  #hard coded end of single nested switch 
## COPY A NESTED SWITCH  === this copies it. it doesn't skip it but I can modify it to skip
############################
start_and_finish=[]
start_and_finish.append(0) #position [0] #ignore
start_and_finish.append(start) #position [1]
start_and_finish.append(finish) #position [2]
#so we have
start_and_finish[1] = 10
start_and_finish[2] = 20
#############################
r=find_nested_switch_game
#linecounter=0
makeitwork=[]
makeitwork.append(0)
## function copy a nested switch()   ==== I just put this into a function

###############################
## copy_a_nested_switch(r):   # what this does is copy one nested switch 
###############################
def copy_a_nested_switch(r):  #copy just one nested string 
    print("=====copy_a_nested_switch() called======")
    print("=====copy_a_nested_switch() called======")
    print("=====copy_a_nested_switch() called======")
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
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
    print(":the result COPY OF NESTED SWITCH time 10:40 am Wednesday joy ")        
    print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner

print("copy a nested switch here")
print("copying a nested switch today 1")
print('test 1 today fireworks time coffee 1')
print("the big string with a nested switch we will copy")
print(find_nested_switch_game)
print('about to call copy_a_nested_switch()')
#######========================================
copy_a_nested_switch(find_nested_switch_game) #this gets put into r as a parameter
#######=========================================
print("this should show lines 10 thru 20 for copying the inner switch star trek beam me up")
print(makeitwork[0])

print("now we will reduce the inner switch to just the switch word on line 10")
print("this should reset it to make it work properly - need to see what the machine sees")




ibm=[]
ibm.append(0)

###  SKIPPING SOME LINES (INPUT STRING, START LINE NUMBER, FINISH LINE NUMBER)
##========================================================================
#####  S K I P P I N G      S O M E      L I N E S  ############
##========================================================================
def smart_skipping_some_lines(x,start,finish):#start line nest switch and finish  endswitch
	smart = x; counter=0; concatthis =''; #finish = finish + 1 
	print("x=",x,"start=",start,"finish=",finish)
	for line in smart.splitlines():
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		if counter > start and counter <= finish: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish 
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			continue	

	ibm[0] = concatthis	  #this has the switch string with the nested switch cut out

#try it here 
start=10
finish=20
print('test 2 today fireworks time coffee 2')
print("testing reducing an inner switch to just the switch word see if this works")
smart_skipping_some_lines(find_nested_switch_game,start,finish)
print(ibm[0])



#so put in pairs and called smart_skipping_some_lines bottom up for each set of pairs
#see if it works
#first I need to get the LOCATIONS of switch and endswitch put them into a list smart
#Which I already figured out!! Then put them into pairs into a LIST of sublists brilliant




# november 10th, 2021 solving it 	
# if multiple I make the pairs 10,20 as example and then change them bottom up
# that should work. so the numbers will be correct and the integrity of the line numbers will 
# still be correct
#this way I can reuse smar skipping lines as long as I put the output into a list so it's changeable.



	
start_and_finish=[]
start_and_finish.append(0) #position [0] #ignore
start_and_finish.append(start) #position [1]
start_and_finish.append(finish) #position [2]
#so we have

#####===================================================
### take_out_this_switch_body_leaving_just_switch_word








##reduce_inner_switch_to_switch_word(r)
#=======================================
#skip between 10 and 20 which means not between 10 and 20
#this takes out the body of one nested switch leaving the switch word. 
def reduce_inner_switch_to_switch_word(r):  #copy just one nested string 
    print("=====reduce inner switch to switch word only() called======")
    innerswitch=''
    #need to skip the first switch though so take out the first number from list
    #global linecounter #this is new july 15th, 2021
    linecounter=0 #where do start and finish come from ...oh  above, put into a list
    print("it sees for start",start_and_finish[1],"and finish",start_and_finish[2])
    for line in r.splitlines(): #if linecounter is between start and finish
    #this should copy a full (every line) of a nested switch from switch to and including endswitch
        # if lincounter >= 10 and linecounter <= 20; #this is what it means
        #skip greater than 10  and > 20
        if linecounter > int(start_and_finish[1]) and linecounter  <= int(start_and_finish[2]):
            #innerswitch += line + "\n"  #it's concatted to innerswitch string right here
            #simply do nothing 
            print("in the inbetween to skip 11 thru 20 actually")
            linecounter += 1
            continue
        else: #this scenario is if not in that condition above between 10 and 20
            innerswitch += line + "\n" 
            linecounter += 1
            print("copies these lines here")
            continue
    print(":the result COPY OF NESTED SWITCH  ")        
    print(innerswitch)  #this is the copied string between lines 10 and 20 
    roadrunner = innerswitch
    makeitwork[0] = roadrunner


#linecounter=0
makeitwork=[]
makeitwork.append(0)

start_and_finish[1] = 10
start_and_finish[2] = 20
#############################
r=find_nested_switch_game
print(r)
print('now testing skipping inner switch and only leaving switch word where inner switch body was')
#######========================================
reduce_inner_switch_to_switch_word(find_nested_switch_game) #this gets put into r as a parameter
#######=========================================
print("this should show lines 10 thru 20 for copying the inner switch star trek beam me up")
print(makeitwork[0])




#lines 1 thru 9 
 #this looks for the line number of endswitch for the nested switch
print("testing getting a COPY TOP HAT OF MAIN SWITCH")
print('this also grabs and displays the inner switch first line')
#the inner switch needs to be the last line of this string
##================================================
start = 1 #starting from 11 not 10
finish = 10
#linecounter=0
abovenestedswitch=''
print("this was put into a function on July 15th, 2021 ===")
####################################
## copy_top_hat_of_main_switch(): #this grabs the string of the main switch above 
# the first nested switch in this case there is only on 
####################################
terriblysmart=''
def copy_top_hat_of_main_switch(): #this is grabbing the top of 
    #the switch case just above the first nested switch 
    print("======copy top hat of main switch()====")
    global abovenestedswitch
    linecounter=0 #string name find_nested_switch_game
    for line in find_nested_switch_game.splitlines():
         # between >= 1 and <= 10
        if linecounter >= int(start) and linecounter <= int(finish):
            abovenestedswitch += line + "\n"
            linecounter += 1
            continue
        else:
            linecounter += 1
            continue
    print(":the result copy above  first nested switch case ")        
    print(abovenestedswitch)
    terriblysmart = abovenestedswitch

#copy_top_hat_of_main_switch()  #not called yet

print("end of copying top half above nested switch ")  
print("it should end with switch which we will edit")


####################
#replace switch

#linecounter= 0
newlist=[]
newlist.append(0)
#newlist[0]
# I just put this into a function to have control over it 
#COPY COATTAILS BOTTOM OF BIG SWITCH AFTER NESTED SWITCH END
################################################################
## copy_coattails_bottom_of_big_switch_after_nested_switch_end():
################################################################
def copy_coattails_bottom_of_big_switch_after_nested_switch_end():
    print("copy_coattails_bottom_of_big_switch_after_nested_switch_end()")
    linecounter=0
    start = 21 #INPUT PARAMS TO GRB need to put these in a list for efficiency
    finish = 32
    outerswitch=''
    for line in find_nested_switch_game.splitlines(): #string looping thru
        #   IF BETWEEN line numbers 21 and 32 
        if linecounter >= int(start) and linecounter <= int(finish):
            outerswitch += line + "\n"
            linecounter += 1
        else:
            linecounter += 1
            continue   
        
    print("testing getting a COPY COATAILS BOTTOM OF BIG SWITCH")
    print(outerswitch)
    newlist[0]=outerswitch
##===================================================





#this is turning code into a function on july 15th, 2021
#######======
#copy_coattails_bottom_of_big_switch_after_nested_switch_end()
#######=======





#here is where i make this temporary list that I will put the
#input strings of the main switch and the one nested switch for testing

inputstringswitches=[]

###################
##    swap(a,b)
###################
def swap(a,b,c): #c = starbucks[1]
    cooler =c.replace(a,b)
    return cooler #starbucks[1] =string with changes made
    
    
  
#this puts the nest_method on the line selected in the tophalf of the string
#################################
## swap_switch_for_nest_method(n)
################################# 
def swap_switch_for_nest_method(n): # I will add more values later perhaps 3 or 4 for coordinates
    global abovenestedswitch
    abovenestedswitch=terriblysmart
    print("called swap_switch_for_nest_method(n)",n)
    abovenestedswitch = abovenestedswitch.replace("switch(exp){","nested_switch_" + str(n) + "(n)")
    print(abovenestedswitch)
    print("===================")

#june 29th, 2021


def scan_input_string_for_number_of_switches():
    print('work on this')#I have this figured out now elsewhere
    
    
#commented this out on august 3rd testing making big method 
   
#this needs to be put into a method and called below actually
def fishfood(): #necessary testing that's all
    print('about to try new swap method')    
    swap_switch_for_nest_method(2) #feeds it the number 2 for testing
    outerswitch=newlist[0]
    outerswitch= makeitwork[0]
    maybe=abovenestedswitch + outerswitch
    print('we have stripped the nested switch from the main switch')
    print("and inserted a method for now")
    print(maybe)
    ######### put first main switch into inputstringswitches
    print("adding main switch and nested switch taken out into list")
    print("the next step will be to run it thru the silve_module")
    print(" to create teh strings output in python")
    inputstringswitches.append(maybe) #should be position 0

    print("and the nested switch is here before it's converted")
    print(makeitwork[0]) #roadrunner
    #roadrunner = roadrunner.replace("endswitch","}")
    ######### put nested switch into inputstringswitches
    inputstringswitches.append(makeitwork[0]) #should be position 1
    print("====== go for the gold =======")
    print("this shows the resulting strings accessed thru the list that")
    print("they were put into so I can access them now for running silve module")
    print("==--------------==")
    print("here is the result now")
    print(inputstringswitches[0])
    print("now the nested switch")
    #print(inputstringswitches[1])
    galaxy=''
    galaxy = inputstringswitches[1]
    print(galaxy)
    print("Now I replace endswitch with }")### replace endswitch with }
    inputstringswitches[1] = galaxy.replace("endswitch","}")
    print("now looking into inputstringswitches[1] endswitch should be gone")
    print(inputstringswitches[1])
    print("==== end of first major step ==in process of transformation ==")

#################===========
#fishfood()
#################===========






#############################
##  get_inner_switch_line()
#############################
def get_inner_switch_line():
    print("can we get serious here I mean really")       
    bronze=0     
    linecounter=0
    secondswitchline=0  
    for line in find_nested_switch_game.splitlines():
        if "switch" in line: 
            print(line) 
            linecounter += 1 
            print("switch line number = ",linecounter)
            secondswitchline = linecounter
            break
        else:
            linecounter += 1  
            continue
    print("line with inner switch =",secondswitchline)
    print("==================")
#the inner nested switch will obviously end within the same case it starts in.
print("testing to get inner switch line number oct 12 tuesday")
###########==============
get_inner_switch_line()  
###########===============


                
###########################################################
print("")
print("====")
print("")
print("get line number of each switch")
print("each number after first switch is a nested switch")
print("get the line number of each switch")
switcharoo=[]
switcharoo.append(0)

linecounter=0









#######################################
##  get_number_of_nested_switches():
#######################################
def get_number_of_nested_switches():
    print("get_number_of_nested_switches()")
    linecounter=0
    #this looks for the line number of 2nd switch for now more later  
    for line in find_nested_switch_game.splitlines():
        #this looks for cases
        if "switch(" in line:  #grabs first line
            print(line)
            switcharoo.append(linecounter)
            
            linecounter += 1
            continue  
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
              
            #if "switch_nest()" in line:
            #   print(line)
    print("line number of switches",switcharoo)  
    print(switcharoo[2])                

casecounter=0
case_count=0

##########========================
#get_number_of_nested_switches()
##########========================
###############################################################
################ testing call of these methods at once
###========== august 3rd test Tuesday nice air conditioning ====
def nested_switch_trapeze_tricks():
    print("==== nested_switch_TRAPEZE_tricks() called=====")
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
#nested_switch_trapeze_tricks()
#print("end of running nested_switch_trapeze_tricks() Gee what does it do")

####=============================== end of the line here==========



################################
## get line number of cases()
################################
def get_line_number_of_cases():
    print("get_line_number_of_cases()")
    for line in find_nested_switch_game.splitlines():
    #get each case number 
    #check if switch in it
        if "case" in line:  #grabs first line
            case_count += 1
            print("case_count=",case_count)
            print(line)
        
            casecounter += 1
            linecounter += 1
            print(casecounter)
        else: #this looks for the  switch word
            
            linecounter += 1   
            continue
     
#answer 2nd case section    
#nested switch on line 10        
 #answer line 2 inside of case
 #case section 2 starts on line 8
''' OUTPUT
 get line number of each case section
		case 1 thru 3:
1
		case 4 to 7:
2
			case blable:
3
			case more:
4
		case 8 to 10:
5
case line numbers [0, 2, 8, 11, 14, 23]
Line 8 is case second section
We therefeore know that if switch is on line 10
then switch is on the 2nd line after the case section starts

====

get line number of each switch
each number after first switch is a nested switch
get the line number of each switch
	switch(exp) {  
			switch(exp){
line number of switches [0, 1, 10] <<<=== line 10 nested switch
'''
'''
 print('kangaroo hop hop!')
			switch(exp){
			case blable:
			   print("do something")
			   print("yep")
			case more:
			   print("nice")
			default:
			   print("we are done here")
			}'''  
    
    
    
#Monday june 28th, 2021 thinking
#get switch line number and case it's in and line number inside of case
#and what line the switch ends with }
#which I need to know to copy it. I can set the loop to start
#on a particular line and to concat a string and stop
#after coping a set number of lines. 
#Based on line count between switch and } which I can do first
#if line.startswith("switch") do until line startswith("}")




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






   
#def fantastic(): #we would know case number and therefore line number
#   newcounter=0
#  for line in output_string_test.splitlines():
#       if "case" in line:
 #          line_number.append(newcounter) 
       
       #and
       
       #I think that for the parser thats analyzing the input string
       #but the outoput python is quite different.
       #the nested method will be one line
       #so it's really  just adding the one line string
       #to a set of say 5 lines and moving the existing lines down 1 line
       
   #say second line after case 
   #test if something on that line
   #inner_switch_1('test7')
print("what can I do with lists")
print("the night is still young. competing with harvard and stanford")
red=[]
orange=[]
blue=[]
pink=[]
pink.append("\tempty")
red.append("\tone")
orange.append("\tdam")
blue.append('\ttuna')

super = pink[0]  + '\n'  +red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)
red[0] = "\tnestedswitchmethod" 
pink[0]= "\tfunny"
super = pink[0]  + '\n' + red[0] + '\n' + orange[0] + '\n' + blue[0] +'\n'
print(super)

print("========")
line_1=[]
line_2=[]
line_3=[]
line_4=[]
line_5=[]
line_6=[]
line_7=[]
extra_line_1=[]
extra_line_2=[]
extra_line_1.append(0)
extra_line_2.append(0)
football =[]
football.append(0) #method name 
football[0]="\tinner_switch_1('test4')"

line_1.append(0)
line_2.append(0)
line_3.append(0)  #for example nested switch is line 3
line_4.append(0)
line_5.append(0)
#line_6.append(0)

#line_7.append(0)
 #say it's 4 line case 
line_1[0]="\tprint satement line 1"
line_2[0]="\tprint satement line 2"
########################################
line_3[0]="\tprint satement line 3"
line_4[0]="\tprint satement line 4"
print("================")
#if it's on line 3 we take top off to separate it 
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
# new
print("beginning state")
extra_line_1[0]=line_3[0]
extra_line_2[0]=line_4[0]

print("copying that will be don")
print(extra_line_1[0])
print(extra_line_2[0])

print("====bit flipping==== ")
print("putting nested switch in position 3 which is line 3")
line_3[0]=football[0] #designated line for nested switch 
line_4[0]=extra_line_1[0] #this is a novel approach restarting from 1
line_5[0]=extra_line_2[0]

print("after adding the switch nested method in position 3")
print('we then have this:')
print(line_1[0])
print(line_2[0])
print(line_3[0])
print(line_4[0])
print(line_5[0])
print("=========== now adding teh strings to magic concatting them ")
magic=''
magic = line_1[0] +"\n" +line_2[0] +"\n" + line_3[0] +"\n"+ line_4[0] +"\n" + line_5[0]
print(magic)  
print("=====================")  
print("let teh games begin")    
print("done")
#line_5[0]="line 5"
#line_6[0]="line 6"
#line_7[0]="line 7"
#line_8[0]="line 7"
mylist=[]
mylist= ["starter","one","two","three","four","five"]

def sosmart():
    mylist.insert(0,"starter")
    mylist.insert(1,"one")
    mylist.insert(2,"two")
    mylist.insert(3,"three")
    mylist.insert(4,"four")
    mylist.insert(5,"five")
    
    
    
def put_nested_switch_into_line(x):
    mylist.insert(x,"nested_switch") #it replaces the whole line
    print(mylist)
    
    
    
def reset_list():
    for item in mylist:
        del item
    
    print(mylist)

print("333333333333======333===================")
print("new attempt here  Friday June 25th -0--")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

print("======= water tower see how well this works=======")
print(mylist)
put_nested_switch_into_line(2)
sosmart() #resets it
put_nested_switch_into_line(1)
sosmart() #resets it
put_nested_switch_into_line(3)
sosmart()
print("===000000000000100000000000======")

# I ahve to split it in half somewhere and we have top above nested switch line
#and then we have the nestline
#and we have the bottom 

#so if we have lists for each line number of case section up to say up to 10 lines for now
#say switch will go on line 3 of 6 lines for an exmaple
#line 1 and line 2 are top
#line 3 is nest_switch_method
#line 4 to n is the bottom




     
case_guts='''
\tprint("aaaaaa in the main switch")
\tprint("bbbbbb below")
\tprint("ccccc#result of innerswitch running
\t#what ddddddd?? use a list to capture it
\tfallthr eeeeeeeu('word'
'''
    
    #method inner switch withnumber (input will likely be from a list later)
add_this="\tinner_switch_1('test4')\n"
nested_method_name=[]
nested_method_name.append(add_this)
crystal=[]
crystal.append(0)# [0]


#get input string of case section
#
# I need to get the line number where the switch is supposed to go
# based on the input C style location of the nested switch
# based on which case it is in (the sequence starts from 1)
# then detect the line number in order within that case where the switch starts
#
#
  
#exmaple, we need to add nested switchmethod to line 2
#so we copy line1

top=[]
middle=[]
bottom=[] 
put_in_here=[]

#### fudge ########    
def fudge():
    #def copy_one_line_inside_case(x)
    astring=''
    soupstring=''
    line_counter =0
    print(case_guts)  
    
    print("===========STAGE 1=========")  
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == 1:  #grabs first line
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print('first line string=',astring)
    #################
    newstring=''
    coolstring=''
    line_counter =0
# copy from the line where we want to insert (line 2) 
# thru to last line in case section
    print("============STAGE 2===========")
    #this copies 2nd string to string n (the rest)
    
    for line in case_guts.splitlines():
        if line_counter >= 2:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
        
    print(newstring) #this copies all of the lines into newstring
    put_in_here.append(newstring)
    #this is the switch method string on top of rest of case body lines
    #copy from targetline insertion line thur last line
    # we then add the nested switch method to the rest of the case 
    ##########################################
    #this will be a new helper method
    
    #def add switchline to rest of case body()
    #this is necessary BEFORE adding first line
    print("=================STAGE 3=================")
    egg=[]
    nested_switch_method_name=[]
    fossil=[]
    #fossil.append(0)
    #fossil[0] = nested_switch_method_name[0] + put_in_here[0]
    coolstring = add_this + newstring#how so I insert to front of a string
    #higher =nested_method_name[0] + put_in_here[0]
    egg.append(coolstring) #egg[0]
    
    #middle.append(coolstring)
    print(coolstring)
    glory=''
    #this adds the first string followed by coolstring
    #########################
    #this adds the line(s) above the insertion line 
    #put first string ontop of rest of lines of 
    #this adds the first line which was skipped to the new switch line
    #with the rest of the case body
    
    
    #def add_top_above_lines_above_switch_line(a,b)
    #a = string with the switch_method name
    #b = rest of the lines
    print("==========STAGE 4==========")
    nested_switch_method_name.append(astring)
    glory = astring + coolstring#[0] #now it's a list
    print("glory shows")
    print(glory)
                #method name in list     #nested method name + rest of lines in case
    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
    print('from list now') #string add_this
    print(egg[0])
    #bottom.append(glory)
    #print("now printing from the list bottom[0]")
    #print(bottom[0])
#   def add

#then replace first line with new line methodnested name
#    then add paste first line to new beginning of string
print('copy string from line 2 bbs')
fudge()
#now I can insert in line 2

print("========= result of fudge  ============ ")
print("========= Fudge Happy Potter Hogwarts ========")

#convertList = ' '.join(map(str,list1)) 















###################################
## copy one line inside of case (x)
####################################
def copy_one_line_inside_case(x):
    astring=''
    soupstring=''
    line_counter =0
    #print(case_guts)    
    #this copies just the first line to astring
    for line in case_guts.splitlines():
        if line_counter == x:
            astring += line +'\n'
            line_counter += 1
            break
        else:
            line_counter +=1
            continue
    print(' line',x,' string=',astring)
 ####################   
 #copy just the line entered within the case body
copy_one_line_inside_case(1) 
copy_one_line_inside_case(2)
copy_one_line_inside_case(3)
copy_one_line_inside_case(4)
copy_one_line_inside_case(5)






#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========








################################################
##  get_below_after_method_insertion()
################################################
def get_below_after_method_insertion(y):
    newstring=''
    coolstring=''
    line_counter =0
    #this copies 2nd string to string n (the rest)
    for line in case_guts.splitlines():
        if line_counter >= y:
            newstring += line +'\n'
            line_counter += 1
        else:
            line_counter +=1
            continue
    print('below after method insertion',y)   
    print(newstring) #this copies all of the lines into newstring
    #this is the switchm

#this grabs lines within the case after the input line number to the end
get_below_after_method_insertion(2)
get_below_after_method_insertion(3)
get_below_after_method_insertion(4)
get_below_after_method_insertion(5)
 
egg=[]
#def stage_three(a,newstring):#("====STAGE 3====")
#    print('stage_three called')
#    coolstring = add_this + newstring#how so I insert to front of a string
#    egg.append(coolstring) #egg[0]


#stage_three(add_this,newstring)

### stage four ########
#def stage_four():
#    print('stage-four called') #method name in list     #nested method name + rest of lines in case
#    egg[0] = nested_switch_method_name[0] + egg[0] #coolstring
#    print('from list now') #string add_this
#    print(egg[0])  
    
#stage_four()    
#it's going to be in the code gen phase actually where I add the
#one line (so much easier) to the particular case that it's in
#and on the line number within that case below a particular line
#But I the main switch is generated so it should have a marker
#like nested_switch_1_3('test4')
#case number in series and line number within that case

# 
# 
# x=1
# def paste_inner_switch_method_into_string(x):
#      print("===================")#this goes thru the string and detects a nested switch
#      case_counter =0
#      for line in output_string_test.splitlines():    #and copies it and puts it into 
#         case_counter += 1    #acgtaully it gets the start and stop location line numbers
#         if "case" in line:
#             print("case detected in line")
#             case_counter += 1
#             if case_counter == x:
#                 print("this should be our match")
#                 print("this is case number ",case_counter,"and x=",x)
#                 print("therefore we do the MAGIC SHIT HERE")
#                 fantastic()
#                 break
#         else:
#             continue
# 
# list1=[]
# list1.append(0)
# def test_this():
#  #put it into a list
#     list1[0]="inner_switch_1('test7')"
#     say it's line 
# 
# #possibly have it scan thru the output python generated
# I might need a marker  #comment where to put it based on
# just the case. I can finangle where in a case I add it 
# since it's just a method and after I get it placed
# then I can change where in the case it is since it's
# within the case body so I have latitude and the body case 
# will be isolated so there should be some leeway. 





happydays='''

line =""
varholder=[]
varholder.append('0')
###############################============

	
# ===== inswitch ========
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
x = "one" #it was "one"     

tahoe=[]
tahoe.append(0)

victory=[]
victory.append(0)

#######################
### inner switch_1(n):
#######################
def inner_switch_1(n): #test2 is the test
	print("=======inner_switch called==1==",n)
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']

	inswitch(n)
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
			#inner_switch_2('test7') commented out
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
###================


inner_switch_1(zoo[1]) #this calls it with zoo[1]

'''

def darkness():
    print("darkness() =========")
    print(happydays)
    touble=''
    print("darkness called=====>>>>>>>>>=====>>>>")
    print("happy days analyze the pattern for the tabs and how many ")
    counter =0
    print("===================")#this goes thru the string and detects a nested switch
    for line in happydays.splitlines():    #and copies it and puts it into 
        counter += 1    #acgtaully it gets the start and stop location line numbers
        if "\t" in line:
            print("tab detected in line")
            trouble =line.count("\t")
            print(line)
            print("tabs=",trouble," ",counter)
            trouble=''
        else:
            continue
            
darkness()
  
  
  
  
  
  
           
print("HERCULES TEST RIPPING OUT TABS FROM FRONT")   
'''
to set adding tabs i realized there are two modes
regular switch and nested switch
and to subtract a tab i need to cancel nuke tabs in a line then add the desired number
to get what i want

'''  
import re
myString = "\t\t\t\tI want to Remove all white \t spaces, new lines \n and tabs \t"
print(myString)
print("now rip out the tabs")
myString = re.sub(r"[\t]*", "", myString) #was * where I have 2
print(myString)   
print("now add a tab")

myString = "\t" + myString
print(myString)    
myString = "\t" + myString #add second tab
print(myString)              
            




#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






##### this makes the input for zoo[1] lowercase
###############################
## make_input_lower_case() ####
###############################
def make_input_lower_case():
    answer = zoo[1]
    answer = answer.lower()
    zoo[1] = answer    

# what i doing here is putting the dynamic built inners switch python code into a list.
# this is just beautiful and brilliant.

fiddle=[]
fiddle.append(0)
fiddle.append(happydays) #appends the string and puts it into fiddle[1] and exec()
#print(fudge[1])
print("TESTING BLADE RUNNER SERIES =what does an innerswitch by itself need")
print('it is all in one big string about to execute it')
#THIS IS CRITICAL INPUT IN   zoo[1]
zoo[1] = 'test3'# testing (user input lower or upper)
make_input_lower_case() #this converts the input for nested
#see if it works
print(fiddle[1])

exec(fiddle[1]) #this is executing the nested switch method above




sewage = ''
#for item in fiddle[1]:
#    sewage += item
#print("sewage=",sewage)
#print("=====")   
#x =sewage.replace("\t","\t*") #this is so I can see the tabs




samplecode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']

	switch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			fallthru('test2')

		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print ("switch case behavior works in Python now!")
			print("")
			fallthru('test3')         

		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			fallthru('test4')

		elif case in caselist4: #['test4']
			print ("testi  first nested switch ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
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



dumbstringcode ='''
	caselist1= ['test1']
	caselist2= ['test2']
	caselist3= ['test3']
	caselist4= ['test4']
	caselist5= ['google', 'fishfood', 'probability']
	caselist6= ['test6']
			
	switch(n)
	while True:
		if case in caselist1: #['test1']
			print("dam did it work?")
			print("yes it's test == one")
			tahoe[0]="victory" #puts victory into tahoe[0]
			print("")
			fallthru('test2')

		elif case in caselist2: #['test2']
			print("this is inside of inners switch test2")
			print (" case behavior works in Python now!")
			print("")
			fallthru('test3')         

		elif case in caselist3: #['test3']    
			print ("go reindeer")
			print("")
			fallthru('test4')

		elif case in caselist4: #['test4']
			print ("testi  first nested  ol...")
			tahoe[0]="sublime" #puts victory into tahoe[0]
			#######################
			#inner_switch_2('test7') commented out
			#######################
			print("out of inner  1")
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


fridge=[]
fridge.append(0)


print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
print(" TrYING TO DO SOMETHING SIMPLE super simple")
#================================================
x =dumbstringcode.replace("switch","inswitch")
dumbstringcode=x
y = dumbstringcode.replace("fallthru","infallthru")
supergood = y
#=================================================
####### this fixes a bug of the inner switch getting an extra in and it's taken out
#######3=======
print("--------000000000000---testing changing switch and fallthru ====")
print("-------=0000000000000  into inswitch and infallthru ------")
print("testing conversion of a python string of a nested switch")
print("to tranform it into inswitch(), infallthru()")
print("this should be the working version of ")
print("have changing switch to inswitch and fallthru into infallthru")
print(supergood)
print("did it finally work or not===========>>>>>")
z = supergood  #this fixes a bug where the nested switch method is wrong
y = supergood.replace("inner_inswitch","inner_switch")
print("and this should fix the bug of accidentally namming inner_switch")
exam = y
print(exam)
print("===== end of good working code ==============")

#for line in dumbstringcode.splitlines(): #switch case in JS
 #   #print("smartcounter =",smartcounter)
 #   
 #   if "\t\t\tswitch" in line:
 #        umbrella += "inswitch(n)\n"
 #   if "fallthru" in line:
 #       umbrella += "infallthru(
 #       
 #              
       #this is the range I want to print



#this is where the swo string is I was looking for.

print("july 3rd test 2021 6:53 pm")
print("testing nested switch string BETA TESTING ====0")
#find_nested_switch_game ='''
#clever('4')
swo ='''
	switch(exp) { #first true test 
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){     # inner s w i t c h      
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
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


#this one has two nested switches that I will try next. 
swo_next ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			switch(exp){   # inner s w i t c h     =============  
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch #=========================
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			switch(exp){   #this is new 28    ===============   
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #38===================================
			fallthru
		
		default:
			print('the end')
}
'''	
# I seem to recall a bug usin

#this is testing sensing a multiline switch with more than one switch
####===============
#testing moved here for safety
# CHECK FOR THE NUMBER OF SWITCHES WITHIN THE INPUT STRING
nested_switch=[]
nested_switch.append(0)
nested_switch[0]= False # by default
################################################################################
#determines if a string input is a nested switch with at least one inner switch
################################################################################

###################
##  jumanji(y)       tests if string input has at least one nested switch
###################  sets nested_switch[0] = True
def jumanji(y):  #instead of this I just do a count for endswitch which is just one line of code. 
	print("--------------------------")
	print(" --- J U M A N J I -------")
	print("--------------------------")
	print("this determines if it's a nested switch with a nested switch or more in it")
	print("testing jumanji() counting switches and endswitches")
	#just some sample ifs to read what's the input look like 
	print("this is looking into the string below")
	#print(swo)
	print("--- end of string that we will analyze ---")
	print("")
	print("get count of lines startingwith switch in the string")
	#this counts switch number in the string
	switchcounter=0
	for line in y.splitlines(): #determine if switch is in line
	#this looks for switch in the line but endswitch can't be in this line
		if "switch" in line and "end" not in line:
			switchcounter += 1  ## SWITCH COUNTER
			#print("switchcounter=",switchcounter)
			print("yea this starts with switch")
			continue
		else:
			continue
	print("total switches =",switchcounter)
	
	##============================
	#this counts endswitch number in the string
	print("get count of lines startingwith endswitch in the string")
	endswitchcounter=0		
	for line in y.splitlines(): #determine if "endswitch" is in line
		if "endswitch" in line: 
			endswitchcounter += 1  #END SWITCH COUNTER
			#print("endswitchcounter=",endswitchcounter)
			print("yea this starts with endswitch")
			continue
		else:
			continue
	print("TOTAL endswitches =",endswitchcounter) #endswitchcounter
	print("end of this checker ===========")
	print(" total switches",switchcounter, "and total endswitches",endswitchcounter)
	
	#this sets the flag in nested_switch[0] if at least one nested switch
	#===============================================
	#if one or more switch and one or more endswitches
	if switchcounter > 1 and endswitchcounter >=1: #actually if endswitchcounter 1 it's True
		nested_switch[0] = True
	else:
		nested_switch[0] = False
	
	print("the result of this test for if this has nested switch(es)") 
	print("this is the list with the critical nested_switch[0] value")
	print("WHAT DOES THIS SAY --  it should be True")   
	print("nested_switch[0] = ",nested_switch[0])
	print("=================")
	print("=================")
	print("this  below this is dog breath that doesn't work")
	print("====== end of this initial switch counter filter that will eventually")
	print("=== trigger bypass205 to do multiple switches ====")
	
	
#end jumanji()  ===================||	
	
jumanji(swo)  #called here to test it
print("just called jumani with swo and if nested switches below will be True")
print(nested_switch[0])
#this should be the output the nested switch copied








#this is still using endswitch they aren't swopped out yet

## July 5th, 2021  testing Monday July 5th line number 1593
# July 18 added a second nested swithch to test on lines 28 to 38
samplestring ='''
	switch(exp) {  #1
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
			switch(exp){   #28 this is new ======28       
				case 'autumn':
					print("falling leaves")
					print("sunlight from the sky")
					fallthru
				case 'winter':
					print("snow time")
					break
				default:
					print("so much creativity")
			endswitch   #======== ============38
			fallthru
		
		default:
			print('the end')
}
'''	

#######################
#### testing ######
### samplestring with switches taken out ####
#### and nested methods replacing it ########
######## july 22 ###testing #####
##### this represents the accurate main switch with proper indentation
samplestring_main ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
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
			print('== autumn nest===')
			nested_switch_2(n)   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''	


#nested_switch_2(n)
#july 21st 2021 get teh number of lines in the string
# count endsswitches to get number of nested switches
# do the main switch last which erases(skips) the nested switches
#here I count the number of lines in the string to get last line 
# the tricky part was figuring out when to grab the main switch but I couuld actually
#do it first it doesn't matterand make a copy of it and modify the copy


#so I would add a third record to the pears dictionary 1, 44
######=== total lines in the string for the main switch =========
#using the whole string I know that the nested switches will be on the first line
thecounter=0
for line in samplestring.splitlines():
    print(line)
    thecounter += 1
    
print("the total lines =",thecounter)
print("================ wile e coyote =======")





tuna ='''
	exp = '4'
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp = 'blable'
			switch(exp){  #this one has input here         
				case 'blable':
					print("do something")
					print("yep")
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			exp = 'fish' #and we have input here too. 
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
}
'''




# ibm list is used for holding switch strings 
ibm=[]
ibm.append(0)

use_number=[]
use_number.append(0) #[0]

#def between(x,condition,y):
    
#experimentatl copy the nested switch ignore the rest and only Do one.


#this only copies one nested switch within the main switch
#this i pased on knowing the input 
#these are hard coded here

#just put this here to see if it works correctly
# saturday july 17th, 10:11 am starbucks
print("STARBUCKS CRUCIAL testing saturday morning")
'''
this is first emptyhing the switch and endswitch locations lists



'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





print("the one below this line should produce 2 switches and one with 10,20")
#this find the location one one pair of a nested switch and end switch

#this gets the start and end from samplestring
#empty_switch_and_endswitch_list_locations()



#this has the output of filling these lists
#switch_location
#endswitch_location

print("stopping this now to see what it looks like with the switch list and endswitch list")
#return  # to stop the program
''' THIS IS THE OUTPUT OF RUNNING THE FUNCTION ABOVE

===  THESE ARE THE SWITCH AND ENDSWITCH LOCATIONS === 
I need to delete teh first swithc location
switch_location= [10, 28]
endswitch_location= [20, 38]
'''

print("=== shazam level about to try fancy stuff ====")

#loop
#pairlist is actually a list 
pairlist=[];theforce=[]
#this would just add the switch location
alpha='';beta ='';counter =0;jedi='';
#this reads in data from switch_location
#               and from endswitch_location

#######################
def fill_pairlist_with_switch_and_endswitch_pairs(yy): #input string in yy
    print("MASSIVE MAMMOTH TEST of creating pairs and storing in a list")
    print("this uses JEDI welder to build the pairs together ==")
    print("====fill pairlist with switch and endswitch pairs()=====")
    get_switch_and_endswitch_locations(yy) #===== using sample stringh 
    print("this is grabbing the switch locations which are dynamically added to a dictionary for pairlist")
    print("the length of switch location =",len(switch_location))
    print("the length of end switch locatoin =",len(endswitch_location))
    print("==============...............============")
    # loop thru list switch_location ==============================
    counter =0;allpha='';beta='';           #so this is one small set switch and endswitch line numbers
    for item in switch_location: #this loops thru the list switch_location          
        alpha = switch_location[counter]
        beta  = endswitch_location[counter] #they should be the same length 
        #here the positions are appended to pairlist dictionary
        pairlist.append([alpha,beta])       #always in sets of 2 #adds alpha and beta as list into pairlist  list
        print("pairlist=",pairlist)
        counter += 1
    print("======================")
    print("what is in the pairlist?????")
    for item in pairlist:
        print(item) #should look like this [number,number]
    
    print("=====================================================") 
    
    print('next test..saturday morning testing oh joy ..')
    for item in pairlist:
        alpha = item[0]
        beta  = item[1]
        print("alpha,beta=",alpha,beta)   
        
        
        
        
    newcounter=0
    print("the length of the pairs =",len(pairlist))
    #loop thru pairlist
    for item in pairlist:  #this is the combined pairlist
        print(item)
        sosmart = pairlist[newcounter] #here I access first and second numbers in pairlist
        print(sosmart[0]);print(sosmart[1]) 
        print("====== JEDI TEST ========")#not to be confused with jumanji above 
        #this takes in data from switch_location list and endswitch_location
        # and glues them together into a new pair list into 
        # list called theforce
        #this is constructing filling the data in the dictionary pair values
        jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
        print('jedi=',jedi) #like this [12,16]
        
        #I am adding this to a list but I thought that my plan
        #initially was to add it to a dictionary
        
        #this is adding to the list theeforce the pairs of switch and endswitch
        #here I am appending the pairlist into list theforce
        theforce.append(jedi) #the pair is added  to theforce list
        turbo  =theforce[newcounter]
        newcounter += 1
    print("theforce=",theforce)
    print("the length of theforce list =",len(theforce))
    print("did we make it this far... in a galaxy")
    #adding loop here to test this
    print("doing a newest test  christmas tree of the pairs in list theforce")
    acounter=0
    print("====magic brew time=====")
    for item in theforce:  #the pair of switch,endswitches are added to list theforce
        print(item)
        print("=======")
        cool =item
        print("cool=",cool)
       
        print("acounter=",acounter)
        x=''
        x = cool.split(",")  # see if this trick works
        print(x[0], x[1]) # see if this trick works
        print("end game")
        acounter += 1
        continue
    print("end of printing each item in theforce") #these should be sublists of the pairs
###=====


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def cleanse(x):
    x = eval(x)
    return x;
    
#modified this method on august 11th wednesday, 1:11pm
############################################
##     adding data list to dictionary
############################################
def adding_data_list_to_dictionary(dictname,key,newdata_list):
    return
    print("adding data list to dictionary()")
    print("LOOK AT THOSE at input params see if they are right first")
    print("dictname=",dictname)
    print(key)
    print(newdata_list)
    print(dictname,key,newdata_list)
    #return #temporarily halts this from running  ==== I had a return here killing the method
   # dictname[key]=newdata_list #maybe this will work
    thisdict["color"] = "[12,22]"
    print("called adding data list to dictionary")
    #tryit =eval("" + dictname + "[" + key + "]" + "= " + newdata_list +"")
    #tryit =eval("" + 
    #exec(tryit)
     #it should be in the dictionary now so try to access it
     
    angel =dictname
    thekey= key
    newdata_list
    print(angel)
    print(thekey)
    print(newdata_list)
    print("====>>>====>>>end of games...")
    #print(tryit) #to see what it sees
    
    #thisdict["4"] = "[12,22]" #adding data list as string to dictionary
    
    #eventually I will add 1 to dictionary length
    
    ##########################################
    #dictname + key + [12,22] input format 
    ##########################################
    #dictionary name should be known
    print(thisdict)
    for item in thisdict.values():
        print(item)
    print("testing getting value in dictionary by key")
    x = thisdict["color"]
    
    #x = thisdict.get("4") #this should work also
    print(x) #together
    x = eval(x)#just dreamed this up and it worked
    print("this represents getting the x and y for a nested switch locations")
    print("first number",x[0])#seperate
    print("second number",x[1]) #separate
        
#OUTPUT
'''
called adding data list to dictionary
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, '4': '[12,22]'}
Ford
Mustang
1964
[12,22]
testing getting value in dictionary by key
[12,22]
first number 12
second number 22
'''
print("fast wile e coyote test  adding data list to a dictionary")
print("==========")
print("==========")

#adding_data_list_to_dictionary(thisdict,'5','[12,22]')

print("now we will test trying to access what I just added to dictionary")

#y=thisdict['5']
print("y=",y) #should be [12,22]

def testing_pair_list():
    print("====testing pair list ==does it work babe ==")
    print("====testing pair list ==does it work babe ==")
    print("====testing pair list ==does it work babe ==")
    print("====testing pair list ==does it work babe ==")
    print("====testing pair list ==does it work babe ==")
    print("======testing pair list() == fireworks time in tahoe ====")
    print("theforce[0]=",theforce[0]) #first pair coordinates start stop
    print("theforce[1]=",theforce[1]) # second pair coordinates start stop
    print("===starting loop thru list theforce =======")
    newcounter=0
    print("dog breath test")
    for item in theforce: #list of pairs just filled 
        print(item)
        #this only works for two numbers 2 number long currently
        dog = theforce[newcounter] #here I access first and second numbers in pairlist
        x = dog.split(",")  # see if this trick works
        print(x[0])
        print("doing surgery cutting off first character")
        charlie=''
        charlie = x[0]
        super=x[1]
        print("super=",super)
        print("=====")
        charlie = charlie[1:] #cuts off first one
        print("charlie =",charlie)
       
        super =super[:-1]     #cuts off last one
        print("super=",super)
        print("===...=.=.=.=.=.=.=.=.=.=.")
        print("===...=.=.=.=.=.=.=.=.=.=.")
        charlie=''
        charlie = x[0]
        charlie = charlie[4:]
        print("charlie =",charlie)
        #print(x[1])
        print("==========")
        newcounter += 1 #python doesn't have ++
        
    print("=== end of looping thru list =======")
    
    
print("MAJOR TEST august 7th, 2021 morgan hill starbucks mocha time")    
print("testing this dam code again...")    

#=======================================================
## this makes the pair list for locations of nested switches august 7th, 2021 
print("DOING TEST of PAIRS of switch and endswitch necessary to do copy and skip comamnds")
print("===================== big test today wednesday =========")
print("what this entails is the mechanics of switch and endswitch locations")
print("which need to be dead on to work correctly for separating the nested strings")
print(" ---- THIS MUST WORK DEAD ON --- for the show of separating teh strings")
print("  --- so this creates the information needed to correctly separate the strings")

print('-------------gas moneky garage test-----------')
print(" === puff the magic dragon time here august 11th ===")
fill_pairlist_with_switch_and_endswitch_pairs(red_robin)
print("we are outside of starbucks coding in the car for concentration and productivity")
testing_pair_list() #this shows the outpout of grabbing the switch
# and endswitch pairs (sets)
#this way I can use the pair list to copy the nested switches
#========================================================

#print("oh wow does this actually PEAR TREE SHAKE  work pairlist below")
#print("number of pairs =",len(pairlist)) #this is beautiful!!!

#print("oh wow look at this pairlist I made=== starbucks mocha===...")
#print("the length of pairlist =", len(pairlist))
#print('after first attempt')
#sosmart =pairlist[0] #first position
#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])




#print("====== JEDI TEST ========")
#this is constructing filling the data in the dictionary pair values
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#this is building a pair [4, 8]   #an example 

#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)
#theforce.append(jedi)


#print("I simply add the jedi string which is a list (brilliant)
#print("to theforce list sooo nice")
#make a method here 

#fill jedi with one set 
#print("=======NEXt JEDI TEST ======")
#sosmart =pairlist[1] #second position meaning second nested switch 


#print("wow will this work >> that would be so cool")
#print(sosmart[0])
#print(sosmart[1])
#x = 10
#y = 20
#jedi = "[" + str(sosmart[0]) + "," + str(sosmart[1]) + "]" 
#print("celebration time it almost works completely fireworks")
#print('jedi=',jedi)

# feed jedi set of 2 numbers into the forcelist with an append
#was theforce
#theforce.append(jedi)

#print("theforce=",theforce)
#print("the length of theforce list =",len(theforce))

########################
#print("the =========== force here ========force shows",theforce)
#print("theforce[0]=",theforce[0]) #set one of pair of a switch start and endswitch
#print("theforce[1]=",theforce[1]) # set second pair of a switch and endswitch locations

# so this is building the pears lists of switch endswitch so then I would add the pearslist
#to a dictionary now I think. 

############













#this would just add the switch location


#I can createa  new list to make the pairs first
#go thru grabbing the first number first
#then on the second loop add the second the endswitch

#fill the pears dictionary now
#exit()


#print("switch_location=",switch_location)
#print("endswitch_location=",endswitch_location)

#what is the output???
print("snow man here ")
print("I need to have it flow into the range below lists")
#these are hard coded in here 
print("the output from get swtich and endswitchlocatin for samplestring")
print("right below this line")
print(" RODAN FLYING......")

#for some strange reason the get swithc and endswitch locations are off by 1

#switch_location[0] -=  1
#endswitch_location[0] -=  1
print("what type is it switch_location[0]",type(switch_location[0]))
#test =switch_location[0] 
#test=test-1
#switch_location[0] = test
print("switch_location now",switch_location)

#test =endswitch_location[0] 
#test=test-1
#endswitch_location[0] = test
print("endswitch_location now",endswitch_location)

##============================================================
#these are in switch_location and in endswitch_location


######################################################
list_of_switch_range=[]
list_of_switch_range.append(0)
list_of_switch_range.append(0) #was 10 hard coded 
list_of_switch_range.append(0) #was 20 hard coded

#list_of_switch_range[1] = switch_location
#list_of_switch_range[2] = endswitch_location
##############################################################
## july 17th, 2021 11:12 am
print("IS THIS WORKING OR NOT ==========")
#here we feed the input switch and endswitch into range lists
#THIS WORKS FOR JUST ONE INNER NESTED SWITCH 

nest_string='''
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
			endswitch 
'''
print("wild wild west test...")

#
'''
 this transfers the line location of switch and endswitch
 to list of switch range 1 and 2 from 
 switch_location and endswitch_location


'''
#28,38 for second string
# I am skipping using this now NOT using this method 
##################################################
##  get_one_nested_switch_start_and_finish()
##################################################
def get_one_nested_switch_start_and_finish():  # this gets the input from switch_location[0]
    print("get_one_nested_switch_start_and_finish()")
# and from  endswitch_location[0]

## this takes in the two lists of list_of_switch_range[1] and list_of_switch_range[2]
    print("=== ||=== get one nested switch start and finish line numbers")
    #force feeding it the second nested switch location input data 
    #these are hard coded for testing 
    #switch_location[0]    = 28  #july 18th testing 2nd nested switch
    #endswitch_location[0] = 38  #july 18th testing 2nd nested switch 
    list_of_switch_range[1] =switch_location[0] #force it in here
    list_of_switch_range[2] =endswitch_location[0]
    #list_of_switch_range[0]=0
    #list_of_switch_range[1]=10
    print(list_of_switch_range[1])
    print(list_of_switch_range[2])
    #list_of_switch_range[2]=20


the_nest_string= fridge[0] 
#this is what has the string_with_nested_switches in it
# THIS TAKES TABS OUT OF THE ENTIRE NESTED SWITCH 









##########################################
##  take_out_x_tabs_from_front_of_line(n):
##########################################
def take_out_x_tabs_from_front_of_line(n,the_nest_string):
	print("take out ",n," tabs from front of line - of string")
	print("take_out_x_tabs_from_front_of_line(n)") #make this is into a method 
	wildness=''
	for line in the_nest_string.splitlines(): #nest_string
		if n == 3:
			wildness += line.replace("\t\t\t\t","\t") #strips one right
		if n == 2: #this leaves 1 tab in front of each line
			wildness += line.replace("\t\t\t","\t") #strips one right
		if n == 1:
			wildness += line.replace("\t\t","\t") #strips one right
		wildness += "\n"
	print("after minor surgery see if this works")
	print(wildness)
	fridge[0] = wildness
	return wildness # this worked




#store in a dictionary each pair of switch and end switch params
# then I loop thru it with the numbers

####============ july 19th 2021  Monday ===================
# I already have the code to build a list of all switches and endswitches
# but I need to put them into a dictionary when I do that search to capture them as pairs

##================================

'''
swtich endswitch location
for trackcing hwer eto grab each nested switch

list with nestd swithc method name with number loop thru it
alist=[]
so = "10,20"
alist.append(so)

thisdict={
"brand":"Ford",
"2":alist[0],
"year":1964
}


#grab content by number
x = thisdict.get("2")
print(x)

# macro between
# put n thru m in a list
# then just this
# if x in list_of_numbers


'''

print("testing dictionary to hold switch endswitch pairs (pear tree)")
print(" ==== testing using a dictionary now ==== mayflower ship===")
alist=[]
alist.append(0)
alist.append(10)
alist.append(20)
alist.append(30)
alist.append(40)

color_table={
    "brand":"mocha",
    "Red": [10,20],
    "3": [30,40]
}

coffee = color_table["Red"][0]
print(coffee)
coffee = color_table["Red"][1]
print(coffee)
#grab content by number
#coffee = thisdict.get("2")
#print(coffee) #it should print 10,20
#print("now another one")
#coffee = thisdict.get("3")
#print(coffee) #it should print 10,20


friend1=[]
friend2=[]

thisdict =	{
  "1": [4,7],
  "2": [10,20],
  "3": [21,30]
}
for x in thisdict.values():
  print(x)
  cool = x
  print(cool[0])
  print(cool[1])
  friend1.append(cool[0])
  friend1.append(cool[1])
  print("good times")
  print(friend1)
  





### successful test for between macro ################### july 19th, 2021 ########## 

print("testing between macro and how it will work")
mylist=[]

mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

testlist =[]
testlist=[1,2,3,4,5,6,7,8,9,10]
#####################
##  between test()
#####################
def between_test(): #between macro 
#it would have to be like this
#if a between(x,y)
    print("BETWEEN TEST HERE ----")
    print("bla bla bla")
    print("between test")
    #x = 7
    print("the final outcome..")
    # if x >= switchline and x <= end switchline  #meaning  from start number thru endnumber
    #if x is between switchnumber and endswitch number
    #the list would contain the start number thru the stop mumber 
    # if x is between startnumber and endnumber:
    counter=0 #the logic is to be between x and y it's inclusive of x and y also
    for item in testlist: #so we look for a narrow range within the large input range
        if item in mylist:
            print("yes",item)
            counter += 1
            
        else:
            print("nope",item)
            counter += 1

print("=====do test of between macro proof of concept=====")
between_test() #this tests if we have a list of numbers 1 to 6

print("testing this with between")
zoo = 4
#if zoo between 1 and 6:
alist=[]
alist=[1,2,3,4,5,6]
print("======= BEtWEEN TESt ========")
print("testing the replacement for using betwen")
print("if zoo(4) is between 1 and 6")
if zoo  in alist:
    print("yes it's between 1 and 6",zoo)
else:
    print("nope",zoo)


###=========================
##   between() macro
##==========================
def between(x,y,z):
    print("between called for if x in list between y and z")
    if x in alist: #1 thru 6
        print("True yes ",x, "between ", y, " and ",z)
    else:
        print("False,",x," is not between ",y," and ",z)



print("doing between macro tests....")
between(4,1,6)
between(10,1,6)
between(0,10,25)


#also next add
##==================
##  after macro
##  before macro
##================

############## testing using  a dictinary to store
############## pears of switch and endswitch pairs

#this will be generated. but I think that
# I might have the dictionary pears already existing.

###====================== dictionary storage area =================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================
###====================== dictionary storage area ================================

#dictionary called pears
peartree = {}  


#given name peartree of dictionary
def get_value_of_key_original(x): #peartree hardcoded in
    car=eval("peartree.get('" + str(x) +"')")
    print(car)
    return car #so if it is a list it should return a list right?z

#given name peartree of dictionary
def get_value_of_key(dict,x):
    car=eval("" + dict +".get('" + str(x) +"')") #maybe
    print(car)
    return car #so if it is a list it should return a list right?z


########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists
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
    
    
def add_data_to_peartree(x,z):
    answer =''
    answer = "peartree['" + str(x) +"'] = z " #[10,20]
    print("just before exec add data to peartree")
    print(answer)
    exec(answer)
    
fool_on_hill= '[10,20]'
print("TESTING adding data to a dictionary")
add_data_to_peartree(1,fool_on_hill)
print("peartree has in its contents=")
print(peartree) 







#testing adding data record to dictionary dynamically.
#Declare a dictionary (empty) 
print("dynamiclaly add data to dictionary = DRIVE THRU ")
print("testing dynanmically adding data to a dictionary Drive Thru")
data = {'a': 1, 'b': 2, 'c': 3}
print(data)
data.update({'d':3,'e':4})  # Updates 'c' and adds 'd'
print("====after adding d and e dictioanry data======")
print(data)

fun={} #dictionary called fun
print("first the fun dictionary is empty")
print(fun)
#input values to dynamically add data for teh switch endswitch to dictionary

print("adding data to drivethru dictionary ")
print(" RED WHITE AND BLUE ")
drivethru={}
#drivethru.update('1': '[10,20]')
#drivethru.update('2': '[30,40]')
#3drivethru.update('3': '[50,60]')
#drivethru.update('4': '[70,80]')
#print(drivethru)

#zerohour=get_value_of_key(3)
#print("zerohour=",zerohour)

cherish=[10,20]
skyblue =[28,38]

def get_dictionary_size(x): #length
    shit= len(x)
    print("size of this dictionary",x," is",shit)
    print("so the result is ",shit)
    return shit;
    


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
##################################################################
print("here dynamic attempt --boo scoopy doo van does this work----->>")
dynamically_add_data_to_dictionary(fun,gold,silver)
print("3  =[42,46]")
print("4  =[50,52]")

print('after updating fun dictionary dynamically  strawberry fields===')
print(fun)
print(fun.get("1"))
rat=fun.get("1")
print("below should be 10 and 20 for the result")
print(rat[0])
print(rat[1])

print(fun.get("3"))
rat=fun.get("3")
print("below should be 42 and 46 for the result")
print(rat[0])
print(rat[1])

print(fun.get("4"))
rat=fun.get("4")
print("below should be 50 and 52 for the result")
print(rat[0])
print(rat[1])

print("==== end of adding to data to dictionary dynamically ===")
for k,v in fun.items():
    print(k, v)
    print(v[0],v[1])
    print("----------")

#modidfy this get value to use dictoinary name as parameter  
print("here we are testing get_value_of_key(dictname,keynumber)  (fun,3)")  
#note dictionary name as param MUST BE A STRING in quotes 
love=get_value_of_key('fun',3) #dictionary name and key number

print('the value of key  in fun =',love)
print("should return 42, 46")
print(love[0]) #42
print(love[1]) #46

print("testing getting the length of the fun dictionary")
golddust=''
golddust =get_dictionary_size(fun) #so I would call this before adding to it so
print("so now we can get the number for number of items in a dictionary")
print("we have ", golddust," as the length for dictionary fun")
#that I can add just the new data list [3,4] example and not think about key number
# basedon the length I just add 1 to it
print("above this line should be the size of the dictionary fun pumpkins")
######################################################################
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

def playing_with_dictionary_structs():
    print("playing with dictionary access...")
    x = car.get("model")
    print("testing getting car model")
    print(x)

playing_with_dictionary_structs()

   
#but I just thought I can have a running total in a list too
def do_something():
    print("Muppets Animal")
    result=''
    do_this_baby() # I think that the list peartree was empty when I was testing it
    print(peartree)
    print("get size of dictionary ... a test")
    #how do I determine if a list is empty
    if len(peartree) > 0:
        result= len(peartree)
        print("length of peartree =",result)
    else:
        print("peartree is empty and equal to 0")
        print(len(peartree))
    print(result)
    return result
######################################
do_something()

    


print("doing simple test here to get value of key number in peartree dictionary")
print("====Domino's Pizza==")
firstone=get_value_of_key_original(1) #its using peartree
print('the value of key 1 in peartree =',firstone)
print("does this work or not???")
print(firstone[0])
print(firstone[1])

print("=========")
secondone=get_value_of_key_original(2)
print('the value of key 1 in peartree =',secondone)
print(secondone[0])
print(secondone[1])

 #peartree['1'] = [10,20]
 #peartree['2'] = [28,38] 
    

#example getting the size of dictionary peartree    
get_size_of_dictionary(peartree)

###############################################
## dnanmically add one record to dictionary
###############################################
def dynamically_add_one_record_to_dictionary():
    #first pass go thru dictionary to determine it's current length put that into a list
    super=''
    super=get_size_of_dictionary(peartree)
    #so to add 1 to super for next record
    testtheory='[42,60]' #this is hardcoded here but testing at this stage so it's ok
    #super += 1
    #combine = firsthalf + secondhalf 
    #print(combine)
    #eval(combine)
    #print(combine) 
    peartree['3'] = [42,60] #there would have to be 4 slots already to work
    print(peartree)
    get_size_of_dictionary(peartree)
    print("now yellow big bird test =========")
    ### look here this is correct below that owrks 
    fish =  "peartree['4'] = [66,80]"
    #what I built up above needs to look like this string 
    
    exec(fish)
    get_size_of_dictionary(peartree)
    
    
    ##########################
    num = 5
    numb1 = 200
    numb2 = 280
    firsthalf  = "peartree['" + str(num) + "'] ="
    secondhalf = "[" + str(numb1) + "," + str(numb2) + "]"
    print('look here very carefully....')
    print('secondhalf=',secondhalf)
    together = firsthalf + secondhalf
    print("look at below this line does it look right GROUCH")
    print(together)
    exec(together)
    
    
    
    get_size_of_dictionary(peartree)
    #print(peartree['5'])
    print("get value of 5",peartree.get('5'))
    ###########################
    '''
    loop thru peartree:
        print(item)
    '''
    for item in peartree:
        print(item)
        
    for x in peartree.values():
        print(x)
        
    print("chocolate somores. ")
    sweet =get_value_of_key_original(1)
    print("sweet key 1 =",sweet)
    
    get_value_of_key_original(2)
    get_value_of_key_original(3)
    get_value_of_key_original(4)   
    get_value_of_key_original(5)
   

#this will be used to take in a set of two numbers switch endswitch
#to add to the pears dictionary
#### makes [24,34] from ab and returns it
#### make list with two pieces of data (ab)
def make_list_with_two_pieces_of_data(a,b):
    jedi=''
    jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail
    return jedi
    
#making peartree['1'] is not tough

#what about this
#dynamically build it [10,20]
x = 10
y = 20
jedi = "[" + str(x) + "," + str(y) + "],"  #notice it adds the comma on the tail

print("")
print(" lightning round")
print("testing dynamically creating a two slot list to add to a dictionary")
x = 22
y = 33
raz=make_list_with_two_pieces_of_data(x,y)
#this does this
#  jedi = "[" + str(x) + "," + str(y) + "]," 
print("should return [22,33]")
print(raz)



print("celebration time it almost works completely fireworks")
print('jedi=',jedi) #creates [10,20],

print("interesting test to dynamically add a record to peartree dictionary")
print("KERMIT THE FROG test riding a bicycle")
run=get_size_of_dictionary(peartree)
print("size of dictionary before adding to it ",run)
dynamically_add_one_record_to_dictionary()
run=get_size_of_dictionary(peartree)
print("size of dictionary now is ",run)
#######################################################
do_this_baby()
print("did this work or not")
print("july 20th, 2021 wow time flies")
print(peartree)
###################################################################||

#######################
peartree = {}   #this will always exist and needs to exist to work.
buton=[]   #this is the passing of the buton in track and field relays
buton.append(0) #two positions here in this inner list
buton.append(0)
########
## I need to fill the pear tree data values from after 
## I generate teh switch_location and endswitch_location lists

### PRACTICING ADDING DATA TO A DICTIONARY CALLED PEARTREE  


# test input
# this adds a datum to peartree
# this is the method to add a 
# new switch pair to dictionary peartree

#it was add_this <<=========
# now it's this
#####################################
## add_data_to_pears()
#####################################
### the dictionary name is hardcoded as peartree
# peartree is a dictionary
# buton is a list with two slots 

def add_data_to_pears(x,apple):
    print("add_data_to_pears()",x,apple)
    peartree[x]=apple  #this is where the list is added
    print(peartree)


#adding data to dictionary pears here 
 #july 21st 
 #simple var with data is a list anonymous which is what I will construct
apple = [10,20] #<<====== right here I need to produce this from the switch output
x = '1'    
add_data_to_pears(x,apple)  #feeding a new switch pair into peartree

##======
apple = [28,38]
x = '2'  #here I have to provide the number, now I can figure out what 
#it needs to be by getting the length of the dictionary and adding 1 to it.
#for th enext input of data to add to the dictionary. 
add_data_to_pears(x,apple)
##======

print('tahoe test')
print("testing getting a list out of the dictionary in terms of whats in it")
cd=get_value_of_key_original(2) #see if it returns [28,38]
print(cd)

################################################
###### TESTING FILLING A DICTIONARY ############
###############################################@

# I will nede a loop
# july 21st, 2021
#this looks into peartree for a key to return a value
# the values it put into buton[0]and buton[1]
 
# this is accessing the peartree
##############################
##  ACCESS_SWITCH_1_N
##############################
def access_switch_1_n(t):
  print("access_switch_1_n() called")
  print(peartree.get(t)) #was '1'
  one=peartree.get(t)
  print(one[0])
  print(one[1])
  #################
  # added July 21st
  buton[0]= one[0]
  buton[1]= one[1]
  print("this is looking into buton list")
  print("================//================")
  print("buton[0]=",buton[0])
  print("buton[1]=",buton[1])
  print("================//================")
  ##################
  print("I can now grab")
  print("the nest switch params")
  print("from the pear tree")
  print("to feed  copy nest method")
  print("first",one[0],"second",one[1])

#this is accessing the pears dictionary to get the data by the key
### this calls the method above   
t='1' 
access_switch_1_n(t) #accesses key 1


t='2' 
access_switch_1_n(t) #accesses key 2


###############################

# output 
'''
add_this called
{'1': [10, 20]}
add_this called
{'1': [10, 20], '2': [28, 38]}
access switch called
[10, 20]
10
20
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 10 second 20
access switch called
[28, 38]
28
38
I can now grab
the nest switch params
from the pear tree
to feed  copy nest method
first 28 second 38

'''
#<href="https://discover.cs.ucsb.edu/commonerrors/pythonerrors.html"> python common errors UC Santa Barabara</a>

########
b=''
##############################################
## ACCESSING DATA IN PEARTREE DICTIONARY #####
##############################################
def accessing_data_in_peartree_dictionary():
    print("====accessing data in peartree dictionary ==")
    print("====Accessing data  from peartree dictionary()....====")
    print("accessing keys in the peartree  which I would do with a loop later.")
    #print now accessing the dictionary that has been filled with data
    #x = peartree("1")
    print(peartree)
    x =peartree['1']  #adding data to a dictionary
    print(x)
    print(x[0],x[1])
    print("============")
    #x = peartree("2")
    x=peartree['2']  #adding data to a dictionary 
    print(x)
    print(x[0],x[1])
    print("how did it go Hogwarts after flying the car over London")
    
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    ########$$$$$$$$$$$$$$$$###################
    
    #this is where I access the dictionary
    # and call the code to get the nested swith
    # based on the switch and endswitch location params
    
    print("==== now trying a LOOP thru peartree =====")
    counter =1  #starting from 1
    for item in peartree:
        x = str(counter)
        b = peartree[x] #this was "1"
        print(b[0],b[1]) #these will always be the same 
        counter += 1
## output is correct
'''
==== now trying a LOOP thru peartree =====
10 20
28 38

'''
#this is for the numbering and access to the nested switches
# and governing them and number the nested_switches and managing it all perfectly.
#================ thursday, august 19th, 2021 solution =============================
#so with this approach number is simple 1 to n for each tab level
#only thing that I change is level depth of indentation
#so if we have main switch and then 3tab depth then 5tab depth
#level0, level1, level2
#level stands for nested switch depth
#so I can use the numbering 1 thru n for each switch
#and use the numbering system and just add the level[0] in a list
#level[0] is main 1, 2, 3, 4, 5 #nested numbering
#level[1] tab depth 5 is first level nested switch if nested within 1, 2, 3
#level[2] tab depth 7 is second level nested with , 1, 2, 3
#level[3] tab depth 9 is third level 
#def loop thru pears dictionary and call  nested switch
#==================================================================

#this calls the method above:        
accessing_data_in_peartree_dictionary()

### this would be after filling this with switch_location and endswitch_location method

print("practicing with this hardcoded input data for switch and endswitch to prove it works")
print("down at pears tree here hard coded ")
# this represents a dictionary called pears already loadded with data
#=================================================
########################
##  PEARS DICTIONARY
########################
pears =	{  #for pear tree in backyard (2 of them)
  "1": [10,20], # I can make these now 
  "2": [28,38],
  "3": [1,44]
}



#see if this works
#=================================================

##### this does absolutely nothing 
# I need to make a method to add main switch to string list
def add_main_switch_params_to_dictionary():
    print("how it will work")
    #methods count end switches
    #Take answer add 1
    #loop thru input switch string get total number of lines
    #"3" : [1,44],  #is the result
    #call method to add it to dictionary


#pears['3'] = [4,7] #example
# 

print("====dictionary pears====")
print(pears)
print("==========")
print("====dictionary peartree====")
print(peartree)

print("==== practicing with dictionary called pears ========")
#access the dictionary one key in particular to get the value
#print('pears[3] which is the key number')
#x = pears["3"]
#print("x = ",x) #this should be 4,7
#print("============")
 
 
def say_something(x):
    print("say something test here")
    print('cool[0]=',x[0], "cool[1]=",x[1])
     


print("PRACTICING LOOP THRU THE PEAR DICTIONARY WITH HARD CODED DATA FOR TESTING")
print("============")
print("== PEARS  dictionary now LOOPING THRU IT===")
print("listening to teh Beach Boys to see if it works ----")
#looping thru dictionary called thisdict
'''
for x in pears.values(): #looping thru pears dictionary holding switch and end switch pairs locations
    
    print(x)
    cool = x
    #print(cool[0])
    #print(cool[1])
    print(cool[0],cool[1])
    #say_something(cool)
    copy_one_nested_switch_string(m82)
    print("========================")
       
'''       
    




 #add item to dictionary
#pears['3'] = [4,7] #example
print(pears)
 #access dictionary
#x = pears("1")
 
 #remove item from dictionary
#thisdict.pop("model")
 
 
#now when I loop thru switch and endswithc lines
#have it fill the dictionary with the data



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





#always do one nest. Just change the switch start and stop sooo simple


## MAIN TRIGGER FOR TESTING THIS CODE OF EXTRACTING NESTED SWITCH STRINGS 
###################################################
## #this means I need to feed in the one switch location and one endswitch location
## that need to have been already figured out
nest_string=[]


##  copy_one_nested_switch_string(m82)   <<=======     this is the main trigger for the test july 18th 
##  I will need to add another paramter to determine which nestd switch is grabbed 
def extra(): # does nothing
	print("did it work??")
	
	print("#method  get_switch_and_endswitch_locations()")
	######### just commented out line below july 19th 1:10 pm
	
	#get_switch_and_endswitch_locations(m82) # presumes only one nested switch inside param would be passed here to to pass thru this is new  method call
	######## I will need to take out this method above out of this function
	######## this currenlty only takes in the first switch by design 
	#this builds a list of switch_location and endswitch_location all of them
	# but this function conpy one nested stirng ONLY USES the first switch and first endswitch
	###################################################################
	#this gets switch_location[0] and endswitch_location[0]
	print("copy one nested switch string ()")
	print("get start of nested switch and end of nested switch")
	print("#method get_one_nested_switch_start_and_finish()()")
	#get_one_nested_switch_start_and_finish() # method call 
	#this just copies the locations of switch and endswitch into 
	
	
def say(x):
	print(x)	
	
######################################################
##  def copy_one_nested_switch_string(m82,zebra,cow) bigstring,switchloc,endswitchloc
######################################################
def copy_one_nested_switch_string(m82,zebra,cow): #so I would add a param to determine which nest to grab july 18th 
	print("let's look at the input")
	print(m82)   #main string name
	print(zebra) #switch    location
	print(cow)   #endswitch location
	
	print("========COPY ONE NESTED SWITCH STRING()== called=====")
	#input_string[0]=samplestring
	counter=0		
	buildstring=''
	print("printing samplestring first")
	#print(m82)This ONLY GRABS the first position which is 0 for switch and endswitch
	#when I loop thru this in the peartree dictionary I will put the current pair into 
	#switch_location[0] and endswitch_location[0]
	######################################################
	print("WHAT ..... is in these two lists position 0 swith and endswitch")
	#print("it sees in y",y, "well how does it look")
	####################################
	print("passing the params for switch and endswion and endswitchlcoation")
	del switch_location[:] #these were passed as params that govern grabbing the right string
	switch_location.append(zebra)#input param to switch_location[0]
	print(switch_location[0])
	del endswitch_location[:] 
	endswitch_location.append(cow) #input param to endswitch_locaiton[0]
	print(endswitch_location[0])
	print("input switch_location[0]",switch_location[0]) #10
	print("input endswitch_location[0]",endswitch_location[0]) #20
	#print("what it sees in switchlocation0 and endloaction0")
	print("===========================================")
	# LOOP thru string
	#print("list_of_switch_range[1]",list_of_switch_range[1]) #10
	#print("list_of_switch_range[2]",list_of_switch_range[2]) #20
	for line in m82.splitlines(): #determine if "endswitch" is in line
		#this by default starts copying the string once line greater than 2
		#this says if counter between 10 and 20 including start number and finish number		
		#############################################
		if "switch" in line and "endswitch" not in line: #this shows just switch
			print("switch in this line",counter)
		if "endswitch" in line:
			print("endswitch in this line",counter)
		##############################################	
		#right here if counter is between min line number and max line number
		alpha = int(switch_location[0])
		beta  = int(endswitch_location[0])   
		#this loops thru string and copies lines to buildstring
		if counter >= alpha and counter <= beta: #if counter between(within) alpha and beta:
			buildstring += line + "\n" #I need to start at the 10th line
			counter += 1	
			continue
		else:
			counter += 1 #wasn't adding to counter
			continue #really
	print("the new creation concatted should be buildstring=")
	fridge[0]=buildstring  #here buildstring is stored in firdge[0]
	print("what is in the fridge[0] the nested switch copied")
	print(fridge[0]) #the copied nested string is in here  fridge[0]
	#############################################
	newstring='';cool_string = fridge[0]
	print("#method take_out_x_tabs_from_front_of_line()")
	#calls method take_out_x_tabs_from_front_of_line
	newstring=take_out_x_tabs_from_front_of_line(2,cool_string) #this is running #takes off 2 leading tabs
	fridge[0] = newstring
	print("final outcome Tron")
	print(fridge[0]) #this results in the nested switch string with  2 tabs taken off front of each line
	################################################
	# July 21st, 2021 4:16 pm Gilroy Starbucks
	#this copies the string just copied and put it into nest_string
	nest_string.append(fridge[0]) ##<<<===== right here the nested string is added to nest_string
	#this is filling nest_string with the contents of each nested string
	#then fridge[0] is added to the list nest_string
	print('get length of nest string')
	print("nest_string length=",len(nest_string))
	say("now this is what is nest_string")
	for item in nest_string:
	    print(item)
	    
	#need to delete teh first three tabs
	fridge[0] ='' #this empties fridge[0]
	#################################################
	print("copy a nested string and output it") #august 5th, 2021
	#print(nest_string)
	
print("====TESTING COPYING A NESTED STRING ======1 2 3 A  B C===....")	
print("====STAR TREK ENTERPRISE ===....")	
print("this is where I call the function to copy JUST ONE nested switch")
# july 18th I would need to add another paramter here like 2, for second nested switch 
print(" MASSIVE TEST SATURDAY MORNING SOFTWARE IN STARBUCKS==")
say("testing the copying of a string with params of start stop and string name")
copy_one_nested_switch_string(red_robin,11,33) #reads sample string here 
#output into fridge[0]

#this should just call one nested string
# I will put the loop to go thru peartree dictionary
#and call copy_one_nested_switch_string(samplestring)
#and have it added to a list


# I will need to append it 


#this calls in order these methods
'''
pears =	{  #for pear tree in backyard (2 of them)
  "1": [10,20], # I can make these now 
  "2": [28,38],
}
'''



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========




################# creation of loopstring list to hold string that will hold the nested switch string

loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
'''
#########################################
## loop thru pears dictionary
## and calls copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])
## to copy one nested switch at a time
    #it might just have to go thru once to fill pears
    # going thru a dictionary I need to designate which pair 
   
    ##########################################
    ## this loops thru the dictionary pears
    ##########################################
    print("about to loop thru pear values")
    #looping through dictionary pears 
      #say_something(cool) #this way the switch and endswitch locations are passed into the function
        ##########################################################
        ## this calls COPY ONE NESTED SWITCH STRING()
        ##########################################################
        print("about to start copy_one_nested_switch_string()")
'''

#https://www.youtube.com/watch?v=qtpxiNvGCp4
#########################################
##   copy_one_nested_switch_case_body()
#########################################
def copy_one_nested_switch_case_body():
    print("copy one nested switch case body () .....")
    print("make the impossible into reality VIKING SHIP")
    print("show WHAT the hell is in pears")
    print(pears)
    counter = 1
    # pears is a dictionary with values of start switch and end switch
    ## LOOP ######## this loops thru pears dictionary
    print("this loops thru pears list ")
    print("=====================lightning strikes ========")
    for x in pears.values(): #looping thru pears dictionary holding  switch pairs locations in an anonymous list
        print('this is number',counter)
        print(x)
        cool = x #(which is a pair thus only two values)
        print("cool=",cool)
        print(cool[0],cool[1]) #this is switch and endswitch line numbers 
        print("copy one nested switch string")
        #this uses the pair location start switch and end switch numbers
        copy_one_nested_switch_string(loopstring[0],cool[0],cool[1])  #first is 1 second is 2 
        #switch_location[0]=''
        cool='' #this resets it
        counter += 1
        print("========================")
    #end loop

###=== this goes thru pears dictionary  and copies the nested switch strings
print("=== GODZILLA Time  ===")
copy_one_nested_switch_case_body() # this calls the loop

print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)




#this is the resulting output of copying the string embedded in the main switch

holdthis=[]
holdthis.append(0)

#this swaps endswitch with }
######################################
## take_out_endswitch(stringname)  #from bottom of nested switch 
######################################
def take_out_endswitch(stringname):
	print("take out endswitch called")
	galaxy = stringname
	print(galaxy)
	holdthis[0] = galaxy.replace("endswitch","}")
	#so the whole modified string after ripping out endswitch is now in holdthis[0]
	print(holdthis[0])
	galaxy = holdthis[0] #now galaxy gets what is in holdthis[0]
	return galaxy #and this is returned
	






###===================================================
##   show_list_of_nested_strings_separated()
###===================================================
## july 21st 2021 349pm gilroy starbucks
###=== this shows the nest_string list of nested switches
#this just loops thru nest_string which has the seperated nested strings
def show_list_of_nested_strings_separated():
    print("======show list of nested strings separated=====")
    print(" == StayPuff Marshmellow Man ==")
    counter =0
    print("loops thru nest_string that we filled up in copy_one_nested_switch_string(m82,zebra,cow)")
    #this requires nest_string which is looped thru
    
    # loop thru nest_string list     to take out endswitch
    for item in nest_string: #nest_string must have refined main switch with nest methods numbered already
        if "endswitch" in item: #swap endswitch with '}'
            print("== endswitch detected ==") #should be 2 of them
            print(counter) #takes out endswitch from this current string here
            holdthis[0]=take_out_endswitch(nest_string[counter])#takes out endswitch from each string
            nest_string[counter] = holdthis[0] #voodoo magic
            counter += 1
        else:
            print("oh good") #absolutely nothing happens here
            counter += 1
                
    print("see if it fixed it here")
    print("this is showing what's in nest_string list")
    #this loops thru nest_string to show after the changes were made
    print('this should be it right here the seperated nest strings')
    print("remember that the main switch string is totally different ")
    print("printing out the nest_string list right here play baseball Yankees")
    for item in nest_string:
        print(item)
    print("==========")
print("===============================================================")
print("middle ground filler here to separate the change just made.")
print("===============================================================")
show_list_of_nested_strings_separated()
#now replace teh third string(the main string)
# this is to simulate cutting out the inner switches
## july 22nd, 2021 

####===========================================================###
####===========================================================###
####===========================================================###
print("july 22nd 2021 additions...")
###============== this is working correctly now ==========
## more_testing()
##========================================================================


######################
##  more_testing()
######################
def more_testing():
    print("=== more_testing() == charisma ===method testing ")
    #this is adding samplestring with main to nest_string[2] to see what it will look like when working
    print("let's see what is already in nest_string ===> SpaceX pretest ")
    print("to see what is in nest_string")
    for item in nest_string:
        print(item)
    print("so slow 3 which is nest_string[2] has the main string in it")
    #let'see how it looks"
    print("==== after simple test of contents of nest_string")
    print("========")
    print("here we replace it with what will be after I modify it. this is dummy data testing")
    print("finished main string with nested methods added put into nest_string[2]")
    nest_string[2] = samplestring_main # the third one - putting in a different string premade
    #this is what is different right here in the line above
    
    #testing what the stages need to look like
    #to test what it should look like but doesn't yet
    print(" now we will try it again and see how it looks ")
    print(" after changing main string boo boo ")
    #loop thru nest_string
    for item in nest_string:
        print(item)
        print("===========///======aug 22nd sunday ========")



more_testing()

####===========================================================###
####===========================================================###
####===========================================================###


### this works this takes the copied nested switch
### and sets the proper indentation for it
#so it takes out 2 really but we have to say 3
## july 17th 10:12am 2021 starbucks

#the eye opening= make a list of the methods sequence
#tuesday, August 10th, 2021 ====,,,,,,,,,,,==========




loopstring=[]
loopstring.append(0) #so we have loopstring[0] to fill now
loopstring[0]=samplestring #see if this works  #this is the mai nested string
print('big test here ')
print("loopstring[0]=",loopstring)
doves=[]
copy_one_nested_switch_case_body() # this calls the loop

print("pears dictionary",pears)
print("now empty pears dictionary")
#empty pears dictionary here works 
pears.clear() #this clear the pears dictionary 
print("pears now",pears)

show_list_of_nested_strings_separated()
more_testing()


###==========================================================

#def tab_swap(x,y):
#    replace(x,y)

########==============
#wilderness=
#def set_front_tabs(x):
#    wildness=''
#    for line in nest_string.splitlines():
#        wildness += line.tab_swap(3,1) #strips one right
#        wildness += "\n"
#    print("after minor surgery see if this works")
 #   print(wildness)






# copy line by line stripping all tabs
# and then based on if starts wwith swtich 1 tab
# if case 2 tabs
# if not switch and not case three tabs
# if endswitch one tab
# if default two tabs


#unless I make a new string _so I want to remove teh first 2 tabs only
alpha_string=''
str1=''
#for line in nest_string.splitlines(): 
#    #put line into list, del first three tabs then conver to string
#   aline = line.split() 
#    print(aline) 
#    str1 += str1.join(aline) + "\n"
#    #print(str1)
#    
#print("string now is...")
#for item in str1:
#    print(item)


 



#########################################==============
## === skipping_some_lines() ========   July 5th, 2021 ===============
#########################################
#this works for one nested switch right now
#this goes thru a nested switch and takes out the nested single switch.

### solution found for dealing with deeply nested switches
#I think that I can use this if I take out the innermost switch
## first and then it should work  
# so the plan of attack is to change(yes change) the inner most
# depth switch first
#and work back to the next level till I am at the first level of depth.


#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========

#string,start,finish
#first it will just detect one nested switch , soon it will detect many

#this loops thru a string and makes a copy of the string
# but skips over a range example lines 10 thru 20

###  SKIPPING SOME LINES (INPUT STRING, START LINE NUMBER, FINISH LINE NUMBER)
##========================================================================
#####  S K I P P I N G      S O M E      L I N E S  ############
##========================================================================
def skipping_some_lines(x,start,finish):#start line nest switch and finish  endswitch
	smart = x; counter=0; concatthis =''; #finish = finish + 1 
	print("x=",x,"start=",start,"finish=",finish)
	for line in smart.splitlines():
	#this preserves the switch word and skips the rest of nested switch body including endswitch
		if counter > start and counter <= finish: #if only between start and finish skip these lines
			#skip  #so greater than start(switch) and less than finish 
			counter += 1
			continue	
		else: #this builds the string by concatting it
			concatthis += line + "\n" #notice we add a new line at the end
			counter += 1
			continue	

	ibm[0] = concatthis	  #this has the switch string with the nested switch cut out

	
	
##########################################################################################
print("TESTING skipping_some_lines(ibm[0],skip_range[0],skip_range[1]")
print("10 thru 20 but keeping the first line on 10 which is switch")
print("then 28 thru 38 keeping first line on 28 which is switch")
print("well, how did it go ")
print(" skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip skip ")
print("=====")
print("==========")
print("================")
print("======================")

skip_range=[]
#skip_range.append(0);   
#skip_range.append(0) 
#july 5th, 2021
#so I still need to get the start and finish lines  switch and endswitch for input 
del ibm[:] #empties it
#print(ibm[0])
ibm.append(samplestring) #so in  ibm[0]
print(ibm[0])
#===================print testing on july 24th saturday  2021 at 9:36am =================
print("at this point we have this in ibm[0] after taking out the first nested switch")
#del skip_range[:]
print("LOOP TEST THRU RANGE LIST Goofy dog")
range_list=[]
skip_range.append(0) #slot [0]
skip_range.append(0) #slot[1]
#this would be done separately and is filling the range_list with the switch to endswitch params
#this will be a separate method for range input for the switch endswitches
#here the sublists of the param of each nested switch are added to range_list
#this is hard coded here filling the nested switch numbers 


#range_list=[[10,20],28,38]]  #that's right I do this backwards from bottom up!!!

'''
this goes thru the main switch string and makes a copy
of the main string in stages copying the whole thing
except for the range for each nested switch.


'''
## this means delete nested switches bodies except leave inner switch word only
##===================================================
#  REDUCE MAIN NESTED SWITCHES TO JUST SWITCH WORD
# debugged on august 5th 2021 gilroy starbucks
##===================================================
## this makes teh final main switch with the inner switch bodies stripped out
## just leaving the switch word where the nested switch was.
range_list.append([10,20]) #these are added in order and then reversed
range_list.append([28,38]) # so that the nested switches are erased bottom up
print('range_list=',range_list)
range_list.reverse()#reverses it NOTICE WE REVERS THE LIST TO CHANGE IT BOTTOM UP
#Yes I am reversing the range_list to do the changes bottom up so they don't lose their place
print(range_list) #should be [28,38],[10,20] to do from the bottom up
##======================================================
##   reduce_main_nested_switches_to_just_switch_word():
##=======================================================
#this takes out the inner switches except for the switch word
### this uses range_list!!!!!!!!!!!!!!!!!
def reduce_main_nested_switches_to_just_switch_word(astring):
    print("= R2D2 ==## $$ ## == reduce main nested switches to just switch word()==========")
    print("this cuts out the nested switches bodies leaving just the word switch")
    print("starting ibm[0] with samplestring")
    print(ibm[0])  #the key is the range_list
    print('range_list=',range_list)  ### this is the dependency the range_list necessary for this to work
    #loop thru range_list
    print("we loop thru the range_list here")
    print("let's see what RADAR is in the range_list",range_list) #see if it's reversed or not
    #loops thru range_list with pairs of switch end and endswitch
    for item in range_list: ##range_list=[[10,20],28,38]] ==========================
        print("**",item, item[0],item[1])
        skip_range[0]= item[0]; 
        skip_range[1]= item[1]
        print("skip_range=",skip_range)
        #this builds a new string by skipping the nested switch sections
        #but leaves the inner switch (switch(x) word intact
        # skipping_some_lines() called here 
        # ibm[0] has the samplestring in it from above
        skipping_some_lines(astring,skip_range[0],skip_range[1]) 
        #del skip_range[:] #this clear it out afterwords to wipe the slate clean
    print("this is the final output of the transformation halloween approaches")
    print("output of = R2D2 == taking inner nested switches body out and putting just keeping swithc word")
    print(ibm[0]) #this prints out the result 
    print("=====================")
##======================================================

#here we go  
print("the goofy dog test")  
print('we start with this string')

#print(ibm[0])
print("OLYMPICS BLAZING... gold medal time")
print("=====calling reduce main nested switches to just switch word(========)")
print("HERE NOW...this should be the sample string with the nested switches cut out leaving just switch word")
inputnowstring= ibm[0]
reduce_main_nested_switches_to_just_switch_word(inputnowstring)
# print this skips the nested switch body and creates a different version of the main switch
# and takes out the nested switches but leaves the switch word
print('after the olympics end...')
     
#print(ibm[0])
print(" starting anew here doing it the old way")
ibm.append(samplestring) #in ibm[0]
print(ibm[0])
print("that's all lemon tree software ==")
print("about to exit the program after seeing the nested switches taken out of main string")
#exit()
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/ ghostly  /=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")
print("===========///=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/======")

#skip_range.append(0)
#skip_range.append(0)
skip_range[0] =28
skip_range[1] =38
print("=============")
print("skip_range=",skip_range)
print("=============")

skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 28,38 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print("now we have this after taking out both the first and second nested switch")
#print(ibm[0])
#fuse=[]
#fuse.append(0)

#del skip_range[:]

#skip_range.append(10)
#skip_range.append(20)

#I guess I can put the ranges into a list and then reverse it and 
#loop thru it.
print('at this juncture what is in ibm[0]')
print(ibm[0])
print("starting out we have this before stripping out the nested switches")
#ibm[0] = fuse[0] #to preserve changes made 
print("input values on 2nd pass =")
skip_range[0] =10
skip_range[1] =20
print(ibm[0])
print(skip_range[0])
print(skip_range[1])
print("========")
print("skip_range=",skip_range)
print("=========")

print('==== make it dam happen == ')
skipping_some_lines(ibm[0],skip_range[0],skip_range[1])  # 10,20 #so I could put those in a list
# this says go thru string and skip lines 10 thru 20-
print(ibm[0])
print(" where is it now lemonade stand ???")
del skip_range[:] #this has to be cleared out. 
#skip range needs to be cleared out for the next nest parameters here
##===============================
print("==== the end===both nested switches should only have the switch word reminaing ===")



print("===end of copying a string and skipping lines 10 thru 20===")   
print("in ibm[0] we have",ibm[0])
print("===== this is after running skipping_some_lines(smaplestring,10,20)")
print("===========")

smart_number=[]
smart_number.append('starter')
smart_number.append(0)
smart_number.append(0)
smart_number[1] = '1'
smart_number[2] = '2'
#switch is on line 10 need to change it this is looking for the switch

#this is changing ALL OCCURENCES of switch at the 
#same time just just the one I want it to change.
# I need to localize is it to one line number.

#have it change one and then break starting on the line above


#The problem I have is if I replace each switch with the nested numbers
#then the other code won't work so perhaps I need to add a comment
#the issue is making the main strings which should only have the first level inner switches
#which is governed by tab depth of 5 representing the second level
# since tab level 3 is the first main switch.
# I could do number 1 thru n for each level initally and then change them
# or I came up with the number top down 1 thru n but level list solves the problem 
#That was my genius

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#in terms of faster programming it's about communication and control
# the lollipop is the what level but above that are higher abstraction levels
# where yet more speed can be achieved and sustained
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========
#I think I will do the one nest level for now and add the other nest levels afterwords
#decision made august 22nd, 2021 9:08 am

# I have the main module which has nested methods
# I can use this for making nested switches with nested switch methods too
# but right now I want to get the nested feature working before implimenting it
#######3==================================
#Actually I can do the main and the nested that have inner switch words not changed yet
#And then apply the conversion to numbered switches
##=====================


danumber=''
##============================================
# swap_switch_for_nest_method_new(danumber)
#=============================================
print("about to do OPTIMUS PRIME === GO BABY GO ===")
def swap_switch_for_nest_method_new(danumber): # I will add more values later perhaps 3 or 4 for coordinates
	print("#### swap switch for nest method new  ####")
	print(" =======OPTIMUS Prime======")
	print("these are the input params")
	print("q= ", "danumber= ",danumber)
	global abovenestedswitch
	abovenestedswitch=ibm[0] #loading from ibm[0] good
	print("called swap_switch_for_nest_method(n)")
	print("it is using this number in use_number[0]",use_number[0])
	acounter=0
	for line in abovenestedswitch.splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20
		if acounter == danumber and "switch" in line: #line with switch in it  
			print(line)
			#HARD CODED NOW WITH NUST nested_switch_x(n) the series number is added later for simplicity
			abovenestedswitch = abovenestedswitch.replace("switch(exp){","nested_switch_x"  + "(n)")
			print("YES switch is in this dam line")
			print("AFTER CHANGING THE NUMBER IN NESTED SWITCH")
			print(abovenestedswitch)
			ibm[0] = abovenestedswitch
			print("===================")
			print(ibm[0])
			break #because we are only doing it once to replace only ONE switch
			acounter += 1
		else:
			acounter += 1
			continue


print("now this should be the switch in the middle")
print(" line on line 10 replaced with method call instead")
# this takes in what is in ibm[0] and the outputs it to ibm[0] also, quite clever.     
#swap_switch_for_nest_method_new(1)   
print("now we use ibm[0] and insert a method where the internal switch was located")
print(ibm[0])

print("== end of show ==== ")
#exit()



# I think that I will go through a string and 
# return a list of the locations of switches 
# (skipping the first switch)
# switch and endswitch line numbers
# was just thinking that it's obviously a switch otherwise
# we wouldn't be here so NO NUMBER for main switch (brilliant)
#it still matters but it's obvious that it is there. It's actually
# the main switch and the frame for nested switches. 

ibm[0]=tuna #input of string into ibm[0]
list_of_nested_switches=[]
list_of_nested_switches.append(12)
list_of_nested_switches.append(32)

#here I am using a list which has the line numbers of the inner switches locations
print(list_of_nested_switches)  #so it would look like this 
#this goes through the input main switch and changes nested "switch" into a nested_switch numbered

#this is used for managing the nested switches by getting their location to know
#where to copy them when extracting them from a main switch
# today is july 17th, 2021 9:33 am

print('testing this to make list of all switch locations and all endswitch locations')
print(tuna)
switch_location=[]
endswitch_location=[]
print("beginning === put location of switch and endswitch into lists")
print("====---------------------- saturday coding ----------===")

ourcounter=0
#for line in abovenestedswitch.splitlines(): 
for line in tuna.splitlines():
    
    if line.startswith("switch"):
        print("this lines starts with switch")
        switch_location.append(ourcounter)
    
    
    if line.startswith("endswitch"):
        print("this line starts with endswitch")
        endswitch_location.append(ourcounter)
        
    ourcounter += 1
        
print("====OUTPUT TO DETERMINE location of each switch and endswitch====")
print("")
print("switch_location=",switch_location)
print("endswitch_location=",endswitch_location)
print("")
print("===make your dreams reality===")
        



# july 24th, 2021 
#the input for this MUST be the already reduced main switch which
# has just the switch word in place where each nested switch thru endswitch was.


###  Thursday, August 19th, 2021 time 9:07 am
# I think that I just need to not worry about the other nested switches
# and just do the first level of nested switch since the others will just be in the other switches
# so let' say I have two nested switches deep
# I only have to have (for the main switch) the first level nestedswitch
# so then the situation becomes the numbering because in this first level of nested switches
# they would be numbered in sequence 1, 2, 3 etc  
# if say there are two nested in teh first main swith then sub1
# but for the inner levels (the next tab level) I would have to do 4,5,6 I suppose
# so continuing sequence or 1.1 and so forth
# I need to come up with a simple numbering system maybe Alpha first level Alph
###
#what if I have pairs, simple numbering but 
##===========================================	
## number_nested_switches_in_sequence()
##===========================================
#put the input I just created into ibm[0]
#this would be the main string after the nested switches are taken out  leaving switch word
forcedinputstring='''
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
			print('== autumn nest===')
			switch(exp){   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''
trouble=[]
trouble.append(forcedinputstring)
#this is using preset nested switch starting locations 11 and 29 for this test
# this is for making the nested switch numbered method 


#this swaps switch with nested_switch_" n
##########################################
## number_nested_switches_in_sequence():  #this is using hardcoded input for testing
##########################################
def number_nested_switches_in_sequence(): # list_of_nested_switches[11,29]
	print("=R2D2= number_nested_switches_in_sequence()  ===========")
	newcount=1  #number of nested switches starts from 1
	## wait do I loopthru it get the position of the inner switches now why not
	## modification on july 24th 
	print("to see what it sees first")
	#this is string above called forcedinputstring
	print(trouble[0])  #it was ibm[0] which I will change it back to later
	mystring=''
	mystring = trouble[0] #putting the string into trouble[0]
	newcounter=0
	foundone=[]
	# this gets the inner switch locations after the inner switch bodies have been stripped out (deleted)
	##===============================
	for line in mystring.splitlines():  #this fills list foundone with switch line numbers
		if "switch(exp)" in line:
			print("true we found switch")
			foundone.append(newcounter) #this fills the foundone list of line numbers with switch in it
			newcounter += 1
			continue
		else:
			newcounter += 1
			continue
	#=== end loop ========================
	print("we are done looking for the inner switch locations")
	print("====================")
	print("thefoundone llist has",foundone)
	print("the length is", len(foundone))
	print("========........======")
	print(" ") #below we delete the first switch which is on line 1
	del foundone[0] #this should delete the first switch we don't need 
	print("now we have for foundone list",foundone)
	## end getting inner switch lcoations
	##======================================
	
	#shiney= ibm[0] #so it will skip the first few lines skipping the first switch 
	thecounter = 0 #tracking lines in the string   oh it's using preset numbers
	print('the list of nested switches starting line',foundone)
	switchcount=0
	magic_string=''
	seagull='' #WAS shiney.splitlines()
	for line in trouble[0].splitlines(): #determine if "endswitch" is in line
		#this should skip lines between 10 thru 20
		#we know that the lines that the inner switch resides in is between 10 and 20 
		#skip over 10 thru 20 #IT HAS TO BE AFTER THE FIRST 2 LINES TO SKIP THE FIRST SWITCH
		#if  switchcount > 0  and thecounter in foundone:
		
		if  thecounter in foundone:  #this must be line numbers of inner switches
		#this line of code is absolutely beautiful and elegant 
			print("thecounter=",thecounter)
			print("switchcount=",switchcount)
			########We know the line numbers do it on one pass perhaps
			# it should only go to the lines in the list of nested switches
			line = line.replace("switch(exp){","nested_switch_"  + str(newcount) +"(n)")
			magic_string += line + "\n"
			#NEW line above
			newcount += 1  #break #because we are only doing it once to replace only ONE switch #start  = thecounter #this resets the range n to skip what it just did.
			thecounter += 1 #this adds to the neste switch counter
			continue    
		else:
			magic_string += line + "\n"
			# new ling e
			thecounter += 1
			continue
	print("=====-----======-----======------=====----====----====---")
	print("magic_string=")
	print(magic_string)
	print("========")
	for line in magic_string.splitlines():
		print(line)
		
	print("were the changes made - this is kind of important at this stage RED ALERT")
	trouble[0] = magic_string #here it's fed into trouble[0] so it's in a list now
	print("did I rip out the nested switches or are they still intact???")
	print("trouble[0]=",trouble[0])	
	#ibm[0] = shiney
			
####================================			
print('about to call number-nested_switches_in_sequence() to test it extendo bus just passed')
number_nested_switches_in_sequence()
print("it should have ran already testing bugs bunny here ")
print("the nested switch words should be nested numbered methods now")
			
#exit()

print("we are at line 4434 now and after finishing doing number_nested_switches_in_sequence() ==>>")
print("this is where the exit() was.......1..2...3..4....5..555..666...777..8.8..9999.10 10==")













#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========





			
###============== Sunday July 25th, 2021  10:19 am Cafe Borrone ===============
# the idea is to put the information for each nested switch case
# into the dictionary in terms of it's exact information
# so to fill the data into the nested switch dictionary I will need
# to loop thru the switch string and gather the data for each switch location
# and it's particulars and add it to the dictionary (this should be done first')
# the idea occurred to me since each nested switch has a specific location
# and juggling them can get quite confusing so this way I know which is which
# and where it is.
#=======================================================================
####################
## DICTIONARY HERE 
####################
#putting a named list inside of known dictionary
nest_data=[]
# I probably won't need this.
nested_switch_data =	{  #for pear tree in backyard (2 of them)
#key [level tab depth,number case,  line number, series number
"1": [3,2,23,1], # I can make these now 
"2": [3,3,43,2],
}

print(nested_switch_data)

result=[]
result.append(0)

###############################################################
## RAM LIST TO HOLD TEMPORARY DATA FROM LIST WITHIN DICTIONARY
###############################################################
ram_list=[]
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)
ram_list.append(0)

########################
## get_nest_data(key)
########################
def get_nest_data(x): #puts it temporarily into result[0]
	print("get nest data called",x)
	#this grabs the value from the key and puts it into result[0]
	#these are teh parameters for tehe signature for this nested switch
	result[0]=nested_switch_data.get(x)
	#s- there would be a list within result[0]
	#why not instead populate a list
	print("this is what is in result[0]")
	print(result[0])
	for item in result[0]:
	    ram_list.append(item) #see if this fills it or not
	print('ram_list=',ram_list)
#############################		

  #test data input
############################
##  add_to_nest_data(x,y)
############################
cool_list=[]

x = cool_list
def add_to_nest_data(x,y):
	print("====add to nest data() called with ", x  ,"and",y)
	nested_switch_data["my_list_" + str(x) ] = y

#print("my_list_1[0]",my_list_1[0])
#print("gosh")
######====================================
########
print("working on access a dictionary in a precise positiion in a list")
print("that is in the dictionary")
my_dict={}
#add a dictionary #this might be just what I need actually 
my_dict["my_list"] =[3,1,4,1]
print('terrible')
print('trying mydict[0] see if it works')
print(my_dict["my_list"][0]) #the key
print(my_dict["my_list"][1]) #the key
print(my_dict["my_list"][2]) #the key
print(my_dict["my_list"][3]) #the key
alpha = my_dict["my_list"][0]
print("alpha sees =",alpha)
#check in the list


# 

my_list_1=[]
my_list_2=[]
my_list_3=[]
#####======================================
y = [1,2,3,4,5]
add_to_nest_data(1,y)

y = [23,26,34,42,52]
add_to_nest_data(2,y)

y = [63,66,64,72,72]
add_to_nest_data(3,y)
print("=================")
print(my_list_1)
print(my_list_2)
print(my_list_3)

#print(my_list_2)
#alpha = mylist_1[0] #should be 1
print("is this even working....",alpha)

print(" == looping through nested_switch_data to see the contents == ")
print("TESTING ship wreck the contents of the dictionary now,,,")
for key,value  in nested_switch_data.items():
	print(key,value)
	













################################
##  NESTED_SWITCH_INFO
###############################	
def nested_switch_info(x):
	get_nest_data(x)
	#this will get the info from the dictionary		
			
			
			
switch_location=[]
endswitch_location=[]
#  WE ARE HERE THIS IS WHERE THE BIG TEST BEGINS TO REPLACE INNER SWITCHES WITH METHODS ON THE FLY
##=================
#if we already have the numbers it should work, later I will have it find the locations first
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG==")
print("=====GODZILLA and KING KONG ===BIG TEST here in the switch with 2 nested switches")
print("========")
print("this does the bottom half the bottom nested switch first ")
print("this is becuase it's governed by the corect line numbers")
print("and if I take out the top switch code then the numbers for the lower switch will be wrong")
print("I just realized that") #this is the purpose of experimentation
ibm[0] = tuna  #I am force feeding it into ibm[0]

# I have to tell it what number to use to number the nested method using
# use_number[0]= 2 example








################
# the skipping is done by the main switch when I cam copying it and taking out the 
# nested switches below but keeping the switch word that I then convert to a method nested numbered
#################
#NUMBERING OF NESTED SWITCH HAS TO BE DONE BOTTOM UP SINCE WE ARE RIPPING OUT THE NESTED SWITCH AFTER THE SWITCH WORD
#oh I will have to do this bottom up so the line numbers are correct. 
print("I am taking out the lower switch first (later I will copy it first)")
skipping_some_lines(ibm[0],28,38) #changes 2nd nested switch
use_number[0]=2
swap_switch_for_nest_method_new(21) #second number has the switch in it 
#the first number is the number for the nested_switch
print("this now does the top nested switch")
print("here I am taking out the first nested switch later I will copy it first")
skipping_some_lines(ibm[0],10,20) #changes first nested switch in the sequence
use_number[0]=1
swap_switch_for_nest_method_new(11) #second number has the line number with switch   #needs to be 1 not 2
print("this is the end of Godzill and King Kong testing")







#this should be called only once and 
print("====++++now testing running number_nested_switches_in_sequence()")
#number_nested_switches_in_sequence()
print("we have just completed the first nesteed switch skipping and putting a nested method 1 in ")
print("ibm[0] should show the main switch with 2 methods where the inner switches were previously")
print("this is the output of the string ibm[0]")
print(ibm[0])
print("I am going to loop thru the switch and change the lines with nested_switch")
print("============= Godzilla =============")
print("END OF GODZILLA AND RODAN AND MOTHRA")


#go thru a number the switches numerically top down

























hawaii ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#######
			switch(exp){          
				case 'blable':
					print("do something")
					print("yep")
					######
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
						endswitch 
						######
					fallthru
				case 'more':
					print("nice")
					break
				default:
					print("we are done here")
			endswitch 
			######
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			#######
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
			#######
			fallthru
		
		default:
			print('the end')
}
'''	
get_switch_and_endswitch_locations(hawaii)
print("this would have just gotton the switch and endswitch line number locations above...")
print("I found it, I was looking for this code")
#empty_switch_and_endswitch_list_locations()

get_switch_and_endswitch_locations(tuna)
###======================================================
#july 19th 2021 testing this feature now morgan hill starbucks
########################################################
#empty_switch_and_endswitch_list_locations()
#print("the one below this line should produce 2 switches and one with 10,20")
#print("why is this wrong")
#get_switch_and_endswitch_locations(samplestring) #samplestring 
#get switch and endswitch lcoations for one nest
#it's off by one says 11,21
#input is 10 and 20 and yet this says the line number is 11 and 21 for nested switch

empty_switch_and_endswitch_list_locations()
print("the one below this line should produce 2 switches and one with 10,20")
print("why is this wrong")
print("get result of get switch and endswitch locations from samplestring")
print("earth is over level ======")
print("earth is over level ======")
print("=== tea time =============")
get_switch_and_endswitch_locations(samplestring) # sammplestring


###  july 14th wednesday 2021 working on this
#real number is count endswitches and add 1 for total switches

#endswitches number is how many nested switches

# this empties the lists storing the switch and end switch locations

#del switch_location[:]
#del endswitch_location[:]

#get_switch_and_endswitch_locations(hawaii)

print("this is the string with two nested switches")
print("here we go wednesday coding - the bicycle gloves are great")
print("first clearing out the lists that hold the locations of the switch and endswitches")
print("this clears out the swith and endswitch locations in the list so it starts empty")

#I was deleting the crucial lists so the code down below couldn't behave correctly

#del switch_location[:]
#del endswitch_location[:]
#feed the string into the method to get the switch and endswitch locations
# but delete the first switch details which isn't important at this point.

#get_switch_and_endswitch_locations(tuna)
#this creates a list that can be of any size and then I can subtract the first switch
#and then divide the number by 2 to get teh number of switches or just count teh switches
'''
nest1=[]

nest1.append(switch_location[0])
nest1.append(endswitch_location[0])
nest2=[]
nest2.append(switch_location[1])
nest2.append(endswitch_location[1])

#wait a  second with each pass the output will be teh same unless I have 
#a list of say ten spaces tol hold locations to be proactive.
#####################################################
print("nest1=",nest1)
print("the two values in nest1 are",nest1[0],nest1[1])
print("nest2=",nest2)
print("the two values in nest2 are",nest2[0],nest2[1])
'''


#++++++++++=========================================================
### july 7th 2021 experimenting 
### testing cutting out two nested switches one at a time
### and replacing the switch location with the nested method with a number
# I need to do these separately first to make that they work
##===========================================
##===========================================
#skipping_some_lines(tuna,nest1[0],nest1[1])
#swap_switch_for_nest_method_new(1)

#and I need to make sure that the resulting string to modify the second phase is correct
#skipping_some_lines(tuna,nest2[0],nest2[1])
#swap_switch_for_nest_method_new(2)
##============================================
##============================================
# what I will attempt it going thru the double nested switch with two nests
# and delete the two nests and put nest methods in the location of the inner switches.
# and then after that is figured out I will first copy each inner switch
# Based on the nested switch locations I find I can determine how many nested switches
# espcially with teh endswitch count 



#######================================================================#########==========

#######================================================================#########==========

#######================================================================#########==========






















#made this july 10th in silver file just pasted it here.
### important - need to add methods inswitch and infallthu at to
# the order should have already been reversed so that the main switch string is last.

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
    function_definitions ="def inswitch():\nprint(test this) \n\n def infallthru():\n print('do something')\n\n"
    volleyball += function_definitions #must be first
    #stanford list should alread by reversed so that main switch is last
    for item in stanford:
        volleyball += "\n\n"
        volleyball += "count="
        volleyball += str(count) + "\n"
        volleyball += item
        volleyball += "\n\n" #spacer 2 lines
        volleyball += "============ divider =========== \n"
        count += 1
        print(count)
    
    # here I can manipulate the output python code 
    # uppercase_test[0] == True:
    # baseline[0]="nada"
    print("volleyball =",volleyball)	

#build_stacked_cake_string_combining_stanford_list()
levels_list_major=[]

levels_list_minor=[]


testing_nesting1='''
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
			print('== autumn nest===')
			switch(exp){   #this is new 28       
			fallthru
		
		default:
			print('the end')
}
'''
#  desired outpout after changing a nested switch 
## with inner switches with new methods added numbered
#  this is the desired output 
testing_nesting2='''
	switch(exp) {  
		case 1 thru 3:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			deep_nested_switch_level_1_1(exp)      ###================     
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== autumn nest===')
			deep_nested_switch_level_1_2(exp)      ###================   
			fallthru
		
		default:
			print('the end')
}
'''
