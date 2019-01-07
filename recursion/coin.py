'''
@Description: 动态规划解决硬币找零问题
@Version: 
@Author: biofool2@gmail.com
@Date: 2019-01-07 16:12:13
@LastEditTime: 2019-01-07 17:08:55
@LastEditors: Please set LastEditors
'''


# 递归方法
# num_coins = min(
# 1 + num_coins(original_count - 1)
# 1 + num_coins(original_counr - 5)
# 1 + num_coins(original_counr - 10)
# 1 + num_coins(original_counr - 25)
# )


# 递归调用次数过多，程序运行缓慢
# 添加known_results记录包含此找零的最小硬币数量，可降低递归调用次数
def change_coin_rec(coin_val, change, known_results):
    min_coins = change
    if change in coin_val:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_val if c<=min_coins]:
            num_coins = 1 + change_coin_rec(coin_val, change-i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


# 动态规划方法
def change_coin_dp(coin_val, change, return_all=False):
    # 记录包含从0到找零值change的所有值的解
    min_coins = [0] * (change + 1)
    coins_used = [0] * (change + 1) # 记录使用过的硬币
    for cent in range(change+1):
        coin_cnt = cent
        new_coin = 1
        for j in [c for c in coin_val if c <= cent]:
            if min_coins[cent - j] + 1 < coin_cnt:
                coin_cnt = min_coins[cent - j] + 1
                new_coin = j
        min_coins[cent] = coin_cnt
        coins_used[cent] = new_coin
    if return_all:
        return min_coins, coins_used
    else:
        return min_coins[change]

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        cur_coin = coins_used[coin]
        print(cur_coin)
        coin -= cur_coin

if __name__ == "__main__":
    coin_val = [1, 5, 10, 21, 25]
    change = 63
    # known_res = [0] * (change+1)
    # print(change_coin_rec(coin_val, change, known_res))
    min_coins, coins_used = change_coin_dp(coin_val, change, return_all=True)
    print("The min coins list is : ", min_coins)
    print("The used coins list as follows : ", coins_used)
    print_coins(coins_used, change)