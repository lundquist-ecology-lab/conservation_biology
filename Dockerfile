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
COPY common/ ./common/
COPY unit1/ ./unit1/
COPY unit2/ ./unit2/
COPY unit3/ ./unit3/
COPY unit4/ ./unit4/
COPY unit5/ ./unit5/
COPY unit6/ ./unit6/
COPY data_analysis_activity/ ./data_analysis_activity/
COPY unit7/ ./unit7/
COPY unit8/ ./unit8/
COPY unit9/ ./unit9/

# Copy the Streamlit configuration file
COPY .streamlit /app/.streamlit
COPY assets /app/assets

# Expose the port that Streamlit uses
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
