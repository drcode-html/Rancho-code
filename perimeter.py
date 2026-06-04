while True:
 shape = input("what shape (or type quit to stop)").lower()
 
 if shape == "quit":
   break
 elif shape  == "square" or shape == "rectangle":
   l = int(input("length:"))
   b = int(input("breath:"))
   print("perimeter",2*(l+b))
   print("area",l*b)
 elif shape == "circle": 
   r = int(input("radius:"))
   print("perimeter",2*3.14*r)
 else:
   print("sorry shape is unknown")




