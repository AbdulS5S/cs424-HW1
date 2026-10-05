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

## Task 3: Data Description and Domain Questions

My final dataset has 24 data observations, which represent four study spaces at UIC: SCE Pier Room, SCE Inner Circle, Library 1st Floor, and Library 2nd Floor. These were observed at around 9 AM, 2 PM, and 4 PM on different days and weeks. So In this dataset, I kept the information about the location, the time of observation, percentage of occupied seats, noise level, study activity, and outlet availability.

The data shows how the study spaces change depending on the place and time of day. One limitation is that I only observed each place on a few days, so it might not show what the spaces are like every day. Some of the data was also based on my own judgment. For example, the occupancy percentage was estimated, and sometimes noise level or outlet availability for example could be between two values.

When turning my observations into data, I also lost some details. For example I did not count every person or seat exactly, and did not record things like how long people stayed or why they picked a certain study space. So i mainly focused on the things that were easier to observe and compare.

### Domain Questions

1. **Which study spaces are the most crowded, and how does that change during the day?**  
   I can use `location`, `time`, and `occupancy_percentage` to compare how busy each place gets.

2. **Are more crowded study spaces usually louder?**  
   I can compare `occupancy_percentage` and `noise_level` to see if there is a pattern.

3. **Which places are used more for group study and which are used more for studying alone?**  
   I can use `location` and `study_activity` to compare the different spaces.

4. **When and where are outlets harder to find?**  
   I can compare `outlet_availability`, `location`, `time`, and `occupancy_percentage` to see if outlets are harder to find when a place gets busy.

These questions are pretty similar to my original questions, but I changed them a little based on the data I actually collected. Since i changed from exact seat counts to occupancy percentage, i mostly focused more on how crowded the spaces were instead of the exact number of available seats.
