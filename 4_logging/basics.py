# ----------------------------------------------------------------------------------------------------------------------
#   Basic logging

# logging is a built in library, no need to add dependency.
import logging as log

# Configure logger.
log.basicConfig(
    filename='test.log',                                # Specify log file. By default logging statements only write to stdout, and no files.
    level=log.INFO,                                     # Specify log level. Specified level and lower log levels will be logged.
    format='%(asctime)s:%(levelname)s:%(message)s')     # Specify log message format. See https://docs.python.org/3/library/logging.html#logrecord-attributes for format.

# To log, simply call one of those log functions.
log.debug("debug bla bla")
log.info("info bla bla")
log.warning("warning bla bla")
log.error("error bla bla")
log.critical("critical bla bla")

# ----------------------------------------------------------------------------------------------------------------------
#     Log levels
# Log levels are ordered - when setting logger to a specific level, everything on that level and lower levels will be logged, everything on higher levels won't be.

# DEBUG     Detailed information, typically of interest only when diagnosing problems.
# INFO      Confirmation that things are working as expected.
# WARNING   An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR     Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL  A serious error, indicating that the program itself may be unable to continue running.

# ----------------------------------------------------------------------------------------------------------------------
