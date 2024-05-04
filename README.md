<div id="top"></div>

<!-- PROJECT LOGO and HEADER -->
<div style="overflow: hidden;">
  <img src="https://github.com/jojiku/Gellada/assets/56271473/f7ed681a-5302-4bd1-a567-3a23687c9745" alt="Project Logo" style="float: right; margin-left: 20px; margin-bottom: 10px; width: 100px; height: auto;">
  <h1 align="center"> 🦊 Gellada </h1>
  <p align="center">
  ⚡ Chit chat bot based on llama3 + postgreSQL ⚡
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
