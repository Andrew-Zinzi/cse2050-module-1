from product import Product

def recursive_total_price(products) -> float:
    if len(products) == 0:
        return 0.0
    
    return products[0].get_price() + recursive_total_price(products[1:])

def bubble_sort(products): 
    p = len(products)
    
    for i in range(p-1):
        swapped = False
    
        for j in range(p - 1 - i):
            if products[j].get_id() > products[j + 1].get_id():
                products[j], products[j + 1] = products[j+1] , products[j]
                swapped = True
        if not swapped:
                break
def selection_sort(products):
    p = len(products)

    for i in range(p-1):
        max_index = 0
        for j in range(p - i):
            if products[j].get_id() > products[max_index].get_id():
                max_index = j
        if (p - i - 1) != max_index:
            products[p-i-1], products[max_index] = products[max_index], products[p-i-1]
def insertion_sort(products):
    for i in range(1,len(products)):
            j = i
            while j > 0 and products[j].get_id() < products[j-1].get_id():
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

def binary_search(products, product_id, low=0, high=None):
    if high is None: high = len(products) - 1
    if low > high: return - 1
    mid = (low + high) // 2
    mid_id = products[mid].get_id()
    if product_id == mid_id:
        return mid
    elif product_id < mid_id:
        return binary_search(products, product_id, low, mid - 1)
    else:
        return binary_search(products, product_id, mid + 1, high)



