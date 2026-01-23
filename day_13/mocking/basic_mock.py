import sys
import os
import sys

#1. Example - 1 - Standard Output Streaming
print("Hello World!")  # goes to sys.stdout, where sys.stdout is a file-like object
print(sys.stdout)      # shows what stdout actually is

#2. Example - 2 - Standard Output Streaming
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("output.txt", "w") as f:
    sys.stdout = f  # redirect all prints to the file
    print("This will go into output.txt")

# Reset stdout to console
sys.stdout = sys.__stdout__
print("This goes to the terminal again")


#3. Example - 3 - Writing and Reading from StringIO
import io

buffer = io.StringIO()        # create an in-memory file
buffer.write("Hello World\n") # write to it
buffer.write("More text\n")

# Read what we wrote
contents = buffer.getvalue()
print(contents)


#4. Example - 4 - Using io.StringIO() & sys.stdout(for redirecting the prints to the in-memory file fake_output) to Capture Print Output
import io
import sys

# Create a fake output stream
fake_output = io.StringIO()

# Temporarily redirect sys.stdout
sys.stdout = fake_output

print("This will not go to the console")
print("It will go into StringIO")

# Get the printed text
captured = fake_output.getvalue()

# Reset stdout
sys.stdout = sys.__stdout__

print("Captured output was:")
print(captured)


