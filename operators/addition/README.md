## Addition

In Python, the `+` sign is used to refer to addition. However, the addition is not entirely constrained to integers and floats only.

You're able to add almost all common types of Python together!

### Table of Addition

Here, you'll see what types you're able to add together. The general rule of thumb is to add only common types and try not to add two variables with different types.

|          | Strings   | Integers  | Floats    | Lists     |
|----------|-----------|-----------|-----------|-----------|
| Strings  |  **OK**   | TypeError | TypeError | TypeError |
| Integers | TypeError |  **OK**   |  **OK**   | TypeError |
| Floats   | TypeError |  **OK**   |  **OK**   | TypeError |
| Lists    | TypeError | TypeError | TypeError |   **OK**  |

### Syntax

Adding items together is as simple as using `+`, just like you would in everyday mathematics. The following are some examples:

```python
5 + 2                   # 7
'Hello' + 'world!'      # 'Hello, world!'
5 + 2.5                 # 7.5
2.1 + 4.3               # 6.4
['Hello'] + ['world!']  # ['Hello', 'world!']
```

#### Addition with variables

Just like above, simply use `+` between the items you'd like to add together to add them all up. The following are some examples:

```python
integerA = 1
integerB = 2
integerTotal = integerA + integerB  # integerTotal = 3
```

To see more examples, check out [addition.py](https://github.com/Avicity7/pyhelp/blob/master/operators/addition/addition.py)!