import math
from scipy.stats import norm

# defining the variables
S = 42 # Underlying Price
K = 40 # Strike Price
T = 0.5# Time til expiration
r = 0.1 # risk free Rate
vol = 0.2# Volatility (Standard Deviation of Option Prices)

# Formula for d1
d1 = (math.log(S/K) + (r + 0.5 * vol**2)*T) / (vol * math.sqrt(T))

# Formula for d2
d2 = d1 - (vol * math.sqrt(T))

# Calculate Call Option Price
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Calculate Put Option Price
P = K * math.exp(- r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Printing results:
print('The value of d1 is: ', round(d1,4))
print('The value of d2 is: ', round(d2,4))
print('The value of call option is: $', round(C,4))
print('The value of put option is: $', round(P,4))