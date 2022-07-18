import requests


def io_bound_func():
    print('값을 입력해주세요')
    input_value = input()
    return int(input_value) + 100


def io_bound_func2():
    result = requests.get("https://google.com")
    return result


if __name__ == '__main__':
    for i in range(10):
        result = io_bound_func2()
    print(result)