l = ["Bob", "Rolf", "Anne"]
''' tuple cannot be modify '''
t = ("Bob", "Rolf", "Anne")
''' set has no duplicate elements and no order '''
s = {"Bob", "Rolf", "Anne"}

l[0] = "Smith"
l.append("Pepe")
l.remove("Anne")
s.add("Whatever")
print(l)
print(l[0])
print(t[1])
print(s)