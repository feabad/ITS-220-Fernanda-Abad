<<<<<<< HEAD
scores = []
names = []
result_f = open("results.txt") 
for line in result_f:
 (names, scores) = line.split()
 scores.append(float(scores))
 names.append(names)
result_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("The highest scores were:")
print(names[0]+'with'+str(scores[0])
print(names[1]+'with'+str(scores[1])
print(names[2]+'with'+str(scores[2])
=======
scores = []
names = []
result_f = open("results.txt") 
for line in result_f:
 (names, scores) = line.split()
 scores.append(float(scores))
 names.append(names)
result_f.close()
scores.sort()
scores.reverse()
names.sort()
names.reverse()
print("The highest scores were:")
print(names[0]+'with'+str(scores[0])
print(names[1]+'with'+str(scores[1])
print(names[2]+'with'+str(scores[2])
>>>>>>> 8162d74a42f4593e60b9831a9f4ee35d5cf1f5c9
