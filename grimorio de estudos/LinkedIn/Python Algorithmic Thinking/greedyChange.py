
def make_change(target_amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coinType = []
    coinCount = 0
    coinSum = target_amount
    coinSelected = 0
    while coinSum != 0:
        for x in range(len(coins)):
            if coins[x] <= coinSum: # por algum motivo quebra aqui
                if coins[x] > coinSelected:
                    coinSelected = coins[x]
        coinType.append(coins[x])
        coinSum = coinSum - coins[x]
        coinCount += 1
    
    print(f"{coinCount} coins used: {coinType}")
            
print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p