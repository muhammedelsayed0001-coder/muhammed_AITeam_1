'''

NumPy is built on C, which is way faster for 
processing heavy data. Instead of looping through
every single item one by one .


NumPy uses vectorized
operations to handle the entire dataset at once. When
you're doing serious "number crunching" with millions of samples,
standard Python lists just can't keep up with that kind of scale


---------------------------------------------------------------------


Multicollinearity in the Normal Equation

The Problem :
The Normal Equation has 
(XᵀX)⁻¹ in it meaning we must invert a matrix. 
When two features are highly correlated (or duplicates), 
this matrix can't be inverted. No inverse = no solution.

Why?
Think of it this way: if feature B = 2 × feature A
the model has infinite ways to split the weight between them and get the same answer.
Math can't pick one it breaks.
The Fix: Ridge Regression

θ^= (XᵀX +λI )⁻¹ Xᵀy  

We just add a small number (λ) to the diagonal of the matrix before inverting.
This is enough to make it invertible again.

Think of it like adding a tiny unique fingerprint to each feature  
now the matrix is no longer "confused" and can be inverted cleanly.

No features removed  
Unique solution guaranteed
Tiny bias introduced  worth the tradeoff


'''