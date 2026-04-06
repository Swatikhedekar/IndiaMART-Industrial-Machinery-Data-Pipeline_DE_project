from matplotlib import text
from playwright.sync_api import sync_playwright
import json
import time

URL = "https://dir.indiamart.com/impcat/industrial-machinery.html"


def scrape_indiamart():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        # Set user agent (better stability)
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

        print("Opening IndiaMART...")
        page.goto(URL, timeout=60000)

        # Wait for full load
        page.wait_for_load_state("networkidle")

        # Scroll to load all products
        for _ in range(5):
            page.mouse.wheel(0, 5000)
            time.sleep(2)

        # Select all product containers
        products = page.locator("main ul > li")

        count = products.count()
        print(f"Total products found: {count}")

        for i in range(count):
            product = products.nth(i)

            try:
                # PRODUCT NAME
                name = product.locator("a.template7-product-name").inner_text(timeout=3000)

                # PRICE
                price = None
                try:
                    price = product.locator("span.template7-product-price").inner_text(timeout=2000)
                except:
                    pass

                # SUPPLIER
                supplier = None
                try:
                    supplier = product.locator("a.template7-seller-name").inner_text(timeout=2000)
                except:
                    pass

                # address (fallback using span index)
                address = None
                
                try:
                    address = product.locator("address span").inner_text().strip()

                except:
                    pass
                # RATING
                rating = None
                try:
                    rating = product.locator("span.b").inner_text(timeout=2000)
                except:
                    pass

                results.append({
                    "product_name": name,
                    "price": price,
                    "supplier": supplier,
                    "address": address,
                    "rating": rating
                })

            except Exception as e:
                print("Error:", e)
                continue

        browser.close()

    return results


def main():
    data = scrape_indiamart()

    # Save JSON
    with open("data/indiamart_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Saved {len(data)} records to JSON")


if __name__ == "__main__":
    main()