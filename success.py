
display='''
1.Addition of two numbers
2.Subraction of two numbers
3.Multiplication of two numbers
4.Division of two numbers
5.Power Of Number
6.Exit the program'''
while True:
      a=int (input("enter value of a : "))
      b=int (input("enter value of b : "))

      print(display)
      ch = int(input ("enter your choice : "))
      if ch==1 :
            print(f"addition of two numbers = {a+b}")
      elif ch==2 :
            print(f"subraction of two numbers = {a-b}")
      elif ch==3 :
            print(f"multiplication of two numbers = {a*b}")
      elif ch==4 :
            try:
                  print(f"division of two numbers = {a/b}")
            except:
                  print("Zero Division Error")
      elif ch==5:
            print(f"{a} Power {b} = {a**b}")
      elif ch==6 :
            exit()
      else:
            print("Something Wrong!")

