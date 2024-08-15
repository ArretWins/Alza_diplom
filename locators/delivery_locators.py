from selenium.webdriver.common.by import By


class DeliveryLocators:
    DELIVERY_CONTAINER = (By.XPATH, '//div[@id="order2DeliveryContainer"]')
    ALZA_BOX = (By.XPATH, '//div[contains(text(), "AlzaBox")]')
    SHOWROOM = (By.XPATH, '//div[contains(text(), "Showroom")]')
    MARKET = (By.XPATH, '//div[contains(text(), "Predajne")]')
    MARKETS_AND_BOXES = (By.XPATH, '//div[contains(text(), "miesta")]')
    DELIVERY_TO_ADDRESS = (By.XPATH, '//div[contains(text(), "na adresu")]')
    ALZA_BOX_CHECKBOX = (By.XPATH, '//label[@for="deliveryCheckbox--12"]')
    SHOWROOM_CHECKBOX = (By.XPATH, '//label[@for="deliveryCheckbox-684"]')
    MARKET_CHECKBOX = (By.XPATH, '//label[@for="deliveryCheckbox--11"]')
    MARKETS_AND_BOXES_CHECKBOX = (By.XPATH, '//label[@for="deliveryCheckbox--10"]')
    DELIVERY_TO_ADDRESS_CHECKBOX = (By.XPATH, '//label[@for="deliveryCheckbox-3090"]')

    CONFIRM_BUTTON = (By.XPATH, '//a[@id="confirmOrder2Button"]')

    DIALOG_BODY = (By.XPATH, '//div[@id="deliveryContainer--12-219130725"]')
    CLOSE_DIALOG_BUTTON = (By.XPATH, '//span[contains(@class,"close-button")]')

    BRATISlAVA_MARKET = (By.XPATH, '//h4[contains(text(), "Nivy")]')
    TATRACENTRUM_MARKET = (By.XPATH, '//h4[contains(text(), "(Tatracentrum)")]')
    MARKET_CONFIRM = (By.XPATH, '//button[@data-testid="salesNetwork-pickupHere"]')

    PAY_BY_CARD_BUTTON = (By.XPATH, '//label[@for="paymentCheckbox-216"]')
    CHECKED_LABEL = (By.XPATH, '//label[@class=" alzacheckbox classic checked"]')
    SHOWROOM_COMFIRM = (By.XPATH, '//a[contains(@class, "green dialogButton")]')

    STREDA_MARKET = (By.XPATH, '//h4[contains(text(), "Streda")]')
    OPENING_HOURS = (By.XPATH, '//button[@class="openingHours"]')

    DROGERIA = (By.XPATH, '//button[@data-testid="salesNetwork-place-1015950-2680"]')
    DROGERIA_CONFIRM = (By.XPATH, '//button[@data-testid="salesNetwork-pickupHere"]')

    DELIVERY_INPUT = (By.XPATH, '//input[@role="combobox"]')
    DELIVERY_TIME_BUTTON = (By.XPATH, '//button[@data-testid="order2-delivery-day-time-item"]')
