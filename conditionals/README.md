## Conditionals

### Table of Contents

- [What are conditionals?](#what-are-conditionals)
- [`if` statements](#if-statements)
- [`elif` statements](#elif-statements)
- [`else` statements](#else-statements)
- [Important points](#important-points)
- [Test your learning](#test-your-learning)

### What are conditionals?

As their names suggest, conditionals refer to specific code features in Python that allow you do run certain code on a specific condition. In Python (and almost any other programming language, too), you're likely to deal with conditionals a lot, more likely than not in the form of the **`if-elif-else`** statement.

Let's walk you through conditionals!

---

### `if` statements

Let's set a context: imagine yourself going to work/school. What would be the steps that you'd take before leaving your place of residence?

You may think of:

- taking the bus when it's raining
- walking (assuming your workplace/school is nearby) when it's not

In a normal English sense, you'd likely say:

> *If it's raining, I'll take the bus. Otherwise, I'll just walk.*

Similarly, the syntax of Python's `if` statement is similar!

```python
if condition1:
    # Code to run when condition1 is true
```

Using the context above, let's suppose that it *is* raining. We also suppose `takeTheBus()` to be a function that represent taking the bus. We'll likely do something like:

```python
isRaining = true

if isRaining:
    takeTheBus()
```

> **Tip!**
>
> In the statement `if isRaining`, most people may usually do it as `if (isRaining == true)`. This isn't necessary, since `isRaining` is already a boolean value. Unless you're using other types, you can just use the variable itself.

### `elif` statements

Let's say that you have an alternative scenario where if it's not raining but windy, you'll want to walk indoors as much as possible.

In Python, the `elif` (else if) statement is up next after the `if` statement. As the name suggests, `elif` simply means "otherwise, on this condition, do this instead". 

The syntax of `elif` statements is as follows:

```python
if condition1:
    # Code to run when condition1 is true
elif condition2:
    # Code to run when condition2 is true
```

> **Tip!**
>
> You're free to add as many `elif` statements as you'd like. Note, though, that if you'd like the opposite of `condition1` to run (for example, when it is not raining), then you may want to consider using `else` instead.

Let's use the example above. We'll say that `walkIndoors()` is a function already declared.

```python
isRaining = true
isWindy = true

if isRaining:
    takeTheBus()
elif isWindy:
    walkIndoors()
```

### `else` statements

Earlier on, we covered both `if` and `elif`. Now, we'll cover `else`. In contrast to `elif`, `else` runs only after all conditions have failed (in the example, if `isRaining` and eventually `isWindy` results to `false`, then the `else` portion will be run). 

This is useful for catching all and any other conditions when all your conditions fail; in other words, `else` acts as the "otherwise" statement.

The syntax for the `else` statement is as follows:

```python
if condition1:
    # Code to run when condition1 is true
elif condition2:
    # Code to run when condition2 is true
...
else:
    # Code to run when all previous conditions are false (an exception)
```

Using the context above, let's finally compile all of them in a full `if-elif-else` statement! We'll suppose that `walk()` is the function that does exactly as it describes: walking.

```python
isRaining = true
isWindy = true

if isRaining:
    takeTheBus()
elif isWindy:
    walkIndoors()
else:
    walk()
```

---

### Important points

- [What can be optional?](#what-can-be-optional)
- [Can I order `if-elif-else` randomly?](#can-i-order-if-elif-else-randomly)

#### What can be optional?

In declaring conditionals based on the `if-elif-else` statement, the `elif` and `else` statements are optional.

```python
# OK
if (input() == '5'):
    print('Input is 5.')
```

#### Can I order `if-elif-else` randomly?

No, you can't! It's also not logically right to have the otherwise `else` or `elif` before the actual condition `if`.

```python
# This is wrong!
else:
    print('Hello!')
if (input() == '5'):
    print('Input is 5.')
```

### Test your learning

Think you've gotten the idea of conditionals? Try this question to see if you can implement it! Fire up IDLE (or other text editors of your choice) and let's go!

1. [Grades](#grades)
2. [Temperatures](#temperatures)

#### Grades

You're a teacher working on creating a system that can automatically generate a student's grade. This table describes the school's grading criteria:

|    Score (inclusive)     | Grade |
|--------------------------|-------|
|       39 and below       |   F9  |
|         40 - 44          |   E8  |
|         45 - 49          |   D7  |
|         50 - 54          |   C6  |
|         55 - 59          |   C5  |
|         60 - 64          |   B4  |
|         65 - 69          |   B3  |
|         70 - 74          |   A2  |
|       75 and above       |   A1  |

Write your code that takes in a score and prints out the corresponding grade.

##### Helpful Tips

- Use the evaluative symbols (`==`, `<`, `>`, `<=`, `>=`) to compare values. Note that you need to make sure that the input is an integer.
- Use Python's `input()` function to get the user's input on the score to be checked.
    - If you're planning to use evaluating symbols, consider type casting your input to integers using `int(input())`.
- You may need multiple `elif` statements.

##### Solutions

Coming really soon!

#### Temperatures

You're someone who, for whatever reasons, love temperature. In fact, you've gathered interesting information on temperatures, and would like to share with people about how each temperature feels like. This table describes what should be outputted from your code later on; this code assumes the Celcius scale (sorry, Fahrenheit):

| Temperature (°C) |    Description   |
|------------------|------------------|
|  -30 and below   |    Really cold!  |
|     -29 - 0      |    Pretty cold   |
|      1 - 15      |  Pretty average  |
|     16 - 25      |    Pretty warm   |
|     26 - 32      |    Fairly hot    |
|   33 and above   |    Really hot!   |

Write your code that takes in a temperature and prints out the corresponding description.

##### Helpful Tips

- Use the evaluative symbols (`==`, `<`, `>`, `<=`, `>=`) to compare values. Note that you need to make sure that the input is an integer.
- Use Python's `input()` function to get the user's input on the score to be checked.
    - If you're planning to use evaluating symbols, consider type casting your input to integers using `int(input())`.
- You may need multiple `elif` statements.

##### Solutions

Coming really soon!

