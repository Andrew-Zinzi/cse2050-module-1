def recursive_total_price(products) -> float:
    if len(products) == 0:
        return 0.0
    
    return products[0].get_price() + recursive_total_price(products[1:])

def bubble_sort(products): 
    p = len(products)
    
    for i in range(p-1):
        swapped = False
    
        for j in range(p - 1 - i):
            if products[j] > products[j + 1]:
                products[j], products[j + 1] = products[j+1] , products[j]
                swapped = True
        if not swapped:
                break
def selection_sort(products):
    p = len(products)

    for i in range(p-1):
        max_index = 0
        for j in range(p - i):
            if products[j] > products[max_index]:
                max_index = j
        if (p - i - 1) != max_index:
            products[p-i-1], products[max_index] = products[max_index], products[p-i-1]
def insertion_sort(products):
    for i in range(1,len(products)):
            j = i
            while j > 0 and products[j] < products[j-1]:
                products[j], products[j-1] = products[j-1], products[j]
                j -= 1
    
def fewest_coins(coins: list[int], amount: int, memo: dict = None) -> int:
    """Return the minimum number of coins needed to make amount using top-down memoization."""
    if memo is None:
        memo = {}
    
    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")
    
    if amount in memo:
        return memo[amount]
    
    min_coins = float("inf")
    
    for coin in coins:
        result = fewest_coins(coins, amount - coin, memo)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)
            
    memo[amount] = min_coins
    return min_coins

def binary_search(products, product_id):
    if len(products) == 0: return False
    med = len(products) // 2
    if product_id == products[med]:
        return True
    elif product_id < products[med]:
        return binary_search(products[:med], product_id)
    else:
        return binary_search(products[med + 1:], product_id)



