scores = [1,2,3,5]
ages = [8,9,10,1]


players = sorted(zip(ages, scores))
print(players)

memo = {}

def dp(index, last_score):
    if index == len(players):
        return 0
    if (index, last_score) in memo:
        return memo[(index, last_score)]

    current_age, current_score = players[index]

    # Option 1: Skip the current player
    max_score = dp(index + 1, last_score)

    # Option 2: Include the current player (only if no conflict)
    if current_score >= last_score:
        max_score = max(max_score, current_score + dp(index + 1, current_score))

    memo[(index, last_score)] = max_score
    return max_score
res=dp(0,0)
print(res)