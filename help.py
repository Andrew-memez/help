players = ['tft','n','e']
batles = []
for i in players:
    for j in players:
        batles.append([i,j])
batles.sort()
print(batles)
for i in batles:
    for j in batles:
        if i == j:
            batles.remove(i)
print(batles)