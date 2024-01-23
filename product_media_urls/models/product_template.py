from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    media_url = fields.Char(string='Media URL')
    is_media_url_active = fields.Boolean(string='Active Media URL', default=True)

    @api.model
    def fetch_media_from_url(self):
        # Logic to fetch media from the media_url field
        # This method should be called by a scheduled action or manually
        for record in self:
            if record.is_media_url_active and record.media_url:
                # Implement fetching mechanism here
                # Placeholder for actual media fetching logic
                pass

    @api.model
    def display_fetched_media(self):
        # Logic to display fetched media on the website
        # This method can be used in the website's frontend to display the media
        pass

    @api.model
    def log_media_fetch_error(self, error):
        # Logic to log errors during media fetching
        # This method should create a log entry in a model designed for error logging
        self.env['product.media.url.error'].create({
            'product_template_id': self.id,
            'error_message': str(error),
        })

    @api.model
    def configure_media_urls(self, values):
        # Logic to configure media URLs in the backend
        # This method can be used in the configuration interface to set media URLs
        self.update(values)

    @api.constrains('media_url')
    def validate_media_url(self):
        # Logic to validate the media URL input
        # This method should ensure that the media URL is valid and reachable
        for record in self:
            if record.media_url:
                # Placeholder for actual URL validation logic
                pass

class ProductMediaUrlError(models.Model):
    _name = 'product.media.url.error'
    _description = 'Product Media URL Error Log'

    product_template_id = fields.Many2one('product.template', string='Product Template', required=True)
    error_message = fields.Text(string='Error Message', required=True)