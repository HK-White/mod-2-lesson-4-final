import random
#Similsr to task/section one with time of day added per instuction
moods = ["happy", "sad", "pumped", "drained"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
times = ["morning", "afternoon", "evening"]
for i in range(1):
    mood = random.choice(moods)
    for i in range(1):
        time = random.choice(times)
        for j in range(1, 7):
            day = random.sample(days, 1)[0]
            print(f"On {day} {time}, you reported that you were feeling {mood}")
            break
#Section 2, Task 1 by H. White