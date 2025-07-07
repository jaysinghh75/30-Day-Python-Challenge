# Challenge Day 25

from pydantic import BaseModel, EmailStr, field_validator, ValidationError

# ✅ Define a user model with automatic validation
class UserD(BaseModel):
    name: str                   # Name must be a string
    email: EmailStr             # Email must be a valid email format
    age: int                    # Age must be an integer

    # ✅ Custom validator to check age range (18 to 100)
    @field_validator('age')
    @classmethod
    def validator_age(cls, value):
        if value < 18 or value > 100:
            raise ValueError('The age should be between 18 and 100')
        return value

    # ✅ Method to show user details
    def show(self):
        print(f"Name: {self.name}| Email: {self.email}| Age: {self.age}")

# 🌟 Get user input from console
print("Enter Your Details below")
user_name = input("Enter your name: ")
user_email = input("Enter your email: ")
user_age = input("Enter your age: ")

try:
    # 🛠️ Create user object (this will auto-validate all inputs)
    u = UserD(name=user_name, email=user_email, age=user_age)
    u.show()

except ValidationError as e:
    # ❌ If any validation fails, show clean error messages
    print("\n❌ Validation Error(s):")
    for err in e.errors():
        field = err['loc'][0]         # Field name (like 'email' or 'age')
        msg = err['msg']              # Description of the problem
        input_val = err.get('input')  # The actual value that caused the error
        print(f"- {field}: '{input_val}' → {msg}")
