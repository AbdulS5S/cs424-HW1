import pandas as pd

data = pd.read_csv("CS424.csv")

print(data)

print(data.isnull())

print(data.duplicated())

data["date"] = pd.to_datetime(data["date"])

data["occupancy_percentage"] = pd.to_numeric(data["occupancy_percentage"])

data["time_order"] = data["time"].replace({
    "9:00 AM": 1,
    "2:00 PM": 2,
    "4:00 PM": 3
})

data["noise_score"] = data["noise_level"].replace({
    "Quiet": 1,
    "Medium": 2,
    "Loud": 3
})

data["outlet_score"] = data["outlet_availability"].replace({
    "Easy": 1,
    "Medium": 2,
    "Hard": 3
})

data.to_csv("preped_data.csv", index=False)

print("finished")
