from scrapingant_client import ScrapingAntClient
from pathlib import Path

file_path = Path('output.nobrowser.html')

client = ScrapingAntClient(token='')

result = client.general_request(url='https://www.stubhub.com/cincinnati-bengals-tickets/performer/6045/', browser=False)

file_path.write_text(result.content)

