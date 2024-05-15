import requests
from bs4 import BeautifulSoup
from typing import List
from .sleep import sleep


class BonBanhCrawler:
    def __init__(self, origin_url: str, num_page: int, sleep: bool = True):
        self.origin_url = origin_url
        self.num_page = num_page
        self.sleep = sleep

    def get_soup_response(self, url: str) -> BeautifulSoup:
        """
        This function takes a URL as input and returns a BeautifulSoup object.
        It sends a GET request to the URL and
        parses the response text with BeautifulSoup.

        Parameters:
        url (str): The URL to send the GET request to.

        Returns:
        BeautifulSoup: The parsed HTML response text.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_data(self, url) -> List:
        """
        This function takes a URL as input and
        returns a list of data extracted from the HTML.
        It finds all elements with the class "car-item",
        extracts the href attribute and the element itself,
        and appends them to the data list.
        Additionally, it also fetches the detail data for each item
        by sending a GET request to the detail URL.

        Parameters:
        url (str): The URL to extract data from.

        Returns:
        list: A list of lists, where each sublist contains the detail URL,
        the element itself, and the detail data.
        """
        print(f"Starting to crawl data from: {url}")
        home_soup = self.get_soup_response(url)
        all_items = home_soup.find_all(class_="car-item")
        n = len(all_items)
        print(f"Found {n} items.")
        data = [[] for i in range(n)]
        for idx, item in enumerate(all_items):
            try:
                item_detail_url = item.find("a")["href"]
                detail_url = f"https://bonbanh.com/{item_detail_url}"
                data[idx].append(detail_url)
                data[idx].append(str(item))
                if self.sleep:
                    sleep(1, 2)
                data[idx].append(self.get_detail_data(detail_url))
                print(f"Successfully extracted item {idx+1}: {detail_url}")
            except Exception as e:
                print("An error while get item URL:", e)
        print()
        return data

    def get_detail_data(self, url: str):
        """
        This function takes a URL as input,
        sends a GET request to the URL,
        parses the response text with BeautifulSoup,
        and returns the first element with the id 'sgg'.

        Parameters:
        url (str): The URL to send the GET request to.

        Returns:
        bs4.element.Tag: The first HTML element with the id 'sgg',
        or None if no such element is found.
        """
        detail_soup = self.get_soup_response(url)
        return str(detail_soup.find(id="sgg"))

    def crawl(self) -> List:
        """
        This method crawls a specified number of pages
        starting from the origin URL.
        It first checks if the number of pages is less than 1,
        in which case it returns an empty list.
        Then, it gets the data from the origin URL
        and sleeps for a random amount of time.
        After that, it gets the data from each subsequent page,
        sleeping for a random amount of time between each page
        to avoid overloading the server.
        The data from each page is appended to the 'data' list.

        Returns:
        list: A list of data extracted from the HTML of each page.
        """
        if self.num_page < 1:
            return []
        data = self.get_data(self.origin_url)
        if self.sleep:
            sleep(2, 4)
        for i in range(2, self.num_page + 1):
            data += self.get_data(self.origin_url + f"/page,{i}")
            if self.sleep:
                sleep(2, 4)
        return data
