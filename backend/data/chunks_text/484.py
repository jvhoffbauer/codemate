- This test case uses `unittest.mock.patch` to replace the built-in print function and capture its output using a custom testing print function provided by SQLModel's `get_testing_print_function`.
- The `test_tutorial` function imports the module containing the tutorial example (`docs_src.tutorial.where`) and sets up necessary variables such as the database URL and engine.
- It then creates an empty list called `calls` to store captured printing statements during execution of the tutorial example.
- Inside the context manager created by `with patch`, the main function of the tutorial is executed while capturing all printed statements through the custom testing print function.
- After executing the tutorial, the test checks if each expected statement appears in the `calls` list, removes it from the list, and finally ensures that there are no remaining unexpected statements left in the list.