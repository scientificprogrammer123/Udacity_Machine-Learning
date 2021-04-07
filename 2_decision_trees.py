# lesson 2. supervised learning, classification or regression quiz:
# input,          output,                   C or R?
# credit history, lend money?               C (binary)
# picture,        high school/college/grad, C (trinary)
# picture,        age,                      C or R (ages can be fractional)

# lesson 3. classification learning
# instances (inputs), picture, salary
# concepts FUNCTION, maps input to output, an idea that describes a set of things
#                    it is also a mapping between objects in the world and membership
#                    in a set, which makes it a function
# target concept, answer
# hypothesis class, set of all classification functions you are willing to entertain
# sample, training set, set of (inputs, correctly labelled output pair)
# candidate, concept =?= target concept
# testing set, looks like training set, training set and testing set should not 
#              be the same
# You have to do generalization, generalization is the whole point of machine learning.

# lesson 6. example 1, dating
# eatery - type: italian, french, thai
# atmosphere - fancy, hole in wall, casual
# occupied?
# hot date?
# cost, $$, ##
# hungry?
# weather?
# A decision tree is a representation, then you can build an algorithm using it.
#            hungry?
#
#       rainy?     type of restaurant?
#
#           TRUE_OUTPUT

# lesson 8, representation quiz
# occupied | type  | rainy | hungry | hot date | happiness | class |
# T        | pizza | T     | T      | T        | T         |  nogo |
# F        | thai  | T     | T      | T        | F         |  nogo |
# T        | thai  | T     | T      | T        | F         |  go   |
# F        | other | F     | T      | T        | F         |  nogo |
# T        | other | F     | T      | T        | T         |  go   |
#
#              occupied?
#            f|        \t
#           nogo      type?
#               pizza|  thai\  other\
#                  nogo     go    happiness?
#                                f|        \t
#                               nogo       go
#
# The way decision trees work is that you have to start from the top of the tree
# There are 3 candidate concepts: occupied, type, happiness

# lesson 9, 20 questions
# -animal? yes
# -person? yes
# -famous? yes
# -we know personally? no
# -living person? no
# -music? yes
# -20th century? no
# -rap? no
# -singer? yes
# -female? no
# -recent death? yes
# -name? Michael?
# -Michael Jackson? yes
# 13 questions in order, narrow down in space, narrow down sequence, further narrow
# down possibilities.

# lesson 10, decision trees: learning
# 1. pick best attribute, best = splitting things roughly in half
# 2. asked question
# 3. follow the path
# 4. go to 1., until got an answer

# lesson 11, best attribute quiz
# the best attribute split gives you the most order in the system

# lesson 12, decision tree expressiveness
# A and B
#       A
#    T|   F\
#     B    -
#  T|  \F
#  +   -
#
#       B
#    T|   F\
#     A    -
#  T|  \F  
#  +   -

# lesson 13, decision tree expressiveness
# A or B
#      B
#   T|   \F
#   +    A
#     T|   \F
#     +    -
#
#      A
#   T|   \F
#   +    B
#     T|   \F
#     +    -

# lesson 14, decision tree xor
# A xor B
#        A
#    T|    \F
#     B    B
#   T|\F T|\F
#   - +  + -
# full truth table 

# lesson 15, decision tree n-or
#            A1
#           T|\F
#           T A2
#            T|\F
#            T A3
#             T|\F
#             T A4
#               ...
#                AN
#               T|\F
#               T  F
# linear order n, any parity
# 
# decision tree n-xor, 2^N-1 nodes, O(2^N)

# lesson 16, decision trees 
# -> xor is hard
# -> n attributes (Boolean) O(N!)
# how many trees
# output is Boolean
# 
# truth table
# A1 A2 A3 ... AN output
# T  T  T      T  
# T  T  T      F
# F  T  T      T
# there are 2^N rows    

# lesson 17, decision tree expressiveness
# how many ways to fill in the output, 2^(2^N)

# lesson 18, ID3
# loop:
#  *A <- best attribute
#  *Assign A as decision attribute for node
#  *For each value of A, create a descendent of node
#  *Sort training example to leaves
#  *If examples perfectly classified, stop
#  *Else iterate over leaves
#
# best attribute is defined as:
# Gain(S,A) = Entropy(s) - sum_v |S_v|/|S| Entropy(S_v)
#
# Information gain is the reduction in randomness, over the labels that you have
# with the set of data, based upon knowing the value of a particular attribute.
# So the formula's simply this, the information gain over S and A, where S is the 
# collection of training examples that you are looking at, and A is a particular 
# attribute, is simply defined as the entropy with respect to the labels, of the 
# set of training examples you have (S), minus sort of the expected or average
# entropy that you would have over each set of examples that you have with a 
# particular value.
#
# So we are picking an attribute, and that attribute could have a bunch of different
# values, like true/false, short/medium/tall, and that is represented by v.
#
# Entropy is a measure of randomness. For a coin, p(head)=0.5, no information gain, 
# so maximum entropy, or 1 bit of entropy. For a two headed coin, p(head)=1, so
# no information, no randomness, no entropy whatsoever, so zero bits of entropy.
#
# Look at the set of examples and set of labels you have, count the numbers that
# are coming up, red X and green O, if they are evenly split, then the entropy is
# maximal, no knowledge of whether more likely to get X or get O. OTOH, if all the 
# X's are together, then already knoow beforehand that you are going to get X. So
# if you have more of one label than the other, the amount of entropy goes down.
#
# The formula for entropy is:
#              - sum_v P(v) log P(v)
# This is a measure of information. This is a measure of randomness in some variable
# you haven't seen. It is the likelihood of you already knowing what you are going
# to get if you close your eyes and pick one of the training examples, versus you
# not knowing what you are going to get. 
#
# Goal is to maximize the entropy gain.           

# lesson 19, ID3 bias
# restriction bias, hypothesis set that you care about, H
# preference bias, h in H, which h do we prefer
#
# which hypotheses does ID3 prefer:
# good splits at the top, perfer hypothesis that is good at the top
# prefer correct vs incorrect
# prefer shorter trees to longer trees

# lesson 20, decision tree continuous at the top
# Continuous attributes, e.g. age, weight, distance

# lesson 21, other considerations
# Does it make sense to repeat an attribute along a path in the tree?
#      A
#     | \
#    B
#   |
#  A
# For continuous value atributes, it makes sense to ask a tree question again, 
# less than 20 or greater thank 30

# lesson 22, decision tree other considerations
# when do we stop? 
# when everything is classified correctly, 
# when there are no more attributes.
# no overfitting.

# lesson 23, regression
# splitting, variance, 

# lesson 24, what have we learned?
# 1. decision tree representation
# 2. top down algorithm for producing a decision tree, ID3
# 3. expressiveeness of decision trees
# 4. bias of ID3
# 5. best attributes (GAIN(s,a))
# 6. prune tree to avoid overfitting