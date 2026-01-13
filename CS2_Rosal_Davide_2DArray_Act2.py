steps = [
    [4500, 5200, 4800, 5500, 5300],  
    [4000, 4100, 3900, 4200, 4600],  
    [6000, 5800, 5900, 6100, 6200]   
]

friends = ["Friend 1", "Friend 2", "Friend 3"]

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    minimum = min(steps[i])
    maximum = max(steps[i])

    print(friends[i], " - ", "Total steps:",total, "|", "Average: ",average, "|", "Min: ",minimum, "|", "Max: ",maximum)