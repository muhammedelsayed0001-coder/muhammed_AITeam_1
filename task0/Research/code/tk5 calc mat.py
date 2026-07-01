
def create_matrix (rows,columns):
    matrix_1 = []  #main matrix

    for num in range(rows) :    
        sec_matrix=[]  # "secandry matrix" saving result
        for num2 in range(columns) :
            add =int(input(f"Enter value at ({num},{num2}): ")) #show the num of the (row,colm)
            sec_matrix.append(add) 
    return matrix_1 

rows = int(input("enter rows :"))
columns = int(input("enter column :"))


matrix_1=create_matrix(rows,columns)
print ("Your matrix:")
for row in matrix_1:     
    print(row)              # to have the normal look of matrix as in math  

matrix_2=create_matrix(rows,columns)
print ("2nd Your matrix :")
for row in matrix_2:
    print(row)

#creating the sum mechanism 

def matsum(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    result = []
    
    
    for i in range(rows): 
        row = []
        for j in range(cols):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
    return result    

result = matsum(matrix_1, matrix_2)
print("Sum result:\n")
for row in result:
    print(row)
    
# sublimation mechanism

def matsub(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    result = []
    for i in range(rows): 
        row = []
        for j in range(cols):
            row.append(arr1[i][j] - arr2[i][j])
        result.append(row)
    return result    

result = matsub(matrix_1, matrix_2)
print("Sub result:\n")
for row in result:
    print(row)


# Multiplication mechanism
# matA = n*m then matB = m*z
# M =[1st row ]*[1st col] -> (1,1)*(1*1)+(1,2)*(2*1) --> put the value in new [matrix] & 
# contuine the process untill u reatch the last place in the matrix
#   [ 1 , 2 ]  [ 1 , 2 ]      [ (1*1)+(2*3) , (1*2)+(2*4) ]    [ 7 , 10  ] 
#   [ 3 , 4 ]  [ 3 , 4 ]  =   [ (3*1)+(4*3) , (3*2)+(4*4) ] =  [ 15 , 22 ]
  

def mat_mult(arr1, arr2):
    rows_1 = len(arr1)
    cols_1 = len(arr1[0])
    rows_2 = len(arr2)      
    cols_2 = len(arr2[0])
    result = []
    
    if cols_1 != rows_2 :
        print ("math error ")

    for i in range(rows_1):
        rslt1=[]            
        for j in range(cols_2):  
           m=0
           for k in range(cols_1):
                m += arr1[i][k] * arr2[k][j]  # [i][k] * [k][j]  [k] * [k] عشان القانون 
           rslt1.append(m)                    # Mat1 * Mat2 = n*m m*y  
        result.append(rslt1)        
    
    return result


result = mat_mult(matrix_1, matrix_2)
print("Multiplication result: \n")
for row in result:
    print(row)




# Scalar multiplication mechanism

def matscl_mult(scalar, arr1):
   
    rws = len(arr1)
    cols = len(arr1[0])
    result_sc = []

    for row in arr1:
        nw_rslt1=[]
        for num in range(cols):       
            nw_rslt1.append( scalar * rws[cols])
        result_sc.append(nw_rslt1)
    return result_sc 

scalar = int(input("enter scalar : \n"))

result_sc = matscl_mult(scalar, matrix_1)        

print("Scalar multiplication result_sc: \n")
for rws in result_sc:
    print(rws)


    

# Scalar sum & sub mechanism

def scalarsum(scalar, arr1):
    rws = len(arr1)
    cols = len(arr1[0])
    result_sca = []
    
    for NUM1 in range(rws): 
        row_result = []
        for NUM2 in range(cols):
            row_result.append(scalar + arr1[NUM1][NUM2])
        result.append(row_result)
    return result_sca    

scalar = int(input("enter scalar : \n"))  
result_sca = matsum(scalar, matrix_1)
print("Sum result:\n")
for row_result in result_sca:
    print(row_result)




# Scalar sub mechanism 

def scalarsub(scalar, arr1):
    rws1 = len(arr1)
    cols1 = len(arr1[0])
    result_sub = []
      
    for NUM1 in range(rws1): 
        row_result = []
        for NUM2 in range(cols1):
            row_result.append(arr1[NUM1][NUM2] - scalar )
        result_sub.append(row_result)
    return result_sub  
  
scalar = int(input("enter scalar : \n")) 
result_sub = scalarsub(scalar, matrix_1)
print("Scalar sub:\n")
for row_result in result_sub:
    print(row_result)    



# Normalization
    
def matnorm(arr):
    rows = len(arr)
    cols = len(arr[0])

    min_val = arr[0][0]
    max_val = arr[0][0]
    result = []
        
    for i in range(rows): 
        for j in range(cols):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
            if arr[i][j] > max_val:
                max_val = arr[i][j]

# Normalization :
#  x = ( every number from dataset - min ) / ( max num - min num)

    for i in range(rows): 
        row = []
        for j in range(cols):
            row.append( (arr[i][j] - min_val) / (max_val - min_val) )
        result.append(row)
    return result    

result = matnorm(matrix_1)
print("Normalization = :\n")
for row in result:
    print(row)
     



