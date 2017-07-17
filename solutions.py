
# coding: utf-8
 
#Question 1, Anagram check
"""Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a 
boolean True or False.
"""

# return True if two input strings are equal when sorted

def is_anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    return s1 == s2



# search for some anagram of t in s

def find_anagram(s, t):
    
    if s and t:
        pattern_length = len(s)
        match_length = len(t)
        
        for i in range(pattern_length - match_length + 1):
            if is_anagram(s[i: i + match_length], t):
                return True        
    return False


# main
def question1(s, t):
    return find_anagram(s, t)
# testcases
# base testcase

pattern = "udacity"
match = "ad"
print question1(pattern, match)  # expect True

# Output : True 

# edge testcase-1

pattern = "udacity"

match = "???"
print question1(pattern, match)  # expect False

# Output : False 

# edge testcase-2

pattern = "udacity"
match = None
print question1(pattern, match)  # expect False

# Output : False 

 

#Question 2, 
"""Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string."""
def question2(a):
    if len(a)==0:
        return -1
    a = a.lower()
    def is_palindrome(a):   #returns T/F
        return str(a) == str(a)[::-1]    

    longest_palindrome = ""

    i = 0
    j = 1

    #new value can't be longest palindrome if len(string[i:j]) <= len(longest palindrome)

    while i < (len(a) - len(longest_palindrome)):
        #don't look beyond the possible indexes
        if j <= len(a):
            temp_string = a[i:j]
            #only worth checking if it is eligible to be the longest 
            if len(temp_string) > len(longest_palindrome):
                if is_palindrome(temp_string) == True:
                    longest_palindrome = temp_string
            j += 1

        #move forward one place, start over
        else:
            i += 1
            j = i+1
    return longest_palindrome


print question2("racecar")
# racecar
print question2("cumaaaquat")
# aaa
print question2("")
# -1

 
#Question 3,  


def question3(G):

    vertices = G.keys()

    p = {}   #parent node

    rank = {}

    for vertice in vertices:

        p[vertice] = vertice

        rank[vertice] = 0

    min_spanning_tree = []

    edges = []

    for node in vertices:

        edges.sort()

    for edge in edges:

        weight, vertice1, vertice2 = edge

        if find(vertice1) != find(vertice2):

            union(vertice1, vertice2)

            min_spanning_tree.add(edge)

    return min_spanning_tree





testgraph = {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}

print question3(testgraph)
"""
#Test Case 1
print question1("udacity","ad")
#output

#Test Case 2
print question1("udacity","") #edge case
#output

#Test Case 3
print question1("","ad") #edge case
"""
 
parent = {}

rank = {}



# initialize disjoint sets. each set contains one vertice. rank is used to keep the 

# tree MST flat as much as possible for faster search.

def make_set(vertice):

    parent[vertice] = vertice

    rank[vertice] = 0



# find the set to which this vertice belongs

def find(vertice):

    if parent[vertice] != vertice:

        parent[vertice] = find(parent[vertice])

    return parent[vertice]



# merge the sets represented by these two given root nodes

def union(vertice1, vertice2):

    root1 = find(vertice1)

    root2 = find(vertice2)

    if root1 != root2:

        if rank[root1] > rank[root2]:

            parent[root2] = root1

        else:

            parent[root1] = root2

            if rank[root1] == rank[root2]: rank[root2] += 1



# perform kruskal algorithm to find mst

def kruskal(vertices, edges):

    minimum_spanning_tree = set()

    for vertice in vertices:

        make_set(vertice)



    # sort edges by increasing weights

    edges = sorted(edges, key=lambda x : x[2])

    

    for edge in edges:

        vertice1, vertice2, wt = edge

        if find(vertice1) != find(vertice2):

            union(vertice1, vertice2)

            minimum_spanning_tree.add(edge)

            

    return minimum_spanning_tree



# main

def question3(G):

    

    graph = G

    vertices = []

    edges = []

    

    # pre process given input graph and extract all vertices and edges

    for vertice in graph.keys():

        # collect vertices

        vertices.append(vertice)

        # build edge tuples

        verticeEdges = graph[vertice]

        for verticeEdge in verticeEdges:

            fromNode = vertice

            toNode, weight = verticeEdge

            edges.append((fromNode, toNode, weight))

        

    # perform Kruskal algo

    ms_tree = kruskal(vertices, edges)

    

    # post process results into the required output format

    output = {}

    for node in ms_tree:

        fromNode, toNode, weight = node

        

        if toNode < fromNode:

            fromNode = node[1]

            toNode = node[0]

            

        if fromNode in output:

            output[fromNode].append((toNode, weight))

        else:

            output[fromNode] = [(toNode, weight)]

            

    return output



# testcases

print "\nAnswer 3:"

import pprint

pp = pprint.PrettyPrinter()



# base testcase

G = {'A': [('B', 1), ('C', 7)],

     'B': [('A', 1), ('C', 5), ('D', 3), ('E', 4)],

     'C': [('A', 7), ('B', 5), ('D', 6)],

     'D': [('B', 3), ('C', 6), ('E', 2)],

     'E': [('B', 4), ('D', 2)],

    }

print "Graph-1:"

pp.pprint(G)

answer = question3(G) # expect {'A': [('B', 1)], 'B': [('C', 5), ('D', 3)], 'D': [('E', 2)]}

print "Minimum Spanning Tree:", answer



# edge testcase-1

G = {'A': [('B', 1), ('C', 1)],

     'B': [('A', 1), ('C', 1)],

     'C': [('A', 1), ('B', 1)],

    }

print "Graph-2:"

pp.pprint(G)

answer = question3(G) # expect {'A': [('C', 1), ('B', 1)]}

print "Minimum Spanning Tree:", answer



# edge testcase-2

print "Graph-3:"

G = {}

pp.pprint(G)

answer = question3(G) # expect {}

print "Minimum Spanning Tree:", answer
 

#Question 4,  
"""Find the least common ancestor between two nodes on a binary search tree. """

def question4(T, r, n1, n2):
  
    n1_ps = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_ps.append(n1)
        
    if len(n1_ps) == 0:
        return -1
    
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_ps:
            return n2

    return -1 

def parent(T, n):
     #return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i

    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
# Output: 3
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,3,3)
# Output: -1
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,4,1)
# Output: 3

"""

#Test Case 1
print question1("udacity","ad")
#output

#Test Case 2
print question1("udacity","") #edge case
#output

#Test Case 3
print question1("","ad") #edge case
"""
 


#Question 5, LinkedList mth node from the last
"""Find the element in a singly linked list that's m elements from the end. """
# Node class 
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    i = ll
    j = ll
    #increment i m spaces forward from the start
    for val in range(m):
        if i is None:
            return None
        i = i.next
    #when i is none, j is the ith element from the end
    while i is not None:
        i = i.next
        j = j.next
    return j.data


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)
ll.next.next.next.next.next = Node(6)


#Test Case 1
print question5(ll, 3)
#Test Case 2
print question5(ll, 20) # edge case
#Test Case 3
print question5(None, 3) # edge case
 

 


