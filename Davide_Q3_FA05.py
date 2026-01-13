steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

for day in range(len(steps[0])):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily_totals.append(total)
    print(days[day], "total steps:", total)

highest_total = max(daily_totals)
most_active_index = daily_totals.index(highest_total)

print("Most active days overall:", days[most_active_index], "(", highest_total, ")")
   