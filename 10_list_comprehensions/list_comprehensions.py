numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

'''arrays ids'''
print("friends: ", id(friends), "starts_s: ", id(starts_s))