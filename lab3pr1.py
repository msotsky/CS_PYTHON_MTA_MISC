def multiply(x, y):
    if y == 0 or x == 0:
        return 0
    elif y == 1:
        return x
    elif x == 1:
        return y
    else:
        return x + multiply(x, y - 1)


        
#Write a recursive function called dot() that takes two lists L and K as input and returns their dot product. If the two lists are not of equal length, then 0.0 should be returned. The dot() function should also return 0.0 when both lists are empty. You can assume that the two input lists contain only numeric values. 
 
#Recall the dot product definition: The dot product of two vectors or lists is the sum of the products of the elements at the same index in each of the two vectors. For example, if we have 𝐿 = [5,3] and 𝐾 = [6,4] then the dot product of 𝐿 and 𝐾 is 42.0, which comes from 5∗6 + 3∗4. (Note that this result is the floating point value 42.0, because we are defining the base case as 0.0) 
 
#Unlike the mult() function, you are not restricted from using the regular multiplication operator in your solution.

def dot(K, L):
    if len(K) != len(L) or len(L) == 0 and len(K)== 0:
        return 0.0
    else:
        return (L[0] * K[-1]) + (L[-1] * K[0])
