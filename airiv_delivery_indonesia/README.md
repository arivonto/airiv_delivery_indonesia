# Indonesia Shipping & Logistics Aggregator (Biteship, RajaOngkir, Local Couriers)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Target: Indonesia Logistics](https://img.shields.io/badge/Market-Indonesia%20Couriers-green.svg)](https://airiv.id)

A high-performance, zero-overhead logistics and courier aggregator connector developed specifically for **Odoo 18.0 Community Edition**. Built to empower Indonesian e-commerce, distributors, and UMKM enterprises with automated real-time shipping rate lookups, sub-district accuracy, on-demand courier dispatching, and automated waybill (AWB / Resi) tracking.

---

## Detailed Features & Supported Courier Networks

### 1. Biteship Shipping Aggregator
* **Direct Multi-Courier Integration**: Real-time rate lookup and booking for **JNE** (REG, YES, JTR), **SiCepat** (SIUNT, BEST, GOKIL), **J&T Express** (EZ, J&T Super), **Anteraja**, **POS Indonesia**, **TIKI**, and **Lion Parcel**.
* **On-Demand & Same-Day Dispatch**: Instant motorcycle courier dispatch via **GoSend** (Instant & SameDay) and **GrabExpress**.
* **Automated Waybill & Resi Sync**: Fetches real-time airway bill numbers directly into Odoo stock pickings.
* **Volumetric Weight Standard**: Automatic conversion using the Indonesian national logistics formula:
  $$\text{Volumetric Weight (kg)} = \frac{\text{Length (cm)} \times \text{Width (cm)} \times \text{Height (cm)}}{6000}$$

### 2. RajaOngkir Tariff Engine
* **Coverage Across 38 Provinces**: Full database of Indonesian provinces, regencies/cities (*Kota/Kabupaten*), and sub-districts (*Kecamatan*).
* **Multi-Tier Compatibility**: Works across RajaOngkir Starter, Basic, and PRO account levels.
* **Domestic & International Rates**: Seamless calculations for regular domestic parcels and POS Indonesia EMS cross-border shipments.

---

## API Credential Acquisition Guide

### A. Biteship API Setup
1. Register or log in to the [Biteship Dashboard](https://dashboard.biteship.com/).
2. Navigate to **Developers > API Keys**.
3. Copy your **API Key** (`biteship_live_...` or `biteship_test_...`).
4. Look up your warehouse **Origin Area ID** (e.g., `IDNP6IDNC148IDND859IDZ15412` for South Tangerang / Jakarta area).

---

### B. RajaOngkir API Setup
1. Log in to the [RajaOngkir Portal](https://rajaongkir.com/).
2. Go to **Account Panel > API Key**.
3. Copy your **API Key**.
4. Retrieve your origin **City ID** or **Sub-district ID** from the RajaOngkir location directory.

---

## Installation & Odoo Configuration

1. **Deploy Module**:
   Place `airiv_delivery_indonesia` inside your Odoo `custom_addons` directory.

2. **Activate Module**:
   * Enable Developer Mode (`?debug=1`).
   * Go to **Apps > Update Apps List**.
   * Search for `Indonesia Shipping & Logistics Aggregator` and click **Activate**.

3. **Configure Delivery Carriers**:
   * Go to **Inventory > Configuration > Delivery > Shipping Methods** (or **Sales > Configuration > Shipping Methods**).
   * Create a new shipping method:
     * **Provider**: Select `Biteship Aggregator` or `RajaOngkir Engine`.
     * Under the dedicated settings tab, enter your **API Key** and **Origin Area ID**.
     * Select your desired courier rail (e.g., JNE, SiCepat, GoSend).
     * Click **Save**.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL client compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `delivery`, `stock`, `sale_management` |
| **Server Overhead** | Zero (direct asynchronous API calls, no third-party middleware) |
| **Locale & Standards** | Indonesian Rupiah (Rp), Grams / Kilograms, WIB (UTC+7) |
