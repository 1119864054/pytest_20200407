from framework.base_action import BaseAction


class PagePIPY(BaseAction):
    banner = ('xpath', '//h1[@class="homepage-banner__title"]')
    search_box = ('xpath', '//*[@id="search"]')
    search_btn = ('xpath', '//*[@id="content"]/div[1]/div/form/button')
    first_res = ('xpath', '//*[@id="content"]/div/div/div[2]/form/div[3]/ul/li[1]')
    download_files_tab = ('xpath', '//*[@id="files-tab"]')
    whl_file = ('xpath', '//*[@id="files"]/table/tbody/tr[1]/th/a')

    def get_banner(self):
        return self.get_element_text(self.banner)

    def input_search_box(self, search_content):
        self.input_element(self.search_box, search_content)

    def click_search_btn(self):
        self.click_element(self.search_btn)

    def get_first_res(self):
        self.click_element(self.first_res)
        self.click_element(self.download_files_tab)
        self.click_element(self.whl_file)
