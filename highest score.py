<<<<<<< HEAD
names = []
scores = []
age = []
result_f = open("results.txt")
for line in result_f:
    (names, scores, age) = line.split()
    names.append(name)
    scores.append(float(score))
    age.append(age)
result_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("The top scores were:")
print(scores[0])
print(scores[1])
print(scores[2])
=======
names = []
scores = []
age = []
result_f = open("results.txt")
for line in result_f:
    (names, scores, age) = line.split()
    names.append(name)
    scores.append(float(score))
    age.append(age)
result_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("The top scores were:")
print(scores[0])
print(scores[1])
print(scores[2])
>>>>>>> 8162d74a42f4593e60b9831a9f4ee35d5cf1f5c9
