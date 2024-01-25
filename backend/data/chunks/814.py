    def extract_entities(self, records: List[Dict[str, str]]):
        """Apply the pre-trained model to a batch of records

        records (list): The list of "document" dictionaries each with an
            `id` and `text` property

        RETURNS (list): List of responses containing the id of
            the correlating document and a list of entities.
        """
        ids = (doc[self.input_id_col] for doc in records)
        texts = (doc[self.input_text_col] for doc in records)

        res = []

        for doc_id, spacy_doc in zip(ids, self.nlp.pipe(texts)):
            entities = {}
            for ent in spacy_doc.ents:
                ent_id = ent.kb_id
                if not ent_id:
                    ent_id = ent.ent_id
                if not ent_id:
                    ent_id = self._name_to_id(ent.text)

                if ent_id not in entities:
                    if ent.text.lower() == ent.text:
                        ent_name = ent.text.capitalize()
                    else:
                        ent_name = ent.text
                    entities[ent_id] = {
                        "name": ent_name,
                        "label": ent.label_,
                        "matches": [],
                    }
                entities[ent_id]["matches"].append(
                    {"start": ent.start_char, "end": ent.end_char, "text": ent.text}
                )

            res.append({"id": doc_id, "entities": list(entities.values())})
        return res