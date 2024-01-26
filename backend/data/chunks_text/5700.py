- Defines a function `bind_model_admin` that takes two arguments `cls`, `pk_admin`, and an optional argument `insfield`.
- Checks whether the property of the instrumented attribute is a relationship property or not. If it's not, returns none.
- Retrieves the secondary table from the relationship property. If it's null, returns none.
- Iterates through all foreign keys of the secondary table to find the associated third-party table.
- Sets up the `admin` object with the help of site.get_model_admin().
- Stores the link model information in the `admin` object's dictionary called 'link_models'.
- Returns a form named `LinkModelForm` which contains the necessary parameters such as `pk_admin`, `display_admin`, `link_model`, `link_col`, and `item_col`.