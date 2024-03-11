from litellm import completion

user_input = None

while user_input != "quit":
    user_input = input("\nEnter your question or 'quit' to exit: ")
    messages = [{"content": user_input, "role": "user"}]

    response = completion(model="gpt-3.5-turbo", messages=messages)
#    print(response)

    content = response.choices[0].message.content


    print("\n" + content + "\n", sep='\n')

print("Goodbye!")
