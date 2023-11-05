
import replicate

# Initialize an empty list to store the input lines
# Initialize an empty string to store the input
multiline_input = ""

# Use a loop to read each line of input
while True:
    line = input("Enter a line of text (or press Enter to finish): ")

    # Check if the user pressed Enter (an empty line)
    if not line:
        break

    # Concatenate the line to the existing input
    multiline_input += line + "\n"

# Remove the trailing newline character
multiline_input = multiline_input.rstrip()

output_file_path = "output.txt"

output = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={"prompt": "Create flashcards based on the following text: " + multiline_input}
)
# The meta/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
with open(output_file_path, "w") as output_file:
    # Iterate over the output and write it to the file
    for item in output:
        output_file.write(item)

print(f"Output saved to {output_file_path}")

