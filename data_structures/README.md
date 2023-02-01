## DAta Structures
Data structures are basically just that - structures which can hold some data together
In other words, used to store a collection of related data
There are four of them:
### Lists [item1, item2, item3]
Data structure that holds an ordered collection of items
A list is a mutable data type(can be altered)

#### A little about objects and classes
When we declare a variable , say i and assign it a value , say 5.
We can think of it as creating a an object(instance) i of class(type) 'int'. 
A list is also a class, and a class can have functions(methods) defined to use 
with respect to the class only. One can use these pieces of functionality only 
when you have an object of that class. For example, 'append' is a method of the list class 
which allows you to add an item to the end of the list. A class can also have fields(variables)
defined for use with respect to that class only. These variables/names can be used only 
when one has an object of the class.
Both the methods and fields can be accessed by the dot notation.

### Tuples (object1,object2)
A tuple is a collection of multiple objects. 
It is immutable an can be accessed using the indexing
operator

### Dictionaries {key1:value1, key2:value2}
A dictionary is a collection of key-value pairs. 
The key must be unique and immutable like a string, and the values can either be mutable 
or immutable objects
The key-value pairs are not ordered.

### Sequences
Lists, tuples and strings are sequences
The main features of sequences are:
1. Membership tests(i.e. the `in` and `not in` expressions)
2. Indexing operations, whch allows us to fetch a particular item in the sequence directly
3. Slicing operation, allows for retrieval of a slice of the sequence

### Sets
Sets are unordered collection of simple objects. 
Are used when the existance of an object in a collection is far more important than the order
 or how many times it occurs.

