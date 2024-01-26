- Calculates normalized difference between bands 1 and 2 using NumPy where mask is False
- Converts arrays to float32 data type for better numerical stability during calculations
- Expands array dimensions to match ImageData format with a single channel
- Returns new ImageData object with calculated values as count, original mask, assets, CRS, and bounds