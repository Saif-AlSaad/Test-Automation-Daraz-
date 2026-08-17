from pages.cart_page import CartPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


logger = LogGen.loggen()


# =========================================================
# BUG-02: DOUBLE ADD TO CART
# =========================================================

def test_double_add_to_cart(driver):

    logger.info(
        "========== BUG-02 DOUBLE ADD TO CART TEST STARTED =========="
    )

    cart = CartPage(driver)

    # STEP 1: Open Daraz
    logger.info("STEP 1: Opening Daraz")

    cart.open()

    # STEP 2: Search product
    logger.info("STEP 2: Searching product")

    cart.search_product(
        ReadConfig.get_product()
    )

    cart.click_search()

    # STEP 3: Open first product
    logger.info("STEP 3: Opening first product")

    cart.click_first_product()

    cart.switch_to_new_tab()

    # STEP 4: Get product name
    product_name = cart.get_product_name()

    print("\n========== BUG-02 RESULT ==========")
    print("Product:", product_name)

    # STEP 5: Add product to cart - FIRST CLICK
    logger.info(
        "STEP 5: First Add to Cart click"
    )

    cart.click_add_to_cart()

    # Wait a little for cart action
    import time
    time.sleep(2)

    # STEP 6: Take screenshot after first click
    cart.take_screenshot(
        "screenshots/BUG-02_first_add_to_cart.png"
    )

    # STEP 7: Try clicking Add to Cart again
    logger.info(
        "STEP 7: Second Add to Cart click"
    )

    try:

        cart.click_add_to_cart()

        print(
            "Second Add to Cart click was accepted."
        )

        print(
            "BUG CANDIDATE: Same product can be added again "
            "without a clear prevention/quantity control."
        )

    except Exception:

        print(
            "Second Add to Cart click was not accepted."
        )

        print(
            "No duplicate-add behavior observed."
        )

    # STEP 8: Screenshot
    cart.take_screenshot(
        "screenshots/BUG-02_double_add_to_cart.png"
    )

    logger.info(
        "========== BUG-02 DOUBLE ADD TO CART TEST FINISHED =========="
    )
    