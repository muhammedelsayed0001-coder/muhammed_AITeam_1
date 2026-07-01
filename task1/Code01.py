import numpy as np

grades  = np.array([
[85, 78, 92, 88],   
[70, 76, 80, 65],
[90, 88, 94, 91],
[60, 65, 58, 62],
[100,95, 98, 97]
])

# rows = 5 & colums = 4

print(f'shape = {grades .shape}\n' )

#  The mean grade of each student.

# 2d matrix so the axis = 0 is the row and the axis = 1 is the colum 
print(f'mean grade of each student = \n{np.mean(grades , axis=1)}\n')  

print(np.mean(grades[0][0:4]))
print(np.mean(grades[1][0:4]))
print(np.mean(grades[2][0:4]))
print(np.mean(grades[3][0:4]))
print(f'{np.mean(grades[4][0:4])}\n')



#  The mean grade of each subjects.

print(f'{np.mean(grades , axis=0)}\n')

# students whose average grade is greater than 85

print(f'whose average grade is greater than 85 = \n{grades[grades.mean(axis=1)>=85]}\n')

#  Adding a bonus of 5 marks to all grades  

print (f' bonus of 5 marks = {grades  + 5} \n' ) 

# Normalize

Normalize = (f'Normalizetion = \n{(grades- grades.min()/ grades.max() - grades.min())}')
print(f'{Normalize}\n')

# Flatten
print(grades.flatten())