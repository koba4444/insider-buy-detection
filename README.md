Based on the requirements, here are the core classes, functions, and methods that will be necessary:

1. `SECWebsiteScraper`: This class will handle the scraping of the SEC website to collect Form 4 reports for insider buying transactions.
   - `search_company(company_name: str) -> List[str]`: This method will search for the company on the SEC website and return a list of filing URLs.
   - `get_form4_reports(filing_urls: List[str]) -> List[Form4Report]`: This method will extract the Form 4 reports from the given filing URLs and return a list of `Form4Report` objects.

2. `Form4Report`: This class will represent a single Form 4 report for insider buying.
   - Properties:
     - `insider_name: str`: The name of the insider.
     - `company_name: str`: The name of the company.
     - `transaction_date: datetime`: The date of the transaction.
     - `shares_bought: int`: The number of shares bought.

3. `DataStorage`: This class will handle the storage of the collected data.
   - `save_form4_reports(reports: List[Form4Report])`: This method will save the Form 4 reports to a data storage system.

Now let's proceed with creating the necessary files and writing the code.

**1. `sec_website_scraper.py`**

