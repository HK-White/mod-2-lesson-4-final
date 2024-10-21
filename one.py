import random
moods = ["happy", "sad", "pumped", "drained"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

for i in range(1):
    mood = random.choice(moods)
    for j in range(1, 7):
        day = random.sample(days, 1)[0]
        print(f"On {day}, you were {mood}")
        break