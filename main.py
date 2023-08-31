import csv
import requests
from bs4 import BeautifulSoup
import time

def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all(
        'div',
        class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'
    )

    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_='job-search-card__location').text.strip()
        job_link = job.find('a', class_='base-card__full-link')['href']

        writer.writerow([
            job_title,
            job_company,
            job_location,
            job_link
        ])

    print('Data updated')

    if page_number < 25:
        page_number += 25
        linkedin_scraper(webpage, page_number)
    else:
        file.close()
        print('File closed')

if __name__ == "__main__":
    position = input("Digite a posição que você está procurando: ").replace(" ", "%20")
    location = input("Digite a localização (ou 'remoto'): ").replace(" ", "%20")
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f'linkedin-jobs-{position}-{location}-{timestamp}.csv'
    
    file = open(filename, 'w', encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location', 'Apply'])
    
    webpage = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={position}&location={location}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start='

    linkedin_scraper(webpage, 0)
