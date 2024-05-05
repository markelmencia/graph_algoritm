# graph_algoritms
Some algoritms related to Graph Theory.
\
\
Graph Theory is a very prevalent field in Computer Science and is used in several algoritms for a wide range of purposes. These are some graph algoritms I've learned in my Discrete Mathematics class, coded in Python.

## Graph Isomorphism Algoritm

This algoritm is used to determine whether two graphs are isomorphic or not. [Here's](https://en.wikipedia.org/wiki/Graph_isomorphism) the Wikipedia page about graph isomorphism. The algoritm needs the equivalent [adjacency matrixes](https://en.wikipedia.org/wiki/Adjacency_matrix) of two graphs. After checking that both graphs have the same vertex and edge amount, and that the degrees of every vertex in one graph are equivalent to the one's of the other, this algoritm will rearrange one of the two matrixes to then iterate through every possible permutation of the graph. If one of these permutations equals to the other graph, it means that those two graphs are isomorphic.
