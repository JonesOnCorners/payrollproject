from django.test import TestCase
from .models import Employee, Payroll

import unittest
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from model_mommy import mommy

# Create your tests here.

class EmployeeModelTests(TestCase):
    
    def create_employee(self, employee_id = 300, employee_name = 'Satish Pukale', working_hours = 10, hourly_rate   = 10, is_admin = 'Y', created_by = 'Jaydeep Karale', updated_by  = 'Jaydeep Karale',active = 'Y'):
        return Employee.objects.create(employee_id  = employee_id,
                                       employee_name  = employee_name,
                                       working_hours  = working_hours,
                                       hourly_rate    = hourly_rate,
                                       is_admin       = is_admin,
                                       created_by     = created_by,
                                       updated_by     = updated_by,
                                       active         = active)

    
    def test_employee_creation(self):
        #emp = Employee.objects.values('is_admin').filter(pk = 111)
        e = self.create_employee()
        #self.assertTrue(isinstance(e, Employee))
        self.assertEqual(e.__str__(),'300 Satish Pukale 10 10 Y')
    
    # def test_employee_isadmin_view(self):
    #     e = self.create_employee()
    #     url = reverse('payrollprocess.views.index')

        
class TestEmployeeModelMommy(TestCase):

    def test_employee_model(self):
        e = mommy.make(Employee)
        self.assertTrue(isinstance(e, Employee))
        self.assertEqual(e.__str__(), str(str(e.employee_id)+ '1 ' + e.employee_name +' '+ str(e.working_hours) +' '+ str(e.hourly_rate) +' '+ e.is_admin))

#     def setUp(self):
#         #self.driver = webdriver.Chrome(executable_path='C:/Users/Jaydeep.Karale/Desktop/Blogs/PayRoll/payroll/payrollprocess/chromedriver.exe')
#         self.driver = webdriver.Firefox(executable_path='C:/Users/Jaydeep.Karale/Desktop/Blogs/PayRoll/payroll/payrollprocess/geckodriver.exe')
#         self.driver.implicitly_wait(5)


#     def test_sigin_index(self):
#         #wait = WebDriverWait(self.driver, 30)
#         self.driver.get('http://localhost:8000/payroll')
#         #self.driver.get('http://google.com')
#         #self.driver.find_element_by_id('testview').click()
#         #link = self.driver.find_element_by_id('testview')
#         print(link)
        
#         #time.sleep(5)
#         #link.click()
#         #self.assertIn("http://127.0.0.1:8000/payroll/testview", self.driver.current_url)

        
#         #userID = self.driver.find_element_by_xpath('//label[@for="id_username"]')
#         #userID = self.driver.find_element_by_xpath("//tr[@for='id_username']/label")
#         #userID.send_keys('jayd')
#         #pwd = self.driver.find_element_by_xpath('//table/label[@for="id_password"]')
#         #pwd  = self.driver.find_element_by_id('id_password')
#         #pwd.send_keys('123')
#         #self.driver.find_element_by_id('submit').click()
#         #self.assertIn("http://127.0.0.1:8000/payroll.", self.driver.current_url)
    
#     def tearDown(self):
#         self.driver.quit

# class MySeleniumTests(StaticLiveServerTestCase):
#     #fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver(executable_path='C:/Users/Jaydeep.Karale/Desktop/Blogs/PayRoll/payroll/payrollprocess/geckodriver.exe')
#         cls.selenium.implicitly_wait(10)

#     # @classmethod
#     # def tearDownClass(cls):
#     #     cls.selenium.quit()
#     #     super().tearDownClass()

    
#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/payroll/'))
#         #self.selenium.find_element_by_id('//*[@href]')
#         link = self.selenium.find_element_by_id('testview')
#         #username_input = self.selenium.find_element_by_name("username")
#         #username_input.send_keys('myuser')
#         #password_input = self.selenium.find_element_by_name("password")
#         #password_input.send_keys('secret')
#         #self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()