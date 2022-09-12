def getdate():
    import datetime
    return datetime.datetime.now()


print("-----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------------")

choice1 = int(input("choose between person1 , person2 , person3 as 1/2/3  - "))
choice2 = input("choose between diet and excercise -  ")
choice2.lower()
choice3 = input("enter or retrieve - ")
choice3.lower()

if choice3 == "enter":
    if choice1 == 1:

        if choice2 == "diet":
            f = open("person1_diet.txt", "a")
            var1 = input("what did you eat  ")
            f.write(str([str(getdate())])+var1)
            f.write("\n")
            f.close()
        if choice2 == "exercise":
            g = open("person1_exer.txt", "a")
            var2 = input("which exercise did you do  ")
            g.write(str([str(getdate())])+var2)
            g.write("\n")
            g.close()
    if choice1 == 2:
        if choice2 == "diet":
            h = open("person2_diet.txt", "a")
            var3 = input("what did you eat  ")
            h.write(str([str(getdate())])+var3)
            h.write("\n")
            h.close()
        if choice2 == "exercise":
            i = open("person2_exer.txt", "a")
            var4 = input("which exercise did you do  ")
            i.write(str([str(getdate())])+var4)
            i.write("\n")
            i.close()
    if choice1 == 3:
         if choice2 == "diet":
            j = open("person3_diet.txt", "a")
            var5 = input("what did you eat  ")
            j.write(str([str(getdate())])+var5)
            j.write("\n")
            j.close()
         if choice2 == "exercise":
            k = open("person3_exer.txt", "a")
            var6 = input("which exercise did you do  ")
            k.write(str([str(getdate())])+var6)
            k.write("\n")
            k.close()
if choice3 == "retrieve":

    if choice1 == 1:

        if choice2 == "diet":
            f = open("person1_diet.txt", "r+")
            print(f.read())
            f.close()
        if choice2 == "exercise":
            g = open("person1_exer.txt", "r+")
            print(g.read())
            g.close()
    if choice1 == 2:

        if choice2 == "diet":
            h = open("person2_diet.txt", "r+")
            print(h.read())
            h.close()
        if choice2 == "exercise":
            i = open("person2_exer.txt", "r+")
            print(i.read())
            i.close()

    if choice1 == 3:

         if choice2 == "diet":
            j = open("person3_diet.txt", "r+")
            print(j.read())
            j.close()
         if choice2=="exercise":
            k=open("person3_exer.txt","r+")
            print(k.read())
            k.close()
