# JMesPathTransformer
uncompleted code, only for reference 

This is a simple JSON transfomer based on JMESPath library. By providing a template, It will convert a JSON file into another JSON file in different format. 

Usage:
transform(input_json_file_name, template_json_file_name)

This will transform the input file. The result will be stored in a new file called 'output.json'

Functions:
transform: Transform an input Json file to an optimiazed format regarding the template
flatten: Do the traversal and flatten the input document to avoid nested dictionary
isJmesPathString: Determines that a string value is a JmesPath if it ends with "$path"
jmesPathValue: Performs a JmesPath query

Problems: 
Compared to the NodeJs version, this transformer:
  1. cannot deal with $each and $exist
  2. do not have an async traverse 
  3. do not include other mapping functions
  4. cannot handle errors and exceptions
  5. only deal with one type of the JMESPath operation (the most direct and basic one)

Possible future development:
  1. adding evaluate function to identify and perform different JMESPath operations
  2. adding exception handler
  3. upgrading to support $each and $exist, async traverse and mapping functions


