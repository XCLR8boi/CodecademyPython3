last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects =["physics","calculus","poetry","history"]
# lets create a new list called grade
grades = [98,97,85,88]


gradebook =[]
# print(gradebook)
for i in range(len(subjects)):
    gradebook.append([subjects[i],grades[i]])
print(gradebook)

#point 5
gradebook.append(["computer science",100])

# point 6
gradebook.append(["visual arts",93])

# point 7
gradebook[-1][-1] = 98
# print(gradebook)

# point 8 and 9 
gradebook[2][1] = "Pass"
print(gradebook)

# point 10 
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)