question_templates = {
    1: '''Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of {command}?''',

    2: '''
Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
Send a HTTPS request to {url} with the URL encoded parameter {param} set to {email}
What is the JSON output of the command? (Paste only the JSON body, not the headers)''',

    3: '''Let's make sure you know how to use npx and prettier.
Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command}
What is the output of the command?''',
    
    4: '''
Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets.
{formula}
What is the result?''',

    5: '''
    Let's make sure you can write formulas in Microsoft Excel. Type this formula into Microsoft Excel.
Note: This will ONLY work in Office 365.
{excel_formula}
What is the result?''',

    6: '''{html_element}
Just above this paragraph, there's a hidden input with a secret value.
What is the value in the hidden input?''',

    7: '''How many {day_name} are there in the date range {start_date} to {end_date}?
The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).''',

    8: '''Download and unzip file  which has a single {csv_file} file inside.
What is the value in the {column_name} column of the CSV file?''',

    9: '''Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the {first_field} field. In case of a tie, sort by the {second_field} field. Paste the resulting JSON below without any spaces or newlines.
    {json_array}''',

    10: '''Download and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.
What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?''',

    11: '''Let's make sure you know how to select elements using CSS selectors. Find all {html_element}'s having a {given_class} class in the hidden element below. What's the sum of their {given_attribute} attributes?
{hidden_html}
Sum of data-value attributes:''',

    12: '''Download and process the files in  which contains three files with different encodings:
{file_1}: CSV file encoded in {encoding_1}
{file_2}: CSV file encoded in {encoding_2}
{file_3}: Tab-separated file encoded in {encoding_3}
Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches {symbol_1} OR {symbol_2} OR {symbol_3} across all three files.
What is the sum of all values associated with these symbols?''',

    13: '''Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called {file_name} with the value {value} and push it.
Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)''',

    14: '''Download  and unzip it into a new folder, then replace all {existing_word} (in upper, lower, or mixed case) with {new_word} in all files. Leave everything as-is - don't change the line endings.
What does running {command} in that folder show in bash?''',

    15: '''Download  and extract it. Use ls with options to list all files in the folder along with their date and file size.
What's the total size of all files at least {file_size_number} bytes large and modified on or after {date_string}?''',

    16: '''Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
What does running {command} in bash on that folder show?''',

    17: '''Download  and extract it. It has 2 nearly identical files, {file_1} and {file_2}, with the same number of lines.
How many lines are different between {file_1} and {file_2}?''',

    18: '''There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.
{ticket_table}
What is the total sales of all the items in the {ticket_type} ticket type? Write SQL to calculate it.''',

    19: '''Write documentation in Markdown for an **imaginary** analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include:
{markdown_requirements}
''',

    20: '''Download the image below and compress it losslessly to an image that is less than 1,500 bytes. By losslessly, we mean that every pixel in the new image should be identical to the original image.
Upload your losslessly compressed image (less than 1,500 bytes)''',

    21: '''Publish a page using GitHub Pages that showcases your work. Ensure that your email address {email_id} is in the page's HTML.
GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:
<!--email_off-->{email_id}<!--/email_off-->
What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/''',

    22: '''Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: {email_id}.
{python_code}
What is the result? (It should be a 5-character string)''',

    23: '''Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:
    {python_code}
    What is the result? (It should be a number)''',

    24: '''Download this  which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api''',

    25: '''Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address {email}. For example:
jobs:
  test:
    steps:
      - name: {email}
        run: echo "Hello, world!"
Trigger the action and make sure it is the most recent action.
What is your repository URL? It will look like: https://github.com/USER/REPO''',

    26: '''Create and push an image to Docker Hub. Add a tag named {tag} to the image.
What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general''',

    27: '''Download . This file has 2-columns:

studentId: A unique identifier for each student, e.g. 1, 2, 3, ...
class: The class (including section) of the student, e.g. 1A, 1B, ... 12A, 12B, ... 12Z
Write a FastAPI server that serves this data. For example, /api should return all students data (in the same row and column order as the CSV file) as a JSON like this:
{json_format}
If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api''',

    28: '''Ngrok is a tool that creates secure tunnels to your localhost, making your local development server accessible to the internet. It's essential for testing webhooks, sharing work in progress, or debugging applications in production-like environments.

Run the command uvx ngrok http 8000 to create a tunnel to your local server on port 8000. This generates a public URL that you can share with others.

To get started, log into ngrok.com and get an authtoken from the dashboard. Copy it. Then run:

ngrok config add-authtoken $YOUR_AUTHTOKEN
Now you can forward any local port to the internet. For example:
{codes}
Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6_K.llamafile model with it.

Create a tunnel to the Llamafile server using ngrok.

What is the ngrok URL? It might look like: https://[random].ngrok-free.app/

''',

    29: '''One of the test cases involves sending a sample piece of meaningless text:
{meaningless_text}
Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

Make sure you pass an Authorization header with dummy API key.
Use {model_name} as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be exactly the text contained above.
This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

Note: This uses a dummy httpx library, not the real one. You can only use:

response = httpx.get(url, **kwargs)
response = httpx.post(url, json=None, **kwargs)
response.raise_for_status()
response.json()''',

    30: '''To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.
One specific test case an understanding of text tokenization. Your task is to generate data for that test case.
Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:
{user_message}
... how many input tokens does it use up?''',

    31: '''As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:
Uses model gpt-4o-mini
Has a system message: Respond in JSON
Has a user message: Generate 10 random addresses in the US
Uses structured outputs to respond with an object addresses which is an array of objects with required fields: {required_fields} .
Sets additionalProperties to {additionalPropertiesBoolean} to prevent additional properties.
Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.
What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)''',

    32: '''Your team is tasked with integrating OpenAI's vision model into the invoice processing workflow. The chosen model, gpt-4o-mini, is capable of analyzing both text and image inputs simultaneously. When an invoice is received—for example, an invoice image may contain a vendor email like alice.brown@acmeglobal.com and a transaction number such as 34921. The system needs to extract all embedded text to automatically populate the vendor management system.
The automated process will send a POST request to OpenAI's API with two inputs in a single user message:
Text: A simple instruction {text_instruction}
Image URL: A base64 URL representing the invoice image that might include the email and the transaction number among other details.
Here is an example invoice image:
Write just the JSON body (not the URL, nor headers) for the POST request that sends these two pieces of content (text and image URL) to the OpenAI API endpoint.
Use gpt-4o-mini as the model.
Send a single user message to the model that has a text and an image_url content (in that order).
The text content should be {text_instruction}
Send the image_url as a base64 URL of the image above. CAREFUL: Do not modify the image.
Write your JSON body here:''',

    33: '''Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:
{verification_message_1}
{verification_message_2}
The goal is to capture this message, convert it into a meaningful embedding using OpenAI's text-embedding-3-small model, and subsequently use the embedding in a machine learning model to detect anomalies.
Your task is to write the JSON body for a POST request that will be sent to the OpenAI API endpoint to obtain the text embedding for the 2 given personalized transaction verification messages above. This will be sent to the endpoint https://api.openai.com/v1/embeddings.
Write your JSON body here:''',

    34: '''As part of a pilot project, ShopSmart has curated a collection of 25 feedback phrases that represent a variety of customer sentiments. Examples of these phrases include comments like “Fast shipping and great service,” “Product quality could be improved,” “Excellent packaging,” and so on. Due to limited processing capacity during initial testing, you have been tasked with determine which pair(s) of 5 of these phrases are most similar to each other. This similarity analysis will help in grouping similar feedback to enhance the company’s understanding of recurring customer issues.
ShopSmart has written a Python program that has the 5 phrases and their embeddings as an array of floats. It looks like this:
{embeddings}
Your task is to write a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.
Write your Python code here:''',

    35: '''Imagine you are an engineer on the InfoCore team. Your task is to build a FastAPI POST endpoint that accepts an array of docs and query string via a JSON body. The endpoint is structured as follows:
{post_req_structure}
Service Flow:
Request Payload: The client sends a POST request with a JSON body containing:
docs: An array of document texts from the internal knowledge base.
query: A string representing the user's search query.
Embedding Generation: For each document in the docs array and for the query string, the API computes a text embedding using text-embedding-3-small.
Similarity Computation: The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to determine which documents best match the intent of the query.
Response Structure: After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON response might look like this:
{response_structure}
Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2".
Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity''',

    36: '''Each question is direct and templatized, containing one or more parameters such as an employee or ticket number (which might be randomized). In the backend, a FastAPI app routes each request by matching the query to one of a set of pre-defined functions. The response that the API returns is used by OpenAI to call the right function with the necessary arguments.
Pre-Defined Functions:
For this exercise, assume the following functions have been defined:
{functions}
Each function has a specific signature, and the student’s FastAPI app should map specific queries to these functions.
Example Questions (Templatized with a Random Number):
{example_questions}
Develop a FastAPI application that:
Exposes a GET endpoint /execute?q=... where the query parameter q contains one of the pre-templatized questions.
Analyzes the q parameter to identify which function should be called.
Extracts the parameters from the question text.
Returns a response in the following JSON format:
{response_format}
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute''',

    37: '''ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages. Count the number of ducks in page number {page_number}.
Understanding the Data Source: ESPN Cricinfo's ODI batting statistics are spread across multiple pages, each containing a table of player data. Go to page number {page_number}.
Setting Up Google Sheets: Utilize Google Sheets' IMPORTHTML function to import table data from the URL for page number {page_number}.
Data Extraction and Analysis: Pull the relevant table from the assigned page into Google Sheets. Locate the column that represents the number of ducks for each player. (It is titled "0".) Sum the values in the "0" column to determine the total number of ducks on that page.
What is the total number of ducks across players on page number {page_number} of ESPN Cricinfo's ODI batting stats?
''',

    38: '''Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to access movie data.
Filter: Filter all titles with a rating between {ratings_start} and {ratings_start}.
Format: For up to the first 25 titles, extract the necessary details: ID, title, year, and rating. The ID of the movie is the part of the URL after tt in the href attribute. For example, tt10078772. Organize the data into a JSON structure as follows:
{json_structure}
Submit: Submit the JSON data in the text box below.
''',

    39: '''Write a web application that exposes an API with a single query parameter: ?country=. It should fetch the Wikipedia page of the country, extracts all headings (H1 to H6), and create a Markdown outline for the country. The outline should look like this:
{markdown_outline}
API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?''',

    40: '''As part of this initiative, you are tasked with developing a system that automates the following:
API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Mumbai. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
Data Transformation: Extract the localDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each localDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the localDate and the value is the enhancedWeatherDescription.
The output would look like this:
{json_format}
What is the JSON weather forecast description for {required_city}?''',

    41: '''What is the maximum latitude of the bounding box of the city Tehran in the country Iran on the Nominatim API?
API Integration: Use the Nominatim API to fetch geospatial data for a specified city within a country via a GET request to the Nominatim API with parameters for the city and country. Ensure adherence to Nominatim’s usage policies, including rate limiting and proper attribution.
Data Retrieval and Filtering: Parse the JSON response from the API. If multiple results are returned (e.g., multiple cities named “Springfield” in different states), filter the results based on the provided osm_id ending to select the correct city instance.
Parameter Extraction: Access the boundingbox attribute. Depending on whether you're looking for the minimum or maximum latitude, extract the corresponding latitude value.
Impact
By automating the extraction and processing of bounding box data, UrbanRide can:
Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs.
Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents.
Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements.
Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality.
What is the {maximum_or_minimum} latitude of the bounding box of the city {city_name} in the country {country_name} on the Nominatim API? Value of the {maximum_or_minimum} latitude''',

    42: '''Search using the Hacker News RSS API for the latest Hacker News post mentioning {mentioning_word} and having a minimum of {minimum_points} points. What is the link that it points to?
Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of points.
Extract and Present Data: Extract the most recent <item> from this result. Get the <link> tag inside it.
Share the result: Type in just the URL in the answer.
What is the link to the latest Hacker News post mentioning {mentioning_word} having at least {minimum_points} points?''',

    43: '''Using the GitHub API, find all users located in the city {city_name} with over {followers_count} followers.
When was the newest user's GitHub profile created?
API Integration and Data Retrieval: Leverage GitHub’s search endpoints to query users by location and filter them by follower count.
Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria.
Sort and Format: Identify the "newest" user by comparing the created_at dates provided in the user profile data. Format the account creation date in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z").
Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
''', 

    44: '''Create a scheduled GitHub action that runs daily and adds a commit to your repository. The workflow should:
Use schedule with cron syntax to run once per day (must use specific hours/minutes, not wildcards)
Include a step with your email {email} in its name
Create a commit in each run
Be located in .github/workflows/ directory
After creating the workflow:
Trigger the workflow and wait for it to complete
Ensure it appears as the most recent action in your repository
Verify that it creates a commit during or within 5 minutes of the workflow run
Enter your repository URL (format: https://github.com/USER/REPO):''',

    45: '''This file,  contains a table of student marks in Maths, Physics, English, Economics, and Biology.
Calculate the total {subject_whose_marks_to_be_calculated} marks of students who scored {marks_in_criterion_subject} or more marks in {criterion_subject} in groups {group_start_number}-{group_end_number} (including both groups).
Data Extraction:: Retrieve the PDF file containing the student marks table and use PDF parsing libraries (e.g., Tabula, Camelot, or PyPDF2) to accurately extract the table data into a workable format (e.g., CSV, Excel, or a DataFrame).
Data Cleaning and Preparation: Convert marks to numerical data types to facilitate accurate calculations.
Data Filtering: Identify students who have scored marks between 31 and Physics in groups 1-25 (including both groups).
Calculation: Sum the marks of the filtered students to obtain the total marks for this specific cohort.
What is the total {subject_whose_marks_to_be_calculated} marks of students who scored {marks_in_criterion_subject} or more marks in {criterion_subject} in groups {group_start_number}-{group_end_number} (including both groups).''',

    46: '''As part of the Documentation Transformation Project, you are a junior developer at EduDocs tasked with developing a streamlined workflow for converting PDF files to Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients.
 has the contents of a sample document.
Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible.
Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file.
Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission.
What is the markdown content of the PDF, formatted with prettier@3.4.2?''',

    47:'''You need to clean this Excel data and calculate the total margin for all transactions that satisfy the following criteria:
Time Filter: Sales that occurred up to and including a specified date (Tue Oct 24 2023 09:13:39 GMT+0530 (India Standard Time)).
Product Filter: Transactions for a specific product (Iota). (Use only the product name before the slash.)
Country Filter: Transactions from a specific country (IN), after standardizing the country names.
The total margin is defined as:

Your solution should address the following challenges:

Trim and Normalize Strings: Remove extra spaces from the Customer Name and Country fields. Map inconsistent country names (e.g., "USA", "U.S.A", "US") to a standardized format.
Standardize Date Formats: Detect and convert dates from "MM-DD-YYYY" and "YYYY/MM/DD" into a consistent date format (e.g., ISO 8601).
Extract the Product Name: From the Product field, extract the portion before the slash (e.g., extract "Theta" from "Theta/5x01vd").
Clean and Convert Sales and Cost: Remove the "USD" text and extra spaces from the Sales and Cost fields. Convert these fields to numerical values. Handle missing Cost values appropriately (50% of Sales).
Filter the Data: Include only transactions up to and including Tue Oct 24 2023 09:13:39 GMT+0530 (India Standard Time), matching product Iota, and country IN.
Calculate the Margin: Sum the Sales and Cost for the filtered transactions. Compute the overall margin using the formula provided.
By cleaning the data and calculating accurate margins, RetailWise Inc. can:

Improve Decision Making: Provide clients with reliable margin analyses to optimize pricing and inventory.
Enhance Reporting: Ensure historical data is consistent and accurate, boosting stakeholder confidence.
Streamline Operations: Reduce the manual effort needed to clean data from legacy sources.
Download the Sales Excel file: 

What is the total margin for transactions before {date_string} (India Standard Time) for {product_name} sold in {country} (which may be spelt in different ways)?''', #Do later

    48: '''As a data analyst at EduTrack Systems, your task is to process this text file and determine the number of unique students based on their student IDs. This deduplication is essential to:
Ensure Accurate Reporting: Avoid inflated counts in enrollment and performance reports.
Improve Data Quality: Clean the dataset for further analytics, such as tracking academic progress or resource allocation.
Optimize Administrative Processes: Provide administrators with reliable data to support decision-making.
You need to do the following:
Data Extraction: Read the text file line by line. Parse each line to extract the student ID.
Deduplication: Remove duplicates from the student ID list.
Reporting: Count the number of unique student IDs present in the file.
By accurately identifying the number of unique students, EduTrack Systems will:
Enhance Data Integrity: Ensure that subsequent analyses and reports reflect the true number of individual students.
Reduce Administrative Errors: Minimize the risk of misinformed decisions that can arise from duplicate entries.
Streamline Resource Allocation: Provide accurate student counts for budgeting, staffing, and planning academic programs.
Improve Compliance Reporting: Ensure adherence to regulatory requirements by maintaining precise student records.
Download the text file with student marks 
How many unique students are there in the file?''',

    49: '''As a data analyst, you are tasked with determining how many successful GET requests for pages under {url_prefix} were made on {day_of_week} between {start_hour} and {end_hour} during May 2024. This metric will help:

Scale Resources: Ensure that servers can handle the peak load during these critical hours.
Content Planning: Determine the popularity of regional content to decide on future content investments.
Marketing Insights: Tailor promotional strategies for peak usage times.
This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.

Each row has these fields:

IP: The IP address of the visitor
Remote logname: The remote logname of the visitor. Typically "-"
Remote user: The remote user of the visitor. Typically "-"
Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
Size: The size of the response in bytes. E.g. 1234
Referer: The referer URL. E.g. https://s-anand.net/
User agent: The browser used. This will contain spaces and might have escaped quotes.
Vhost: The virtual host. E.g. s-anand.net
Server: The IP address of the server.
The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)

All data is in the GMT-0500 timezone and the questions are based in this same timezone.

By determining the number of successful GET requests under the defined conditions, we'll be able to:

Optimize Infrastructure: Scale server resources effectively during peak traffic times, reducing downtime and improving user experience.
Strategize Content Delivery: Identify popular content segments and adjust digital content strategies to better serve the audience.
Improve Marketing Efforts: Focus marketing initiatives on peak usage windows to maximize engagement and conversion.
What is the number of successful GET requests for pages under {url_prefix} from {start_hour} until before {end_hour} on {day_of_week}?''',

    50: '''This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.
Each row has these fields:
IP: The IP address of the visitor
Remote logname: The remote logname of the visitor. Typically "-"
Remote user: The remote user of the visitor. Typically "-"
Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
Size: The size of the response in bytes. E.g. 1234
Referer: The referer URL. E.g. https://s-anand.net/
User agent: The browser used. This will contain spaces and might have escaped quotes.
Vhost: The virtual host. E.g. s-anand.net
Server: The IP address of the server.
The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)

All data is in the GMT-0500 timezone and the questions are based in this same timezone.

Filter the Log Entries: Extract only the requests where the URL starts with {section}. Include only those requests made on the specified {date_string}.
Aggregate Data by IP: Sum the "Size" field for each unique IP address from the filtered entries.
Identify the Top Data Consumer: Determine the IP address that has the highest total downloaded bytes. Reports the total number of bytes that this IP address downloaded.
Across all requests under {section} on {date_string}, how many bytes did the top IP address (by volume of downloads) download?''',

    51: '''As a data analyst at GlobalRetail Insights, you are tasked with extracting meaningful insights from this dataset. Specifically, you need to:
Group Mis-spelt City Names: Use phonetic clustering algorithms to group together entries that refer to the same city despite variations in spelling. For instance, cluster "Tokyo" and "Tokio" as one.
Filter Sales Entries: Select all entries where:
The product sold is {product_sold}.
The number of units sold is at least {no_of_products_sold_atleast}.
Aggregate Sales by City: After clustering city names, group the filtered sales entries by city and calculate the total units sold for each city.
By performing this analysis, GlobalRetail Insights will be able to:

Improve Data Accuracy: Correct mis-spellings and inconsistencies in the dataset, leading to more reliable insights.
Target Marketing Efforts: Identify high-performing regions for the specific product, enabling targeted promotional strategies.
Optimize Inventory Management: Ensure that inventory allocations reflect the true demand in each region, reducing wastage and stockouts.
Drive Strategic Decision-Making: Provide actionable intelligence to clients that supports strategic planning and competitive advantage in the market.
How many units of {product_sold} were sold in {city_name} on transactions with at least {no_of_products_sold_atleast} units''',

    52: '''As a data recovery analyst at ReceiptRevive Analytics, your task is to develop a program that will:
Parse the Sales Data:
Read the provided JSON file containing 100 rows of sales data. Despite the truncated data (specifically the missing id), you must accurately extract the sales figures from each row.
Data Validation and Cleanup:
Ensure that the data is properly handled even if some fields are incomplete. Since the id is missing for some entries, your focus will be solely on the sales values.
Calculate Total Sales:
Sum the sales values across all 100 rows to provide a single aggregate figure that represents the total sales recorded.
By successfully recovering and aggregating the sales data, ReceiptRevive Analytics will enable RetailFlow Inc. to:
Reconstruct Historical Sales Data: Gain insights into past sales performance even when original receipts are damaged.
Inform Business Decisions: Use the recovered data to understand sales trends, adjust inventory, and plan future promotions.
Enhance Data Recovery Processes: Improve methods for handling imperfect OCR data, reducing future data loss and increasing data accuracy.
Build Client Trust: Demonstrate the ability to extract valuable insights from challenging datasets, thereby reinforcing client confidence in ReceiptRevive's services.
Download the data from 
What is the total sales value?''',

    53: '''As a data analyst at DataSure Technologies, you have been tasked with developing a script that processes a large JSON log file and counts the number of times a specific key, represented by the placeholder {target_key}, appears in the JSON structure. Your solution must:
Parse the Large, Nested JSON: Efficiently traverse the JSON structure regardless of its complexity.
Count Key Occurrences: Increment a count only when {target_key} is used as a key in the JSON object (ignoring occurrences of {target_key} as a value).
Return the Count: Output the total number of occurrences, which will be used by the operations team to assess the prevalence of particular system events or errors.
By accurately counting the occurrences of a specific key in the log files, DataSure Technologies can:
Diagnose Issues: Quickly determine the frequency of error events or specific system flags that may indicate recurring problems.
Prioritize Maintenance: Focus resources on addressing the most frequent issues as identified by the key count.
Enhance Monitoring: Improve automated monitoring systems by correlating key occurrence data with system performance metrics.
Inform Decision-Making: Provide data-driven insights that support strategic planning for system upgrades and operational improvements.
Download the data from 
How many times does {target_key} appear as a key?''',

    54: '''Your task as a data analyst at EngageMetrics is to write a query that performs the following:
Filter Posts by Date: Consider only posts with a timestamp greater than or equal to a specified minimum time ({dat_time_string}), ensuring that the analysis focuses on recent posts.
Evaluate Comment Quality: From these recent posts, identify posts where at least one comment has received more than a given number of useful stars ({no_of_useful_starts}). This criterion filters out posts with low or mediocre engagement.
Extract and Sort Post IDs: Finally, extract all the post_id values of the posts that meet these criteria and sort them in ascending order.
By accurately extracting these high-impact post IDs, EngageMetrics can:

Enhance Reporting: Provide clients with focused insights on posts that are currently engaging audiences effectively.
Target Content Strategy: Help marketing teams identify trending content themes that generate high-quality user engagement.
Optimize Resource Allocation: Enable better prioritization for content promotion and further in-depth analysis of high-performing posts.
Write a DuckDB SQL query to find all posts IDs after {date_time_string} with at least 1 comment with {no_of_useful_stars} useful stars, sorted. The result should be a table with a single column called post_id, and the relevant post IDs should be sorted in ascending order.''', #Do later

    55: '''Access the Video: Use the provided YouTube link to access the mystery story audiobook.
Convert to Audio: Extract the audio for the segment between {start_time} and {end_time}.
Transcribe the Segment: Utilize automated speech-to-text tools as needed.
By producing an accurate transcript of this key segment, Mystery Tales Publishing will be able to:

Boost Accessibility: Provide high-quality captions and text alternatives for hearing-impaired users.
Enhance SEO: Improve the discoverability of their content through better keyword indexing.
Drive Engagement: Use the transcript for social media snippets, summaries, and promotional materials.
Enable Content Analysis: Facilitate further analysis such as sentiment analysis, topic modeling, and reader comprehension studies.
What is the text of the transcript of this Mystery Story Audiobook between {start_time} and {end_time} seconds?''',

    56: '''As a digital forensics analyst at PixelGuard Solutions, your task is to reconstruct the original image from its scrambled pieces. You are provided with:
The 25 individual image pieces (put together as a single image).
A mapping file detailing the original (row, col) position for each piece and its current (row, col) location.
Your reconstructed image will be critical evidence in the investigation. Once assembled, the image must be uploaded to the secure case management system for further analysis by the investigative team.
Understand the Mapping: Review the provided mapping file that shows how each piece's original coordinates (row, col) relate to its current scrambled position.
Reassemble the Image: Using the mapping, reassemble the 5x5 grid of image pieces to reconstruct the original image. You may use an image processing library (e.g., Python's Pillow, ImageMagick, or a similar tool) to automate the reconstruction process.
Output the Reconstructed Image: Save the reassembled image in a lossless format (e.g., PNG or WEBP). Upload the reconstructed image to the secure case management system as required by PixelGuard’s workflow.
By accurately reconstructing the scrambled image, PixelGuard Solutions will:
Reveal Critical Evidence: Provide investigators with a clear view of the original image, which may contain important details related to the case.
Enhance Analytical Capabilities: Enable further analysis and digital enhancements that can lead to breakthroughs in the investigation.
Maintain Chain of Custody: Ensure that the reconstruction process is documented and reliable, supporting the admissibility of the evidence in court.
Improve Operational Efficiency: Demonstrate the effectiveness of automated image reconstruction techniques in forensic investigations.
Here is the image. It is a 500x500 pixel image that has been cut into 25 (5x5) pieces:
Here is the mapping of each piece:
{mappings}
Upload the reconstructed image by moving the pieces from the scrambled position to the original position:'''








    




















}