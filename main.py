print("enter no. of function")
print("-1-binomial")
print("-2-negative binomial")
print("-3-geomitric")
print("-4-hyper_geomitric")
print("-5-poisson")
print("your input:")

x = int(input("your input:"))

if x == 1:
    import binomial
    binomial

elif x == 2:
    import neg_binomial
    neg_binomial
elif x == 3:
    import geometric
    geometric
elif x == 4:
    import hygeo
    hygeo
elif x == 5:
    import poisson
    poisson
else:
    print("wrong input!!!!")