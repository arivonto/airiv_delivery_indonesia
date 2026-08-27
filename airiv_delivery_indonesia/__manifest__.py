# -*- coding: utf-8 -*-
{
    'name': 'Indonesia Shipping & Logistics Aggregator (Biteship, RajaOngkir, JNE, SiCepat, J&T, GoSend)',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Unified Indonesian Logistics & Instant Courier Engine (Biteship & RajaOngkir REST APIs)',
    'description': """
Unified Indonesian Shipping & Delivery Connector for Odoo 18 Community.
- Biteship API Integration (JNE, SiCepat, J&T, Anteraja, GoSend, GrabExpress, POS, Lion)
- RajaOngkir Integration (Starter, Basic, and PRO sub-district rate engine)
- Real-Time Shipping Cost Calculation & Volumetric Weight Conversion (Dimensi / 6000)
- Automated Tracking Number & Waybill (AWB / Resi) Synchronization
- Zero External Server Overhead - Direct REST API Client
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['delivery', 'stock', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_carrier_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
