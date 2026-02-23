<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README - Handicraft Khazana Shop</title>
</head>
<body>

    <h1>Handicraft Khazana Shop</h1>
    
    <p>
        Handicraft Khazana Shop is a specialized e-commerce platform built with Django that connects expert artisans with buyers to showcase and sell unique Indian handicrafts like wood carvings and brass engravings. The project features role-based access control, allowing verified sellers to manage their own inventories via a dedicated dashboard while providing customers with a curated shopping experience.
    </p>

    <hr>

    <h2>Core Features</h2>
    <ul>
        <li><strong>Role-Based Accounts:</strong> Users can register as either a "Buyer" or a "Seller" using a custom signup form.</li>
        <li><strong>Seller Dashboard:</strong> A private area for artisans to list new products, view their current inventory, and delete items they no longer wish to sell.</li>
        <li><strong>Admin Approval System:</strong> A security layer where administrators manually verify seller accounts before they are permitted to list products on the public shop.</li>
        <li><strong>Product Attribution:</strong> Every item displayed on the home page clearly shows the name of the artisan who created it.</li>
        <li><strong>Shopping & Checkout:</strong> A fully functional cart system that sends an automated email confirmation to the buyer upon a successful purchase.</li>
    </ul>

    

    <h2>Technical Stack</h2>
    <ul>
        <li><strong>Framework:</strong> Django (Python 3.13)</li>
        <li><strong>Frontend:</strong> HTML5 and CSS3</li>
        <li><strong>Database:</strong> SQLite</li>
        <li><strong>Authentication:</strong> Django built-in authentication extended with a UserProfile model</li>
    </ul>

    <h2>Installation Guide</h2>
    <ol>
        <li>Clone the repository to your local machine.</li>
        <li>Create a virtual environment: <code>python -m venv .venv</code>.</li>
        <li>Activate the environment and install Django: <code>pip install django</code>.</li>
        <li>Generate the database: <code>python manage.py makemigrations</code> followed by <code>python manage.py migrate</code>.</li>
        <li>Start the server: <code>python manage.py runserver</code>.</li>
    </ol>

    <h2>Project Logic (File Overview)</h2>
    <ul>
        <li><strong>models.py:</strong> Defines the <code>UserProfile</code> (handling roles), <code>Category</code>, and <code>Product</code> (linked to specific sellers).</li>
        <li><strong>views.py:</strong> Contains the logic for the marketplace, the seller verification process, and the restricted artisan dashboard.</li>
        <li><strong>urls.py:</strong> Manages the routing for the shop, including the custom user management and approval paths.</li>
    </ul>

    

    <hr>
    <p><em>Developed as a B.Tech CSE Project</em></p>

</body>
</html>
