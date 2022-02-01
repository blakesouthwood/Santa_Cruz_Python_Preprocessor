import site_b   #toying around with site_b and site_c
from site_b  import * 

#if switch numbers to transfer > length of snowtime
#smartlistlocations[13, 9, 6, 6, 7, 13, 9, 6, 6, 7]
#smartlistlocations= [13, 9, 6, 6, 7, 13, 9, 6, 6, 7, 13, 9, 6, 6, 6, 7]

def do_something():
    a = 2
    b = 2
    c = a + b
    print("c=",c)
    return c

def testing_this_out():
    #print('testing_this_out')
    #print('breaking out of while true')
    while True:
        cool = 0
        do_something()
        cool = 1
        if cool == 1: #true
            #print('breaking out')
            break; #breaks out of while True
    #print("now for something relaly different")
    #print("this is nice")
    
#testing_this_out()

mylist=[1,2,3,4,5,6,7,8,9,10]
good=[]
def trythis():
    #print(":try this test=-=-=-=-= trythis()  -=-=-=-= gizmo -=-=-=-=-=-=-==--== ")
    #good = mylist[-5:]
   # print("good=",good)
    print(":==========")
    print("should be original mylist=",mylist)
    courage = mylist[-5] #seeing if this works or not 
    print('courage=',courage)
        
  
    print('trouble list=',trouble)
   



trythis()
##===================================================================

red_robin ='''
	switch(exp){  
		case 1 thru 6: 
			print("green lantern green lantern green aliens!")
			print('this green green green . it actually works')
			print('how green green green, yes way ')
			
			
		case 7 to 10:
			print('green lantern green lantern green  between 7 and 10 !')
			
			#############
			exp ='blable'
			
			switch(exp)  
				case 'blable':
					print("we are blable here   inside of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice kayaking race")
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
			#exp = 3
			print('this should write this line still within bounds of outer sw')
			switch(exp)
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
			print('taught me how to write code')
			fallthru
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


red_robin2 ='''
	switch(exp){  
		case 1 thru 6: 
			print("====   red white blue    =====")
			print("====   white   =====")
			print("===    blue    ======")
			
			#it should stop here
		case 7 to 10:
			print("this is =======red white blue====== ")
			print('pass Dutch Flat, Cisco, and Kings Beach to NorthStar !')
			print(" this is 7 to 10 here we are")
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
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
			#exp = 3
			switch(exp)
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
#33289

red_robin3 ='''
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
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]=" did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do  of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
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
			#exp = 3
			switch(exp)
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



red_robin4 ='''
	switch(exp){  
		case 1 thru 6: 
			print("====zebra black and white =====")
			print("====   zebra   =====")
			print("===    tahoe summiting    ======")
			
			#it should stop here
		case 7 to 10:
			print("this is =====zebra black and white ====== ")
			print('pass Dutch Flat, Cisco, and Kings Beach to NorthStar !')
			print(" this is 7 to 10 here we are")
			break
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("this is the second string to try of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
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
			#exp = 3
			switch(exp)
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
			print("11 to 15 in ==zebra black and white==")
			print('big numbers here this is 11 thru 15  ')
			print('=this is the last c ase ==')
			print('-----------------')
			####################
			exp ='snow fire'
			switch(exp){   
				case 'fishy':
					print("do something")
					print("yep")
					fallthru
				case 'snow fire':
					print("inside of snow fire from zeba black white")
					#############
					break
				default:
					print("we are done here")
			endswitch 
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	
#33289



red_robin5 ='''
	switch(exp){  
		case 1 thru 6: 
			print("grey aliens!")
			print('greys aliens')
			print('green aliens ')
			
			
		case 7 to 10:
			print('green lantern green lantern green  between 7 and 10 !')
			
			#############
			exp ='blable'
			
			switch(exp)  
				case 'blable':
					print("inside of an inner sw itch here we are blable here   inside of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					break
					####################
					exp = 'tahoe'
					switch(exp){ 
						case 'tahoe':
							print("do THIS IS SO COOLinside of sw 15")
							print("oh is this going to really work now ... really it is")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							result[0]='fallen leaf lake waterskiing fell'
							
							####################
							exp = 'winter'
							switch(exp){    
								case 'winter':
									print("this is possibly sw 25")
									print("listening to mit debugging session in summer")
									print("yep")
									fallthru
								case 'fallen leaf lake':
									print("nice kayaking race")
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
			#exp = 3
			print('this should write this line still within bounds of outer sw')
			switch(exp)
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
			print('taught me how to write code')
			fallthru
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


print("on to the next one==5 test now ======")

import time
start_time = time.time()


print(" === 1st test === nested==")

num = 1   
main_control_sequencer(num,red_robin)#red_robin  #this will be the the modifed endswitch eventually 
print("==yanks==testing 2 now ")
print('=======after first pass===before second pass ===')
#show_it_to_me()  

print(" === 2nd test === nested==")
num = 7   
main_control_sequencer(num,red_robin2)#red_robin  #this will be the the modifed endswitch eventually 
#print("====after second pass== before 3rd pass=== ")
#show_it_to_me()

print(" === 3rd test === nested==")
#print("about to do second call of a second nested switch string")
#print("this is the third PASS doing regular red_robon second now")
num = 1   
main_control_sequencer(num,red_robin3)#red_robin  #this will be the the modifed endswitch eventually 
#print("=====after 3rd pass ======")
#show_it_to_me()
#print("go I want to fly like superman")
print("================number 4 test ======")


num = 1   
main_control_sequencer(num,red_robin4)#red_robin  #this will be the the modifed endswitch eventually 

print("last one now the 5th test ====")
num = 1   
main_control_sequencer(num,red_robin5)#red_robin  #this will be the the modifed endswitch eventually 



print("the end is near")


#cloudy_day =

# 	switch(exp) {  
# 		case 1 thru 3:
# 			print("where\'s the dog house!")
# 			print('first prize')
# 			print('you block head Charlie Brown')
# 			fallthru
# 			
# 		case 4 to 7:
# 			print('kangaroo hop hop!')
# 			exp='more'
# 			switch(exp){   # === line 10 beginning of single nested switch ======      
# 				case 'blable':
# 					print("inside of the inner sw here")
# 					print("yep")
# 					fallthru
# 				case 'more':
# 					print("nice")
# 					break
# 				default:
# 					print("we are done here")
# 			endswitch #this is key here =============line 20 end of nested switch ====
# 			print('taught me how to write code')
# 			fallthru
# 			
# 		 
# 		case 8 to 10:
# 			print('mocha blast')
# 			print('== baskin robins ice cream on El Camino Real===')
# 			fallthru
# 		
# 		default:
# 			print('the end')
# }
	


#num = 1#1    
#main_control_sequencer(num,cloudy_day)
#red_robin  #this will be the the modifed endswitch eventually 

#print("after doing SECOND nested switch")



print("result of the seconds it took to run is..")
print("--- %s seconds ---" % (time.time() - start_time))


