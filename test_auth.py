from auth import get_password_hash, verify_password

try:
    print("Testing string password...")
    pwd = "password123"
    hashed = get_password_hash(pwd)
    print(f"Hashed: {hashed}")
    valid = verify_password(pwd, hashed)
    print(f"Verified: {valid}")

    print("Testing integer-like string password...")
    pwd_num = "123456"
    hashed_num = get_password_hash(pwd_num)
    print(f"Hashed num: {hashed_num}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
