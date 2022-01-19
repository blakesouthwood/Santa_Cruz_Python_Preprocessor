import tahoe_dream1_working_bliss
from tahoe_dream1_working_bliss  import * 

fishy=''' 
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you genius coder  Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			exp='more'
			switch(exp){   # === line 10 beginning of single nested switch ======      
				case 'blable':
					print("inside of the inner sw here")
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
			print('== baskin robins ice cream on El Camino Real===')
			fallthru
		
		default:
			print('the end')
}
'''


red_robin ='''
	switch(exp){  
		case 1 thru 6: 
			print("test make it happen. go up to the Donnor Summit!")
			print('this has taken my breath away. it actually works')
			print('how is this even possible Tahoe beckens, yes way ')
			
			
		case 7 to 10:
			print('OH mY GOD Is THIS WORKING Jason Borne  between 7 and 10 !')
			#############
			exp ='blable'
			switch(exp)  
				case 'blable':
					print("we are blable here   inside of sw itch 11 this is really cool ")
					print("this is really working, fantastic...")
					result[0]="Blake did it"
					#break
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
			print('big numbers here  ')
			print('=this is the last c ase ==')
			print('-----------------')
			break 
		default:
			print('no matches so sorry about that chap')
			print(' ')
}
'''	


print("===doing testing now....====")
num = 1#1    
main_control_sequencer(num,red_robin)#red_robin  #this will be the the modifed endswitch eventually 


#print('========now for test 2======')

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
