<!-- @format -->

# Nodal Analysis

## Resistances

In a circuit made up of just resistances, calculating the nodal volatges becomes quite easy using KVL and KCL.\
The mathematics behind this follows

$$
\left[G\right]v = I
$$

where the matrix G is called conductivity matrix
If $G = \left[g_{ij}\right]$,\
$\left[g_{ij}\right] = -\left(\sum{R_{ij}^{-1}}\right) \text{ when } i \neq j$\
where $R_{ij}$ is the resistance connected between node 1 and 2.\
when $i = j$,\
$\left[g_{ii}\right] = -\left(\sum{R_{i}^{-1}}\right)$\
where $R_i$ is a resistance with one node as $i$\
The vector $I$ is just a vector of input currents. Currents arriving at a branch are treated as positive, other wise negative
