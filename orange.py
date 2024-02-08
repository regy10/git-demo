name=input("what is your name? :")
match name:
    case "John":
       print("Banana")
    case "Ashura": 
        print("Ubungo")
    case _:
        print("Invalid input")
       
score=int(input("what is your score? :"))
   
if score >=90 and score <=100:
      print("grade: A")
elif score >=80 and score <=89:
      print("grade: B")
elif score >=70 and score <=79:
      print("grade: C")
elif score >=60 and score <=69:
      print("grade: D")
else:
      print("you failed")

