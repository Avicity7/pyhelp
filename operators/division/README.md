## Division

In Python, the `/` sign is used to refer to division. However, the division is constrained to integers and floats only.

### Table of Division

Here, you'll see what types you're able to divide together. The general rule of thumb is to add only common types and try not to add two variables with different types.

|          | Strings   | Integers  | Floats    | Lists     |
|----------|-----------|-----------|-----------|-----------|
| Strings  | TypeError | TypeError | TypeError | TypeError |
| Integers | TypeError |   **OK**  |  **OK**   | TypeError |
| Floats   | TypeError |   **OK**  |  **OK**   | TypeError |
| Lists    | TypeError | TypeError | TypeError | TypeError |

### Syntax

Dividing items is as simple as using `/`. The following are some examples:

```python
5 / 2                   # 2.5
5 / 2.5                 # 2.0
```

#### Division with variables

Just like above, simply use `/` between the items you'd like to divide (a divided by b). The following are some examples:

```python
integerA = 1
integerB = 2
integerTotal = integerA / integerB  # integerTotal = 0.5
```

### Floor Dividing

In Python, all forms of division will always return a *float* value. In the event where you want an *integer* instead of a float, you will need to use `//` instead. The `//` symbol represents **floor division**, where the last decimal value is disregarded. Here's an example:

```python
floorA = 5
floorB = 2
floorTotal = floorA // floorB       # floorTotal = 2 (0.5 is disregarded)
```

### Zero Division Error

In Python, there exists a special form of error, known as a **`ZeroDivisionError`**. As the name suggests, this error will appear if you're trying to divide a certain value by 0; logically, in mathematics, this isn't allowed, either. Here's an example:

```python
integerC = 2
integerD = 0
integerTotalII = integerC / integerD # Prints an error message with ZeroDivisionError
```

To see more examples, check out [division.py](https://github.com/Avicity7/pyhelp/blob/master/operators/division/division.py)!