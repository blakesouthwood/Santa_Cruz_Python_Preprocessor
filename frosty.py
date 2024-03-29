###==== importing files ===================
from woodstock import *          #  1,845  lines of code
from Linus import *              # 27,105  lines of code
from snoopy_doghouse import *    # 12,329  lines of code
from tron3 import *              #    397  lines of code

####====importing lists ====================
from Linus import switch_numbers_to_transfer #list
from snoopy_doghouse import output           #list
from tron3 import topvalue                   #list
#############################################
#from Linus import switch_numbers_to_transfer# alist
# december 13th, 2021 Monday 10;35 am Morgan Hill Starbucks, California
print("== running from frosty.py ====")
varholder=[];
varholder.append(0)

red_robin ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you super smart head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			#############
			switch(exp){  
				case 'blable':
					print("do something")
					####################
					switch(exp){   
						case 'tahoe':
							print("do something")
							print("yep")
							fallthru
						case 'fallen leaf lake':
							print("nice")
							####################
							switch(exp){   
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
					endswitch #38
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
			switch(exp){ 
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
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
		
		default:
			print('the end')
}
'''	

inputstring =''

#print("======== STAGE 1 ====woodstock.py=================")
#inputstring = red_robin
#create_list_of_pairs_now(inputstring); #makes switch,endswitch line number pairs
#calling functions in linus uses gold_list
#this separates the switches built using copy body using pairs x,y  
#this needs to be called before filling the list obviously 

#print("======== STAGE 2 ====Linus.py =================")
#split_up_big_string_into_nested_switches(red_robin)  
#waterfall_chain_methods_gold_master() 
#should output the quail list of strings ready for bypass205()

#print("======== STAGE 3 ====snoopy_doghouse.py=================")
#create_def_switch_methods_concatted_together_in_one_string()
#print("after finishing snoopy_doghouse.py")
#output combined python switch methods ready to be executed.


#https://www.youtube.com/watch?v=X0Hyxq7iOwI
#reducing lines for stage 3
def show_generated_code():
    print("show generated python switch methods code")
    for line in toocool[0].splitlines():
      print(line)
      
def stage(x):
    print("#=== STAGE "+str(x)+ "==")

#reducing lines of code for  stage 2
def split_up_switches_and_prepare_for_parser(inputstring):
   split_up_big_string_into_nested_switches(inputstring);stage(2);  
   waterfall_chain_methods_gold_master(); stage(2);  

colorfilm=[]
silver=''
##==================================================================
##  create_generated_python_switch_methods_concatted(inputstring):
##===================================================================
def create_generated_python_switch_methods_concatted(inputstring):
   ##==============stage 1==uses woodstock.py==============================
   print("stage 1 called in frosty=== ") #pairs of switch and endswitch by tab depth
   create_list_of_pairs_now(inputstring);stage(1); 
   ##=============stage 2===uses Linus.py=================================
   print("stage 2 called in frosty=== ") #get each switch case body 
   split_up_switches_and_prepare_for_parser(inputstring)
   ##=============stage 3====uses snoopy_doghouse.py=======================
   print("stage 3 called in frosty=== ")  # stage 3 snoopy_doghouse.py
   create_def_switch_methods_concatted_together_in_one_string();stage(3);
   show_generated_code()
   print("--dec 14th -2021--generated docstring  python switch case code methods-----")
   ##============stage 4====uses tron3.py========================
   print("stage 4 called in frosty== concat the dynamically generated python= ",topvalue[0])
   clever_cat(); stage(4) #this concats the python switch methods and exec(code)


topvalue[0]='1'
inputstring = red_robin    
create_generated_python_switch_methods_concatted(inputstring)    
    
    #create_def_switch_methods_concatted_together_in_one_string()
print('how did it do..finished in frosty.py.')