- This method is a private (underscore prefixed) class method of SQLModel, which calculates keys to be included or excluded from serialization based on user input and settings. - It takes several optional arguments for customizing key selection behavior, including `include`, `exclude`, `exclude_unset`, and `update`. - The method returns an abstract set (i.e., unordered collection without duplicates) of selected keys as output.