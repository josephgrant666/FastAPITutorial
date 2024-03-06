# Password Hashing

# Install the passlib and bcrypt library: pip install passlib[bcrypt]

from passlib.context import CryptContext

pwd_Context = CryptContext(schemes=["bcyrpt"], deprecated="auto")