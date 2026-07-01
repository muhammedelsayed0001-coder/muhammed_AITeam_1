# [ what , why , when ]  matrix Normalization 
 
'''
matrix Normalization is 

    changing the scale like when u exchance an currency from one to anther 
    for example from eg pound -> us dollar
    or changing btw diffrent system temp i.e. celsius to fahrenheit ... 

 -->    Normalization = X` = ( any number from dataset  - min ) / ( max num - min num)

 -------------------------------------------------------------------------------------------   
 
-->    Z-score normalization, also called standardization,      ---> {from text from geek4geek }
    transforms data so that it has a mean (average)
    of 0 and a standard deviation of 1. 
    This process adjusts 
    data values based on
    how far they deviate from the mean , measured in units of standard deviation.
    
    (Z) is the Z-score.
    (X) is the value of the data point.
    (μ) is the mean of the dataset.
    (σ) is the standard deviation of the dataset.
   
                                                        X` = ( X - μ ) / σ

-------------------------------------------------------------------------------------------
     
 -->  and there are diffrent methodes to Normalize data that are in diffrent shapes
      Row normalization (vector normalization) , Column normalization ,Frobenius norm normalization                                                                                                             
   

-------------------------------------------------------------------------------------------    


When we use it ? 

age = [20,60]
salary = [8000 , 25000] 
Since the values are on very different scales, we normalize them so the model treats all features fairly

Standardization 
Shifts data so it has mean 0 and standard deviation 1

-------------------------------------------------------------------------------------------

Why ?? 

make model learn faster     |       if we didn't use it may be make the model un accurate
notice the patterns         |       "hallucinate"  
more efftions               |

unbiased comparison



'''