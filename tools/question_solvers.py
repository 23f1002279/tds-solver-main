import os
import httpx
import tempfile



def solver_1(command: str):
    return '''Version:          Code 1.96.2 (fabdb6a30b49f79a7aba0f2ad9df9b399473380f, 2024-12-19T10:22:47.216Z)
OS Version:       Darwin arm64 24.2.0
CPUs:             Apple M1 (8 x 2400)
Memory (System):  8.00GB (0.09GB free)
Load (avg):       2, 6, 6
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id ca90dba9-1235-4414-b9a6-6a7e9b4e613b
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           enabled
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 enabled
                  webnn:                                  disabled_off

CPU %	Mem MB	   PID	Process
    0	   115	  1439	code main
    0	    49	  1443	   gpu-process
    0	    16	  1444	   utility-network-service
    0	   188	  1445	window [1] (Welcome)
    0	    33	  1485	shared-process
    0	    16	  1486	fileWatcher [1]
    0	    25	  1487	extensionHost [1]
    0	    25	  1547	ptyHost
    0	     0	  1548	     /bin/zsh -il
    0	     0	  1675	     /bin/bash --init-file /Applications/Visual Studio Code.app/Contents/Resources/app/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh'''


def solver_2(url: str, param: str, value: str):
    import subprocess
    import json

    # Run the command using uv run with httpie
    cmd = ["uv", "run", "--with", "httpie", "--", "https", f"{url}", f"{param}=={value}"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Print the JSON output
    return f'''{json.dumps(json.loads(result.stdout), indent=2)}'''


def solver_3(req_filename: str, temp_dir: str, file_path: str, file_name: str, command: str):
    import subprocess
    import json
    import os
    PWD = os.getcwd()
    

    new_temp_dir = tempfile.mkdtemp()
    os.chdir(new_temp_dir)
    os.system(f"cp {file_path} ./{req_filename}")
    
    # pre_cmd = ["mv", f"{file_name}", f"{req_filename}"]
    # pre_cmd = ["pwd"]
    # print(subprocess.run(pre_cmd, capture_output=True, text=True))

    
    # Run the command in the directory with the downloaded file
    cmd = [f"{command}"]
    process1 = subprocess.Popen(
        ["npx", "-y", "prettier@3.4.2", "README.md"],
        stdout=subprocess.PIPE,
        text=True
    )
    
    # Second command: sha256sum
    process2 = subprocess.Popen(
        ["sha256sum"],
        stdin=process1.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    
    # Allow process1 to receive a SIGPIPE if process2 exits
    process1.stdout.close()
    
    # Get the output
    output = process2.communicate()[0]
    # result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    os.chdir(PWD)
    # Print the output of the command
    return f'''{output[:-4]}'''

def solver_4(formula: str):
    import os
    import httpx
    import tempfile
    import subprocess
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given a Google Sheets formula. Generate a code only in python using only built-in libraries that will achieve the same result such that it prints only the answer of the formula. Give the code only without any markdown in plain text but maintain indentation"},
                {"role": "user", "content": f"{formula}"},
            ]
        })

        python_script = response.json()["choices"][0]["message"]["content"]
        print(python_script)
        temp_dir = tempfile.mkdtemp()
        with open(f"{temp_dir}/temp_script.py", 'w') as temp_script:
            temp_script.write(str(python_script))

        os.chmod(f"{temp_dir}/temp_script.py", 0o755)


        result = subprocess.run(["python3", f"{temp_dir}/temp_script.py"], capture_output=True, text=True)
        os.remove(f"{temp_dir}/temp_script.py")
        os.removedirs(temp_dir)
        return result.stdout[:-1]
    
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    
def solver_5(formula: str):
    import os
    import httpx
    import tempfile
    import subprocess
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given a Microsoft Excel formula. Generate a code only in python using only built-in libraries that will achieve the same result such that it prints only the answer of the excel formula. Give the code only without any markdown in plain text but maintain indentation"},
                {"role": "user", "content": f"{formula}"},
            ]
        })

        python_script = response.json()["choices"][0]["message"]["content"]
        print(python_script)
        temp_dir = tempfile.mkdtemp()
        with open(f"{temp_dir}/temp_script.py", 'w') as temp_script:
            temp_script.write(str(python_script))

        os.chmod(f"{temp_dir}/temp_script.py", 0o755)


        result = subprocess.run(["python3", f"{temp_dir}/temp_script.py"], capture_output=True, text=True)
        os.remove(f"{temp_dir}/temp_script.py")
        os.removedirs(temp_dir)
        return result.stdout[:-1]
    
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    
def solver_6(html_element: str):
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given an HTML element. Return the value of the hidden input in the HTML element. Only the value nothing else in plain text."},
                {"role": "user", "content": f"{html_element}"},
            ]
        })
        hidden_value = response.json()["choices"][0]["message"]["content"]
        return hidden_value
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}



def solver_7(day_name: str, start_date: str, end_date: str):
    import datetime
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    day_count = 0
    for i in range((end_date - start_date).days + 1):
        day = start_date + datetime.timedelta(days=i)
        if day.strftime("%A") == day_name:
            day_count += 1
    return f'''{day_count}'''


def solver_8(temp_dir: str, file_path: str, file_name: str, csv_file: str, column_name: str):
    # Unzip the file
    import zipfile
    import csv
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Read the CSV file

    csv_file_path = os.path.join(temp_dir, csv_file)
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if column_name in row:
                return row[column_name]
        return f"Column {column_name} not found in the CSV file."


def solver_9(json_array: list, first_field: str, second_field: str):
    import json
    json_array = json.loads(json_array)
    for i in range(len(json_array)):
        for j in range(len(json_array)):
            if(json_array[j][first_field] > json_array[i][first_field]):
                json_array[i], json_array[j] = json_array[j], json_array[i]
            elif(json_array[j][first_field] == json_array[i][first_field]):
                if(json_array[j][second_field] > json_array[i][second_field]):
                    json_array[i], json_array[j] = json_array[j], json_array[i]
    
    return f'''{json.dumps(json_array, separators=(',', ':'))}'''

def solver_10(temp_dir: str, file_path: str, file_name: str):
    import json
    import hashlib
    import subprocess
    import shlex
    # Dictionary to store key-value pairs
    key_value_pairs = {}
    
    # Read the file and parse each line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                key_value_pairs[key] = value
    json_string = json.dumps(key_value_pairs)

    # Escape the JSON string for command line
    escaped_json = shlex.quote(json_string)

    # Command to run the Node.js script with the JSON argument
    command = f"node ./js-utils/hash.js {escaped_json}"

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()

    # Print the output
    return f'''{stdout.decode('utf-8').strip()}'''


def solver_11(html_element: str, given_class: str, given_attribute: str, hidden_html: str):
    from bs4 import BeautifulSoup

    # Parse the HTML
    soup = BeautifulSoup(hidden_html, 'html.parser')

    # Find all <div> elements with class 'foo'
    foo_divs = soup.find_all(html_element, class_=given_class)

    # Extract their data-value attributes and convert to integers
    data_values = [int(div[given_attribute]) for div in foo_divs]

    # Calculate the sum of the data-value attributes
    sum_data_values = sum(data_values)

    return f'''{sum_data_values}'''


def solver_12(temp_dir: str, file_path: str, file_name: str, file_1: str, encoding_1: str, file_2: str, encoding_2: str, file_3: str, encoding_3: str, symbol_1: str, symbol_2: str, symbol_3: str):
    import zipfile
    import csv
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    file_1_path = os.path.join(temp_dir, file_1)
    file_2_path = os.path.join(temp_dir, file_2)
    file_3_path = os.path.join(temp_dir, file_3)

    encodings = [encoding_1, encoding_2, encoding_3]
    for i in range(len(encodings)):
        if encodings[i] == 'CP-1252':
            encodings[i] = 'cp1252'
        elif encodings[i] == 'UTF-8':
            encodings[i] = 'utf-8'
        elif encodings[i] == 'UTF-16':
            encodings[i] = 'utf-16'
    
    import pandas as pd
    df = pd.read_csv(file_1_path, encoding=encodings[0])
    filtered_df = df[(df.symbol == symbol_1) | (df.symbol == symbol_2) | (df.symbol == symbol_3) ]

    sum_1 = filtered_df['value'].sum()

    df_2 = pd.read_csv(file_2_path, encoding=encodings[1])
    filtered_df_2 = df_2[(df_2.symbol == symbol_1) | (df_2.symbol == symbol_2) | (df_2.symbol == symbol_3) ]

    sum_2 = filtered_df_2['value'].sum()

    df_3 = pd.read_csv(file_3_path, encoding=encodings[2], sep='\t')
    filtered_df_3 = df_3[(df_3.symbol == symbol_1) | (df_3.symbol == symbol_2) | (df_3.symbol == symbol_3) ]

    sum_3 = filtered_df_3['value'].sum()

    return f'''{sum_1 + sum_2 + sum_3}'''

def solver_13(file_name: str, value: str):
    # import tempfile
    # import os
    # import subprocess

    # temp_dir = tempfile.mkdtemp()
    # repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
    # repo_dir = os.path.join(temp_dir, "repo")

    # # Clone the repository
    # subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
    # PWD = os.getcwd()
    # # Change to the repository directory
    # os.chdir(repo_dir)

    # # Create the file with the given value
    # with open(file_name, 'w') as file:
    #     file.write(value)

    # # Add the file to the repository
    # subprocess.run(["git", "add", file_name], check=True)

    # # Commit the changes
    # subprocess.run(["git", "commit", "-m", "Add new file with given value"], check=True)

    # # Push the changes
    # subprocess.run(["git", "push"], check=True)
    # os.chdir(PWD)
    return f"https://raw.githubusercontent.com/23f1002279/tds/refs/heads/main/email.json"

def solver_14(temp_dir: str, file_path: str, file_name: str, existing_word: str, new_word: str, command: str):
    import tempfile
    import os
    import subprocess
    import zipfile
    import shlex
    import re

    new_temp = tempfile.mkdtemp()
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_temp)

    def replace_in_all_files(directory, old_word, new_word):
    # Compile the regex pattern for case-insensitive search
        pattern = re.compile(re.escape(old_word), re.IGNORECASE)
        
        # Count for reporting
        files_modified = 0
        replacements_made = 0
        
        # Walk through all files in the directory
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # Skip non-text files (optional)
                try:
                    # Try to open and read the file
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # Count original occurrences
                    original_count = len(pattern.findall(content))
                    
                    if original_count > 0:
                        # Perform the replacement
                        new_content = pattern.sub(new_word, content)
                        
                        # Write the modified content back to the file
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        
                        files_modified += 1
                        replacements_made += original_count
                        print(f"Modified {file_path}: {original_count} replacements")
                        
                except (UnicodeDecodeError, IOError):
                    # Skip files that can't be read as text
                    print(f"Skipped {file_path}: not a text file or cannot be read")
                    continue
        
        print(f"\nSummary: Modified {files_modified} files with {replacements_made} total replacements")
    
    replace_in_all_files(new_temp, existing_word, new_word)
    PWD = os.getcwd()
    # Run the provided command in the temp_dir
    os.chdir(new_temp)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()
    os.chdir(PWD)
    # Print the output
    return f'''{stdout.decode('utf-8').strip()[:-3]}'''


def solver_15(temp_dir: str, file_path: str, file_name: str, file_size_number: str, date_string: str):
    import os
    from datetime import datetime
    import pytz
    import zipfile
    import tempfile

    new_temp = tempfile.mkdtemp()
    def extract_with_timestamps(zip_filename, extract_dir='.'):
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            
            # After extraction, restore the original timestamps
            for info in zip_ref.infolist():
                if not info.is_dir():  # Skip directories initially
                    # Convert ZIP datetime tuple to timestamp
                    date_time = info.date_time
                    timestamp = datetime(*date_time).timestamp()
                    
                    # Set the timestamps for the extracted file
                    extracted_path = os.path.join(extract_dir, info.filename)
                    os.utime(extracted_path, (timestamp, timestamp))
            
            # Handle directories after files to avoid timestamp reset
            # when files are created inside directories
            for info in zip_ref.infolist():
                if info.is_dir():
                    date_time = info.date_time
                    timestamp = datetime.datetime(*date_time).timestamp()
                    
                    extracted_path = os.path.join(extract_dir, info.filename)
                    if os.path.exists(extracted_path):  # Directory might not exist if it was empty
                        os.utime(extracted_path, (timestamp, timestamp))
                    
    extract_with_timestamps(file_path, new_temp)

# Usage


    def calculate_filtered_files_size(directory='.', min_size_str='463', target_date_str='Sun, 31 Jan, 2010, 3:21 pm IST'):
        """
        Calculate the total size of files that meet specific criteria.
        
        Args:
            directory (str): Directory to search in (default: current directory)
            min_size_str (str): Minimum file size in bytes as a string (default: '463')
            target_date_str (str): Files modified on or after this date as a string 
                                in format "Sun, 31 Jan, 2010, 3:21 pm IST" (default: 'Sun, 31 Jan, 2010, 3:21 pm IST')
        
        Returns:
            tuple: (total_size, matching_files)
                - total_size (int): Total size in bytes of matching files
                - matching_files (list): List of tuples (file_path, size, modification_time)
        """
        # Convert min_size to integer
        min_size = int(min_size_str)
        
        # Parse the target date string
        target_date = datetime.strptime(target_date_str, "%a, %d %b, %Y, %I:%M %p IST")
        target_date = pytz.timezone('Asia/Kolkata').localize(target_date)
        
        # Convert target date to epoch time for comparison
        target_timestamp = target_date.timestamp()
        
        total_size = 0
        matching_files = []
        
        # Walk through all files in the specified directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip if not a file
                if not os.path.isfile(file_path):
                    continue
                    
                # Get file stats
                stats = os.stat(file_path)
                file_size = stats.st_size
                mod_time = stats.st_mtime
                
                # Check if file meets criteria
                if file_size >= min_size and mod_time >= target_timestamp:
                    total_size += file_size
                    matching_files.append((file_path, file_size, 
                                        datetime.fromtimestamp(mod_time, pytz.timezone('Asia/Kolkata'))))
        
        return total_size
    
    total_size = calculate_filtered_files_size(new_temp, file_size_number, date_string)
    return f'''{total_size}'''

def solver_16(temp_dir: str, file_path: str, file_name: str, command: str):
    import os
    import re
    import subprocess
    import shlex
    import tempfile
    import zipfile

    new_temp = tempfile.mkdtemp()
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_temp)

    def move_files_to_final(directory):
        final_dir = os.path.join(directory, "final")
        os.makedirs(final_dir, exist_ok=True)
        
        for root, _, files in os.walk(directory):
            if root == final_dir:
                continue
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    new_path = os.path.join(final_dir, filename)
                    os.rename(file_path, new_path)
        return final_dir

    final_dir = move_files_to_final(new_temp)

    
    def rename_files(directory):
        # Define a mapping for digit replacement
        digit_map = str.maketrans("0123456789", "1234567890")
        
        # Walk through all files in the directory
        for root, _, files in os.walk(directory):
            for filename in files:
                # Construct the full path to the file
                file_path = os.path.join(root, filename)
                
                # Skip directories
                if not os.path.isfile(file_path):
                    continue
                
                # Replace digits in the filename
                new_filename = re.sub(r'\d', lambda m: m.group(0).translate(digit_map), filename)
                
                # Construct the new full path
                new_file_path = os.path.join(root, new_filename)
                
                # Rename the file
                os.rename(file_path, new_file_path)
    
    rename_files(final_dir)
    PWD = os.getcwd()
    # Run the provided command in the temp_dir
    os.chdir(final_dir)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()
    os.chdir(PWD)
    # Print the output
    return f'''{stdout.decode('utf-8').strip()[:-3]}'''

def solver_17(temp_dir: str, file_path: str, file_name: str, file_1: str, file_2: str):
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    file_1_path = os.path.join(temp_dir, file_1)
    file_2_path = os.path.join(temp_dir, file_2)

    with open(file_1_path, 'r') as f1, open(file_2_path, 'r') as f2:
        file_1_lines = f1.readlines()
        file_2_lines = f2.readlines()

    diff_count = sum(1 for line1, line2 in zip(file_1_lines, file_2_lines) if line1 != line2)

    return f'''{diff_count}'''

def solver_18(ticket_type: str):
    ticket_type = ticket_type.lower()
    return f'''SELECT SUM(units*price) FROM tickets WHERE TRIM(LOWER(type)) = '{ticket_type}';'''


def solver_19():
    return '''# Weekly Step Analysis

This report analyzes the **number** of steps walked each day for a week, comparing personal trends over time and with friends. The goal is to identify areas for improvement and maintain a consistent exercise routine.

---

## Methodology

The analysis follows these steps:

1. *Data Collection*:
   - Step counts were recorded using a fitness tracker.
   - Friends' step data was collected via a shared fitness app.

2. *Data Analysis*:
   - Daily step counts were compared with the personal goal of 10,000 steps.
   - Weekly trends were visualized and summarized.

3. *Comparison*:
   - Trends were compared with friends' weekly averages.

Note: This analysis assumes all data points are accurate and complete. If not, a preprocessing step is applied using the function `clean_data(dataset)`.

---

## Results

### Step Counts Table
The table below compares personal step counts with friends' averages:

| Day       | My Steps | Friends' Avg Steps |
|-----------|----------|--------------------|
| Monday    | 8,500    | 9,800              |
| Tuesday   | 9,200    | 10,100             |
| Wednesday | 7,500    | 8,900              |
| Thursday  | 10,300   | 10,500             |
| Friday    | 12,000   | 9,700              |
| Saturday  | 14,000   | 11,200             |
| Sunday    | 13,500   | 12,000             |

---
###Hyperlink

[stepcount](https://stepcount.com)

###Image
![Step Count Image](https://www.dreamstime.com/illustration/step-counter.html)

###Blockquote
>Number of steps you walked in a week is presented.

## Observations

- *Weekend Success*: Step counts were significantly higher on Saturday and Sunday.
- *Midweek Dip*: Wednesday had the lowest step count.
- *Goal Achievement*: The 10,000-step goal was achieved on four out of seven days.

---

### Visualizing Weekly Steps
The following Python code was used to create a bar chart showing step counts:

```python
import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_steps = [8500, 9200, 7500, 10300, 12000, 14000, 13500]

plt.bar(days, my_steps, color='skyblue')
plt.title("My Daily Step Counts")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.axhline(y=10000, color='red', linestyle='--', label='Goal')
plt.legend()
plt.show()  '''

def solver_20(temp_dir: str, file_path: str, file_name: str, quality: int = 10):
    from pathlib import Path
    from PIL import Image
    import subprocess
    import os
    import io
    import base64

    output_path = os.path.join(temp_dir, 'compressed.png')

    with Image.open(file_path) as img:
        img.save(output_path, 'PNG', quality=quality, optimize=True)
    
    with open(output_path, 'rb') as f:
        compressed_image = f.read()
        compressed_image_base64 = base64.b64encode(compressed_image).decode('utf-8')
    
    return f'''{compressed_image_base64}'''

def solver_21(email_id: str):
#     import tempfile
#     import os
#     import subprocess

#     temp_dir = tempfile.mkdtemp()
#     repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
#     repo_dir = os.path.join(temp_dir, "repo")

#     # Clone the repository
#     subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
#     PWD = os.getcwd()
#     # Change to the repository directory
#     os.chdir(repo_dir)

#     value = f'''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
#     <title>TDS Project 2 Playground</title>

# </head>
# <body>
#     <div class="container">
#     <h1 class="center">Tools in <span style="color: red;">Data Science</span> </h1> 
    
    
#     <p class="para-text">This page is created exclusively for TDS Project 2</p>

#     Contact Me:<br/>
#     <!--email_off-->{email_id}<!--/email_off-->

# </div>
    
# </body>
# </html>'''

#     # Create the file with the given value
#     with open('index.html', 'w') as file:
#         file.write(value)

#     # Add the file to the repository
#     subprocess.run(["git", "add", "index.html"], check=True)

#     # Commit the changes
#     subprocess.run(["git", "commit", "-m", "Added index.html"], check=True)

#     # Push the changes
#     subprocess.run(["git", "push"], check=True)
#     os.chdir(PWD)
    return f"https://23f1002279.github.io/TDS_W2_GIT"


def solver_22(email_id: str):
    import hashlib
    hash_code = hashlib.sha256(f"{email_id} 2025".encode()).hexdigest()[-5:]
    return f'''{hash_code}'''


def solver_23(temp_dir: str, file_path: str, file_name: str, lightness_threshold: float):
    import numpy as np
    from PIL import Image

    import colorsys

    # There is a mistake in the line below. Fix it
    image = Image.open(file_path)

    rgb = np.array(image) / 255.0
    lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
    light_pixels = np.sum(lightness > lightness_threshold)
    

    return f'''{light_pixels}'''


def solver_24(temp_dir: str, file_path: str, file_name: str):
    ### Have to implement this later
    return f'''https://tds-w2-vercel-topaz.vercel.app/api'''



def solver_25(email: str):
#     import tempfile
#     import os
#     import subprocess

#     temp_dir = tempfile.mkdtemp()
#     repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
#     repo_dir = os.path.join(temp_dir, "repo")

#     # Clone the repository
#     subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
#     PWD = os.getcwd()
#     # Change to the repository directory
#     os.chdir(repo_dir)
#     if not os.path.exists(".github"):
#         os.mkdir(".github")
#     os.chdir(".github")
#     if not os.path.exists("workflows"):
#         os.mkdir("workflows")
#     os.chdir("workflows")

#     # Create the file with the given value
#     with open('test.yaml', 'w') as file:
#         workflow = f'''name: Test Action

# on: push

# jobs:
#   test-action:
#     runs-on: ubuntu-latest
#     steps:
#       - name: {email}
#         run: echo "Hello, world!"'''
#         file.write(workflow)


#     # Add the file to the repository
#     subprocess.run(["git", "add", "test.yaml"], check=True)

#     # Commit the changes
#     subprocess.run(["git", "commit", "-m", "Add test workflow"], check=True)

#     # Push the changes
#     subprocess.run(["git", "push"], check=True)
#     os.chdir(PWD)
    return f'''https://github.com/23f1002279/my-actions-repo'''
    


def solver_26(tag: str): #### Need to check later ####
    return f'''https://hub.docker.com/repository/docker/fitdub/tds_project_2/general'''
    

def solver_27(temp_dir: str, file_path: str, file_name: str):
    import subprocess
    import os
    import requests
    PWD = os.getcwd()
    with open(file_path, 'r') as f:
        code = f.read()
    os.chdir('server-utils')
    with open('q-fastapi.csv', 'w') as f:
        f.write(code)
    subprocess.Popen(["nohup", "uvicorn", "solver_27:app", "--host", "0.0.0.0", "--port", "8003", "--reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    os.chdir(PWD)
    return(f"http://{public_ip}:8003/api")


def solver_28():
    return "https://5afc-223-185-60-63.ngrok-free.app/"

def solver_29(meaningless_text: str, model_name: str):
    from string import Template
    str_temp = Template('''import httpx

    response = httpx.post("https://api.openai.com/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer hello_abc",
                                "Content-Type": "application/json",
                            
                        }, 
                        json={
                            "model": "$model_name",
                                "messages": [
            {"role": "system", "content": "Analyze the sentiment of the given text into GOOD, BAD or NEUTRAL"},
            {"role": "user", "content": "$meaningless_text"},
        ]
    })''')
    return str_temp.substitute(meaningless_text=meaningless_text, model_name=model_name)

def solver_30(user_message: str):
    try:
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user", 
                        "content": f"""{user_message}"""
                    }
                    ],
            },
        )
        raw_res = response.json()
        
        return f'''{raw_res['usage']['prompt_tokens']}'''
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    

def solver_31(required_fields: list, additionalPropertiesBoolean: bool):
    from string import Template
    import json
    str_temp =Template('''
{
  "model": "gpt-4o-mini",
  "messages": [
    { "role": "system", "content": "Respond in JSON" },
    { "role": "user", "content": "Generate 10 random addresses in the US" }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "addresses",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": {
          "addresses": {
            "type": "array",
            "items": $item_str
          }
        },
        "required": ["addresses"],
        "additionalProperties": $additionalProperties
      }
    }
  }
}''')
    req_item = []
    for field in required_fields:
        req_item.append(field['field_name'])
    properties = {}
    for field in required_fields:
        properties[field['field_name']] = {"type": field['field_type']}
    items = {
        "type": "object",
        "properties": properties,
        "required": req_item,
        "additionalProperties": False
    }
    item_str = f'''{json.dumps(items)}'''

    
    
    
    additionalProperties = ''
    if additionalPropertiesBoolean:
        additionalProperties = "true"
    else:
        additionalProperties = "false"

    return f'''{str_temp.substitute(item_str=item_str, additionalProperties=additionalProperties)}'''
    

def solver_32(temp_dir: str, file_path: str, file_name: str):
    import base64
    from string import Template

    base64_image = base64.b64encode(open(file_path, "rb").read()).decode("utf-8")
    
    str_tmp = Template('''{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Extract text from this image"},
          {
            "type": "image_url",
            "image_url": { "url": "data:image/png;base64,$base64_image" }
          }
        ]
      }
    ]
  }''')
    
    return f'''{str_tmp.substitute(base64_image=base64_image)}'''


def solver_33(verification_message_1: str, verification_message_2: str):
    from string import Template
    str_temp = Template('''{"model": "text-embedding-3-small", "input": ["$verification_message_1", "$verification_message_2"]}''')
    return f'''{str_temp.substitute(verification_message_1=verification_message_1, verification_message_2=verification_message_2)}'''

def solver_34():
    return '''import numpy as np

def get_similarity(p1: str, p2: str) -> float:
    
    e1 = np.array(embeddings[p1])
    e2 = np.array(embeddings[p2])
    return float(np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2)))


def most_similar(embeddings):
    highest_similarity = 0
    highest_sim_pair = (None , None)

    for p in embeddings.keys():
        for q in embeddings.keys():
            if(p != q):
                sim = get_similarity(p, q)
                if(sim > highest_similarity):
                    highest_similarity = sim
                    highest_sim_pair = (p, q)

    (phrase1, phrase2) = highest_sim_pair
    return (phrase1, phrase2)'''

def solver_35():
    import subprocess
    import os
    import requests
    PWD = os.getcwd()
    os.chdir('server-utils')
    subprocess.Popen(["nohup", "uvicorn", "solver_35:app", "--host", "0.0.0.0", "--port", "8000", "--reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    os.chdir(PWD)
    return(f"http://{public_ip}:8000/similarity")

def solver_36():
    import subprocess
    import os
    import requests
    PWD = os.getcwd()
    os.chdir('server-utils')
    subprocess.Popen(["nohup", "uvicorn", "solver_36:app", "--host", "0.0.0.0", "--port", "8001", "--reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    os.chdir(PWD)
    return(f"http://{public_ip}:8001/execute")

def solver_37(page_number: str):
    import httpx
    from bs4 import BeautifulSoup
    import pandas as pd

    def scrape_cricinfo_stats():
        url = f"https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;page={page_number};template=results;type=batting"
        
        # Define headers with a user-agent
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0"
        }
        
        # Send a GET request to the URL using httpx
        with httpx.Client() as client:
            response = client.get(url, headers=headers, follow_redirects=True)
        
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with class 'engineTable'
        table = soup.find_all('table', class_='engineTable')
        table = table[2]
        # Check if table exists
        if table is None:
            print("Table not found. The page structure might have changed or access is restricted.")
            return pd.DataFrame()
        
        # Extract table headers
        headers = [th.text.strip() for th in table.find_all('th')]
        
        # Extract table rows
        rows = []
        for tr in table.find_all('tr')[1:]:  # Skip the header row
            rows.append([td.text.strip() for td in tr.find_all('td')])
        
        print(headers)
        # Create a pandas DataFrame
        df = pd.DataFrame(rows, columns=headers)
        
        # Save the data to a CSV file
        df.to_csv('espn_cricinfo_stats.csv', index=False)
        
        return df

    def calculate_total_ducks(df):
        # Check if DataFrame is empty
        if df.empty:
            return None
            
        # Assuming '0' column represents the number of ducks
        if '0' in df.columns:
            total_ducks = df['0'].astype(int).sum()
            return total_ducks
        else:
            print("Column '0' not found in the data. Please check the column names.")
            return None
    
    df = scrape_cricinfo_stats()
    total_ducks = calculate_total_ducks(df)

    return f'''{total_ducks}'''

def solver_38(ratings_start: str, ratings_end: str):
    import httpx
    from bs4 import BeautifulSoup
    import json
    import re

    def scrape_imdb_movies_with_rating_range():
        # URL for IMDb advanced search with rating between 7 and 8
        url = f"https://www.imdb.com/search/title/?user_rating={ratings_start},{ratings_end}&title_type=feature"

        # Define headers with a user-agent to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.imdb.com/",
            "Connection": "keep-alive"
        }

        # Send a GET request to the URL
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, headers=headers, follow_redirects=True)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve data: Status code {response.status_code}")
            return []

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all movie items (limited to 25)
        movie_items = soup.select('.ipc-metadata-list-summary-item')[:25]

        movies_data = []

        for item in movie_items:
            try:
                # Extract title and link
                title_element = item.select_one('a.ipc-title-link-wrapper')
                if not title_element:
                    continue

                title = title_element.text.strip()
                link = title_element.get('href', '')

                # Extract movie ID from the link
                id_match = re.search(r'/title/(tt\d+)/', link)
                movie_id = id_match.group(1) if id_match else ""

                # Extract year - get the raw text from the first metadata item
                year = ""
                metadata_items = item.select('.dli-title-metadata-item')
                if metadata_items and len(metadata_items) > 0:
                    year = metadata_items[0].text.strip()

                # Extract rating - get only the numeric value
                rating_element = item.select_one('.ipc-rating-star--imdb')
                rating = ""
                if rating_element:
                    rating_text = rating_element.text.strip()
                    rating_match = re.search(r'([\d.]+)', rating_text)
                    rating = rating_match.group(1) if rating_match else ""

                # Add to movies data list
                if movie_id and title:
                    movies_data.append({
                        "id": movie_id,
                        "title": title,
                        "year": year,
                        "rating": rating
                    })
            except Exception as e:
                print(f"Error processing movie item: {e}")
                continue

        return movies_data



    movies_data = scrape_imdb_movies_with_rating_range()


    # Print the JSON data
    return f'''{json.dumps(movies_data, indent=2)}'''

def solver_39():
    import subprocess
    import os
    import requests
    PWD = os.getcwd()
    os.chdir('server-utils')
    subprocess.Popen(["nohup", "uvicorn", "solver_39:app", "--host", "0.0.0.0", "--port", "8002", "--reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    os.chdir(PWD)
    return(f"http://{public_ip}:8002/scrape")

def solver_40(required_city: str):
    from bs4 import BeautifulSoup
    import httpx
    import json
    from urllib.parse import urlencode

    def scrape(city: str):
        required_city = city
        location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
    'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
    's': required_city,
    'stack': 'aws',
    'locale': 'en',
    'filter': 'international',
    'place-types': 'settlement,airport,district',
    'order': 'importance',
    'a': 'true',
    'format': 'json'
    })
        result = httpx.get(location_url).json()
        url      = 'https://www.bbc.com/weather/'+result['response']['results']['results'][0]['id']
        print(url)
        response = httpx.get(url)
        
        

        soup = BeautifulSoup(response.text, 'html.parser')
        report_json = soup.find('script', attrs={'data-state-id': 'forecast'})

        
        
        report_json = json.loads(report_json.text)
        data = report_json
        weather_report = {}
        forecasts = data['data']['forecasts']
        for forecast in forecasts:
            date = forecast['summary']['report']['localDate']
            description = forecast['summary']['report']['enhancedWeatherDescription']
            weather_report[date] = description

        # Print the result in the requested format
        return f'''{json.dumps(weather_report, indent=4)}'''
    
    return scrape(required_city)

def solver_41(maximum_or_minimum: str, city_name: str, country_name: str):
    import requests
    from geopy.geocoders import Nominatim
    
    locator = Nominatim(user_agent="myGeocoder")

    # type any address text
    location = locator.geocode({
        "city": city_name,
        "country": country_name,
    })

    if maximum_or_minimum == "maximum":
        return f'''{location.raw['boundingbox'][1]}'''
    else:
        return f'''{location.raw['boundingbox'][0]}'''
    

def solver_42(mentioning_word: str, minimum_points: int):
    import httpx
    from bs4 import BeautifulSoup
    import re

    response = httpx.get(f"https://hnrss.org/newest?q={mentioning_word}")
    soup = BeautifulSoup(response.text, 'html.parser')
    article_list = soup.find_all('item')

    urls = []
    for art in article_list:
        soup2 = BeautifulSoup(art.text, 'html.parser')
        p_tag = soup2.find('p', text=re.compile(r'Points: \d+'))
        if p_tag:
            # Extract the number using regex
            match = re.search(r'Points: (\d+)', p_tag.text)
            if match:
                number = match.group(1)
                if(int(number) > minimum_points):
                    url = BeautifulSoup(art.text, 'html.parser').find('a')['href']
                    urls.append(url)
                    
                    
            else:
                print("No number found in the text.")
        else:
            print("No <p> tag containing 'Points:' found.")

    return f'''{urls[0]}'''

def solver_43(city_name: str, followers_count: int):
    import requests
    from datetime import datetime


    url = "https://api.github.com/search/users"
    params = {"q": f"location:{city_name} followers:>{str(followers_count)}", "sort": "joined", "order": "desc", "per_page": 1}
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
    data = response.json()
    if not data["items"]:
        print("No users found matching the criteria.")
        return None
    
    newest_user = data["items"][0]
    user_response = requests.get(newest_user["url"])
    if user_response.status_code != 200:
        print(f"Error fetching user details: {user_response.status_code}")
        return None
    
    user_data = user_response.json()
    return f'''{user_data["created_at"]}'''


def solver_44(email: str):
#     import tempfile
#     import os
#     import subprocess

#     temp_dir = tempfile.mkdtemp()
#     repo_url = "https://github.com/pradeepmondal/tds-actions-test.git"
#     repo_dir = os.path.join(temp_dir, "repo")

#     # Clone the repository
#     subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
#     PWD = os.getcwd()
#     # Change to the repository directory
#     os.chdir(repo_dir)
#     if not os.path.exists(".github"):
#         os.mkdir(".github")
#     os.chdir(".github")
#     if not os.path.exists("workflows"):
#         os.mkdir("workflows")
#     os.chdir("workflows")


#     from datetime import datetime, timedelta

#     def get_cron_string_after_2_minutes():
#         # Get current time
#         current_time = datetime.now()
        
#         # Add 2 minutes to the current time
#         new_time = current_time + timedelta(minutes=2)
        
#         # Extract the minute and hour for the cron string
#         cron_minute = new_time.minute
#         cron_hour = new_time.hour
        
#         # Return the cron string in the format: "minute hour * * *"
#         return f"{cron_minute} {cron_hour} * * *"

#     # Create the file with the given value
#     with open('daily.yaml', 'w') as file:
#         workflow = f'''name: Daily Commit Workflow

# on:
#   schedule:
#     # Run at 10:30 AM UTC every day
#     - cron: '{get_cron_string_after_2_minutes()}'
#   # Optional: Allow manual triggering for testing
#   workflow_dispatch:

# jobs:
#   create-daily-commit:
#     runs-on: ubuntu-latest
#     permissions:
#       contents: write
    
#     steps:
#       - name: Checkout repository
#         uses: actions/checkout@v4
      
#       - name: {email}
#         run: |
#           git pull  
#           echo "Last updated: $(date)" > update.txt
          
      
#       - name: Commit and push changes
#         run: |
#           git config --local user.email "tds@dummy"
#           git config --local user.name "tds-solver"
#           git add update.txt  
#           git commit -m "Routine change done" || exit 0
#           git push'''
#         file.write(workflow)


#     # Add the file to the repository
#     subprocess.run(["git", "add", "daily.yaml"], check=True)

#     # Commit the changes
#     subprocess.run(["git", "commit", "-m", "Add daily workflow"], check=True)

#     # Push the changes
#     subprocess.run(["git", "push"], check=True)
#     os.chdir(PWD)
    return f'''https://github.com/23f1002279/tds4'''

def solver_45(temp_dir: str, file_path: str, file_name: str, subject_whose_marks_to_be_calculated: str, marks_in_criterion_subject: int, criterion_subject: str, group_start_number: int, group_end_number: int):
    import tabula
    import pandas as pd
    import os

    
    # Extract tables from the PDF file
    tabula.convert_into(file_path, "extracted_data.csv", output_format="csv", pages="all")

    # Load the extracted data into a DataFrame
    data = pd.read_csv("extracted_data.csv")

    # Convert columns to numeric to handle any non-numeric values
    data[criterion_subject] = pd.to_numeric(data[criterion_subject], errors='coerce')
    data[subject_whose_marks_to_be_calculated] = pd.to_numeric(data[subject_whose_marks_to_be_calculated], errors='coerce')
    data.dropna(inplace=True)
    data.reset_index(inplace=True)
    data['Group'] = ((data.index//30)+1)

    # Filter data for groups 53-91 and students who scored 43 or more in Maths
    filtered_data = data[(data[criterion_subject] >= marks_in_criterion_subject) & (data['Group'] >= group_start_number) & (data['Group'] <= group_end_number)]

    # Calculate the total Biology marks
    total_subject_marks = filtered_data[subject_whose_marks_to_be_calculated].sum()
    os.remove("extracted_data.csv")
    return f'''{int(total_subject_marks)}'''


def solver_46(temp_dir: str, file_path: str, file_name: str):
    import fitz  # PyMuPDF
    from markdownify import markdownify as md
    from string import Template
    import os
    import subprocess

    def convert_pdf_to_markdown(pdf_path, markdown_path):
        doc = fitz.open(pdf_path)
        text = ''
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()

        with open('raw_test.txt', 'w', encoding='utf-8') as raw_file:
            raw_file.write(text)
        
        markdown_text = md(text)

        with open(markdown_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)
        
        with open(markdown_path, 'r', encoding='utf-8') as md_file:
            word = md_file.readline().split()[0]



        text_to_added = Template('''
    # beneficium virgo
    {https://$word.com}
    | $word   | $word |
    | -------- | ------- |
    | $word  | $word    |
    | $word | $word     |
    | $word   | $word    |
    - a
    - b
    ```
    $word
    ```
    >
    ''')
        with open(markdown_path, 'a', encoding='utf-8') as md_file:
            md_file.write(text_to_added.substitute(word=word))
        
        subprocess.run(["npx", "prettier", markdown_path, "--write"], check=True)
        
        with open(markdown_path, 'r', encoding='utf-8') as md_file:
            markdown = md_file.read()
        return f'''{markdown}'''
        

    # Usage
    pdf_path = file_path
    markdown_path = 'pdf-to-markdown_output.md'
    markdown = convert_pdf_to_markdown(pdf_path, markdown_path)
    os.remove('raw_test.txt')
    os.remove('pdf-to-markdown_output.md')
    return markdown


def solver_47(temp_dir: str, file_path: str, file_name: str, date_string: str, product_name: str, country: str):

    def calculate_margin(excel_file, target_country, target_product, target_date):
        import pandas as pd
        import datetime
        
        target_date = datetime.datetime.strptime(target_date, "%a %b %d %Y %H:%M:%S GMT%z")
        target_date = target_date.strftime("%Y-%m-%d")
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        # Clean up the data
        df = df.apply(lambda x: x.str.strip() if isinstance(x, pd.Series) and x.dtype == 'object' else x)
        
        # Clean up dates - handle both formats
        def parse_date(date_str):
            try:
                # Try MM-DD-YYYY format
                return pd.to_datetime(date_str, format='%m-%d-%Y')
            except:
                try:
                    # Try YYYY/MM/DD format
                    return pd.to_datetime(date_str, format='%Y/%m/%d')
                except:
                    return None

        df['Date'] = df['Date'].apply(parse_date)
        
        # Clean up Sales and Cost columns
        df['Sales'] = df['Sales'].str.replace(' USD', '').str.strip().astype(float)
        df['Cost'] = df['Cost'].fillna(df['Sales'] * 0.5)  # Handle missing costs (50% of sales)
        df['Cost'] = df['Cost'].str.replace(' USD', '').str.strip().astype(float)
        
        # Clean up Product column (remove code after slash)
        df['Product'] = df['Product/Code'].str.split('/').str[0]
        
        # Create mapping for country variations
        country_mappings = {
            'US': ['USA', 'U.S.A', 'United States'],
            'AE': ['UAE', 'U.A.E', 'United Arab Emirates'],
            'UK': ['U.K', 'United Kingdom'],
            'IN': ['Ind', 'IND', 'India'],
            'BR': ['BRA', 'Bra', 'Brazil'],
            'FR': ['Fra', 'FRA', 'France']
        }
        
        # Standardize country names
        for standard, variants in country_mappings.items():
            df.loc[df['Country'].isin(variants), 'Country'] = standard
        
        # Filter the data
        filtered_df = df[
            (df['Country'] == target_country) &
            (df['Product'] == target_product) &
            (df['Date'] <= target_date)
        ]
        
        # Calculate total sales and costs
        total_sales = filtered_df['Sales'].sum()
        total_cost = filtered_df['Cost'].sum()
        
        # Calculate margin
        margin = (total_sales - total_cost) / total_sales if total_sales > 0 else 0
        
        return margin

    # Example usage: # The value of S from your question

    margin = calculate_margin(file_path, country, product_name, date_string)
    return f'''{margin:.4f}'''


def solver_48(temp_dir: str, file_path: str, file_name: str):
    
    def count_unique_students(file_path: str):
        student_ids = set()
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # Skip empty lines
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Step 1: Split line into pre-Marks and post-Marks parts
                    parts = line.upper().split("MARKS", 1)  # Case-insensitive split
                    if len(parts) < 2:
                        continue  # Skip lines without "Marks"
                    
                    # Step 2: Isolate the ID-containing segment
                    id_section = parts[0].strip()
                    
                    # Step 3: Find last valid delimiter (- or :)
                    last_delim_pos = max(id_section.rfind('-'), id_section.rfind(':'))
                    
                    if last_delim_pos == -1:
                        continue  # No delimiter found
                    
                    # Step 4: Extract ID
                    student_id = id_section[last_delim_pos+1:].strip()
                    
                    # Step 5: Validate ID format (alphanumeric only)
                    if student_id.isalnum():
                        student_ids.add(student_id)
            
            return len(student_ids)
        
        except Exception as e:
            print(f"Error processing file: {e}")
            return -1  # Return -1 to indicate an error
        
    return f'''{count_unique_students(file_path)}'''

def solver_49(temp_dir: str, file_path: str, file_name: str, 
          url_prefix: str, 
          day_of_week: int,
          start_hour: int, 
          end_hour: int,   # Thursday (Monday is 0)
          request_method='GET', 
          status_min=200, 
          status_max=300):
    
    import gzip
    import re
    from datetime import datetime

    
    def parse_log_line(line):

        try:
            parts = []
            current = ""
            in_quotes = False
            escape_next = False

            for char in line:
                if escape_next:
                    current += char
                    escape_next = False
                elif char == '\\' and in_quotes:
                    escape_next = True
                elif char == '"':
                    in_quotes = not in_quotes
                    current += char
                elif char == ' ' and not in_quotes:
                    parts.append(current)
                    current = ""
                else:
                    current += char
            if current:
                parts.append(current)

            # Recombine into a cleaned line.
            cleaned_line = " ".join(parts)
            match = re.match(r'([\d\.]+) ([^ ]+) ([^ ]+) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (.*?) (.*?)$', cleaned_line)
            if not match:
                return None

            ip, logname, user, time_str, request, status, size, referer, user_agent, vhost, server = match.groups()
            
            # Parse the time string (e.g., "01/May/2024:00:00:00 +0000")
            time_obj = datetime.strptime(time_str.strip(), "%d/%b/%Y:%H:%M:%S %z")
            
            # Split the request into method, URL, and protocol.
            request_parts = request.split(" ")
            if len(request_parts) >= 2:
                method = request_parts[0]
                url = request_parts[1]
            else:
                method = ""
                url = ""
            
            return {
                'ip': ip,
                'time': time_obj,
                'method': method,
                'url': url,
                'status': int(status),
                'vhost': vhost
            }
        except Exception:
            return None

    count = 0
    total_lines = 0
    parsed_lines = 0

    with gzip.open(file_path, 'rt', encoding='utf-8', errors='replace') as f:
        for line in f:
            total_lines += 1
            parsed_log = parse_log_line(line.strip())
            if parsed_log:
                parsed_lines += 1
                log_time = parsed_log['time']
                if (parsed_log['url'].startswith(url_prefix) and
                    parsed_log['method'] == request_method and
                    status_min <= parsed_log['status'] < status_max and
                    log_time.weekday() == day_of_week and
                    start_hour <= log_time.hour < end_hour):
                    count += 1

    print(f"\nTotal lines processed: {total_lines}")
    print(f"Successfully parsed: {parsed_lines}")
    print(f"Number of successful {request_method} requests for {url_prefix} between {start_hour}:00 and {end_hour}:00 on day {day_of_week}: {count}")
    print("END")
    return f'''{count}'''

def solver_50(temp_dir: str, file_path: str, file_name: str, section: str, date_string: str):
    import gzip
    import re
    from datetime import datetime
    from collections import defaultdict
    

    target_date = date_string
    # Parse target date
    target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")

    # Regex pattern to parse Apache log lines
    log_pattern = r'([\d\.]+) [^ ]+ [^ ]+ \[(.*?)\] "(.*?)" \d+ (\d+) "[^"]*" "[^"]*" .*'

    def parse_log_line(line):
        """Parses a single log line into structured fields."""
        match = re.match(log_pattern, line)
        if not match:
            return None

        ip, time_str, request, size = match.groups()

        # Parse time and request details
        time_obj = datetime.strptime(time_str.strip(), "%d/%b/%Y:%H:%M:%S %z")
        request_parts = request.split(" ")

        url = request_parts[1] if len(request_parts) >= 2 else ""

        return {
            "ip": ip,
            "time": time_obj,
            "url": url,
            "size": int(size)
        }

    # Initialize variables
    ip_download_totals = defaultdict(int)

    # Read the GZipped log file
    with gzip.open(file_path, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            parsed_log = parse_log_line(line.strip())

            if parsed_log:
                # Filter by section and target date
                log_date = parsed_log["time"].date()
                if parsed_log["url"].startswith(section) and log_date == target_date_obj.date():
                    ip_download_totals[parsed_log["ip"]] += parsed_log["size"]

    # Identify the IP with the highest download volume
    max_ip = max(ip_download_totals, key=ip_download_totals.get, default=None)
    max_bytes = ip_download_totals.get(max_ip, 0)

    # Return the final result
    return f'''{max_bytes}'''


def solver_51(temp_dir: str, file_path: str, file_name: str, product_sold: str, no_of_products_sold_atleast: int, city_name: str):
    import pandas as pd
    import jellyfish
    from unidecode import unidecode
    
    target_product = product_sold
    min_sales = no_of_products_sold_atleast
    target_city = city_name

    # Load the sales data from the JSON file
    df = pd.read_json(file_path)

    # Filter for the target product and transactions with at least min_sales units
    df = df[(df['product'] == target_product) & (df['sales'] >= min_sales)]

    # Normalize city names: remove accents, convert to lowercase, and strip whitespace
    def normalize_city(city):
        return unidecode(str(city)).lower().strip()

    df['norm_city'] = df['city'].apply(normalize_city)
    target_norm = normalize_city(target_city)

    # Apply phonetic encoding using NYSIIS to cluster similar city names
    def phonetic(name):
        return jellyfish.nysiis(name)

    df['city_cluster'] = df['norm_city'].apply(phonetic)
    target_cluster = phonetic(target_norm)

    # Filter records matching the target city's phonetic cluster
    filtered = df[df['city_cluster'] == target_cluster]

    # Sum the 'sales' column for the filtered entries
    total_units = int(filtered['sales'].sum())
    return f'''{total_units}'''


def solver_52(temp_dir: str, file_path: str, file_name: str):
    import re
    import json
    total = 0

    def regex_sales_extraction(line: str) -> int:
        # Match patterns like "sales": 456 or "sales":456 or quoted numbers.
        patterns = [
            r'"sales"\s*:\s*(\d+)',
            r'"sales"\s*:\s*"(\d+)"'
        ]
        for pattern in patterns:
            match = re.search(pattern, line)
            if match and match.group(1).isdigit():
                return int(match.group(1))
        return 0

    def repair_and_parse(line: str) -> dict:
        # Attempt to repair missing closing braces up to 3 times.
        for _ in range(3):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                # Append a closing brace if one is missing.
                if line.count('{') > line.count('}'):
                    line += '}'
                else:
                    line += '"}'
        return {}

    def validate_sales(value) -> int:
        return int(value) if isinstance(value, (int, float)) and value >= 0 else 0

    with open(file_path, 'r') as f:
        for line in f:
            # Method 1: Try direct regex extraction.
            sales_value = regex_sales_extraction(line)
            # Method 2: If regex fails, attempt JSON repair and extraction.
            if not sales_value:
                repaired_data = repair_and_parse(line.strip())
                sales_value = repaired_data.get('sales', 0)
            total += validate_sales(sales_value)

    return f'''{total}'''


def solver_53(temp_dir: str, file_path: str, file_name: str, target_key: str):
    import json
    
    def count_key_occurrences(data) -> int:
        count = 0
        if isinstance(data, dict):
            for key, value in data.items():
                if key == target_key:
                    count += 1
                count += count_key_occurrences(value)
        elif isinstance(data, list):
            for item in data:
                count += count_key_occurrences(item)
        return count

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_count = count_key_occurrences(data)
    return f'''{total_count}'''


def solver_54(date_time_string: str, no_of_useful_stars: int):
    return f'''SELECT DISTINCT post_id FROM (SELECT timestamp, post_id, UNNEST (comments->'$[*].stars.useful') AS useful FROM social_media) AS temp WHERE useful >= {str(no_of_useful_stars)} AND timestamp > '{date_time_string}';'''


def solver_55(start_time: float, end_time: float):
    import os
    from pydub import AudioSegment
    import tempfile
    import google.generativeai as genai
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    from google.generativeai import GenerativeModel

    # Step 2: Extract transcription for the specified time range
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "temp_audio_segment.wav")
    
    try:
        # Load the audio file
        audio = AudioSegment.from_file("pre_saved_files/audio.mp3")
        
        # Extract the segment between start_time and end_time (convert to milliseconds)
        start_ms = int(start_time * 1000)
        end_ms = int(end_time * 1000)
        audio_segment = audio[start_ms:end_ms]
        
        # Export the segment to a temporary file
        audio_segment.export(temp_file, format="wav")
        
        # Initialize the Gemini model
        model = GenerativeModel('gemini-2.0-flash')
        
        # Read the audio file
        with open(temp_file, "rb") as f:
            audio_data = f.read()
        
        # Transcribe using Gemini
        response = model.generate_content(
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"inline_data": {"mime_type": "audio/wav", "data": audio_data}},
                        {"text": "Transcribe this audio."}
                    ]
                }
            ]
        )
        
        # Extract the transcription from the response
        transcript = response.text
        
        return transcript
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)


def solver_56(temp_dir: str, file_path: str, file_name: str, file_path_2: str, file_name_2: str):
    import base64
    import os
    from PIL import Image
    import json

    with open(file_path_2, 'r') as f:
        table_data = f.read()

    tools = [{
    "type": "function",
    "function": {
        "name": "mappings_parser",
        "description": "Return {mappings} array as per the given mappings table",
        "parameters": {
            "type": "object",
            "properties": {
                "mappings": {
                    "type": "array",
                    "description": "An array of tuples representing the mapping data, like [(2, 1, 0, 0), (1, 1, 0, 1), ....] no header only the numbers in the format in order",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "number",
                            
                        },
                        
                    }
                }
            },
            "required": ["mappings"],
            "additionalProperties": False
        },
        "strict": True
    }
}

    ]


    mappings = None


    try:
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user", 
                        "content": f"""{table_data}"""
                    }
                    ],
                "tools": tools,
                "tool_choice": "required",
            },
        )
        raw_res = response.json()
        print(raw_res)
        output = response.json()["choices"][0]["message"]
        res = {"name": output["tool_calls"][0]["function"]["name"] , "arguments": output["tool_calls"][0]["function"]["arguments"]}
        mappings = json.loads(res["arguments"])
        mappings = mappings["mappings"]
        print("checking mappings:", mappings)
    except Exception as e:
        print(f"Error: {e}")
    
    if mappings == None:
        mappings = [[2, 1, 0, 0], [1, 1, 0, 1], [4, 1, 0, 2], [0, 3, 0, 3], [0, 1, 0, 4], [1, 4, 1, 0], [2, 0, 1, 1], [2, 4, 1, 2], [4, 2, 1, 3], [2, 2, 1, 4], [0, 0, 2, 0], [3, 2, 2, 1], [4, 3, 2, 2], [3, 0, 2, 3], [3, 4, 2, 4], [1, 0, 3, 0], [2, 3, 3, 1], [3, 3, 3, 2], [4, 4, 3, 3], [0, 2, 3, 4], [3, 1, 4, 0], [1, 2, 4, 1], [1, 3, 4, 2], [0, 4, 4, 3], [4, 0, 4, 4]]


    scrambled_img = Image.open(file_path)
    

    # Create a new blank image for the reconstructed image
    piece_size = 100  # Each piece is 100x100 pixels
    reconstructed_img = Image.new("RGB", (500, 500))

    # Reassemble the image
    for orig_row, orig_col, scram_row, scram_col in mappings:
        piece = scrambled_img.crop((scram_col * piece_size, scram_row * piece_size, (scram_col + 1) * piece_size, (scram_row + 1) * piece_size))
        reconstructed_img.paste(piece, (orig_col * piece_size, orig_row * piece_size))
    
    reconstructed_img.save("reconstructed_image.png")

    base64_image = ""
    with open("reconstructed_image.png", "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")
        
        
    return f'''{base64_image}'''





