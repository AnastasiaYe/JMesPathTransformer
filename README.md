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
  cannot deal with $each and $exist
  do not have a async traverse 
  do not include other mapping functions
  cannot handle errors and exceptions
  only deal with one type of the JMESPath operation (the most direct and basic one)

Possible future development:
  adding evaluate function to identify and perform different JMESPath operations
  adding exception handler
  upgrading to support $each and $exist, async traverse and mapping functions


