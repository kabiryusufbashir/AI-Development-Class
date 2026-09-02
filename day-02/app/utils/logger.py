import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)

logger.info("Application started.")
logger.info("Loading Model")
logger.info("Mode Loaded Successfully")
logger.info("Prediction Completed Successfully")