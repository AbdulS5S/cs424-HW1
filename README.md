# cs424-HW1
Collecting data and sketching visualizations

## Task 1

For this project, I want to look at different study spaces around UIC. As I use these places a lot, and I noticed that some can be really crowded and busy at certain times while others are not. Other than that some places are also quieter, better for group work, or have more seats and outlets available. I want to compare a few study spaces and see how they change depending on the time.

### Domain Questions

1. Which study spaces are usually the most crowded?
2. How does the noise level change at different places and times?
3. Which study spaces are used more for group work and which are used more for studying alone?
4. At what times and in which study spaces are seats and outlets harder to find?

### Data Collection Plan
So if we talk about Data Collection Plan It is:
One observation will be one study space at a certain time.

So i will look at around 3 or 4 study spaces around UIC at different times. Each time, I will record the location, time, how many seats are being used, how many seats there are total, the noise level, whether people are mostly alone or in groups, and how easy it is to find an outlet.

So looking at different places and different times will help me compare the study spaces instead of only looking at one place.

As I am doing this project by myself, I will collect all of the data. I will try to use the same categories each time so the observations stay consistent.

One limitation is that things like noise level and whether people are studying alone or in groups are based on what I see, so they might not always be exact. Also, the number of people in a study space can change pretty quickly.

### Initial Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| `location` | Categorical | Study space being observed | Library |
| `time` | Temporal | Time I looked at the space | 6:00 PM |
| `filled_seats` | Quantitative | About how many seats are being used | 50 |
| `total_seats` | Quantitative | About how many seats are in the area | 55 |
| `noise_level` | Ordered | How noisy the space is | Quiet / Medium / Loud |
| `study_activity` | Categorical | Whether people are mostly alone, in groups, or mixed | Mostly alone |
| `free_outlet` | Ordered | How easy it is to find an free outlet | Easy / Medium / Hard |

## Task 2:

So I collected 12 observations from the four study spaces. While collecting the data, I noticed that counting the exact number of occupied seats and total seats was harder than I expected, especially when the spaces were busy.

So because of this, I changed to `occupancy_percentage`. As instead of counting every seat, I estimated how full the space was as a percentage. This was much easier to record and still showed how crowded each study space was.

Other than that, the other attributes like for example noise level, study activity, and outlet availability worked fine, so I kept them the same.

For the final data collection, I observed the four study spaces on multiple days at around 9 AM, 2 PM, and 4 PM. I ended up with 24 total observations. The full dataset is included in the csv file.

### Final Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| `date` | Temporal | Date of the observation | 2026-09-22 |
| `location` | Categorical | Study space being observed | SCE - Pier Room |
| `time` | Temporal | Time of the observation | 2:00 PM |
| `occupancy_percentage` | Quantitative | Percentage of the study space that was occupied | 90% |
| `noise_level` | Ordered | How noisy the study space was | Quiet / Medium / Loud |
| `study_activity` | Categorical | Whether people were mostly alone, in groups, or mixed | Mixed |
| `outlet_availability` | Ordered | How easy it was to find an available outlet | Easy / Medium / Hard |
