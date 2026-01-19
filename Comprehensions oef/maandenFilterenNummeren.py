maanden= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# maandenNUM = [f"{index}: {mon[:3].upper()}" for (index,mon) in enumerate(maanden, start=1) if len(mon) <= 5]
maandenNUM = [f"{index}: {mon[:3].upper()}" for (index, mon) in enumerate([month for month in maanden if len(month) <= 5])]

print(maandenNUM)