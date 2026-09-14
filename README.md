# Indonesia Shipping & Logistics Aggregator (Biteship, RajaOngkir, JNE, SiCepat, J&T, GoSend)

Unified Indonesian Logistics & Instant Courier Engine (Biteship & RajaOngkir REST APIs)

## Odoo Apps Store

This repository contains the Odoo 18 module package for `airiv_delivery_indonesia`.

Required store assets are maintained in:

```text
airiv_delivery_indonesia/static/description/
  icon.png
  banner.png
  index.html
```

## Technical

- Odoo version: `18.0.1.0.0`
- License: `LGPL-3`
- Author: `AIRIV`
- Website: `https://airiv.id`

## Quality Gate

GitHub Actions runs the AIRIV Odoo Apps Store CI audit on branch `18.0`.

## Core Capabilities & Architecture

- Shipment planning from sales and inventory context.
- Carrier, service, package, delivery zone, and dispatch coordination.
- Milestone, exception, proof-of-delivery, and customer follow-up visibility.

The workflow connects native Odoo orders, stock operations, partners, and addresses to an AIRIV delivery planning and operations review layer.

## Feature & Workflow Automation

1. Configure warehouses, carriers, services, zones, and operators.
2. Verify address, package, and source stock operation.
3. Assign carrier, create shipment reference, and record dispatch.
4. Update milestones, exceptions, delivery status, and follow-up ownership.

## Installation Guidance

Clone branch `18.0` into the Odoo addons path, restart Odoo, update the Apps list, and install the module. Configure logistics context before dispatching operational records.

## Configuration Checklist

- Verify address, contact, delivery zone, and service.
- Confirm source operation and package availability.
- Assign carrier, service, and shipment reference.
- Record delay or failed delivery exceptions with an owner.

## Repository Layout

```text
airiv_delivery_indonesia/
  models/                 Delivery and shipment models
  views/                  Operational views and menus
  security/               Access rules
  static/description/     Apps Store assets
  __manifest__.py         Odoo metadata
```

## Contact Info

- Author: AIRIV
- Website: https://airiv.id
- GitHub: https://github.com/arivonto
- Repository: https://github.com/arivonto/airiv_delivery_indonesia
- Odoo series: `18.0`
