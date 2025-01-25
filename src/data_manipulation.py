import pandas as pd

data = {
    "rocket": ["Falcon 1", "Falcon 9", "Falcon Heavy"],
    "launches": [5, 100, 3],
}

df = pd.DataFrame(data)

print("All data")
print(df)

print("")
print("Rockets")
print(df["rocket"])

falcon9_df = df[df["rocket"] == "Falcon 9"]
print("")
print("Falcon 9")
print(falcon9_df)

df["success_rate"] = [0.4, 0.98, 1.0]
print("")
print("New success rates")
print(df["success_rate"])
