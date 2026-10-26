import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("preped_data.csv")

data_9 = data[data["time"] == "9:00 AM"]
data_2 = data[data["time"] == "2:00 PM"]
data_4 = data[data["time"] == "4:00 PM"]

avg_9 = data_9["occupancy_percentage"].mean()
avg_2 = data_2["occupancy_percentage"].mean()
avg_4 = data_4["occupancy_percentage"].mean()

times = ["9 AM", "2 PM", "4 PM"]
occupancy = [avg_9, avg_2, avg_4]

plt.bar(times, occupancy)

plt.xlabel("Time")
plt.ylabel("Average Occupancy")
plt.title("Average Occupancy by Time")

plt.savefig("task3_occupancy.png")

plt.figure()

quiet_data = data[data["noise_level"] == "Quiet"]
medium_data = data[data["noise_level"] == "Medium"]
loud_data = data[data["noise_level"] == "Loud"]

avg_quiet = quiet_data["occupancy_percentage"].mean()
avg_medium = medium_data["occupancy_percentage"].mean()
avg_loud = loud_data["occupancy_percentage"].mean()

noise = ["Quiet", "Medium", "Loud"]
occupancy = [avg_quiet, avg_medium, avg_loud]

plt.bar(noise, occupancy)

plt.xlabel("Noise Level")
plt.ylabel("Average Occupancy")
plt.title("Average Occupancy by Noise Level")

plt.savefig("task3_noise.png")

plt.figure()

pier = data[data["location"] == "SCE - Pier Room"]
inner = data[data["location"] == "SCE - Inner Circle"]
lib1 = data[data["location"] == "Library - 1st Floor"]
lib2 = data[data["location"] == "Library - 2nd Floor"]

pier_9 = pier[pier["time"] == "9:00 AM"]["outlet_score"].mean()
pier_2 = pier[pier["time"] == "2:00 PM"]["outlet_score"].mean()
pier_4 = pier[pier["time"] == "4:00 PM"]["outlet_score"].mean()

inner_9 = inner[inner["time"] == "9:00 AM"]["outlet_score"].mean()
inner_2 = inner[inner["time"] == "2:00 PM"]["outlet_score"].mean()
inner_4 = inner[inner["time"] == "4:00 PM"]["outlet_score"].mean()

lib1_9 = lib1[lib1["time"] == "9:00 AM"]["outlet_score"].mean()
lib1_2 = lib1[lib1["time"] == "2:00 PM"]["outlet_score"].mean()
lib1_4 = lib1[lib1["time"] == "4:00 PM"]["outlet_score"].mean()

lib2_9 = lib2[lib2["time"] == "9:00 AM"]["outlet_score"].mean()
lib2_2 = lib2[lib2["time"] == "2:00 PM"]["outlet_score"].mean()
lib2_4 = lib2[lib2["time"] == "4:00 PM"]["outlet_score"].mean()

labels = [
    "Pier 9AM", "Pier 2PM", "Pier 4PM",
    "Inner 9AM", "Inner 2PM", "Inner 4PM",
    "Lib1 9AM", "Lib1 2PM", "Lib1 4PM",
    "Lib2 9AM", "Lib2 2PM", "Lib2 4PM"
]

values = [
    pier_9, pier_2, pier_4,
    inner_9, inner_2, inner_4,
    lib1_9, lib1_2, lib1_4,
    lib2_9, lib2_2, lib2_4
]

plt.bar(labels, values)

plt.ylabel("Outlet Availability")
plt.title("Outlet Availability by Location and Time")

plt.yticks([1, 2, 3], ["Easy", "Medium", "Hard"])
plt.xticks(rotation=45)

plt.savefig("task3_outlets.png")
plt.show()
