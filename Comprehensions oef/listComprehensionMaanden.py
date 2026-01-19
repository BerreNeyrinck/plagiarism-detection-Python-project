maanden= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# maandenNUM = [f"{maanden.index(mon)+1}: " + mon[:3].upper() for mon in maanden]

maandenNUM = [f"{index}: {mon[:3].upper()}" for (index,mon) in enumerate(maanden, start=1)]

print(maandenNUM)