import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class LoginRequest:
    login_name: Optional[str] = None
    login_password: Optional[str] = None
    login: Optional[str] = None