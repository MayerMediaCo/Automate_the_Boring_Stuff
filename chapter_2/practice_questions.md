# Practice Questions

\1. What are the two values of the Boolean data type?  How do you writethem?

True and False - must be written with a capital letter

\2. What are the three Boolean operators?

* and
* or
* not

\3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what theyevaluate to).

The "and" Operator

| expression   | evaluation   |
|--------------|--------------|
| ------------ | ------------ |
| T & T        | True         |
| T & F        | False        |
| F & T        | False        |
| F & F        | False        |

The "or" Operator

| expression   | evaluation   |
|--------------|--------------|
| ------------ | ------------ |
| T or T       | True         |
| T or F       | True         |
| F or T       | True         |
| F or F       | False        |

The "not" Operator

| expression   | evaluation   |
|--------------|--------------|
| ------------ | ------------ |
| not True     | False        |
| not False    | True         |

\4. What do the following expressions evaluate to?

``` python
(5 > 4) and(3 == 5)
not(5 > 4)
    (5 > 4) or(3 == 5)
not((5 > 4) or(3 == 5))
    (True and True) and(True == False)
    (not False) or(not True)
```

\5. What are the six comparison operators?

* == - Equal to
* != - Not equal to
* < - less than
* \> - greater than
* <= - Less than or equal to
* \>= - Greater than or equal to

\6. What is the difference between the equal to operator and the assign-ment operator?

The equal to (==) operator evaluates expressions. The assignment (=) operator assigns values to variables

\7. Explain what a condition is and where you would use one.

Conditions are the same thing as expressions but are a more specific name in the context of flow control statements.

\8. Identify the three blocks in this code:

```python
spam = 0
if spam == 10: # block
    print('eggs') # block
    if spam > 5:
        print('bacon') # block
    else:
        print('ham')
    print('spam')
print('spam')
```

\9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```python
spam = 0
if spam == 1:
  print('Hello')
elif spam = 2:
  print('Howdy')
else:
  print('Greetings!')
```

\10. What can you press if your program is stuck in an infinite loop?

CTRL-C

\11. What is the difference between break and continue?

Break stops the loop from running and continue moves the flow of the loop along.

\12. What is the difference between range(10), range(0, 10), and range(0, 10, 1)in a for loop?

range(10) prints from 0 to the defined range

range(0,10) prints the range between two numbers

range(0,10,1) prints the range between two numbers and the steps taken between numbers

\13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

```python
# for loop
for i in range(1,11):
  print(i)

# while loop
i = 0
while i < 11:
  print(i)
  i = i + 1
```

\14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

spam.bacon()

Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.
