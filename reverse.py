"""ef reversed_strings(oh):
    xoh = ''
    c = len(oh)
    while(c>0):
        xoh = xoh + oh[c-1]
        c =c -1
    return (xoh)
print(reversed_strings('harshit123'))
#pehle define karo phir function ko finally call karo ;
#phir length nikalo





def x(oh):
    y = oh[::-1]
    print(y)
x('harshit')

#we can can do it by string slicing method also"""






def l(oh):
    
 y = len(oh)-1
 for i in range(y,-1,-1):

  print(oh[i],end = '')

l("harshitt")
#one more method to solve this with the help pof string slicing




