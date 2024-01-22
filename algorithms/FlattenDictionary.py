"""
Flatten Dictionary

author: adambechtold
interviewer: Jimmy
whiteboardLink: https://link.excalidraw.com/l/ATbTqvQ19d9/6Mc8ozf3K2J
date: 2024.01.22
link: https://www.pramp.com/challenge/AMypWAprdmUlaP2gPVLZ
"""

def flatten_dictionary(dictionary):
  #return flatten_dict_with_prefix(dictionary, "")
  result = {}
  flatten_dict_top_down("", dictionary, result)
  return result
  

def flatten_dict_with_prefix(dictionary, prefix):
  result = {}

  for key, value in dictionary.items():
    # Add key to prefix (if key and prefix exist)
    key_to_add = ""
    if prefix and key != "":
      key_to_add = ".".join([prefix, key])
    elif not prefix:
      key_to_add = key
    else:
      key_to_add = prefix

    # If value is not a dict, it is already flat. Add it to the flattened dictionary
    if not isinstance(value, dict):
      result[key_to_add] = value
    
    # Else, flatten the children of this value and add them to the flattend dictionary
    #   Each should use the key_to_add as their prefix
    else:
      for flat_key, flat_value in flatten_dict_with_prefix(value, key_to_add).items():
        result[flat_key] = flat_value

  return result

# This almost works.
# Try this input: {"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}
def flatten_dict_top_down(initial_key, dictionary, flat_dictionary):
    for key, value in dictionary.items():
      if not isinstance(value, dict):
        if not initial_key or initial_key == "":
          flat_dictionary[key] = value
        else:
          flat_dictionary[".".join([initial_key, key])] = value

      else:
        if not initial_key or initial_key == "":
          flatten_dict_top_down(key, value, flat_dictionary)
        else:
          flatten_dict_top_down(".".join([initial_key, key]), value, flat_dictionary)

# The logic in this one becomes very complex
# See input:  {"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}
def flatten_dictionary_recursive_bottom_up(dictionary):
  result = {}

  # Iterate through each child within the dictionary
  for key, value in dictionary.items():
    # If the child is not a dictionary, we can return it without flattening it
    if not isinstance(value, dict):
      result[key] = value
  
    # Otherwise, we should iterate through each child...
    else:
      for child_key, child_value in value.items():
        key_to_add = ""
        if key and child_key:
          key_to_add = ".".join([key, child_key])
        elif child_key == "":
          key_to_add = key
        else:
          key_to_add = child_key

        if not isinstance(child_value, dict):
          result[key_to_add] = child_value
        else:
          for flat_key, flat_value in flatten_dictionary(child_value).items():
            result[".".join([key_to_add, flat_key])] = flat_value
            
  return result

# Utilities and Testing
def print_dict(d, curr_depth = 0):
  left_padding = " " * curr_depth * 2
  for key, value in d.items():
    if not isinstance(value, dict):
      print(left_padding + key + ":" + str(value))
    if isinstance(value, dict):
      print(left_padding + key + ":")
      print_dict(value, curr_depth + 1)

def test_dict(d):
  
  print("\n\nInput:")
  print_dict(d)
  print("\nOutput: Flatten Recursive")
  print_dict(flatten_dictionary(d))
  print("\nOutput: Flatten Recursive (Carry Prefix)")
  print_dict(flatten_dict_with_prefix(d, ""))

d = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
test_dict({"A": 1})
test_dict({"A": 1, "B": 2})
test_dict({"A": 1, "B": {"C": 3, "": 4}})
test_dict(d)

d = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : { "f": 1}
                    }
                }
            }
        }
test_dict(d)


"""
# Problem
## Examples

### Input
{
"A": "1"
}
### Output
{
"A": "1"
}

### Input
{
"A": "1"
"B": {
  "A": 2
}
}

### Output
{
"A": "1"
"BA": 2
}


## Approaches
### Recursive Bottom-Up Approach

flatten(dict, prefix):

  result = {}
  
  for key, value in dict:

    if value is not a dict
      if key == ""
        prefix = prefix minus the trailing "."
       
        
      result[prefix] = value
      

    if the value is a dict
      result[key] = flatten(value, prefix + '.' + key)
      
https://link.excalidraw.com/l/ATbTqvQ19d9/6Mc8ozf3K2J
      







"""