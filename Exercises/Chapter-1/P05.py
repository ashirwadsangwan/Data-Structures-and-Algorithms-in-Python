def countWord(List):
    wordCounter  = {}

    for word in List:
        if word not in wordCounter:
            wordCounter[word] = 1
        else:
            wordCounter[word] += 1

    return wordCounter


if __name__ == "__main__":
    words = str(input().split())
    print(countWord(words))
