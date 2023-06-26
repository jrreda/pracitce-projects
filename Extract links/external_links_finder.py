import os
import re
import pandas as pd
from tqdm.auto import tqdm
from datetime import datetime


def find_external_links_in_file(file_path):
    cannot_read_files = []
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Find all <link> tags with href attributes
        link_tags = re.findall(r'<link[^>]+href=["\'](.*?)["\']', content)

        # Find all <img> tags with src attributes
        img_tags = re.findall(r'<img[^>]+src=["\'](.*?)["\']', content)

        # Find all @font-face declarations with src attributes
        font_face_tags = re.findall(
            r'@font-face[^}]+src:\s*url\(["\'](.*?)["\']', content
        )

        # Find all <script> tags with src attributes
        script_tags = re.findall(r'<script[^>]+src=["\'](.*?)["\']', content)

        # Filter out the external/CDN links
        external_links = [
            link
            for link in link_tags + img_tags + font_face_tags + script_tags
            if link.startswith(("http://", "https://"))
        ]

        return external_links
    except:
        print(f"Can't read {file_path}")
        cannot_read_files.append(file_path)


def search_project_files_for_external_links(project_path):
    # Define the file extensions to search
    file_extensions = [".html", ".php", ".blade.php"]

    # Collect external links and file information
    results = []
    for dirpath, dirnames, filenames in tqdm(os.walk(project_path)):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(dirpath, filename)
                file_external_links = find_external_links_in_file(file_path)

                # Get file information
                file_name = filename
                file_parent_folder = os.path.basename(dirpath)

                # Append results for each external link found in the file
                if file_external_links is not None:
                    for link in file_external_links:
                        results.append(
                            {
                                "Domain": re.search(
                                    "https?://([A-Za-z_0-9.-]+).*", link
                                ).group(1),
                                "External Link": link,
                                "File Name": file_name,
                                "File Parent Folder": file_parent_folder,
                                "File Path": file_path,
                            }
                        )
    return results


# search for the external links in the project
project_path = (
    r"C:\xampp\htdocs\glob\Code\html2"
)
external_links_results = search_project_files_for_external_links(project_path)


# Save the external links in a csv file
df = pd.DataFrame(
    data=external_links_results,
    columns=["Domain", "External Link", "File Name", "File Parent Folder", "File Path"],
)
now = datetime.utcnow().strftime("%Y-%m-%d")
df.to_csv(f"external-links_{now}.csv", index=False)
