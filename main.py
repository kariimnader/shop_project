from shop.prices import total as t
from shop.discounts import apply_discount as ad
from shop.delivery import delivery_fee as df
bill = t(50, 3)
print("Original bill:", bill)
print("After discount:", ad(bill))
print("With delivery:", df(ad(bill)))