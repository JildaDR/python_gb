revenue = int(input('Please indicate the revenue of the company: '))
costs = int(input('Please indicate the costs of the company: '))
profit = revenue - costs
rent = profit / revenue

if revenue > costs:
    result = 'profitable'
elif revenue == costs:
    result = 'zero profitable'
else:
    result = 'loss-making'

print(f'The company operates with a {result} financial result')

if result == 'profitable':
    print(f'Rentability is {rent:.2f}%')
    emp = int(input('Please indicate the number of employees of the company: '))
    profit_per_emp = profit / emp
    print(f'Profit per employee is {profit_per_emp:.2f}')

