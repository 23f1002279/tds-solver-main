solvers_descriptions = {
    1: {
        "type": "function",
        "function": {
            "name": "solver_1",
            "description": "Gives output of a specific command in VS code",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    2: {
        "type": "function",
        "function": {
            "name": "solver_2",
            "description": "Sends a HTTPS request to {url} with the URL encoded parameter {param} set to {email}",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "the URL to send the request to"
                    },
                    "param": {
                        "type": "string",
                        "description": "the URL encoded parameter"
                    },
                    "value": {
                        "type": "string",
                        "description": "the value set to the parameter"
                    }
                    

                },
                "required": ["url", "param", "value"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    3: {
        "type": "function",
        "function": {
            "name": "solver_3",
            "description": "Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command} . Use npx and prettier.",
            "parameters": {
                "type": "object",
                "properties": {
                    "req_filename": {
                        "type": "string",
                        "description": "the name that the file should be renamed to"
                    },
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["req_filename", "command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    4: {
        "type": "function",
        "function": {
            "name": "solver_4",
            "description": "Converts a Google Sheets formula to a Python code and returns the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "formula": {
                        "type": "string",
                        "description": "the Google Sheets formula"
                    },
                    

                },
                "required": ["formula"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    5: {
        "type": "function",
        "function": {
            "name": "solver_5",
            "description": "Converts a Microsoft excel_formula to a Python code and returns the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "formula": {
                        "type": "string",
                        "description": "the Microsoft Excel formula"
                    },
                    

                },
                "required": ["formula"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    6: {
        "type": "function",
        "function": {
            "name": "solver_6",
            "description": "Extracts the value from a hidden input",
            "parameters": {
                "type": "object",
                "properties": {
                    "html_element": {
                        "type": "string",
                        "description": "the HTML element"
                    },
                    

                },
                "required": ["html_element"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    7: {
        "type": "function",
        "function": {
            "name": "solver_7",
            "description": "Counts the number of {day_name} between {start_date} and {end_date}",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_name": {
                        "type": "string",
                        "description": "the day name"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "the start date"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "the end date"
                    }
                    

                },
                "required": ["day_name", "start_date", "end_date"],
                "additionalProperties": False
            },
            "strict": True
    }
    },

    8: {
        "type": "function",
        "function": {
            "name": "solver_8",
            "description": "Unzip and extracts the value in a given column from a CSV file",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_file": {
                        "type": "string",
                        "description": "the name of the CSV file"
                    },

                    "column_name": {
                        "type": "string",
                        "description": "the name of the column"
                    }             

                },
                "required": ["csv_file", "column_name"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    9: {
        "type": "function",
        "function": {
            "name": "solver_9",
            "description": "Sorts a {json_array} of objects by the value of the {first_field} field. In case of a tie, sort by the {second_field} field.",
            "parameters": {
                "type": "object",
                "properties": {
                    "json_array": {
                        "type": "string",
                        "description": "the JSON array of objects"
                    },
                    "first_field": {
                        "type": "string",
                        "description": "the first field for sorting"
                    },
                    "second_field": {
                        "type": "string",
                        "description": "the second field for sorting"
                    }
                    

                },
                "required": ["json_array", "first_field", "second_field"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    10: {
        "type": "function",
        "function": {
            "name": "solver_10",
            "description": "Converts a multi-cursor text into a single JSON object",
            "parameters": {
                "type": "object",
                "properties": {
                    

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    11: {
        "type": "function",
        "function": {
            "name": "solver_11",
            "description": "Finds all {html_element}'s having a {given_class} class in the {hidden_html}. Returns the sum of their {given_attribute} attributes",
            "parameters": {
                "type": "object",
                "properties": {
                    "html_element": {
                        "type": "string",
                        "description": "the HTML element"
                    },
                    "given_class": {
                        "type": "string",
                        "description": "the class name"
                    },
                    "given_attribute": {
                        "type": "string",
                        "description": "the attribute name"
                    },
                    "hidden_html": {
                        "type": "string",
                        "description": "it is termed as the hidden HTML but this is the html that is passed along with the prompt"
                    }
                    

                },
                "required": ["html_element", "given_class", "given_attribute", "hidden_html"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    12: {
        "type": "function",
        "function": {
            "name": "solver_12",
            "description": "Sum up all the values where the symbol matches {symbol_1} OR {symbol_2} OR {symbol_3} across all three files. The symbols are separated by OR in the format - {symbol_1} OR {symbol_2} OR {symbol_3}. Symbols would not include the 'OR' word",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol_1": {
                        "type": "string",
                        "description": "It is the first symbol to match. It would be between the word matches and the first OR like matches {symbol_1} OR. Make sure not to include the 'OR' word"
                    },
                    "symbol_2": {
                        "type": "string",
                        "description": "the second symbol to match, it will be after the first OR and before the second OR. It would not include the 'OR' word"
                    },
                    "symbol_3": {
                        "type": "string",
                        "description": "the third symbol to match, it will be just after the second OR. It would not include the 'OR' word"
                    },
                    "file_1": {
                        "type": "string",
                        "description": "the name of the first file"
                    },
                    "encoding_1": {
                        "type": "string",
                        "description": "the encoding of the first file"
                    },
                    "file_2": {
                        "type": "string",
                        "description": "the name of the second file"
                    },
                    "encoding_2": {
                        "type": "string",
                        "description": "the encoding of the second file"
                    },
                    "file_3": {
                        "type": "string",
                        "description": "the name of the third file"
                    },
                    "encoding_3": {
                        "type": "string",
                        "description": "the encoding of the third file"
                    }
                    

                },
                "required": ["symbol_1", "symbol_2", "symbol_3", "file_1", "encoding_1", "file_2", "encoding_2", "file_3", "encoding_3"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    13: {
        "type": "function",
        "function": {
            "name": "solver_13",
            "description": "Commit a single JSON file called {file_name} with the value {value} and push it. Enter the raw Github URL of email.json so we can verify it.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "type": "string",
                        "description": "the name of the file"
                    },
                    "value": {
                        "type": "string",
                        "description": "the value to be committed"
                    }
                    

                },
                "required": ["file_name", "value"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    14: {
        "type": "function",
        "function": {
            "name": "solver_14",
            "description": "This function replaces all {existing_word} with {new_word} in all files and Leave everything as-is, then run the command {command} T",
            "parameters": {
                "type": "object",
                "properties": {
                    "existing_word": {
                        "type": "string",
                        "description": "the word to be replaced"
                    },
                    "new_word": {
                        "type": "string",
                        "description": "the word to be replaced with"
                    },
                    "command": {
                        "type": "string",
                        "description": "the command to be run"
                    }
                    

                },
                "required": ["existing_word", "new_word", "command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    15: {
        "type": "function",
        "function": {
            "name": "solver_15",
            "description": "Lists all files in the folder along with their date and file size. Returns the total size of all files at least {file_size_number} bytes large and modified on or after {date_string}",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_size_number": {
                        "type": "string",
                        "description": "the minimum file size"
                    },
                    "date_string": {
                        "type": "string",
                        "description": "the date string in the format %a, %d %b, %Y, %I:%M %p %Z"
                    }
                    

                },
                "required": ["file_size_number", "date_string"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    16: {
        "type": "function",
        "function": {
            "name": "solver_16",
            "description": "Moves all files under folders into an empty folder. Then renames all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt. Then execute the given command {command}",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "the command to be run"
                    }
                    

                },
                "required": ["command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    17: {
        "type": "function",
        "function": {
            "name": "solver_17",
            "description": "Counts the number of lines that are different between {file_1} and {file_2}",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_1": {
                        "type": "string",
                        "description": "the name of the first file"
                    },
                    "file_2": {
                        "type": "string",
                        "description": "the name of the second file"
                    }
                    

                },
                "required": ["file_1", "file_2"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    18: {
        "type": "function",
        "function": {
            "name": "solver_18",
            "description": "Calculates total sales of all the items in the {ticket_type} ticket type. For that the ticket_type parameter is required.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticket_type": {
                        "type": "string",
                        "description": "the string containing the type of ticket"
                    }
                    

                },
                "required": ["ticket_type"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    19: {
        "type": "function",
        "function": {
            "name": "solver_19",
            "description": "Writes documentation in Markdown for an imaginary analysis of the number of steps you walked each day for a week, comparing over time and with friends.",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    20: {
        "type": "function",
        "function": {
            "name": "solver_20",
            "description": "Compresses the image losslessly to an image that is less than 1,500 bytes",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    21: {
        "type": "function",
        "function": {
            "name": "solver_21",
            "description": "Publishes a page using GitHub Pages that showcases your work. Ensures that your email address {email_id} is in the page's HTML.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_id": {
                        "type": "string",
                        "description": "the email ID"
                    }
                    

                },
                "required": ["email_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },


    22: {
        "type": "function",
        "function": {
            "name": "solver_22",
            "description": "Runs the given program on Google Colab, allowing all required access to your email ID: {email_id}",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_id": {
                        "type": "string",
                        "description": "the email ID"
                    },

                },
                "required": ["email_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    23: {
        "type": "function",
        "function": {
            "name": "solver_23",
            "description": "Runs the given code on Google Colab to calculate the number of pixels with a certain minimum brightness",
            "parameters": {
                "type": "object",
                "properties": {
                    "lightness_threshold": {
                        "type": "number",
                        "description": "the minimum brightness as described in the python code snippet"
                    }
            
                },
                "required": ["lightness_threshold"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    24: {
        "type": "function",
        "function": {
            "name": "solver_24",
            "description": "Calculates the average marks of all students in the class and deploy in vercel",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    25: {
        "type": "function",
        "function": {
            "name": "solver_25",
            "description": "Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address {email}.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "the email ID"
                    }
                    

                },
                "required": ["email"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    26: {
        "type": "function",
        "function": {
            "name": "solver_26",
            "description": "Create and push an image to Docker Hub. Add a tag named {tag} to the image.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tag": {
                        "type": "string",
                        "description": "the tag to be added"
                    }
                    

                },
                "required": ["tag"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    27: {
        "type": "function",
        "function": {
            "name": "solver_26",
            "description": "Creates a fastapi server and returns the url endpoint",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },


    28: {
        "type": "function",
        "function": {
            "name": "solver_28",
            "description": "Creates a tunnel to the Llamafile server using ngrok",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    29: {
        "type": "function",
        "function": {
            "name": "solver_29",
            "description": "Analyze the sentiment of the given {meaningless_text} into GOOD, BAD or NEUTRAL using OpenAI's {model_name}",
            "parameters": {
                "type": "object",
                "properties": {
                    "model_name": {
                        "type": "string",
                        "description": "the model name"
                    },
                    "meaningless_text": {
                        "type": "string",
                        "description": "the meaningless text"
                    }
                    

                },
                "required": ["model_name", "meaningless_text"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    30: {
        "type": "function",
        "function": {
            "name": "solver_30",
            "description": "Calulates the number of input tokens used by OpenAI's GPT-4o-Mini with just this user message: {user_message}",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_message": {
                        "type": "string",
                        "description": "the user message given in the prompt for which the input tokens are to be calculated. It is the paragrapth after the sentence - 'Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:' in the prompt and before the sentence: '... how many input tokens does it use up?' in the prompt"
                    }
                    

                },
                "required": ["user_message"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    31: {
        "type": "function",
        "function": {
            "name": "solver_31",
            "description": "Writes the JSON body to send to https://api.openai.com/v1/chat/completions for a specific request with the {required_fields} and {additionalPropertiesBoolean}",
            "parameters": {
                "type": "object",
                "properties": {
                    "required_fields": {
                    "type": "array",
                    "description": "Array of the required fields",
                    "items": {
                        "type": "object",
                        "properties": {
                        "field_name": {
                            "type": "string",
                            "description": "Name of the field"
                        },
                        "field_type": {
                            "type": "string",
                            "description": "Type of the field",
                            "enum": ["string", "number", "boolean", "date", "object"]
                        }
                        },
                        "required": ["field_name", "field_type"],
                        "additionalProperties": False
                    }
                    },
              
                    "additionalPropertiesBoolean": {
                        "type": "boolean",
                        "description": "the boolean value for additional properties"
                    }
                    

                },
                "required": ["required_fields", "additionalPropertiesBoolean"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    32: {
        "type": "function",
        "function": {
            "name": "solver_32",
            "description": "Extracts the required details as per the {text_instruction} from an image passed as base64 image to openai's API",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    33: {
        "type": "function",
        "function": {
            "name": "solver_33",
            "description": "Create embeddings of the two given verification messages {verification_message_1} and {verification_message_2} using OpenAI's API",
            "parameters": {
                "type": "object",
                "properties": {
                    "verification_message_1": {
                        "type": "string",
                        "description": "the first verification message"
                    },
                    "verification_message_2": {
                        "type": "string",
                        "description": "the second verification message"
                    }
                    
                },
                "required": ["verification_message_1", "verification_message_2"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    34: {
        "type": "function",
        "function": {
            "name": "solver_34",
            "description": "Creates a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity.",
            "parameters": {
                "type": "object",
                "properties": {

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    35: {
        "type": "function",
        "function": {
            "name": "solver_35",
            "description": "Calculates the cosine similarity between the query embedding and each document embedding.",
            "parameters": {
                "type": "object",
                "properties": {
                    
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    36: {
        "type": "function",
        "function": {
            "name": "solver_36",
            "description": "Implements function calling for the given functions",
            "parameters": {
                "type": "object",
                "properties": {
                    
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    37: {
        "type": "function",
        "function": {
            "name": "solver_37",
            "description": "Fetches the cricket data from the given {page_number} of ESPN Cricinfo's ODI batting stats",
            "parameters": {
                "type": "object",
                "properties": {
                    "page_number": {
                        "type": "string",
                        "description": "the page number"
                    }
                    
                },
                "required": ["page_number"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    38: {
        "type": "function",
        "function": {
            "name": "solver_38",
            "description": "Fetches imdb data for the titles between rating {ratings_start} and {ratings_end}",
            "parameters": {
                "type": "object",
                "properties": {
                    "ratings_start": {
                        "type": "string",
                        "description": "the start rating"
                    },
                    "ratings_end": {
                        "type": "string",
                        "description": "the end rating"
                    }

                    
                },
                "required": ["ratings_start", "ratings_end"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    39: {
        "type": "function",
        "function": {
            "name": "solver_39",
            "description": "Scrape the wikipedia page for a given country, write all the headings <h1>, <h2>, ...., <h6> in a markdown file. Generate a Markdown-formatted outline that reflects the hierarchical structure of the content.",
            "parameters": {
                "type": "object",
                "properties": {
 
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    40: {
        "type": "function",
        "function": {
            "name": "solver_40",
            "description": "Finds the JSON weather forecst description for the {required_city}",
            "parameters": {
                "type": "object",
                "properties": {
                    "required_city": {
                        "type": "string",
                        "description": "the city for which the weather forecast is required"
                    }
                    
                },
                "required": ["required_city"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    41: {
        "type": "function",
        "function": {
            "name": "solver_41",
            "description": "Finds the {maximum_or_minimum} latitude of the bounding box of the city {city_name} in the country {country_name} on the Nominatim API. Returns the value of the {maximum_or_minimum} latitude",
            "parameters": {
                "type": "object",
                "properties": {
                    "maximum_or_minimum": {
                        "type": "string",
                        "description": "either 'maximum' or 'minimum' string as per the prompt"
                    },
                    "city_name": {
                        "type": "string",
                        "description": "the city name"
                    },
                    "country_name": {
                        "type": "string",
                        "description": "the country name"
                    }
                    
                },
                "required": ["maximum_or_minimum", "city_name", "country_name"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    42: {
        "type": "function",
        "function": {
            "name": "solver_42",
            "description": "the link to the latest Hacker News post mentioning {mentioning_word} having at least {minimum_points} points",
            "parameters": {
                "type": "object",
                "properties": {
                    "mentioning_word": {
                        "type": "string",
                        "description": "the word mentioned in the post"
                    },
                    "minimum_points": {
                        "type": "number",
                        "description": "the minimum points"
                    }
                    
                },
                "required": ["mentioning_word", "minimum_points"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    43: {
        "type": "function",
        "function": {
            "name": "solver_43",
            "description": "Finds the newest github user located in the city {city_name} with over {followers_count} followers",
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {
                        "type": "string",
                        "description": "the city name"
                    },
                    "followers_count": {
                        "type": "number",
                        "description": "the followers count"
                    }
                    
                },
                "required": ["city_name", "followers_count"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    44: {
        "type": "function",
        "function": {
            "name": "solver_44",
            "description": "Creates a GitHub action with that include a step with the {email}",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "the email ID"
                    }
                    
                },
                "required": ["email"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    45: {
        "type": "function",
        "function": {
            "name": "solver_45",
            "description": "Finds the total {subject_whose_marks_to_be_calculated} marks of students who scored {marks_in_criterion_subject} or more marks in {criterion_subject} in groups {group_start_number}-{group_end_number} (including both groups).",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject_whose_marks_to_be_calculated": {
                        "type": "string",
                        "description": "the subject whose total marks are to be calculated"
                    },
                    "marks_in_criterion_subject": {
                        "type": "number",
                        "description": "the marks in the criterion subject"
                    },
                    "criterion_subject": {
                        "type": "string",
                        "description": "the criterion subject, that is the subject name in the codition"
                    },
                    "group_start_number": {
                        "type": "number",
                        "description": "the start group number, that is the starting group number in the condition"
                    },
                    "group_end_number": {
                        "type": "number",
                        "description": "the end group number, that is the ending group number in the condition"
                    }
                    
                },
                "required": ["subject_whose_marks_to_be_calculated", "marks_in_criterion_subject", "criterion_subject", "group_start_number", "group_end_number"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    46: {
        "type": "function",
        "function": {
            "name": "solver_46",
            "description": "Convert a pdf to a markdown file",
            "parameters": {
                "type": "object",
                "properties": {

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    47: {
        "type": "function",
        "function": {
            "name": "solver_47",
            "description": "Finds the total margin for transactions before {date_string} (India Standard Time) for {product_name} sold in {country} (which may be spelt in different ways)",
            "parameters": {
                "type": "object",
                "properties": {
                    "date_string": {
                        "type": "string",
                        "description": "the date string in the format '%a %b %d %Y %H:%M:%S GMT%z'"
                    },
                    "product_name": {
                        "type": "string",
                        "description": "the product name"
                    },
                    "country": {
                        "type": "string",
                        "description": "the country name code"
                    }

                },
                "required": ["date_string", "product_name", "country"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    48: {
        "type": "function",
        "function": {
            "name": "solver_48",
            "description": "Finds the number of unique students are there in the file",
            "parameters": {
                "type": "object",
                "properties": {

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    49: {
        "type": "function",
        "function": {
            "name": "solver_49",
            "description": "Finds the number of successful GET requests for pages under {url_prefix} from {start_hour} until before {end_hour} on {day_of_week}",
            "parameters": {
                "type": "object",
                "properties": {
                    "url_prefix": {
                        "type": "string",
                        "description": "the URL prefix, in the format '/url_prefix/' "
                    },
                    "start_hour": {
                        "type": "number",
                        "description": "the start hour"
                    },
                    "end_hour": {
                        "type": "number",
                        "description": "the end hour"
                    },
                    "day_of_week": {
                        "type": "number",
                        "description": "the day of the week in number, Monday is 0, Tuesday is 1, Wednesday is 2, Thursday is 3, Friday is 4, Saturday is 5, Sunday is 6"
                    }

                },
                "required": ["url_prefix", "start_hour", "end_hour", "day_of_week"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    50: {
        "type": "function",
        "function": {
            "name": "solver_50",
            "description": "Finds across all requests under {section} on {date_string}, how many bytes did the top IP address (by volume of downloads) download",
            "parameters": {
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": "the section name, in the format '/section/' "
                    },
                    "date_string": {
                        "type": "string",
                        "description": "the date string in the format 'YYYY-MM-DD'"
                    }

                },
                "required": ["section", "date_string"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    51: {
        "type": "function",
        "function": {
            "name": "solver_51",
            "description": "Finds How many units of {product_sold} were sold in {city_name} on transactions with at least {no_of_products_sold_atleast} units",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_sold": {
                        "type": "string",
                        "description": "the product sold"
                    },
                    "city_name": {
                        "type": "string",
                        "description": "the city name"
                    },
                    "no_of_products_sold_atleast": {
                        "type": "number",
                        "description": "the number of products sold atleast"
                    }
                },
                "required": ["product_sold", "city_name", "no_of_products_sold_atleast"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    52: {
        "type": "function",
        "function": {
            "name": "solver_52",
            "description": "Finds the total sales value",
            "parameters": {
                "type": "object",
                "properties": {

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    53: {
        "type": "function",
        "function": {
            "name": "solver_53",
            "description": "Finds how many times does {target_key} appear as a key",
            "parameters": {
                "type": "object",
                "properties": {
                    "target_key": {
                        "type": "string",
                        "description": "the target key"
                    }

                },
                "required": ["target_key"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    54: {
        "type": "function",
        "function": {
            "name": "solver_54",
            "description": "Finds the DuckDB SQL query to find all posts IDs after {date_time_string} with at least 1 comment with {no_of_useful_stars} useful stars, sorted. The result should be a table with a single column called post_id, and the relevant post IDs should be sorted in ascending order",
            "parameters": {
                "type": "object",
                "properties": {
                    "date_time_string": {
                        "type": "string",
                        "description": "the date time string in the ISO 8601 format"
                    },
                    "no_of_useful_stars": {
                        "type": "number",
                        "description": "the number of useful stars"
                    }

                },
                "required": ["date_time_string", "no_of_useful_stars"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    55: {
        "type": "function",
        "function": {
            "name": "solver_54",
            "description": "Finds the text of the transcript of this Mystery Story Audiobook between {start_time} and {end_time} seconds",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_time": {
                        "type": "number",
                        "description": "the starting timestamp"
                    },
                    "end_time": {
                        "type": "number",
                        "description": "the ending timestamp"
                    }

                },
                "required": ["start_time", "end_time"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    56: {
    "type": "function",
    "function": {
        "name": "solver_56",
        "description": "Reconstruct the image by moving the pieces from the scrambled position to the original position as per the given {mappings}",
        "parameters": {
            "type": "object",
            "properties": {

            },
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    }
}





    












}