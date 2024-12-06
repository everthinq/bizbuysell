Bizbuysell
------------------------------------------------------
Scraping [https://www.bizbuysell.com/established-businesses-for-sale/](https://www.bizbuysell.com/established-businesses-for-sale/)

## Installation
1. Clone the repository:
    ```sh 
    git clone https://github.com/everthinq/bizbuysell.git
   ```
2. Install the required dependencies:
    ```sh 
    pip install -r requirements.txt
   ```

## How to run
1. Go to the project directory:
   ```sh 
   cd ~/Projects/Scrapy/bizbuysell
   ```
2. Run this to get json file:
   ```sh 
   scrapy crawl bizbuysell -o bizbuysell.json
   ```
   
## Description
I've completed the scraping of bizbuysell.com single category through the
internal API, gathering 12000 items in under 10 minutes
by making 1 request per 1 page.\
There is a video explanation of my solution below.

## Improvements
However, I couldn’t retrieve the `Gross Revenue` info since it’s not available in the JSON response. My proposed solution is to access each business’s individual page and extract that field from the HTML. This approach would be significantly slower because I would need to do 1 request per 1 business which will significantly increase the amount of requests. For example, I did 400 requests to get 12000 items via internal API calls, but in order to get `Gross Revenue` info I would need to do 12000 requests to get 12000 items. Also, there is a bizbuysell’s heavy security system which I need to bypass by using proxies and browser emulation.

## Watch the video:
[![Watch the video](https://img.youtube.com/vi/YISmuT1HuIo/maxresdefault.jpg)](https://www.youtube.com/watch?v=YISmuT1HuIo)
