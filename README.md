<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Gelladae</h3>

  <p align="center">
    Chit chat bot
  </p>
</div>


### Installation

1. Clone the repo
   ```
   git clone -b randv_main https://github.com/pavviaz/itmo_pdl.git
   ```
2. Place SentenceTransformer checkpoint folder into `embedder/weights` directory, and example resume and vacancies CSVs into `api/init_data` (<a href="https://disk.yandex.ru/d/lujblP9pdXRiIw">our weights and data</a>, `ce_model.zip` is model folder, `resume_train_no_index.csv` and `vac_train_no_index.csv` are for resume and vacancies data respectively). Change path for model and data in config files if needed
3. Create `.env` file in root directory with following keys
    ```
    DB_NAME=<EXAMPLE_DB_NAME>
    DB_USER=<EXAMPLE_DB_USER>
    DB_PASSWORD=<EXAMPLE_DB_PASSWD>
    DB_HOST=<EXAMPLE_DB_HOST>
    DB_PORT=5044

    EMBEDDER_URL=http://embedder:5043
    ``` 
4. Build & run containers
   ```
   sudo docker-compose build
   sudo docker-compose up
   ```
Congratulations! Streamlit is now available at `http://localhost:8501/` and API endpoints are at `http://localhost:5041/docs`.
