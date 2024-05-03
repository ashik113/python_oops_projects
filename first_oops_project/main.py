from medicine import Medicine
from solution import Solution

list_medicines = []
n = int(input())
for i in range(n):
    medicine_name = input()
    batch = input()
    disease = input()
    price = int(input())

    list_medicines.append(Medicine(medicine_name=medicine_name, batch=batch, disease=disease, price=price))

disease = input()
result = Solution.get_price_by_disease(medicines=list_medicines, disease=disease)
for i in result:
    print(i)
