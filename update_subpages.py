import re

def update_file(path, new_title, new_banner_desc, new_overview, new_included_title, new_included_desc, features, timeline):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update title
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title} - Virtue Crennovative Solutions</title>', content)
    
    # Update inner banner title
    content = re.sub(r'<h1 class="inner-banner-title services-details">.*?</h1>', f'<h1 class="inner-banner-title services-details">{new_title}</h1>', content)
    
    # Update inner banner desc
    content = re.sub(r'<p class="inner-banner-description services-details-banner-description">.*?</p>', f'<p class="inner-banner-description services-details-banner-description">{new_banner_desc}</p>', content)
    
    # Update Service Overview
    content = re.sub(r'<h2>Service Overview:</h2>.*?<h2>', f'<h2>Service Overview:</h2><p>{new_overview}</p><h2>', content, flags=re.DOTALL)
    
    # Update What's Included title
    content = re.sub(r'<h2>What&#x27;s Included in .*?Services:</h2>', f'<h2>What&#x27;s Included in {new_included_title} Services:</h2>', content)
    
    # Update the rest up to the figure
    start_tag = f'<h2>What&#x27;s Included in {new_included_title} Services:</h2>'
    
    features_html = '<h5>Features:</h5><ul role="list">' + ''.join(f'<li>{f}</li>' for f in features) + '</ul>'
    features_html += '<h5>Delivery Timeline:</h5><ul role="list">' + ''.join(f'<li>{t}</li>' for t in timeline) + '</ul>'
    
    pattern = re.compile(start_tag + r'.*?(?=<figure)', re.DOTALL)
    replacement = start_tag + f'<p>{new_included_desc}</p>' + features_html
    content = pattern.sub(replacement, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# File 2: web-development.html -> Branding and Logo Design
update_file(
    r'c:\Users\Ashley\OneDrive\Documents\VCS\vcs_new\services-subpages\web-development.html',
    'Branding and Logo Design',
    'Professional branding services to create a memorable and cohesive identity. Logo Design, Color Palette & Typography, Brand Guidelines, Rebranding Services.',
    'Professional branding services to create a memorable and cohesive identity.',
    'Branding and Logo Design',
    'Professional branding services to create a memorable and cohesive identity.',
    ['Logo Design', 'Color Palette & Typography', 'Brand Guidelines', 'Rebranding Services'],
    ['Starting from 1-2 weeks']
)

# File 3: branding.html -> Social Media Management & Strategy
update_file(
    r'c:\Users\Ashley\OneDrive\Documents\VCS\vcs_new\services-subpages\branding.html',
    'Social Media Management & Strategy',
    'Comprehensive social media services including content creation and strategy. Content Calendars, Post Design, Ad Campaigns, Growth Strategy.',
    'Comprehensive social media services including content creation and strategy.',
    'Social Media Management & Strategy',
    'Comprehensive social media services including content creation and strategy.',
    ['Content Calendars', 'Post Design', 'Ad Campaigns', 'Growth Strategy'],
    ['Ongoing']
)

# File 4: product-design.html -> Tech & Brand Consulting and Strategy
update_file(
    r'c:\Users\Ashley\OneDrive\Documents\VCS\vcs_new\services-subpages\product-design.html',
    'Tech & Brand Consulting and Strategy',
    'Expert consulting to align your technology and brand strategy with business goals. Brand Positioning, Tech Stack Review, Market Strategy, Growth Planning.',
    'Expert consulting to align your technology and brand strategy with business goals.',
    'Tech & Brand Consulting and Strategy',
    'Expert consulting to align your technology and brand strategy with business goals.',
    ['Brand Positioning', 'Tech Stack Review', 'Market Strategy', 'Growth Planning'],
    ['Starting from 2-4 weeks']
)
