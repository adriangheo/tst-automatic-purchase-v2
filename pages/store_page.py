from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class StorePage(BasePage):
    url = 'https://staging4.tstprep.com/store/'

    @property
    def courses_for_duolingo(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Courses for the Duolingo English Test')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def private_lessons_for_duolingo(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Private Lessons for the Duolingo English Test')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def score_evaluation_for_duolingo(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Score Evaluation for the Duolingo English Test')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def complete_practice_test_pack(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Complete Practice')]][text()[contains(.,'Test Pack')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def emergency_course(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Emergency')]][text()[contains(.,'Course')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def score_builder_program(self):
        locator = Locator(By.XPATH,"//h3[text()[contains(.,'Score Builder')]][text()[contains(.,'Program')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def private_lessons_1_4_sections(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Private Lessons')]][text()[contains(.,'1-4 sections')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def trial_lesson(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Trial')]][text()[contains(.,'Lesson')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def speaking_evaluation(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Speaking')]][text()[contains(.,'Evaluation')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def writing_essay_evaluations(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Writing')]][text()[contains(.,'Essay Evaluations')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def reading_group_classes(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Reading')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def listening_group_classes(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Listening')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def speaking_group_classes(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Speaking')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def writing_group_classes(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Writing')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def reading_practice_pack(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Reading')]][text()[contains(.,'Practice Pack')]]")
        return BaseElement(driver = self.driver, locator=locator)
    @property
    def listening_practice_pack(self):
        locator = Locator(By.XPATH, "//h3[text()[contains(.,'Listening')]][text()[contains(.,'Practice Pack')]]")
        return BaseElement(driver = self.driver, locator=locator)

    @property
    def first_pricebox_btn(self):
        locator = Locator(By.CSS_SELECTOR, ".pricebox-button")
        return BaseElement(driver = self.driver, locator=locator)