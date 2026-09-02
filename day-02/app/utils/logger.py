# Import Python's built-in logging module.
import logging

# Configure the default logging behavior for the application.
logging.basicConfig(
    # Show INFO, WARNING, ERROR, and CRITICAL messages by default.
    level=logging.INFO,
    # Define how each log message should appear in the terminal.
    format=(
        # Show the date and time of the log message.
        "%(asctime)s | "
        # Show the log level, such as INFO or ERROR.
        "%(levelname)s | "
        # Show the actual log message.
        "%(message)s"
    )
)

# Create a logger for the current module so other files can import and use it.
logger = logging.getLogger(__name__)