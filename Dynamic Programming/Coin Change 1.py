# Coin Change (minimum number of coins)

h={}
def coin_change(coins,amount,i):
    if i==len(coins):
        return float('inf')
    if amount==0:
        return 0
    else:
        if amount in h.keys():
            return h[amount]
        if coins[i]<=amount:
            h[amount]=min(1+coin_change(coins,amount-coins[i],i),coin_change(coins,amount,i+1))
            return h[amount]
        else:
            h[amount]=coin_change(coins,amount,i+1)
            return h[amount]
coins,amount=[1,2,3],14
print(coin_change(coins,amount,0))