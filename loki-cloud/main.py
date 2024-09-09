import logging
import logging.config
import tomllib
import time
import random
from pathlib import Path

LOG_DIR = Path('tmp')
LOG_DIR.mkdir(exist_ok=True, parents=True)

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
        try:
            if random.random() < 0.3:
                raise ValueError('This is a simulated ValueError!')
        except ValueError as e:
            logger.warning(f'{e}')

        # 20% 확률로 ERROR 로그 생성
        try:
            if random.random() < 0.2:
                # ZeroDivisionError를 인위적으로 발생
                result = 1 / 0
        except ZeroDivisionError as e:
            logger.exception(f'{e}')

        # 1초 간격으로 로그 생성
        time.sleep(1)

except KeyboardInterrupt:
    logger.info("Logging stopped by user.")
