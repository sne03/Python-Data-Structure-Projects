import sys
# Add Your functions here
# You are allowed to change the main function. 
# Do not change the template file name.
def combinations(lst,comb=None,i=0,l2 = []):
    if comb == None:
        comb = [0] * len(lst)

    if i >= len(lst):
        sub = [str(lst[i]) for i in range(len(lst)) if comb[i] == 1]
        for i in range(len(sub)):
            sub[i] = int(sub[i])
        l2.append(sub)

    else:
        comb[i] = 0
        combinations(lst,comb,i+1)
        comb[i] = 1
        combinations(lst,comb,i+1)
    return l2

def max_profit(prices,increase=0,money=0):
    combos = combinations(prices)
    max = 0
    for elem in combos[1:]:
        if sum(elem) <= money:
            value = 0
            for nums in elem:
                w = prices.index(nums)
                product = increase[w] * nums
                value += product
            if value > max:
                max = value
    return max/100

def main():
    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)
# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)
    
    # The third line is a list of house prices in million dollar which is a list of\textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   
    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])
# Add your implementation here .... 
    result =  max_profit(prices,increase,money)
# Add your functions and call them to generate the result. 
    print(result)
    
    
main()