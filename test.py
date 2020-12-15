import random
score = 300

def add_zombie(score):
    perc = random.randint(1, 100)
    perc_spread = [0]
    for i in range(4):
        if score <= 400:
            if i == 0:
                perc_spread.append(-.1 * score + 40)
            elif i == 1:
                perc_spread.append((-.15 * score + 60) + perc_spread[1])
            elif i == 2:
                perc_spread.append((.1 * score) + perc_spread[2])
            elif i == 3:
                perc_spread.append((.15 * score) + perc_spread[3])
    print(perc_spread)
    for i in range(1, 5):
        if perc_spread[i] >= perc and perc_spread[i - 1] < perc:
            print(f'type {i} zombie')
            break

for _ in range(20):
    add_zombie(score)