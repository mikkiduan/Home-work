
n = 6786876084
approx = n/2
while True:
    better = (approx + n/approx)/2
    print(better)
    if abs(better - approx) < 0.00001:
        if better ** 2== n:
           
        return better
    approx = better

print(better)
            