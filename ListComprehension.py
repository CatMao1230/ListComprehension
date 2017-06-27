ls = [x**2 for x in range(1, 11) if x % 2 == 1]
ls.extend(-x**2 for x in range(1,11) if x % 2 == 0)
print sum(ls)