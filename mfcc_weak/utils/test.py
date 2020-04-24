import os

def run():
    files = [f for f in os.listdir('./')]
    print(files)

if __name__ == '__main__':
    run()