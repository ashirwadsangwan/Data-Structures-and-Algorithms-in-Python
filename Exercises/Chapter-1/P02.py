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

if __name__ == "__main__":
    num = 16
    identifier = 2
    print(lessThan(num, identifier))

