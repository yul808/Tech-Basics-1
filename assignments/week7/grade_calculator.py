#%%
with open("../week7/Technical Basics I_2025 - Sheet1.csv", "r") as f:
    f.readline()
    for line in f:
        line = line.replace("\n", "")
        print(line)
        entries = line.split(",")
        print(entries)
        price = entries[1]

print("*******Due to time problems, this calculator is not able to calculate your grade and will try again later.*******")
#%%
