#!/usr/bin/env python3
"""
Add Ayush's specific career details and project URLs
"""
import re

def add_specific_ayush_content(file_path):
    """Add very specific details about Ayush's career and projects"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Very specific replacements
    replacements = [
        # Career timeline descriptions
        (r'Zeta Global[\s\S]{0,200}?(Senior|Lead|Staff)',
         'Zeta Global</span> as Lead Analyst, where I built automation tools for query generation, omnichannel lift analysis, and AI-powered segmentation models that optimize campaign performance and reduce manual effort by 60%'),

        # MiQ descriptions (formerly Facebook)
        (r'MiQ[\s\S]{0,200}?(Engineer|Developer)',
         'MiQ</span> where I developed targeting and dashboarding solutions leveraging APIs and contextual matching, boosting YouTube VTR by 12% and optimizing B2B client outreach'),

        # Project URLs - find patterns that look like project links or descriptions
        ('zeta-analytics', 'zeta-analytics-query-generator.netlify.app'),
        ('everythingadtech', 'everythingadtech.com'),
        ('issue-estimator', 'issue-estimator-gray.vercel.app'),
        ('tutorial-generator', 'tutorial-generator-gray.vercel.app'),

        # Add specific achievement metrics
        ('reduced manual effort', 'reduced manual effort by 60%'),
        ('improved performance', 'boosted YouTube VTR by 12%'),
        ('saved time', 'saving 80% time on reporting'),
        ('1000 users', '1,000+ daily users'),
        ('\\$100K', '$115K upsell'),
        ('\\$200K', '$250K in upweights'),

        # Education details
        (r'(Manipal Institute of Technology)[\s\S]{0,100}?(202[0-9])',
         'Manipal Institute of Technology (2017–2021)</span>, where I completed my Bachelor of Technology in Electrical and Electronic Engineering'),

        # Professional title variations
        ('Data Analyst', 'Analytics Lead'),
        ('Marketing Specialist', 'Data-Driven Marketer'),
        ('Product Manager', 'Product Builder'),

        # Work period formats - adjust specific years for roles
        (r'(Lead Analyst)[\s\S]{0,50}?(202[0-9])[^0-9]', r'\1 | Zeta Global (2024–Present)'),
        (r'(Founder.*?Everything\s*AdTech)[\s\S]{0,50}?(202[0-9])', r'\1 (2023–2024)'),
        (r'(Senior Analyst.*?MiQ)[\s\S]{0,50}?(202[0-9])', r'\1 (2023–2024)'),
        (r'(Analyst.*?MiQ)(?!.*Senior)[\s\S]{0,50}?(202[0-9])', r'\1 (2021–2023)'),
        (r'(Business Analyst Intern.*?MiQ)[\s\S]{0,50}?(202[0-9])', r'\1 (2021)'),
    ]

    changes_made = 0
    for pattern, replacement in replacements:
        try:
            if isinstance(pattern, str) and not pattern.startswith('(?'):
                # Simple string replacement
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    changes_made += 1
                    print(f"✓ Added: '{replacement[:50]}...'")
            else:
                # Regex replacement
                new_content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE)
                if count > 0:
                    content = new_content
                    changes_made += count
                    print(f"✓ Updated {count}x: pattern → '{replacement[:50]}...'")
        except Exception as e:
            print(f"  Skipped pattern: {e}")

    # Write final content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Added {changes_made} specific details!")
    return changes_made

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    add_specific_ayush_content(file_path)
