# ----------------------------------------------------------------------------------------------------------------------
#     Log levels
# Setting logger to a specific level means only messages on that level and lower will be logged.
# Default logging level is WARNING. This means by default log.info() and log.debug() won't print anything.

# DEBUG     Detailed information, typically of interest only when diagnosing problems.
# INFO      Confirmation that things are working as expected.
# WARNING   An indication that something unexpected happened, or indicative of some problem in the near future
#           (e.g. ‘disk space low’). The software is still working as expected.
# ERROR     Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL  A serious error, indicating that the program itself may be unable to continue running.

# ----------------------------------------------------------------------------------------------------------------------
#   Basic logging

# logging is a built in library, no need to add dependency
import logging as log

# Configure logger - output file, log level, log format.
# By default (without configuring) logs are written to stdout only. By default logging level is WARNING (ignores info and debug).
log.basicConfig(
    filename='test.log',                                # Log file.
    level=log.INFO,                                     # Log level.
    format='%(asctime)s:%(levelname)s:%(message)s')     # Log message format.   See https://docs.python.org/3/library/logging.html#logrecord-attributes for format.

# Call one of those log functions to log on that level
log.debug("debug bla bla")
log.info("info bla bla")
log.warning("warning bla bla")
log.error("error bla bla")
log.critical("critical bla bla")


# ----------------------------------------------------------------------------------------------------------------------
#   Log to both file and stdout.

import logging as log
import sys

# A handler sends log messages to appropriate destination. A logger can have more than one handler.
# We need to provide a list of handlers - one for file, and one for stdout.
log.basicConfig(
    level=log.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[log.StreamHandler(sys.stdout), log.FileHandler("output.log")])



