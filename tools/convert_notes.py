import os
import re

def convert_admonition_blocks(directory="."):
    """
    Finds and replaces custom markdown admonition blocks (e.g., '> [!WARNING]')
    and custom DLIST blocks (e.g., '> [!DLIST|label:...]') with the 
    MkDocs-compatible format (e.g., '!!! type [Title]').

    Args:
        directory (str): The root directory to start the recursive search from.
    """
    
    # 1. Regex for standard admonition blocks (WARNING, ATTENTION, etc.)
    # Content group (group 2) now uses a more greedy pattern: 
    # (?:^>.*\n?)+ to capture any line starting with '> ' (including blank ones like '> ')
    standard_admonition_pattern = re.compile(
        r'^> \[!(ATTENTION|CAUTION|DANGER|ERROR|HINT|IMPORTANT|NOTE|TIP|WARNING)\]\s*\n' # Block header
        r'((?:^>.*\n?)+)', # Enhanced Block content: captures lines starting with '> ' until the next line NOT starting with '>'
        re.MULTILINE | re.IGNORECASE
    )

    # 2. Regex for custom DLIST blocks (remains robust)
    dlist_admonition_pattern = re.compile(
        r'^> \[!DLIST\|label:([A-Za-z0-9_]+)\]\s*\n' # DLIST Block header, capturing label
        r'((?:^> [ \t]?.*\n?)+)', # Block content
        re.MULTILINE
    )

    print(f"🚀 Starting **recursive** conversion in root directory: {os.path.abspath(directory)}\n")
    processed_files_count = 0
    admonitions_count = 0

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    new_content = content
                    
                    
                    # --- Replacement function for DLIST blocks ---
                    def dlist_replacement_func(match):
                        nonlocal admonitions_count
                        admonitions_count += 1
                        
                        admonition_type = "note" 
                        title = match.group(1).replace('_', ' ') 
                        
                        content_lines = match.group(2).splitlines()
                        
                        new_content_lines = []
                        for line in content_lines:
                            # Remove the leading '>' and any following space/tab
                            stripped_line = line.lstrip('>').lstrip(' \t')
                            new_content_lines.append(stripped_line)
                        
                        # Reconstruct the block: !!! type "Title"
                        mkdocs_block = f"!!! {admonition_type} \"{title}\"\n"
                        
                        # Indent all lines of the content by 4 spaces
                        indented_content = '    ' + '\n    '.join(new_content_lines).strip()
                        
                        return f"{mkdocs_block}{indented_content}\n\n"

                    # --- Replacement function for Standard blocks ---
                    def standard_replacement_func(match):
                        nonlocal admonitions_count
                        admonitions_count += 1
                        
                        # Get the type and convert to lowercase
                        admonition_type = match.group(1).lower()
                        
                        # Get the content and strip the leading '> ' from each line
                        content_lines = match.group(2).splitlines()
                        
                        new_content_lines = []
                        for line in content_lines:
                            # Remove the leading '>' and any following space/tab
                            # This handles: '> ', '>  ', '> \t' and just '>' on a line
                            stripped_line = line.lstrip('>').lstrip(' \t')
                            new_content_lines.append(stripped_line)
                        
                        # Reconstruct the block in MkDocs Admonition format
                        mkdocs_block = f"!!! {admonition_type}\n"
                        
                        # Indent all lines of the content by 4 spaces
                        indented_content = '    ' + '\n    '.join(new_content_lines).strip()
                        
                        return f"{mkdocs_block}{indented_content}\n\n"

                    
                    # 1. Process DLIST blocks first
                    new_content = dlist_admonition_pattern.sub(dlist_replacement_func, new_content)

                    # 2. Process standard blocks (ATTENTION, WARNING, etc.)
                    new_content = standard_admonition_pattern.sub(standard_replacement_func, new_content)
                    
                    # Write back to the file only if changes were made
                    if new_content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✅ Modified: {file_path}")
                        processed_files_count += 1

                except Exception as e:
                    print(f"❌ Error processing file {file_path}: {e}")

    print("\n---")
    print(f"✨ Conversion Complete.")
    print(f"Files modified: **{processed_files_count}**")
    print(f"Admonition blocks converted: **{admonitions_count}**")

if __name__ == "__main__":
    convert_admonition_blocks(directory=".")