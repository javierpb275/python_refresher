friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local_2 = {"Rolf"}
abroad_2 = {"Bob", "Anne"}

friends_2 = local_2.union(abroad_2)

print(friends_2)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)

print(both)