from fastapi import FastAPI, Request
import uvicorn 
import numpy as np
import random

app = FastAPI()

# use the post decorator directly below this
'''
    Initialize M and B as np arrays
'''
M = np.array([[1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5]])

B =np.array([[1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5]])

   
