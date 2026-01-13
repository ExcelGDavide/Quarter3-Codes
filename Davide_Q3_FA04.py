steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

names = ["Me", "Lia", "Jake"]

totals = []

for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)

highest_total = max(totals)
lowest_total = min(totals)

highest_index = totals.index(highest_total)

print("Person with the highest total steps:", names[highest_index])
print("Highest total steps:", highest_total)
print("Lowest total steps:", lowest_total)
print("Difference between highest and lowest:", highest_total - lowest_total)