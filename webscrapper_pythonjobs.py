import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

job_title=[] #List to store name of the job
job_company=[] #List to store company name of the job
job_location=[] #List to store location of the job
job_date = []#List to store date of the job
apply_link = []# List to store the link to apply for the job

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
#job_elements = results.find_all("div", class_="card-content")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    date_element = job_element.find("p", class_="is-small has-text-grey")
    link_url = job_element.find_all("a")[1]["href"]


    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(date_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()

    job_title.append(title_element.text.strip())
    job_company.append(company_element.text.strip())
    job_location.append(location_element.text.strip())
    job_date.append(date_element.text.strip())
    apply_link.append(link_url.strip())


df = pd.DataFrame({'Job Name':job_title,'Company Name':job_company,'Location':job_location, 'Date': job_date, 'ApplyHere: ': apply_link})
df.to_csv('python_jobs.csv', index=False, encoding='utf-8')
