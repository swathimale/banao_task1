from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

from selenium.webdriver.support.wait import WebDriverWait


# Function to measure response time
def measure_response_time(driver):
    start_time = time.time()
    driver.get("https://atg.party")
    end_time = time.time()
    response_time = end_time - start_time
    return response_time



# Start a Chrome WebDriver session
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver=webdriver.Chrome()

try:
    #Checking HTTP response code for a URL
    url = 'https://atg.party'
    response = requests.get(url)
    print(f'HTTP response code for {url}: {response.status_code}')
    assert response.status_code == 200

    # Check HTTP response code and measure response time
    response_time = measure_response_time(driver)
    print(f"Response time of page load: {response_time} seconds")
    print(driver.title)
    #assert driver.title == "ATG Party"
    assert driver.title == "Across The Globe (ATG) - Professional and Personal Social Networking"


    # Click on LOGIN

    login_button =driver.find_element(By.CLASS_NAME,"login-link")
    login_button.click()
    time.sleep(2)  # Wait for the login modal to load


    email_input =driver.find_element(By.ID,"email_landing")
    email_input.click()
    email_input.clear()
    email_input.send_keys(" wiz_saurabh@rediffmail.com")

    password_input =driver.find_element(By.ID,"password_landing")
    password_input.click()
    password_input.clear()
    password_input.send_keys("Pass@123")

    submit_button = driver.find_element(By.CLASS_NAME,"landing-signin-btn")
    submit_button.click()

    time.sleep(2)

    print(driver.title)
    time.sleep(2)
 # Wait for login process to complete

    # Step 4: Go to the URL: atg.party/article
    article_url = "https://atg.party/article"
    driver.get(article_url)
    time.sleep(2)
    # Step 5: Fill in title and description
    title_input = driver.find_element(By.ID,'title')
    title_input.click()
    title_input.clear()
    title_input.send_keys("Python: The Versatile Language Shaping Modern Development")


    description_input = driver.find_element(By.XPATH,"//*[@data-empty='true']")
    description_input.click()
    time.sleep(5)

    description_input.send_keys("Python, a versatile and powerful programming language, has gained immense popularity for its simplicity and readability. "
                                "Known for its ease of use and rich ecosystem, Python is favored by beginners and seasoned developers alike."
                                " ### Python's Simplicity and Readability"
                                "Python's syntax emphasizes readability and clarity, making it easy to learn and understand. Its straightforward and expressive nature allows developers to write concise and effective code. For example, Python uses indentation to define code blocks, eliminating the need for braces or semicolons found in other languages. This feature not only enhances code readability but also encourages good programming practices."
                                "### Versatility and Ecosystem"
                                "Python boasts a vast ecosystem of libraries and frameworks that cater to various domains, including web development, data analysis, machine learning, and scientific computing. Libraries like NumPy, Pandas, and Matplotlib enable efficient data manipulation and visualization, making Python a top choice for data scientists and analysts. Flask and Django are popular frameworks for web development, offering robust tools for building scalable and secure web applications."
                                "### Learning and Community"
                                "Python's beginner-friendly nature and extensive documentation contribute to its popularity among learners. Its readability lowers the barrier to entry for new programmers, fostering a supportive and inclusive community. Python's active community continually contributes to its growth by developing libraries, sharing knowledge through forums and conferences, and providing mentorship to newcomers. "
                                "### Applications Python finds applications in diverse fields: "
                                "- **Web Development**: Frameworks like Django and Flask facilitate rapid development of web applications. "
                                "- **Data Science**: Libraries such as NumPy and Pandas support data manipulation and analysis."
                                " - **Machine Learning**: TensorFlow and PyTorch are leading libraries for building and training machine learning models"
                                "- **Automation**: Python's scripting capabilities enable automation of repetitive tasks, enhancing productivity."
                                " ### Conclusion"
                                "Python's simplicity, readability, versatility, and thriving community have cemented its place as a preferred language for developers worldwide. Whether you're a beginner exploring programming for the first time or an experienced professional tackling complex projects, Python offers the tools and resources needed to succeed in today's dynamic technological landscape. Its continual evolution and adaptability ensure it remains a cornerstone of modern software development.")

    # Step 6: Upload cover image
    time.sleep(5)
   # cover_image_input = driver.find_element(By.CLASS_NAME,'add-cover-image')
    #cover_image_path = '\Resources\coverimage.jpg'
   # cover_image_input.send_keys(cover_image_path)

     #Step 7: Click on POST button
    post_button = driver.find_element(By.ID,'hpost_btn')
    post_button.click()
    time.sleep(5)  # Wait for the article to be posted

     #Step 8: Log the URL of the new page
    new_url = driver.current_url
    print(f"URL of the new page after posting: {new_url}")

finally:
    #driver.quit()
    print(driver.title)