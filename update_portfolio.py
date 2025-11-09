#!/usr/bin/env python3
"""
Script to update portfolio content while maintaining Framer styling
"""

def update_portfolio_content(file_path):
    """Read and update the HTML file with new content"""

    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Store original content for backup
    backup_path = file_path.replace('.html', '_backup.html')
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup created: {backup_path}")

    # Meta tags updates
    replacements = [
        # Title and meta descriptions
        ('<title>Purplefolio | Portfolio For Web Developers.</title>',
         '<title>Ayush Dutta | Data-Driven Marketing & Analytics Lead</title>'),

        ('<meta name="description" content="A minimalist portfolio for web developers">',
         '<meta name="description" content="Data-driven marketer, product builder, and analytics lead at Zeta Global. Designing tools that merge data science, automation, and creativity.">'),

        # Open Graph tags
        ('<meta property="og:title" content="Purplefolio | Portfolio For Web Developers.">',
         '<meta property="og:title" content="Ayush Dutta | Data-Driven Marketing & Analytics Lead">'),

        ('<meta property="og:description" content="A minimalist portfolio for web developers">',
         '<meta property="og:description" content="Data-driven marketer, product builder, and analytics lead at Zeta Global. Designing tools that merge data science, automation, and creativity.">'),

        # Twitter Card tags
        ('<meta name="twitter:title" content="Purplefolio | Portfolio For Web Developers.">',
         '<meta name="twitter:title" content="Ayush Dutta | Data-Driven Marketing & Analytics Lead">'),

        ('<meta name="twitter:description" content="A minimalist portfolio for web developers">',
         '<meta name="twitter:description" content="Data-driven marketer, product builder, and analytics lead at Zeta Global. Designing tools that merge data science, automation, and creativity.">'),

        # Main introduction text
        ("I&apos;m a frontend developer based in Italy, I&apos;ll help you build beautiful websites your users will love.",
         "Hi, I&apos;m Ayush Dutta — a data-driven marketer, product builder, and analytics lead at Zeta Global. I design tools and frameworks that merge data science, automation, and creativity to drive smarter campaign decisions and scalable insights."),

        # About/Journey section
        ("My journey as a front-end developer started back in 2010, working as a ",
         "My work bridges programmatic advertising, analytics automation, and AI-enabled solutions that simplify complex workflows across teams. I&apos;ve held roles including "),

        # Experience examples - we'll need to find and replace specific company/role mentions
        ("After being on my own for a while, I decided to enter the corporate world, and I started working as a software developer at ",
         "I specialize in building automation tools for query generation, omnichannel lift analysis, and AI-powered segmentation models. My journey includes roles at "),

        # Apple/MusicKit project reference
        ("Contributed extensively to MusicKit.js, a JavaScript framework that allows developers to add an Apple Music player to their web apps",
         "Built automation tools for query generation, omnichannel lift analysis, and AI-powered segmentation models that optimize campaign performance and reduce manual effort by 60%"),
    ]

    # Apply all replacements
    changes_made = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes_made += 1
            print(f"✓ Replaced: {old[:50]}...")
        else:
            print(f"✗ Not found: {old[:50]}...")

    # Write the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n{changes_made} replacements made successfully!")
    print(f"Updated file: {file_path}")

    return changes_made

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    update_portfolio_content(file_path)
