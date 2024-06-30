links1 = []
links2 = []

matching_links = []
mismatched_links = []

with open("Ссылки1.txt", "r") as f:
    for i in f:
        links1.append(i.replace("\n", ""))

with open("Ссылки2.txt", "r") as f:
    for i in f:
        links2.append(i.replace("\n", ""))


for i in links1:
    if i in links2 or i.replace("!", "") in links2:
        matching_links.append(i)
    else:
        mismatched_links.append(i)

for i in links2:
    if i not in links1 and i.replace("!", "") not in links1:
        mismatched_links.append(i)

with open("Совпадающие ссылки.txt", "w") as f:
    for i in matching_links:
        f.write(f"{i}\n")

with open("Несовпадающие ссылки.txt", "w") as f:
    for i in mismatched_links:
        f.write(f"{i}\n")

print(matching_links)
print(mismatched_links)
