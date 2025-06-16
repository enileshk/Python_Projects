import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations={}
    arr=np.array(list).reshape(3,3)
    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }

    for name, func in funcs.items():
        col_values = func(arr, axis=0).tolist()
        row_values = func(arr, axis=1).tolist()
        flat = float(func(arr))

        calculations[name] = [col_values, row_values, flat]

    return calculations

