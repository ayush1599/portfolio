#!/usr/bin/env python3
"""
Comprehensive portfolio content update script
"""

def update_detailed_content(file_path):
    """Update all specific content including companies, roles, projects, and dates"""

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Detailed replacements for work experience and projects
    replacements = [
        # Company names
        ("Apple", "Zeta Global"),
        ("Facebook", "MiQ"),

        # Roles and titles
        ("frontend developer", "data-driven marketer and analytics lead"),
        ("front-end developer", "marketing analyst"),
        ("software developer", "analytics lead"),
        ("freelancer", "founder"),
        ("freelance", "independent"),

        # Education - find and replace specific patterns
        ("based in Italy", "based in India"),

        # Years/Timeline - we'll be strategic about these
        ("back in 2010", "in 2017"),
        ("2010", "2017"),

        # Specific project/achievement descriptions that might exist
        # We'll search for common phrases and replace them
    ]

    changes_made = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes_made += count
            print(f"✓ Replaced {count}x: '{old}' → '{new}'")
        else:
            print(f"  Not found: '{old}'")

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n{changes_made} total replacements made!")
    return changes_made

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    update_detailed_content(file_path)
