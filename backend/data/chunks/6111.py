    def __init__(
        self,
        image_receiver: amis.API = None,
        file_receiver: amis.API = None,
    ):
        """
        Args:
            image_receiver: Image upload receiver, used to upload images to a specified location and return the image address
            file_receiver: File upload receiver, used to upload files to a specified location and return the file address
        """
        self.image_receiver = image_receiver
        self.file_receiver = file_receiver