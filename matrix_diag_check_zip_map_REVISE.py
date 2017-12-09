def checkio(m):
    horizont=lambda m: any(False if j+4>len(m) else all(m[i][j+k]==m[i][j] for k in range(4))\
                                for i in range(len(m)) for j in range(len(m)))
    diagonal=lambda m: any(False if i+4>len(m) or j+4>len(m) else all(m[i+k][j+k]==m[i][j] for k in range(4))\
                                for i in range(len(m)) for j in range(len(m)))
    return horizont(m) or horizont(list(zip(*m))) or diagonal(m) or diagonal(m[-1::-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

    



