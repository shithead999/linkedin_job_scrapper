# LinkedIn Jobs Data Analysis and Visualization Project

## Project Overview
This project offers a comprehensive analysis and visualization of LinkedIn job data. It aims to provide insightful trends and patterns in the job market, focusing on key sectors, job roles, and geographical distribution of opportunities. The project integrates data scraping, cleaning, and sophisticated visualizations using Google Sheets and Power BI.

## Components
1. **Data Scraping**: Python script `scrapper.py` is used to extract job listings from LinkedIn, capturing details such as job title, company name, location, and required qualifications.
2. **Data Cleaning and Preparation**: The `writer.py` script processes and cleans the scraped data. The output consists of three CSV files: `company_no_duplicates2.csv`, `detail_clean.csv`, and `job.csv`, which contain refined and structured job data.
3. **Data Analysis**: A comprehensive analysis is performed on the cleaned datasets, focusing on industry trends, job requirements, and geographical job distribution.
4. **Data Visualization**:
    - **Google Sheets Dashboard**: This interactive dashboard in Google Sheets allows users to explore job data through filters and basic charts.
    - **Power BI Dashboard** (`dashboard.pbix`): An advanced dashboard providing in-depth analysis with dynamic visualizations.

## Technologies Used
- Python for scraping and data processing.
- Google Sheets for initial visualization.
- Power BI for advanced data analytics and visualization.

## Setup and Usage


### Prerequisites
Before starting, ensure you have the following installed:
- Python (version 3.10)
- Necessary Python libraries: [Selenium, dataclasses, pandas, BeautifulSoup, etc.]
- Power BI Desktop (for viewing the `.pbix` file)
- Access to Google Sheets (for the Google Sheets dashboard)

### Setting Up the Python Environment
1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Set up a Virtual Environment** (recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Required Libraries**:
    ```
    pip install selenium
    pip install dataclasses
    pip install pandas
    pip install beautifulsoup
    
    ```
  
### Running the Data Scraping and Cleaning Scripts
1. **Clone the Repository**:
    ```
    git clone https://github.com/shithead999/linkedin_job_scrapper
    cd linkedin_job_scrapper
    ```
2. **Run the Scraper**:
    ```
    python scrapper.py
    ```
   This script will scrape data from LinkedIn and save it in CSV files.
3. **Clean the Data**:
    ```
    python writer.py
    ```
   This will process the scraped data and output cleaned datasets.

### Accessing the Dashboards
#### Google Sheets Dashboard
1. **Open the Google Sheets Dashboard**: The link to the dashboard is [Google Sheets Dashboard Link](https://docs.google.com/spreadsheets/d/1gY4cg91obCTTHvm4K6o4itGcYQgJ0D3pdmMi5LjOTc8/edit#gid=726703983).
2. **Interact with the Dashboard**: Use the provided filters and controls to explore the data.
   Based on the screenshots provided, here is a summary of the Google Sheets dashboard:


#### Power BI Dashboard
1. **Open the Power BI Dashboard**:
    - Open Power BI Desktop.The link to dashboard is [PowerBi Dashboard](https://drive.google.com/file/d/1C0MYvBQ5xseh3xIYz81cDuugXOsJ9CwO/view?usp=sharing)
    - Go to `File > Open` and select the `dashboard.pbix` file from the project directory.
2. **Explore the Dashboard**: Interact with the various visualizations and filters to analyze the job market data.

### Troubleshooting
If you encounter any issues with setting up or running the project:
- Ensure all prerequisites are correctly installed.
- Check for any error messages in the script output and resolve dependencies if required.
- For dashboard-specific issues, ensure you have the correct access permissions and software versions.

For further assistance, contact me at "sakshisanghi0001@gmail.com"



## Dashboard Overview

### Google Sheets Dashboard
### Dashboard for LinkedIn Jobs

#### Vacancies and Applicant Averages
- **Number of Vacancies in each Industry**: A pie chart displays the distribution of job vacancies across various industries. This visual helps quickly identify which sectors have the most opportunities.
- **Average number of applicants in each vacancy**: A large numerical display shows the average number of applicants per job opening, providing insight into the competitiveness of the job market.
  ![Screenshot 2024-01-02 164024](https://github.com/shithead999/linkedin_job_scrapper/assets/111310463/1cf3f036-9fb7-480e-96c9-db24d0392b1b)


#### Job Levels and Categories
- **Count of levels in Jobs**: A bar chart breaks down the number of jobs by level, such as Mid-Senior, Entry, and others, offering a view of the job distribution by seniority.

#### Industry and Employee Counts
- **Employee count vs industry**: A horizontal bar chart shows the number of employees across different industries, potentially indicating the size and employment capacity of each sector.

#### General Job Categories and Designations
- **Count of General Job Category**: A vertical bar chart details the number of jobs in general categories like Software Engineer, Data Scientist, and others, highlighting the demand in each field.
- **Count of designation**: A donut chart presents the proportion of various designations within the dataset, such as Sales, Marketing, QA Engineer, etc.
  ![Screenshot 2024-01-02 164046](https://github.com/shithead999/linkedin_job_scrapper/assets/111310463/36364825-444e-4897-b309-d731d7dcef26)


#### Applicants, Industry Followers, and Geographical Distribution
- **Number of Applicants in each Job Category**: Another vertical bar chart displays the absolute number of applicants for each job category, which, when compared with the average number of applicants, may indicate relative interest or oversaturation in each category.
- **LinkedIn Followers by Industry**: A ring chart illustrates the percentage of LinkedIn followers by industry, giving an indication of the popularity or engagement of each sector on the platform.
- **Geographical Map**: A map highlights the geographical distribution of job opportunities, with markers denoting the location and density of job listings, useful for understanding the geographic job market landscape.
  ![Screenshot 2024-01-02 164103](https://github.com/shithead999/linkedin_job_scrapper/assets/111310463/cab17674-8db1-4ab4-a10a-3c473fe1114d)



Each of these elements serves to provide a comprehensive overview of the job market as reflected in LinkedIn's data. Interactive filters likely allow users to refine the displayed data based on specific industries, job categories, and other parameters, making the dashboard a dynamic tool for job market analysis.


### Power BI Dashboard
The Power BI dashboard in `dashboard.pbix` offers an immersive data visualization experience. It includes the following key features:
- **Interactive Filters**: Users can filter data based on industry, job role, location, and other key metrics.
- **Trend Analysis Charts**: Visual representations of job market trends over time, including growth sectors and emerging job roles.
- **Geographical Heat Maps**: A map view showing job distribution across different regions, highlighting areas with the highest job concentrations.
- **Industry and Role Comparisons**: Bar and pie charts comparing different industries and roles in terms of job availability and requirements.
- **Customizable Views**: Users can customize views and drill down into specific data points for a more detailed analysis.
  ![image](https://github.com/shithead999/linkedin_job_scrapper/assets/111310463/42ad1176-ff1a-424c-8da2-19cc0c54dc00)
  ![image](https://github.com/shithead999/linkedin_job_scrapper/assets/111310463/abefdfc8-7fe8-4234-b39e-8c6af65cbf13)



#### Navigating the Dashboard
1. **Filter Selection**: Use the sidebar to select filters and refine the data displayed.
2. **Viewing Trends**: Click on trend charts to see how job markets have evolved.
3. **Exploring Geographical Data**: Interact with the map to view regional job market distributions.
4. **Comparing Industries and Roles**: Use the comparison charts to understand the landscape of different job sectors and roles.

## Future Work
Plans for future enhancements include:
- Automating the data scraping process.
- Integrating real-time data updates.
- Expanding the analysis to include salary trends and job satisfaction ratings.
- Developing predictive models for job market trends.

## Contact
For queries or contributions, contact me at sakshisanghi0001@gmail.com

https://github.com/shithead999

## Acknowledgments
This project was completed during my internship at [Geekster](https://www.geekster.in/).
I'd like to thank the Geekster team for providing me with the opportunity to work on this project and for the support and guidance they offered throughout the process. The insights and experience gained during this time were invaluable to the successful completion of the project.


