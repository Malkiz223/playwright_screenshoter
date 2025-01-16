import os

from playwright.sync_api import sync_playwright


def take_screenshot():
    with sync_playwright() as p:
        print("Инициализация Playwright и запуск браузера.")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        url = "https://example.com"
        print(f"Переход на страницу: {url}")
        page.goto(url)

        screenshot_dir = "/app/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, "example_com_screenshot.png")
        print(f"Сохранение скриншота в: {screenshot_path}")
        page.screenshot(path=screenshot_path)
        print(f"Скриншот успешно сохранен: {screenshot_path}")

        print("Браузер запущен. Закройте его вручную для завершения.")

        browser.close()
        print("Браузер закрыт.")


if __name__ == "__main__":
    print("Запуск скрипта для создания скриншота.")
    take_screenshot()
    print("Скрипт завершён.")
