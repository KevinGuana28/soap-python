Here is the `README.md` file in English:

```markdown
# Instructions to Run the Flask SOAP Server

This project sets up a simple SOAP server using Flask, with Cross-Origin Resource Sharing (CORS) enabled.

## Prerequisites

- Python must be installed on your machine. You can download it from [here](https://www.python.org/downloads).

## Install the Required Dependencies

Before running the server, you need to install the necessary dependencies.

1. **Install the Flask-CORS package** to enable CORS in your Flask server:

   ```bash
   pip install Flask-CORS
   ```

2. **Install Flask and lxml** libraries, which are required to run the server:

   ```bash
   pip install Flask lxml
   ```

## Run the Server

1. **Ensure the `soap_server.py` file is in your project directory.**

2. **Run the server** by executing the following command in your terminal or command prompt:

   ```bash
   python soap_server.py
   ```

   This will start the SOAP server on your local machine.

## Expected Outcome

Once the server is running:

1. Open your web browser.
2. Click the "Send" button.
3. You should see the message "Hello World" as the server's response.

## Notes

- This server is for local testing and development purposes.
- Make sure there are no other applications using the same port that the server will use.
- If you face any issues with CORS, ensure the Flask-CORS package was installed and correctly configured.
```

This `README.md` gives instructions on how to set up and run a SOAP server using Flask in English. Let me know if you need any further adjustments!