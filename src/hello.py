squares = [value**2 for value in range(1,11)]
print(squares[:4])
print(squares[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for players in players[:3]:
    print(players.title())