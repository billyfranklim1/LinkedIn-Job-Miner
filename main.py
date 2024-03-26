import csv
import requests
from bs4 import BeautifulSoup
import time

black_list_companies = ['GeekHunter', 'Netvagas', 'Oowlish']

def make_request(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")
        return None

def scrape_linkedin_jobs(webpage, max_pages=10):
    all_jobs = []
    for page_number in range(max_pages):
        next_page = f"{webpage}&start={page_number * 25}"
        response = make_request(next_page)
        if not response:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

        for job in jobs:
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
            job_location = job.find('span', class_='job-search-card__location').text.strip()
            job_link = job.find('a', class_='base-card__full-link')['href']
            job_date_element = job.find('time', class_='job-search-card__listdate')
            job_date = job_date_element.get('datetime') if job_date_element else 'No date'

            if job_company not in black_list_companies:
                all_jobs.append([job_title, job_company, job_location, job_date, job_link])

    return all_jobs

def save_jobs_to_csv(jobs, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location', 'Timestamp', 'Apply'])
        writer.writerows(jobs)

def main():
    position = input("Digite a posição que você está procurando: ").replace(" ", "%20")
    location = input("Digite a localização (ou 'remoto'): ").replace(" ", "%20")
    
    print("Nível de experiência:\n1. Estagiário\n2. Assistente\n3. Junior\n4. Pleno/Senior")
    level_input = input("Escolha o nível de experiência desejado (1-4): ")
    level = {"1": "1", "2": "2", "3": "3", "4": "4"}.get(level_input, "2")
    
    print("Período de postagem:\n1. Últimas 24 horas\n2. Última semana\n3. Último mês")
    time_posted_input = input("Escolha o período de postagem (1-3): ")
    time_posted = {"1": "r86400", "2": "r604800", "3": "r2592000"}.get(time_posted_input, "r2592000")
    
    print("Tipo de trabalho:\n1. Presencial\n2. Remoto\n3. Híbrido")
    work_type_input = input("Escolha o tipo de trabalho (1-3): ")
    work_type = {"1": "1", "2": "2", "3": "3"}.get(work_type_input, "2")
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f'linkedin-jobs-{position}-{location}-{timestamp}.csv'
    
    webpage = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={position}&location={location}&f_TPR={time_posted}&f_E={level}&f_WT={work_type}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    
    all_jobs = scrape_linkedin_jobs(webpage)
    save_jobs_to_csv(all_jobs, filename)
    print('Arquivo salvo com sucesso.')

if __name__ == "__main__":
    main()
