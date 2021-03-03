# Hypothes.is annotation extractor

An extensible Python command-line script for extracting [Hypothes.is](https://web.hypothes.is/) annotations from a web page located at a given URL or a local [PDF](https://www.iso.org/standard/51502.html) file.

##### Requirements:

+ [Python 3.7+](https://www.python.org/downloads/)
+ [Git](https://git-scm.com/) **or** an archive extractor like [7-Zip](https://www.7-zip.org/)
+ URL to a webpage that has Hypothes.is annotations on it / A direct URL or local filepath to a PDF file that contains Hypothes.is annotations
+ If you are extracting private (non-public) annotations from a Hypothes.is group, you need its [Group ID](https://web.hypothes.is/help/how-to-join-a-private-group/).
+ You will need your Hypothes.is API key to use the script. You can find this [here](https://hypothes.is/account/developer) after logging in to your Hypothes.is account.

#### For Users: running the script

Steps:

1. Get a copy of the code:
    
    + If you are using Git, type this command in your commandline tool: `git clone https://github.com/kodymoodley/extract-hypothesis-annotations-from-url.git`
    + If you are using an archive extractor, download this repository's code archive from [here](https://github.com/kodymoodley/extract-hypothesis-annotations-from-url/archive/master.zip) and extract it to the desired folder on your file system.

2. In your commandline tool, change into the `extract-hypothesis-annotations-from-url/` directory of your copy of the code.

3. **Important:** create a fresh [virtual environment](https://docs.python.org/3/tutorial/venv.html) with a default or base installation of Python 3.7+  

4. Run the command `pip install -r requirements.txt` which will install all required libraries for the extractor in your fresh Python virtual environment.

5. On installation completion of the required libraries in Step 4, run the command `python extract_hypothesis_annotations_from_url.py --help`. This will display instructions on the inputs required for the script and where to obtain them

## Notes:

+ The script only extracts annotation **tags** for highlighted texts on the web page located at the input URL or the local PDF file. Of course, you are free to extend this functionality and adapt the script for your specific purposes according to specified license.
+ [Hypothes.is API documentation](https://h.readthedocs.io/en/latest/api-reference/v1/)

## Acknowledgements:
This script makes use of [Sean Hammond's](https://www.seanh.cc/) Python [PDF fingerprinting code](https://www.seanh.cc/2017/11/22/pdf-fingerprinting/), which is a Python port of the PDF fingerprinting algorithm used in the [PDF.js](https://www.npmjs.com/package/pdfjs) library.

## License
Copyright (C) 2020, Kody Moodley

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
