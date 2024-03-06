import numpy as np
import statistics
# Heights in cm
heights = np.array([150, 160, 155, 180, 170, 165, 163, 158, 175, 165])

# Weights in kg
weights = np.array([50, 55, 60, 80, 70, 65, 62, 58, 75, 68])
print(f"Median of Heights is {statistics.median(heights)}")
print(f"Median of Weights is {statistics.median(weights)}")
print(f"Variance of Heights {np.var(heights)}")
print(f"Standard deviation for Heights is  {np.std(heights)}")

BMI= weights/(heights*0.01)**2
print(f"BMI{BMI}")
averageBMI=np.average(BMI)
print(f"Average for BMI {averageBMI}")