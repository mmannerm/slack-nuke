# slack-nuke

## Usage

1. Clone the Git repository
2. `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
3. Create an app in slack.
   * https://github.com/sgratzl/slack-cleaner#configuring-app
   * https://github.com/sgratzl/slack-cleaner#permission-scopes-needed
4. Create a file `config.yml` with following contents:
    ```
    ---
    tokens:
      - <insert token here for slack-api> 
    ```
5. `./nuke.py`
