import logging


class Log_Generator:

    @staticmethod
    def log_gen():
        # Create a file handler to store logs in a file
        file_handler = logging.FileHandler(".\\Log_Files\\About_Us_Page_Final.log", mode="w")
        file_handler.setLevel(logging.INFO)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Create a console handler to display logs on the console

        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        # console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)
        return logger

