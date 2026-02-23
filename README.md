<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About - Handicraft Khazana Shop</title>
    <style>
        :root {
            --primary: #5d4037;
            --secondary: #8d6e63;
            --accent: #27ae60;
            --bg: #fdfaf5;
            --card-bg: #ffffff;
            --text: #333;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }
        h1, h2, h3 { color: var(--primary); }
        h1 { border-bottom: 2px solid var(--secondary); padding-bottom: 10px; }
        .feature-list { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0; }
        .feature-item { 
            background: var(--bg); 
            padding: 15px; 
            border-radius: 8px; 
            border-left: 4px solid var(--accent);
        }
        code {
            background: #eee;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background: #2d2d2d;
            color: #ccc;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }
        .badge {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <span class="badge">v1.0.0</span>
    <h1>🏺 Handicraft Khazana Shop</h1>
    
    <p><strong>Handicraft Khazana Shop</strong> is a specialized e-commerce platform built with <strong>Django</strong> that connects expert artisans with buyers to showcase and sell unique Indian handicrafts. The platform bridges the gap between traditional craftsmanship and modern commerce.</p>

    

    <h2>✨ Key Features</h2>
    <div class="feature-list">
        <div class="feature-item">
            <strong>Dual User Roles</strong><br>
            Specialized registration flows for Buyers and Sellers via a custom signup system.
        </div>
        <div class="feature-item">
            <strong>Admin Verification</strong><br>
            A manual approval gateway to verify sellers before they can list products.
        </div>
        <div class="feature-item">
            <strong>Artisan Dashboard</strong><br>
            A private workspace for artisans to manage their inventory in real-time.
        </div>
        <div class="feature-item">
            <strong>Secure Cart</strong><br>
            Session-based shopping cart with automated email order confirmations.
        </div>
    </div>

    <h2>🚀 Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Python 3.13 & Django</li>
        <li><strong>Frontend:</strong> HTML5, CSS3, JavaScript</li>
        <li><strong>Database:</strong> SQLite (Development)</li>
        <li><strong>Communication:</strong> Django Mail Service</li>
    </ul>

    <h2>📥 Installation</h2>
    <p>To set up this project locally, follow these commands:</p>
    <pre>
# Setup Virtual Environment
python -m venv .venv
.venv\Scripts\activate

# Install Django
pip install django

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Start Server
python manage.py runserver</pre>

    <h2>📂 Core Files</h2>
    <ul>
        <li><code>models.py</code>: Role-based UserProfile and Product structures.</li>
        <li><code>views.py</code>: Secure registration and e-commerce logic.</li>
        <li><code>main_home.html</code>: Responsive hub with artisan attribution.</li>
    </ul>

    <hr>
    <center>
        <p>© 2026 Handicraft Khazana Shop | Developed by B.Tech CSE Student</p>
    </center>
</div>

</body>
</html>
