import numpy as np

x = np.array (
    [50, 60, 80, 100, 120] 
)
# row = 1 & colum = 5 


y = np.array (
    [150, 180, 240, 300, 330]
)
#column vector
x=x.reshape(-1,1)
print(x)

#column of ones       
x_1 = np.hstack([np.ones((x.shape[0] , 1 )),x])
print (x_1)  

#  θ = (Xᵀ X)⁻¹ Xᵀ y   --> equation to mathmaticlly Predicte value of a house proportionally with the
#                                                     area of the house  

# #note @ for mulit for matrix and * form element ?


Xt = x_1 . T    # 2*5

XTX=  Xt @ x_1  # 2*5 @ 5*2 = 2*2

XTX_inverse = np.linalg.inv (XTX) # --> 2*2

XTY = Xt @ y  # 2*5 @ (5,)

theta = XTX_inverse @ XTY  # 2*2 @ 2, = (2,)


# y = (θ₁*x ) + θ₀     θ₀ -> inter of the y 
#                      θ₁ -> slope                    

#  Predictions of a new house  = θ (const) * area of the house 
 
# Predictions

new_house    = np.array([1, 90])   # bias=1, size=90
price_90m     = new_house @ theta
print(f"\nPredicted price for 90 m² house: {price_90m:.2f} thousand") 