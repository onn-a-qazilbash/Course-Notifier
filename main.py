from selenium import webdriver
import time
import json

from txt_msg import TextMessage


class Notifier:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)

        self.keys = {}

        self.driver = webdriver.Chrome(options=chrome_options)
        self.text_message = None
        self.available_coures = {}
        self.sleep = 3
    
    def init_driver(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def init_routes(self):
        creds = open('./routes.json')
        self.keys = json.load(creds)
        creds.close()


    def init_text_msg(self):
        account_sid = self.keys["account_sid"]
        auth_token = self.keys["auth_token"]
        incoming = self.keys["numbers"]["send_from"]
        outgoing = self.keys["numbers"]["send_to"]

        self.text_message = TextMessage(account_sid, auth_token, incoming, outgoing)
        

    def load_page(self):
        """
        Visists the websites and clicks on the "sign in" button
        """
        website = self.keys["website"]
        sign_in_button = self.keys["elements"]["sign_in_button"]

        self.driver.get(website)
        print(f"Visiting {self.driver.title}")
        time.sleep(self.sleep)
        # Click to go to sign in page
        self.driver.find_element_by_id(sign_in_button).click()

        return self.driver.title        


    def login(self):
        """
        If we need to authenticate, this function locates the forms
        and send the username and password
        """
        # get creds from file
        ccid = self.keys["ccid"]
        password = self.keys["password"]
        # get element ids from file
        ccid_form_k = self.keys["elements"]["ccid_form"]
        password_form_k = self.keys["elements"]["password_form"]
        submit_btn_k = self.keys["elements"]["submit_btn"]
        # locate forms and submit button
        ccid_form = self.driver.find_element_by_id(ccid_form_k)
        password_form = self.driver.find_element_by_id(password_form_k)
        submit_btn = self.driver.find_element_by_class_name(submit_btn_k)

        time.sleep(self.sleep)

        ccid_form.send_keys(ccid)
        time.sleep(1)
        password_form.send_keys(password)
        time.sleep(1)
        submit_btn.click()


    def click_on_watchlist(self):
        """
        Clicks on the watchlist link in the navbar
        """
        nav_swtich_k = self.keys["elements"]["nav_swtich"]
        watch_list_link = self.keys["elements"]["watch_list_link"]

        time.sleep(self.sleep)
        self.driver.switch_to.frame(nav_swtich_k)

        # find watchlist link
        watch_list = self.driver.find_element_by_partial_link_text(watch_list_link)
        watch_list.click()



    def nav_to_watchlist(self):
    
        main_switch_k = self.keys["elements"]["main_switch"]
        radio_btn = self.keys["elements"]["winter_2021_radio_btn"]
        continue_btn_k = self.keys["elements"]["continue_btn"]

        time.sleep(self.sleep)
        # navigate to watchlist page
        self.driver.switch_to.frame(main_switch_k)
        winter_2021_radio_btn = self.driver.find_element_by_id(radio_btn)
        continue_btn = self.driver.find_element_by_id(continue_btn_k)

        # click on the buttons and hit submit
        winter_2021_radio_btn.click()
        time.sleep(self.sleep)
        continue_btn.click()
        
    def get_courses(self):
        """
        Retrieves all the courses in the watchlist
        """
        course_table_k = self.keys["elements"]["course_table"]
        course_table = self.driver.find_element_by_id(course_table_k).text.split('\n')
    
        for item in range(3, len(course_table), 6):
            course_name = course_table[item]
            seats = int(course_table[item+4].split('/')[0])

            # if a course has at least one seat available, add it to the dict
            if seats > 0:
                self.available_coures[course_name] = seats


    def empty_seat(self):
        # returns true if at least one course has 1 or more seats available
        return (len(self.available_coures) > 0)

    def send_text(self):
            message = "\nALERT\n"
            for course in self.available_coures:
                message += f"{course} has {self.available_coures[course]} seat(s) available.\n"

            self.text_message.add_message(message)
            self.text_message.send()

    def refresh(self):
        self.driver.refresh()

    def end_script(self):
        self.driver.close()

def get_web_title():
    
    web_title_file = open('./supp.json')
    web_title = json.load(web_title_file)
    web_title_file.close()
    return web_title["web_title"]

def main():

    web_title = get_web_title()

    refresh_interval = 600
    cycles = 1

    notifier = Notifier()
    notifier.init_driver()

    notifier.init_routes()
    notifier.init_text_msg()

    print("Starting script... \n")
    page_title = notifier.load_page()
    if page_title == web_title:
        notifier.login()
    
    notifier.click_on_watchlist()

    for cycle in range(cycles):
        print("Checking for availability... \n")

        notifier.nav_to_watchlist()
        notifier.get_courses()

        if notifier.empty_seat():
            notifier.send_text()
        else:
            print("No seats available currently... \n")
        
        if cycle != cycles-1:
            time.sleep(refresh_interval)
            notifier.refresh()
    
    print("Ending script... \n")
    notifier.end_script()


if __name__ == "__main__":
    main()


