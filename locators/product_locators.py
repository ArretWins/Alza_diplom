from selenium.webdriver.common.by import By


class ProductLocators:
    PRODUCT_NAME = (By.XPATH, '//h1[@itemprop="name"]')
    PRODUCT_DESCRIPTION = (By.XPATH, '//div[@class="nameextc"]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="price-box__body"]')
    PRODUCT_GALLERY = (By.XPATH, '//div[@class="component detailGallery"]')
    PRODUCT_RATING = (By.XPATH, '//span[@class="ratingValue"]')
    DETAIL_DIALOG = (By.XPATH, 'class="detailDialogsRoot-alz-1"')

    DELIVERY_TITLE = (By.XPATH, '//div[@data-testid="productDetail-availability-locationAvailability"]')
    DELIVERY_BAR = (By.XPATH, '//div[@class="niceScrollbars availability-alz-77"]')
    DELIVERY_INPUT = (By.XPATH, '//input[contains(@class,"MuiAutocomplete-inputFocused")]')
    DELIVERY_INFO = (By.XPATH, '//div[@class="availability-alz-132"]')

    CLOSE_DIALOG_BUTTON = (By.XPATH, '//button[@data-testid="dialog-close-button"]')
    COMMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'descriptionTab-alz-9 blue')]")
    BUY_BUTTON = (By.XPATH, '//a[@class="btnx new green buy js-buy-button"]')
    TO_BASKET_BUTTON = (By.XPATH, '//button[contains(@class, "positive btn-textLeft")]')

    CAROUSEL_CONTENT = (By.XPATH, '//div[@data-testid="carousel-RecommendedAccessoryCarousel_1_70"]')
    BACK_TO_PRODUCT_BUTTON = (By.XPATH, '//a[@id="varBBackButton"]')
    FORWARD_BUTTON = (By.XPATH, '//a[@id="varBToBasketButton"]')

    CROSS_SELL_MESSAGE = (By.XPATH, '//a[@class="productInfo__texts__message"]')
    COMPARE_ITEMS = (By.XPATH, '//a[@class="compare"]')
    SUCCESS_COMPARE_ITEMS = (By.XPATH, '//div[@class="alzaDialogBody"]')

    ALL_PHOTOS = (By.XPATH, '//a[@id="tabFoto"]')
    PHOTO_LAB = (By.XPATH, '//a[@rel="fotoTab"]')
    FANCY_BOX = (By.XPATH, '//div[contains(@class, "fancybox-opened")]')

    DISCUSSION_POSTS = (By.XPATH, '//a[@id="hlTabDiscussionPosts"]')
    DISCUSSION_INPUT = (By.XPATH, '//input[@class="textbox discussion-filter__search-input"]')
    ANSWER_SPAN = (By.XPATH, '//span[@class="reactionsCountSuffix"]')
    EXPERT_IMAGE = (By.XPATH, '//img[@class="authorImage vendorExpert"]')
