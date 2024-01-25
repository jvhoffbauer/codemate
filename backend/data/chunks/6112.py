    def _wrap_form_item(self, formitem: FormItem) -> FormItem:
        """Wrap formitem, add image and file upload receiver."""
        if formitem.type == "input-image" and not getattr(formitem, "receiver", None):
            formitem.receiver = self.image_receiver
        elif formitem.type == "input-file" and not getattr(formitem, "receiver", None):
            formitem.receiver = self.file_receiver
        elif formitem.type == "input-rich-text":
            formitem.receiver = (
                getattr(formitem, "receiver", None) or self.image_receiver
            )
            formitem.videoReceiver = (
                getattr(formitem, "videoReceiver", None) or self.file_receiver
            )
        if formitem.type in {"input-image", "input-file"}:
            # Add manual input file link component.
            formitem = amis.Group(
                name=formitem.name,
                body=[
                    formitem,
                    formitem.copy(
                        exclude={"maxLength", "receiver"},
                        update={"type": "input-text"},
                    ),
                ],
            )
        return formitem