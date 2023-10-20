import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

def scrape_rimi_price():
    url = "https://www.rimi.lv/e-veikals/en/products/alcoholic-beverages/beer/import-beer/alus-corona-extra-4-5-0-355l/p/1371038"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find(class_="price")

    if price_element:
        price_parts = []

        if soup.find(class_="price-badge__body"):
            price_element = soup.find(class_="price-badge__price")
            discount_card = True
        else:
            discount_card = False

        # Extract the price parts
        for part in price_element.select("span, sup, sub"):
            if part.string:
                price_parts.append(part.string)

        # Join the price parts and remove unwanted characters
        price = ''.join(price_parts).strip().replace('€', '').replace(',', '.')

        # Convert the price to cents and format it
        formatted_price = f"{float(price) / 100:.2f}"

        return formatted_price, discount_card, url
    else:
        return None, None, None


def scrape_barbora_price():
    url = "https://www.barbora.lv/produkti/alus-corona-extra-4-5-proc-355-ml-d"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find("span", class_="b-product-price-current-number")

    if price_element:
        price = price_element.string.strip()

        # Remove unwanted characters from the price string
        price = price.replace('€', '').replace(',', '.').strip()

        # Format the price
        formatted_price = f"{float(price):.2f}"

        return formatted_price, url
    else:
        return None, None


def scrape_alkoutlet_price():
    url = "https://alkoutlet.lv/alus-corona-extra-4-5.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".product-info-main .price")

    if price_element:
        price = price_element.string.strip()

        # Remove unwanted characters from the price string
        price = price.replace('€', '').replace(',', '.').strip()

        # Format the price
        formatted_price = f"{float(price):.2f}"

        return formatted_price, url
    else:
        return None, None


def scrape_cenuklubs_price():
    url = "https://cenuklubs.lv/alus-corona-extra-4-5-0-355l-ar-depoz-589477.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".price")

    if price_element:
        price = price_element.string.strip().replace('€', '')

        return price, url
    else:
        return None, None

def scrape_spiritsandwine_price():
    url = "https://www.spiritsandwine.lv/lv/alus/corona-extra-3136378/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".product-price-sale .actual")

    if price_element:
        price = price_element.string.strip().replace('€', '')

        return price, url
    else:
        return None, None


def scrape_lidl_price():
    url = "https://www.lidl.lv/lv/p/piedavajumi-no-pirmdienas-alus-extra/p22752"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".pricebox__price")

    if price_element:
        price = price_element.text.strip()

        # Remove unwanted characters from the price string
        price = price.replace('€', '').replace(',', '.').strip()


        formatted_price = f"{float(price):.2f}"

        return formatted_price, url
    else:
        return None, None



def scrape_androidcompare_price():
    url = "https://androidcompare.com/role-of-a-startup-cto/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".price")

    if price_element:
        price = price_element.string.strip()
        return price, url
    else:
        return None, None


def scrape_toplv_price():
    url = "https://etop.lv/index.php?route=product/product&product_id=160368&"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Check for the special price class first
    price_element = soup.select_one(".autocalc-product-special")

    # If not found, fall back to the regular price class
    if not price_element:
        price_element = soup.select_one(".autocalc-product-price")

    if price_element:
        price = price_element.text.strip()

        # Remove unwanted characters from the price string
        price = price.replace('€', '').replace(',', '.').strip()

        # Format the price
        formatted_price = f"{float(price):.2f}"

        return formatted_price, url
    else:
        return None, None


def scrape_superalko_price():
    url = "https://www.superalko.lv/product-detail/corona-beer-45-355-cl"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Check for the special price class first
    price_element = soup.select_one(".total_price")

    # If not found, fall back to the regular price class
    if not price_element:
        price_element = soup.select_one(".total_price")

    if price_element:
        price = price_element.text.strip()

        # Remove unwanted characters from the price string
        price = price.replace('€', '').replace(',', '.').strip()

        # Format the price
        formatted_price = f"{float(price):.2f}"

        return formatted_price, url
    else:
        return None, None



def scrape_lats_price():
    url = "https://www.e-latts.lv/alus-gaisais-corona-extra-4-5-0-355l.21799.p"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".SlideIfoBox .product_price.price")
    old_price_element = soup.select_one(".SlideIfoBox .OldPrice")

    if price_element:
        price = price_element.text.strip()
    else:
        price = None

    if old_price_element:
        old_price = old_price_element.text.strip()
    else:
        old_price = None

    return price, old_price, url


def scrape_vynoteka_price():
    url = "https://vynoteka.lv/en/corona-extra-alus-pud-0355l-45"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one(".main-section .product-price__current")

    if price_element:
        price_int = price_element.find(class_="product-price__int").get_text(strip=True)
        price_decimal = price_element.find(class_="product-price__decimal").get_text(strip=True)
        currency = price_element.find(class_="product-price__currency").get_text(strip=True)

        # Combine the integer and decimal parts of the price
        formatted_price = f"{price_int}.{price_decimal}"

        return formatted_price, url
    else:
        return None, None


@app.route('/')
def index():
    rimi_price, discount_card, rimi_url = scrape_rimi_price()
    barbora_price, barbora_url = scrape_barbora_price()
    alkoutlet_price, alkoutlet_url = scrape_alkoutlet_price()
    cenuklubs_price, cenuklubs_url = scrape_cenuklubs_price()
    superalko_price, superalko_url = scrape_superalko_price()
    toplv_price, toplv_url = scrape_toplv_price()
    lats_price, lats_old_price, lats_url = scrape_lats_price()
    vynoteka_price, vynoteka_url = scrape_vynoteka_price()
    spiritsandwine_price, spiritsandwine_url = scrape_spiritsandwine_price()
    lidl_price, lidl_url = scrape_lidl_price()

    return render_template(
        'index.html',
        rimi_price=rimi_price,
        rimi_url=rimi_url,
        barbora_price=barbora_price,
        barbora_url=barbora_url,
        alkoutlet_price=alkoutlet_price,
        alkoutlet_url=alkoutlet_url,
        cenuklubs_price=cenuklubs_price,
        cenuklubs_url=cenuklubs_url,
        superalko_price = superalko_price,
        superalko_url = superalko_url,
        toplv_price=toplv_price,
        toplv_url=toplv_url,
        lats_price=lats_price,
        lats_old_price=lats_old_price,
        lats_url=lats_url,
        vynoteka_price=vynoteka_price,
        vynoteka_url = vynoteka_url,
        lidl_price=lidl_price,
        lidl_url=lidl_url,
        spiritsandwine_price=spiritsandwine_price,
        spiritsandwine_url=spiritsandwine_url,
        discount_card=discount_card
    )

if __name__ == '__main__':
    app.run()
