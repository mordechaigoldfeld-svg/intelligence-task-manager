import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s",
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler("./logs/app.log",encoding="utf-8")])


logger=logging.getLogger()




logger.info("test login")


