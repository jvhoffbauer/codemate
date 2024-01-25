def _multiply_by_two(data, mask):
    mask.fill(255)
    data = data * 2
    return data, mask