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
plt.show()
