def number(a, base):
    try: 
        return int(a, base)
    except ValueError:
        return (-1)


print(number ("40", 2))
print(number ("100", 2))
