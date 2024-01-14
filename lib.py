def process_response(response):
  """
  Simple processing of a requests response 
  """

  print(f"Status code: {response.status_code}")
  
  if response.status_code == 200:
    print("Success!")
  else:
    print("Error!")

  # Do some processing on response.text 
  processed_text = response.text.upper()

  return processed_text