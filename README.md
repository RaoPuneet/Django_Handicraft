🏺 Handicraft Khazana Shop
Handicraft Khazana Shop is a specialized e-commerce platform built with Django that connects expert artisans with buyers to showcase and sell unique Indian handicrafts. The platform bridges the gap between traditional craftsmanship and modern commerce, offering a curated space for items like brass engravings, wood carvings, and miniature paintings.

✨ Key Features
👤 User Roles & Management
Dual User Roles: Specialized registration flows for Buyers and Sellers via a custom signup system.

Admin Verification: A manual approval gateway where administrators must verify sellers before they can list products, ensuring marketplace quality.

Secure Auth: Full authentication suite including login, logout, and password reset functionality.

🛠 Seller Tools
Dedicated Dashboard: A private workspace for artisans to manage their inventory in real-time.

Inventory Control: Sellers can add new masterpieces with images and categories, or remove items they no longer wish to sell.

Artisan Attribution: Every product card on the home page automatically credits the specific artisan who created it.

🛒 Shopping Experience
New Arrivals: Dynamic homepage section highlighting the latest handcrafted additions.

Category Filtering: Organized browsing by craft type (e.g., Woodwork, Brass, Paintings).

Cart & Checkout: Fully functional session-based shopping cart with automated email order confirmations.

🚀 Tech Stack
Backend: Python 3.13 & Django

Frontend: HTML5, CSS3, JavaScript

Database: SQLite (default)

Communication: Django Mail for welcome and order notifications

📥 Installation
Clone the project

Bash
git clone https://github.com/yourusername/HandicraftKhazana.git
cd HandicraftKhazana
Setup Virtual Environment

Bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
Install Dependencies

Bash
pip install django
Initialize Database

Bash
python manage.py makemigrations
python manage.py migrate
Run the Application

Bash
python manage.py runserver
📂 File Highlights
models.py: Custom UserProfile with role-based logic and Product models with seller foreign keys.

views.py: Robust logic handling secure registration, seller verification, and e-commerce flows.

main_home.html: The central hub featuring role-specific navigation and artisan product cards.

🛡️ Administrative Control
Instead of using the command line to manage users, this project includes a custom User Management View where admins can see a "Role" column and click an Approve button to verify new artisans directly in the browser.
