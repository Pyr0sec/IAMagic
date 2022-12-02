```

 ██▓ ▄▄▄       ███▄ ▄███▓ ▄▄▄        ▄████  ██▓ ▄████▄  
▓██▒▒████▄    ▓██▒▀█▀ ██▒▒████▄     ██▒ ▀█▒▓██▒▒██▀ ▀█  
▒██▒▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄  ▒██░▄▄▄░▒██▒▒▓█    ▄ 
░██░░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██ ░▓█  ██▓░██░▒▓▓▄ ▄██▒
░██░ ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒░▒▓███▀▒░██░▒ ▓███▀ ░
░▓   ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░ ░▒   ▒ ░▓  ░ ░▒ ▒  ░
 ▒ ░  ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░  ░   ░  ▒ ░  ░  ▒   
 ▒ ░  ░   ▒   ░      ░     ░   ▒   ░ ░   ░  ▒ ░░        
 ░        ░  ░       ░         ░  ░      ░  ░  ░ ░      
                                               ░        
```
IAMagic scans and enumerates AWS access credentials and displays information like all the permissions policies attached to the account, buckets, running instances etc.


Requirements
---
```
- Python 3.x
- awscli (credentials must be configured)
```


Installation
---
```
git clone https://github.com/Pyr0sec/IAMagic
cd IAMagic
pip install -r requirements.txt
```


Usage
---
```shell
(venv) C:\Users\puruj\Documents\git\IAMagic>python IAMagic.py -h                                 
usage: IAMagic.py [-h] [[-id ACCESS_KEY_ID] [-key SECRET_ACCESS_KEY] | [--profile PROFILE]] [--enumerate]

options:
  -h, --help            show this help message and exit
  -id ACCESS_KEY_ID, --access-key-id ACCESS_KEY_ID
                        Accepts AWS access key ID as an argument
  -key SECRET_ACCESS_KEY, --secret-access-key SECRET_ACCESS_KEY
                        Accepts AWS Secret access key as an argument
  --profile PROFILE     Used to specify an AWS profile on your system (like awscli), Uses default credentials if not specified any.
  --enumerate           Further enumerates the credentials by Checking    
```


Examples
---
```bash
python IAMagic.py --profile <aws-profile-here> --enumerate
python IAMagic.py -id <access-key> -key <secret-key> --enumerate
```


Screenshots
---
![Untitled (1)](https://user-images.githubusercontent.com/74669749/205364142-98d07cf6-7046-4104-bfac-f3cdac29bc6e.png)
![Untitled](https://user-images.githubusercontent.com/74669749/205365446-cb92c08b-aa60-4f16-9fa7-241b412c5a5b.png)
![2](https://user-images.githubusercontent.com/74669749/205368513-375b2fa6-7dc4-4c0e-9983-0da8805cdc72.png)

https://www.buymeacoffee.com/Pyrosec
