import time


def retry(func, retries=1, delay=1):
    for attempt in range(retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == retries:
                raise e
            time.sleep(delay)
