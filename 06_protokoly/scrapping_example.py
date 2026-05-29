from pathlib import Path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://www.wytwory.pl/pl/c/Obrazki-i-obrazy/46"
OUTPUT_DIR = Path("images")
OUTPUT_DIR.mkdir(exist_ok=True)

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

print(f"Znaleziono {len(images)} obrazkow")

# a, b = 1, 2

for i, img in enumerate(images, start=1):
    src = img.get("src")

    if not src:
        continue

    image_url = urljoin(URL, src)
    print("pobieram", image_url)

    try:
        img_response = requests.get(image_url)
        img_response.raise_for_status()

        ext = image_url.split(".")[-1].split("?")[0]
        filename = OUTPUT_DIR / f"image_{i}.{ext}"

        with open(filename, "wb") as f:
            f.write(img_response.content)
        print("Done")

    except Exception as e:
        print(f"Blad przy {image_url}: {e}")






