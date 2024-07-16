# Chatbot Project

This project implements a chatbot using Rasa and Docker.

## Endpoint

Use the following endpoint to interact with the chatbot:

**Endpoint URL:** `http://localhost:5005/webhooks/rest/webhook`

### Example Test

You can test the endpoint using `curl`:

```bash
curl --request POST \
     --url http://localhost:5005/webhooks/rest/webhook \
     --header 'Content-Type: application/json' \
     --data '{
            "sender": "test_user",
            "message": "Hi there!",
            "metadata": {}
          }'
```

## Simple Steps to Run the Project Using Docker

Follow these steps to run the chatbot project using Docker:

1. **Install Docker:**

   - If Docker is not installed, follow the instructions [here](https://docs.docker.com/engine/install/) to install Docker on your machine.

2. **Clone the Project:**

   ```bash
   git clone git@github.com:findAkash/Chatbot-alproj.git
   cd Chatbot-alproj
   ```

3. **Start Docker Containers:**

   ```bash
   docker-compose up -d
   ```

   This command starts the Docker containers defined in `docker-compose.yml`. It might take some time initially.

4. **Verify Running Containers:**
   To verify that the containers are running, use:

   ```bash
   docker ps
   ```

   You should see two containers running: one for the Rasa server and another for the action server.

5. **Access the Chatbot Endpoint:**
   - **Endpoint:** `http://localhost:5005/webhooks/rest/webhook`
   - **Method:** POST
   - **Body:**
     ```json
     {
       "sender": "test_user",
       "message": "Hi there!"
     }
     ```

---

### Additional Notes:

- Customize the `sender` and `message` fields in the example JSON payload according to your testing needs.
- Ensure that Docker is configured correctly and has access to necessary resources (like ports and volumes) as per your `docker-compose.yml` setup.

This structured `README.md` should provide clear instructions on how to interact with your chatbot endpoint and how to get the project up and running using Docker. Adjust any paths or specific details according to your project's actual setup.
