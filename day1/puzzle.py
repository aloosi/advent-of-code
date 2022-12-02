#part 1
print(max([sum([int(x) for x in i.split("\n")])for i in open("input.txt", "r").read()[:-1].split("\n\n")]))
#part 2
print(sum(sorted([sum([int(x) for x in i.split("\n")])for i in open("input.txt", "r").read()[:-1].split("\n\n")],reverse=True,)[0:3]))