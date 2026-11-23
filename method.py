from collections import defaultdict

numbers = defaultdict(int)

numbers["apple"] += 1

print(numbers["apple"])  # 1
print(numbers["banana"]) # 0




from collections import deque

queue = deque([10, 20, 30])

queue.popleft()

print(queue)



from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)



from collections import Counter

fruits = Counter(["apple", "banana", "apple", "orange", "banana", "apple"])

print(fruits.most_common(2))



from collections import deque

queue = deque([10, 20, 30])

queue.append(40)

print(queue)



def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)