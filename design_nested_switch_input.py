#design_nested_switch_input.py
#main0 switch 
# June 10th, 2021 designing input for parser to analyze the nested switches
#modelled on C style design of nested switches
switch(exp) {
		case 'cholpolty':  
			#nested switch example
			##==nested 1 switch=== the nesting waterfall is dependent on====================
			##== the first switch being triggered for the others to be triggered
			print("inside of cholpolyt")
			switch(exp)
			    case 'panda express':
			        print('good food')
			        print("in hollister ")
			        adder(1)
			        buildstring('soon it')
			        print('BARK')
			
		
		        case 'starbucks':
			        print('where is my mocha')
			        
			        #nested_2 switch example
			        ##=======================
			        switch(exp)
			            case 'panda express':
			                print('good food')
			                print("in hollister ")
			                adder(1)
			                buildstring('soon it')
			                print('BARK')
			
		
		                case 'starbucks':
			                print('where is my mocha')
			                print("and my sausage sandwich...")
			                adder(2) #this won't do anything until it is executed
			                buildstring(' will work')
			                #########
			                #nested_3 switch example
			                ##=======================
			                switch(exp)
			                    case 'panda express':
			                         print('good food')
			                         print("in hollister ")
			                         adder(1)
			                         buildstring('soon it')
			                         print('BARK')
			
		
		                         case 'starbucks':
			                         print('where is my mocha')
			                         print("and my sausage sandwich...")
			                         adder(2) #this won't do anything until it is executed
			                         buildstring(' will work')
			
		
		                        case 'big testing':
			                        print('where is my mocha')
			                        print("and my sausage sandwich...")
			                        adder(3)
			                        buildstring(' and I will celebrate')
			                        break
				
		                        default:
			                        print('no results')
			                        print("that is all")
			                        break
                            }
			                endswitch  # I decided to do it this way for readability
			            ###### end nest 3=================
			                #needs break or fallthru 
		
		                case 'big testing':
			                print('where is my mocha')
			                print("and my sausage sandwich...")
			                adder(3)
			                buildstring(' and I will celebrate')
			                break
				
		                default:
			                print('no results')
			                print("that is all")
			                break
                        }
			            endswitch  # I decided to do it this way for readability
			            ##### end nest 2============
		                #have to be break or fallthru here
		        case 'big testing':
			        print('where is my mocha')
			        print("and my sausage sandwich...")
			        adder(3)
			        buildstring(' and I will celebrate')
			        break
				
		        default:
			        print('no results')
			        print("that is all")
			        break
                }
			    endswitch  # I decided to do it this way for readability
		        #have to be break or fallthru here (just realized this)
		        ####= end nest 1================
		case 'panda express':
			print('good food')
			print("in hollister ")
			adder(1)
			buildstring('soon it')
			print('BARK')
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(2) #this won't do anything until it is executed
			buildstring(' will work')
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3)
			buildstring(' and I will celebrate')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)
#main switch