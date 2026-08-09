# 🛒 Daraz Automation Testing Framework

A Selenium-based Test Automation Framework for Daraz Bangladesh built using **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

---

## 🚀 Technologies Used

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Reports
- Logging
- ChromeDriver

---

## 📂 Project Structure

```
Daraz_Automation/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── cart_page.py
│
├── screenshots/
│
├── testcases/
│   ├── test_login.py
│   ├── test_search_1.py
│   ├── test_search_2.py
│   ├── test_search_3.py
│   ├── test_product_price.py
│   ├── test_cart.py
│   └── test_config_setup.py
│
├── test_data/
│
├── utilities/
│   ├── logger.py
│   ├── read_properties.py
│   └── excel_utils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# ✅ Automated Test Scenarios

### 🔹 Login Test

- Open Daraz
- Click Login
- Enter Email & Password
- Click Login Button
- Capture Screenshot

---

### 🔹 Search Product Test

- Search Product
- Open First Product
- Capture Product Title
- Capture Product Price
- Capture Product URL

---

### 🔹 Product Price Test

- Search Product
- Open Product
- Verify Product Price
- Capture Screenshot

---

### 🔹 Add To Cart Test

- Search Product
- Open Product
- Add Product to Cart
- Capture Screenshot

---

# 📸 Screenshots

Screenshots are automatically saved inside:

```
screenshots/
```

Example:

```
login_result.png
search_result.png
product.png
product_price.png
cart.png
```

---

# 📊 HTML Report

Generate Report

```bash
pytest --html=reports/report.html
```

Open

```
reports/report.html
```

---

# ▶️ Run Tests

Run all tests in order:

```bash
python -m pytest -v
```

Run the login test:

```bash
python -m pytest testcases/test_login.py -v
```

Run search product 1:

```bash
python -m pytest testcases/test_search_1.py -v
```

Run the product price test:

```bash
python -m pytest testcases/test_product_price.py -v
```

Run the cart test:

```bash
python -m pytest testcases/test_cart.py -v
```

Run search product 2:

```bash
python -m pytest testcases/test_search_2.py -v
```

Run search product 3:

```bash
python -m pytest testcases/test_search_3.py -v
```

Run tests quietly:

```bash
python -m pytest -q
```

---

# 📋 Current Features

- ✅ Page Object Model (POM)
- ✅ Selenium WebDriver
- ✅ Pytest Framework
- ✅ HTML Report
- ✅ Logging
- ✅ Screenshot Capture
- ✅ Product Search
- ✅ Product Price Verification
- ✅ Login Automation
- ✅ Add to Cart Automation

---

# 📈 Test Result

Example test run:

```bash
python -m pytest -q
```

Current suite includes:

- ✔ Login test
- ✔ Search product 1
- ✔ Product price test
- ✔ Cart test
- ✔ Search product 2
- ✔ Search product 3
- ✔ Config loader check

---

# 🔮 Future Improvements

- Data Driven Testing (Excel)
- Cross Browser Testing
- Headless Execution
- GitHub Actions CI/CD
- Docker Support
- Allure Report

---

# Author

**Saif Al Saad**

Software Engineering Student

Daffodil International University

Major: Software Quality Assurance & Testing (SQAT)


---

⭐ If you found this project useful, don't forget to Star this repository.