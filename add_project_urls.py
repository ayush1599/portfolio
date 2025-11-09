#!/usr/bin/env python3
"""
Add project URLs and ensure all Ayush's specific information is present
"""

def add_project_details(file_path):
    """Add project URLs and detailed descriptions"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Project-specific updates
    replacements = [
        # Add project URLs where "Zeta Analytics Query Generator" appears
        ('Zeta Analytics Query Generator', 'Zeta Analytics Query Generator - zeta-analytics-query-generator.netlify.app'),

        # EverythingAdTech
        ('Everything AdTech', 'EverythingAdTech.com'),

        # Issue Estimator
        ('Issue Estimator', 'Issue Estimator - issue-estimator-gray.vercel.app'),

        # Tutorial Generator
        ('Tutorial Generator', 'Tutorial Generator - tutorial-generator-gray.vercel.app'),

        # Career descriptions - enhanced
        ('Built automation tools for query generation',
         'Built automation tools for query generation, omnichannel lift analysis, and AI-powered segmentation models that optimize campaign performance and reduce manual effort by 60%'),

        ('programmatic advertising education hub',
         'programmatic advertising education hub with 1,000+ daily users. Designed backend automation for real-time news aggregation and scheduling'),

        ('targeting and dashboarding solutions',
         'targeting and dashboarding solutions leveraging APIs and contextual matching, boosting YouTube VTR by 12% and optimizing B2B client outreach'),

        ('Automated campaign snapshot reporting',
         'Automated campaign snapshot reporting (saving 80% time), delivered insights driving $115K upsell, and developed DSP/DCM discrepancy tools saving $9K'),

        ('pacing and KPI tracking tools',
         'pacing and KPI tracking tools that enhanced campaign monitoring and led to $250K in upweights'),

        # Education details
        ('Manipal Institute of Technology',
         'Manipal Institute of Technology (2017–2021) - Bachelor of Technology in Electrical and Electronic Engineering'),

        # Professional title enhancements
        ('Lead Analyst | Zeta Global',
         'Lead Analyst | Zeta Global (2024–Present)'),

        ('Founder & Developer | Everything',
         'Founder & Developer | EverythingAdTech (2023–2024)'),

        ('Senior Analyst | MiQ',
         'Senior Analyst | MiQ (2023–2024)'),

        # Make sure full role description appears
        ('Analyst | MiQ', 'Analyst | MiQ (2021–2023)'),

        ('Business Analyst Intern', 'Business Analyst Intern | MiQ (2021)'),
    ]

    changes_made = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes_made += 1
            print(f"✓ Enhanced: '{old[:45]}...'")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ {changes_made} enhancements applied!")
    return changes_made

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    add_project_details(file_path)
