from time import time
import requests


class Timer:

    def __init__(self, function):
        self._function = function

    def __call__(self, *args, **kwargs):
        start = time()
        return_value = self._function(*args, **kwargs)
        end = time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value


class Webpage:
    _url = None

    def __init__(self, url):
        self._url = url

    @Timer
    def get_webpage(self):
        return requests.get(self._url).text


if __name__ == '__main__':
    webpage = Webpage('https://google.com')
    print(webpage.get_webpage(webpage))
