# LinkedIn Job Miner

## 🌟 Overview

**LinkedIn-Job-Miner** is a Python-based web scraping tool designed to simplify your job search. It automatically collects and aggregates job postings from LinkedIn based on the position and location you're interested in. Say goodbye to the tedious process of manually searching for the right job!

## 🌐 Features

- Scrape job postings by title and location
- Save scraped data in a CSV file
- Automated pagination to collect multiple listings
- Easy to set up and run

## 📦 Installation

### Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Clone the Repository

```bash
git clone https://github.com/billyfranklim1/LinkedIn-Job-Miner.git
cd LinkedIn-Job-Miner
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage


Simply run the script, and it will prompt you for the job position and location. The script will scrape LinkedIn job postings and save them in a CSV file named `linkedin-jobs-{position}-{location}-{timestamp}.csv`.

```bash
python main.py
```

## 📝 Contributing

Feel free to fork the project, open a PR, or submit issues.

## 📜 License

This project is open-source and available under the MIT License.
