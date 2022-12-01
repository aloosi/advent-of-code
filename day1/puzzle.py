print(max([sum([int(x) for x in i.split("\n")])for i in open("calories.txt", "r").read()[:-1].split("\n\n")]))
print(sum(sorted([sum([int(x) for x in i.split("\n")])for i in open("calories.txt", "r").read()[:-1].split("\n\n")],reverse=True,)[0:3]))
