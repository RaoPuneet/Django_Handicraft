Handicraft Khazana Shop
Handicraft Khazana Shop is a specialized e-commerce platform built with Django that connects expert artisans with buyers to showcase and sell unique Indian handicrafts. The project features role-based access control, allowing verified sellers to manage their own inventories via a dedicated dashboard while providing customers with a curated shopping experience.

🚀 Features
Role-Based Access Control: Distinct interfaces and permissions for Buyers and Sellers.

Artisan Dashboard: Sellers can add, view, and delete their own unique craft items.

Product Management: Detailed listings including categories, prices, images, and artisan attribution.

Admin Verification: A manual approval system for sellers to ensure the quality and authenticity of the marketplace.

E-commerce Core: Functional shopping cart and checkout process with email order confirmations.

Secure Authentication: User registration and login system with encrypted passwords and profile management.

🛠️ Tech Stack
Backend: Python 3.13, Django

Frontend: HTML5, CSS3 (Custom brand theme)

Database: SQLite (Development)

Email Service: Django Mail for welcome and order notifications

📂 Project Structure
models.py: Defines the Product, Category, and UserProfile (Role-based) structures.

views.py: Contains the logic for the marketplace, seller dashboard, and secure user management.

urls.py: Handles all routing from product browsing to admin management.

templates/: Custom HTML layouts including main_home.html, seller_dashboard.html, and auth forms.

🔧 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/HandicraftKhazana.git
cd HandicraftKhazana
Create a virtual environment:

Bash
python -m venv .venv
.venv\Scripts\activate
Install dependencies:

Bash
pip install django
Run Migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Start the Server:

Bash
python manage.py runserver
📝 Usage
As a Buyer: Browse the "New Arrivals", add items to your cart, and receive an email receipt upon payment.

As a Seller: Sign up as a seller, wait for admin approval, and then use your dashboard to list your handicrafts.
