from odoo import http
from odoo.http import request

class ProductMediaController(http.Controller):

    @http.route(['/product/media/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product_media(self, product, **kwargs):
        media_url = product.media_url
        if not media_url:
            return request.render('product_media_urls.product_media_not_found', {})
        
        try:
            response = http.request.render('product_media_urls.product_media_display', {
                'product': product,
                'media_url': media_url,
            })
            return response
        except Exception as e:
            error_message = str(e)
            request.env['product.template'].sudo().message_post(
                body=error_message,
                subtype='product_media_urls.mt_media_url_fetch_error'
            )
            return request.render('product_media_urls.product_media_error', {
                'error_message': error_message,
            })