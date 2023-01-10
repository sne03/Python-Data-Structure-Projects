def max_earnings(earnings):
    earnings_list = list(earnings)
    max_value = 0
    for j in range(0, len(earnings_list), 1):
        for k in range(j, len(earnings_list), 1):
            max_value2 = 0
            for l in range(j, k + 1, 1):
                max_value2 += earnings_list[l]
            if max_value < max_value2:
                max_value = max_value2
    return max_value