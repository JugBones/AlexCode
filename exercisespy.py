let = int(input("Enter a integer digit : "))

if let%11==0:
    print ("a",end=" ")
if let%9==0:
    print ("b",end=" ")
if let%7==0:
    print ("c",end=" ")
if let%2==0:
    print ("d",end=" ")
if let%11>0 and let%9>0 and let%7>0 and let%2>0 :
    print ("e")

