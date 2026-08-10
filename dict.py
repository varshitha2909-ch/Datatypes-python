D1={"Sid":1001,"Sname":"Varshi","Smarks":942,"Subject":"Python"}
print(D1)
print(type(D1))

print("====Operations====")
print(D1.keys())

print(D1.values())

print(D1.items())

print(D1.pop("Smarks"))
print(D1)

print(D1.popitem())
print(D1)

D1.update({"Sid":2002})
print(D1)

D2=D1.get("Sname")
print(D2)
