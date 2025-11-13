import logging

def setup_logging(script_name):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the script
    handler = logging.FileHandler(f'C:\\Users\\SREEJA REDDY\\Downloads\\heart project\\logs\\{script_name}.log', mode='w',encoding='utf-8'   )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger