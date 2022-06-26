import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 

 
# a = pd.DataFrame(np.array([[1,2],[3,4],[5,6],[7,8]]),columns=['x','y'],dtype=float)
 
# b = pd.DataFrame(np.array([[1,2]]),columns=['x','y'],dtype=float)
#不重置索引,上下拼接
# df = pd.concat([a,b],axis=0,join='inner',ignore_index=True)
#m,n = a.shape
#m0,n0 = b.shape
 
a = np.array([[1,2],[3,4],[5,6],[7,8]])
b = np.array([[1,2]])

from sklearn.metrics.pairwise import cosine_similarity
r = cosine_similarity(a,b)
print(r)

