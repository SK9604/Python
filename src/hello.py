bicycles = ['trek', 'cannondale', 'redline', 'specialized']
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

dele = 'trek'
bicycles.remove(dele)
print(bicycles)