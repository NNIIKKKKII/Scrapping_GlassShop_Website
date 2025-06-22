
# 👓 GlassesShop Web Scraper

This Scrapy spider extracts product details from the [GlassesShop](https://www.glassesshop.com/bestsellers) website. It collects data such as product name, price, and image link from the Bestsellers page and follows pagination to scrape multiple pages.

---

## 📦 Features

- Scrapes product name, price, and image URL
- Follows pagination across all bestsellers pages
- Saves data in structured format (e.g., JSON, CSV)
- Built using Scrapy, a fast and powerful web scraping framework

---

## 📁 Project Structure

```
glasses_scraper/
│
├── glasses_scraper/
│   ├── spiders/
│   │   └── glasses.py       # Main spider script
│   ├── __init__.py
│   └── settings.py
├── scrapy.cfg
└── README.md
```

---

## 🧠 Scraped Data Fields

Each product will contain:

- `Product_Name`: Name of the product
- `Product_Price`: Price of the product
- `Product_img_link`: Link to the product image

---

## 🚀 How to Run

1. **Install Scrapy** (if not already installed):

   ```bash
   pip install scrapy
   ```

2. **Navigate to your project folder**:

   ```bash
   cd glasses_scraper
   ```

3. **Run the spider**:

   To export data to a JSON file:

   ```bash
   scrapy crawl Glasses -o products_Dataset.json
   ```

   Or export to CSV:

   ```bash
   scrapy crawl Glasses -o products_Dataset.csv
   ```

---


## ⚠️ Disclaimer

This project is for educational purposes only. Ensure you follow [GlassesShop's Terms of Service](https://www.glassesshop.com/terms) before using this scraper extensively. Use responsibly and respect site limitations.

---

## 👨‍💻 Author

- **Nikhil Pareeshwad**
- Tech Stack: Python, Scrapy, Data Engineering Tools

---

## 📬 Contact

Feel free to reach out for collaboration or feedback!
