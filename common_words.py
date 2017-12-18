def checkio(first, second):
    both_lines = (",".join([first, second])).split(",")
    common_words = []
    for i in both_lines:
        if both_lines.count(i) >=2:
            if i not in common_words:
                common_words.append(i)
    
    res =",".join(sorted(common_words))
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
