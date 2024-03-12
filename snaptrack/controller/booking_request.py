from odoo import http
from odoo.http import request


class BookingRequestController(http.Controller):
    @http.route("/booking", type="http", auth="public", website=True, csrf=False)
    def booking_request_form(self, **post):
        if request.httprequest.method == "POST":
            # Extract data from the POST request
            description = post.get("description")
            customer_id = request.env.user.id
            request_details = post.get("request_details")
            preferred_date = post.get("preferred_date")

            # Create a new record in the snaptrack.booking.request model
            BookingRequest = request.env["snaptrack.booking.request"]
            booking_request_vals = {
                "description": description,
                "customer_id": customer_id,
                "request_details": request_details,
                "preferred_date": preferred_date,
            }
            booking_request = BookingRequest.create(booking_request_vals)
            print(customer_id)

            # Redirect to a confirmation page or any other page
            return request.redirect("/contactus-thank-you")

        # If the request method is not POST, render the form template

        customers = request.env["res.partner"].search([])

        product_categories = request.env["product.product"].search([])
        return http.request.render(
            "snaptrack.booking_request_form",
            {
                "customers": customers,
            },
        )
