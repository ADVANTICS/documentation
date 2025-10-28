import os
import glob

# The specific line we are looking to remove.
# We strip it of leading/trailing whitespace before comparison.
TARGET_LINE = "[!UPDATE] {docsify-updated}"

def cleanup_markdown_files(directory='.'):
    """
    Scans a directory (and all its subdirectories) for .md files and removes 
    the TARGET_LINE if it is the first line of the file.
    """
    print(f"Scanning directory and subdirectories starting from: {os.path.abspath(directory)} for Markdown files...")
    
    # Use glob to find all markdown files in the current directory AND recursively 
    # in all subdirectories using the '**/'. The 'recursive=True' argument is mandatory.
    markdown_files = glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)
    
    if not markdown_files:
        print("No .md files found.")
        return

    modified_count = 0

    for filepath in markdown_files:
        try:
            # Skip directories, although recursive glob should only return files
            if os.path.isdir(filepath):
                continue
            
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if not lines:
                # File is empty, skip
                continue

            # Check the first line after stripping whitespace
            first_line_stripped = lines[0].strip()

            if TARGET_LINE in first_line_stripped:
                # Use relative path for cleaner output
                relative_path = os.path.relpath(filepath, directory)
                print(f"-> Found target line in: {relative_path}. Modifying...")
                
                # Write back all lines except the first one
                new_content = lines[1:]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(new_content)
                
                modified_count += 1
            else:
                # print(f"File: {filepath} does not start with the target line. Skipping.")
                pass

        except FileNotFoundError:
            # Should not happen with glob results, but good practice
            print(f"Error: File not found: {filepath}")
        except Exception as e:
            print(f"An unexpected error occurred while processing {filepath}: {e}")

    print("-" * 30)
    print(f"Cleanup complete. Total files modified: {modified_count}")
    print(f"Total .md files checked: {len(markdown_files)}")

if __name__ == "__main__":
    # The script will now recursively search for markdown files from where it is executed.
    cleanup_markdown_files()
