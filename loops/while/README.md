## `while` loops

In Python, the `while` loop is often used to recursively run specific code on a specific condition. It is recommended to use the `while` loop with a condition that can end; otherwise, your code may loop forever and waste useful resources!

## Progressing with `while` loops

Imagine this scenario: you would like to have a counter alongside printing the product of 5 and the counter number. If you have prior knowledge on the `for` loop, you'd likely consider doing this:

```python
for i in range(1, 101):
    print("Loop " + str(i))
    print(5 * i)
```

This works fine, but you can also use `while` loops instead!

Here's the syntax for `while()` loops:

```python
while condition:
    # Code to run while condition is True
```

> **Note!**
>
> As much as possible, try to make sure that `condition` doesn't always resolve to True. Otherwise, you'll get an *infinite loop* and the user will need to manually intercept the program to stop it.

Let's try to understand the solution for the context above using a `while` loop:

```python
counter = 1

while (counter <= 100):
    print("Loop " + str(counter))
    print(5 * counter)
    counter += 1
```

As you can see, the `counter` variable is incremented by 1 every time the loop runs. That way, the loop doesn't run infinitely, but stops just after counter is 100.

## Conclusion

Let's consolidate our learning with the `while` loop. If you know the `for` loop, when is it suitable to use `for` and `while`?

|        `for()`        |        `while()`        |
|-----------------------|-------------------------|
| Looping through items | Repetition on condition |

When using the `while` loop, you will need to be careful. One common error while using the loop is:

- Infinite looping
    - What happened: The condition of your `while` loop has never resulted to `False`, causing your loop to infinitely loop.
    - What to do: Try to see if there are any logical errors in your code.