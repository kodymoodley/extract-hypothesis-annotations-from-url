# Hypothes.is annotation extractor

An extensible Python script for extracting [Hypothes.is](https://web.hypothes.is/) annotations from a web page located at a given URL.

##### Requirements:

+ [Python 3.7+](https://www.python.org/downloads/)
+ [Git](https://git-scm.com/) **or** an archive extractor like [7-Zip](https://www.7-zip.org/)

#### For Users: running the script

Steps:

1. Get a copy of the code:
    
    + If you are using Git, type this command in your commandline tool: `git clone https://github.com/kodymoodley/extract-hypothesis-annotations-from-url.git`
    + If you are using an archive extractor, download this repository's code archive from [here](https://github.com/kodymoodley/extract-hypothesis-annotations-from-url/archive/master.zip) and extract it to the desired folder on your file system.

2. In your commandline tool, change into the `extract-hypothesis-annotations-from-url/` directory of your copy of the code.

3. **Important:** create a fresh [virtual environment](https://docs.python.org/3/tutorial/venv.html) with a default or base installation of Python 3.7+  

4. Run the command `pip install -r requirements.txt` which will install all required libraries for the analyser in your fresh Python virtual environment.

5. On installation completion of the required libraries in Step 4, run the command `python extract_hypothesis_annotations_from_url.py --help`. This will display instructions on the inputs required for the script and where to obtain them

## Notes:

+ The script only extracts annotations **tags** for highlighted texts on the web page located at the input URL. Of course, you can extend this functionality and adapt the script for your specific purposes. 
+ [Hypothes.is API documentation](https://h.readthedocs.io/en/latest/api-reference/v1/)
+ You will need your Hypothes.is API key to use the script. You can find this here (after logging in to your Hypothes.is account): [https://hypothes.is/account/developer](https://hypothes.is/account/developer)

## License
Copyright (C) 2020, Kody Moodley

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
