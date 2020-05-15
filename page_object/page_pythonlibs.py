from framework.base_action import BaseAction


class PagePYTHONLIBS(BaseAction):
    whl_url = ('xpath', '/html/body/ul[1]/li[3]/ul/li[1]/a')

    def download_whl(self):
        print(self.get_element_text(self.whl_url))
        self.click_element(self.whl_url)
        self.sleep(13)
