class NotFound(Exception):
     #print('not found it') #you can give message here
     pass
def menu(name):
    if name == 'pizza':
        return 200
    else:
        raise NotFound #you cang msg here too,NotFound('not found food')
try:
    print(menu('pizza'))
    
except NotFound as e:
  # print('not found') #you can give msg here too 
   print(e)
      