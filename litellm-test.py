from litellm import completion

user_input = None

while user_input != "quit":
    user_input = input("\nEnter your question or 'quit' to exit: ")
    messages = [{"content": user_input, "role": "user"}]

    response = completion(model="gpt-3.5-turbo", messages=messages)
#    print(response)

    resp_str = str(response.choices)

    content_start = resp_str.find("content='") + len("content='")
    content_end = resp_str.find("', role=")
    content = resp_str[content_start:content_end]

    print("\n" + content + "\n", sep='\n')

print("Goodbye!")
