import requests
from bs4 import BeautifulSoup
from typing import List
from datetime import datetime

from projects.insider_buying.workspace.form4_report import Form4Report


class SECWebsiteScraper:
    def __init__(self):
        self.base_url = "https://www.sec.gov"

    def search_company(self, company_name: str) -> List[str]:
        search_url = f"{self.base_url}/cgi-bin/browse-edgar?action=getcompany&CIK={company_name}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        filing_urls = []

        # Extract filing URLs for Form 4 reports
        filings_table = soup.find("table", class_="tableFile2")
        if filings_table:
            rows = filings_table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) >= 3:
                    filing_type = cells[0].text.strip()
                    filing_href = cells[1].find("a", href=True)
                    if filing_type == "4" and filing_href:
                        filing_url = f"{self.base_url}{filing_href['href']}"
                        filing_urls.append(filing_url)

        return filing_urls

    def get_form4_reports(self, filing_urls: List[str]) -> List[Form4Report]:
        form4_reports = []

        for filing_url in filing_urls:
            response = requests.get(filing_url)
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract insider buying information from Form 4 reports
            table = soup.find("table", class_="tableFile")
            if table:
                rows = table.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) >= 5:
                        transaction_date = datetime.strptime(cells[3].text.strip(), "%Y-%m-%d")
                        shares_bought = int(cells[4].text.strip().replace(",", ""))
                        form4_report = Form4Report(cells[1].text.strip(), cells[2].text.strip(), transaction_date, shares_bought)
                        form4_reports.append(form4_report)

        return form4_reports

if __name__ == "__main__":
    sECWebsiteScraper = SECWebsiteScraper()
    filing_urls = sECWebsiteScraper.search_company("GME")
    ans = sECWebsiteScraper.get_form4_reports(filing_urls)
