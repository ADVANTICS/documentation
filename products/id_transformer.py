import os
import re
import argparse

# The regular expression looks for:
# 1. Start of line (^)
# 2. One or more hash marks followed by a space (#+ ) - Captured in Group 1
# 3. The actual heading text, non-greedily (.+?) - Captured in Group 2
# 4. A space, followed by the literal text ':id='
# 5. The ID itself, non-greedily (.+?) - Captured in Group 3
# 6. End of line ($)
# Example match: # State :id=Advantics_Controller_Status-State
ID_PATTERN = re.compile(r'^(#+ )(.+?) :id=(.+?)$', re.MULTILINE)

# The replacement string uses the captured groups:
# \1 (Original Prefix) + \2 (Original Title) + { #\3 } (New ID format)
# Example replacement: # State { #Advantics_Controller_Status-State }
REPLACEMENT_STRING = r'\1\2 { #\3 }'

def transform_markdown_content(content):
    """
    Applies the regex transformation to the content of a single Markdown file.
    
    Args:
        content (str): The raw text content of the file.
        
    Returns:
        tuple: (modified_content, count_of_changes)
    """
    # Use subn to perform substitution and get the count of replacements
    modified_content, count = ID_PATTERN.subn(REPLACEMENT_STRING, content)
    return modified_content, count

def process_directory_recursively(root_dir):
    """
    Recursively walks through a directory, processes Markdown files, and
    updates their content in-place.
    
    Args:
        root_dir (str): The starting directory path.
    """
    if not os.path.isdir(root_dir):
        print(f"Error: Directory not found at path: {root_dir}")
        return

    total_changes = 0

    print(f"Starting transformation in directory: {root_dir}")

    # os.walk generates the file names in a directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check for common markdown extensions
            if filename.endswith(('.md', '.markdown')):
                filepath = os.path.join(dirpath, filename)
                
                # Skip symbolic links to avoid infinite loops or permission errors
                if os.path.islink(filepath):
                    print(f"Skipping symlink: {filepath}")
                    continue
                    
                print(f"Processing: {filepath}")
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                        
                    modified_content, changes_in_file = transform_markdown_content(original_content)
                    
                    if changes_in_file > 0:
                        # Write back the modified content
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        
                        print(f"    ✅ Applied {changes_in_file} transformation(s).")
                        total_changes += changes_in_file
                    else:
                        print("    ... No changes needed.")
                        
                except Exception as e:
                    print(f"    ❌ Failed to process {filepath}: {e}")

    print("-" * 30)
    print(f"Transformation complete. Total IDs converted: {total_changes}")

def main():
    """Main function to parse arguments and run the processing."""
    parser = argparse.ArgumentParser(
        description="Recursively transforms MkDocs custom heading ID syntax."
    )
    parser.add_argument(
        'path', 
        nargs='?', # Makes the path argument optional
        default='.', # Defaults to the current directory
        help="The root directory to start searching for markdown files (e.g., 'docs'). Defaults to the current directory ('.')."
    )
    
    args = parser.parse_args()
    process_directory_recursively(args.path)

if __name__ == '__main__':
    main()

