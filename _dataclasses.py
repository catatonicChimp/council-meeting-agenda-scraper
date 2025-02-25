from dataclasses import dataclass
from typing import Callable, Optional
from regexes import Regexes


@dataclass
class ScraperReturn:
    """Designates what a scraper should return.\n
    If a given item in the scraper is None, it will be skipped.\n
    `name`: The name of the meeting (e.g. City Development Delegated Committee).\n
    `date`: The date of the meeting (e.g. 2021-08-01).\n
    `time`: The time of the meeting (e.g. 18:00).\n
    `webpage_url`: The URL of the webpage where the agenda is found.\n
    `download_url`: The URL of the PDF of the agenda.\n
    """

    name: str
    date: str
    time: str
    webpage_url: str
    download_url: str


@dataclass
class Council:
    """Represents a council with a scraper and regexes.\n
    `name`: council name.\n
    `scraper`: a function that returns a ScraperReturn instance or None.\n
    `regexes`: optional custom regexes used to parse the data in the PDF scraped by the scraper.\n
    `results`: generated by the run_scraper() function.
    """

    name: str
    scraper: Callable[[], Optional[ScraperReturn]]
    regexes: Optional[Regexes] = None
    results: Optional[ScraperReturn] = None

    def run_scraper(self):
        """Runs the scraper and stores the results."""
        self.results = self.scraper()
