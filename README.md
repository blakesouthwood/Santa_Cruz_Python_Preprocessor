read in this order March 21,2024 Thursday evening PST Silicon Valley

radical_cs_theory

revised_cs_theory.py

//both are in raw form because of big files.
// I made more discoveries for the revised theory for more speed in revised_cs_theory.py

# Santa_Cruz_Python_Preprocessor
Feb 22 2024
Lot going on. Will add error correction code soon. 

all code will be cleaned up and commented as soon as I find the time. 

I have been dreaming up a new project that answers Dijkstra's Turing Lecture about the future of programming and it's really exciting. I need to make a  prototype for my theory in stages. 

January 18, 2024
Playing with Bard and Chat GPT I think that the codebase will be reduced by at least 90%
after I refactor it using Bard and GPT.


January 6, 2024

I learned more about coding and design on this project than on anything else I have ever coded
and I am realizing the importance of this book that I'm writing. I will carefully plan it and
write it and edit it thoroughly so that it is clear and concise and short and to the point. If there is only one thing that I'm known for thousands of years from now it will be this book which will ensure the success of any software project. And this is my title, let me see if it
it's available. It is. I am so happy. 

Ensure the Success of 
Any Software Project
And Finish Your System

This software project was a labor of love and then it crashed and burned and I have never
felt so low in my entire life. I wanted this feature to work so badly and I made many blunders along the way and there was scoope creep and rushing and not documenting and not designing or rather just in time design on the fly really. There was no pseudocodeing. Not a method anywhere within the code base. 

What saved this project was the realization of what I did right on a project that I built
'for fun to make my job easier as a phone rep in the financial industry" that I built
in my free time on weekends mostly bit by bit. That is what saved this project a previously 
successful project that was built in stages and was literally bug free. 


Jan 1, 2024
I will create new files so the difference can be seen and so the original code isn't destroyed.
The point is there will be the old and new and I will use a different main directory for the refactored
version which will be done with Bard and GPT when I find the time. 

Dec 18th 2023 9:10pm
I am looking forward to refactoring the code for the switch case and cleaning it up a little more
and simultaneously I'm writing a book about my experience of taking on a large complex project
and I will note the mistakes that I made. I will then cover what I did precisely to fix
this mammoth project. The whole project was like climbing up El Capitan sevearl times in the
winter. The first version only used stackoverflow for help a few times. The second version
will be refactored with chat gpt and bard. I only attempted this project because I really
wanted a switch case for python that looked identical to javascript with the same behavior
and halfway through I added macros which came in handy doing cool C style code in the fallthroughs. 


UPdate Dec 18th, 2023
for esthetics the switch case can be in the regular code and a comment #startswitch will be above first switch
and a comment #end switch will be at the bottom and a macro will be triggered to put the switch into
a method by the preprocessor so it will look good and run the tricky way that it's implimented. That was my dream.
I wanted it not to be in a triple string quote which looks horrible. So I just came up with that final view
and I will make a method make that happen. And each switch will be numbered to differentiate them
based in their order of occurrence starting with 0 for the first one. The numbering will be done based on 
order of occurence.


UPDATE: November 9th, 2023
I will refactor all of the code using Chat GPT and Bard before Christmas 2023. This is going to be pushed out
two weeks due to other issues I am having right now. 

I also need to add exceptions and error flagging for mangled switch case form or missing
a case where there should be one or a missing endswitch. I just realized that because I
had initially forgotten to add that error-sensing scenario. 

I will add a flag debugger to prescan through each switch case to make sure they are all
syntactically correct before proceeding and if not it will return with an error message
if something in the syntax is wrong like a missing case or misspelled switch or if there
is an indentation error somewhere within the switch case. This is necessary to prevent
translation errors by the whole program which would otherwise prevent correct translation.

I might rewrite the whole codebase in Cython for greater speed and/or write some parts
in C.

I also plan to make a separate C macro application that is in a separate module file so
it can be used in any python program utilizing a custom version of the preprocessor that
is currently used for the switch chase.  The only feature about C that I actually like
is macros. 

I had absolutely no idea how hard this project was going to be but I just kept coding.
The problem that I endured was there was no design and no map and I kept the design in
my head. I has massive scope creep but I had big hopes and dreams for my softwar working
because I  adore switch cases because they are so elegant so I kept going.
So essentially this project was making a parser and codegen and macros which is just a replace
using a preprocessor scan before running the code which is sweet to see run. 
I was in no rush whatsoever and I would listen to college radio music and go into a trance
and half a day would go by in a second and it was like the code was channeled to me because
when I am out of the trance I can't understand the code. I learned some hard lessons like
the need to precomment and design before jumping into coding anything. 


UPDATE: December 10th, 2023  I will implement my macro so that the switch case works
as a method and that way it won't look funky in a triple string assigned to a var.

What is unique and different about how this switch case works is to break the rules of Python
it works inside of a docstring that has a variable name sw to break the constraining restraints of Python
so think of it like a plastic window on an envelope and this freestyle C looking code is converted into python.
It's a multiline variable string that is interpreted in a parser and then put into lists and then fed to the code generator
that generates a multiline string which is then exec(string).

For debugging I added some methods 
hide_input_switch_string()   show_input_switch_string()  #<<==== this shows the input string for the switch before it's parsed
hide_generated_code()  show_generated_code()             #<<=== this is shows and hides the generated python code of the switche:
                                                         # it uses if elif else 
							 
The current updated version is:  official_switch_case_silver.py
The test input file is:          test_inputs_beta.py
Documentation and how it works:  angel_falls.py

Required: default case last ending with a break beneath it.
Currently indentation of 1 tab before switch(exp)
2 tabs for case line.
3 tabs for inside of case.
The next version I'm working on will be freestyle that does auto-indentation converting the input
since currently the input string is the guide post for the required indentation for die hard python finantics.


Using the switchcase  underneath I am going to impliment as macros in the preprocessor
goto label: I was in awe of goto in C and macros so that was my ultimate goal for Python
but only after getting switch case to work identical in appearanceand behavior as ANSI C.
#will likely take a week or two. Coded the goto label  a year ago but just refining it.

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
