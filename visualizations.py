import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("preped_data.csv")

pier = data[data["location"] == "SCE - Pier Room"]
inner = data[data["location"] == "SCE - Inner Circle"]
lib1 = data[data["location"] == "Library - 1st Floor"]
lib2 = data[data["location"] == "Library - 2nd Floor"]

pier_9 = pier[pier["time"] == "9:00 AM"]["occupancy_percentage"].mean()
pier_2 = pier[pier["time"] == "2:00 PM"]["occupancy_percentage"].mean()
pier_4 = pier[pier["time"] == "4:00 PM"]["occupancy_percentage"].mean()

inner_9 = inner[inner["time"] == "9:00 AM"]["occupancy_percentage"].mean()
inner_2 = inner[inner["time"] == "2:00 PM"]["occupancy_percentage"].mean()
inner_4 = inner[inner["time"] == "4:00 PM"]["occupancy_percentage"].mean()

lib1_9 = lib1[lib1["time"] == "9:00 AM"]["occupancy_percentage"].mean()
lib1_2 = lib1[lib1["time"] == "2:00 PM"]["occupancy_percentage"].mean()
lib1_4 = lib1[lib1["time"] == "4:00 PM"]["occupancy_percentage"].mean()

lib2_9 = lib2[lib2["time"] == "9:00 AM"]["occupancy_percentage"].mean()
lib2_2 = lib2[lib2["time"] == "2:00 PM"]["occupancy_percentage"].mean()
lib2_4 = lib2[lib2["time"] == "4:00 PM"]["occupancy_percentage"].mean()

times = ["9 AM", "2 PM", "4 PM"]

plt.plot(times, [pier_9, pier_2, pier_4], marker="o", label="Pier Room")
plt.plot(times, [inner_9, inner_2, inner_4], marker="o", label="Inner Circle")
plt.plot(times, [lib1_9, lib1_2, lib1_4], marker="o", label="Library 1st Floor")
plt.plot(times, [lib2_9, lib2_2, lib2_4], marker="o", label="Library 2nd Floor")

plt.xlabel("Time")
plt.ylabel("Average Occupancy (%)")
plt.title("Occupancy by Location and Time")

plt.legend()

plt.savefig("task4_p1.png")

plt.figure()

plt.scatter(data["occupancy_percentage"], data["noise_score"])

plt.xlabel("Occupancy (%)")
plt.ylabel("Noise Level")
plt.title("Occupancy and Noise Level")

plt.yticks([1, 2, 3], ["Quiet", "Medium", "Loud"])

plt.savefig("task4_p2.png")
plt.show()
