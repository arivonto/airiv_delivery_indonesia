# Indonesia Shipping & Logistics Aggregator (Biteship, RajaOngkir, Local Couriers)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Target: Indonesia Logistics](https://img.shields.io/badge/Market-Indonesia%20Couriers-green.svg)](https://airiv.id)

A complete, high-performance logistics and courier aggregator connector developed specifically for **Odoo 18.0 Community Edition**. Built to empower Indonesian e-commerce businesses, wholesale distributors, and UMKM enterprises with automated real-time shipping rate calculations, sub-district (*kecamatan*) precision, instant motorcycle courier dispatching, and automated waybill (*nomor resi*) tracking—all with **zero external server overhead** and native App Drawer integration.

---

## Detailed Features & Supported Courier Networks

### 1. Biteship Shipping Aggregator
* **Multi-Courier Real-Time Rates**: Dynamic pricing queries covering major Indonesian domestic logistics providers:
  * **JNE Express**: Regular (REG), Yakin Esok Sampai (YES), JNE Trucking / Cargo (JTR).
  * **SiCepat Ekspres**: SiUntung (Regular), Best (Next Day), Gokil (Cargo).
  * **J&T Express**: EZ (Standard Regular), J&T Super, J&T Cargo.
  * **Anteraja**: Regular, Next Day, Same Day, Cargo.
  * **POS Indonesia**: Pos Reguler, Pos Next Day, Pos Kilat Khusus, EMS Internasional.
  * **TIKI**: Regular (REG), Over Night Service (ONS), Trucking Service (TRC).
  * **Lion Parcel**: ONEPACK, REGPACK, JAGOPACK, BIGPACK.
* **On-Demand & Instant Motorcycle Dispatch**: Real-time integration with **GoSend** (Instant & SameDay) and **GrabExpress** for local same-day parcel deliveries with automated driver pickup coordination.
* **Automatic Waybill & Resi Synchronization**: Generates and syncs official carrier tracking numbers (AWB / Resi) directly to Odoo delivery orders (`stock.picking`).
* **Thermal Shipping Label Retrieval**: Fetch direct thermal print URLs (`80mm` and `100x150mm` sticker labels) directly from the delivery interface.

### 2. RajaOngkir Tariff Engine
* **Complete 38-Province Geographical Database**: Supports destination lookups down to Province (*Provinsi*), City/Regency (*Kota/Kabupaten*), and Sub-District (*Kecamatan*).
* **Multi-Tier Compatibility**: Fully supports RajaOngkir Starter, Basic, and PRO account configurations.
* **Cross-Border Postal Calculations**: International shipping tariff lookups via POS Indonesia EMS and international express partners.

### 3. Volumetric Weight Calculation Standard
Automated calculation matching the Indonesian logistics standard:

$$\text{Volumetric Weight (kg)} = \frac{\text{Length (cm)} \times \text{Width (cm)} \times \text{Height (cm)}}{6000}$$

The system automatically compares physical weight against dimensional weight and submits the chargeable weight to courier pricing APIs.

---

## API Credential Acquisition Guide

### A. Biteship Setup (Sandbox & Production)
1. Register or log in to the [Biteship Merchant Dashboard](https://dashboard.biteship.com/).
2. Navigate to **Developers > API Keys** in the sidebar.
3. Copy your API Key:
   * **Sandbox Key**: e.g., `biteship_test.eyJhbGciOi...`
   * **Production Key**: e.g., `biteship_live.eyJhbGciOi...`
4. Retrieve your warehouse **Origin Area ID**:
   * Go to **Locations > Warehouse / Origin Address**.
   * Copy the 10-digit Area ID code (e.g., `IDNP6IDNC148IDND859IDZ15412` for South Tangerang / Jakarta area).
5. (Optional) In **Webhooks**, set the Tracking Notification endpoint to: `https://your-domain.com/delivery/biteship/webhook`.

---

### B. RajaOngkir Setup (Starter, Basic, PRO)
1. Log in to the [RajaOngkir Portal](https://rajaongkir.com/).
2. Go to **Account Panel > API Key**.
3. Copy your **API Key** (e.g., `a1b2c3d4e5f67890abcdef1234567890`).
4. Select your account tier (**Starter**, **Basic**, or **PRO**) based on your subscription.
5. Retrieve your origin **City ID** (Starter/Basic) or **Sub-district ID** (PRO) from the location reference list.

---

## Installation & Odoo Configuration

1. **Deploy Module Files**:
   Ensure `airiv_delivery_indonesia` is placed in your Odoo `custom_addons` directory.

2. **Activate Module**:
   * Enable Developer Mode (`?debug=1`).
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia Shipping & Logistics Aggregator` and click **Activate**.

3. **Access via App Drawer**:
   * Click the top-left **9-dot App Switcher** (App Drawer).
   * Open the **Indonesian Logistics** application.

4. **Configure Shipping Methods**:
   * Navigate to **Operations > Courier Services**.
   * Create or select a carrier service (e.g., *Biteship - JNE Regular*, *Biteship - SiCepat*, *RajaOngkir - J&T*).
   * Under the **Biteship Aggregator** or **RajaOngkir Engine** tab, paste your API Key and Origin Area ID.
   * Select your courier code and service tier filter.
   * Click **Save**.

5. **Sales Orders & Outgoing Deliveries**:
   * When creating a Sales Quotation, click **Add Shipping** to fetch live courier rates.
   * Confirm the sale order; when validating the Delivery Order in **Operations > Waybills & Shipments (Resi)**, the tracking waybill number and label link are generated automatically.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL client & App Drawer compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `delivery`, `stock`, `sale_management` |
| **Server Overhead** | Zero (direct asynchronous API calls, no relay servers) |
| **Volumetric Divisor** | Standard 6,000 (air/land freight) |
| **Localization Standard** | Indonesian Rupiah (Rp), Grams / Kilograms, WIB (UTC+7) |
