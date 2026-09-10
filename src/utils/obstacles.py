from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException
)


def fechar_popups(driver):
    """
    Fecha popups aleatórios que possam bloquear a interação.
    """

    try:
        overlays = driver.find_elements(By.CSS_SELECTOR, ".np-overlay")

        for overlay in overlays:
            try:
                botao = overlay.find_element(By.TAG_NAME, "button")

                if botao.is_displayed():
                    botao.click()
                    print("Popup fechado.")

            except (
                NoSuchElementException,
                StaleElementReferenceException
            ):
                continue

    except Exception as erro:
        print(f"Erro ao verificar popup: {erro}")