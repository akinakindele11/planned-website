# Planned Limited Website

Professional website for Planned Limited - specialist project planning, controls, and Primavera P6 administration services.

## File Structure

```
planned-website/
├── about.html                    # About Us page
├── services.html                 # Services Hub page  
├── contact.html                  # Contact & Inquiry page
├── faq.html                       # FAQ page
├── css/
│   └── style.css                 # Shared responsive stylesheet
├── js/
│   └── main.js                   # Shared JavaScript (mobile menu, FAQ toggles)
└── (other pages: index.html, industries.html, blog/, services/)
```

## Pages Created

### 1. about.html
- Hero section with company introduction
- "Who Is Planned Limited?" section
- Mission statement
- 6 key differentiators (Specialist Focus, Primavera P6 Mastery, Flexible Engagement, Cost-Effective, Cross-Industry Versatility, Results-Driven)
- 4 core values (Excellence, Integrity, Partnership, Adaptability)
- 4-step approach (Consultation, Planning, Monitoring, Reporting)
- Call-to-action section
- BreadcrumbList + Organization schema

### 2. services.html
- Hero section with service overview
- 5 service cards (Project Planning, Project Controls, Risk Analysis, Resource Management, P6 Administration)
- "How Do We Work?" section with 4 engagement models
- Call-to-action section
- BreadcrumbList schema

### 3. contact.html
- Hero section "Get in Touch"
- Two-column layout with:
  - Contact form (Name, Email, Company, Phone, Service Type dropdown, Message)
  - Contact details (Email, Phone, LinkedIn, Website, 24-hour response promise)
- "What Happens After You Contact Us" - 4-step process
- Call-to-action section
- BreadcrumbList + LocalBusiness schema

### 4. faq.html
- 15 FAQ items organized in 4 sections:
  - General (4 items)
  - Services & Process (4 items)
  - Tools & Technical (3 items)
  - Costs & Commercial (5 items)
- Interactive accordion with toggleFaq() function
- FAQPage + BreadcrumbList schema

## Navigation & Footer

All pages include:
- **Navigation**: Logo, Home, Services dropdown, About Us, Industries, Blog, FAQ, Contact, CTA button
- **Mobile menu**: Hamburger toggle for responsive design
- **Footer**: 4-column layout with brand, services, company links, and contact info

## Styling & JavaScript

### css/style.css
- Responsive design with mobile-first approach
- Breakpoints: 768px (tablets), 480px (phones)
- CSS variables for colors and spacing
- Grid layouts (grid-3, grid-4)
- Hover effects and transitions
- Form styling with focus states
- Accordion styling for FAQ

### js/main.js
- `toggleMobileMenu()` - Show/hide mobile navigation
- `toggleFaq(element)` - Toggle FAQ accordion items (single open)
- Mobile dropdown menu handling
- Form submission placeholder

## Key Features

- British English spelling throughout
- Professional but approachable tone
- Proper SEO meta tags and structured data (schema.org)
- Mobile responsive design
- Accessible form elements
- Smooth animations and transitions
- 24-hour customer response promise
- Grid-based layouts
- Service type dropdown on contact form
- Interactive FAQ with smooth toggles

## Color Scheme

- Primary: #0066cc (Blue)
- Secondary: #004499 (Dark Blue)
- Accent: #ff6600 (Orange)
- Text: #1a1a1a (Dark)
- Light Text: #666666 (Gray)
- Background: #f9f9f9 (Off-white)

## Customization Notes

- Update company contact details in footer and contact page
- Replace address placeholder in LocalBusiness schema
- Connect form submission to actual backend service
- Add logo image at path: images/logo.png
- Customize service descriptions and links as needed
- Update LinkedIn company link to actual profile
