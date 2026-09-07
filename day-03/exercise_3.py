import numpy as np

# This is the input vector.
# It contains 3 features, so its shape is (3,).
input_vector = np.array([2, 4, 6])

# This is the weight matrix.
# Its shape is (3, 2):
# - 3 rows because we have 3 input features
# - 2 columns because we want 2 output values
weights = np.array([
    [0.5, 0.2],
    [0.3, 0.8],
    [0.9, 0.4]
])

# This is the bias vector.
# It contains 2 values because the output will contain 2 values.
bias = np.array([1, 2])

# The @ symbol performs matrix multiplication.
# input_vector has shape (3,)
# weights has shape (3, 2)
# The result has shape (2,)
# Then NumPy adds the bias vector to the result.
output = input_vector @ weights + bias

print("Input vector:", input_vector)
print("Weights:")
print(weights)
print("Bias:", bias)
print("Output:", output)

print("Input shape:", input_vector.shape)
print("Weights shape:", weights.shape)
print("Bias shape:", bias.shape)
print("Output shape:", output.shape)

print("Explanation:")
print("The input has 3 features, so its shape is (3,).")
print("The weights have shape (3, 2), meaning 3 input features connect to 2 output values.")
print("The bias has shape (2,), so one bias value is added to each output.")
print("The final output has shape (2,), meaning the layer produces 2 output values.")
