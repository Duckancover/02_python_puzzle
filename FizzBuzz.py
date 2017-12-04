def check(num):
    if num % 5 == 0:
        if num % 3 ==0:
           return print ("fizBuzz")         
        return print ("fizz")        
    elif num % 3 == 0:
        return print ("buzz") 
    else:
        return print (num)

if __name__ == "__main__":
    check(87)
    check(10)
    check(7)
    check(18)