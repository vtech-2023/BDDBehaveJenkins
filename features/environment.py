import time

import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



# This will contain HOOKS - HOOKS in BEHAVE are like PYTEST DECORATERS/ANNOTATION - @pytest


# Hooks to run before scenario and after scenario.
# Hooks to run before step and after step.
# Hooks to run before all and after all

# After step hook
def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)

# Before step hook
def before_step(context, step):
    pass

# Before Scenario Hook
def before_scenario(context, driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.set_page_load_timeout(500)
    context.driver.implicitly_wait(30)

#After Scenario Hook
def after_scenario(context, driver):
    time.sleep(3)
    context.driver.quit()