#def printhalfdiamond(num):
 #   for i in range(num):
  #      print(" * "*(2*i+1))
   # for i in range(num-1,0,-1):
    #    print(" * "*( 2 *i-1))


def printfulldiamond(num):
    for i in range(num):
        print(" "*(num-i-1) + "*"*(2*i + 1))
    for i in range(num-2,-1,-1):
        print(" "*(num-i-1) + "*"*(2*i + 1))

x =int(input("enter ur nb: "))
#printhalfdiamond(x)
printfulldiamond(x)
