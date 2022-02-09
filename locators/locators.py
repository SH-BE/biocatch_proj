from selenium.webdriver.common.by import By


class home_locators:
    CATEGORY_LIST = (By.ID, 'gh-cat')
    SEARCH_BOX = (By.CLASS_NAME, 'ui-autocomplete-input')


class searched_items_locators:
    MAX_PRICE = (By.XPATH, "//*[contains(@aria-label,'Maximum Value in')]")
    ITEMS = (By.CLASS_NAME, 's-item__link')
    ICON = (By.CLASS_NAME, 'gh-cart-icon')


class product_locators:
    ADD_TO_CART = (By.ID, 'isCartBtn_btn')


class cart_locators:
    TOTAL = (By.XPATH, "//*[@data-test-id='SUBTOTAL']")
    GO_TO_CHECKOUT = (By.CLASS_NAME, 'call-to-action')
    CHECKOUT_AS_A_GUEST = (By.ID, 's0-0-20-10-signin-chooser-layer-1-1-3')


class checkout_locators:
    AMOUNT = TOTAL = (By.XPATH, "//*[@data-test-id='TOTAL']")
