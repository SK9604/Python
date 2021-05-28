bicycles = ['cannondale', 'trek', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[-1])
bicycles[1] = 'hello'
print(bicycles[1])
bicycles.append('bye')
print(bicycles[-1])
print(bicycles)
pop_bicycles = bicycles.pop()

print(pop_bicycles)
print(bicycles)

dele = 'cannondale'
bicycles.remove(dele)
bicycles.append('do')
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)