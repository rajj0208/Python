import multiprocessing
import multiprocessing.process
import requests

def downloadPhoto(url, name):
    print(f"Started downloading {name}")
    respose = requests.get(url)
    open(f"C:/Users/LENOVO/Desktop/python/myphoto/photo{name}.jpg", "wb").write(respose.content)
    print(f"Finsish Downloading {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []

# for i in range(5):
#     downloadPhoto(url, i)

    for i in range(10):
        p = multiprocessing.Process(target=downloadPhoto, args=[url, i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()
