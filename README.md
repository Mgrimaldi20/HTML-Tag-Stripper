# HTML Tag Stripper

A tool that strips HTML tags from a .html file to get the plain text.

## Options  
    `-h    
        Help. Print this message and exit.`        
        
    `<filename>`     
        The name of the file in the current directory to strip HTML tags from.  
        The output will be printed to the terminal and stored in a file called  
        "rawtxt.txt"

## Usage
	Package is imported with command `import htmlstripper`.  
	The class then needs to be created with `stripper = HTMLStripper()`.    
	Return the new string with stripped tags with `my_string = stripper.strip_tags(old_string)`.  
        
## Author  
    Written by Marco Grimaldi  
