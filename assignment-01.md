

# CMPS 2200 Assignment 1

**Name:**Austin Nguyen


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, because $2^{n+1} \equiv 2^{n} * 2$, and since this is simply multiplying by a constant, it is in $O(2^n)$.
.  

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  It is not in $O(2^n)$, because if you take the limit as n approaches infinity, it is a magnitude bigger than $O(2^n)$.
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, because when you take the limit as n approaches infinity and use L'Hopitals Rule, when using n instead of n^{1.01}, the derivative is 1, while
.  the derivative of $\mathrm{log}^2 n$ is just a multiplication of a log divided by n, which implies that it will grow much slower than n. Since $n < n^{1.01}$,
.  it must conclude that $n^{1.01}$ is also not in $O(\mathrm{log}^2 n)$.
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, since from the previous problem we learned that $n$ would grow larger than $\mathrm{log}^2 n)$, then $n^{1.01}$ would also grow larger, and such asymptotically
.  dominate.
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, because when taking the limit, you notice that $\sqrt{n}$ grows larger, as the derivative of $\sqrt{n} = \frac{1}{2\sqrt{n}}$, which grows faster as
.  $\mathrm{log} n$ has a factor of n on the denominator.
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, since form the pervious problem we learned that $\sqrt{n}$ would grow faster.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

. This function first checks if x = 0 or 1, to which it will return 0. Then, it will recursively add x - 1 and x - 2 x times, to which the recursive function will 
. stop once x = 1 or 0. The function will then return the Fibonnaci numbers where x = the "index" of the sequence.
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work done by the implementation is $O(n)$.
.  The span done by the implementation is also $O(n)$.


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  Since the total number of operations stays the same, the work of the function is still $O(n)$.
.  However, since time it takes is cut since it will split the work into halves over and over again, the span is now $O(\mathrm{log}n)$.


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  Depending on the number of processesors, since the work is still $O(n)$, the work when parallelized is $O(n/p)$, with p being the amount of processors.
.  Similarly, depending on the amount of processors, the span will be reduced to $O(\frac{\mathrm{log}n}{\mathrm{log}p})$
