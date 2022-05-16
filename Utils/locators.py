from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    username = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    password = (By.XPATH, "//input[@type='password']")
    login = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']//span[text()='Login']")
    login_success = (By.XPATH, "//div[contains(text(),'My Account')]")
    hover_over_my_account = (By.XPATH, "//div[text()='My Account']")
    logout = (By.XPATH, "//div[normalize-space()='Logout']")
    logout_status = (By.XPATH , "//a[text()='Login']")


class HomePageLocators(object):
    grocery = (By.XPATH, "//div[text() = 'Grocery']")
    hover_snacks = (By.XPATH, "//div[text()='Snacks & Beverages']")
    select_biscuits = (By.XPATH, "//a[@class ='_6WOcW9 _2-k99T']")
    hover_personal_baby_care = (By.XPATH, "//div[text()='Personal &  Baby Care']")
    select_perfume = (By.XPATH, "//a[text()='Deos, Perfumes & Talc']")
    hover_Home_Kitchen = (By.XPATH, "//div[text()='Home & Kitchen']")
    select_cookware = (By.XPATH, "//a[text()='Cookware & Non Stick']")
    hover_fashion = (By.XPATH, "//div[text()='Fashion']")
    select_menswear = (By.XPATH, "//a[@class='_6WOcW9 _2-k99T']")
    hover_over_my_account = (By.XPATH, "//div[text()='My Account']")
    select_my_profile = (By.XPATH, "//div[normalize-space()='My Profile']")


class GroceryPageLocators(object):
    get_items_in_grocery = (By.XPATH, "//div[@class= '_1MbXnE']")
    select_item_1 = "//div[contains(text(), '"
    select_item_2 = "') and @class = '_2DFZTN']//ancestor::div[@class = '_35mN4f']//descendant::button[@class = " \
                    "'_2KpZ6l GX4Kov']"


class MyCartPageLocators(object):
    cart = (By.XPATH, "//span[normalize-space()='Cart']")
    view_all_items = (By.XPATH, "//span[@class='EWTJAy']")
    get_item_names_from_cart = (By.XPATH, "//div[@class='_-4o6jJ']//a")
    close_view_cart = (By.XPATH, "//button[contains(text(),'✕')]")
    remove_from_cart = (By.XPATH, "//div[text() = 'Remove Basket']")
    confirm_remove = (By.XPATH, "//div[@class = 'td-FUv WDiNrH']//div[text() = 'Remove Basket']")


class SearchAndFilterPage(object):
    search = (By.XPATH, "//input[@placeholder='Search for products, brands and more']")
    searchlist_items = (By.XPATH, "//div[@class = 'lrtEPN _17d0yO']")
    get_items_from_search = (By.XPATH, "//a[@class = '_2rpwqI']//following::a[@class = 's1Q9rs']")


class FashionPageLocators(object):
    select_items_from_list = (By.XPATH, "//div/a[@class = 'IRpwTa']")
    click_wishlist_1 = "#//div/a[contains(text(), '"
    click_wishlist_2 = "')]//ancestor::div[@class = '_1xHGtK _373qXS']//descendant::div[@class ='_36FSn5']"


class MyProfileLocators(object):
    manage_address = (By.XPATH, "//div[text()='Manage Addresses']")
    add_new_address = (By.XPATH, "//div[contains(text(),'ADD A NEW ADDRESS')]")
    name = (By.XPATH, "//input[@name='name']")
    phone = (By.XPATH, "//input[@name='phone']")
    pincode = (By.XPATH, "//input[@name='pincode']")
    locality = (By.XPATH, "//input[@name='addressLine2']")
    address = (By.CSS_SELECTOR, "textarea[name='addressLine1']")
    city = (By.XPATH, "//input[@name='city']")
    state = (By.XPATH, "//select[@name='state']")
    address_type_home = (By.XPATH, "//label[@for='HOME']//div[1]")
    address_type_work = (By.XPATH, "//label[@for='WORK']//div[1]")
    save = (By.XPATH, "//button[normalize-space()='Save']")
    get_saved_name = (By.XPATH, "//span[@class='_3CfVDh']")
    get_saved_number = (By.XPATH, "//span[@class='_1Z7fmh _3CfVDh']")
    get_address = (By.XPATH, "//span[@class='_2adSi5 WlNme0']")
