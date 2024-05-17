"""def sum_n_terms(a,b,c,d,e):
      y = a+b+c+d+e
      print(y)
     #retun sirf value return karta ahi print nhi karta hai
      #good for those whixh use two argument fucntions

sum_n_terms(10,6,10,10,10)"""

def s(numbers):
    y = 0
    for x in numbers :
        y = y+x
    print(y)
s(10,-6,30,10,20)
#for printing the sum we need to give the value in the form of 
#list or the tuple otherwise it will give you the argument error in 
#which the output will show that sum takes one arguments