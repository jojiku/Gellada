<div id="top"></div>

<!-- PROJECT LOGO -->
![image](https://github.com/jojiku/Gellada/assets/56271473/1e8caa6b-5cff-493d-b195-af3f6ce7b53f)




<br />
<div align="center">

<h3 align="center">Gellada</h3>
   <p align="center">
    Chit chat bot based on llama3 + postgreSQL
  </p>
</div>
Working Gellada is here: https://t.me/helper_111bot

### Installation

1. Clone the repo
   ```
   git clone https://github.com/jojiku/Gellada.git
   ```
2. Install the required packages:
   ```
   cd Gellada
   pip install -r requirements.txt
   ```
3. Rename example_env.txt to `.env` file in root directory and change only telegram token:
    ```
    TELEGRAM_TOKEN "YOUR_TOKEN"
    ```
    Change telegram token in \src\utils\config.py as well:
    ```
    TELEGRAM_PARAMS = {
    "telegram_token": "YOUR_TOKEN"}
    ```
   
4. Run main.py:
   ```
   python main.py
   ```
 Docker-compose and docker dont really work, use only the above sequence
