###=== importing files ===================
from woodstock import *
from Linus import * 
from snoopy_doghouse import * 
from tron3 import *
#from ready_player_one import * 
#from drivethru import *

####====importing lists ====================
from Linus import switch_numbers_to_transfer
from snoopy_doghouse import output #list
from tron3 import topvalue #list
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



def stage(x):
    print("#=== STAGE "+str(x)+ "==")

colorfilm=[]
silver=''
def create_generated_python_switch_methods_concatted(inputstring):
   ##==============================================
   # stage 1 woodstock.py
   print("stage 1 called in frosty")
   create_list_of_pairs_now(inputstring);stage(1); 
   ##=================================================
   # stage 2 Linus
   print("stage 2 called in frosty")
   split_up_big_string_into_nested_switches(inputstring);stage(2);        # stage 2 Linus.py  
   waterfall_chain_methods_gold_master(); stage(2);  
   ##========================================
   #stage 3 snoopy_doghouse.py   
   print("stage 3 called in frosty ==")
   create_def_switch_methods_concatted_together_in_one_string();stage(3); # stage 3 snoopy_doghouse.py
   #print("length of stnaford",len(stanford))
   print("--dec 14th ---genersted docstring  python code-----")
   for line in toocool[0].splitlines():
      print(line)
    ##========================================
   #stage 4 tron3.py   
   print("====stage 4 frosty====")
   print("calling clever_cat() from frosty now to concat the")
   print("dynamically generated python switch cases that look like javascript")
   topvalue[0]='1'
   print('here we go')
   clever_cat(); stage(4) #this triggers indirectly the exec(string) of dynamic python!!


inputstring = red_robin    
create_generated_python_switch_methods_concatted(inputstring)    
    
    #create_def_switch_methods_concatted_together_in_one_string()
print('how did it do..finished in frosty.py.')