# Product Media via URL's Module Configuration Guide

## Table of Contents

1. Introduction
2. Prerequisites
3. Configuration Steps
   1. Accessing the Configuration Menu
   2. Setting Up Media URLs
   3. Activating Media URL Fetching
   4. Error Logging and Display
4. Advanced Configuration
5. Conclusion

## 1. Introduction

This guide provides step-by-step instructions on how to configure the Product Media via URL's Module for Odoo Version 16 Community Edition. The module allows for dynamic fetching of product images and additional media from external URLs to be displayed on your website.

## 2. Prerequisites

Before you begin the configuration process, ensure that you have:

- Installed the Product Media via URL's Module. Refer to the `installation_guide.md` for instructions.
- Administrative access to your Odoo instance.

## 3. Configuration Steps

### 3.1 Accessing the Configuration Menu

To configure the Product Media via URL's Module:

1. Log in to your Odoo backend with administrative credentials.
2. Navigate to the `Apps` menu and search for `product_media_urls`.
3. Open the module to access the configuration settings.

### 3.2 Setting Up Media URLs

To set up media URLs for your products:

1. Go to the `Sales` menu, then click on `Products`.
2. Select a product to edit or create a new product.
3. Scroll down to the `Media URLs` section.
4. In the `media_url_input` field, enter the external URL where the product image or media is hosted.
5. Save your changes.

### 3.3 Activating Media URL Fetching

To activate media URL fetching for a product:

1. Follow the steps in 3.2 to access the `Media URLs` section of a product.
2. Locate the `is_media_url_active` checkbox.
3. Check the box to activate media URL fetching for the product.
4. Save your changes.

### 3.4 Error Logging and Display

If there is an error during media fetching:

1. Navigate to the `Settings` menu within the `product_media_urls` module.
2. Click on the `Error Log` submenu.
3. Review the error messages in the `error_log_container` to diagnose and resolve issues.

## 4. Advanced Configuration

For advanced configurations such as setting up scheduled jobs for media fetching, refer to the `ir_cron_data.xml` file and modify the `product_media_url_cron` to suit your needs.

## 5. Conclusion

After following these steps, your Product Media via URL's Module should be properly configured. For any issues that arise during the configuration process, please consult the `troubleshooting_guide.md` for assistance.