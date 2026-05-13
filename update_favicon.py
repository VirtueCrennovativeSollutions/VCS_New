import os
import re

def update_favicon(root_dir):
    favicon_tag_root = '<link href="images/favicon.ico" rel="shortcut icon" type="image/x-icon" />'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, root_dir)
                depth = rel_path.count(os.sep)
                
                prefix = '../' * depth
                favicon_tag = f'<link href="{prefix}images/favicon.ico" rel="shortcut icon" type="image/x-icon" />'
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Regex to find existing favicon links
                # It can be single line or multi-line
                pattern = re.compile(r'<link[^>]*rel=["\']shortcut icon["\'][^>]*>', re.IGNORECASE)
                
                if pattern.search(content):
                    new_content = pattern.sub(favicon_tag, content)
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                else:
                    # If not found, try to insert it after charset or title
                    if '<head>' in content:
                        head_pos = content.find('<head>') + 6
                        new_content = content[:head_pos] + '\n  ' + favicon_tag + content[head_pos:]
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Inserted: {file_path}")

if __name__ == "__main__":
    update_favicon('.')
