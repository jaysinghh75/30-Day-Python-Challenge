# Challenge Day 17

# Enforce a naming convention (CamelCase) using a metaclass

# ✅ Custom metaclass to enforce naming rules for class names
class EnforceNamingConvention(type):
    def __new__(cls, class_name, bases, attrs):
        # Check if class name does NOT start with an uppercase letter or contains underscores
        if not class_name[0].isupper() or "_" in class_name:
            raise ValueError(f"Class name {class_name} should be in CamelCase")
        else:
            print(f"Class {class_name} is created!!")
        
        # If valid, create the class using the parent 'type'
        return super().__new__(cls, class_name, bases, attrs)

# ✅ This class name is in CamelCase – valid
class HelloWorld(metaclass=EnforceNamingConvention):
    pass

# ❌ Invalid class name – starts with lowercase
try:
    class helloWorld(metaclass=EnforceNamingConvention):
        pass
except Exception as e:
    print(e)  # Output: Class name helloWorld should be in CamelCase

# ❌ Invalid class name – contains an underscore
try:
    class Hello_World(metaclass=EnforceNamingConvention):
        pass
except Exception as e:
    print(e)  # Output: Class name Hello_World should be in CamelCase 
