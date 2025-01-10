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
              [2, 3, 4, 5, 6],
              [3, 4, 2, 1, 5],
              [4, 2, 1, 5, 3],
              [7, 6, 5, 3, 4]])

B =np.array([[3, 1, 2, 5, 4],
              [6, 2, 1, 3, 4],
              [1, 5, 7, 6, 4],
              [2, 5, 6, 4, 3],
              [3, 7, 5, 2, 1]])

   
#Implement the formula MX + B
#Have two function one using numpy and another not using numpy
#Return 
@app.post("/calculate")
async def f(request: Request):
    body = await request.json()

    matrix = body.get("matrix")

    if not matrix or len(matrix) != 5 or any(len(row) != 5 for row in matrix):
        return {"error": "Matrix must be 5x5"}


    X = np.array(matrix)

    print(X)

    # Calculate using numpy
    numpy_result = with_numpy(M, X, B)
    
    # Calculate without numpy
    non_numpy_result = without_numpy(M, B, X)

    # Apply sigmoid function
    sigmoid_result = sigmoid(numpy_result)

    return {
        "matrix_multiplication": numpy_result.tolist(),
        "non_numpy_multiplication": non_numpy_result,
        "sigmoid_output": sigmoid_result.tolist()
    }
