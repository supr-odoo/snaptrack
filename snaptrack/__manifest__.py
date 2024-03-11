{
    "name": "snaptrack",
    "application": True,
    "depends": ["base", "sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "views/booking_request_views.xml",
        "views/service_category_details.xml",
        "views/snaptrack_sales_views.xml",
        "views/snaptrack_menu.xml",
    ],
    "demo": ["demo/products.xml"],
    "installable": True,
}
