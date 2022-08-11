import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)  # Use force = True to enable force logging otherwise log file will not be created
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
