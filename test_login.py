import os
import random

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

Base_url = os.environ.get("Base_url")
Login_username = os.environ.get("Login_username1")
Login_password = os.environ.get("Login_password1")

def test_login(page):
    page.goto(Base_url)
    page.get_by_role("textbox", name="Enter username or email").fill(Login_username)
    page.get_by_test_id("login-password-input").fill(Login_password)
    page.get_by_role("button", name="Sign in").click(timeout=60000)
    expect(page).to_have_url("https://crm.hanuranext.com/login")
    page.get_by_role("link", name="Employees").click()
    expect(page).to_have_url("https://crm.hanuranext.com/employees")
    page.get_by_role("link", name="+ New employee").click()
    expect(page).to_have_url("https://crm.hanuranext.com/employees/new")
    number = random.randint(1, 10000)
    page.get_by_role("textbox", name="FIRST NAME").fill("John")
    page.get_by_role("textbox", name="LAST NAME").fill(f"Smith{number}")
    # get email using test_id
    page.get_by_test_id("employee-form-email").fill(f"johnsmith{number}@abc.com")
    page.get_by_test_id("employee-form-title").fill("Software Engineer")
    # get department using combobox and fill qa
    page.get_by_test_id("employee-form-department").select_option("QA")
    # populate hire date using role and name
    page.get_by_role("textbox", name="HIRE DATE").fill("2023-06-01")
    page.get_by_role("button", name="Create employee").click(timeout=15000)
    page.get_by_role("link", name="Back to employees").click()
    expect(page).to_have_url("https://crm.hanuranext.com/employees")
    page.goto("https://crm.hanuranext.com/employees")
    page.get_by_placeholder("Search by name, title, or email...").fill(f"John Smith{number}")
    
    page.pause()

