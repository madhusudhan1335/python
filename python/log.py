import logging as log

log.basicConfig(filename='log.txt',level = log.ERROR)

def calcu():
    try:
        lst = [10,20,30,40,50,60,0]
        num = int(input('enter num:'))
        den = int(input('enter den:'))
        res = lst(num)/lst(den)
        print(res)
        
    except ZeroDivisionError as e:
        log.error(e)
        print(e)
    except IndexError as e:
        log.error(e)
        print(e)
    except Exception as e:
        log.error(e)
        print(e)
        
calcu()
print('termination')

        
    