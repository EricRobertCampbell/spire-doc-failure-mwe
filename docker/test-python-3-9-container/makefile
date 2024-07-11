# Define the target file
TARGET = table.docx

# Define the dependencies
DEPS = test.py requirements.txt Dockerfile

# Default target
all: $(TARGET)

# Build the target
$(TARGET): $(DEPS)
	# Remove all stopped containers
	# docker rm $$(docker ps -aq)
	
	# Build the Docker image
	docker build --no-cache -t 3.9-container .
	# Run the Docker container
	docker run --name 3.9-container 3.9-container
	# Copy the generated file from the container
	docker cp 3.9-container:/usr/src/app/$(TARGET) .

# Clean target to remove the generated file
clean:
	rm -f $(TARGET)

