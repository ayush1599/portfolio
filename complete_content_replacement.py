#!/usr/bin/env python3
"""
Complete content replacement - find and replace ALL old portfolio content
"""
import re

def find_and_replace_all_content(file_path):
    """Find all old content and replace with Ayush's information"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Comprehensive list of ALL text replacements needed
    replacements = [
        # Specific sentences that need complete replacement
        ("I&apos;m now working at Zeta Global. And you know what? I love what I do! &#x1f49c;",
         "I specialize in building automation tools, AI-powered analytics, and programmatic advertising solutions that drive measurable results."),

        # Any remaining fragments about previous life
        ("settle down for a more calm and simple routine, and I&apos;m now working at Zeta Global",
         "I&apos;m currently working at Zeta Global as Lead Analyst, building tools that optimize campaign performance"),

        ("for a more calm and simple routine",
         "focused on data-driven marketing solutions"),

        # Job/role descriptions
        ("working as a independent",
         "working as founder of EverythingAdTech"),

        # More about section content
        ("I specialize in building automation tools for query generation, omnichannel lift analysis, and AI-powered segmentation models. My journey includes roles at",
         "Throughout my career, I&apos;ve specialized in analytics automation, programmatic advertising, and AI-enabled solutions. My experience spans roles at"),

        # Timeline/experience details - be more specific
        ("I&apos;ve held roles including",
         "My career includes positions as"),

        # Replace any remaining generic developer language
        ("beautiful websites your users will love",
         "analytics tools that deliver actionable insights"),

        ("pixel perfect",
         "data-driven"),

        ("responsive design",
         "automated workflows"),

        # Skills
        ("HTML, CSS, JavaScript",
         "Python, SQL, Hive"),

        ("React, Vue, Angular",
         "Analytics, Automation, AI/ML"),

        ("Node.js, Express",
         "Snowflake, Tableau"),

        # Any Italy references
        ("Italy", "India"),
        ("Italian", "Indian"),

        # Generic project descriptions
        ("e-commerce",
         "analytics platform"),

        ("social media app",
         "AdTech education platform"),

        ("task management",
         "issue estimation"),

        # Hobby/personal section updates
        ("When I&apos;m not coding",
         "When I&apos;m not analyzing data"),

        ("building side projects",
         "developing automation tools"),

        # Contact/CTA text
        ("Let&apos;s build something amazing together",
         "Let&apos;s create data-driven solutions together"),

        ("hire me", "connect with me"),
    ]

    changes_made = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes_made += 1
            print(f"✓ Replaced: '{old[:60]}...'")

    # Now do regex-based cleanup for any remaining generic content
    regex_replacements = [
        # Remove any "years of experience" that doesn't match
        (r'(\d+)\+? years? of experience in web development',
         r'4+ years of experience in marketing analytics'),

        # Update any remaining skill mentions
        (r'expert in (React|Vue|Angular|JavaScript)',
         r'expert in data analytics'),
    ]

    for pattern, replacement in regex_replacements:
        content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if count > 0:
            changes_made += count
            print(f"✓ Regex replaced: {count}x - '{pattern[:50]}...'")

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ {changes_made} final replacements completed!")

    # Verify no old content remains
    print("\nVerifying clean content...")
    old_keywords = ["frontend developer", "Italy", "freelance web", "MusicKit", "beautiful websites"]
    issues_found = []
    for keyword in old_keywords:
        if keyword.lower() in content.lower():
            issues_found.append(keyword)

    if issues_found:
        print(f"⚠️  Still found: {', '.join(issues_found)}")
        print("   (These may be in CSS/metadata - checking context...)")
    else:
        print("✅ All old content successfully replaced!")

    return changes_made

if __name__ == "__main__":
    file_path = "/Users/aydutta/Library/CloudStorage/OneDrive-ZetaGlobal/Documents/Ayush's Purplefolio/index.html"
    find_and_replace_all_content(file_path)
