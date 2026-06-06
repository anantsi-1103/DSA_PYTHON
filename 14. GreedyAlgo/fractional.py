def fractional_KnapSnack(capacity , profits, weights):
    items = []


    for i in range(len(profits)):
        ratio = profits[i]/weights[i]
        items.append((ratio , profits[i], weights[i]))

    # sort in descending order
    items.sort(reverse=True)

    total_profit = 0  # 24 

    for ratio, profit, weight in items:
        if capacity>= weight:
            total_profit += profit
            capacity -= weight # 5
        
        else:
            fraction = capacity/weight
            total_profit += profit * fraction
            break

    return total_profit


profits = [25,24,15]
weights = [18,15,10]
capacity = 20

print(fractional_KnapSnack(capacity, profits, weights))