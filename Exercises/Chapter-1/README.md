This chapter introduces you to the basics of Pyhton programming and the data types used in that. So, cut to the chase I am going to discuss only the project problems at the end of the chapter here.

## Projects
### P1: 
```
Write a Python program that outputs all possible strings formed by using the characters 
`"c","a","t","d","o","g"` exactly once.

```
To do this task first what we need to understand the problem and the problem is asking us to write all the formations of the words which contain all of the above written characters exactly once.

So, if we take first character `c` and fix it then we have 5 places to fill so the next character `a` has five choices to sit, similarly the next character `t` has four choices to choose from and so on and we can say that the initial character `c` can take any of the six places. So, it's a permutation problem where our solution would be the factorial of number of characters. This string will give us 720 new words which could be make out of these characters and which is 6!.

```python

def toString(List):
    return ''.join(List)
    

def permute(string, low, high):
    
    '''
    This function takes three parameters
    1. String
    2. start index of the string
    3. ending index of the string
    '''

    if low == high:
        print(toString(string))

    else:
        for i in range(low + 1, high + 1):
            string[low], string[i] = string[i], string[low]
            permute(string, low+1, high)
            string[low], string[i] = string[i], string[low]

```

### P2: 
```
Write a Python program that takes a number as an input and returns the number of times this number needs to be divided by 2 such that it gives you a number less than 2.
```
It is a simple problem, we'll start a counter at the top which will count the number of times the loop is iterating. The loop will keep running until the the condition inside the loop is false.

```python

def lessThan(num, identifier):
    '''
    Here we have to find the number of times the `num` should be divided by identifier such that it
    it gives you a number lesser than the identifier.
    '''
    count = 0
    while (num>=identifier):
        num = num/2
        count += 1
    
    return count

```

### P3:
```
The task here is to build a simple calculator which can perform simple arithmetics.
```

```python
def calculator(num1, num2, operator):
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    else:
        return "Operator is not found!"


```

### P4: Birthday Paradox
```
The problem is simple. But we need to make some assumptions beforehand.
    Assumptions:
                1. Birthdays of n people are unrelated. i.e. no twins.
                2. Each of 365 days are equally likely to be someone's birthday.
                3. `n` is less than or equal to 365.
    Now, if there are 366 people, we know there are atleast 2 people who share their birthday so number
    of people should be less than or equal to 365.

    Now, There are `n` people and 365 possibilities of birthdays so the total cases for all of these
    `n` people would be `pow(365, n)`.

    But finding the people who have the same birthdays is pretty hectic task but what we can do is
    we can find the people who have different birthdays and subtract them from 1 to find the desired
    results.
```

```python
def birthdayParadox(n):

    total_cases = pow(365, n)
    permutations = permutation(365, n)

    return (1-(permutations/total_cases))

    
def factorial(n): return 1 if n==0 else n*factorial(n-1)
    
def permutation(n, k):
    return factorial(n)/factorial(n-k)

```

### P5:
```
Count the frequency of each word in a given list.

```

```python
def countWord(List):
    wordCounter  = {}

    for word in List:
        if word not in wordCounter:
            wordCounter[word] = 1
        else:
            wordCounter[word] += 1

    return wordCounter
```