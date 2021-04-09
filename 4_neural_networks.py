# lesson 1: neural networks
# cell body, neuron, axon, synapse
# spike trains travel down the axon, and causes excitation to occur at other axons.
# a computation unit.
# 
# x1 -> w1 ->
# x2 -> w2 -> theta -> y 
# x3 -> w3 ->
#
# sum_{=1}^{k} xi*wi,    activation
# >=theta, firing threshold
# 
# For perceptron, yes: y=1
#                 no:  y=0
#

# lesson 2, ANN
# x1   1     w1  0.5   theta=0, y=0
# x2   0     w2  0.6
# x3  -1.5   w3  1

# lesson 3, how powerful is a perceptron? and
# y = 0,1
# w1 = 1/2
# w2 = 1/2
# theta = 3/4
#
# if x1=0, x2*1/2=3/4, x2=3/2
# if x2=0, x1*1/2=3/4, x1=3/2
#
# r = return 0, g = return 1
# 
# 1    g   g    g    g    g
# 0.75 rg  g    g    g    g
# 0.5  r   rg   g    g    g
# 0.25 r   r    rg   g    g
# 0    r   r    r    rg   g 
#      0   0.25 0.5  0.75 1

# lesson 4, how powerful is a perceptron 4?
# if we focus on x1 E {0,1}, x2 E {0,1}
# what is y? y is and

# lesson 5, how powerful is a perceptron 5?
# w1 = 0.5
# w2 = 0.5
# theta = 1/4
#
# if we focus on x1 E {0,1}, x2 E {0,1}
# what is y? y is or
#
# 
# 1    g   g    g    g    g
# 0.75 g   g    g    g    g
# 0.5  g   g    g    g    g
# 0.25 rg  g    g    g    g
# 0    r   rg   g    g    g 
#      0   0.25 0.5  0.75 1

# lesson 6, how powerful is a perceptron? not
# x1=1, y=0
# x1=0, y=1
# w1=-0.5, theta=0
#
#    G R  
# -1 0 1 2
#
# and or not are all expressible as perceptron units 

# lesson 7, xor function
# theta = 0.5
# x1->      -> 0.5 ->
#      and  -> -1  -> or -> y
# x2->      -> 0.5 ->
#
# x1 x2 and  or xor=or-and
# 0   0   0   0   0
# 0   1   0   1   1
# 1   0   0   1   1
# 1   1   1   1   0

# lesson 8, perceptron training
# perceptron rule -> single unit
# wi = wi + delta wi
# delta wi = nu(yi- yi^hat)xi
# yi^hat = (sum_i wi yi >= 0)
#
# y: target
# y_hat: output
# nu: learning rate
# x: input
#
# repeat x,y
#  bias  x    y (0/1)
#      | xxxx y
#      | xxxx y
#      | xxxx y
#      | xxxx y
#      | xxxx y
#      | xxxx y
#      | xxxx y
#      | xxxx y
#  theta w
#
# y y_hat y-y_hat
# 0 0     0
# 0 1     -1
# 1 0     1
# 1 1     0
#
# 2D training set, learn a half plane
# if the half plane is linearly separable, then perceptron rule will find it in
# finite number of iterations.
#
# if the data is not linearly seperable, see if it ever stops, 
# problem, this algorithm never stops, 
# so run while there are some errors, if you solve the halting problem then you 
# can solve the halting problem.

# lesson 9, gradient descent
# need something that can work for linearly non-separability.
# 
# a = sum_i x_i w_i
# y^hat = {a>=0}
# E(w) = 1/2 sum_{(x,y) E D} (y-a)^2
# d E(w) / d w_i = d/dw_i 1/2 sum_{(x,y) E D} (y-a)^2
#                = sum_{(x,y) E D} (y-a) d/dw_i -sum_i x_i w_i'
#                = sum_{(x,y) E D} (y-a)(-x_i) <- looks a lot like the perceptron rule

# lesson 10, comparison of learning rules
# delta w_i = nu (y-y^hat) x_i, perceptron: guarantee of finite convergence, in the case of linearly separable
# delta w_i = nu (y-a) x_i,     gradient descent: calculus, robust, converge to local optimum
# activation, vs activation and thresholding it

# lesson 11, comparison of learning rules
# quiz: why not do gradient descent on y^hat
# intractable, no
# non differentiable, yes
# grows too fast, no
# multiple answers, no

# lesson 12, sigmoid
# sigma(a) = 1 / (1+e^(-a))
# as a -> -infinity, sigma(a)->0
# as a -> +infinity, sigma(a)->1
# D sigma(a) = sigma(a) (1-sigma(a))

# lesson 13, neural network sketch
# input, hidden layers, hidden layers, output
#
# whole thing is differentiable, 
#
# back propogation, computationally beneficial organization of the chain rule
# we are just computing the derivatives with respect to the different weights
# in the network, all in one convenient way, that has, this lovely interpretation 
# of having information flowing from the inputs to the outputs. And then error
# information flowing back from the outputs towards the inputs, and that tells you
# how to compute all the derivatives. And then, therefore how to make all the weight
# updates to make the network produce something more like what you want it to 
# produce. so this is where the learning is actually taking place.
# 
# the error function can have many local minimums, or local optima, stuck

# lesson 14, optimizing weights
# -> gradient descent
# -> advanced optimization methods, optimization and learning are the same according to people
#
# momentum terms in the gradient, in gradient descent, continue in direction, 
# higher order derivatives, combinations of weights hamiltonia, and what not
# randmized optimization
# penalty for complexity
# philosophy based optimization, has this been tried?
#
# add more nodes, 
# add more layers, 
# higher weights
# these parameters make the network more complex
# make it as simple as possible.

# lesson 15, restrition bias
# restriction bias tells you the representational power, i.e. what you are able to represent
# set of hypotheses we will consider
# perceptron units are linear
# half spaces
# sigmoids
# complex
# much more complex, not as much 
# Boolean: network of threshold-like units
# continuous function: connected, no jumps, hidden
# arbitrary: stitched together
#
# dangers of overfitting: cross validation
# error - iterations
# cross validation error can increase again, so if it works, then just stop 

# lesson 16, preference bias
# preference bias tells you, given two representations, why I would prefer one
# over the other.
# prefer correct tree, prefer shorter tree
# how do we start weights:
# small, random values, for weights, avoid local minima, variability, 
# large weights leads to overfitting, 
# small random values, simple explaination, 
# neural networks implement simpler explaination, occam's razor
# don't make something more complex unnecessarily
# better generalization

# lesson 17, summary
# perceptron, linear threshold unit, can create boolean function
# perceptron rule - finite time for linearly separable
# general differentiable - backprop and gradient descent
# preference/restriction bias of neural networks