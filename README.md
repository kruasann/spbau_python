# Projects

- [GUI application](#GUI)
- [Monte Carlo method](#Monte-Carlo)
- [Relations count](#Relations count)

## GUI
  The application allows you to create notes and saves them to files "<date>.txt" (you can choose it using a calendar in the app).
  
## Monte Carlo
  The method computes a definite integral. The Monte Carlo method consists in randomly choosing N points in the area of the function's graph (with xs from x1 to x2 and ys from y1 to y2). When the points are arranged, you need to calculate the number of points (M) that are located in the area bounded by the function. Theт the limit of (x2 - x1) * (y2 - y1) * (M / N) is the integral of the function from x1 to x2 as N approaches infinity.
  
## Relations count
  This problem was proposed to me in a Discrete mathematics course. The program generates all possible relations on sets of a given size and returns a distribution matrix of counted relations depending on their properties. There is an implementation using a relations generator class and a faster one using numba. You also can see Relations.jpg file that helps to understand the calculation result.
