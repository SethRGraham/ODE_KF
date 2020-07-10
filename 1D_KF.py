import numpy as np
from scipy.integrate import odeint 

# Defining the dynamic model
def model(y,t):
    dydt = 3.4 + (-y ** 2.3)
    return dydt

# Let our initial position be at 3 meters.
y0 = int(input('Please enter in the initial condition: ' ));

# For the first 5 seconds, our multiple sensors will take 15 data position measurements. 
t = np.linspace(0,5,15)

# Now, we solve the differential equation. 
y = odeint(model,y0,t)


# Establishing position measurments, resulting motion, measurement uncertanty, 
# motion uncertanty, mean measurement estimate, and uncertainty.

position = y
motion = np.diff(y)
measurement_sigma = 4;
motion_sigma = 2;
mean_estimate = 3;
uncertainty = 1000;

# Defining update & predict functions for Kalman Filter. 
def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

# Iterating functions for number of measurements taken. 
for n in range(len(position)):
    [mean_estimate, uncertainty] = update(mean_estimate, uncertainty, position[n], measurement_sigma)
    print('update: ', [mean_estimate, uncertainty])
    
    [mu, sig] = predict(mean_estimate, uncertainty, motion[n], motion_sigma)
    print('predict: ', [mean_estimate, uncertainty])
