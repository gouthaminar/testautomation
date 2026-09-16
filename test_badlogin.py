import os

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

Base_url = os.environ.get("Base_url")
Login_username = os.environ.get("Login_username2")
Login_password = os.environ.get("Login_password2")

def test_login(page):
    page.goto(Base_url)
    page.get_by_role("textbox", name="Enter username or email").fill(Login_username)
    page.get_by_test_id("login-password-input").fill(Login_password)
    page.get_by_role("button", name="Sign in").click(timeout=60000)
    page.get_by_test_id("login-error-banner")
