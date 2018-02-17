
>>> user1=[i for i in range(1,15)]
>>> user2 = [i for i in range(10,25)]
>>> user3=list(user1)
>>> user4=list(user2)
>>> set(user3).intersection(user4)
{10, 11, 12, 13, 14}

