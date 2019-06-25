# Write a Python program that outputs all possible strings formed by using the characters "c","a","t",
# "d","o","g" exactly once.

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
        for i in range(low, high + 1):
            string[low], string[i] = string[i], string[low]
            permute(string, low+1, high)
            string[low], string[i] = string[i], string[low]
            
            
if __name__ == "__main__":
    
    string1 = ['c','a','t','d','o','g']
    low = 0
    high = len(string1)-1

    print(permute(string1, low, high))