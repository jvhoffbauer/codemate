- Takes a `HousePredictionPayload` object as input and returns a pre-processed numpy array with shape (1, n), where `n` is the number of features in the payload.
- Converts the payload to a list using `payload_to_list()`, which may involve additional processing or transformation depending on the format of the payload.
- Reshapes the resulting list into a single row numpy array for feeding it into the machine learning model during prediction.