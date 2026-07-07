# Drug Traceability System

A blockchain-based drug traceability platform built with **Django**, **Solidity**, and **Ethereum (Ganache)**. The system provides end-to-end tracking of pharmaceutical products — from manufacturers, through pharmacies, to end users — with immutable on-chain records to combat counterfeit drugs and ensure supply chain transparency.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Database Configuration](#-database-configuration)
- [Running the Application](#-running-the-application)
- [Blockchain Setup (Ganache)](#-blockchain-setup-ganache)
- [Smart Contract](#-smart-contract)
- [Application Modules](#-application-modules)
- [URL Routes](#-url-routes)
- [Data Models](#-data-models)
- [Screenshots / Templates](#-screenshots--templates)
- [Project Walkthrough](#-project-walkthrough)
- [Security Notes](#-security-notes)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## 🔍 Overview

Counterfeit drugs are a global problem. This project leverages **Ethereum blockchain** technology to provide a tamper-proof, decentralized ledger for tracking drugs across the pharmaceutical supply chain.

The system supports **four user roles**:
1. **Admin** — manages manufacturer approvals
2. **Manufacturer** — registers drugs, manages stock
3. **Pharmacy** — purchases from manufacturers, sells to end users
4. **User (Customer)** — purchases drugs and views transaction history

Every drug addition and transaction is logged both in the **MySQL database** (for fast querying) and the **Ethereum blockchain** (for immutability and auditability).

---

## ✨ Features

### Admin
- Secure login
- View all registered manufacturers
- Approve or reject manufacturer registrations

### Manufacturer
- Sign up and log in
- Add new drugs (name, type, uses, instructions, cost, MRP, stock)
- View drug catalog
- Add stock for existing drugs
- View current stock levels

### Pharmacy
- Sign up and log in
- Browse manufacturer drug catalogs
- Add drugs to cart and place orders (purchase stock from manufacturers)
- View purchased stock
- View inventory available for customers

### User (End Customer)
- Sign up and log in
- Browse pharmacies and view available drugs
- Add drugs to cart and place orders
- View purchase history
- View order details (with blockchain-verified records)

### Blockchain
- All drug data is hashed/recorded to the Ethereum blockchain via a Solidity smart contract
- Provides immutable proof of every drug addition and transfer
- Connected to a local **Ganache** Ethereum blockchain for development

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend Framework | Django 4.x |
| Frontend | HTML5, CSS3, JavaScript (Django Templates) |
| Database | MySQL |
| Blockchain | Ethereum (Solidity 0.8.0) |
| Local Blockchain | Ganache (CLI or GUI) |
| Web3 Library | Web3.py (Python) |
| Solidity Compiler | py-solc-x |
| Async Support | aiohttp, aiohappyeyeballs |
| ASGI Server | Daphne / Uvicorn-compatible |

---

## 📂 Project Structure

```
DrugTrace/
│
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── BlockChain.py                # Standalone blockchain test script
├── check_ganache.py             # Utility to check if Ganache is running
│
├── contracts/
│   └── DataStorage.sol          # Solidity smart contract
│
├── DrugTrace/                   # Main Django project package
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Root URL configuration
│   ├── asgi.py                  # ASGI configuration
│   └── wsgi.py                  # WSGI configuration
│
├── webapp/                      # Main Django app
│   ├── __init__.py
│   ├── admin.py                 # Django admin registration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # App URL configuration
│   ├── BlockChain.py            # Blockchain helper used by views
│   ├── tests.py                 # Unit tests
│   │
│   ├── migrations/              # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── static/                  # Static assets
│   │   ├── css/
│   │   ├── js/
│   │   ├── fonts/
│   │   └── images/
│   │
│   └── templates/               # HTML templates
│       ├── base.html
│       ├── a_base.html
│       ├── m_base.html
│       ├── p_base.html
│       ├── u_base.html
│       ├── index.html
│       ├── admin.html
│       ├── adminhome.html
│       ├── manufacturer.html
│       ├── pharmacies.html
│       ├── user.html
│       ├── userhome.html
│       ├── m_home.html
│       ├── p_home.html
│       ├── adddrug.html
│       ├── viewdrug.html
│       ├── viewstock.html
│       ├── pviewdrug.html
│       ├── pviewstocks.html
│       ├── uviewdrug.html
│       ├── u_view.html
│       ├── viewmanufacturers.html
│       ├── viewcart_p.html
│       ├── viewcart_u.html
│       ├── pay.html
│       └── pay2.html
│
└── .venv/                       # Virtual environment (not committed)
```

---

## ✅ Prerequisites

Before running this project, make sure you have the following installed:

1. **Python 3.9+**
2. **pip** (Python package manager)
3. **MySQL Server** (5.7+ or 8.0+)
4. **Node.js & npm** (for Ganache)
5. **Ganache** — Install via npm:
   ```bash
   npm install -g ganache
   ```
   Or download the Ganache GUI from [Truffle Suite](https://trufflesuite.com/ganache/).

6. **Git** (optional, for cloning)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd DrugTrace
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **Linux/Mac:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `py-solc-x` library will download the Solidity compiler (0.8.0) automatically on first run.

---

## 🗄 Database Configuration

The project uses **MySQL**. Configure it in `DrugTrace/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DrugTrace',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Steps:

1. Start MySQL server.
2. Create the database:
   ```sql
   CREATE DATABASE DrugTrace;
   ```
3. Update `USER` and `PASSWORD` in `settings.py` to match your MySQL credentials.
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. (Optional) Create a superuser for the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

---

## ▶ Running the Application

### Start the Django Development Server

```bash
python manage.py runserver
```

The application will be available at:
```
http://127.0.0.1:8000/
```

---

## ⛓ Blockchain Setup (Ganache)

Ganache provides a local Ethereum blockchain for development and testing.

### Option A: Ganache GUI
1. Open Ganache.
2. Click **"Quickstart"** to create a workspace.
3. Note the **RPC Server** URL (default: `http://127.0.0.1:7545`).
4. Note one of the **account addresses** and its **private key**.

### Option B: Ganache CLI
```bash
ganache --port 7545
```

### Update the Project's Blockchain Config

In `webapp/BlockChain.py` (and `BlockChain.py`), update:

```python
ganache_url = "http://127.0.0.1:7545"     # Ganache RPC URL
account_1   = "0xYourAccountAddress..."    # Ganache account address
private_key = "0xYourPrivateKey..."        # Ganache account private key
```

### Check Ganache Connection

```bash
python check_ganache.py
```

Expected output if running:
```
Port 7545 is open - Ganache appears to be running
```

### Test the Smart Contract

```bash
python BlockChain.py
```

This will:
1. Compile `contracts/DataStorage.sol`
2. Deploy the contract to Ganache
3. Add sample data (`"1"`, `"2"`, `"3"`) under the key `sajid24x7@gmail.com`
4. Retrieve and print the data

Expected output:
```
Retrieved Data: ['1', '2', '3']
```

---

## 📜 Smart Contract

The Solidity contract (`contracts/DataStorage.sol`) is intentionally minimal — a generic key-value store for traceability data:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorage {
    mapping(string => string[]) data;

    function addData(string memory key, string memory value) public {
        data[key].push(value);
    }

    function getData(string memory key) public view returns (string[] memory) {
        return data[key];
    }
}
```

- **`addData(key, value)`** — appends `value` to the array stored under `key`.
- **`getData(key)`** — returns the full array of values for `key` (read-only).

In this project, the contract is used to anchor drug-batch and transaction events. Each user/email acts as a `key`, and each event (drug added, stock updated, purchase) is appended as a `value`.

---

## 🧩 Application Modules

The `webapp` Django app implements the four user roles. Each role has its own base template for a consistent UI:

| Role | Base Template | Index Page |
|---|---|---|
| Admin | `a_base.html` | `adminhome.html` |
| Manufacturer | `m_base.html` | `m_home.html` |
| Pharmacy | `p_base.html` | `p_home.html` |
| User | `u_base.html` | `userhome.html` |

---

## 🌐 URL Routes

All app routes are namespaced under `/` (root).

### Common
- `/` — `homepage` (landing page)

### Admin (`a_base`)
- `/adminlogin/` — Admin login page
- `/adminloginaction/` — Admin login handler
- `/adminhome/` — Admin dashboard
- `/adminlogout/` — Admin logout
- `/viewmanufacturers/` — View all manufacturers
- `/acceptor/` — Approve/Reject manufacturer

### User / Customer (`u_base`)
- `/user/` — User login page
- `/usignupaction/` — User signup handler
- `/userloginaction/` — User login handler
- `/userlogout/` — User logout
- `/userhome/` — User dashboard
- `/viewprofile/` — View profile
- `/u_viewdrug/` — Browse drugs
- `/addtocart_u/` — Add to cart
- `/uviewcart/` — View cart
- `/payment_u/` — Process payment
- `/view_u/` — View order

### Manufacturer (`m_base`)
- `/manufacturer/` — Manufacturer login
- `/msignupaction/` — Manufacturer signup
- `/mloginaction/` — Manufacturer login
- `/mhome/` — Manufacturer dashboard
- `/mlogout/` — Logout
- `/adddrug/` — Add new drug
- `/viewdrug/` — View drug catalog
- `/viewstock/` — View stock
- `/addstock/` — Add stock

### Pharmacy (`p_base`)
- `/pharmacy/` — Pharmacy login
- `/psignupaction/` — Pharmacy signup
- `/ploginaction/` — Pharmacy login
- `/plogout/` — Logout
- `/p_home/` — Pharmacy dashboard
- `/pviewdrugs/` — View available drugs
- `/addtocart_p/` — Add to cart (purchase from manufacturer)
- `/pviewcart/` — View pharmacy cart
- `/payment_p/` — Process payment
- `/pviewstocks/` — View owned stock

### Django Admin
- `/admin/` — Built-in Django admin (requires superuser)

---

## 🗃 Data Models

Defined in `webapp/models.py`:

### `users`
Customer accounts
- `name`, `email`, `pass_word`, `phone`, `city`, `gender`

### `manufacturers`
Drug manufacturer accounts (admin-approved)
- `name`, `email`, `pass_word`, `city`, `address`, `stz` (state)

### `pharmacies`
Pharmacy accounts
- `name`, `email`, `pass_word`, `city`, `address`, `phone`

### `drug`
Drug catalog (one row per drug-batch)
- `did` (drug ID, primary key), `drugname`, `mname` (manufacturer), `typ_e`, `uses`, `instructions`, `cost`, `mrp`, `cname` (company), `cemail` (company email), `stock`

### `drugstock_p`
Stock owned by a pharmacy (purchased from a manufacturer)
- `did`, `drugname`, `mname`, `typ_e`, `uses`, `instructions`, `cost`, `mrp`, `pname` (pharmacy name), `pemail`, `stock`

### `cart_p`
Pharmacy shopping cart (orders placed with manufacturers)
- `did`, `mname`, `totcost`, `count`, `pemail`

### `cart_u`
End-user shopping cart (orders placed with pharmacies)
- `did`, `drugname`, `mname`, `cost`, `totcost`, `count`, `pharmacy`, `pemail`, `email`, `stz`

---

## 🖼 Screenshots / Templates

The frontend uses Django templates with static CSS/JS. Key templates include:

- `index.html` — Landing page (links to all four role logins)
- `admin.html`, `adminhome.html` — Admin login & dashboard
- `manufacturer.html`, `m_home.html` — Manufacturer login & dashboard
- `pharmacies.html`, `p_home.html` — Pharmacy login & dashboard
- `user.html`, `userhome.html` — Customer login & dashboard
- `adddrug.html` — Form to add a new drug
- `viewdrug.html`, `viewstock.html` — Manufacturer drug & stock views
- `pviewdrug.html`, `pviewstocks.html` — Pharmacy drug & stock views
- `uviewdrug.html`, `u_view.html` — Customer drug & order views
- `viewcart_p.html`, `viewcart_u.html` — Cart views
- `pay.html`, `pay2.html` — Payment pages

> Drop screenshots into the repo and reference them here with `![Alt](static/images/screenshot.png)` for richer documentation.

---

## 🔁 Project Walkthrough

1. **Admin** signs in (default credentials need to be created manually in DB or via the Django shell) and approves **manufacturers**.
2. A **manufacturer** signs up, logs in, and adds drugs to the catalog. Each addition is recorded to the blockchain.
3. A **pharmacy** signs up, logs in, browses manufacturer catalogs, and purchases drugs (adding them to its stock).
4. A **user** signs up, browses pharmacies, and orders drugs.
5. Every step writes to both **MySQL** (for queries) and **Ethereum** (via the `DataStorage` contract) for immutable traceability.

---

## 🔐 Security Notes

> ⚠️ This is a **development / academic project**, **not production-ready**.

- `SECRET_KEY` in `settings.py` is hardcoded — change it for any non-local use.
- `DEBUG = True` — disable in production.
- `ALLOWED_HOSTS = []` — set explicitly in production.
- `account_1` and `private_key` are checked into the repo — **never** commit real keys.
- MySQL credentials are in plaintext — use environment variables.
- Passwords are stored in plaintext (`pass_word` field) — hash them with Django's `make_password` before any real deployment.
- No CSRF exemption is configured for blockchain calls — review the views carefully.

**Recommended before production:**
- Use environment variables for `SECRET_KEY`, DB credentials, and blockchain keys (e.g., `python-decouple` or `django-environ`).
- Enable HTTPS and set `SECURE_*` flags.
- Hash all passwords using Django's auth system.
- Switch from Ganache to a permissioned Ethereum network (e.g., Quorum, Besu).
- Add proper authentication & role-based access control.

---

## 🛠 Troubleshooting

| Issue | Solution |
|---|---|
| `Failed to connect to Ganache` | Ensure Ganache is running on port 7545. Run `python check_ganache.py`. |
| `solcx` install error | `py-solc-x` downloads Solidity 0.8.0 on first compile. Ensure internet access or pre-install. |
| `Access denied for user 'root'@'localhost'` | Update `USER` and `PASSWORD` in `DrugTrace/settings.py`. |
| `No module named web3` | Activate the virtual environment and run `pip install -r requirements.txt`. |
| `mysqlclient` install fails on Windows | Install Microsoft C++ Build Tools, or use `pip install mysqlclient` from an elevated prompt. |
| Migrations not applied | Run `python manage.py makemigrations webapp && python manage.py migrate`. |
| `ValueError: not enough values to unpack` from web3 | Update to `web3.to_wei` (used in `webapp/BlockChain.py`); the root `BlockChain.py` uses the older `toWei`. |

---

## 🚧 Future Enhancements

- QR-code generation for each drug-batch for physical scanning
- IPFS integration to store large drug documents off-chain with on-chain hashes
- Role-based access control (RBAC) and JWT authentication
- REST API (Django REST Framework) for mobile clients
- Migration to a public/permissioned testnet (e.g., Sepolia, Polygon Mumbai)
- Drug expiry tracking and automated recall
- Real-time notifications for stock-outs and suspicious activity
- Multi-language support

---

## 📄 License

This project is intended for **educational / academic** purposes. Add an explicit license (e.g., MIT, Apache 2.0) if you plan to open-source it.

---

## 👥 Author / Maintainer

**Ganesh Areti** — initial work.

For questions or contributions, please open an issue or submit a pull request.

---

<p align="center">
  <em>Building a transparent, tamper-proof pharmaceutical supply chain — one block at a time.</em>
</p>
