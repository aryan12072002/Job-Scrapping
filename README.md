Job Scraping Project

This project is a web-based application designed to scrape job listings from various online platforms and present them in a structured format. It helps users search for jobs efficiently by consolidating job listings and providing customizable filters.

Features

Job Scraping: Extracts job postings from popular job boards and company websites.

Search and Filter: Allows users to search for jobs based on keywords, location, job type, salary range, etc.

Save and Export: Enables users to save job listings and export them to CSV or PDF formats.

Real-Time Updates: Fetches the latest job postings dynamically.

User-Friendly Interface: Offers a clean and responsive interface for easy navigation.

Tech Stack

Backend: Python, Django, Django REST Framework

Frontend: HTML, CSS, JavaScript (Optional: React.js for a dynamic UI)

Database: MySQL

Web Scraping Tools: Beautiful Soup, Scrapy, or Selenium

Other Tools: Pandas for data processing

Installation

Follow these steps to set up the project locally:

Clone the Repository

git clone https://github.com/yourusername/job-scraping-project.git
cd job-scraping-project

Set Up a Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Set Up the Database

Install MySQL and create a database.

Update the database settings in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run migrations:

python manage.py makemigrations
python manage.py migrate

Run the Development Server

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/.

Usage

Use the search bar to find job listings by keywords or job titles.

Apply filters like location, salary range, and job type.

View job details and save your favorite listings.

Export the results to a CSV or PDF file for offline access.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch for your feature or bug fix.

Commit your changes and push them to your fork.

Open a pull request with a description of your changes.

License

This project is licensed under the MIT License.

Contact

For questions or feedback, feel free to reach out:

Name: Aryan Tayade

Email: tayadearyan98@gmail.com

Portfolio: Aryan Tayade Portfolio

LinkedIn: Aryan Tayade

GitHub: Aryan Tayade
