
fishyone2 ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\")
			print('nimitz')
			print("==area 51==")
			//testing this out

		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			/*
			c style comment her mult-line
			more comments here
			*/
		/* weird and wild here */
		case 'Darth Vader': 
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		default:
			print('no results')
			print("that is all")
			break //what about here too
}
'''



razzle ='''
	switch(exp) {
		case 'ufos':  
			print(\"ww2!\") /* did this one work */
			print('nimitz')
			print("==area 51==")
			//testing this out
			//this is so true 
			/* now putting it here */
		
		case 'Star Wars':
			/* go for the money */
			print('return of the jedi')
			print("Luke Skywalker ")
			/*
			fudge this is not fair
			way to go make it work
			right now on time
			*/
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		/*
		still testing this out
		to see how it works
		*/
		default:
			print('no results')
			print("that is all")
			break
			// some comments here for fun
}
'''

##==================================
##  change_C_style_single_line_comment()
##=================================
#testing using C style comments and convert into python comment
def change_C_style_single_line_comment():

	newstringbuild=''
	for line in fishyone2.splitlines():
		print(line)
		if "//" in line:
			newstringbuild += line.replace("//", "#") + "\n"
		else:
			newstringbuild += line + "\n";

	
	for line in newstringbuild.splitlines():
		print(line)
		
change_C_style_single_line_comment()

print("====")
print("====")

##==================================
##  multiline_C_comment_changer()
##================================= should be 12 and 15 
print("=======now trying mulitlcine C comment changer=======")
def multiline_C_comment_changer(): #for demonstration presuming only one multiline comment initially
	print("========: multiline_C_comment_changer()======")#so do one pass first to get locations
	newstringbuild2=''
	mycounter=1
	start=1
	stopper=1
	newthought=fishyone2
	## phase 1 get location
	if "/*" not in fishyone2:
		print("no nested C comment in this string")
		return
	#################################
	print("print phase 111111")
	mycounter = 0
	print("====FIRST LOOP MULTILINE TO GET start position ===")
	for line in fishyone2.splitlines():
		print(line)
		if "/*" in line :# change to # get line number
			print("found /* in string in line ",mycounter)
			start= mycounter
			print("start=",start)
			mycounter += 1
			break
		else:
			mycounter += 1	
	###########=======
	#acounter=0
	#for line in fishyone2.splitlines()
	
	
	print("====second LOOP MULTILINE TO GET stopper position ===")		
	mycounter = 0
	for line in fishyone2.splitlines():		
		if  "*/" in line:    #as ender
			stopper= mycounter
			print("stopper=",stopper)
			break #I can break here because we don't need to go any further
			mycounter += 1
		else:
			mycounter += 1	
			
	print("we are looking for start 12 and stopper 15==")
	print("start =", start)
	print("stopper=", stopper)

	middleground=''
	################################# 
	newcounter=0     
	
	print("====SECOND LOOP MULTILINE REPLACE C STYLE MULTIINE COMMENT MARKERS===")

	print("phase 222222")
	print('start is ',start,"and stopper=",stopper)
	for line in fishyone2.splitlines():

		#=====  IF COUNTER GREATER THAN START==AND LESS THAN STOPPER==
		if newcounter >= start and newcounter <= stopper:
			print("==newcounter >= start and <==== stopper")
			print("newcounter=",newcounter)
			middleground += line + "\n"
			#print("====newcoutner > start and < stopper====")
			
			newcounter += 1
		else:
			newcounter += 1
	
	for line in middleground.splitlines():
		print(line)
	
	newcounter=0
	print("buildling top half for fun===0=0=0=0=0=0=0=0=0=0=0")
	#print('start is ',start,"and stopper=",stopper)
	tophalf=''
	for line in fishyone2.splitlines():

		#=====  IF COUNTER GREATER THAN START==AND LESS THAN STOPPER==
		if newcounter < start :
			#print("==newcounter >= start and <==== stopper")
			#print("newcounter=",newcounter)
			tophalf += line + "\n"
			print(line) #print("====newcoutner > start and < stopper====")
			
			newcounter += 1
			
		else:
			break
		#	newcounter += 1
			
	print("=====SHOWING OFF TOP HALF for testing purposes=======")		
	for line in tophalf.splitlines():
		print(line)
	solid=''
	solid = tophalf
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("buildling top half for fun")
	print("=====")
	print("=============0000000==")
	#print('start is ',start,"and stopper=",stopper)
	newcounter=16
	deepseahalf=''
	print("stopper =",stopper)
	#what about copy the whole string and then chop off the top that should work
	
	for line in fishyone2.splitlines():

		#=====  IF COUNTER GREATER THAN START==AND LESS THAN STOPPER==
		if newcounter > stopper and "}" not in line :
			#print("==newcounter >= start and <==== stopper")
			#print("newcounter=",newcounter)
			deepseahalf += line + "\n"
			print(line)
			
			newcounter += 1
		
			
	print("showing off the bottom half for testing purposes")		
	for line in deepseahalf.splitlines():
		print(line)
	

	
	
	print("============= the great divider here ==========")
	print("============= the great divider here ==========")		
	print("building the bototm half now") 
	newcounter =0  #starting at stoopper 
	realbottomhalf=''
	for line in fishyone2.splitlines():

		#=====  IF COUNTER GREATER THAN START==AND LESS THAN STOPPER==
		if newcounter > stopper  and newcounter < len(fishyone2):
			print("what is on the next line")
			print(line)
			realbottomhalf += line + "\n"
			#print("====newcoutner > start and < stopper====")
			newcounter += 1
		
	
	#print("======bottom half testing here====")
	#for line in realbottomhalf.splitlines():
	#		print(line)
	#itlooks like this
	#	   /*
	#		c style comment her mult-line
	#		more comments here
	#		*/
			
	print("========phase 3===/\/\/\/\/\/\/\/=====phase 3====")
	
	for line in middleground.splitlines():
		print(line) 
	
	yetanotherstring=''	
	for line in middleground.splitlines():
	
	#######== phase 1 ==############# top section #########
		if "/*" in line:
			print(line)
			tabcount = line.count("\t")
			yetanotherstring += line.replace("/*", "#") + "\n" #top brilliant 
		####### end of phase 1 ##########################
		
		####== phase 2 ==#############/* not in line and */ not in line ############
		if "/*" not in line and "*/" not in line: #if neither are in this line
		####### no /* and */ in line ################
			line = line.strip()
			aline = '\t\t\t' + "#" + line + '\n'
			yetanotherstring += aline
		######## end of phase 2 ############################# 
		
		
		#continue
		##== phase 3 ==############### #########################
		if "*/" in line:
			yetanotherstring += line.replace("*/", "#") + "\n" #bottom brilliant
		####end of phase 3 ########################################    
	print("we are hear what does this look like really")
	mycounter =0
	print("this should be the middle headache what does this look like")
	for line in yetanotherstring.splitlines():  #this will be the middle inbetween layer 
		print(line)
		mycounter +=1
	
	print("end of fancy replacement of /* thru */ and replacing with # correctly")
	 #this is using a C style multiline comment and changing python commenting out   
	 #demonstration commenting out in python style a few lines of code 
	 #inserting yetanotherstring which is modified
	
	tophalf=''
	bottomhalf=''
	counter =0	
	print('======phase 4444444=====')
	print('start is ',start,"and stopper=",stopper)
	for line in yetanotherstring.splitlines():
		if newcounter <= start:  #stop here
			tophalf += line + "\n"
			counter += 1
			
	print("======and this is the TOP half ========")    
	for line in tophalf.splitlines():
		print(line)
	 
	counter=0
	for line in yetanotherstring.splitlines():
		if newcounter >= stopper:  #stop here
			bottomhalf += line + "\n" 
			counter += 1  
	 
	print("bottom half for kicks")
	print("========and this is BOTTOM HALF ====super nova===") 
	starpower=''
	newcounter = 0   
	stopper = 15
	for line in fishyone2.splitlines():
		#=====  IF COUNTER GREATER THAN START==AND LESS THAN STOPPER==
		if newcounter > stopper:
			#print("newcounter =",newcounter)
			#starpower = line
			
			starpower += line + "\n"
			print(line)#print("====newcoutner > start and < stopper====")
			
			newcounter += 1
		else:
			newcounter += 1
			
	print("this shoudl be the bototm of the string the bottom half")
	for line in starpower.splitlines():
		print(line)       	
		
	print("this is what it will look like...victory====== ")	
	#for line in yetanotherstring.splitlines():
	#	print(line)	
	newstringbuild=''
	for line in solid.splitlines():  #this is an afterthefact just in time change
		print(line)
		if "//" in line:
			newstringbuild += line.replace("//", "#") + "\n" #does a swap
		else:
			newstringbuild += line + "\n";
	solid = newstringbuild		
	print("======DOES THIS LOOK RIGHT NOW=?? sure does========")
	
	for line in solid.splitlines():
		print(line)
		
	
	for line in tophalf.splitlines():  #this will be the middle inbetween layer 
		print(line)
	
	for line in starpower.splitlines():
		print(line) 
		
multiline_C_comment_changer() 

#########################
#the idea is go thru once actually
#the rule is if within /*  and */ then can't have // inside of it
def on_the_fly_comment_changer(stringname):
	#breakpoint()
	print("==BIG CHANGE NOW=====on_the_fly_comment_changer()===big flies====")
	smarttabs='';buildstring='';series_comment= False;smarttabs='';megaline='' 
	for line in stringname.splitlines():
		###=================================================================
		#checks if // in line  this chnages it into #
		if "//" in line: #presuming /* and */ are not in this line
			buildstring += line.replace("//", "#") + "\n" #for a single line obviously
			
		# just added this to handle if /* comment one line with this */
		# can't use this in middle of line of a code though for now
		if "/*" in line and "*/" in line: # and series_comment == False:
			series_comment= False #this is where and when I set it to False here we set the flag back to False
			megaline += line.replace("/*", "#") #replaces first /* with #
			megaline = megaline.replace("*/", "")  + "\n"
			#print("megaline here =",megaline)
			buildstring += megaline + "\n"
	
		###=================================================================
		#checks if /* in line and changes it to # and sets series_comment to True
		if "/*" in line and "*/" not in line and "//" not in line and series_comment == False:
			series_comment = True  #notice set flag to True here 
			tabcount = line.count("\t")
			smarttabs = tabcount #this is new
			print('smarttabs=',smarttabs)
			buildstring += line.replace("/*", "#") + "\n" #top brilliant 
		###=================================================================
		#checks if */ in line and series_comment == True this puts # at front of line 
		if "*/" not in line and "/*" not in line and "//" not in line and series_comment == True:
			line = line.strip()
			tabresult = smarttabs * '\t'
			aline = tabresult + "#" + line + '\n'  #the issue is 3 tabs by default
			buildstring += aline
		###=================================================================
		if "*/" in line and series_comment == True:
			series_comment= False #this is where and when I set it to False here we set the flag back to False
			buildstring += line.replace("*/", "#") + "\n" 

		if series_comment == False and "//" not in line and "/*" not in line and "*/" not in line:
			buildstring +=  line + "\n";
	
	stringname = buildstring
	#for line in stringname.splitlines():
	#	print(line)
	##################################
	return stringname
	
	
	
	
print("this is the on-the-fly test")
cool1 =on_the_fly_comment_changer(fishyone2) #this is the input string for testing

for line in cool1.splitlines():
	print(line)
	
	
cool2=on_the_fly_comment_changer(razzle) #this is the input string for testing

for line in cool2.splitlines():
	print(line)

'''        
#thought I could go thru the whole string in a loop
# this is an idea
#and when I detect /*  replace that line and subsequent lines with // until 
#and including */
#then go thru the loop and replace each // with #
'''
#so first pass build new string
#detect // and start /*  and stop */
#but as I go change // to # and change on-the-fly /* with #
#and continue putting # until and including */
#trigger flag make it true at start of /* and then change it to 
#False after last end */

#because there might be series of // // and /*  */ scattered throughout string

#this is governed by looping for length of fishyone2
#but only modifies from start to stopper
# I need to cut out the 4 lines first though
# I can just copy the lines before the multine comment
# and copy the lines below the multileinc coment
# and then glue the modified 3 lines and concat them together

///refactroed by gpt on may 25, 2024

It seems like you're trying to refactor some code, particularly handling C-style comments in Python. Here's the refactored version of your code:

python
Copy code
def change_C_style_single_line_comment(input_string):
    new_string = ""
    for line in input_string.splitlines():
        if "//" in line:
            new_string += line.replace("//", "#") + "\n"
        else:
            new_string += line + "\n"
    return new_string

def multiline_C_comment_changer(input_string):
    new_string = ""
    inside_comment = False
    for line in input_string.splitlines():
        if "/*" in line:
            inside_comment = True
            new_string += line.replace("/*", "#") + "\n"
        elif "*/" in line:
            inside_comment = False
            new_string += line.replace("*/", "#") + "\n"
        elif inside_comment:
            new_string += "\t\t\t#" + line.strip() + "\n"
        else:
            new_string += line + "\n"
    return new_string

def on_the_fly_comment_changer(input_string):
    new_string = ""
    inside_comment = False
    for line in input_string.splitlines():
        if "//" in line:
            new_string += line.replace("//", "#") + "\n"
        elif "/*" in line:
            inside_comment = True
            new_string += line.replace("/*", "#") + "\n"
        elif "*/" in line:
            inside_comment = False
            new_string += line.replace("*/", "#") + "\n"
        elif inside_comment:
            new_string += "\t\t\t#" + line.strip() + "\n"
        else:
            new_string += line + "\n"
    return new_string

fishyone2 = '''
    switch(exp) {
        case 'ufos':  
            print("ww2!")
            print('nimitz')
            print("==area 51==")
            //testing this out

        
        case 'Star Wars':
            print('return of the jedi')
            print("Luke Skywalker ")
            /*
            c style comment her mult-line
            more comments here
            */
        /* weird and wild here */
        case 'Darth Vader': 
            print('flying in it tie-fighter')
            print("the force is strong in this one...")
            break
            
        default:
            print('no results')
            print("that is all")
            break //what about here too
    }
'''

razzle = '''
    switch(exp) {
        case 'ufos':  
            print("ww2!") /* did this one work */
            print('nimitz')
            print("==area 51==")
            //testing this out
            //this is so true 
            /* now putting it here */
        
        case 'Star Wars':
            /* go for the money */
            print('return of the jedi')
            print("Luke Skywalker ")
            /*
            fudge this is not fair
            way to go make it work
            right now on time
            */
        case 'Darth Vader':
            print('flying in it tie-fighter')
            print("the force is strong in this one...")
            break
            
        /*
        still testing this out
        to see how it works
        */
        default:
            print('no results')
            print("that is all")
            break
            // some comments here for fun
    }
'''

print("Refactored fishyone2:")
print(change_C_style_single_line_comment(fishyone2))
print("\nRefactored razzle:")
print(multiline_C_comment_changer(razzle))

print("\nRefactored fishyone2 with on-the-fly comment changer:")
print(on_the_fly_comment_changer(fishyone2))
print("\nRefactored razzle with on-the-fly comment changer:")
print(on_the_fly_comment_changer(razzle))
I've separated your code into functions to handle different types of comments: single-line comments, multiline comments, and a version that changes comments on-the-fly as it processes each line. Each function takes an input string and returns the modified string. You can use these functions to refactor your code more efficiently.



