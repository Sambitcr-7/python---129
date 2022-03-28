def percent(marks):
#  return ((marks[0]+ marks[1] + marks[2]+marks[2] +marks[3] )/400)*100
 p = ((marks[0]+ marks[1] + marks[2]+marks[2] +marks[3] )/400)*100
 return p
# percentage1 = (sum(marks)/400)*100



marks1 = [45, 78,86,77]
# percentage1 = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
percentage1 = percent(marks1)




marks2 = [75,98,78]
# percentage2 = (sum(marks2)/400)*100
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100
percentage2 = percent(marks2)
print(percentage1,percentage2)