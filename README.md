# Playwright POM Automation Project

Ushbu loyiha [automationexercise.com](https://www.automationexercise.com/) sayti uchun E2E testlarini o'z ichiga oladi.

## O'rnatish
1. Loyihani yuklab oling.
2. Virtual muhitni yarating: `python -m venv venv`
3. Kutubxonalarni o'rnating: `pip install -r requirements.txt`
4. Playwright brauzerlarini o'rnating: `playwright install`

## Testni ishga tushirish
`pytest --headed --slowmo 1500 --alluredir=allure-results tests/test_e2e.py`

## Hisobotni ko'rish
`allure serve allure-results`