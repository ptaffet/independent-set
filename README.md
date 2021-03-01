# Maximal Independent Sets in a few Challenging Graphs

This repository contains results from challenge problems located at https://oeis.org/A265032/a265032.html. I used Gurobi version 9.1 to solve the simple ILP formulation.

In particular, this repository makes two small contributions:
* For `1dc.2048`, I show that the largest independent set indeed has size 172. Gurobi took about 350k seconds to prove this bound.
* For `1zc.1024`, I prove a bound of 116 on the size of a maximal independent set. The previous known bound was 117 and the best known feasible solution is of size 112. Gurobi took 1.4 million seconds to prove this bound.

For all computations, I used a `c2-standard-8` VM during a free trial of Google Cloud Platform.
