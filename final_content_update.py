#!/usr/bin/env python3
"""
Final comprehensive content update with Ayush's complete information
"""
import re

def final_content_update(file_path):
    """Apply all remaining content updates"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Store patterns we need to find and replace
    # These are based on typical portfolio sections

    replacements = []

    # Education updates
    replacements.extend([
        # University/College info
        (r'University of [A-Z][a-z]+', 'Manipal Institute of Technology'),
        (r'Bachelor.*?Computer Science', 'Bachelor of Technology in Electrical and Electronic Engineering'),
        (r'degree in Computer Science', 'degree in Electrical and Electronic Engineering'),
        (r'BSc.*?Computer Science', 'B.Tech in Electrical and Electronic Engineering'),
    ])

    # Work experience timeline entries
    # We'll target year patterns near company names
    replacements.extend([
        # Timeline years - being careful not to replace font unicode ranges
        (r'(?<![0-9])(2018)(?![0-9])', '2021'),  # Earliest work year
        (r'(?<![0-9])(2020)(?![0-9])', '2023'),
        (r'(?<![0-9])(2022)(?![0-9])', '2024'),
        (r'(?<![0-9])(2023)(?![0-9])', '2024'),
        (r'(?<![0-9])(2024)(?![0-9])', '2025'),
    ])

    # Job titles and descriptions
    replacements.extend([
        ('Senior Software Engineer', 'Lead Analyst'),
        ('Software Engineer', 'Senior Analyst'),
        ('Junior Developer', 'Analyst'),
        ('Web Developer', 'Marketing Analyst'),
        ('Full Stack Developer', 'Analytics Lead'),
    ])

    # Project descriptions - replace generic portfolio projects with your actual projects
    replacements.extend([
        # Generic project names to your actual projects
        ('E-commerce Platform', 'Zeta Analytics Query Generator'),
        ('Social Media App', 'EverythingAdTech.com'),
        ('Task Manager', 'Issue Estimator'),
        ('Weather App', 'Tutorial Generator'),
    ])

    # Skills section updates
    replacements.extend([
        ('JavaScript, React, Node.js', 'Python, SQL, Hive, Snowflake'),
        ('HTML, CSS, TypeScript', 'Data Analytics, Programmatic Advertising'),
        ('MongoDB, PostgreSQL', 'Query Optimization, Campaign Analysis'),
        ('React, Vue, Angular', 'AI/ML Models, Automation Tools'),
    ])

    changes_made = 0

    # Apply regex replacements
    for pattern, replacement in replacements:
        try:
            new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
            if count > 0:
                content = new_content
                changes_made += count
                print(f"✓ Replaced {count}x: '{pattern[:40]}...' → '{replacement[:40]}...'")
        except Exception as e:
            print(f"  Error with pattern '{pattern}': {e}")

    # Additional specific text replacements
    text_replacements = [
        # Projects section
        ('Built a responsive e-commerce platform', 'Built a parameterized query builder for Hive, Snowflake, and S3'),
        ('Developed a social networking application', 'Created and scaled a programmatic advertising education hub with 1,000+ daily users'),
        ('Created a task management system', 'Developed an AI-based estimator that predicts complexity and effort for development tasks'),
        ('Weather forecast application', 'Documentation-to-tutorial generator for faster contributor onboarding'),

        # About/Bio section additions
        ('passionate about creating', 'specialized in building automation tools and data-driven solutions'),
        ('clean, user-friendly interfaces', 'scalable analytics frameworks'),
        ('modern web technologies', 'programmatic advertising and marketing analytics'),

        # Achievement/impact statements
        ('users love', 'drives measurable campaign performance'),
        ('pixel-perfect designs', 'data-driven insights'),
        ('responsive layouts', 'automated workflows'),
    ]

    for old, new in text_replacements:
        if old in content:
            content = content.replace(old, new)
            changes_made += 1
            print(f"✓ Text replaced: '{old[:40]}...'")

    # Write the final content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ {changes_made} total changes applied!")
    print("Portfolio updated successfully!")

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    final_content_update(file_path)
