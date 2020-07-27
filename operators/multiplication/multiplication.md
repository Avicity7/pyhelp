## Multiplication

In Python, the `*` sign is used to refer to subtraction. However, multiplication is not entirely constrained to integers and floats only.

### Table of Subtraction

Here, you'll see what types you're able to add together with. The general rule of thumb is to add only common types, and try not to add two variables with different types.

|          | Strings   | Integers  | Floats    | Lists     |
|----------|-----------|-----------|-----------|-----------|
| Strings  | TypeError |   **OK**  | TypeError | TypeError |
| Integers | **OK** |   **OK**  |  **OK**   | **OK** |
| Floats   | TypeError |     **OK**    |     **OK**    | TypeError |
| Lists    | TypeError | **OK** | TypeError |     TypeError    |

### Syntax

Multiplying items together is as simple as using `*`, just like you would in regular mathematics. The following are some examples:

```python
5 * 2                   # 10
5 * 2.5                 # 12.5
"MyString" * 3          # MyStringMyStringMyString
```

#### Multiplication with variables

Just like above, simply use `*` between the items you'd like to multiply together. The following are some examples:

```python
integerA = 1
integerB = 2
integerTotal = integerA * integerB  # integerTotal = 2
```