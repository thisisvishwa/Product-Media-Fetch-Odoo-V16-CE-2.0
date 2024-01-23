odoo.define('product_media_urls.ProductMediaURLWidget', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var _t = core._t;

    publicWidget.registry.ProductMediaURLWidget = publicWidget.Widget.extend({
        selector: '.oe_product_media_url',
        events: {
            'error .product-media-url-img': '_onImageError',
        },

        /**
         * @override
         */
        start: function () {
            var self = this;
            this._super.apply(this, arguments);
            this._fetchAndDisplayMedia();
            return $.when();
        },

        /**
         * Fetch media from the configured URL and display it.
         * @private
         */
        _fetchAndDisplayMedia: function () {
            var self = this;
            var $mediaDisplayArea = this.$el.find('.media_display_area');
            var mediaURL = this.$el.data('media-url');

            if (mediaURL) {
                $('<img/>', {
                    class: 'product-media-url-img',
                    src: mediaURL,
                    error: function () {
                        self._onImageError();
                    }
                }).appendTo($mediaDisplayArea);
            }
        },

        /**
         * Handle image loading errors.
         * @private
         */
        _onImageError: function () {
            var $errorLogContainer = this.$el.find('.error_log_container');
            $errorLogContainer.text(_t('Failed to load media from URL.'));
            $errorLogContainer.addClass('product-media-url-error');
        },
    });

    return {
        ProductMediaURLWidget: publicWidget.registry.ProductMediaURLWidget,
    };
});