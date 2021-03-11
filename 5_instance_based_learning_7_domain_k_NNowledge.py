# Python Program to calculate euclidian distance and manhattan distance
import math

#regression = average

#pos_x = float(input("position x"))
#pos_y = float(input("position y"))

pos_x = 4
pos_y = 2

nn1_x = 1
nn1_y = 6
nn1_val = 7

nn2_x = 2
nn2_y = 4
nn2_val = 8

nn3_x = 3
nn3_y = 7
nn3_val = 16

nn4_x = 6
nn4_y = 8
nn4_val = 44

nn5_x = 7
nn5_y = 1
nn5_val = 50

nn6_x = 8
nn6_y = 4
nn6_val = 68


euclidian_distance1 = math.sqrt((nn1_x - pos_x)**2 + (nn1_y - pos_y)**2)
manhattan_distance1 = abs(nn1_x - pos_x) + abs(nn1_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t\t\t and {3}".format(nn1_x, nn1_y, euclidian_distance1, manhattan_distance1))

euclidian_distance2 = math.sqrt((nn2_x - pos_x)**2 + (nn2_y - pos_y)**2)
manhattan_distance2 = abs(nn2_x - pos_x) + abs(nn2_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t and {3}".format(nn2_x, nn2_y, euclidian_distance2, manhattan_distance2))

euclidian_distance3 = math.sqrt((nn3_x - pos_x)**2 + (nn3_y - pos_y)**2)
manhattan_distance3 = abs(nn3_x - pos_x) + abs(nn3_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t and {3}".format(nn3_x, nn3_y, euclidian_distance3, manhattan_distance3))

euclidian_distance4 = math.sqrt((nn4_x - pos_x)**2 + (nn4_y - pos_y)**2)
manhattan_distance4 = abs(nn4_x - pos_x) + abs(nn4_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t and {3}".format(nn4_x, nn4_y, euclidian_distance4, manhattan_distance4))

euclidian_distance5 = math.sqrt((nn5_x - pos_x)**2 + (nn5_y - pos_y)**2)
manhattan_distance5 = abs(nn5_x - pos_x) + abs(nn5_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t and {3}".format(nn5_x, nn5_y, euclidian_distance5, manhattan_distance5))

euclidian_distance6 = math.sqrt((nn6_x - pos_x)**2 + (nn6_y - pos_y)**2)
manhattan_distance6 = abs(nn6_x - pos_x) + abs(nn6_y - pos_y)
print("The euclidian and manhattan distance of {0},{1} to the position of interest = {2} \t and {3}".format(nn6_x, nn6_y, euclidian_distance6, manhattan_distance6))

#put the distances in an array
euclidian_distances = [euclidian_distance1, euclidian_distance2, euclidian_distance3, euclidian_distance4, euclidian_distance5, euclidian_distance6]; 
manhattan_distances = [manhattan_distance1, manhattan_distance2, manhattan_distance3, manhattan_distance5, manhattan_distance6, manhattan_distance6];

print()
one_nn_euclid_distance = nn2_val/1 #need to automate distance selection
three_nn_euclid_distance = (nn2_val + nn5_val + nn6_val)/3 #need to automate distance selection
print("1-NN euclidian distance to the position of interest = {0}".format(one_nn_euclid_distance))
print("3-NN euclidian distance to the position of interest = {0}".format(three_nn_euclid_distance))
one_nn_manhattan_distance = (nn2_val+nn5_val)/2 #need to automate distance selection
three_nn_manhattan_distance = (nn2_val + nn5_val + nn3_val + nn6_val)/4 #need to automate distance selection
print("1-NN manhattan distance to the position of interest = {0}".format(one_nn_manhattan_distance))
print("3-NN manhattan distance to the position of interest = {0}".format(three_nn_manhattan_distance))
#1_nn and 3_nn should be not too far off, if it is then there is a lot of variance in the spatial dataset
#also since we are using regression, just average the numbers.

#function: y = (x_1)^2 + x_2 = 18, the first feature is more important
#number is all well off

#preference bias of KNN
#1. locality - near points are similar
#2. smoothness - averaging
#3. all points matter equally

#curse of dimensionality
#locally weighted regression

#instance based learning
#lazy vs eager learning
#KNN
#nearest neighbour: similarity (distance)
#domain knowledge matters
#classification vs. regression
#averaging
#locally weighted regression
#bellman's curse of dimentionality o(d^2)
#you need to know a little bit about the problem to solve the problem

