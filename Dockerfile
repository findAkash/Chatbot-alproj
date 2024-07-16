# Use the official Rasa image
FROM rasa/rasa:3.6.2-full

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary
COPY requirements.txt ./

# Install extra requirements for actions code, if necessary
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Copy actions folder to working directory
COPY ./actions /app/actions

# Copy your pre-trained model into the Docker image
COPY ./models /app/models

# Copy custom models if necessary (uncomment next line)
# COPY ./custom_models /app/custom_models

# By best practices, don't run the code with root user
USER 1001
