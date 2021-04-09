# lesson 1, what is regression?
# supervised learning, take examples of inputs and outputs,
# then take another input, and predict the output
# discrete outputs, continuous outputs,<- we are looking at continuous outputs
# 
# We expect Charles' children to be between Charles' height and average height.

# lesson 2, regression and function approximation
# use a function to approximate the relationship between parent height and children
# height. This is called regression to the mean.

# lesson 3, regression in machine learning
# have to interpolate
# linear relationship, minimize linear relationship
# 

# lesson 4, find the best fit line
# how to find best fit line, via the least square error
# how to solve:
# 1. hill climbing, y=mx+b, try different values of m and b
# 2. can we use calculus? yes
# 3. can we use random search? pick random values of m and b
# 4. should we ask a phsicist
#
# f(x) = c (constant)
# E(c) = sum_{i=1}^{n} (y_i-c)^2
# use calculus to find the minimum:
# dE(c)/dc = sum_{i=1}^{n} 2(y_i-c)(-1) loss function
# -sum_{i=1}^{n} 2(y_i-c) = 0
# sum_{i=1}^{n} y_i - sum_{i=1}^{n} c = 0
# nc = sum_{i=1}^{n} y_i
# c = sum_{i=1}^{n} y_i / n

# lesson 5, order of polynomial
# k=0, constant
# k=1, line
# k=2, parabola
# f(x) = c0 + c1x + c2x^2
# order of polynomial cannot exceed the #datapoints
#
# plot training error vs. order of polynomil
 
# lesson 6, pick the degree
# use order 3 because it looks better

# lesson 7, polynomial regression
# x|y, c0+c1x+c2x^2+c3x^3 = y
#
# [1 x1 x1^2 x1^3] [c0] = [y1]
# [1 x2 x2^2 x2^3] [c1] = [y2]
# [1 x3 x3^2 x3^3] [c2] = [y3]
# [1 x4 x4^2 x4^3] [c3] = [y4]
# [...           ]        [  ]
# [1 xn xn^2 xn^3]        [yn]
#
# Xw ~= Y, solve using least square:
# X^T Xw ~= X^T Y
# X^T Xw ~= X^T Y
# (X^TX)^(-1) X^TXw ~= (X^TX)^(-1) X^TY 
# x = (X^TX)^(-1)X^TY this is how you compute the weight

# lesson 8, error
# training data has errors in it, no modelling f but modelling f+e, where do errors
# come from?
# sensor error
# miliciously - being given bad error
# transcription error
# unmodelled influences

# lesson 9, cross validation
# training set and test set
# we want to generalize to the real world
# we want the data to be indendent, and identically distributed, this is a 
# fundamental assumption.

# lesson 10, cross validation
# we want a model that is complex enough to fit the data without causing problems
# on the test set.
#
# Take some of the training set data, and use it as cross validation set.
# use 4 folds 1 2 3 4
# train on 1 2 3, test on 4
# train on 2 3 4, test on 1
# train on 3 4 1, test on 2
# train on 4 1 2, test on 3
#
# housing example revisited: 
# training error improves
# cross validation error falls then rises
# 
# underfit, fit, overfit, you want to be in the goldilocks zone

# 11 other inputs
# other input spaces, 
# -> scalar input, continuous, x
# -> vector input, continuous, x_bararrow
# include more input features, 
# size, distance from zoo, hyperplanes
# one dimensional input, line
# 2 dimension input, plane
#
# predict credit score:
# do they have a job? {0,1}
# age? 
# assets
# haircolor, red, beige, brown, blonde, black, blue
# RGB, enumerate

# 12 conclusion
# what did we learn:
# historical facts
# model selection and under/overfitting
# cross validation
# linear, polynomial regression
# best constant in terms of squared error: mean
# representation for regression