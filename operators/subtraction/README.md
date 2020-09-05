## Subtraction

In Python, the `-` sign is used to refer to subtraction. However, unlike addition, the subtraction is constrained to integers and floats only.

### Table of Subtraction

Here, you'll see what types you're able to add together. The general rule of thumb is to add only common types and try not to add two variables with different types.

|          | Strings   | Integers  | Floats    | Lists     |
|----------|-----------|-----------|-----------|-----------|
| Strings  | TypeError | TypeError | TypeError | TypeError |
| Integers | TypeError |  **OK**   |  **OK**   | TypeError |
| Floats   | TypeError |  **OK**   |  **OK**   | TypeError |
| Lists    | TypeError | TypeError | TypeError | TypeError |

### Syntax

Subtracting items together is as simple as using `-`, just like you would in everyday mathematics. The following are some examples:

```python
5 - 2                   # 3
5 - 2.5                 # 2.5
2.1 - 4.3               # -2.2
```

#### Subtraction with variables

Just like above, simply use `-` between the items you'd like to subtract together. The following are some examples:

```python
integerA = 1
integerB = 2
integerTotal = integerA - integerB  # integerTotal = -1
```

To see more examples, check out [subtraction.py](https://github.com/Avicity7/pyhelp/blob/master/operators/subtraction/subtraction.py)!