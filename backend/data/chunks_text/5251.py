- Defines a function `RescalingParams()` that takes an optional list of strings as input called `rescale`.
- The function returns a list of tuples containing float values when `rescale` is not null.
- Each tuple represents the min and max values for rescaling a specific band's data. Multiple ranges can be provided by separating them with commas within each string element in `rescale`.