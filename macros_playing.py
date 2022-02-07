#if condition = true
#condition = "('apple == 1 and banana == 10')"
print("macros playing is a simple demonstration of the possibilities that would")
print("make is possible to write incredibly expressive Python using macros from Lisp")
print("macros are used inside of docstrings with var name")
print("===macros: demonstrated when, unless, until ========")
print("these are implimented in the same")
print("window in an envelope techneque with the code with")
print("a triple string and parsed and replacing the macro")
print("with the python equivalent though to the eye it seems")
print("like suddenly that parts of LISP are possible in Python.")
print("========================================")
'''
apple = 2
banana = 2
condition = (apple == banana)

when condition is True:
    print("True")
else:
    print('False')

##============================= 

until total < 10:
    print("not yet ",total)
    total += 1
print("now total has reached 10")

##=============================
score = 50


unless condition is False:
   print("score =",score)
   print("this worked if this shows up")
   print(" special code would run here")
   print("proving the condition was FALSE ==")
else:
   print("it is indeed true")
   print("score =",score)
   print("if it was True this would show up")


print("=======================")

'''



print("===============================")
print("====WHEN macro demonstration===")
print("===============================")

starbucks='''
apple = 2
banana = 2
condition = (apple == banana)
when condition is True:
    print("True")
else:
    print('False')

'''

#this is translated into 
#if condition == True
#which is further translated as a macro really into
#if apple == banana:

#runthis(starbucks)
print(starbucks)
starbucks =starbucks.replace('is','== ')
starbucks =starbucks.replace('when','if ') #notice the change here
#starbucks=starbucks.replace('condition', "(apple == banana)")
print("===============")
print('this is the expanded macros view')
print(starbucks) #just checking if apple == 2 and banana == 2
print("the result of the condition is:")
print("")
#this is actually computing this after the macro expansion:
#apple = "2"
#banana = "2"
#if apple == banana: #if both vars numbers are the same 
exec(starbucks)

print("===============================")
print("====UNTIL macro demonstration===")
print("===============================")

##==================================================
### macro  until ===================================
##==================================================
funny='''
   
 
total = 0
# u n t i l condition == True do something

until total < 10:
    print("not yet ",total)
    total += 1
print("now total has reached 10")
'''
print(funny)
print("=================")
funny =funny.replace('until','while ')
print("this is the expanded macro view")
print(funny)
exec(funny)


#===================================================
### macro unless ===================================
#===================================================
print("===============================")
print("====UNLESS macro demonstration===")
print("===============================")
#The code in the unless block will be executed
# if the given condition is false.
#trying u n l e s s
# if  when condition not true(meaning = False)
condition = "(score >= 40)"
stars='''
score = 50
#score= 33
unless condition == False:
   print("score =",score)
   print("this worked if this shows up")
   print(" special code would run here")
   print("proving the condition was FALSE ==")
else:
   print("it is indeed true")
   print("score =",score)
   print("if it was True this would show up")

'''



print("uses unless and condition macros")
print(stars)
stars =stars.replace('unless','if ')
print(stars)
print("====")
stars =stars.replace('condition',"(score >= 40)")
print("this is the expanded macro view")
print(stars)
print("=====")

exec(stars)




