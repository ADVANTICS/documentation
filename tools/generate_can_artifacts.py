#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from pathlib import Path

def main():
    # Determine paths
    script_path = Path(__file__).resolve()
    tools_dir = script_path.parent
    # Assuming structure: workspace/Applications/documentation/tools/script.py
    # So workspace root is script.parent.parent.parent
    # But user said workspace is /home/amin/Documents/ADVANTICS/charge-controllers-workspace/Applications
    # And script is in .../Applications/documentation/tools
    # So workspace root relative to script is ../..
    workspace_root = tools_dir.parent.parent
    
    # Source files
    src_v2 = workspace_root / "etka-mcp-25-chargers/etka/chargers/advantics/generic/v2/Advantics_Generic_EVSE_protocol_v2.kcd"
    src_v3 = workspace_root / "etka-mcp-25-chargers/etka/chargers/advantics/generic/v3/Advantics_Generic_EVSE_protocol_v3.kcd"
    
    # Destination directory
    dest_dir = workspace_root / "documentation/products/shared-charge-controllers/charger-can-interfaces"
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Tool path
    kcd_to_dbc_tool = tools_dir / "kcd_to_dbc.py"
    
    files_to_process = [src_v2, src_v3]
    
    for src in files_to_process:
        if not src.exists():
            print(f"Error: Source file not found: {src}")
            continue
            
        # Copy file
        dest_kcd = dest_dir / src.name
        print(f"Copying {src.name} to {dest_dir}")
        shutil.copy2(src, dest_kcd)
        
        # Generate DBC
        dest_dbc = dest_dir / src.with_suffix('.dbc').name
        print(f"Generating DBC for {dest_kcd.name}...")
        
        cmd = [
            sys.executable,
            str(kcd_to_dbc_tool),
            "--kcd", str(dest_kcd),
            "--out", str(dest_dbc)
        ]
        
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error generating DBC for {src.name}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
