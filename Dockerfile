FROM python:latest

# Attributes for MetaData
LABEL authors = "Nicola Ricciardi"

WORKDIR /Docker_Directory
COPY . .

# This command create a volume mapped to some folder on the Host machine (we don't know where)
# VOLUME ["/Docker_Directory/Storage"]

# Set the PYTHONPATH to include the "Docker_Directory" directory
ENV PYTHONPATH "${PYTHONPATH}:/Docker_Directory"

# Ensure the storage directory exists
RUN mkdir -p /Docker_Directory/Storage

CMD ["python", "./Main_Code/main.py"]