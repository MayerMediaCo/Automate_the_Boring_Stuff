# Practice Questions

\1. Why are functions advantageous to have in your programs?

Functions help compartamentalize code into logical groups.  They also provide reusability across a program.

\2. When does the code in a function execute: when the function is defined or when the function is called?

Code in a function executes when the function is called

\3. What statement creates a function?

The 'def' statement creates a function

\4. What is the difference between a function and a function call?

A function is a group of code that works together. A function call is a declaration to run those groups of code

\5. How many global scopes are there in a Python program? How many local scopes?

There is only one global scope. Local scopes are created whenever a function is called.

\6. What happens to variables in a local scope when the function call returns?

Variables in the local scope are forgotten.

\7. What is a return value? Can a return value be part of an expression?

The return value is the value an expression evaluates to. Return values can be used as part of an expression

\8. If a function does not have a return statement, what is the return value of a call to that function?

Functions that do not have a return statement always return None as a value

\9. How can you force a variable in a function to refer to the global variable?

A "global statement" can be used to force a variable to refer to the global variable

\10. What is the data type of `None` ?

 `NoneType` data type

\11. What does the import `areallyourpetsnamederic` statement do?

Importing modules allows you to use all of the functions available within that module

\12. If you had a function named `bacon()` in a module named spam, how would you call it after importing spam?

 `spam.bacon()` 

\13. How can you prevent a program from crashing when it gets an error?

You can utilize `try` and `except` statements to handle errors and avoid crashing the program

\14. What goes in the `try` clause? What goes in the `except` clause?

The code that can potentially have an error is put in a `try` clause.
What should happen instead of running the error goes into the `except` clause
