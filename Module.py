def function():
    print("This is a function in module.py")


if __name__ == "__main__":
    print('module.py is being run directly')
else:
    print('module.py is being imported')
