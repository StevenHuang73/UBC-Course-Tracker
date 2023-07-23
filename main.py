# Program monitors course and returns all sections that are available to register 

def Course_Monitor():
  from course import Course
  from discordwebhook import Discord

  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()

  course0 = Course("CPSC", "110", "101")
  course1 = Course("WRDS", "150B", "931")
  course2 = Course("WRDS", "150B", "921")
  courses = {course0, course1, course2}

  discord =   Discord(url="https://discord.com/api/webhooks/1129058997136265327/QBWgQGG63jOZ4oUwkzHfkUyYr8Eu73wvm15Yds5qkCtjuICfY60wJ1gH_BKgHAM-qXtp")
  for course in courses:
  
    url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept="+course.dept+"&course="+course.number+"&section="+course.section

    driver.get(url)
    driver.implicitly_wait(5)
    findings = driver.find_element(By.XPATH, "//td[contains(text(),'Total Seats Remaining:')]/following-sibling::td")
    text = findings.text
    seats = int(text)

    if seats > 0:
      discord.post(content = course.dept + " " + course.number + " " + course.section + " has " + str(seats) + " seats open.")




