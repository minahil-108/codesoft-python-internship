import random

print("WELCOMW TO PY-PASSWORD GENERATOR\n")
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[0, 1, 2 ,3, 4, 5 ,6 ,7 ,8 ,9]
characters=['@','#','$','%','&','*']

nletter=int(input("how many letters you want to be in your password ? \n"))
n_num=int(input("how many numbers you want to be in your password ? \n"))
n_char=int(input("how many characters you want to be in your password ? \n"))

password=""
# easy level
for let in range(0,nletter):
  x=random.choice(letter)
  # print(x)
  password+=x
  
for num in range(0,n_num):
  y=random.choice(numbers)
  # print(y)
  y=str(y)
  password+=y

for char in range(0,n_char):
  z=random.choice(characters)
  # print(z)
  password+=z


# hard level

# print(f"here is your password : {password}")
# print(password)
sum=""
a=len(password)
for pas in range(0,a):
  new=random.choice(password)
  sum+=new

print(f"here is your random password : {sum}")