# Santa_Cruz_Python_Preprocessor

The current updated version is:  official_switch_case_silver.py
The test input file is:  test_inputs_beta.py
Documentation and how it works:  angel_falls.py


June 9th, 2021 8 am California time.
The switch case now works and macros work for numbers case 1 thru 10:   and case 100 to 200:
Two tumblers work for doing dynamic coding in Python like what is possible in JavaScript in
a switch case. Adder does math adding in a demonstration and Buildstring concats strings
in waterfall fashion when tumbling between cases that have implicit or explict fallthrus.
The absence of a break is an implicit fallthru.
Explicit fallthrus look  like this fallthru  or fallthrough.

The switch engine works now without reloading the module.
C style UPPERCASE constant example.
clever('PALOMAR')
#right now it NEEDS to take strings to digest and parse it"
#I need to add my new code for this to work properly"
show_input_switch_string()   #input so what the string right below here
show_generated_code()

sw =''' 
	switch(exp) {
		case CASPER:  
			print(\"squirt gun!\")
			print("water everywhere")
			break
			
		case COYOTE:
			print("Sesame Street")
			print(" groucho and animal")
			print("this is so fun")
			break
			
		case PALOMAR:
			print("it actually works")
			print(" third attempt")
			print("deer and quail about")
			
			
		case LAKE_TAHOE:
			print("good skiing")
			print(" alpine meadows")
			print("all of the stars")
			break
			
		case FRANCE:
			print("massive ship blocking canal in Egypt")
			print("it was stuck for six days")
			
			
		case AMERICA:
			print('manure')
			print("no more horses")
			break
		
				
		default:
			print('one walking quack d')
			print("walking geese")
			break
}
'''
endswitch(sw)

#traditional switch case
clever('rasberries and cream') #this would change varholder[0] 

#show_generated_code()

sw ='''
	switch(exp) {
		case 'rasberries and cream':  
			print("wheres the cream house")
			print("tastes good at cafe borrone")
			break
			
		case 'gone fishing':
			print('fallen leaf lake')
			fallthrough	
			
		case 'driving car':
			print('where is the gti')
			print("really a porsche...")
			
			
		case 'macbook pro':
			print('fast laptop')
			print("when will the code work...")
			break
			
		default:
			print('six walking duck de fa ul t')
			print("flying geese")
			break
}
'''
endswitch(sw)


clever('star wars') #this would change varholder[0] 

#hide_generated_code() #from this point forward

print("-----3rd switch -------")

sw ='''
	switch(exp) {
		case 'star trek':  
			print(\"energize!\")
			print("beam me up")
			print("Captain Kirk")
			break
	
		
		case 'Star Wars':
			print('return of the jedi')
			print("Luke Skywalker ")
			fallthru
		
		case 'Darth Vader':
			print('flying in it tie-fighter')
			print("the force is strong in this one...")
			break
			
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)


#example using tumbler
clever('panda express')
#show_input_string()   #input so what the string right below here
#show_generated_code() #output
hide_input_switch_string()   #input so what the string right below here
hide_generated_code()

sw ='''
	
	switch(exp) {
		case 'cholpolty':  
			print(\"burrito!\")
			print("bowl")
			print("lemonade")
			break
	
		
		case 'panda express':
			print('good food')
			print("in hollister ")
			adder(2)  #<<=== adder does math takes a number and adds it to rolling total
			buildstring('merry')
			print('BARK')
			
		
		case 'starbucks':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(3) #this won't do anything until it is executed
			buildstring(' christmas')  #<<=== buildstring concats strings between cases via fallthrus
			
		
		case 'big testing':
			print('where is my mocha')
			print("and my sausage sandwich...")
			adder(7)
			buildstring(' and happy new year')
			break
				
		default:
			print('no results')
			print("that is all")
			break
}
'''
endswitch(sw)

#number switch case
clever('7')

hide_input_switch_string()   #input so what the string right below here
hide_generated_code()

sw = '''
	switch(exp) {  
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
			print("where's the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru

		case 6:
		case 7:
		case 8:
		case 9:
		case 10:
			print('kangaroo hop hop!')
			print('taught me how thru write code')
			break
					 
		case 11:
		case 12:
		case 13:
		case 14:
		case 15:
			print('mocha blast')
			print('== 31 flavors===')
			print('== at Starbucks in Gilroy ===')
					

		case 16:
		case 17:
		case 18:
		case 19:
		case 20:
			print('sweet sixteen ski fast in the powder')
			print('sweet powder snow, lovely snow')
			break
			
			
		case 21:
			print('Heavenly valley')
			print('big snow flakes there and moggles')
			break
			
		case 26:
			print('oh yeah')
			print('tahoe here I come')
			fallthru
			
		case 27:
			print('fuck yeah')
			print('go baby go fly dammit')
			break
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			
			break
}
'''
endswitch(sw)

#number switch case using macros to and thru
clever('2') #this would change varholder[0] 

print("this is a REAL MACRO TEST ON THE REAL CODE ENGINE ")
#show_input_switch_string()   #input so what the string right below here
#show_generated_code()

hide_input_switch_string()   #input so what the string right below here
hide_generated_code()
#show_generated_code()
  
sw ='''
	switch(exp) {  
		case 1 thru 3:
			print("where\'s the dog house!")
			print('first prize')
			print('you block head Charlie Brown')
			fallthru
			
		case 4 to 7:
			print('kangaroo hop hop!')
			print('taught me how to write code')
			fallthru
			
		 
		case 8 to 10:
			print('mocha blast')
			print('== 31 flavors===')
			fallthru
			
			
		case 21:
			print('Blake you did it a real good job')
			print('macros working in Python')
			print(' I did it - it works')
			
			
			
		default:
			print('six walking duck de fa ul t')
			print('flying geese')
			break
}
'''
endswitch(sw)

#I am currently taking out the print statements 


Dec 28th, 2020
talk about a photo finish. Finally got javascript switch case working in python. the dream has been realized.
What a rush. Totally mind blowing. Wow.
One switch currently works. Will work on adding numbers and having several switches.
I have done nested switches working but not ready for here yet.
I did this because the Harvard Professor in CS50 said Python didn't have a switch case ... so I made one.
Updating later tonight. So cool. 
Preprocessor for Python to make code more readable, faster to write and test, fewer bugs, increase productivity
I wanted to make Python faster and easier to code and think in so I did.
Since this project has grown and will represent several cool features I'm calling
it JetPack.
