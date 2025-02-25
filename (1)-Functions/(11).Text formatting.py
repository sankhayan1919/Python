def format_name(first_name,last_name):
  formatted_first_name=first_name.lower()
  formatted_last_name=last_name.lower()
  return(f"Formatted name is: {formatted_first_name} {formatted_last_name}")
formatted_first_name=input("enter:")
formatted_last_name=input("enter:")
if formatted_first_name=="" or formatted_last_name=="":
  print("none")
else:
  print(format_name(formatted_first_name, formatted_last_name))