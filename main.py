data = input('\nEnter your key here: ')
userinput = int(input('If you want to put your private keys into the database, press 1 '))
if userinput == 1:
 with open('dataset.txt', "a") as file:
   file.write(data)
else:
    print('Thank you for your attention!')






