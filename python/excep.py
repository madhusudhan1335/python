import logging as l
l.basicConfig(filename='log1.txt',level=l.ERROR)

def pro():
    try:
        s = [10,20,30,40,50,60,0]
        in1 = int(input('enter index:'))
        num = int(input('enter num:'))
        den = int(input('enter den:'))
        print(s[in1])
        c = num/den
        print(c)
    except ZeroDivisionError as e:
        print(e)
        l.error(e)
    except IndexError as e:
        print(e)
        l.error(e)
    except ValueError as e:
        print(e)
        l.error(e)
    except Exception as e:
        print(e)
        l.error(e)

pro()
