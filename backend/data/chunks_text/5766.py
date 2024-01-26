- Retrieves a list of column operations to display links to related pages on an admin page
- Loops through each link model form and retrieves its corresponding form item using `get_form_item()` method
- Adds a new column operation with the label from the linked page's schema, a fixed width, and breaks at any screen size (using "*" as the breakpoint value). The button for this column is set to the previously obtained form item.