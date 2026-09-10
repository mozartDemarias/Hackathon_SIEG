import os

from dotenv import load_dotenv

from src.browser.driver import create_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Carregar Variáveis de Ambiente
load_dotenv()

def clicar_com_seguranca(driver, locator, timeout=10):
    fechar_popups(driver)

    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    fechar_popups(driver)

    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    elemento.click()

def main():
    driver = create_driver()
    base_url = os.getenv("BASE_URL")

    if not base_url:
        raise ValueError("BASE_URL não definida no .env")

    driver.get(base_url)

    try:
        wait = WebDriverWait(driver, 30)

        # Entrar para logar
        botao_entrar = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="/app/login"]')
            )
        )

        botao_entrar.click()

        # Busca dados do .env
        team_token = os.getenv("SITE_TOKEN")
        password = os.getenv("SITE_PASSWORD")

        if not team_token or not password:
            raise ValueError("TEAM_TOKEN ou SITE_PASSWORD não definidos no .env")

        # Espera os campos aparecerem
        campo_token = wait.until(
            EC.visibility_of_element_located((By.ID, "teamToken"))
        )

        campo_senha = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        # Preenche
        campo_token.send_keys(team_token)
        campo_senha.send_keys(password)

        # Clica em acessar
        botao_acessar = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[type="submit"]')
            )
        )

        botao_acessar.click()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()