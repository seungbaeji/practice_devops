import logging
import logging.config
import tomllib
import time
import random

# TOML 파일 읽기
with open('logger.toml', 'rb') as f:
    config = tomllib.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger()

# 주기적으로 로그 생성
try:
    while True:
        # INFO 로그 생성
        logger.info('This is an INFO log message from my application.')

        # 30% 확률로 WARNING 로그 생성
        if random.random() < 0.3:
            logger.warning('This is a WARNING log message!')

        # 20% 확률로 ERROR 로그 생성
        if random.random() < 0.2:
            logger.error('This is an ERROR log message!')

        # 1초 간격으로 로그 생성
        time.sleep(1)

except KeyboardInterrupt:
    print("Logging stopped.")
