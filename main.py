from shop.prices import total as t
from shop.discounts import apply_discount as ad

bill = t(50, 3)
print("Original bill:", bill)
print("After discount:", ad(bill))