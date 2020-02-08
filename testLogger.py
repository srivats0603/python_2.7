import logging
import json_log_formatter
import sys
import os

def runLogging(**logging_info):
    for item in logging_info:
        if item == 'log_dir':
            log_dir = logging_info[item]
            print "logging in directory", logging_info[item]
        if item == 'log_level':
            print "with current logging level", logging_info[item]
    logFileName = os.path.join(log_dir,'my-log.json')
    testFormatStr = '%(message)%(levelname)%(name)%(asctime)'
    testFormatter = json_log_formatter.JSONFormatter(testFormatStr)
    testJSONhandler = logging.FileHandler(filename=logFileName)
    testJSONhandler.setFormatter(testFormatter)
    testLogger = logging.getLogger('my_json')
    testLogger.addHandler(testJSONhandler)
    testLogger.setLevel(logging.INFO)
    testLogger.info('test Info Message')
    testLogger.error('test Error Message')
    return


if __name__ == '__main__':


    start_message = sys.argv[1]
    do_logging = str(sys.argv[2]).upper()
    if do_logging == 'TRUE':
        if len(sys.argv) < 5:
            print "enter the logger directory and level"
            exit()
        else:
             logDir = sys.argv[3]
             logLevel = sys.argv[4]
             runLogging(log_dir=logDir,log_level=logLevel)
    
