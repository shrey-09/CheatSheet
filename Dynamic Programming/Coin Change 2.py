# Coin Change (total number of ways)

h={}
def coin_change(coins,amount,i):
    if amount==0 and i<len(coins):
        return 1
    if i>=len(coins):
        return 0
    else:
        if (amount,i) in h.keys():
            return h[(amount,i)]
        if coins[i]<=amount:
            h[(amount,i)]=coin_change(coins,amount,i+1)+coin_change(coins,amount-coins[i],i)
            return h[(amount,i)]
        else:
            h[(amount,i)]=coin_change(coins,amount,i+1)
            return h[(amount,i)]
coins,amount=[1,2,3,5,6],14
print(coin_change(coins,amount,0))