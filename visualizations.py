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

plt.figure(figsize=(9, 7))

plt.subplot(2, 2, 1)
plt.plot(times, [pier_9, pier_2, pier_4], marker="o")
plt.title("Pier Room")

plt.subplot(2, 2, 2)
plt.plot(times, [inner_9, inner_2, inner_4], marker="o")
plt.title("Inner Circle")

plt.subplot(2, 2, 3)
plt.plot(times, [lib1_9, lib1_2, lib1_4], marker="o")
plt.title("Library 1st Floor")

plt.subplot(2, 2, 4)
plt.plot(times, [lib2_9, lib2_2, lib2_4], marker="o")
plt.title("Library 2nd Floor")

plt.tight_layout()

plt.savefig("task6_it1.png")

plt.figure(figsize=(9, 7))

plt.subplot(2, 2, 1)
plt.plot(times, [pier_9, pier_2, pier_4], marker="o")
plt.title("Pier Room")
plt.ylim(0, 110)
plt.text(0, pier_9 + 2, str(round(pier_9, 1)) + "%")
plt.text(1, pier_2 + 2, str(round(pier_2, 1)) + "%")
plt.text(2, pier_4 + 2, str(round(pier_4, 1)) + "%")

plt.subplot(2, 2, 2)
plt.plot(times, [inner_9, inner_2, inner_4], marker="o")
plt.title("Inner Circle")
plt.ylim(0, 110)
plt.text(0, inner_9 + 2, str(round(inner_9, 1)) + "%")
plt.text(1, inner_2 + 2, str(round(inner_2, 1)) + "%")
plt.text(2, inner_4 + 2, str(round(inner_4, 1)) + "%")

plt.subplot(2, 2, 3)
plt.plot(times, [lib1_9, lib1_2, lib1_4], marker="o")
plt.title("Library 1st Floor")
plt.ylim(0, 110)
plt.text(0, lib1_9 + 2, str(round(lib1_9, 1)) + "%")
plt.text(1, lib1_2 + 2, str(round(lib1_2, 1)) + "%")
plt.text(2, lib1_4 + 2, str(round(lib1_4, 1)) + "%")

plt.subplot(2, 2, 4)
plt.plot(times, [lib2_9, lib2_2, lib2_4], marker="o")
plt.title("Library 2nd Floor")
plt.ylim(0, 110)
plt.text(0, lib2_9 + 2, str(round(lib2_9, 1)) + "%")
plt.text(1, lib2_2 + 2, str(round(lib2_2, 1)) + "%")
plt.text(2, lib2_4 + 2, str(round(lib2_4, 1)) + "%")

plt.tight_layout()

plt.savefig("task6_it2.png")

plt.show()
