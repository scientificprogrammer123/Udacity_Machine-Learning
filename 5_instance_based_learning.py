# lesson 1, instance based learning
# before:
# ^
# |     *    <x,y>1
# |    *     <x,y>2
# |   *      <x,y>3
# |  *       <x,y>4
# | *        <x,y>5     => f(x)
# _______
#
# this sucks, don't do this, no learning, no function etc etc

# lesson 2, instance based learning now
# <x,y>1
# <x,y>2
# <x,y>3
# <x,y>4
# now use a lookup table, and do f(x)=lookup(x)
# it remembers
# it is fast
# it is simple
# wx+b, it is conservative, not willing to go out on a limb, no generalization
# it is sensitive to noise?
# generalization? no
# overfitting? yes

# lesson 3, cost of the house
# black dot house is in the same neighbourhood as the other colour houses
# look at the nearest neighbour
# look at the nearest neighbours, look at more neighbours

# lesson 4, cost of the house 2
# k nearest neighbour, make k a free parameter
# distance is analogous to similarity
# K nearest neighbour
# 

# lesson 5, KNN
# given: training data D={x_i, y_i}
#        distance metric d(q,x), similarity function, i.e. domain knowledge
#        number of neighbours k, you care about, i.e. domain knowledge
#        query point q, 
#  - NN = {i: d(q, x_i) k smallest}, find these closest neighbours to the query point, a set of points
#
# return:
#  - classification, in classification, we want a label, they should "vote", of the Y_is, take the plurality, mode, what if they are tied, then pick one
#          NN = {i: d(q,x_i) k smallest}, you have the Ys associate with the NNs, so they should vote
#          whichever the Yi is the most frequent among the closest points wins.
#          find a vote f the Yis, and you take the plurality, whichever one occurs the most frequently, the mode
#          If there is a tie, then you pick the closest one, the one that is most commonly represented in the data
#          period, or randomly pick each time, or some other method.
#  - regression, in regresion the y_is are numbers, we have a bunch of numbers, 
#          and we have the closest y_is, take the average of these numbers, the mean
#          no need to deal with the tie
#          
# It is very simple algorithm, but a lot of things are left to the designer, i.e.
# distance metric, the number k, how you are going to break the tie, how you choose
# to implement the voting, mean or the average operation you choose to do here.
#
# Another thing you can do is do a vote that is say, weighted by how far away you are,
# that would help with the tie, you could also do weighted average, the Y_i values that
# are closer to the query point are weighted higher, weighted by similarity, like 1/distance.
# 2 quizzes.

# lesson 6, won't you compute my nearest neighbour?
# given n sorted data points,
# 3 different learning allgorithms
# we want to know running time and space
# the 3 cases are 1 nearest neighbour, k nearest neighbour, and linear regression
# points are already sorted
# we are given a query point, 
# how much space you need to accomplish your task, after training
# There is a time to learn, space to learn
# Then there is a query,
# What is the big(o) time?
# 
#                  running time      space
# 1-NN   learning             1          n
#        query         log_2(n)          1
# k-NN   learning             1          n
#        query       log_2(n)+k          1
# linear learning             n    1 (m,b)
# regres query                1          1
#
# For one nearest neighbour, for learning you just take the sorted list and leave it there. The classifier
# or regresser has linear space. At query time, you take the sorted list and find the nearest neighbour,
# because list is sorted, you can use binary search, which has log_2(n) time, if it is not sorted
# you need n time.
# For space you need constant 1.
#
# For K nearest neighbour, for learning/training is the same process as one nearest neighbour, 
# you just pass the sorted list along, so time is 1. Space is n. For query, it seems 
# more subtle, single nearest neighbout time is 1, Once it is found, then the other k-1
# nearest neighbout might be k-1, so it is log_2(n)+k, we know that k is smaller or equal 
# to n. Space, you would need 1 space, or constant space.
#
# For linear regression, for learning you map real number input to real number output, 
# take mx+b form, need to find m and b, need to invert matrix, scanning through list
# so order n, there is probably a nice linear regression algorithm for it. For space
# the data passed forward, m, b, so constant time.
# For query the time is 1, for query the time is 1. 
# So for liner regression, the time for learning is long, the time for computing is short.
#
# Linear regression is a eager learner, 1-NN and K-NN are lazy learners

# lesson7 - domain k knowledge
# Python Program to calculate euclidian distance and manhattan distance
import math
#
# regression = average
#
# pos_x = float(input("position x"))
# pos_y = float(input("position y"))
#
# query point
pos_x = 4
pos_y = 2
#
# datapoints
nn1_x = 1
nn1_y = 6
nn1_val = 7
print("Datapoint 1 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn1_x, nn1_y, nn1_val))
#
nn2_x = 2
nn2_y = 4
nn2_val = 8
print("Datapoint 2 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn2_x, nn2_y, nn2_val))
#
nn3_x = 3
nn3_y = 7
nn3_val = 16
print("Datapoint 3 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn3_x, nn3_y, nn3_val))
#
nn4_x = 6
nn4_y = 8
nn4_val = 44
print("Datapoint 4 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn4_x, nn4_y, nn4_val))
#
nn5_x = 7
nn5_y = 1
nn5_val = 50
print("Datapoint 5 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn5_x, nn5_y, nn5_val))
#
nn6_x = 8
nn6_y = 4
nn6_val = 68
print("Datapoint 6 x-pos, y-pos, value ={0},{1}, \t and {2}".format(nn6_x, nn6_y, nn6_val))
print()
# compute euclidian distances from  dataset to query point
euclidian_distance1 = math.sqrt((nn1_x - pos_x)**2 + (nn1_y - pos_y)**2)
manhattan_distance1 = abs(nn1_x - pos_x) + abs(nn1_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t\t\t and {3}".format(nn1_x, nn1_y, euclidian_distance1, manhattan_distance1))
#
euclidian_distance2 = math.sqrt((nn2_x - pos_x)**2 + (nn2_y - pos_y)**2)
manhattan_distance2 = abs(nn2_x - pos_x) + abs(nn2_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t and {3}".format(nn2_x, nn2_y, euclidian_distance2, manhattan_distance2))
#
euclidian_distance3 = math.sqrt((nn3_x - pos_x)**2 + (nn3_y - pos_y)**2)
manhattan_distance3 = abs(nn3_x - pos_x) + abs(nn3_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t and {3}".format(nn3_x, nn3_y, euclidian_distance3, manhattan_distance3))
#
euclidian_distance4 = math.sqrt((nn4_x - pos_x)**2 + (nn4_y - pos_y)**2)
manhattan_distance4 = abs(nn4_x - pos_x) + abs(nn4_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t and {3}".format(nn4_x, nn4_y, euclidian_distance4, manhattan_distance4))
#
euclidian_distance5 = math.sqrt((nn5_x - pos_x)**2 + (nn5_y - pos_y)**2)
manhattan_distance5 = abs(nn5_x - pos_x) + abs(nn5_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t and {3}".format(nn5_x, nn5_y, euclidian_distance5, manhattan_distance5))
#
euclidian_distance6 = math.sqrt((nn6_x - pos_x)**2 + (nn6_y - pos_y)**2)
manhattan_distance6 = abs(nn6_x - pos_x) + abs(nn6_y - pos_y)
print("The euclidian distance, and manhattan distance from {0},{1} to the position of interest = {2} \t\t and {3}".format(nn6_x, nn6_y, euclidian_distance6, manhattan_distance6))
# put the distances in an array
euclidian_distances = [euclidian_distance1, euclidian_distance2, euclidian_distance3, euclidian_distance4, euclidian_distance5, euclidian_distance6]; 
manhattan_distances = [manhattan_distance1, manhattan_distance2, manhattan_distance3, manhattan_distance5, manhattan_distance6, manhattan_distance6];
###
### need to automatically select the distances from query point to nearest neighbours ###
###
print()
one_nn_euclid_distance = nn2_val/1 ###need to automate distance selection
three_nn_euclid_distance = (nn2_val + nn5_val + nn6_val)/3 ###need to automate distance selection
print("The value of 1-NN using euclidian distance to the position of interest = {0}".format(one_nn_euclid_distance))
print("The value of 3-NN using euclidian distance to the position of interest = {0}".format(three_nn_euclid_distance))
print()
one_nn_manhattan_distance = (nn2_val+nn5_val)/2 #need to automate distance selection, there are 2 neighbours that are closest to query point
three_nn_manhattan_distance = (nn2_val + nn5_val + nn3_val + nn6_val)/4 #need to automate distance selection, there are 4 neighbours that are closest to query point
print("The value of 1-NN using manhattan distance to the position of interest = {0}".format(one_nn_manhattan_distance))
print("The value of 3-NN using manhattan distance to the position of interest = {0}".format(three_nn_manhattan_distance))
# 1_nn and 3_nn should be not too far off, if it is then there is a lot of variance in the spatial dataset
# also since we are using regression, just average the numbers.
#
# You get different answers based on what you what method you use.
#
# Charles has a function in mind for regression:
# function: y = (x_1)^2 + x_2, using this function, the answer is 18
# K-nn does not seem to do well, because none of the answers match the function

# lesson 8, KNN bias
# preference bias of KNN - our belief about what makes a good hypothesis
# 1. locality - near points are similar to one another, there is some distance function that minimizes sum of square error, so there should be a best distance function
# 2. smoothness - averaging, we expect functions to behave smoothly
# 3. all features matter equally
#
# So it's a mix of the manhattan distance and euclidian distance, So Michael is taking the euclidian distance, 
# take the first component, take the difference, square it, take the second component, 
# take the difference, absolute value it, add those things together, if he does the absolute value of it, 
# he still gets a tie, but the output answer ends being 12, which is better than 24.7, and that is better
# than 8, which is what it was before.

# lesson 9, curse of dimensionality
# As the number of features or dimensions grow, the amount of data we need to generalize accurately
# also grows exponentially.
#
# The curse of dimensionality says that everytime you add one of these features, you add another dimension
# to your input space, you add another dimension to your input space, and you are going to need
# exponentially more data as you add those features, in order to be able to generalize accurately.
#
# This is a very serious problem, and it captures a little bit of what the difficulties are in KNN. If 
# you have a distance function or a similarity function, that assumes everthing is relevant, or equally
# relevant, or important, and some of them aren't, you are going to see a lot of data before you can
# figure that out, before it sort of washes itself away. It helps to draw a picture, next lesson.

# lesson 10, curse of dimensionality 2
# 2 dots on a line:
# .----------., 10 spaces between these 2 points
# each green x segment is 1/10.
#
# Next we go to a 2 d segment
# .
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# .----------.
# now yu'll notice, that each x still represents 1/10 of the space, but that the 1/10
# it is representing is really really big. How can I make it so that each of the x I
# put down represent ...
# fill up the x'ses represent a square.
# There are 100 x's, 100 points need to cover space
#
# What happens if I want to move in 3 dimensions, so 10^3 datapoints, or 1000 datapoints
# so curse of dimensionality is a curse for ML in general. It is a real problem.

# lesson 11, some other stuff
# distance metric d(x,q) = euclidian, manhattan (weighted distance)
# a way to deal with curse of dimensinality
# mismatches
#
# how to pick k, what happens when k=n? average all of the numbers, 
# What happens if you do a weighted average. Near the points of query, you will
# see more influence than the fuer away points of query.
#
# locally weighted regression
# locally weighted linear regression, this would end up looking like a curve.
# This is cool because you start with a bunch of lines, then end up with a more
# complicated curve that is complicated by the data around your point of interest.

# lesson 12, what we have learned?
# instance based learning, why is it called instance based learning? because we
# learn based on the instance we have brought up
#
# lazy vs eager learning, lazy learning puts off the work until needed, 
#
# KNN - lazy learner, k nearest neighbour
#
# nearest neighbour: similarity (distance), what it means. Similarity is another way
# to capture domain knowledge, KNN is another way to capture domain knowledge.
# domain knowledge matters.
#
# classification vs. regression, KNN can handle both of them
#
# notion of similarity and notion of averaging, overall term for a bunch of things
#
# How to compose various different learning algorithms together, i.e.locally weighted regression, instance based
# idea along with linear regression to get local weighted regression, locally smooth, globally bumpy
#
# bellman's curse of dimentionality o(d^2), more features you include, more data you need to fill up that space, exponential
# eg y=x1^2 + x2, 10/12 examples bad, 100k good, a lot of data needed
#
# To get around the curse of dimensionality, you need to blunt it, you need to know a 
# little bit about the problem to solve the problem. Any learning algorithm is going to be
# no better than average, unless you have domain knowledge, so domain knowledge
# matters!!
#
# So for ML, you need to know a little bit about the problem to know what you do.
# Whole point of class is to expose students to different techniques, and domain
# knowledge so people know what to do to best utilize machine learning.

