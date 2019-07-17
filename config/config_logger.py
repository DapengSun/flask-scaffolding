# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-17 18:11 
# file: config_logger.py
# ide: PyCharm

'''
logger配置
'''

# TimedRotatingFileHandler配置
# S: Seconds
# M: Minutes
# H: Hours
# D: Days
# W: Week day (0=Monday)
# midnight: Roll over at midnight
# interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件
# backupCount: 表示日志文件的保留个数
import logging

LOGGER_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
LOGGER_FILE_PATH = 'logs/cmdb.log'
LOGGER_SIZE = 1024 * 1024 * 8
LOGGER_BACKUP_COUNT = 20
LOGGER_WHEN = 'D'
LOGGER_INTERVAL = 1
LOGGER_LEVEL = logging.DEBUG

