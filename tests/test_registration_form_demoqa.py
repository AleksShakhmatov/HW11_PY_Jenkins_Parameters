from pathlib import Path

import allure
from allure_commons.types import Severity
from selene import have, command, browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "AleksSH")
@allure.feature("Registration")
@allure.story("Fill registration form check")
def test_registration_form_demoqa():
    with allure.step("Open registrations form"):
        browser.open('/automation-practice-form')

    with allure.step("Fill form"):
        browser.element('#firstName').type('Coluchy')
        browser.element('#lastName').type('Aleksandr')
        browser.element('#userEmail').type('AC@ya.com')
        browser.element('[for="gender-radio-1"]').click()
        browser.element("#userNumber").type('4455667788')
        browser.element('#subjectsInput').type('computer').press_enter()
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element('[value="6"]').click()
        browser.element('.react-datepicker__year-select').click().element('[value="1986"]').click()
        browser.element('.react-datepicker__day--008').click()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/8.png')))
        browser.element('#currentAddress').type('India').press_enter()
        browser.element("#react-select-3-input").type("Rajasthan").press_enter()
        browser.element("#react-select-4-input").type("Jaiselmer").press_enter()
        browser.element('#submit').press_enter()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts('Coluchy Aleksandr', 'AC@ya.com', 'Male', '4455667788', '08 July,1986', 'Computer Science',
                             'Sports', '8.png', 'India', 'Rajasthan Jaiselmer'))
