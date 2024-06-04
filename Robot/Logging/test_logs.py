import inspect
import logging

class Test_Logs:
    @staticmethod
    def custom_logs(level=logging.DEBUG):
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        logger.setLevel(level)
        fh = logging.FileHandler("E:\\Robot\\Logging\\test_log.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

