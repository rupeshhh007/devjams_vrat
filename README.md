Mental Health Awareness Web Page Documentation
Overview
This HTML document represents a web page dedicated to raising awareness about mental health. It includes sections for information, resources, and a contact form, along with navigation elements and interactive features.
File Structure
•	index.html (This document)
•	/static/
o	style.css (Custom styles for the page)
o	script.js (JavaScript for interactivity)
HTML Structure
Head Section
The <head> section contains metadata and links to external resources:
•	Character Set: UTF-8 for encoding.
•	Viewport: Ensures responsive design on mobile devices.
•	Stylesheets:
o	Font Awesome for icons.
o	Google Fonts for typography.
o	Local stylesheet for custom styles.
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/style.css">
    <title>Mental Health Awareness</title>
</head>
Body Section
The <body> contains the main content of the web page:
Header
Includes a welcoming header and a navigation menu with links to different sections:
<header>
    <h1>Welcome to Mental Health Awareness</h1>
    <nav>
        <ul>
            <li><a href="#info"><i class="fas fa-info-circle"></i> About</a></li>
            <li><a href="#resources"><i class="fas fa-book-open"></i> Resources</a></li>
            <li><a href="#contact"><i class="fas fa-envelope"></i> Contact</a></li>
            <li><a href="/responses"><i class="fas fa-eye"></i> View Responses</a></li>
        </ul>
    </nav>
</header>
Main Content
The <main> section features three primary sections:
1.	About Mental Health
o	Provides an overview of mental health.
<section id="info">
    <h2>About Mental Health</h2>
    <p>Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, and act.</p>
</section>
Resources
•	Lists helpful resources related to mental health
<section id="resources">
    <h2>Resources</h2>
    <ul>
        <li><a href="https://www.nami.org" target="_blank">National Alliance on Mental Illness (NAMI)</a></li>
        <li><a href="https://www.mentalhealth.gov" target="_blank">MentalHealth.gov</a></li>
        <li><a href="https://www.suicidepreventionlifeline.org" target="_blank">National Suicide Prevention Lifeline</a></li>
    </ul>
</section>
Contact Us
•	Contains a contact form for users to reach out.
<section id="contact">
    <h2>Contact Us</h2>
    <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" required>
        <label for="message">Message:</label>
        <textarea id="message" required></textarea>
        <button type="submit">Send</button>
    </form>
</section>
Menu Button
A button to toggle a menu with additional information:
<div class="menu-container">
    <button class="menu-button" onclick="toggleMenu()">Menu</button>
    <div class="menu" id="menu">
        <ul>
            <li><a href="#symptoms">Symptoms</a></li>
            <li><a href="#precautions">Precautions</a></li>
            <li><a href="#healthcare-centres">Healthcare Centres</a></li>
            <li><a href="#what-to-do">What to Do</a></li>
            <li><a href="#what-not-to-do">What Not to Do</a></li>
        </ul>
    </div>
</div>
Heart Animation
A decorative heart icon that may represent care and support:
<div class="heart-container">
    <i class="fas fa-heart animated-heart"></i>
</div>
Button Container
Two buttons for quick access to help:
<div class="button-container">
    <button class="emergency-button">Emergency Help</button>
    <button class="help-button">I Need Help</button>
</div>
Footer
A footer that includes copyright information:
<footer>
    <p>&copy; 2024 Mental Health Initiative</p>
</footer>
Scripts
The <script> tag at the end of the document includes a JavaScript file for additional functionality:
<script src="/static/script.js"></script>
Accessibility
•	Uses aria-label attributes for navigation links to enhance accessibility.
•	Form elements have associated labels for better usability.
Conclusion
This web page aims to promote mental health awareness by providing informative content, useful resources, and a means for users to get in touch. The design incorporates user-friendly navigation and interactive features to enhance engagement.

