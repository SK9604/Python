squares = [value**2 for value in range(1,11)]
print(squares[:4])
print(squares[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for players in players[:3]:
    print(players.title())
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are : ")
print(my_foods)
print("\nMy friend's favorite foods are : ")
print(friend_foods)