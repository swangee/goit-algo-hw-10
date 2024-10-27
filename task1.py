import pulp
from pulp import value

# Ініціалізація моделі
model = pulp.LpProblem("Maximize number", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += lemonade + fruit_juice

# Додамо обмеження на використання ресурсів
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

# Розв'яжемо задачу
model.solve()

# Отримаємо результати
lemonade_units = value(lemonade)
fruit_juice_units = value(fruit_juice)
total_production = value(model.objective)

print(lemonade_units, fruit_juice_units, total_production)
