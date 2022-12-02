# convert the input letters to respective (0, 1, 2) by subtracting unicode number
print(sum(map(lambda score: ((score[1] - score[0] + 1) % 3 * 3 + score[1] + 1), ((ord(l[0]) - 65, ord(l[2]) - 88) for l in open('input.txt').read().split('\n')))))
print(sum(map(lambda score: (sum(score) + 2) % 3 + 1 + score[1] * 3, ((ord(l[0]) - 65, ord(l[2]) - 88) for l in open('input.txt').read().split('\n')))))


