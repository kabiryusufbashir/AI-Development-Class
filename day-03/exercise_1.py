import numpy as np

scores = np.array([
    [78, 85, 92, 67],
    [45, 60, 55, 49],
    [88, 76, 95, 90],
    [52, 47, 69, 73],
    [91, 84, 39, 80]
])

student_averages = np.mean(scores, axis=1)
subject_averages = np.mean(scores, axis=0)
highest_score = np.max(scores)
lowest_score = np.min(scores)
scores_below_50 = scores[scores < 50]

print("Student Scores:")
print(scores)

print("Each student's average:", student_averages)
print("Each subject's average:", subject_averages)
print("Highest overall score:", highest_score)
print("Lowest overall score:", lowest_score)
print("Scores below 50:", scores_below_50)
