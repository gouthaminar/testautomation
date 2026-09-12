import random

from playwright.sync_api import expect


def test_login(page):
    page.goto("https://crm.hanuranext.com")
    page.get_by_role("textbox", name="Enter username or email").fill("day1verify")
    page.get_by_test_id("login-password-input").fill("Day1@verify!")
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
    page.pause()

