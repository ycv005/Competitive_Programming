def knapsackTopDown(items, weight, ind, cache):
    mx = 0
    if ind in cache and weight in cache[ind]:
        # print("using dp")
        return cache[ind][weight]
    else:
        # print("simple recursion")
        for i in range(ind, len(items)):
            local_mx = 0
            if items[i][0]  <= weight:
                # include it
                tmp = items[i][1] + knapsack(items, weight-items[i][0], ind + 1, cache)
                # don't include it
                tmp1 = knapsack(items, weight, ind + 1, cache)
                local_mx = max(tmp, tmp1)
            mx = max(mx, local_mx)
        if ind in cache:
            cache[ind][weight] = mx
        else:
            cache[ind] = {weight: mx}
        return mx

def knapsackBottomUp(items, weight):
    cache = [[]*(weight+1)]*(len(items)+1)

    for i in range(1, len(items)):
        for j in range(weight+1):
            # current item weight is more then avail weight
            if items[i-1][0] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i-1][j - items[i-1][0]] + items[i-1][1])
    return cache[len(items)][weight]

def knapsackBottomUp1DArray(items, weight):
    cache = [0]*(weight+1)

    for i in range(len(items)):
        newCache = [0]*(weight+1)
        for j in range(weight+1):
            if items[i][0]>j:
                newCache[j] = cache[j]
            else:
                newCache[j] = max(cache[j], cache[j-items[i][0]] + items[i][1])
        cache = newCache
    return cache[w]

def knapsack(items, weight):
    cache = [0]*len(items)


















# [weight, value]
items = [[2,6], [2, 10], [3, 12]]
weight = 5
cache = {}
print(knapsackTopDown(items, weight, 0, cache))
print(knapsack(items, weight))
