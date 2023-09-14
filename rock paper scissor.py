import random

print("\t\t\tWELCOME TO ROCK/PAPER/SCISSORS GAME \n\n")
choice=int(input("what you choose ? \ntype 0 for rock\ntype 1 for paper\ntype 2 for sciccors\n"))




if choice==0:
  print("\n\nyou choose rock\n")
elif choice==1:
  print("\n\nyou choose paper\n")
elif choice==2:
  print("\n\nyou choose scissor\n")
else:
  print("\n\ninvalid choice\n")
  
com_choice=random.randint(0,2)
print(com_choice)

if com_choice==0:
  print("\n\ncomputer choose rock\n")
elif com_choice==1:
 print("\n\ncomputer choose paper\n")
elif com_choice==2:
 print("\n\ncomputer choose scissor\n")
else:
  print("\n\ninvalid choice\n")
  
if choice>=3 and choice <0:
  print("\ninvalid choice you loose")
elif com_choice==2 and choice==0:
  print("\nyou win")
elif com_choice==0 and choice==2:
  print("\nyou loose")
elif com_choice>choice:
  print("\nyou loose")

elif com_choice==choice:
  print("\nits draw")
else:print("\nyou loose")