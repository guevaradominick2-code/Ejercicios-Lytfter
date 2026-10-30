CREATE TABLE `Products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Code` VARCHAR(255) NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry_Date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock_available` INT NOT NULL
);
ALTER TABLE
    `Products` ADD UNIQUE `products_code_unique`(`Code`);
CREATE TABLE `Invoices`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Invoice_number` INT NOT NULL,
    `Purchase_date` DATE NOT NULL,
    `Buyer_email` VARCHAR(255) NOT NULL,
    `Total_amount` DECIMAL(8, 2) NOT NULL
);
ALTER TABLE
    `Invoices` ADD UNIQUE `invoices_invoice_number_unique`(`Invoice_number`);
CREATE TABLE `Products Per Invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `Quantity` INT NOT NULL,
    `Total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Shopping Cart`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer_email` VARCHAR(255) NOT NULL,
    `Products` BIGINT NOT NULL
);
ALTER TABLE
    `Shopping Cart` ADD UNIQUE `shopping cart_buyer_email_unique`(`Buyer_email`);
CREATE TABLE `Shopping_Cart_Items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL
);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_id_foreign` FOREIGN KEY(`id`) REFERENCES `Shopping_Cart_Items`(`cart_id`);
ALTER TABLE
    `Products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `Shopping_Cart_Items`(`product_id`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `Products`(`id`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `Invoices`(`Invoice_number`);