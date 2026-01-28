Absolutely! 😄 I’ll give you a **bunch of ready-to-copy Python examples** for `map`, `filter`, and `reduce`, all in a clean **Markdown-friendly format** so you can paste them and practice. I’ll cover different domains: finance, health, e-commerce, and data.

---

# 🐍 Python `map`, `filter`, `reduce` Examples

## 1️⃣ Finance: Interest Calculation

```python
from functools import reduce

# Principal amounts
principals = [1000, 2500, 4000, 1500]

# Apply 5% interest
interest = map(lambda x: x * 1.05, principals)

# Keep amounts greater than 3000
high_amounts = filter(lambda x: x > 3000, interest)

# Total sum
total = reduce(lambda a, b: a + b, high_amounts)

print("Total amount with interest above 3000:", total)
```

---

## 2️⃣ E-Commerce: Discounted Prices

```python
from functools import reduce

prices = [150, 500, 1200, 350, 700]

# Apply 10% discount
discounted = map(lambda x: x * 0.9, prices)

# Keep items above 400
premium_items = filter(lambda x: x > 400, discounted)

# Total cost
total_cost = reduce(lambda x, y: x + y, premium_items)

print("Total cost of premium items after discount:", total_cost)
```

---

## 3️⃣ Health: BMI Check

```python
from functools import reduce

# Weights (kg) and heights (m)
weights = [70, 80, 50, 90]
heights = [1.75, 1.8, 1.6, 1.7]

# Calculate BMI
bmi = map(lambda wh: wh[0] / (wh[1] ** 2), zip(weights, heights))

# Filter overweight BMI (>25)
overweight = filter(lambda x: x > 25, bmi)

# Count overweight people
count_overweight = reduce(lambda a, b: a + 1, overweight, 0)

print("Number of overweight people:", count_overweight)
```

---

## 4️⃣ Education: Grade Processing

```python
from functools import reduce

marks = [45, 82, 33, 70, 55]

# Pass marks ≥ 50
passed = filter(lambda x: x >= 50, marks)

# Increase all passed marks by 5
improved = map(lambda x: x + 5, passed)

# Total marks of passed students
total_marks = reduce(lambda a, b: a + b, improved)

print("Total marks of passed students:", total_marks)
```

---

## 5️⃣ Ride-Sharing: Earnings

```python
from functools import reduce

# Distances in km
trips = [3, 8, 15, 2, 7]

# Fare = 15 per km
fares = map(lambda x: x * 15, trips)

# Only trips > 5 km
long_trips = filter(lambda x: x > 75, fares)

# Total earnings
total_earnings = reduce(lambda a, b: a + b, long_trips)

print("Total earnings from long trips:", total_earnings)
```

---

## 6️⃣ IoT Sensors: Temperature Alerts

```python
from functools import reduce

temps_c = [22, 35, 28, 40, 31]

# Convert to Fahrenheit
temps_f = map(lambda c: (c * 9/5) + 32, temps_c)

# Filter readings > 95°F
high_temps = filter(lambda f: f > 95, temps_f)

# Maximum high temperature
max_temp = reduce(lambda a, b: a if a > b else b, high_temps)

print("Maximum high temperature:", max_temp)
```

---

## 7️⃣ Text Processing: Word Lengths

```python
from functools import reduce

words = ["Python", "Data", "Science", "AI", "ML"]

# Length of each word
lengths = map(len, words)

# Keep words longer than 2 letters
long_words = filter(lambda x: x > 2, lengths)

# Total length
total_length = reduce(lambda a, b: a + b, long_words)

print("Total length of long words:", total_length)
```

---

## 8️⃣ Shopping Cart: Item Count by Price

```python
from functools import reduce

items = [150, 200, 50, 1200, 800]

# Items over 100
expensive = filter(lambda x: x > 100, items)

# Count expensive items
count = reduce(lambda a, b: a + 1, expensive, 0)

print("Number of expensive items:", count)
```

---

These are all **ready to run** and practice.

If you want, I can make a **huge “50+ practice examples cheat sheet”** for `map`, `filter`, `reduce` that you can just keep as a Markdown notebook. That way you’ll never run out of practice.

Do you want me to do that?
