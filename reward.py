#  File: reward.py
#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name: Sneha Kamal
#  Student UT EID: sk52223
#  Course Name: CS 313E
#  Unique Number:
import sys
max_val = 1000
def getmin(prices, T):
    # Add your code here!
    gift_worth = int(0.1 * T)
    n = len(prices)
    max = 2**64 - 1
    results_table = [[0 for i in range(gift_worth + 1)]for i in range(n + 1)]
    for i in range(1, gift_worth + 1):
        results_table[0][i] = max
    for i in range(1, n + 1):
        for j in range(1, gift_worth + 1):
            if prices[i - 1] > j:
                results_table[i][j] = results_table[i - 1][j]
            else:
                results_table[i][j] = min(results_table[i - 1][j], results_table[i][j - prices[i - 1]] + 1)
    if results_table[n][gift_worth] == max:
        return -1
    else:
        return results_table[n][gift_worth]

if __name__ == "__main__":
    # Read input list of prices for each gift
    prices_str = sys.stdin.readline().split()
    prices = [ int(x) for x in prices_str ]
    # Read total price that the customer spends
    T = int(sys.stdin.readline())
    print(getmin(prices, T))