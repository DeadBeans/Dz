word = 'Процент'
world = 'а'
worlds = 'ов'
for x in range(1, 101):
    ost = x % 10
    if ost == 1 and not(11 <= x <= 14):
        print(x, word)
    elif 2 <= ost <= 4 and not(11 <= x <= 14):
        print(x, word + world)
    else:
        print(x,word + worlds)
