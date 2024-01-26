- `_range_check()` is a utility function that checks whether the given `datarange` value exceeds the maximum allowed range for three digits in base 256 (i.e., 8 bits). - The maximum allowed range is calculated as `maxrange = 256^3`. - If `datarange` is greater than this maximum, it indicates an overflow error and the function returns True; otherwise, False.