from selenium import webdriver
from selenium.webdriver.common.by import By
from dataclasses import dataclass
from writer import write_to_csvs, get_start_value
import random, time

URL = "https://www.linkedin.com/jobs/search/?start={}&keywords={}"


START = get_start_value("detail.csv")

@dataclass
class Job:
    job_id: str = ""
    location: str = None
    designation: str = None
    detail_id: int = None
    company_id: str = ""


@dataclass
class Detail:
    detail_id: int = 0
    involvement: str = None
    level: str = None
    applicants: int = None

@dataclass
class Company:
    company_id: str
    name: str
    industry: str
    employee_count: int
    linkedin_followers: int


# Initialize--------------
options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
# options.add_argument("--proxy-server=%s" % "38.154.227.167:5868") 
driver = webdriver.Chrome(options=options) 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 


driver.get("https://linkedin.com/")
driver.implicitly_wait(10)

username = driver.find_element(by=By.XPATH, value='//*[@id="session_key"]')
password = driver.find_element(by=By.XPATH, value='//*[@id="session_password"]')
driver.implicitly_wait(100)

username.send_keys("abc@gmail.com")
password.send_keys("password")

login_btn = driver.find_element(
    by=By.CLASS_NAME, value="sign-in-form__submit-btn--full-width"
)
login_btn.click()
time.sleep(20)

def process_job(job_id: str, cnt: int):
    time.sleep(random.randint(3,9))
    driver.get(f"https://www.linkedin.com/jobs/collections/?currentJobId={job_id}")
    job_detail_element = driver.find_element(
        by=By.CLASS_NAME, value="job-details-jobs-unified-top-card__content--two-pane"
    )
    driver.implicitly_wait(10)

    role = job_detail_element.find_element(by=By.TAG_NAME, value="h2").text
    driver.implicitly_wait(10)

    primary_desc = driver.find_element(
        by=By.CLASS_NAME,
        value="job-details-jobs-unified-top-card__primary-description-container",
    )
    driver.implicitly_wait(10)


    location = primary_desc.text


    company_action = primary_desc.find_element(by=By.TAG_NAME, value="a")
    driver.implicitly_wait(10)

    company_profile = company_action.get_attribute("href")
    company_profile = company_profile.removesuffix("life/")
    company_profile = company_profile.removesuffix("life")
    print(company_profile)
    applicants = (
        primary_desc.find_element(by=By.TAG_NAME, value="div")
        .find_elements(by=By.TAG_NAME, value="span")[-1]
        .text
    )
    driver.implicitly_wait(10)

    applicants = int(applicants.split()[-2])

    level_n_involvement = job_detail_element.find_element(by=By.CLASS_NAME, value="mt3")
    level_n_involvement = level_n_involvement.find_element(by=By.TAG_NAME, value="ul")
    level_n_involvement = level_n_involvement.find_elements(by=By.TAG_NAME, value="li")[
        0
    ]
    spans = level_n_involvement.find_element(
        by=By.TAG_NAME, value="span"
    ).find_elements(by=By.TAG_NAME, value="span")
    level = spans[-1].text.split()[0]
    involvement = (
        "Full-Time"
        if "full-time" in spans[-2].text.lower()
        else ("Part-Time" if "part-time" in spans[-2].text.lower() else "")
    )
    driver.implicitly_wait(10)


    job = Job(
        job_id=job_id,
        location=location,
        designation=role,
        detail_id=cnt,
    )

    detail = Detail(
        detail_id=cnt,
        involvement=involvement,
        level=level,
        applicants=applicants
    )

    company = process_company(url=company_profile)
    job.company_id = company.company_id

    print(job)
    print(company)
    print(detail)

    return (job, company, detail)

def get_jobs(start):
    text_box = driver.find_element(by=By.TAG_NAME, value="main")
    job_cards = text_box.find_elements(by=By.XPATH, value="//*[@data-job-id]")
    job_ids = []
    cnt = START + start
    for job in job_cards:
        try:
            job_ids.append(job.get_attribute("data-job-id"))
        except Exception as e:
            print("Exception: ", e)
            print(job_ids)
            break
    
    for job_id in job_ids:
        try:
            vals = process_job(job_id=job_id, cnt=cnt)
        except Exception as e:
            print("Exception: ", e)
            cnt+=1
            continue
        cnt+=1
        write_to_csvs(vals[0], vals[1], vals[2])

def process_company(url: str) -> Company:


    # About Section
    time.sleep(random.randint(2,9))
    driver.get(url + "about")
    print(url+"about")
    driver.implicitly_wait(10)
    dds = driver.find_elements(by=By.TAG_NAME, value="dd")
    industry = dds[1].text
    employees = int(dds[3].text.split()[0].replace(",",""))

    # Posts Section
    time.sleep(random.randint(2,9))
    driver.get(url + "posts")
    driver.implicitly_wait(100)
    section = driver.find_element(by=By.CLASS_NAME, value="org-company-info-module__container")
    name = section.find_element(by=By.TAG_NAME, value="h2").text
    followers = int(section.find_element(by=By.TAG_NAME, value="p").text.split()[0].replace(",",""))

    company_id = url.split("/")[-2]
    return Company(
        company_id=company_id,
        name=name,
        industry=industry,
        employee_count=employees,
        linkedin_followers=followers
    )

def main():

    keywords = [ "QA", "Finance"]

    start = 0

    for keyword in keywords:
        for i in range(10):
            time.sleep(random.randint(2,9))
            driver.get(URL.format(start, keyword))
            get_jobs(start=start)
            start += 25




if __name__ == "__main__":
    main()
