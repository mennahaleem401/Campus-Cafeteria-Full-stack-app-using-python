# 🍽️ Campus Cafeteria

Campus Cafeteria is a Django-based web application that allows students and staff to browse a digital cafeteria menu, add items to a shopping cart, and place orders.  
Admins can manage products, track orders, and update their statuses (e.g., from *Pending* to *Completed*).

---

## 🚀 Features

### 👥 Users
- Register, log in, and browse the cafeteria menu.
- Add food and drinks to the shopping cart.
- Place orders and view recently placed orders.

### 🛒 Shopping Cart
- Add/remove products from the cart.
- Automatically calculates the total price.
- Checkout system creates orders and clears the cart.

### 📦 Orders
- Orders are stored with status: **Pending / Completed**.
- Users can view their order history.
- Admins can update the status of each order.

### 🛠️ Admin Panel
- Manage users, products, carts, and orders.
- Inline order items inside each order for easy management.
- Ability to update order status.

---

## 🖼️ Product Images
- Each product has an associated image (stored in `/media/products/`).
- Images are displayed in the menu grid with proper styling.

---

## ⚙️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend:** HTML, CSS (with responsive design)
- **Static & Media Handling:** Django Staticfiles & Media uploads
- **Authentication:** Django Auth System
- **Dependencies:** Pillow (for handling image uploads)


## 📸 Screenshots

<img width="1867" height="887" alt="image" src="https://github.com/user-attachments/assets/dd20a7af-5c4d-446e-af16-d038527c7e00" />
<img width="1872" height="892" alt="image" src="https://github.com/user-attachments/assets/621f4b28-9e35-47bd-9cb6-0a3ed59be4f3" />
<img width="1872" height="842" alt="image" src="https://github.com/user-attachments/assets/4b1003ba-e94b-4088-a8c4-44300ebde245" />
<img width="1860" height="877" alt="image" src="https://github.com/user-attachments/assets/2e04d4ff-efab-4d9b-82b0-e880c8c76df9" />
<img width="1846" height="888" alt="image" src="https://github.com/user-attachments/assets/c4581349-170c-42e8-ba4b-1f02412e61ee" />
<img width="1832" height="883" alt="image" src="https://github.com/user-attachments/assets/b9c8f6c4-599f-4acd-8184-edf3950390d6" />



---

## ✅ Future Improvements

* Add payment gateway integration.
* Implement order notifications.
* Add filtering and search options for menu items.
* Enhance responsive UI for mobile users.

---

👩‍💻 Developed with ❤️ by Menna Haleem

