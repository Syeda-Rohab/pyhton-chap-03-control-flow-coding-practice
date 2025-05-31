# chap 03
# topic : control flow statements in python
# definition of control flow statements in python : 
                                                     # python m control flow statement hamen program ke execution ka flow control karne dete hain , yani decide krte h ke konsa code kab chalega 
# three important control flow statement :
# if statement ( jab hamen kisi condition ke basic par code chalana ho to if statement use krte h )
# if-else statement ( do raste condition true ya false , agar condition true h to aik code chalega warna doosra chalega)
# if else elif ( multiple conditions check krna )
# comparison operators ( conditions banane ke liye ) :
# ( == : equal to ) ( != : not equal to ) ( < : less than ) ( > : greater than ) ( <= : less than or equal to ) ( >= : greater than or equal to )
# logical operators ( multiple conditions ko jorne ke liye ) : 
#  ( and : dono conditions true honi chahiye ) ( or : kam se kam aik condition true honi chahiye ) ( not : condition ka opposite krta h )
# nested if statement ( if ke andar if )


# if statement code implementation : 

age = 18
if age >= 18 :
    print("ap vote deskte hain")

# if else statement code implementation

age = 16
if age >= 18 :
    print("ap vote deskte h")
else :
    ("ap vote nahi deskte")

#if elif else code implementation

marks = 75
if marks >= 90 :
    print ("Grade A")
elif marks >= 75 :
    print ("Grade B")
elif marks >= 75 :
    print ("Grade C")
else :
    print ("Fail")

# comparison operators code implementation

a = 5
print(a == 5) # true 
print(a != 5) # false

b = 10
c = 15
print(b < c) # true 

c = 18
d = 20
print(b > c) # false


# logical operators code implementation

age = 1
has_id = False

if age >= 18 or has_id :
    print("Entry allowed")
else :
    print("Entry denied") # output (entry denied)

    
    age = 20
has_id = False

if age >= 18 or has_id :
    print("Entry allowed")
else :
   print("Entry denied") # output (entry denied)

    # nested if statement code implementation

num = 10
if num > 0 :
    if num % 2 == 0 :
        print("positive even number")
    else :
        print("positive odd number")  # output is positive even number