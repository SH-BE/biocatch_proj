class home_locators:
    CATEGORY_SHOP = ('id', 'gh-cat')

    @staticmethod
    def category_by_text(text):
        return ('xpath', "//*[@class='scnd' and text()='"+text+"']")