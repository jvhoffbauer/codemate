- This endpoint returns a `User` object with name "John" and surname "Doe". - The function annotates its return type as `User`, which is also used in the response schema (implicitly). - By returning the same model that's being used for request/response serialization, we can avoid having to define a separate DTO or transfer object.