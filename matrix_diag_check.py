def checkio(a):

    r = -1
    res1 =0 
    res2 = 0
    res3 = 0
    res4 = 0
    s = 0
    q = 0
    done = False
    for i in a:
        r += 1
        print("iter ______________________________",r, i)
        c = -1
        for ii in i:
            c += 1
            print("index",r,c)
    
            try:
                s = r
                q = c
         #       print("true RC:", r,c)
          #      print("check", r,c)
                while a[r][c] == a[s+1][q]:  #to down
                    res1 +=1
                    s = s + 1
                    print ("down - ",res1)
                    if res1 == 3:
                        done = True
                else:
                    res1 = 0
            except IndexError:
                pass
            
            try:
                s = r
                q = c
                while a[r][c] == a[s+1][q+1]:  #to diag down
                    res2 +=1
                    s = s +1
                    q += 1
                    print ("diag down - ",res2)
                    if res2 == 3:
                        done = True
                    
                else:
                    res2 = 0
            except IndexError:
                pass
            
            try:
                s = r
                q = c
                while (a[r][c] == a[s][q+1]):  #to right
                    res3 +=1
                    q += 1
                    print ("right - ",res3)
                    if res3 == 3:
                        done = True
                    
                else:
                    res3 = 0
            except IndexError:
                res3 = 0                
                pass
            
            try:
                s = r
                q = c
                while a[r][c] == a[s-1][q+1]:  #to diag up
                    res4 +=1
                    q += 1
                    s -= 1
                    print(s, "ssssssss")
                    if s < 0:
                        res4 = 0
                    print ("diag up ----------",res4)
                    if res4 == 3:
                        done = True
                        res4 = 0
                        print("ddddddd",res4)
                    
                else:
                    res4 = 0
            except IndexError:
                res4 = 0
    if done is True:
        return True
    else:
        return False

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
