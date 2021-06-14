aqua='''

global x
x = "one" #it was "one"              #<<=== x must be a string just as matching case == "string", 
                                       #<<=== if using a number it will be converted to a string
                                       #<<=== so x = 22   will work and be converted to "22"
tahoe=[]
tahoe.append(0)
# =======  main  ===================================
def real_main():
    testfunction(x)  #"one" is tested

victory=[]
victory.append(0)

#######################
### inner switch_1
#######################
### this is inner_switch()
def inner_switch_1(n): #test2 is the test
    print("=======inner_switch called==1==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    inswitch(n)                           #<<====== inswitch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')

        elif case  == "test2":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "test4":
            print ("testi  first nested switch ol...")
            tahoe[0]="sublime" #puts victory into tahoe[0]
            #######################
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 1")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   
###================

#######################
### inner switch_2
#######################
### this is inner_switch()
def inner_switch_2(n): #test2 is the test
    print("=======inner_switch called==2==",n)
    casetest1 = ['test5','test6']
    #this is switch inside of inner_switch
    inswitch(n)                           #<<====== inswitch() method is here

    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "test1":
            print("dam did it work?")
            print("yes it's test == one")
            tahoe[0]="victory" #puts victory into tahoe[0]
            infallthru('test2')

        elif case  == "snowman":
            print("this is inside of inners witch test2")
            
            print ("switch case behavior works in Python now!")
            break         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "test3":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            break

        elif case  == "rabbit":
            print ("te what do we have here ool...")
            tahoe[0]="mickey mouse" #puts victory into tahoe[0]
            print("tahoe[0]",tahoe[0])
            #######################
            #inner_switch_2('test7')
            #######################
            print("out of inner switch 2")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1")                            #<<==== I just put case here to show which word matched
            break

        elif case  == "test7":
            print ("gui design")
            break

    #default:
        else:
            print('None')
            break   





# =======  switch  =================================
def switch(x):
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        x = str(x)
    global case
    case = x.lower() 
    
# =======  fallthru       =========================
def fallthru(y):
    eval("switch('" + y + "')")
    
    
#==================
#for inswitch
def inswitch(n):
    if type(x) != str:  #checks to make sure it's a string if for example a number is passed as x
        n = str(n)
    global case
    case = n.lower() 

#=====================
# for infallthru    
def infallthru(n):
    eval("inswitch('" + n + "')")





casetest1 =['google', 'fishfood', 'probability']

#=====  SWITCH CASE CODE  demonstration is inside function testfunction(x) below =========
# this is a function with a switch case
# which has a nested switch case within it inside of a function called inner_switch_1
# =======   testfunction    ========================
def testfunction(x):
    print("=== testfunction called with x====TESTING THIS JUNE 9th======= ",x)
    print('test function testing switch case behavior')
#this is the switch called 
# ========  switch case code =======================
    switch(x)                           #<<====== switch() method is here
    while True:                  #<==== infinite loop used for fall thru method
        if   case  == "one":
            print("this is the first case in the main switch")
            ######################
            inner_switch_1('test4') #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch1 below")
            print("tahoe[0]=",tahoe[0]) #result of innerswitch running
            #what output is there from inner_switch?? use a list to capture it
            fallthru('word')

        elif case  == "word":
            print ("this is back in main switch now !")
            fallthru("rudolph")         #<<===== fallthru() method is here *don't use* break with fallthru()
                                        #<<===== currently it requires the next case match in quotes 
        elif case  == "rudolph":        #<<===== but later I will make it work using just fallthru()
            print ("go reindeer")
            print("=== this is 2nd nested swith differnet case switches have ended")
            ######################
            inner_switch_2('rabbit') #force feeding it for testing switch case function actually 
            ######################
            print("out of from innerswitch2 below")
            print("tahoe[0]=",tahoe[0])    
            break

        elif case  == "phrase":
            print ("testing wow works on Sublime now Coooool...")
            break

        elif case in casetest1: #['google', 'fishfood', 'probability']:   #<<==== several cases in list on one line
            print ("successful test in casetest1") 
                                   #<<==== I just put case here to show which word matched
            break

        elif case  == "22":
            print ("gui design")
            break

    #default:
        else:
            print('none')
            break         
#end loop
#end switch

testfunction('one')
'''

print('it is all in one big string about to execute it')
exec(aqua)
print("after wards we have the results above this line")