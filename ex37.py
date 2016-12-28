"""
and - logical condition, meaning both statements must return true (or false)
as - assigns a value to a variable for used in loops (ex. with X as Y: pass)
*assert - very useful for debugging.  Tells program to test a condition, and trigger an error if the condition is false
break - stops code when hit
class - a grouping of similar objects, used in OOP
continue - keep running through the code
def - used to define a function, class, etc.  (possible all objects?)
del - removes a value from a dictionary
elif - used in an If Statement, this follows the initial If statement if it is not met, can have numerous instances
else - in an If Statement, this catches anything that doesn't match the If (and possible elif) statements above it
*eval - accepts a single expression and returns the value of the given expression (in contrast to exec)
*except - used in a try block to properly capture and handle errors
*exec - can accept a block of code (loops, try/except, class, functions, etc), and returns 'None' (in contrast to eval)
*finally - used in a try statement, the finally clause is always executed before leaving
for - used in a For Loop (ex. for i in range(0,10))
from - defines the module to import the function from in the import statement (ex. from sys import exit)
global - declares a variable at the highest level, across the entire script
if - conditional term, if this than that.  Frequently used in If Statements
import - defines the function to import from a module (ex. from sys import exit)
in - part of For Loops and also used in tests
is - used to test equality
*lambda - used to create a function on the fly, without defining it traditionally
    (similar to function(x) in R -  Python: lambda x: x+1; R: function(x) { x + 1 })
not - flips the logical results (i.e. if a statement returned True, then wrapping with not() would make it return false)
or - used in logical operations, means just one of the statements needs to return True for the entire thing to be True
pass - tells the script to just keep on moving, useful in places where you don't need code now but plan to put in later
print - used to write to the console
*raise - used to raise your own errors, as well as re-raise the current exception in an exception handler
return - passes back a value in a function
try - attempt a block of code, if it fails then follow the except statement that follows it
while - used in a While Loop
*with - wraps the execution of a code block with a context manager (just like try/except/finally).  This ensures system
        resources are properly handled and do not overflow
*yield - used like return, but returns a generator which is a list generated on the fly and not stored in memory

########################################################################################################################

True - boolean value, returned from logical statements
False - boolean value, returned from logical statements
None - used to assign nothing to a variable
strings - format used with text
numbers - format used with integers
floats - format used with numbers tha have decimal point
lists - stores a group of items regardless of their type
dicts - similar to a list, but this has a key-value mapping for each item

########################################################################################################################
--- STRING ESCAPE SEQUENCES ---

\\ 	Backslash
\' 	Single-quote
\" 	Double-quote
\a 	Bell - play a beep sound (works on both Windows and Linux boxes)
\b 	Backspace
\f 	Formfeed - advance down to the next page
\n 	Newline - advance down to a new line
\r 	Carriage - move to the front of the current line
\t 	Tab
\v 	Vertical tab

########################################################################################################################
--- STRING FORMATS ---

%d 	Decimal integers (not floating point). 	"%d" % 45 == '45'
%i 	Same as %d. 	"%i" % 45 == '45'
%o 	Octal number. 	"%o" % 1000 == '1750'
%u 	Unsigned decimal. 	"%u" % -1000 == '-1000'
%x 	Hexadecimal lowercase. 	"%x" % 1000 == '3e8'
%X 	Hexadecimal uppercase. 	"%X" % 1000 == '3E8'
%e 	Exponential notation, lowercase 'e'. 	"%e" % 1000 == '1.000000e+03'
%E 	Exponential notation, uppercase 'E'. 	"%E" % 1000 == '1.000000E+03'
%f 	Floating point real number. 	"%f" % 10.34 == '10.340000'
%F 	Same as %f. 	"%F" % 10.34 == '10.340000'
%g 	Either %f or %e, whichever is shorter. 	"%g" % 10.34 == '10.34'
%G 	Same as %g but uppercase. 	"%G" % 10.34 == '10.34'
%c 	Character format. 	"%c" % 34 == '"'
%r 	Repr format (debugging format). 	"%r" % int == "<type 'int'>"
%s 	String format. 	"%s there" % 'hi' == 'hi there'
%% 	A percent sign. 	"%g%%" % 10.34 == '10.34%'

########################################################################################################################
--- OPERATORS ---

+ 	Addition 	2 + 4 == 6
- 	Subtraction 	2 - 4 == -2
* 	Multiplication 	2 * 4 == 8
** 	Power of 	2 ** 4 == 16
/ 	Division 	2 / 4.0 == 0.5
// 	Floor division 	2 // 4.0 == 0.0  (note: this rounds the output down)
% 	String interpolate or modulus 	2 % 4 == 2
< 	Less than 	4 < 4 == False
> 	Greater than 	4 > 4 == False
<= 	Less than equal 	4 <= 4 == True
>= 	Greater than equal 	4 >= 4 == True
== 	Equal 	4 == 5 == False
!= 	Not equal 	4 != 5 == True
<> 	Not equal 	4 <> 5 == True
( ) Parenthesis 	len('hi') == 2
[ ] List brackets 	[1,3,4]
{ } Dict curly braces 	{'x': 5, 'y': 10}
@ 	At (decorators) 	@classmethod
, 	Comma 	range(0, 10)
: 	Colon 	def X():
. 	Dot 	self.x = 10
= 	Assign equal 	x = 10
; 	semi-colon 	print "hi"; print "there"
+= 	Add and assign 	x = 1; x += 2
-= 	Subtract and assign 	x = 1; x -= 2
*= 	Multiply and assign 	x = 1; x *= 2
/= 	Divide and assign 	x = 1; x /= 2
//= Floor divide and assign 	x = 1; x //= 2
%= 	Modulus assign 	x = 1; x %= 2
**= Power assign  	x = 1; x **= 2


"""