# Filtering a signal

## Problem:
Given a list of values from a file named `log.txt`, the values consist of a signal input that is quite erratic with different peaks and lows and one needs to apply different smoothening filters to "even out" the signal.
some filters are discussed below:

## input:
A file named `log.txt` containing signal values

## output:
A list that has been applied with a filter.

## Muchiko filter:

**Algorithm:** Simple Moving Average filter that slides a window across the data and calculates the average of values within each window.

**Example:** Data: [4, 5, 6, 7, 8], Window Size: 3

| Window | Values | Average | Output |
|--------|--------|---------|--------|
| 1st | (4, 5, 6) | (4+5+6)/3 = 5 | 5 |
| 2nd | (5, 6, 7) | (5+6+7)/3 = 6 | 6 |
| 3rd | (6, 7, 8) | (6+7+8)/3 = 7 | 7 |

**Final Output:** [5, 6, 7] (Smoothed Data)

**How it works:**
- Slide a window of fixed size across the input data
- Calculate the arithmetic mean of all values within the window
- Replace the center value with this mean
- Repeat until all data points are processed
- Eliminates outliers and reduces noise while preserving trends

## Suchino filter

**Algorithm:** Weighted Moving Average filter that applies different weights to values within the window, giving more importance to center values.

**Example:** Data: [4, 5, 6, 7, 8], Window Size: 3, Weights: [0.2, 0.6, 0.2]

| Window | Values | Weighted Sum | Output |
|--------|--------|--------------|--------|
| 1st | (4, 5, 6) | (4×0.2)+(5×0.6)+(6×0.2) = 5.2 | 5.2 |
| 2nd | (5, 6, 7) | (5×0.2)+(6×0.6)+(7×0.2) = 6.0 | 6.0 |
| 3rd | (6, 7, 8) | (6×0.2)+(7×0.6)+(8×0.2) = 7.0 | 7.0 |

**Final Output:** [5.2, 6.0, 7.0] (Weighted Smoothed Data)

**How it works:**
- Similar to Muchiko but assigns weights to each position in the window
- Center values get higher weights (0.6), edges get lower weights (0.2 each)
- Provides smoother transitions and better edge preservation
- More effective at removing noise while maintaining local variations

## hybrid approach (bonus)

**Algorithm:** Combines both Muchiko (Simple MA) and Suchino (Weighted MA) filters for enhanced smoothing.

**Process:**
1. Apply Muchiko filter (simple moving average) to get initial smoothed data
2. Apply Suchino filter (weighted moving average) on the result from step 1
3. Optionally blend results: Final = (α × Muchiko_result) + ((1-α) × Suchino_result), where α ∈ [0, 1]

**Benefits:**
- Combines the simplicity of Muchiko with the sophistication of Suchino
- Double-pass filtering removes more noise while preserving important signal features
- Better handling of sudden peaks or drops (outliers)
- More robust smoothing suitable for real-world noisy data

## Key Learning Takeaways:
- One can learn about different simple filtering methods with simple cleaning methods.
- Applications of "sliding window" concept used in applying the filter/smoothening purpose
- Gives an introductory base to more complex filtering methods in `pandas` library