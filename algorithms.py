
def recursive_total_price(products):
    if len(products) == 0:
        return 0.0

    P = products.pop()
    return P.price + recursive_total_price(products)

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

def fewest_coins(coins,amount):
    if amount in coins:
        return 1
    min_coins = float('inf')
    for coin in coins:
        if coin < amount:
            branch = 1 + fewest_coins(coins, amount - coin)
            if branch < min_coins:
                min_coins = branch
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



