# Program monitors course and returns all sections that are available to register 

def Course_Monitor():
  from course import Course
  from discordwebhook import Discord

  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()

  course1 = Course("MICB", "211", "921")
  course2 = Course("BIOL", "260", "951")
  courses = {course1, course2}

  discord =  Discord(url="https://discord.com/api/webhooks/1225268898685915297/kYtw0-0XgNpGVSuTZEdJaKi72s15J-iq-cPEJodL2el0mFb6jOojglOpFdbvTRz0Fcco")
  for course in courses:
  
    url = "https://courses.students.ubc.ca/cs/courseschedule?sesscd=S&pname=subjarea&tname=subj-section&sessyr=2024&course="+course.number+"&section="+course.section+"&dept=" +course.dept
    print(url)

    driver.get(url)
    driver.implicitly_wait(5)
    findings = driver.find_element(By.XPATH, "//td[contains(text(),'Total Seats Remaining:')]/following-sibling::td")
    text = findings.text
    seats = int(text)

    if seats > 0:
      discord.post(content = "@everyone" + course.dept + " " + course.number + " " + course.section + " has " + str(seats) + " seats open.")
    else:
      discord.post(content = course.dept + " " + course.number + " " + course.section + " has 0 seats open.")





