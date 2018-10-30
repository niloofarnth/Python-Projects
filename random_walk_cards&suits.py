
import random
import statistics
import pandas as pd

def random_walk(N,M):
    points = 0
    suits = list(range(1,M+1))
    suit_prev = random.choice(suits)

    n_each = N/M
    d = {}
    for s in suits:
        d["M{0}".format(s)]= 0 
    for i in range(N-1):
        #print('number{} ={}'.format(i+1,suit_prev))
        #print('points = {}'.format(points))
        d["M{0}".format(suit_prev)] += 1
        #print(d)
        for s in suits:
            if d["M{0}".format(s)] >= n_each:
                suits.remove(s)
        #print(suits)
        suit_next = random.choice(suits)
        if suit_next == suit_prev:
            points += 1
        suit_prev = suit_next
    #print('number{} ={}'.format(i+2,suit_prev))
    #print('points = {}'.format(points))
    d["M{0}".format(suit_prev)] += 1
    #print(d)
    return (points)
    
M = 4 #suits
N = 52 #number of cards
repeat_n = 1000000
all_points = []
for i in range(repeat_n):
    all_points.append(random_walk(N,M))
print(statistics.mean(all_points))
print(statistics.stdev(all_points))
all_p_series = pd.Series(all_points)
P_all = all_p_series[all_p_series> 6]
P = (P_all[P_all > 12]).count()/ P_all.count()
print(all_p_series.head(100))
print(P)

    
