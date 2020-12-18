
"""
Generate Fernet keys to use in Airflow with "crypto" module

More info: https://airflow.readthedocs.io/en/stable/howto/secure-connections.html

Depends on "cryptography" module

  pip install cryptography

"""

from cryptography.fernet import Fernet
fernet_key = Fernet.generate_key()
print(fernet_key.decode()) # your fernet_key, keep it in secured place!
