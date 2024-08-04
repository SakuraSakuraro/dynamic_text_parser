# Dynamic text parser
For parsing text from sites with dynamically changing text

# Instructions for setup and run the script

1. **Enter the website address**  
  First you need to specify the address of your website. To do this, simply replaced the text `"enter website url"` in the code to your website URL. For example:
   ```python
   url = "example.com"
   ```

2. **Identify HTML-tag**  
   Next you need to specify the need HTML tag. Simply replace `"enter name html tag"` to you need name of the tag . For example, if your tag looks like this:
   ```html
   <a name="endofpage"></a>Random text
   ```
   Then in the code, you should specify:
   ```python
   end_tag = soup.find('a', {'name': 'endofpage'})
   ```

3. **Save file**  
   Don't forget saved your changes!

4. **Install requireds modules**  
   Before running the script, check you have installed all necessary modules. Your need:
   - `requests`
   - `beautifulsoup4`
   - `keyboard`  

5. **Run script**  
   Now, go to directory where your file is located and typing the command:
   ```bash
   python dynamic_text_parser.py
   ```
If you changed the file name, be sure to specify the new file name
