print('N  marriage')
num_of_guests = int(input('Enter, how many people will be at the wedding :'))
if num_of_guests > 50:
    print('restaurant')
elif (num_of_guests >= 20) and (num_of_guests <= 50):
    print('cafe')
else:
    print('home')
