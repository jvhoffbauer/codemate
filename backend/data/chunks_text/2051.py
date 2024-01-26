- Commands user to specify a programming language (default: none), which can be auto-completed using existing translations.
- If `INSIDERS_FILE` environment variable exists, uses MkDocs Insider's plugin instead of regular MkDocs.
- Checks whether specified language has an associated directory in 'docs'.
- Prints message indicating what language will be built.
- Creates a new directory for the selected language within the main documentation directory ('site').
- Removes any previous content from the newly created directory.
- Changes working directory to the selected language's directory.
- Runs MkDocs command to generate HTML files based on Markdown documents.
- Copies generated HTML files into the appropriate location within the main documentation directory.
- Returns control back to the parent shell with success message printed in green.