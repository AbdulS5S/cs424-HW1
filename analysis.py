import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("assignment3_evaluation_data.csv")

static = data[data["condition"] == "Static"]
interactive = data[data["condition"] == "Interactive"]

static_accuracy = static["accuracy"].mean() * 100
interactive_accuracy = interactive["accuracy"].mean() * 100

print("Static accuracy:", static_accuracy)
print("Interactive accuracy:", interactive_accuracy)

static_time = static["time_seconds"].mean()
interactive_time = interactive["time_seconds"].mean()

print("Static average time:", static_time)
print("Interactive average time:", interactive_time)

print("Static median time:", static["time_seconds"].median())
print("Interactive median time:", interactive["time_seconds"].median())

print("Static min time:", static["time_seconds"].min())
print("Interactive min time:", interactive["time_seconds"].min())

print("Static max time:", static["time_seconds"].max())
print("Interactive max time:", interactive["time_seconds"].max())

static_task1 = static[static["task"] == 1]["time_seconds"].mean()
static_task2 = static[static["task"] == 2]["time_seconds"].mean()

interactive_task1 = interactive[interactive["task"] == 1]["time_seconds"].mean()
interactive_task2 = interactive[interactive["task"] == 2]["time_seconds"].mean()

print("Static Task 1 average:", static_task1)
print("Static Task 2 average:", static_task2)

print("Interactive Task 1 average:", interactive_task1)
print("Interactive Task 2 average:", interactive_task2)

for i in range(1, 11):
    participant = "Participant_" + str(i)

    p_static = static[static["participant_id"] == participant]
    p_interactive = interactive[interactive["participant_id"] == participant]

    print(participant)
    print("Static:", p_static["time_seconds"].mean())
    print("Interactive:", p_interactive["time_seconds"].mean())

plt.bar(["Static", "Interactive"], [static_accuracy, interactive_accuracy])
plt.ylabel("Accuracy (%)")
plt.title("Accuracy by Condition")
plt.ylim(0, 110)
plt.savefig("task4_accuracy.png")
plt.close()

plt.bar(["Static", "Interactive"], [static_time, interactive_time])
plt.ylabel("Average Time (seconds)")
plt.title("Average Completion Time")
plt.savefig("task4_time.png")
plt.close()
