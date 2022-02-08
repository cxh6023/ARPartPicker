import csv

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def psa_handguard_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    handguard_url = "https://palmettostatearmory.com/ar-15/upper-parts/handguards-rails.html?stock_filter=Show+Only+In+Stock&product_list_mode=list"
    driver.maximize_window()
    driver.get(handguard_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = True
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    handguards = []
    for product in products:
        if "grip" not in product['title'].lower() and "mag" not in product['title'].lower():
            handguards.append(product)
    print("Successfully scraped " + str(
        len(handguards)) + " handguards from " + handguard_url)

    """
    for handguard in handguards:
        print("Title: " + handguard['title'])
        print("Image: " + handguard['image'])
        print("Link: " + handguard['link'])
        print("Price: " + handguard['price'])
        print("\n")
    """
    return handguards


def psa_gas_block_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    gas_block_url = "https://palmettostatearmory.com/ar-15/upper-parts/gas-blocks.html?product_list_mode=list&stock_filter=Show+Only+In+Stock"
    driver.maximize_window()
    driver.get(gas_block_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = True
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    gas_blocks = []
    for product in products:
        gas_blocks.append(product)
    print("Successfully scraped " + str(
        len(gas_blocks)) + " gas blocks from " + gas_block_url)

    """
    for gas_block in gas_blocks:
        print("Title: " + gas_block['title'])
        print("Image: " + gas_block['image'])
        print("Link: " + gas_block['link'])
        print("Price: " + gas_block['price'])
        print("\n")
    """
    return gas_blocks


def psa_gas_tube_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    gas_tube_url = "https://palmettostatearmory.com/ar-15/upper-parts/parts.html?product_list_mode=list"
    driver.maximize_window()
    driver.get(gas_tube_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = True
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    gas_tubes = []
    for product in products:
        if "gas tube" in product['title'].lower():
            gas_tubes.append(product)
    print("Successfully scraped " + str(
        len(gas_tubes)) + " gas tubes from " + gas_tube_url)

    """
    for gas_tube in gas_tubes:
        print("Title: " + gas_tube['title'])
        print("Image: " + gas_tube['image'])
        print("Link: " + gas_tube['link'])
        print("Price: " + gas_tube['price'])
        print("\n")
    """
    return gas_tubes


def psa_charging_handle_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    charging_handle_url = "https://palmettostatearmory.com/ar-15/upper-parts/charging-handles.html?product_list_mode=list&stock_filter=Show+Only+In+Stock"
    driver.maximize_window()
    driver.get(charging_handle_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = True

    charging_handles = []
    for product in products:
        if "latch" not in product['title'].lower():
            charging_handles.append(product)
    print("Successfully scraped " + str(
        len(charging_handles)) + " charging handles from " + charging_handle_url)

    """
    for charging_handle in charging_handles:
        print("Title: " + charging_handle['title'])
        print("Image: " + charging_handle['image'])
        print("Link: " + charging_handle['link'])
        print("Price: " + charging_handle['price'])
        print("\n")
    """
    return charging_handles


def psa_bcg_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    bcg_url = "https://palmettostatearmory.com/ar-15/upper-parts/bolt-carrier-groups.html?stock_filter=Show+Only+In+Stock&product_list_mode=list"
    driver.maximize_window()
    driver.get(bcg_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = True
        products[count]['charging_handle'] = False

    bcgs = []
    for product in products:
        if "bolt" in product['title'].lower() or "bcg" in product[
            'title'].lower():
            bcgs.append(product)
    print("Successfully scraped " + str(
        len(bcgs)) + " bcgs from " + bcg_url)

    """
    for bcg in bcgs:
        print("Title: " + bcg['title'])
        print("Image: " + bcg['image'])
        print("Link: " + bcg['link'])
        print("Price: " + bcg['price'])
        print("\n")
    """
    return bcgs


def psa_barrel_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    barrel_url = "https://palmettostatearmory.com/ar-15/upper-parts/barrels.html?product_list_mode=list&stock_filter=Show+Only+In+Stock"
    driver.maximize_window()
    driver.get(barrel_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = True
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    barrels = []
    for product in products:
        barrels.append(product)
    print("Successfully scraped " + str(
        len(barrels)) + " barrels from " + barrel_url)

    """
    for barrel in barrels:
        print("Title: " + barrel['title'])
        print("Image: " + barrel['image'])
        print("Link: " + barrel['link'])
        print("Price: " + barrel['price'])
        print("\n")
    """
    return barrels


def psa_stripped_upper_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    stripped_upper_url = "https://palmettostatearmory.com/ar-15/upper-parts/upper-receivers.html?product_list_mode=list&stock_filter=Show+Only+In+Stock"
    driver.maximize_window()
    driver.get(stripped_upper_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = True
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    stripped_uppers = []
    for product in products:
        if "kit" not in product['title'].lower() and "receiver" in product[
            'title'].lower():
            stripped_uppers.append(product)
    print("Successfully scraped " + str(
        len(stripped_uppers)) + " stripped uppers from " + stripped_upper_url)

    """
    for stripped_upper in stripped_uppers:
        print("Title: " + stripped_upper['title'])
        print("Image: " + stripped_upper['image'])
        print("Link: " + stripped_upper['link'])
        print("Price: " + stripped_upper['price'])
        print("\n")
    """
    return stripped_uppers


def psa_buffer_tube_assembly_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    buffer_tube_assembly_url = "https://palmettostatearmory.com/ar-15/lower-parts/individual-parts/buffered-tube-assembly-parts.html?product_list_mode=list"
    driver.maximize_window()
    driver.get(buffer_tube_assembly_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for count, item in enumerate(items):
        if count >= 3:
            break
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        if count >= 3:
            break
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = True
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    buffer_tube_assemblies = []
    for product in products:
        buffer_tube_assemblies.append(product)
    print("Successfully scraped " + str(
        len(buffer_tube_assemblies)) + " buffer tube assemblies " + buffer_tube_assembly_url)

    """
    for buffer_tube_assembly in buffer_tube_assemblies:
        print("Title: " + buffer_tube_assembly['title'])
        print("Image: " + buffer_tube_assembly['image'])
        print("Link: " + buffer_tube_assembly['link'])
        print("Price: " + buffer_tube_assembly['price'])
        print("\n")
    """
    return buffer_tube_assemblies

def psa_stripped_lower_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    stripped_lower_url = "https://palmettostatearmory.com/ar-15/lowers/stripped-lowers.html?product_list_mode=list"
    driver.maximize_window()
    driver.get(stripped_lower_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = True
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    stripped_lowers = []
    for product in products:
        stripped_lowers.append(product)
    print("Successfully scraped " + str(
        len(stripped_lowers)) + " stripped lowers from " + stripped_lower_url)

    """
    for stripped_lower in stripped_lowers:
        print("Title: " + stripped_lower['title'])
        print("Image: " + stripped_lower['image'])
        print("Link: " + stripped_lower['link'])
        print("Price: " + stripped_lower['price'])
        print("\n")
    """
    return stripped_lowers

def psa_trigger_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    trigger_url = "https://palmettostatearmory.com/ar-15/lower-parts/enhanced-triggers.html?product_list_mode=list"
    driver.maximize_window()
    driver.get(trigger_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = True
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    triggers = []
    for product in products:
        triggers.append(product)
    print("Successfully scraped " + str(
        len(triggers)) + " triggers from " + trigger_url)
    """
    for trigger in triggers:
        print("Title: " + trigger['title'])
        print("Image: " + trigger['image'])
        print("Link: " + trigger['link'])
        print("Price: " + trigger['price'])
        print("\n")
    """

    return triggers


def psa_stock_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    stock_url = "https://palmettostatearmory.com/ar-15/lower-parts" \
                      "/stocks.html?product_list_mode=list "
    driver.maximize_window()
    driver.get(stock_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = False
        products[count]['stripped_lower'] = False
        products[count]['stock'] = True
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False

    stocks = []
    for product in products:
        if "butt" not in product['title'].lower() and "stock" in product[
            'title'].lower():
            stocks.append(product)
    print("Successfully scraped " + str(
        len(stocks)) + " stocks from " + stock_url)

    """
    for stock in stocks:
        print("Title: " + stock['title'])
        print("Image: " + stock['image'])
        print("Link: " + stock['link'])
        print("Price: " + stock['price'])
        print("\n")
    """
    return stocks


def psa_pistol_grip_scraper():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\b1n4ry\PycharmProjects\chromedriver.exe")

    pistol_grip_url = "https://palmettostatearmory.com/ar-15/lower-parts" \
                      "/grips.html?product_list_mode=list "
    driver.maximize_window()
    driver.get(pistol_grip_url)

    time.sleep(5)

    content = driver.page_source.encode('utf-8').strip()

    soup = BeautifulSoup(content, "html.parser")
    items = soup.find_all("div", class_="inner-details")
    products = []
    for item in items:
        product = {
            'title': item.find('a', class_="product-item-link").text.strip(),
            'link': item.find('a', class_="product-item-link")['href'],
            'price': item.find('span', class_="price").text
        }
        products.append(product)

    items = soup.find_all('img', class_="product-image-photo")
    for count, item in enumerate(items):
        products[count]['image'] = item['src']
        products[count]['pistol_grip'] = True
        products[count]['stripped_lower'] = False
        products[count]['stock'] = False
        products[count]['buffer_tube_assembly'] = False
        products[count]['trigger'] = False
        products[count]['stripped_upper'] = False
        products[count]['barrel'] = False
        products[count]['handguard'] = False
        products[count]['gas_tube'] = False
        products[count]['gas_block'] = False
        products[count]['bolt_carrier_group'] = False
        products[count]['charging_handle'] = False


    pistol_grips = []
    for product in products:
        if "fore" not in product['title'].lower() and "vertical" not in product[
            'title'].lower():
            pistol_grips.append(product)
    print("Successfully scraped " + str(
        len(pistol_grips)) + " pistol grips from " + pistol_grip_url)

    """
    for pistol_grip in pistol_grips:
        print("Title: " + pistol_grip['title'])
        print("Image: " + pistol_grip['image'])
        print("Link: " + pistol_grip['link'])
        print("Price: " + pistol_grip['price'])
        print("\n")
    """
    return pistol_grips


def main():
    parts_list = []
    parts_list.append(psa_pistol_grip_scraper())
    parts_list.append(psa_stock_scraper())
    parts_list.append(psa_trigger_scraper())
    parts_list.append(psa_stripped_lower_scraper())
    parts_list.append(psa_buffer_tube_assembly_scraper())
    parts_list.append(psa_stripped_upper_scraper())
    parts_list.append(psa_barrel_scraper())
    parts_list.append(psa_charging_handle_scraper())
    parts_list.append(psa_gas_tube_scraper())
    parts_list.append(psa_gas_block_scraper())
    parts_list.append(psa_handguard_scraper())

    part_info = ['title', 'link', 'image', 'price', 'pistol_grip',
                 'stripped_lower', 'stock', 'buffer_tube_assembly', 'trigger',
                 'stripped_upper', 'barrel', 'handguard', 'gas_tube',
                 'gas_block', 'bolt_carrier_group', 'charging_handle']

    with open('parts_data.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=part_info)
        writer.writeheader()
        for part in parts_list:
            writer.writerows(part)

main()
