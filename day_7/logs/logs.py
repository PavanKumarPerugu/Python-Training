import logging

# Basic config
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Writing logs
logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
