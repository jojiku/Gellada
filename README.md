<div id="top"></div>

<!-- PROJECT LOGO -->
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
 
