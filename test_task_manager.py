from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TaskManagerTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")  # Adjust to your local server

    def test_add_task(self):
        self.driver.find_element(By.ID, "taskInput").send_keys("New Task")
        self.driver.find_element(By.ID, "addTaskButton").click()
        self.assertIn("New Task", self.driver.page_source)

    def test_delete_task(self):
        self.driver.find_element(By.ID, "taskInput").send_keys("Task to Delete")
        self.driver.find_element(By.ID, "addTaskButton").click()
        delete_button = self.driver.find_element(By.XPATH, "//li[contains(text(), 'Task to Delete')]//button[text()='Delete']")
        delete_button.click()
        self.assertNotIn("Task to Delete", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
