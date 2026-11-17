a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8 ,9]


result = [(a, b, c) for a in [1,2,3] for b in [4,5,6] for c in [7, 8, 9]]
print(result)