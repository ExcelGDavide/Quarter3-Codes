steps = [
    [4500, 5200, 4800, 5000, 5300],   
    [4000, 4100, 3900, 4200, 4600],   
    [6000, 5800, 5900, 6100, 6200]    
]

print("Daily Steps Data:\n")

for i in range(len(steps)):
    print("Person", i + 1, "steps:", steps[i])
    
    total = sum(steps[i])
    average = total / len(steps[i])
    
    print("Total steps:", total)
    print("Average steps:", average)
    print()

max_steps = steps[0][0]

for row in steps:
    for value in row:
        if value > max_steps:
            max_steps = value

print("Highest step count in the dataset:", max_steps)