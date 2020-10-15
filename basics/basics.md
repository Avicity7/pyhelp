## Basics

If you're here, you'd probably like to know more about Python before exploring more. That's great!

This file will hopefully give you a basic rundown of essential Python knowledge and syntax.

### Table of Contents
- [Types](#types)
- [Variables](#variables)

### Types

In Python, there are many common types that you may want to use. Here is a list of the few common types of data used:

|        Type        |      Examples     |
| ------------------ | ----------------- |
| Integers (`int`)   | `5`, `10`, `-5`   |
| Floats (`float`)   | `0.25`, `1.0`     |
| Strings (`str`)    | `"Hello world!"`  |
| Lists (`list`)     | `[0, "a", 0.25]`  |
| Tuples             | `("4 div 2", 2)`  |
| Dictionaries       | `{"name": "John"}`|

#### Integers

In Python, integers are any real numbers that are **whole numbers**. If you would like to use numbers with decimal points, use floats instead.

##### Examples of Integers
```python
5
15
-1000
1234
```

#### Floats

Similar to integers, floats hold numerical values. In contrast with integers, though, floats are meant to contain numbers with **decimal points** (or fractional parts).

Some of Python's native abilities like *division* and *multiplication with floats* will always return a float.

##### Examples of Floats
```python
2.5
3.0
-56.4
12.34
```

##### Issues and Limitations

There may be some instances where performing operations can lead to unexpected results. Take a look at the example below, for example:

```python
>>> 0.1 * 0.2
0.020000000000000004
```

This unusual behaviour is expected; for clarification, take a look at the [official Python documentation](https://docs.python.org/3.8/tutorial/floatingpoint.html). This can cause unexpected results in other situations, too. An example would be when rounding off floats:

```python
>>> round(0.5)
0
```

It's therefore recommended for you to make sure that you run your program and test it vigorously for any bugs. Logic errors are the hardest to catch but are the most prone of being undetected due to their state of being non-fatal errors.

#### Strings

In Python, strings represent any value that holds **text**. In most cases, you would need to use `"` (quotation marks, **not** the left/right double quotation marks) or `'` (apostrophe) to declare strings.

> **Note!**
>
> Note that in string declarations, the quotation marks used must be consistent; `"Hello world!'` ***will*** result in error).

##### Examples of Strings
```python
"Hello world!"
'My string'
"Testing 123"
```

#### Lists

In Python, you can think of lists as boxes where you can have different types of data inside, including lists themselves! This feature is especially helpful if you'd like to deal with some data. To declare a list, use `[` and `]` (opening and closing square brackets) and put the contents of the list inside and separate them with `,` (comma).

##### Examples of Lists
```python
['My', 'list', 1, 1.5, ['papaya', 'banana']]
['Alpha', 'Beta', 'Charlie', 'Delta']
```

##### Traversing and Navigating through Lists

Everything in lists are often termed **items** or **elements**. With lists, you're able to *traverse* (go through) a list and pick out individual items. The location of the item relative to the list itself is known as an **index**. Don't worry; we'll help you with it!

Here are some tips for traversing lists:
- Python, like most (if not all) programming languages begin counting indexes with `0`.
- The syntax of picking out an individual item is `listName[index]`.
- The syntax of picking multiple items is `listName[startIndex: stopIndex]`. Note that the item in `stopIndex` is **non-inclusive** (will not be part of this selection).
- You can use the above with a *step* (skipping multiple selections)

```python
['Alpha', 'Beta', 'Charlie', 'Delta']

# 'Alpha', 'Beta', 'Charlie', 'Delta' are the items in this list. This list has a total of four items.
# 'Alpha' is the first item; therefore, it will have the lowest index. Remember that Python starts counting from 0, thus:
# 'Alpha' has an index of 0
# 'Beta' has an index of 1
# 'Charlie' has an index of 2
# 'Delta' has an index of 3
```

```python
myList = ['Alpha', 'Beta', 'Charlie', 'Delta']

# Picking out individual items
firstItem = myList[0] # myList[0] = 'Alpha'
print(firstItem)      # Prints Alpha


# Picking out multiple items
firstThree = myList[0:3] # Contains up to 'Charlie', 'Delta' is non-inclusive!
print(firstThree)        # Prints ['Alpha', 'Beta', 'Charlie']

# You can also do this!
firstThreeNew = myList[:3] # Python assumes start is 0
print(firstThreeNew)


# Picking out multiple items with step
pattern = myList[::2] # Selects all items, but skips every second item.
print(pattern)        # Prints ['Alpha', 'Charlie']
```

##### Handling Lists

You can use some of Python's existing *methods* to handle lists. **Methods** are often called by `.method()` following a type, but is not entirely restricted to this rule. Here are a few handy methods for lists:

- `append(item)` — adds `item` to an existing list.
```python
myList.append('Eagle') # Becomes ['Alpha', 'Beta', 'Charlie', 'Delta', 'Eagle']
```

- `remove(item)` — removes `item` from an existing list. `item` must be an actual value; failing to do so will result in a `ValueError`.
```python
myList.remove('Delta') # Becomes ['Alpha', 'Beta', 'Charlie', 'Eagle']
```

- `pop(index)` — removes the item at `index` and also returns it.
```python
removedVariable = myList.pop(0)
print(removedVariable) # Prints Alpha
```

Besides methods, you can also use these:

- `+` — adds two lists together.
```python
listA = ['Hello']
listB = ['world!']
print(listA + listB) # Prints ['Hello', 'world!']
```

#### Tuples

Similar to lists, tuples can store data of different types. The main difference between tuples and lists is that tuples are **immutable**; once you've set the values of a tuple, you *cannot* change it at all. Tuples are generally useful to use when you want to group certain related information. To declare a tuple, use `(` and `)` (opening and closing brackets).

##### Examples of Tuples
```python
('banana', 'yellow')
()
```

> **Note!**
>
> To declare a tuple with one element, you need to add a `,` (comma) after the first element, like so:
>
> ```python
> myTuple = (1,)
> ```


#### Dictionaries

Dictionaries are meant to store data, just like lists and tuples. The only caveat is that you are bound to a `string: any` format. Dictionaries also look similar to JSON, and so they are likely the type you'll be handling with when handling JSON files. To declare a dictionary, use `{` and `}` (opening and closing curly brackets).

##### Examples of Dictionaries
```python
{ 'name': 'Johnny' }
```

##### Handling Dictionaries

The syntax of dictionaries are somewhat different compared to lists and tuples; instead of index, dictionaries rely on **keys**. Keys are the first items in a `string: any` format (as an example, the key of the dictionary above is `name`).

To select an individual item, you need to know the key of the item:

```python
print(dictionary['name']) # Prints Johnny
```

To add and update items, use the same syntax above. The key needs to be something that doesn't exist. Otherwise, it'll overwrite the value with that key.

```python
myDictionary = { 'name': 'Johnny' }
myDictionary['age'] = 15 # Adds new item 'age'
myDictionary['name'] = 'John' # Replaces 'Johnny' with 'John'
```

### Variables

In Python, variables are user-defined terms that can hold values for use later on. In some programming languages, you will need to denote whether the variable is *mutable* (can be changed) or *immutable* through `let`/`val` and `var`. However, Python doesn't need this explicitly.

To declare a variable in Python, use the following syntax:

```python
variable = items
```

From then on, `variable` will have the value of `items`.

#### Application

Take the dictionary case above as an example:

```python
myDictionary = { 'name': 'Johnny' }
```

Now, `myDictionary` stores the value of a dictionary (`{ 'name': 'Johnny' }`). Instead of having to use `{ 'name': 'Johnny' }` every single time, you can use `myDictionary` instead. Furthermore, you'll often need to declare dictionaries as variables to do useful things with them.

Here are a few more examples of variables:

```python
myFavouriteNumber = 5
myFavouriteMultiple = 2

# You can do basic arithmetic (as long as the types involved are logical!), too!
print(myFavouriteNumber * myFavouriteMultiple)
print('Hello, world!' * 2)
```