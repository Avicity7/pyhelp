## `for` loops

In Python, the `for` loop is often used to iterate through items. As long as these items are *traversable*, you'll be able to loop through them.

- [Progressing using `range()`](#progressing-using-range)
- [Progressing using items](#progressing-using-items)

### Progressing using `range()`

Imagine this scenario: you'd want Python to count all the way up to 100. Would you do this?

```python
print(1)
print(2)
print(3)
print(4)
...
```

As you can see, this is extremely ineffective and takes a *lot* of time. It's also very rigid in the sense that it only works for this purpose.

In Python, you're able to continuously loop through a range of numbers using the `range()` function!

The syntax for this is:

```python
for variable in range(startInt, stopInt):
    # Code to run every loop
```

> **Note!**
>
> `variable` here can be named whatever you'd like. In most cases, only give this variable a name only if you intend to use it in the loop. Otherwise, it is advised to use `_` (denoting that there is no variable used).

In the syntax above, you'll need to provide the values for `startInt` and `stopInt` respectively. Do note that **the value of `stopInt` is non-inclusive**, meaning that the value `stopInt`, say 100, wouldn't be counted and the loop will run only up to 99.

In the example above, we can re-write the code using a `for` loop as such:

```python
for number in range(1, 101):
    print(number)
```

That's better! Now, Python will run the loop continuously all the way from when `number` is 1 to 100.

### Progressing using items

Let's consider another variable. Let's say that you have a list of strings:

```python
strings = ["Alpha", "Beta", "Charlie", "Delta"]
```

What if you'd want to print out the names of each person individually? Would you do this?

```python
print(strings[0])
print(strings[1])
print(strings[2])
print(strings[3])
```

Or, with some knowledge for `for` loops, maybe you'd do this?

```python
for i in range(0, 4):
    print(strings[i])
```

Those are both valid ways, but as we've discussed, the first is pretty ineffective and rigid. The second one is fine, but can be risky. What happens if you entered `5` instead of `4`? You'd risk your code crashing with an **`IndexError`**.

> **What's an IndexError?**
>
> An IndexError often occurs when using `for` loops with lists. In essence, this error appears when the index exceeds the highest index of the list. Take the list above as an example. Printing `strings[4]` will result in this error, since there's nothing at the fourth index; the highest is three!

Lists are considered iterable and traversable, and therefore we can use the list instead of `range()` in the `for` loop!

Here's the syntax for this loop:

```python
for item in traversableItems:
    # Code to run every loop
```

> **Tip!**
>
> Just like above, you can name `item` to be anything you want.

> **Important!**
>
> You need to make sure that the item you're traversing *is* actually traversable. Otherwise, you'll get a `TypeError`.

Let's now implement this context with our learning:

```python
for string in strings:
    print(string)
```

Now, the loop will iterate through every item in the list and print it out. How neat!

### Conclusion

Let's consolidate our learning with the `for` loop. When is it appropriate to use the items or range?

|             `range()            |                Items                |
|---------------------------------|-------------------------------------|
| Used without traversable items  |     Used with traversable items     |
| Used for counting incrementally | Used for accessing individual items |

If you know the `while` loop, when is it suitable to use `for` or `while`?

|        `for()`        |        `while()`        |
|-----------------------|-------------------------|
| Looping through items | Repetition on condition |

When using the `for` loop, you will need to be careful. Some often errors while using the loop include:

- `IndexError`
    - What happened: You're trying to access an index not within the range of a list.
    - What to do: You're likely using the `range()` method — change the stop or integer to a different value.
- `TypeError`
    - What happened: You're likely trying to traverse a non-traversable list.
    - What to do: Check if your loop is trying to loop through anything non-traversable (not a string or list).