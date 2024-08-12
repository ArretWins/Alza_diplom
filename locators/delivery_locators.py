from selenium.webdriver.common.by import By


class DeliveryLocators:
    DELIVERY_CONTAINER = (By.XPATH, '//div[@id="order2DeliveryContainer"]')
    ALZA_BOX = (By.XPATH, '//label[@for="deliveryCheckbox--12"]')
    SHOWROOM = (By.XPATH, '//label[@for="deliveryCheckbox-684"]')
    MARKET = (By.XPATH, '//label[@for="deliveryCheckbox--11"]')
    MARKETS_AND_BOXES = (By.XPATH, '//label[@for="deliveryCheckbox--10"]')
    DELIVERY_TO_ADDRESS = (By.XPATH, '//label[@for="deliveryCheckbox-1294"]')

    CONFIRM_BUTTON = (By.XPATH, '//a[@id="confirmOrder2Button"]')

    DIALOG_BODY = (By.XPATH, '//div[@id="deliveryContainer--12-219130725"]')
    CLOSE_DIALOG_BUTTON = (By.XPATH, '//span[contains(@class,"close-button")]')

    BRATISlAVA_MARKET = (By.XPATH, '//button[contains(@data-testid, "1009015-2680")]')
    MARKET_CONFIRM = (By.XPATH, '//button[@data-testid="salesNetwork-pickupHere"]')

    PAY_BY_CARD_BUTTON = (By.XPATH, '//label[@for="paymentCheckbox-216"]')
    CHECKED_LABEL = (By.XPATH, '//label[@class=" alzacheckbox classic checked"]')
    SHOWROOM_COMFIRM = (By.XPATH, '//a[contains(@class, "green dialogButton")]')

    SENEC_MARKET = (By.XPATH, '//button[@data-testid="salesNetwork-place-921"]')
    OPENING_HOURS = (By.XPATH, '//button[@class="openingHours"]')

    DROGERIA = (By.XPATH, '//button[@data-testid="salesNetwork-place-1015950-2680"]')
    DROGERIA_CONFIRM = (By.XPATH, '//button[@data-testid="salesNetwork-pickupHere"]')

    DELIVERY_INPUT = (By.XPATH, '//input[@role="combobox"]')
    DELIVERY_TIME_BUTTON = (By.XPATH, '//button[@data-testid="order2-delivery-day-time-item"]')
