What Hash Table Solve
---------------------
* We need to look up some data quickly
    * Some data that was slow to generate or obtain
    
In lieu of linear search...
It doesn't matter if _n_ is small.  O(n) vs O(1)
Any time-consuming process:
* Memoization (caching)
* Network caching
* Indexing
* Removing duplicates from lists
* Detecting duplicates
* Counting duplicates


Hash table loading
------------------
load_factor = number_of_items_in_the_table / number_of_slots_in_array
load_factor = 8/8 = 1.0
load_factor = 16/8 = 2.0
if load_factor > 0.7:   # More than 70% full
    rehash, doubling the size of the table
[stretch] if load_factor < 0.2 and the table size is greater than 8:  # Less than 20% full
    rehash, halving the size of the table
As you add and delete to and from the hash table:
    Keep track of the number of items in the hash table
Rehash:
    Make a new array 2x the size of the old one
    for index in range(len(array)):
        for each entry in the list at that index:
            Add it to the new array
    
0 |-> D
1 |-> H   0.5
2 |-> A
3 |-> C
4 |->
5 |->
6 |->
7 |->
0 |-> D
1 |-> H
2 |-> A
3 |-> C   1.0
4 |-> G
5 |-> B
6 |-> E
7 |-> F
0 |-> D -> M     2.0
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L -> N
4 |-> G
5 |-> B -> O
6 |-> E -> K -> P
7 |-> F
0 |-> D -> M -> Q
1 |-> H -> R -> X -> Y
2 |-> A -> I -> 0
3 |-> C -> J -> L -> N -> Z
4 |-> G -> S -> U
5 |-> B -> O -> 1 -> 2
6 |-> E -> K -> P -> W
7 |-> F -> T -> V
