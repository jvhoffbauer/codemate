    def __init__(
        self, nlp: Language, input_id_col: str = "id", input_text_col: str = "text"
    ):
        """Initialize the SpacyExtractor pipeline.

        nlp (spacy.language.Language): pre-loaded spacy language model
        input_text_col (str): property on each document to run the model on
        input_id_col (str): property on each document to correlate with request

        RETURNS (EntityRecognizer): The newly constructed object.
        """
        self.nlp = nlp
        self.input_id_col = input_id_col
        self.input_text_col = input_text_col