# Use the official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV STREAMLIT_HOME /app
WORKDIR $STREAMLIT_HOME

# Install dependencies first to leverage Docker cache
# Copy only requirements.txt first
COPY requirements.txt .

# Install Python dependencies (Streamlit and any other dependencies)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app files into the container
COPY app.py .
COPY unit1/ ./unit1/
COPY unit2/ ./unit2/
COPY unit3/ ./unit3/

# Copy the Streamlit configuration file
COPY .streamlit /app/.streamlit

# Expose the port that Streamlit uses
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]