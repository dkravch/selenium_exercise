class BasePage:

    def __init__(self, driver, base_url, relative_url=None):

        self.base_url = base_url
        self.relative_url = relative_url if relative_url else ''
        self.driver = driver

    def open(self):
        self.driver.get(self.base_url + self.relative_url)


def singleton(class_):

    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

