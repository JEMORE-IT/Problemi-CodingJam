R = 1000000000
k = 100
P = [2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2]

len_P = len(P)
seen = [False] * len_P

total_bacon = 0
idx = 0
rides = 0
ride_costs = [0] * len_P

def ride(idx):
    cost = 0
    start_idx = idx
    while (cost + P[idx] <= k):
        cost+= P[idx]
        idx = (idx + 1) % len_P
        if idx == start_idx:
            break
    return cost, idx

while (not seen[idx]) and (rides < R):
    seen[idx] = True
    cost, idx = ride(idx)
    total_bacon += cost
    ride_costs[rides] = cost
    rides += 1

if rides < R:
    seen = [False] * len_P
    rep_rides = 0
    add_cost = 0
    while not seen[idx]:
        seen[idx] = True
        cost, idx = ride(idx)
        add_cost += cost
        rep_rides += 1

    repss = ((R - rides) // rep_rides)
    total_bacon += add_cost * repss
    rides += rep_rides * repss
    while rides < R:
        cost, idx = ride(idx)
        total_bacon += cost
        rides += 1

print(total_bacon)
