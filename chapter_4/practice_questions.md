# Practice Questions

\1. What is []?

 `[]` represents an empty list.

\2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam` ? (Assume `spam` contains [2, 4, 6, 8, 10].)

 `spam.insert(2, 'hello')`

For the following three questions, let’s say `spam` contains the list ['a', 'b', 'c', 'd'].

\3. What does spam[int(int('3' * 2) / 11)] evaluate to?

 `'d'`

\4. What does spam[-1] evaluate to?

 `'d'`

\5. What does spam[:2] evaluate to?

 `['a', 'b']`

For the following three questions, let’s say `bacon` contains the list  [3.14, 'cat', 11, 'cat', True].

\6. What does bacon.index('cat') evaluate to?

 `1`

\7. What does bacon.append(99) make the list value in bacon look like?

 `[3.14, 'cat', 11, 'cat', True, 99]`

\8. What does bacon.remove('cat') make the list value in bacon look like?

 `[3.14, 11, 'cat', True, 99]`

\9. What are the operators for list concatenation and list replication?

The `+` operator is used to concatenate lists.  The `*` can be used to replicate lists

\10. What is the difference between the `append()` and `insert()` list methods?

The `append()` method adds the value to the end of the lsit.  The `insert()` method takes two arguments where the first argument is the position to insert the value in the list and the second argument is the value to be inserted.

\11. What are two ways to remove values from a list?

Values can be removed from lists using a `del` statement or by using the `remove()` method.

\12. Name a few ways that list values are similar to string values.

Can be itterated over, can index, slice, and use with for loops, with `len()` , and with the `in` and `not in` operators

\13. What is the difference between lists and tuples?

Lists are mutable and tuples are immutable data structures

\14. How do you type the tuple value that has just the integer value 42 in it?

`(42, )`

\15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

\16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

\17. What is the difference between `copy.copy()` and `copy.deepcopy()` ?

 `copy.copy()` is used to make a copy of a mutable value

 `copy.deepcopy()` is used to make a copy of a list within a list
