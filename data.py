import random
import time
from prometheus_client import start_http_server, Gauge

g = Gauge('custom_metric', 'custom metric')


def update_metric():
    while True:
        g.set(random.randint(0, 100))
        time.sleep(5)


if __name__ == '__main__':
    start_http_server(8000)
    update_metric()