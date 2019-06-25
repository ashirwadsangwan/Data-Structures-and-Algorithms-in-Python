
def birthdayParadox(n):
    '''
    n = number of people in the room
    Our task is to find out the number of people we need so that at least two of them have the same
    birthday.
    
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

    '''
    
    total_cases = pow(365, n)
    permutations = permutation(365, n)

    return (1-(permutations/total_cases))

    


def factorial(n): return 1 if n==0 else n*factorial(n-1)
    
def permutation(n, k):
    return factorial(n)/factorial(n-k)


if __name__ == "__main__":
    n = int(input())
    print(birthdayParadox(n))