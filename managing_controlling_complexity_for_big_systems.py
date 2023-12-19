Coding and designing the switch case was 
a nightmare due to the bugs and I essentially
winged it with little design up front.

I never doubted that it would work but half
way through it became too difficult to fathom
and control and comprehend.

I read up on Alan Perlis, Dijkstra, Tony Hoare,
and the NATO 1968 and 1969 papers and actually
read all of Dijkstra's papers on his Texas
web site and he mentions unmanaged complexity.

I disected my program and reverted to how I built
a huge complex program from individual programs
in the financial industry that had databases
and did complex financial calculations in real-
time and based on that approach that worked I
split up the switch case program into a ton
of files. I then refactored everything so that
multipage functions were reduced to half a page
with methods that had verbs in them.

I debugged the parser and codegen and released
that and then one by one added (connected)
a each new feature until it was working smoothly.
I made each feature a separate program and made
sure it was bug-free before connecting it.

I ended up implimenting nearly all of Yale University's
specs on C for the switch case. I got ambitious
on macros. I figured out how to impliment a C goto
using the switch case code too but it's not
included (but it works) to not insult Dijkstra
though Don Knuth is an advocate for gotos.
I will include the code later.

So after I added the features one by one and
did lots of testing it worked and I was not happy
about having it work within a triple quote string
but that was the only way I knew it would work
anywhere without interferring with other code
since it's not standard Python.

My point is in making the switch case I coded mostly
at night listening to music with headpones and
was in Flow Mode and the code wrote itself.
I was designing while coding and it worked but
the next morning I couldn't figure out what the code
was doing.

So I cleaned up the code and modularized it into
subsystems and did massive refactoring which I've
never really done before to make the code readable
and intelligible and I mapped out the design
in the process to see what the design of the
program actually looked like.

I am writing a book about how I saved this failing
project and how I managed the complexity and 
simplified everything and used an Agile Approach
which was based on my readings of Watts Humphrey
at IBM and Tony Hoare's Turing paper. It was
a triumph to succeed after defeat.

In the process of fixing the broken program that
was mired in chaos and unreadable super complex
code I triumphed. 

Previously I have read about the high failure
rate of large software projects and I wondered
what why they failed. Well I learned the hard
way it's due to feature creep, not documenting,
not commenting, not designing/planning before
hand most of all not writing pseudocode and 
not designing up front.

But I felt nonetheless victorious after
saving the project which for many months
was a sinking ship. I was patient and didn't
rush and I would constantly backup my code.

So I am writing a kindle book about how I saved
a huge project that was on the brink of failing
due to unimaginable complexity.

This project was the size of a woolly mammoth and
I was not intimidated by the size of the codebase but
the complexity was mind-boggling. I repeatedly referred
to this system project as scaling El Capitan
in Yosemite in the winter. The progress so slow. 

I would build a small part of a feature and fight 
the computer trying to get it working due to the
unreal innumerable bugs. The bugs were super
confusing and they had to do with sometimes bad 
logic but other times not knowing if the code
was doing the right behavior or even if the
behavior was even being run. There were so many
unknowns.

Enlightenment only came to me when I switched to using
Visual Studio Code so that I could step through my
code and see the values of all of the variables 
at each step and that made all of the difference in the
world.

The complexity meant I had no idea how the system worked
because I never designed it - I winged it - and I didn't
actually know how the system worked when it was running
and what was being called (functions) and I also didn't
know how to to zero in on the bugs which were deeply inside
of the code base. The bugs wouldn't say "here we are" rather
I had to add phases with print statements to show me
what had been reached and what the var values were
SO THAT I COULD SEE WHAT THE DUMB MACHINE SAW WHEN AND WHERE
and only then could I move forward. So I was essentially
creating a tool to understand what the code was doing
'and how to debug my bloody code that was pissing me off.

I wanted to move forward with momentum and I kept getting
bogged down in the swamp of what the code was doing and
trying to pinpoint where the code instructions (the logic)
was wrong and the road map course that the cursor like
a Tron motorcycle was running through. I look at the code as
if it's on a grid-like in the Tron movie on a flat surface
rather than top-down so that I can visualize it better.

I started making real progress when I split up the system
into submodules and put each feature into a separate file
to prevent bugs from propagating throughout the system. 







Blake Southwood

