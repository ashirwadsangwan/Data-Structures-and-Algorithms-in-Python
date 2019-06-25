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