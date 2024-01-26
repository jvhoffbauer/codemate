- This function takes an `item_id` as input and returns a dictionary containing the corresponding item from the `items` dictionary. - If the `item_id` is not present in the `items` dictionary, it raises a customized HTTP exception with a specific status code (404), message ("Item not found"), and additional header ("X-Error").