import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

data = pd.read_csv("preped_data.csv")

pier = data[data["location"] == "SCE - Pier Room"]
inner = data[data["location"] == "SCE - Inner Circle"]
lib1 = data[data["location"] == "Library - 1st Floor"]
lib2 = data[data["location"] == "Library - 2nd Floor"]

pier9 = pier[pier["time"] == "9:00 AM"]["occupancy_percentage"].mean()
pier2 = pier[pier["time"] == "2:00 PM"]["occupancy_percentage"].mean()
pier4 = pier[pier["time"] == "4:00 PM"]["occupancy_percentage"].mean()

inner9 = inner[inner["time"] == "9:00 AM"]["occupancy_percentage"].mean()
inner2 = inner[inner["time"] == "2:00 PM"]["occupancy_percentage"].mean()
inner4 = inner[inner["time"] == "4:00 PM"]["occupancy_percentage"].mean()

lib19 = lib1[lib1["time"] == "9:00 AM"]["occupancy_percentage"].mean()
lib12 = lib1[lib1["time"] == "2:00 PM"]["occupancy_percentage"].mean()
lib14 = lib1[lib1["time"] == "4:00 PM"]["occupancy_percentage"].mean()

lib29 = lib2[lib2["time"] == "9:00 AM"]["occupancy_percentage"].mean()
lib22 = lib2[lib2["time"] == "2:00 PM"]["occupancy_percentage"].mean()
lib24 = lib2[lib2["time"] == "4:00 PM"]["occupancy_percentage"].mean()

times = ["9 AM", "2 PM", "4 PM"]

plt.figure(figsize=(9, 6))

line1, = plt.plot(times, [pier9, pier2, pier4], label="Pier Room")
line2, = plt.plot(times, [inner9, inner2, inner4], label="Inner Circle")
line3, = plt.plot(times, [lib19, lib12, lib14], label="Library 1st Floor")
line4, = plt.plot(times, [lib29, lib22, lib24], label="Library 2nd Floor")

plt.xlabel("Time")
plt.ylabel("Average Occupancy (%)")
plt.title("Occupancy by Location and Time")

plt.legend()

plt.subplots_adjust(right=0.75)

area = plt.axes([0.77, 0.55, 0.2, 0.25])

names = [
    "Pier Room",
    "Inner Circle",
    "Library 1st Floor",
    "Library 2nd Floor"
]

selected = [True, True, True, True]

buttons = CheckButtons(area, names, selected)

def clicked(name):

    if name == "Pier Room":
        if line1.get_visible() == True:
            line1.set_visible(False)
        else:
            line1.set_visible(True)

    if name == "Inner Circle":
        if line2.get_visible() == True:
            line2.set_visible(False)
        else:
            line2.set_visible(True)

    if name == "Library 1st Floor":
        if line3.get_visible() == True:
            line3.set_visible(False)
        else:
            line3.set_visible(True)

    if name == "Library 2nd Floor":
        if line4.get_visible() == True:
            line4.set_visible(False)
        else:
            line4.set_visible(True)

    plt.draw()

buttons.on_clicked(clicked)

plt.show()
