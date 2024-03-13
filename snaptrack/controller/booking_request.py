from odoo import http
from odoo.http import request


class BookingRequestController(http.Controller):
    @http.route("/booking", type="http", auth="public", website=True, csrf=False)
    def booking_request_form(self, **post):
        if request.httprequest.method == "POST":
            # customer_id = request.env.user.id
            request_details = post.get("request_details")
            preferred_date = post.get("preferred_date")
            address = post.get("address")
            product_category_ids = [int(post.get("product_category_id"))]
            # print(customer_id)
            BookingRequest = request.env["snaptrack.booking.request"]
            booking_request_vals = {
                "request_details": request_details,
                # "customer_id": customer_id,
                "address": address,
                "preferred_date": preferred_date,
                "product_category_id": [(6, 0, product_category_ids)],
            }
            booking_request = BookingRequest.create(booking_request_vals)

            return request.redirect("/contactus-thank-you")

        # customers = request.env["res.users"].search([])
        product_categories = request.env["product.product"].search(
            [("name", "ilike", "photography")]
        )
        return http.request.render(
            "snaptrack.booking_request_form",
            {"product_categories": product_categories},
        )
