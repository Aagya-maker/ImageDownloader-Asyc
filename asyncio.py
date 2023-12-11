import requests
import asyncio

async def logo():
    url = 'https://www.facebook.com/favicon.ico'
    response = requests.get(url)
    open('facebook1.ico', 'wb').write(response.content)
    

async def logo1():
    url = 'https://www.facebook.com/favicon.ico'
    response = requests.get(url)
    open('facebook2.ico', 'wb').write(response.content)
    

async def main():
    L = await asyncio.gather(
        logo(),
        logo1(),
    )

    print(L)

if __name__ == "__main__":
    asyncio.run(main())
