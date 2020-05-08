from framework.base_action import BaseAction


class PagePIPY(BaseAction):
    banner = ('xpath', '//h1[@class="homepage-banner__title"]')

    def get_banner(self):
        return self.get_element_text(self.banner)
