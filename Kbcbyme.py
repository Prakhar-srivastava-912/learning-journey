import random as r
print("\t\tKaun Banega Crorepati!!!!!")
print("Hello and welcome to KBC by Prakhar")
print("\nMe Prakhar Srivastava welcomes you")
print("""\nSo the rules are we go from 1000 to 1 crore rupee each question have
four options. If you don't know the answer then type Quit""")
print("\nSo Let's begin....")
money=0
lis=[["What is the capital of U.P.?","A)Kanpur","B)Lucknow","C)Noida","D)Ayodhya","B"],
     ["What is the capital of M.P.?","A)Gwalior","B)Ujjain","C)Bhopal","D)Jabalpur","C"],
     ["Who is the first president of India?","A)Rajendra prasad","B)Zakir Hussain","C)Sarojni Naidu","D)Pratibha Patil","A"],
     ["What is the square of 0.5?","A)0.025","B)0.25","C)0.205","D)2.5","B"],
     ["In which fight Napolean lost his first major battle?","A)Battle of Leipzig","B)Battle of Aspern-Essling","C)The Russian Campaign","D)Siege of Acre","A"],
     ["If A is double the age of B and C is half the age of E and D is bigger than B D is half the age of E then who is eldest?","A)B","B)A","C)E","D)D","C"],     
     ["Which is the longest river in world?","A)Nile","\t B)Amazon","C)Yangtze","D)Pacific","A"],
     ["Which is the longest movie of bollywood?","A)Lagaan","\t B)Sangam","C)Mera Naam joker","D)Dhurandhar:2","C"],
     ["How many indians are died during Covid-19?","A)533849","B)53389","C)5338449","D)533948","A"],
     ["Aurum is also known as?","A)Copper","B)Silver","C)Platinum","D)Gold","D"],
     ["What is the name of the divine bow wielded by Karna in the Hindu epic Mahabharata?","A)Gandiva","B)Pinaka","C)Indrachapa","D)Vijay","D"],
     ["Who discovered electrons?","A)Thomson","B)Rutherford","C)Dalton","D)Bohr","A"],
     ["Which cricketer scored highest number of ODI centuries?","A)Sachin","B)Virat","C)Gayle","D)Smith","B"],
     ["Which is the smallest bone of human body?","A)Sole","\t B)Sacrum","C)Stirup","D)Sphenoid","C"],
     ["How many countries are in this world?","A)195","B)196","C)193","D)198","A"]
     ]
price=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
r.shuffle(lis)
for i in range(0,len(lis)):
    a=lis[i]
    print("\t\tQuestion for Rs.",price[i])
    print("Question no.",i+1,"->",a[0])
    print(a[1],"\t\t\t\t",a[2])
    print(a[3],"\t\t\t\t",a[4])
    b=input("Choose ur option:- ")
    if(b.upper()=="QUIT"):
        print (f"OK but the correct answer of this question is {a[5]}")
        print("Ok thanks for playing")
        money=price[i-1]
        break
    if(b.upper()==a[5]):
        print("Correct answer")
        if(i==4):
            money=10000
        elif(i==9):
            money=3200000
        elif(i==14):
            money=10000000
    else:
        print("Sorry this is the wrong answer...")
        print("Good Luck next time...")
        break
if(money==10000000):
    print("1 croreeeeee")
print("You win",money)

