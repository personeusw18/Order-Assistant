# Order Assistant

## **Introduction**
Drive-through ordering is an inherently complex process that is prone to confusion and error when relaying order information from customer to employee. Additionally, drive-through ordering is a highly unscalable process that requires one employee to take one order at a time instead of helping in-store customers. Order Assistant aims to remove the complexity and confusion from the drive-through ordering process. By using natural language processing, Order Assistant can increase order accuracy and remove the need to have a dedicated employee taking drive-through orders. 

## **Tech Stack**
| Component | Framework/Language |
|:-----------|:-----------|
| Frontend | React |
| Backend | Python FastAPI |
| Database Technology | GCP Postgres Instance |
| NLP & Text Processing | GCP API's | 

## **API Setup**
Order Assistant uses Python's Fast API. This selection allows us to quickly generate SwaggerUI pages for API endpoint testing. The API is quick and easy to set up if you have pipenv installed. 

```bash
cd api 
pipenv install 
pipenv shell
uvicorn main:app --reload
```

## **Active Endpoints**
1. ```POST /menu```
    - Creates menu object and stores in database instance.
2. ```More endpoints coming soon```

<br />

## **Setup Documentation & Procedure**
<br />

### **Google Cloud Platform Connections**

Order Assistant uses 3 major GCP libaries/APIs.
1. Cloud SQL Admin API
2. Cloud Speech-to-text API
3. Cloud Natural Language API

The Cloud SQL Admin API allows us to create and access the Cloud SQL instance of Postgres. The Cloud Speech-to-text API is used to convert incoming MP3 files into parsable text on the server. Finally, the Cloud Natural Language API deconstructs the provided text into grammatical constructs which simplifies the process of converting this text into a restaurant order. 

### **Database Setup Information**

A PostgreSQL instance was issued from GCP to serve as the main persistent datastore for this repository. The database will contain 5 major tables: Restaurants, Menus, Items, Addons, and Identifiers. These tables are currently a work in progress but are created through the GCP developer console. Our API connects to the SQL cloud instance via the machine's IP address, and the standard Postgres port number. The connection uses pg8000 drivers. A database diagram to be included in this read me is currently a work in progress.
