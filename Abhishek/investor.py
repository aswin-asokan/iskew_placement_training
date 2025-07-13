n = int(input())
investors = list()
for i in range(n):
    investors.append(int(input()))
curr_investment = investors[0]+investors[1]
max_investment = 0
for i in range(1,n-1):
    temp_sum = curr_investment + investors[i+1]
    if max_investment < curr_investment:
        max_investment = curr_investment
    if curr_investment > 0 or temp_sum > 0:
        curr_investment = curr_investment + investors[i+1]
    else:
        curr_investment = investors[i] + investors[i+1]
print(max_investment)